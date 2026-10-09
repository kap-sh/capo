"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#ApiGatewayV2``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_apigatewayv2._auth._signers
import capo_apigatewayv2._auth._sigv4
from capo_apigatewayv2._auth._identity import Credentials
from capo_apigatewayv2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_apigatewayv2._auth._zapros_handler import AuthMiddleware
from capo_apigatewayv2._pagination import resolve_path as _resolve_path
from capo_apigatewayv2._services._aws_config import aws_config
from capo_apigatewayv2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__boolean
    import capo_apigatewayv2.types.__list_of__string
    import capo_apigatewayv2.types.__list_of__string_min20_max2048
    import capo_apigatewayv2.types.__list_of_routing_rule_action
    import capo_apigatewayv2.types.__list_of_routing_rule_condition
    import capo_apigatewayv2.types.__string
    import capo_apigatewayv2.types.__string_min0_max255
    import capo_apigatewayv2.types.__string_min0_max1024
    import capo_apigatewayv2.types.__string_min0_max1092
    import capo_apigatewayv2.types.__string_min1_max255
    import capo_apigatewayv2.types.__string_min1_max307200
    import capo_apigatewayv2.types.access_log_settings
    import capo_apigatewayv2.types.arn
    import capo_apigatewayv2.types.authorization
    import capo_apigatewayv2.types.authorization_scopes
    import capo_apigatewayv2.types.authorization_type
    import capo_apigatewayv2.types.authorizer_type
    import capo_apigatewayv2.types.connection_type
    import capo_apigatewayv2.types.content_handling_strategy
    import capo_apigatewayv2.types.cors
    import capo_apigatewayv2.types.create_api_mapping_request
    import capo_apigatewayv2.types.create_api_mapping_response
    import capo_apigatewayv2.types.create_api_request
    import capo_apigatewayv2.types.create_api_response
    import capo_apigatewayv2.types.create_authorizer_request
    import capo_apigatewayv2.types.create_authorizer_response
    import capo_apigatewayv2.types.create_deployment_request
    import capo_apigatewayv2.types.create_deployment_response
    import capo_apigatewayv2.types.create_domain_name_request
    import capo_apigatewayv2.types.create_domain_name_response
    import capo_apigatewayv2.types.create_integration_request
    import capo_apigatewayv2.types.create_integration_response_request
    import capo_apigatewayv2.types.create_integration_response_response
    import capo_apigatewayv2.types.create_integration_result
    import capo_apigatewayv2.types.create_model_request
    import capo_apigatewayv2.types.create_model_response
    import capo_apigatewayv2.types.create_portal_product_request
    import capo_apigatewayv2.types.create_portal_product_response
    import capo_apigatewayv2.types.create_portal_request
    import capo_apigatewayv2.types.create_portal_response
    import capo_apigatewayv2.types.create_product_page_request
    import capo_apigatewayv2.types.create_product_page_response
    import capo_apigatewayv2.types.create_product_rest_endpoint_page_request
    import capo_apigatewayv2.types.create_product_rest_endpoint_page_response
    import capo_apigatewayv2.types.create_route_request
    import capo_apigatewayv2.types.create_route_response_request
    import capo_apigatewayv2.types.create_route_response_response
    import capo_apigatewayv2.types.create_route_result
    import capo_apigatewayv2.types.create_routing_rule_request
    import capo_apigatewayv2.types.create_routing_rule_response
    import capo_apigatewayv2.types.create_stage_request
    import capo_apigatewayv2.types.create_stage_response
    import capo_apigatewayv2.types.create_vpc_link_request
    import capo_apigatewayv2.types.create_vpc_link_response
    import capo_apigatewayv2.types.delete_access_log_settings_request
    import capo_apigatewayv2.types.delete_api_mapping_request
    import capo_apigatewayv2.types.delete_api_request
    import capo_apigatewayv2.types.delete_authorizer_request
    import capo_apigatewayv2.types.delete_cors_configuration_request
    import capo_apigatewayv2.types.delete_deployment_request
    import capo_apigatewayv2.types.delete_domain_name_request
    import capo_apigatewayv2.types.delete_integration_request
    import capo_apigatewayv2.types.delete_integration_response_request
    import capo_apigatewayv2.types.delete_model_request
    import capo_apigatewayv2.types.delete_portal_product_request
    import capo_apigatewayv2.types.delete_portal_product_sharing_policy_request
    import capo_apigatewayv2.types.delete_portal_request
    import capo_apigatewayv2.types.delete_product_page_request
    import capo_apigatewayv2.types.delete_product_rest_endpoint_page_request
    import capo_apigatewayv2.types.delete_route_request
    import capo_apigatewayv2.types.delete_route_request_parameter_request
    import capo_apigatewayv2.types.delete_route_response_request
    import capo_apigatewayv2.types.delete_route_settings_request
    import capo_apigatewayv2.types.delete_routing_rule_request
    import capo_apigatewayv2.types.delete_stage_request
    import capo_apigatewayv2.types.delete_vpc_link_request
    import capo_apigatewayv2.types.delete_vpc_link_response
    import capo_apigatewayv2.types.disable_portal_request
    import capo_apigatewayv2.types.display_content
    import capo_apigatewayv2.types.display_order
    import capo_apigatewayv2.types.domain_name_configurations
    import capo_apigatewayv2.types.endpoint_configuration_request
    import capo_apigatewayv2.types.endpoint_display_content
    import capo_apigatewayv2.types.export_api_request
    import capo_apigatewayv2.types.export_api_response
    import capo_apigatewayv2.types.get_api_mapping_request
    import capo_apigatewayv2.types.get_api_mapping_response
    import capo_apigatewayv2.types.get_api_mappings_request
    import capo_apigatewayv2.types.get_api_mappings_response
    import capo_apigatewayv2.types.get_api_request
    import capo_apigatewayv2.types.get_api_response
    import capo_apigatewayv2.types.get_apis_request
    import capo_apigatewayv2.types.get_apis_response
    import capo_apigatewayv2.types.get_authorizer_request
    import capo_apigatewayv2.types.get_authorizer_response
    import capo_apigatewayv2.types.get_authorizers_request
    import capo_apigatewayv2.types.get_authorizers_response
    import capo_apigatewayv2.types.get_deployment_request
    import capo_apigatewayv2.types.get_deployment_response
    import capo_apigatewayv2.types.get_deployments_request
    import capo_apigatewayv2.types.get_deployments_response
    import capo_apigatewayv2.types.get_domain_name_request
    import capo_apigatewayv2.types.get_domain_name_response
    import capo_apigatewayv2.types.get_domain_names_request
    import capo_apigatewayv2.types.get_domain_names_response
    import capo_apigatewayv2.types.get_integration_request
    import capo_apigatewayv2.types.get_integration_response_request
    import capo_apigatewayv2.types.get_integration_response_response
    import capo_apigatewayv2.types.get_integration_responses_request
    import capo_apigatewayv2.types.get_integration_responses_response
    import capo_apigatewayv2.types.get_integration_result
    import capo_apigatewayv2.types.get_integrations_request
    import capo_apigatewayv2.types.get_integrations_response
    import capo_apigatewayv2.types.get_model_request
    import capo_apigatewayv2.types.get_model_response
    import capo_apigatewayv2.types.get_model_template_request
    import capo_apigatewayv2.types.get_model_template_response
    import capo_apigatewayv2.types.get_models_request
    import capo_apigatewayv2.types.get_models_response
    import capo_apigatewayv2.types.get_portal_product_request
    import capo_apigatewayv2.types.get_portal_product_response
    import capo_apigatewayv2.types.get_portal_product_sharing_policy_request
    import capo_apigatewayv2.types.get_portal_product_sharing_policy_response
    import capo_apigatewayv2.types.get_portal_request
    import capo_apigatewayv2.types.get_portal_response
    import capo_apigatewayv2.types.get_product_page_request
    import capo_apigatewayv2.types.get_product_page_response
    import capo_apigatewayv2.types.get_product_rest_endpoint_page_request
    import capo_apigatewayv2.types.get_product_rest_endpoint_page_response
    import capo_apigatewayv2.types.get_route_request
    import capo_apigatewayv2.types.get_route_response_request
    import capo_apigatewayv2.types.get_route_response_response
    import capo_apigatewayv2.types.get_route_responses_request
    import capo_apigatewayv2.types.get_route_responses_response
    import capo_apigatewayv2.types.get_route_result
    import capo_apigatewayv2.types.get_routes_request
    import capo_apigatewayv2.types.get_routes_response
    import capo_apigatewayv2.types.get_routing_rule_request
    import capo_apigatewayv2.types.get_routing_rule_response
    import capo_apigatewayv2.types.get_stage_request
    import capo_apigatewayv2.types.get_stage_response
    import capo_apigatewayv2.types.get_stages_request
    import capo_apigatewayv2.types.get_stages_response
    import capo_apigatewayv2.types.get_tags_request
    import capo_apigatewayv2.types.get_tags_response
    import capo_apigatewayv2.types.get_vpc_link_request
    import capo_apigatewayv2.types.get_vpc_link_response
    import capo_apigatewayv2.types.get_vpc_links_request
    import capo_apigatewayv2.types.get_vpc_links_response
    import capo_apigatewayv2.types.id
    import capo_apigatewayv2.types.identity_source_list
    import capo_apigatewayv2.types.import_api_request
    import capo_apigatewayv2.types.import_api_response
    import capo_apigatewayv2.types.integer_with_length_between0_and3600
    import capo_apigatewayv2.types.integer_with_length_between50_and30000
    import capo_apigatewayv2.types.integration_parameters
    import capo_apigatewayv2.types.integration_type
    import capo_apigatewayv2.types.ip_address_type
    import capo_apigatewayv2.types.jwt_configuration
    import capo_apigatewayv2.types.list_portal_products_request
    import capo_apigatewayv2.types.list_portal_products_response
    import capo_apigatewayv2.types.list_portals_request
    import capo_apigatewayv2.types.list_portals_response
    import capo_apigatewayv2.types.list_product_pages_request
    import capo_apigatewayv2.types.list_product_pages_response
    import capo_apigatewayv2.types.list_product_rest_endpoint_pages_request
    import capo_apigatewayv2.types.list_product_rest_endpoint_pages_response
    import capo_apigatewayv2.types.list_routing_rules_request
    import capo_apigatewayv2.types.list_routing_rules_response
    import capo_apigatewayv2.types.max_results
    import capo_apigatewayv2.types.mutual_tls_authentication_input
    import capo_apigatewayv2.types.passthrough_behavior
    import capo_apigatewayv2.types.portal_content
    import capo_apigatewayv2.types.preview_portal_request
    import capo_apigatewayv2.types.preview_portal_response
    import capo_apigatewayv2.types.protocol_type
    import capo_apigatewayv2.types.publish_portal_request
    import capo_apigatewayv2.types.publish_portal_response
    import capo_apigatewayv2.types.put_portal_product_sharing_policy_request
    import capo_apigatewayv2.types.put_portal_product_sharing_policy_response
    import capo_apigatewayv2.types.put_routing_rule_request
    import capo_apigatewayv2.types.put_routing_rule_response
    import capo_apigatewayv2.types.reimport_api_request
    import capo_apigatewayv2.types.reimport_api_response
    import capo_apigatewayv2.types.reset_authorizers_cache_request
    import capo_apigatewayv2.types.response_parameters
    import capo_apigatewayv2.types.rest_endpoint_identifier
    import capo_apigatewayv2.types.route_models
    import capo_apigatewayv2.types.route_parameters
    import capo_apigatewayv2.types.route_settings
    import capo_apigatewayv2.types.route_settings_map
    import capo_apigatewayv2.types.routing_mode
    import capo_apigatewayv2.types.routing_rule
    import capo_apigatewayv2.types.routing_rule_priority
    import capo_apigatewayv2.types.security_group_id_list
    import capo_apigatewayv2.types.selection_expression
    import capo_apigatewayv2.types.selection_key
    import capo_apigatewayv2.types.stage_variables_map
    import capo_apigatewayv2.types.string_with_length_between0_and32_k
    import capo_apigatewayv2.types.string_with_length_between0_and1024
    import capo_apigatewayv2.types.string_with_length_between1_and64
    import capo_apigatewayv2.types.string_with_length_between1_and128
    import capo_apigatewayv2.types.string_with_length_between1_and256
    import capo_apigatewayv2.types.string_with_length_between1_and512
    import capo_apigatewayv2.types.string_with_length_between1_and1024
    import capo_apigatewayv2.types.subnet_id_list
    import capo_apigatewayv2.types.tag_resource_request
    import capo_apigatewayv2.types.tag_resource_response
    import capo_apigatewayv2.types.tags
    import capo_apigatewayv2.types.template_map
    import capo_apigatewayv2.types.tls_config_input
    import capo_apigatewayv2.types.try_it_state
    import capo_apigatewayv2.types.untag_resource_request
    import capo_apigatewayv2.types.update_api_mapping_request
    import capo_apigatewayv2.types.update_api_mapping_response
    import capo_apigatewayv2.types.update_api_request
    import capo_apigatewayv2.types.update_api_response
    import capo_apigatewayv2.types.update_authorizer_request
    import capo_apigatewayv2.types.update_authorizer_response
    import capo_apigatewayv2.types.update_deployment_request
    import capo_apigatewayv2.types.update_deployment_response
    import capo_apigatewayv2.types.update_domain_name_request
    import capo_apigatewayv2.types.update_domain_name_response
    import capo_apigatewayv2.types.update_integration_request
    import capo_apigatewayv2.types.update_integration_response_request
    import capo_apigatewayv2.types.update_integration_response_response
    import capo_apigatewayv2.types.update_integration_result
    import capo_apigatewayv2.types.update_model_request
    import capo_apigatewayv2.types.update_model_response
    import capo_apigatewayv2.types.update_portal_product_request
    import capo_apigatewayv2.types.update_portal_product_response
    import capo_apigatewayv2.types.update_portal_request
    import capo_apigatewayv2.types.update_portal_response
    import capo_apigatewayv2.types.update_product_page_request
    import capo_apigatewayv2.types.update_product_page_response
    import capo_apigatewayv2.types.update_product_rest_endpoint_page_request
    import capo_apigatewayv2.types.update_product_rest_endpoint_page_response
    import capo_apigatewayv2.types.update_route_request
    import capo_apigatewayv2.types.update_route_response_request
    import capo_apigatewayv2.types.update_route_response_response
    import capo_apigatewayv2.types.update_route_result
    import capo_apigatewayv2.types.update_stage_request
    import capo_apigatewayv2.types.update_stage_response
    import capo_apigatewayv2.types.update_vpc_link_request
    import capo_apigatewayv2.types.update_vpc_link_response
    import capo_apigatewayv2.types.uri_with_length_between1_and2048


class ApiGatewayV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ApiGatewayV2Client:
    """A client for the ``ApiGatewayV2`` service.

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
        self._config = ApiGatewayV2ClientConfig(
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
        self, config_overrides: Optional[ApiGatewayV2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApiGatewayV2ClientConfig = config_overrides or {}
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

    def create_api(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        api_key_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        cors_configuration: Optional["capo_apigatewayv2.types.cors.Cors"] = None,
        credentials_arn: Optional["capo_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        disable_schema_validation: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        disable_execute_api_endpoint: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        ip_address_type: Optional[
            "capo_apigatewayv2.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        protocol_type: Optional[
            "capo_apigatewayv2.types.protocol_type.ProtocolType"
        ] = None,
        route_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
        target: Optional[
            "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        version: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_api_response.CreateApiResponse":
        """<p>Creates an Api resource.</p>

        Args:
            api_key_selection_expression: <p>An API key selection expression. Supported only for WebSocket APIs. See <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API Key Selection Expressions</a>.</p>
            cors_configuration: <p>A CORS configuration. Supported only for HTTP APIs. See <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html">Configuring CORS</a> for more information.</p>
            credentials_arn: <p>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null. Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.</p>
            description: <p>The description of the API.</p>
            disable_schema_validation: <p>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</p>
            disable_execute_api_endpoint: <p>Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>
            ip_address_type: <p>The IP address types that can invoke the API.</p>
            name: <p>The name of the API.</p>
            protocol_type: <p>The API protocol.</p>
            route_key: <p>This property is part of quick create. If you don't specify a routeKey, a default route of $default is created. The $default route acts as a catch-all for any request made to your API, for a particular stage. The $default route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.</p>
            route_selection_expression: <p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>
            target: <p>This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.</p>
            version: <p>A version identifier for the API.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_api_request.CreateApiRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_api_response.CreateApiResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_api.create_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_api_request.CreateApiRequest = {}
        if api_key_selection_expression is not None:
            input_["api_key_selection_expression"] = api_key_selection_expression
        if cors_configuration is not None:
            input_["cors_configuration"] = cors_configuration
        if credentials_arn is not None:
            input_["credentials_arn"] = credentials_arn
        if description is not None:
            input_["description"] = description
        if disable_schema_validation is not None:
            input_["disable_schema_validation"] = disable_schema_validation
        if disable_execute_api_endpoint is not None:
            input_["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if route_key is not None:
            input_["route_key"] = route_key
        if route_selection_expression is not None:
            input_["route_selection_expression"] = route_selection_expression
        if tags is not None:
            input_["tags"] = tags
        if target is not None:
            input_["target"] = target
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_api_mapping(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        api_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        api_mapping_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        stage: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_api_mapping_response.CreateApiMappingResponse":
        """<p>Creates an API mapping.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_mapping_key: The API mapping key.
            domain_name: <p>The domain name.</p>
            stage: <p>The API stage.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_api_mapping_request.CreateApiMappingRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_api_mapping_response.CreateApiMappingResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_api_mapping

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_api_mapping.create_api_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_api_mapping_request.CreateApiMappingRequest = {
            "domain_name": domain_name
        }
        if api_id is not None:
            input_["api_id"] = api_id
        if api_mapping_key is not None:
            input_["api_mapping_key"] = api_mapping_key
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_authorizer(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        authorizer_credentials_arn: Optional["capo_apigatewayv2.types.arn.Arn"] = None,
        authorizer_payload_format_version: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        authorizer_result_ttl_in_seconds: Optional[
            "capo_apigatewayv2.types.integer_with_length_between0_and3600.IntegerWithLengthBetween0And3600"
        ] = None,
        authorizer_type: Optional[
            "capo_apigatewayv2.types.authorizer_type.AuthorizerType"
        ] = None,
        authorizer_uri: Optional[
            "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        enable_simple_responses: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        identity_source: Optional[
            "capo_apigatewayv2.types.identity_source_list.IdentitySourceList"
        ] = None,
        identity_validation_expression: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        jwt_configuration: Optional[
            "capo_apigatewayv2.types.jwt_configuration.JWTConfiguration"
        ] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_authorizer_response.CreateAuthorizerResponse":
        """<p>Creates an Authorizer for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_credentials_arn: <p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter. Supported only for REQUEST authorizers.</p>
            authorizer_payload_format_version: <p>Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are 1.0 and 2.0. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a>.</p>
            authorizer_result_ttl_in_seconds: <p>The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.</p>
            authorizer_type: <p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>
            authorizer_uri: <p>The authorizer's Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:<replaceable>{account_id}</replaceable>:function:<replaceable>{lambda_function_name}</replaceable>/invocations. In general, the URI has this form: arn:aws:apigateway:<replaceable>{region}</replaceable>:lambda:path/<replaceable>{service_api}</replaceable> , where <replaceable></replaceable>{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.</p>
            enable_simple_responses: <p>Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a></p>
            identity_source: <p>The identity source for which authorization is requested.</p> <p>For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with $, for example, $request.header.Auth, $request.querystring.Name. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a>.</p> <p>For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example $request.header.Authorization.</p>
            identity_validation_expression: <p>This parameter is not used.</p>
            jwt_configuration: <p>Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.</p>
            name: <p>The name of the authorizer.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_authorizer_request.CreateAuthorizerRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_authorizer_response.CreateAuthorizerResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_authorizer

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_authorizer.create_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_authorizer_request.CreateAuthorizerRequest = {
            "api_id": api_id
        }
        if authorizer_credentials_arn is not None:
            input_["authorizer_credentials_arn"] = authorizer_credentials_arn
        if authorizer_payload_format_version is not None:
            input_["authorizer_payload_format_version"] = (
                authorizer_payload_format_version
            )
        if authorizer_result_ttl_in_seconds is not None:
            input_["authorizer_result_ttl_in_seconds"] = (
                authorizer_result_ttl_in_seconds
            )
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_uri is not None:
            input_["authorizer_uri"] = authorizer_uri
        if enable_simple_responses is not None:
            input_["enable_simple_responses"] = enable_simple_responses
        if identity_source is not None:
            input_["identity_source"] = identity_source
        if identity_validation_expression is not None:
            input_["identity_validation_expression"] = identity_validation_expression
        if jwt_configuration is not None:
            input_["jwt_configuration"] = jwt_configuration
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        stage_name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_deployment_response.CreateDeploymentResponse":
        """<p>Creates a Deployment for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            description: <p>The description for the deployment resource.</p>
            stage_name: <p>The name of the Stage resource for the Deployment resource to create.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_deployment_request.CreateDeploymentRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_deployment_response.CreateDeploymentResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_deployment

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_deployment_request.CreateDeploymentRequest = {
            "api_id": api_id
        }
        if description is not None:
            input_["description"] = description
        if stage_name is not None:
            input_["stage_name"] = stage_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain_name(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        domain_name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and512.StringWithLengthBetween1And512"
        ] = None,
        domain_name_configurations: Optional[
            "capo_apigatewayv2.types.domain_name_configurations.DomainNameConfigurations"
        ] = None,
        mutual_tls_authentication: Optional[
            "capo_apigatewayv2.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
        ] = None,
        routing_mode: Optional[
            "capo_apigatewayv2.types.routing_mode.RoutingMode"
        ] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
    ) -> "capo_apigatewayv2.types.create_domain_name_response.CreateDomainNameResponse":
        """<p>Creates a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_configurations: <p>The domain name configurations.</p>
            mutual_tls_authentication: <p>The mutual TLS authentication configuration for a custom domain name.</p>
            routing_mode: <p>The routing mode.</p>
            tags: <p>The collection of tags associated with a domain name.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_domain_name_request.CreateDomainNameRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_domain_name_response.CreateDomainNameResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_domain_name

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_domain_name.create_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_domain_name_request.CreateDomainNameRequest = {}
        if domain_name is not None:
            input_["domain_name"] = domain_name
        if domain_name_configurations is not None:
            input_["domain_name_configurations"] = domain_name_configurations
        if mutual_tls_authentication is not None:
            input_["mutual_tls_authentication"] = mutual_tls_authentication
        if routing_mode is not None:
            input_["routing_mode"] = routing_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_integration(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        connection_id: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and1024.StringWithLengthBetween1And1024"
        ] = None,
        connection_type: Optional[
            "capo_apigatewayv2.types.connection_type.ConnectionType"
        ] = None,
        content_handling_strategy: Optional[
            "capo_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        credentials_arn: Optional["capo_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        integration_method: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        integration_subtype: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        integration_type: Optional[
            "capo_apigatewayv2.types.integration_type.IntegrationType"
        ] = None,
        integration_uri: Optional[
            "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        passthrough_behavior: Optional[
            "capo_apigatewayv2.types.passthrough_behavior.PassthroughBehavior"
        ] = None,
        payload_format_version: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_parameters: Optional[
            "capo_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        request_templates: Optional[
            "capo_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        response_parameters: Optional[
            "capo_apigatewayv2.types.response_parameters.ResponseParameters"
        ] = None,
        template_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        timeout_in_millis: Optional[
            "capo_apigatewayv2.types.integer_with_length_between50_and30000.IntegerWithLengthBetween50And30000"
        ] = None,
        tls_config: Optional[
            "capo_apigatewayv2.types.tls_config_input.TlsConfigInput"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_integration_result.CreateIntegrationResult":
        """<p>Creates an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            connection_id: <p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>
            connection_type: <p>The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.</p>
            content_handling_strategy: <p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            credentials_arn: <p>Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.</p>
            description: <p>The description of the integration.</p>
            integration_method: <p>Specifies the integration's HTTP method type.</p>
            integration_subtype: <p>Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html">Integration subtype reference</a>.</p>
            integration_type: <p>The integration type of an integration. One of the following:</p> <p>AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.</p> <p>AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.</p> <p>HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.</p> <p>HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.</p> <p>MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.</p>
            integration_uri: <p>For a Lambda integration, specify the URI of a Lambda function.</p> <p>For an HTTP integration, specify a fully-qualified URL.</p> <p>For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html">DiscoverInstances</a>. For private integrations, all resources must be owned by the same AWS account.</p>
            passthrough_behavior: <p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.</p> <p>WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.</p> <p>NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.</p> <p>WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.</p>
            payload_format_version: <p>Specifies the format of the payload sent to an integration. Required for HTTP APIs. Supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html">Working with AWS Lambda proxy integrations for HTTP APIs</a>.</p>
            request_parameters: <p>For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.<replaceable>{location}</replaceable>.<replaceable>{name}</replaceable> , where <replaceable>{location}</replaceable> is querystring, path, or header; and <replaceable>{name}</replaceable> must be a valid and unique method request parameter name.</p> <p>For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html">Working with AWS service integrations for HTTP APIs</a>.</p> <p>For HTTP API integrations without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern &lt;action&gt;:&lt;header|querystring|path&gt;.&lt;location&gt; where action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html">Transforming API requests and responses</a>.</p>
            request_templates: <p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.</p>
            response_parameters: <p>Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match pattern &lt;action&gt;:&lt;header&gt;.&lt;location&gt; or overwrite.statuscode. The action can be append, overwrite or remove. The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html">Transforming API requests and responses</a>.</p>
            template_selection_expression: <p>The template selection expression for the integration.</p>
            timeout_in_millis: <p>Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.</p>
            tls_config: <p>The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_integration_request.CreateIntegrationRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_integration_result.CreateIntegrationResult"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_integration

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_integration.create_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_integration_request.CreateIntegrationRequest = {
            "api_id": api_id
        }
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if content_handling_strategy is not None:
            input_["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None:
            input_["credentials_arn"] = credentials_arn
        if description is not None:
            input_["description"] = description
        if integration_method is not None:
            input_["integration_method"] = integration_method
        if integration_subtype is not None:
            input_["integration_subtype"] = integration_subtype
        if integration_type is not None:
            input_["integration_type"] = integration_type
        if integration_uri is not None:
            input_["integration_uri"] = integration_uri
        if passthrough_behavior is not None:
            input_["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None:
            input_["payload_format_version"] = payload_format_version
        if request_parameters is not None:
            input_["request_parameters"] = request_parameters
        if request_templates is not None:
            input_["request_templates"] = request_templates
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if template_selection_expression is not None:
            input_["template_selection_expression"] = template_selection_expression
        if timeout_in_millis is not None:
            input_["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            input_["tls_config"] = tls_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_integration_response(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        content_handling_strategy: Optional[
            "capo_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        integration_response_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        response_parameters: Optional[
            "capo_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        response_templates: Optional[
            "capo_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        template_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_integration_response_response.CreateIntegrationResponseResponse":
        """<p>Creates an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_handling_strategy: <p>Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_key: <p>The integration response key.</p>
            response_parameters: <p>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.{name}, where {name} is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.{name} or integration.response.body.{JSON-expression}, where {name} is a valid and unique response header name and {JSON-expression} is a valid JSON expression without the $ prefix.</p>
            response_templates: <p>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>
            template_selection_expression: <p>The template selection expression for the integration response. Supported only for WebSocket APIs.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_integration_response_request.CreateIntegrationResponseRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_integration_response_response.CreateIntegrationResponseResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_integration_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_integration_response.create_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_integration_response_request.CreateIntegrationResponseRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
        }
        if content_handling_strategy is not None:
            input_["content_handling_strategy"] = content_handling_strategy
        if integration_response_key is not None:
            input_["integration_response_key"] = integration_response_key
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if response_templates is not None:
            input_["response_templates"] = response_templates
        if template_selection_expression is not None:
            input_["template_selection_expression"] = template_selection_expression

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_model(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        content_type: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and256.StringWithLengthBetween1And256"
        ] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        schema: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and32_k.StringWithLengthBetween0And32K"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_model_response.CreateModelResponse":
        """<p>Creates a Model for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_type: <p>The content-type for the model, for example, "application/json".</p>
            description: <p>The description of the model.</p>
            name: <p>The name of the model. Must be alphanumeric.</p>
            schema: <p>The schema for the model. For application/json models, this should be JSON schema draft 4 model.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_model_request.CreateModelRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_model_response.CreateModelResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_model

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_model.create_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_model_request.CreateModelRequest = {
            "api_id": api_id
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if schema is not None:
            input_["schema"] = schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_portal(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        authorization: Optional[
            "capo_apigatewayv2.types.authorization.Authorization"
        ] = None,
        endpoint_configuration: Optional[
            "capo_apigatewayv2.types.endpoint_configuration_request.EndpointConfigurationRequest"
        ] = None,
        included_portal_product_arns: Optional[
            "capo_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
        ] = None,
        logo_uri: Optional[
            "capo_apigatewayv2.types.__string_min0_max1092.__stringMin0Max1092"
        ] = None,
        portal_content: Optional[
            "capo_apigatewayv2.types.portal_content.PortalContent"
        ] = None,
        rum_app_monitor_name: Optional[
            "capo_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
        ] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
    ) -> "capo_apigatewayv2.types.create_portal_response.CreatePortalResponse":
        """<p>Creates a portal.</p>

        Args:
            authorization: <p>The authentication configuration for the portal.</p>
            endpoint_configuration: <p>The domain configuration for the portal. Use a default domain provided by API Gateway or provide a fully-qualified domain name that you own.</p>
            included_portal_product_arns: <p>The ARNs of the portal products included in the portal.</p>
            logo_uri: <p>The URI for the portal logo image that is displayed in the portal header.</p>
            portal_content: <p>The content of the portal.</p>
            rum_app_monitor_name: <p>The name of the Amazon CloudWatch RUM app monitor for the portal.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_portal_request.CreatePortalRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_portal_response.CreatePortalResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_portal.create_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_portal_request.CreatePortalRequest = {}
        if authorization is not None:
            input_["authorization"] = authorization
        if endpoint_configuration is not None:
            input_["endpoint_configuration"] = endpoint_configuration
        if included_portal_product_arns is not None:
            input_["included_portal_product_arns"] = included_portal_product_arns
        if logo_uri is not None:
            input_["logo_uri"] = logo_uri
        if portal_content is not None:
            input_["portal_content"] = portal_content
        if rum_app_monitor_name is not None:
            input_["rum_app_monitor_name"] = rum_app_monitor_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_portal_product(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        description: Optional[
            "capo_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        display_name: Optional[
            "capo_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
        ] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
    ) -> "capo_apigatewayv2.types.create_portal_product_response.CreatePortalProductResponse":
        """<p>Creates a new portal product.</p>

        Args:
            description: <p>A description of the portal product.</p>
            display_name: <p>The name of the portal product as it appears in a published portal.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_portal_product_request.CreatePortalProductRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_portal_product_response.CreatePortalProductResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_portal_product

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_portal_product.create_portal_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_portal_product_request.CreatePortalProductRequest = {}
        if description is not None:
            input_["description"] = description
        if display_name is not None:
            input_["display_name"] = display_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_product_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "capo_apigatewayv2.types.display_content.DisplayContent"
        ] = None,
    ) -> (
        "capo_apigatewayv2.types.create_product_page_response.CreateProductPageResponse"
    ):
        """<p>Creates a new product page for a portal product.</p>

        Args:
            display_content: <p>The content of the product page.</p>
            portal_product_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_product_page_request.CreateProductPageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_product_page_response.CreateProductPageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_product_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_product_page.create_product_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_product_page_request.CreateProductPageRequest = {
            "portal_product_id": portal_product_id
        }
        if display_content is not None:
            input_["display_content"] = display_content

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_product_rest_endpoint_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "capo_apigatewayv2.types.endpoint_display_content.EndpointDisplayContent"
        ] = None,
        rest_endpoint_identifier: Optional[
            "capo_apigatewayv2.types.rest_endpoint_identifier.RestEndpointIdentifier"
        ] = None,
        try_it_state: Optional[
            "capo_apigatewayv2.types.try_it_state.TryItState"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_product_rest_endpoint_page_response.CreateProductRestEndpointPageResponse":
        """<p>Creates a product REST endpoint page for a portal product.</p>

        Args:
            display_content: <p>The content of the product REST endpoint page.</p>
            portal_product_id: <p>The portal product identifier.</p>
            rest_endpoint_identifier: <p>The REST endpoint identifier.</p>
            try_it_state: <p>The try it state of the product REST endpoint page.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_product_rest_endpoint_page_request.CreateProductRestEndpointPageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_product_rest_endpoint_page_response.CreateProductRestEndpointPageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_product_rest_endpoint_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_product_rest_endpoint_page.create_product_rest_endpoint_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_product_rest_endpoint_page_request.CreateProductRestEndpointPageRequest = {
            "portal_product_id": portal_product_id
        }
        if display_content is not None:
            input_["display_content"] = display_content
        if rest_endpoint_identifier is not None:
            input_["rest_endpoint_identifier"] = rest_endpoint_identifier
        if try_it_state is not None:
            input_["try_it_state"] = try_it_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_route(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        api_key_required: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        authorization_scopes: Optional[
            "capo_apigatewayv2.types.authorization_scopes.AuthorizationScopes"
        ] = None,
        authorization_type: Optional[
            "capo_apigatewayv2.types.authorization_type.AuthorizationType"
        ] = None,
        authorizer_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        model_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        operation_name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_models: Optional[
            "capo_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        request_parameters: Optional[
            "capo_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_response_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        target: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_route_result.CreateRouteResult":
        """<p>Creates a Route for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_key_required: <p>Specifies whether an API key is required for the route. Supported only for WebSocket APIs.</p>
            authorization_scopes: <p>The authorization scopes supported by this route.</p>
            authorization_type: <p>The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer.</p>
            authorizer_id: <p>The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.</p>
            model_selection_expression: <p>The model selection expression for the route. Supported only for WebSocket APIs.</p>
            operation_name: <p>The operation name for the route.</p>
            request_models: <p>The request models for the route. Supported only for WebSocket APIs.</p>
            request_parameters: <p>The request parameters for the route. Supported only for WebSocket APIs.</p>
            route_key: <p>The route key for the route.</p>
            route_response_selection_expression: <p>The route response selection expression for the route. Supported only for WebSocket APIs.</p>
            target: <p>The target for the route.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_route_request.CreateRouteRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_route_result.CreateRouteResult"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_route

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_route.create_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_route_request.CreateRouteRequest = {
            "api_id": api_id
        }
        if api_key_required is not None:
            input_["api_key_required"] = api_key_required
        if authorization_scopes is not None:
            input_["authorization_scopes"] = authorization_scopes
        if authorization_type is not None:
            input_["authorization_type"] = authorization_type
        if authorizer_id is not None:
            input_["authorizer_id"] = authorizer_id
        if model_selection_expression is not None:
            input_["model_selection_expression"] = model_selection_expression
        if operation_name is not None:
            input_["operation_name"] = operation_name
        if request_models is not None:
            input_["request_models"] = request_models
        if request_parameters is not None:
            input_["request_parameters"] = request_parameters
        if route_key is not None:
            input_["route_key"] = route_key
        if route_response_selection_expression is not None:
            input_["route_response_selection_expression"] = (
                route_response_selection_expression
            )
        if target is not None:
            input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_route_response(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        model_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        response_models: Optional[
            "capo_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        response_parameters: Optional[
            "capo_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_response_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
    ) -> "capo_apigatewayv2.types.create_route_response_response.CreateRouteResponseResponse":
        """<p>Creates a RouteResponse for a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_selection_expression: <p>The model selection expression for the route response. Supported only for WebSocket APIs.</p>
            response_models: <p>The response models for the route response.</p>
            response_parameters: <p>The route response parameters.</p>
            route_id: <p>The route ID.</p>
            route_response_key: <p>The route response key.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_route_response_request.CreateRouteResponseRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_route_response_response.CreateRouteResponseResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_route_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_route_response.create_route_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_route_response_request.CreateRouteResponseRequest = {
            "api_id": api_id,
            "route_id": route_id,
        }
        if model_selection_expression is not None:
            input_["model_selection_expression"] = model_selection_expression
        if response_models is not None:
            input_["response_models"] = response_models
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if route_response_key is not None:
            input_["route_response_key"] = route_response_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_routing_rule(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        actions: Optional[
            "capo_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction"
        ] = None,
        conditions: Optional[
            "capo_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition"
        ] = None,
        domain_name_id: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        priority: Optional[
            "capo_apigatewayv2.types.routing_rule_priority.RoutingRulePriority"
        ] = None,
    ) -> (
        "capo_apigatewayv2.types.create_routing_rule_response.CreateRoutingRuleResponse"
    ):
        """<p>Creates a RoutingRule.</p>

        Args:
            actions: <p>Represents a routing rule action. The only supported action is invokeApi.</p>
            conditions: <p>Represents a condition. Conditions can contain up to two matchHeaders conditions and one matchBasePaths conditions. API Gateway evaluates header conditions and base path conditions together. You can only use AND between header and base path conditions.</p>
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            priority: Represents the priority of the routing rule.

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_routing_rule_request.CreateRoutingRuleRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_routing_rule_response.CreateRoutingRuleResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_routing_rule

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_routing_rule.create_routing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_routing_rule_request.CreateRoutingRuleRequest = {
            "domain_name": domain_name
        }
        if actions is not None:
            input_["actions"] = actions
        if conditions is not None:
            input_["conditions"] = conditions
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if priority is not None:
            input_["priority"] = priority

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stage(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        access_log_settings: Optional[
            "capo_apigatewayv2.types.access_log_settings.AccessLogSettings"
        ] = None,
        auto_deploy: Optional["capo_apigatewayv2.types.__boolean.__boolean"] = None,
        client_certificate_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        default_route_settings: Optional[
            "capo_apigatewayv2.types.route_settings.RouteSettings"
        ] = None,
        deployment_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        route_settings: Optional[
            "capo_apigatewayv2.types.route_settings_map.RouteSettingsMap"
        ] = None,
        stage_name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        stage_variables: Optional[
            "capo_apigatewayv2.types.stage_variables_map.StageVariablesMap"
        ] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
    ) -> "capo_apigatewayv2.types.create_stage_response.CreateStageResponse":
        """<p>Creates a Stage for an API.</p>

        Args:
            access_log_settings: <p>Settings for logging access in this stage.</p>
            api_id: <p>The API identifier.</p>
            auto_deploy: <p>Specifies whether updates to an API automatically trigger a new deployment. The default value is false.</p>
            client_certificate_id: <p>The identifier of a client certificate for a Stage. Supported only for WebSocket APIs.</p>
            default_route_settings: <p>The default route settings for the stage.</p>
            deployment_id: <p>The deployment identifier of the API stage.</p>
            description: <p>The description for the API stage.</p>
            route_settings: <p>Route settings for the stage, by routeKey.</p>
            stage_name: <p>The name of the stage.</p>
            stage_variables: <p>A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&amp;=,]+.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_stage_request.CreateStageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_stage_response.CreateStageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_stage

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_stage.create_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_stage_request.CreateStageRequest = {
            "api_id": api_id
        }
        if access_log_settings is not None:
            input_["access_log_settings"] = access_log_settings
        if auto_deploy is not None:
            input_["auto_deploy"] = auto_deploy
        if client_certificate_id is not None:
            input_["client_certificate_id"] = client_certificate_id
        if default_route_settings is not None:
            input_["default_route_settings"] = default_route_settings
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if description is not None:
            input_["description"] = description
        if route_settings is not None:
            input_["route_settings"] = route_settings
        if stage_name is not None:
            input_["stage_name"] = stage_name
        if stage_variables is not None:
            input_["stage_variables"] = stage_variables
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_link(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        security_group_ids: Optional[
            "capo_apigatewayv2.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        subnet_ids: Optional[
            "capo_apigatewayv2.types.subnet_id_list.SubnetIdList"
        ] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
    ) -> "capo_apigatewayv2.types.create_vpc_link_response.CreateVpcLinkResponse":
        """<p>Creates a VPC link.</p>

        Args:
            name: <p>The name of the VPC link.</p>
            security_group_ids: <p>A list of security group IDs for the VPC link.</p>
            subnet_ids: <p>A list of subnet IDs to include in the VPC link.</p>
            tags: <p>A list of tags.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.create_vpc_link_request.CreateVpcLinkRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.create_vpc_link_response.CreateVpcLinkResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.create_vpc_link

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.create_vpc_link.create_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.create_vpc_link_request.CreateVpcLinkRequest = {}
        if name is not None:
            input_["name"] = name
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_access_log_settings(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        stage_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the AccessLogSettings for a Stage. To disable access logging for a Stage, delete its AccessLogSettings.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_access_log_settings_request.DeleteAccessLogSettingsRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_access_log_settings

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_access_log_settings.delete_access_log_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_access_log_settings_request.DeleteAccessLogSettingsRequest = {
            "api_id": api_id,
            "stage_name": stage_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_api_request.DeleteApiRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_api.delete_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_api_request.DeleteApiRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api_mapping(
        self,
        api_mapping_id: "capo_apigatewayv2.types.__string.__string",
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an API mapping.</p>

        Args:
            api_mapping_id: <p>The API mapping identifier.</p>
            domain_name: <p>The domain name.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_api_mapping_request.DeleteApiMappingRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_api_mapping

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_api_mapping.delete_api_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_api_mapping_request.DeleteApiMappingRequest = {
            "api_mapping_id": api_mapping_id,
            "domain_name": domain_name,
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        authorizer_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an Authorizer.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_id: <p>The authorizer identifier.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_authorizer_request.DeleteAuthorizerRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_authorizer

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_authorizer.delete_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_authorizer_request.DeleteAuthorizerRequest = {
            "api_id": api_id,
            "authorizer_id": authorizer_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cors_configuration(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a CORS configuration.</p>

        Args:
            api_id: <p>The API identifier.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_cors_configuration_request.DeleteCorsConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_cors_configuration

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_cors_configuration.delete_cors_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_cors_configuration_request.DeleteCorsConfigurationRequest = {
            "api_id": api_id
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        deployment_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Deployment.</p>

        Args:
            api_id: <p>The API identifier.</p>
            deployment_id: <p>The deployment ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_deployment_request.DeleteDeploymentRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_deployment

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_deployment.delete_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_deployment_request.DeleteDeploymentRequest = {
            "api_id": api_id,
            "deployment_id": deployment_id,
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
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_domain_name_request.DeleteDomainNameRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_domain_name

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_domain_name.delete_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_domain_name_request.DeleteDomainNameRequest = {
            "domain_name": domain_name
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_integration_request.DeleteIntegrationRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_integration

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_integration_request.DeleteIntegrationRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        integration_response_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_id: <p>The integration response ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_integration_response_request.DeleteIntegrationResponseRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_integration_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_integration_response.delete_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_integration_response_request.DeleteIntegrationResponseRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
            "integration_response_id": integration_response_id,
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        model_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Model.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_id: <p>The model ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_model_request.DeleteModelRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_model

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_model.delete_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_model_request.DeleteModelRequest = {
            "api_id": api_id,
            "model_id": model_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_portal(
        self,
        portal_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a portal.</p>

        Args:
            portal_id: <p>The portal identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_portal_request.DeletePortalRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_portal.delete_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_portal_request.DeletePortalRequest = {
            "portal_id": portal_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_portal_product(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_portal_product_request.DeletePortalProductRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_portal_product

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_portal_product.delete_portal_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_portal_product_request.DeletePortalProductRequest = {
            "portal_product_id": portal_product_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_portal_product_sharing_policy(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the sharing policy for a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_portal_product_sharing_policy_request.DeletePortalProductSharingPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_portal_product_sharing_policy

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_portal_product_sharing_policy.delete_portal_product_sharing_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_portal_product_sharing_policy_request.DeletePortalProductSharingPolicyRequest = {
            "portal_product_id": portal_product_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_product_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        product_page_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a product page of a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            product_page_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_product_page_request.DeleteProductPageRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_product_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_product_page.delete_product_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_product_page_request.DeleteProductPageRequest = {
            "portal_product_id": portal_product_id,
            "product_page_id": product_page_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_product_rest_endpoint_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        product_rest_endpoint_page_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a product REST endpoint page.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            product_rest_endpoint_page_id: <p>The product REST endpoint identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_product_rest_endpoint_page_request.DeleteProductRestEndpointPageRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_product_rest_endpoint_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_product_rest_endpoint_page.delete_product_rest_endpoint_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_product_rest_endpoint_page_request.DeleteProductRestEndpointPageRequest = {
            "portal_product_id": portal_product_id,
            "product_rest_endpoint_page_id": product_rest_endpoint_page_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_route(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_route_request.DeleteRouteRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_route

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_route.delete_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_route_request.DeleteRouteRequest = {
            "api_id": api_id,
            "route_id": route_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_route_request_parameter(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        request_parameter_key: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a route request parameter. Supported only for WebSocket APIs.</p>

        Args:
            api_id: <p>The API identifier.</p>
            request_parameter_key: <p>The route request parameter key.</p>
            route_id: <p>The route ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_route_request_parameter_request.DeleteRouteRequestParameterRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_route_request_parameter

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_route_request_parameter.delete_route_request_parameter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_route_request_parameter_request.DeleteRouteRequestParameterRequest = {
            "api_id": api_id,
            "request_parameter_key": request_parameter_key,
            "route_id": route_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_route_response(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        route_response_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a RouteResponse.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>
            route_response_id: <p>The route response ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_route_response_request.DeleteRouteResponseRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_route_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_route_response.delete_route_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_route_response_request.DeleteRouteResponseRequest = {
            "api_id": api_id,
            "route_id": route_id,
            "route_response_id": route_response_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_route_settings(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_key: "capo_apigatewayv2.types.__string.__string",
        stage_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the RouteSettings for a stage.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_key: <p>The route key.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_route_settings_request.DeleteRouteSettingsRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_route_settings

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_route_settings.delete_route_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_route_settings_request.DeleteRouteSettingsRequest = {
            "api_id": api_id,
            "route_key": route_key,
            "stage_name": stage_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_routing_rule(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        routing_rule_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> None:
        """<p>Deletes a routing rule.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            routing_rule_id: <p>The routing rule ID.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_routing_rule_request.DeleteRoutingRuleRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_routing_rule

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_routing_rule.delete_routing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_routing_rule_request.DeleteRoutingRuleRequest = {
            "domain_name": domain_name,
            "routing_rule_id": routing_rule_id,
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

    def delete_stage(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        stage_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes a Stage.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_stage_request.DeleteStageRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_stage

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_stage.delete_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_stage_request.DeleteStageRequest = {
            "api_id": api_id,
            "stage_name": stage_name,
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
        vpc_link_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse":
        """<p>Deletes a VPC link.</p>

        Args:
            vpc_link_id: <p>The ID of the VPC link.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.delete_vpc_link_response.DeleteVpcLinkResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.delete_vpc_link

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.delete_vpc_link.delete_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.delete_vpc_link_request.DeleteVpcLinkRequest = {
            "vpc_link_id": vpc_link_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disable_portal(
        self,
        portal_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the publication of a portal portal.</p>

        Args:
            portal_id: <p>The portal identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.disable_portal_request.DisablePortalRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.disable_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.disable_portal.disable_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.disable_portal_request.DisablePortalRequest = {
            "portal_id": portal_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def export_api(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        specification: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        export_version: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        include_extensions: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        output_type: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        stage_name: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.export_api_response.ExportApiResponse":
        """export_api

        Args:
            api_id: <p>The API identifier.</p>
            export_version: <p>The version of the API Gateway export algorithm. API Gateway uses the latest version by default. Currently, the only supported version is 1.0.</p>
            include_extensions: <p>Specifies whether to include <a href="https://docs.aws.amazon.com//apigateway/latest/developerguide/api-gateway-swagger-extensions.html">API Gateway extensions</a> in the exported API definition. API Gateway extensions are included by default.</p>
            output_type: <p>The output type of the exported definition file. Valid values are JSON and YAML.</p>
            specification: <p>The version of the API specification to use. OAS30, for OpenAPI 3.0, is the only supported value.</p>
            stage_name: <p>The name of the API stage to export. If you don't specify this property, a representation of the latest API configuration is exported.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.export_api_request.ExportApiRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.export_api_response.ExportApiResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.export_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.export_api.export_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.export_api_request.ExportApiRequest = {
            "api_id": api_id,
            "specification": specification,
        }
        if export_version is not None:
            input_["export_version"] = export_version
        if include_extensions is not None:
            input_["include_extensions"] = include_extensions
        if output_type is not None:
            input_["output_type"] = output_type
        if stage_name is not None:
            input_["stage_name"] = stage_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_api_response.GetApiResponse":
        """<p>Gets an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_api_request.GetApiRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_api_response.GetApiResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_api.get_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_api_request.GetApiRequest = {
            "api_id": api_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_mapping(
        self,
        api_mapping_id: "capo_apigatewayv2.types.__string.__string",
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_api_mapping_response.GetApiMappingResponse":
        """<p>Gets an API mapping.</p>

        Args:
            api_mapping_id: <p>The API mapping identifier.</p>
            domain_name: <p>The domain name.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_api_mapping_request.GetApiMappingRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_api_mapping_response.GetApiMappingResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_api_mapping

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_api_mapping.get_api_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_api_mapping_request.GetApiMappingRequest = {
            "api_mapping_id": api_mapping_id,
            "domain_name": domain_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_mappings(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_api_mappings_response.GetApiMappingsResponse":
        """<p>Gets API mappings.</p>

        Args:
            domain_name: <p>The domain name.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_api_mappings_request.GetApiMappingsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_api_mappings_response.GetApiMappingsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_api_mappings

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_api_mappings.get_api_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_api_mappings_request.GetApiMappingsRequest = {
            "domain_name": domain_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_apis(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_apis_response.GetApisResponse":
        """<p>Gets a collection of Api resources.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_apis_request.GetApisRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_apis_response.GetApisResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_apis

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_apis.get_apis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_apis_request.GetApisRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_authorizer(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        authorizer_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_authorizer_response.GetAuthorizerResponse":
        """<p>Gets an Authorizer.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_id: <p>The authorizer identifier.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_authorizer_request.GetAuthorizerRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_authorizer_response.GetAuthorizerResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_authorizer

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_authorizer.get_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_authorizer_request.GetAuthorizerRequest = {
            "api_id": api_id,
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_authorizers_response.GetAuthorizersResponse":
        """<p>Gets the Authorizers for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_authorizers_request.GetAuthorizersRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_authorizers_response.GetAuthorizersResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_authorizers

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_authorizers.get_authorizers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_authorizers_request.GetAuthorizersRequest = {
            "api_id": api_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        deployment_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_deployment_response.GetDeploymentResponse":
        """<p>Gets a Deployment.</p>

        Args:
            api_id: <p>The API identifier.</p>
            deployment_id: <p>The deployment ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_deployment_request.GetDeploymentRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_deployment_response.GetDeploymentResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_deployment

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_deployment_request.GetDeploymentRequest = {
            "api_id": api_id,
            "deployment_id": deployment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployments(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_deployments_response.GetDeploymentsResponse":
        """<p>Gets the Deployments for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_deployments_request.GetDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_deployments_response.GetDeploymentsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_deployments

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_deployments.get_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_deployments_request.GetDeploymentsRequest = {
            "api_id": api_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_name(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_domain_name_response.GetDomainNameResponse":
        """<p>Gets a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_domain_name_request.GetDomainNameRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_domain_name_response.GetDomainNameResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_domain_name

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_domain_name.get_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_domain_name_request.GetDomainNameRequest = {
            "domain_name": domain_name
        }

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
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_domain_names_response.GetDomainNamesResponse":
        """<p>Gets the domain names for an AWS account.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_domain_names_request.GetDomainNamesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_domain_names_response.GetDomainNamesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_domain_names

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_domain_names.get_domain_names(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_domain_names_request.GetDomainNamesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integration(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_integration_result.GetIntegrationResult":
        """<p>Gets an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_integration_request.GetIntegrationRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_integration_result.GetIntegrationResult"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_integration

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_integration_request.GetIntegrationRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        integration_response_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_integration_response_response.GetIntegrationResponseResponse":
        """<p>Gets an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_id: <p>The integration response ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_integration_response_request.GetIntegrationResponseRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_integration_response_response.GetIntegrationResponseResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_integration_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_integration_response.get_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_integration_response_request.GetIntegrationResponseRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
            "integration_response_id": integration_response_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integration_responses(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_integration_responses_response.GetIntegrationResponsesResponse":
        """<p>Gets the IntegrationResponses for an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            integration_id: <p>The integration ID.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_integration_responses_request.GetIntegrationResponsesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_integration_responses_response.GetIntegrationResponsesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_integration_responses

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_integration_responses.get_integration_responses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_integration_responses_request.GetIntegrationResponsesRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integrations(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_integrations_response.GetIntegrationsResponse":
        """<p>Gets the Integrations for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_integrations_request.GetIntegrationsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_integrations_response.GetIntegrationsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_integrations

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_integrations.get_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_integrations_request.GetIntegrationsRequest = {
            "api_id": api_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        model_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_model_response.GetModelResponse":
        """<p>Gets a Model.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_id: <p>The model ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_model_request.GetModelRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_model_response.GetModelResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_model

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_model.get_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_model_request.GetModelRequest = {
            "api_id": api_id,
            "model_id": model_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_models(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_models_response.GetModelsResponse":
        """<p>Gets the Models for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_models_request.GetModelsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_models_response.GetModelsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_models

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_models.get_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_models_request.GetModelsRequest = {
            "api_id": api_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model_template(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        model_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_model_template_response.GetModelTemplateResponse":
        """<p>Gets a model template.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_id: <p>The model ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_model_template_request.GetModelTemplateRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_model_template_response.GetModelTemplateResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_model_template

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_model_template.get_model_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_model_template_request.GetModelTemplateRequest = {
            "api_id": api_id,
            "model_id": model_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_portal(
        self,
        portal_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_portal_response.GetPortalResponse":
        """<p>Gets a portal.</p>

        Args:
            portal_id: <p>The portal identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_portal_request.GetPortalRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_portal_response.GetPortalResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_portal.get_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_portal_request.GetPortalRequest = {
            "portal_id": portal_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_portal_product(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        resource_owner_account_id: Optional[
            "capo_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "capo_apigatewayv2.types.get_portal_product_response.GetPortalProductResponse":
        """<p>Gets a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_portal_product_request.GetPortalProductRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_portal_product_response.GetPortalProductResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_portal_product

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_portal_product.get_portal_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_portal_product_request.GetPortalProductRequest = {
            "portal_product_id": portal_product_id
        }
        if resource_owner_account_id is not None:
            input_["resource_owner_account_id"] = resource_owner_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_portal_product_sharing_policy(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_portal_product_sharing_policy_response.GetPortalProductSharingPolicyResponse":
        """<p>Gets the sharing policy for a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_portal_product_sharing_policy_request.GetPortalProductSharingPolicyRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_portal_product_sharing_policy_response.GetPortalProductSharingPolicyResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_portal_product_sharing_policy

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_portal_product_sharing_policy.get_portal_product_sharing_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_portal_product_sharing_policy_request.GetPortalProductSharingPolicyRequest = {
            "portal_product_id": portal_product_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_product_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        product_page_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        resource_owner_account_id: Optional[
            "capo_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "capo_apigatewayv2.types.get_product_page_response.GetProductPageResponse":
        """<p>Gets a product page of a portal product.</p>

        Args:
            portal_product_id: <p>The portal product identifier.</p>
            product_page_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_product_page_request.GetProductPageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_product_page_response.GetProductPageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_product_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_product_page.get_product_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_product_page_request.GetProductPageRequest = {
            "portal_product_id": portal_product_id,
            "product_page_id": product_page_id,
        }
        if resource_owner_account_id is not None:
            input_["resource_owner_account_id"] = resource_owner_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_product_rest_endpoint_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        product_rest_endpoint_page_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        include_raw_display_content: Optional[
            "capo_apigatewayv2.types.__string.__string"
        ] = None,
        resource_owner_account_id: Optional[
            "capo_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "capo_apigatewayv2.types.get_product_rest_endpoint_page_response.GetProductRestEndpointPageResponse":
        """<p>Gets a product REST endpoint page.</p>

        Args:
            include_raw_display_content: <p>The query parameter to include raw display content.</p>
            portal_product_id: <p>The portal product identifier.</p>
            product_rest_endpoint_page_id: <p>The product REST endpoint identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_product_rest_endpoint_page_request.GetProductRestEndpointPageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_product_rest_endpoint_page_response.GetProductRestEndpointPageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_product_rest_endpoint_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_product_rest_endpoint_page.get_product_rest_endpoint_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_product_rest_endpoint_page_request.GetProductRestEndpointPageRequest = {
            "portal_product_id": portal_product_id,
            "product_rest_endpoint_page_id": product_rest_endpoint_page_id,
        }
        if include_raw_display_content is not None:
            input_["include_raw_display_content"] = include_raw_display_content
        if resource_owner_account_id is not None:
            input_["resource_owner_account_id"] = resource_owner_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_route(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_route_result.GetRouteResult":
        """<p>Gets a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_route_request.GetRouteRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_route_result.GetRouteResult"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_route

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_route.get_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_route_request.GetRouteRequest = {
            "api_id": api_id,
            "route_id": route_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_route_response(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        route_response_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_route_response_response.GetRouteResponseResponse":
        """<p>Gets a RouteResponse.</p>

        Args:
            api_id: <p>The API identifier.</p>
            route_id: <p>The route ID.</p>
            route_response_id: <p>The route response ID.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_route_response_request.GetRouteResponseRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_route_response_response.GetRouteResponseResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_route_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_route_response.get_route_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_route_response_request.GetRouteResponseRequest = {
            "api_id": api_id,
            "route_id": route_id,
            "route_response_id": route_response_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_route_responses(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> (
        "capo_apigatewayv2.types.get_route_responses_response.GetRouteResponsesResponse"
    ):
        """<p>Gets the RouteResponses for a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            route_id: <p>The route ID.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_route_responses_request.GetRouteResponsesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_route_responses_response.GetRouteResponsesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_route_responses

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_route_responses.get_route_responses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_route_responses_request.GetRouteResponsesRequest = {
            "api_id": api_id,
            "route_id": route_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_routes(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_routes_response.GetRoutesResponse":
        """<p>Gets the Routes for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_routes_request.GetRoutesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_routes_response.GetRoutesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_routes

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_routes.get_routes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_routes_request.GetRoutesRequest = {
            "api_id": api_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_routing_rule(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        routing_rule_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_routing_rule_response.GetRoutingRuleResponse":
        """<p>Gets a routing rule.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            routing_rule_id: <p>The routing rule ID.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_routing_rule_request.GetRoutingRuleRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_routing_rule_response.GetRoutingRuleResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_routing_rule

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_routing_rule.get_routing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_routing_rule_request.GetRoutingRuleRequest = {
            "domain_name": domain_name,
            "routing_rule_id": routing_rule_id,
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

    def get_stage(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        stage_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_stage_response.GetStageResponse":
        """<p>Gets a Stage.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can only contain alphanumeric characters, hyphens, and underscores. Maximum length is 128 characters.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_stage_request.GetStageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_stage_response.GetStageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_stage

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_stage.get_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_stage_request.GetStageRequest = {
            "api_id": api_id,
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
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_stages_response.GetStagesResponse":
        """<p>Gets the Stages for an API.</p>

        Args:
            api_id: <p>The API identifier.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_stages_request.GetStagesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_stages_response.GetStagesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_stages

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_stages.get_stages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_stages_request.GetStagesRequest = {
            "api_id": api_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_tags(
        self,
        resource_arn: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_tags_response.GetTagsResponse":
        """<p>Gets a collection of Tag resources.</p>

        Args:
            resource_arn: <p>The resource ARN for the tag.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_tags_request.GetTagsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_tags_response.GetTagsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_tags

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_tags.get_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_tags_request.GetTagsRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_vpc_link(
        self,
        vpc_link_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.get_vpc_link_response.GetVpcLinkResponse":
        """<p>Gets a VPC link.</p>

        Args:
            vpc_link_id: <p>The ID of the VPC link.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_vpc_link_request.GetVpcLinkRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_vpc_link_response.GetVpcLinkResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_vpc_link

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_vpc_link.get_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_vpc_link_request.GetVpcLinkRequest = {
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
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.get_vpc_links_response.GetVpcLinksResponse":
        """<p>Gets a collection of VPC links.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.get_vpc_links_request.GetVpcLinksRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.get_vpc_links_response.GetVpcLinksResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.get_vpc_links

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.get_vpc_links.get_vpc_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.get_vpc_links_request.GetVpcLinksRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_api(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        basepath: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        body: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        fail_on_warnings: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
    ) -> "capo_apigatewayv2.types.import_api_response.ImportApiResponse":
        """<p>Imports an API.</p>

        Args:
            basepath: <p>Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.</p>
            body: <p>The OpenAPI definition. Supported only for HTTP APIs.</p>
            fail_on_warnings: <p>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.import_api_request.ImportApiRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.import_api_response.ImportApiResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.import_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.import_api.import_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.import_api_request.ImportApiRequest = {}
        if basepath is not None:
            input_["basepath"] = basepath
        if body is not None:
            input_["body"] = body
        if fail_on_warnings is not None:
            input_["fail_on_warnings"] = fail_on_warnings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_portal_products(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        resource_owner: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.list_portal_products_response.ListPortalProductsResponse":
        """<p>Lists portal products.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            resource_owner: <p>The resource owner of the portal product.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.list_portal_products_request.ListPortalProductsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.list_portal_products_response.ListPortalProductsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.list_portal_products

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.list_portal_products.list_portal_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.list_portal_products_request.ListPortalProductsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_owner is not None:
            input_["resource_owner"] = resource_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_portals(
        self,
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.list_portals_response.ListPortalsResponse":
        """<p>Lists portals.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.list_portals_request.ListPortalsRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.list_portals_response.ListPortalsResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.list_portals

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.list_portals.list_portals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.list_portals_request.ListPortalsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_product_pages(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        resource_owner_account_id: Optional[
            "capo_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "capo_apigatewayv2.types.list_product_pages_response.ListProductPagesResponse":
        """<p>Lists the product pages for a portal product.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            portal_product_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.list_product_pages_request.ListProductPagesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.list_product_pages_response.ListProductPagesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.list_product_pages

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.list_product_pages.list_product_pages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.list_product_pages_request.ListProductPagesRequest = {
            "portal_product_id": portal_product_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_owner_account_id is not None:
            input_["resource_owner_account_id"] = resource_owner_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_product_rest_endpoint_pages(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        max_results: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        resource_owner_account_id: Optional[
            "capo_apigatewayv2.types.__string.__string"
        ] = None,
    ) -> "capo_apigatewayv2.types.list_product_rest_endpoint_pages_response.ListProductRestEndpointPagesResponse":
        """<p>Lists the product REST endpoint pages of a portal product.</p>

        Args:
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>
            portal_product_id: <p>The portal product identifier.</p>
            resource_owner_account_id: <p>The account ID of the resource owner of the portal product.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.list_product_rest_endpoint_pages_request.ListProductRestEndpointPagesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.list_product_rest_endpoint_pages_response.ListProductRestEndpointPagesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.list_product_rest_endpoint_pages

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.list_product_rest_endpoint_pages.list_product_rest_endpoint_pages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.list_product_rest_endpoint_pages_request.ListProductRestEndpointPagesRequest = {
            "portal_product_id": portal_product_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_owner_account_id is not None:
            input_["resource_owner_account_id"] = resource_owner_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_routing_rules(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        max_results: Optional["capo_apigatewayv2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "capo_apigatewayv2.types.list_routing_rules_response.ListRoutingRulesResponse":
        """<p>Lists routing rules.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            max_results: <p>The maximum number of elements to be returned for this resource.</p>
            next_token: <p>The next page of elements from this collection. Not valid for the last element of the collection.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.list_routing_rules_request.ListRoutingRulesRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.list_routing_rules_response.ListRoutingRulesResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.list_routing_rules

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.list_routing_rules.list_routing_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.list_routing_rules_request.ListRoutingRulesRequest = {
            "domain_name": domain_name
        }
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_routing_rules(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        domain_name_id: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        max_results: Optional["capo_apigatewayv2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_apigatewayv2.types.__string.__string"] = None,
    ) -> "Iterator[capo_apigatewayv2.types.routing_rule.RoutingRule]":
        _token = next_token
        while True:
            _response = self.list_routing_rules(
                domain_name,
                config_overrides=config_overrides,
                domain_name_id=domain_name_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("routing_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def preview_portal(
        self,
        portal_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> "capo_apigatewayv2.types.preview_portal_response.PreviewPortalResponse":
        """<p>Creates a portal preview.</p>

        Args:
            portal_id: <p>The portal identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.preview_portal_request.PreviewPortalRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.preview_portal_response.PreviewPortalResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.preview_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.preview_portal.preview_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.preview_portal_request.PreviewPortalRequest = {
            "portal_id": portal_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_portal(
        self,
        portal_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        description: Optional[
            "capo_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
    ) -> "capo_apigatewayv2.types.publish_portal_response.PublishPortalResponse":
        """<p>Publishes a portal.</p>

        Args:
            description: <p>The description of the portal. When the portal is published, this description becomes the last published description.</p>
            portal_id: <p>The portal identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.publish_portal_request.PublishPortalRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.publish_portal_response.PublishPortalResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.publish_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.publish_portal.publish_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.publish_portal_request.PublishPortalRequest = {
            "portal_id": portal_id
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

    def put_portal_product_sharing_policy(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        policy_document: Optional[
            "capo_apigatewayv2.types.__string_min1_max307200.__stringMin1Max307200"
        ] = None,
    ) -> "capo_apigatewayv2.types.put_portal_product_sharing_policy_response.PutPortalProductSharingPolicyResponse":
        """<p>Updates the sharing policy for a portal product.</p>

        Args:
            policy_document: <p>The product sharing policy.</p>
            portal_product_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.put_portal_product_sharing_policy_request.PutPortalProductSharingPolicyRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.put_portal_product_sharing_policy_response.PutPortalProductSharingPolicyResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.put_portal_product_sharing_policy

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.put_portal_product_sharing_policy.put_portal_product_sharing_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.put_portal_product_sharing_policy_request.PutPortalProductSharingPolicyRequest = {
            "portal_product_id": portal_product_id
        }
        if policy_document is not None:
            input_["policy_document"] = policy_document

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_routing_rule(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        routing_rule_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        actions: Optional[
            "capo_apigatewayv2.types.__list_of_routing_rule_action.__listOfRoutingRuleAction"
        ] = None,
        conditions: Optional[
            "capo_apigatewayv2.types.__list_of_routing_rule_condition.__listOfRoutingRuleCondition"
        ] = None,
        domain_name_id: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        priority: Optional[
            "capo_apigatewayv2.types.routing_rule_priority.RoutingRulePriority"
        ] = None,
    ) -> "capo_apigatewayv2.types.put_routing_rule_response.PutRoutingRuleResponse":
        """<p>Updates a routing rule.</p>

        Args:
            actions: <p>The routing rule action.</p>
            conditions: <p>The routing rule condition.</p>
            domain_name: <p>The domain name.</p>
            domain_name_id: <p>The domain name ID.</p>
            priority: <p>The routing rule priority.</p>
            routing_rule_id: <p>The routing rule ID.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.put_routing_rule_request.PutRoutingRuleRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.put_routing_rule_response.PutRoutingRuleResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.put_routing_rule

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.put_routing_rule.put_routing_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.put_routing_rule_request.PutRoutingRuleRequest = {
            "domain_name": domain_name,
            "routing_rule_id": routing_rule_id,
        }
        if actions is not None:
            input_["actions"] = actions
        if conditions is not None:
            input_["conditions"] = conditions
        if domain_name_id is not None:
            input_["domain_name_id"] = domain_name_id
        if priority is not None:
            input_["priority"] = priority

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reimport_api(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        basepath: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        body: Optional["capo_apigatewayv2.types.__string.__string"] = None,
        fail_on_warnings: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
    ) -> "capo_apigatewayv2.types.reimport_api_response.ReimportApiResponse":
        """<p>Puts an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>
            basepath: <p>Specifies how to interpret the base path of the API during import. Valid values are ignore, prepend, and split. The default value is ignore. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html">Set the OpenAPI basePath Property</a>. Supported only for HTTP APIs.</p>
            body: <p>The OpenAPI definition. Supported only for HTTP APIs.</p>
            fail_on_warnings: <p>Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.reimport_api_request.ReimportApiRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.reimport_api_response.ReimportApiResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.reimport_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.reimport_api.reimport_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.reimport_api_request.ReimportApiRequest = {
            "api_id": api_id
        }
        if basepath is not None:
            input_["basepath"] = basepath
        if body is not None:
            input_["body"] = body
        if fail_on_warnings is not None:
            input_["fail_on_warnings"] = fail_on_warnings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reset_authorizers_cache(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        stage_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
    ) -> None:
        """<p>Resets all authorizer cache entries on a stage. Supported only for HTTP APIs.</p>

        Args:
            api_id: <p>The API identifier.</p>
            stage_name: <p>The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.</p>

        Raises:
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.reset_authorizers_cache_request.ResetAuthorizersCacheRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.reset_authorizers_cache

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.reset_authorizers_cache.reset_authorizers_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.reset_authorizers_cache_request.ResetAuthorizersCacheRequest = {
            "api_id": api_id,
            "stage_name": stage_name,
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
        resource_arn: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        tags: Optional["capo_apigatewayv2.types.tags.Tags"] = None,
    ) -> "capo_apigatewayv2.types.tag_resource_response.TagResourceResponse":
        """<p>Creates a new Tag resource to represent a tag.</p>

        Args:
            resource_arn: <p>The resource ARN for the tag.</p>
            tags: <p>The collection of tags. Each tag element is associated with a given resource.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.tag_resource

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    def untag_resource(
        self,
        resource_arn: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        tag_keys: Optional[
            "capo_apigatewayv2.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """<p>Deletes a Tag.</p>

        Args:
            resource_arn: <p>The resource ARN for the tag.</p>
            tag_keys: <p>The Tag keys to delete</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewayv2._operations.api_gateway_v2.untag_resource

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        api_key_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        cors_configuration: Optional["capo_apigatewayv2.types.cors.Cors"] = None,
        credentials_arn: Optional["capo_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        disable_schema_validation: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        disable_execute_api_endpoint: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        ip_address_type: Optional[
            "capo_apigatewayv2.types.ip_address_type.IpAddressType"
        ] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        route_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        target: Optional[
            "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        version: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_api_response.UpdateApiResponse":
        """<p>Updates an Api resource.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_key_selection_expression: <p>An API key selection expression. Supported only for WebSocket APIs. See <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions">API Key Selection Expressions</a>.</p>
            cors_configuration: <p>A CORS configuration. Supported only for HTTP APIs.</p>
            credentials_arn: <p>This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, don't specify this parameter. Currently, this property is not used for HTTP integrations. If provided, this value replaces the credentials associated with the quick create integration. Supported only for HTTP APIs.</p>
            description: <p>The description of the API.</p>
            disable_schema_validation: <p>Avoid validating models when creating a deployment. Supported only for WebSocket APIs.</p>
            disable_execute_api_endpoint: <p>Specifies whether clients can invoke your API by using the default execute-api endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.</p>
            ip_address_type: <p>The IP address types that can invoke your API or domain name.</p>
            name: <p>The name of the API.</p>
            route_key: <p>This property is part of quick create. If not specified, the route created using quick create is kept. Otherwise, this value replaces the route key of the quick create route. Additional routes may still be added after the API is updated. Supported only for HTTP APIs.</p>
            route_selection_expression: <p>The route selection expression for the API. For HTTP APIs, the routeSelectionExpression must be ${request.method} ${request.path}. If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.</p>
            target: <p>This property is part of quick create. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. The value provided updates the integration URI and integration type. You can update a quick-created target, but you can't remove it from an API. Supported only for HTTP APIs.</p>
            version: <p>A version identifier for the API.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_api_request.UpdateApiRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_api_response.UpdateApiResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_api

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_api.update_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_api_request.UpdateApiRequest = {
            "api_id": api_id
        }
        if api_key_selection_expression is not None:
            input_["api_key_selection_expression"] = api_key_selection_expression
        if cors_configuration is not None:
            input_["cors_configuration"] = cors_configuration
        if credentials_arn is not None:
            input_["credentials_arn"] = credentials_arn
        if description is not None:
            input_["description"] = description
        if disable_schema_validation is not None:
            input_["disable_schema_validation"] = disable_schema_validation
        if disable_execute_api_endpoint is not None:
            input_["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if name is not None:
            input_["name"] = name
        if route_key is not None:
            input_["route_key"] = route_key
        if route_selection_expression is not None:
            input_["route_selection_expression"] = route_selection_expression
        if target is not None:
            input_["target"] = target
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api_mapping(
        self,
        api_mapping_id: "capo_apigatewayv2.types.__string.__string",
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        api_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        api_mapping_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        stage: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_api_mapping_response.UpdateApiMappingResponse":
        """<p>The API mapping.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_mapping_id: <p>The API mapping identifier.</p>
            api_mapping_key: <p>The API mapping key.</p>
            domain_name: <p>The domain name.</p>
            stage: <p>The API stage.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_api_mapping_request.UpdateApiMappingRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_api_mapping_response.UpdateApiMappingResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_api_mapping

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_api_mapping.update_api_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_api_mapping_request.UpdateApiMappingRequest = {
            "api_mapping_id": api_mapping_id,
            "domain_name": domain_name,
        }
        if api_id is not None:
            input_["api_id"] = api_id
        if api_mapping_key is not None:
            input_["api_mapping_key"] = api_mapping_key
        if stage is not None:
            input_["stage"] = stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_authorizer(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        authorizer_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        authorizer_credentials_arn: Optional["capo_apigatewayv2.types.arn.Arn"] = None,
        authorizer_payload_format_version: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        authorizer_result_ttl_in_seconds: Optional[
            "capo_apigatewayv2.types.integer_with_length_between0_and3600.IntegerWithLengthBetween0And3600"
        ] = None,
        authorizer_type: Optional[
            "capo_apigatewayv2.types.authorizer_type.AuthorizerType"
        ] = None,
        authorizer_uri: Optional[
            "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        enable_simple_responses: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        identity_source: Optional[
            "capo_apigatewayv2.types.identity_source_list.IdentitySourceList"
        ] = None,
        identity_validation_expression: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        jwt_configuration: Optional[
            "capo_apigatewayv2.types.jwt_configuration.JWTConfiguration"
        ] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_authorizer_response.UpdateAuthorizerResponse":
        """<p>Updates an Authorizer.</p>

        Args:
            api_id: <p>The API identifier.</p>
            authorizer_credentials_arn: <p>Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, don't specify this parameter.</p>
            authorizer_id: <p>The authorizer identifier.</p>
            authorizer_payload_format_version: <p>Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are 1.0 and 2.0. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a>.</p>
            authorizer_result_ttl_in_seconds: <p>The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.</p>
            authorizer_type: <p>The authorizer type. Specify REQUEST for a Lambda function using incoming request parameters. Specify JWT to use JSON Web Tokens (supported only for HTTP APIs).</p>
            authorizer_uri: <p>The authorizer's Uniform Resource Identifier (URI). For REQUEST authorizers, this must be a well-formed Lambda function URI, for example, arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:<replaceable>{account_id}</replaceable>:function:<replaceable>{lambda_function_name}</replaceable>/invocations. In general, the URI has this form: arn:aws:apigateway:<replaceable>{region}</replaceable>:lambda:path/<replaceable>{service_api}</replaceable> , where <replaceable></replaceable>{region} is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial /. For Lambda functions, this is usually of the form /2015-03-31/functions/[FunctionARN]/invocations. Supported only for REQUEST authorizers.</p>
            enable_simple_responses: <p>Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a></p>
            identity_source: <p>The identity source for which authorization is requested.</p> <p>For a REQUEST authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with $, for example, $request.header.Auth, $request.querystring.Name. These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html">Working with AWS Lambda authorizers for HTTP APIs</a>.</p> <p>For JWT, a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example $request.header.Authorization.</p>
            identity_validation_expression: <p>This parameter is not used.</p>
            jwt_configuration: <p>Represents the configuration of a JWT authorizer. Required for the JWT authorizer type. Supported only for HTTP APIs.</p>
            name: <p>The name of the authorizer.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_authorizer_request.UpdateAuthorizerRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_authorizer_response.UpdateAuthorizerResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_authorizer

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_authorizer.update_authorizer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_authorizer_request.UpdateAuthorizerRequest = {
            "api_id": api_id,
            "authorizer_id": authorizer_id,
        }
        if authorizer_credentials_arn is not None:
            input_["authorizer_credentials_arn"] = authorizer_credentials_arn
        if authorizer_payload_format_version is not None:
            input_["authorizer_payload_format_version"] = (
                authorizer_payload_format_version
            )
        if authorizer_result_ttl_in_seconds is not None:
            input_["authorizer_result_ttl_in_seconds"] = (
                authorizer_result_ttl_in_seconds
            )
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_uri is not None:
            input_["authorizer_uri"] = authorizer_uri
        if enable_simple_responses is not None:
            input_["enable_simple_responses"] = enable_simple_responses
        if identity_source is not None:
            input_["identity_source"] = identity_source
        if identity_validation_expression is not None:
            input_["identity_validation_expression"] = identity_validation_expression
        if jwt_configuration is not None:
            input_["jwt_configuration"] = jwt_configuration
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_deployment(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        deployment_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_deployment_response.UpdateDeploymentResponse":
        """<p>Updates a Deployment.</p>

        Args:
            api_id: <p>The API identifier.</p>
            deployment_id: <p>The deployment ID.</p>
            description: <p>The description for the deployment resource.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_deployment_request.UpdateDeploymentRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_deployment_response.UpdateDeploymentResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_deployment

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_deployment.update_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_deployment_request.UpdateDeploymentRequest = {
            "api_id": api_id,
            "deployment_id": deployment_id,
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

    def update_domain_name(
        self,
        domain_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        domain_name_configurations: Optional[
            "capo_apigatewayv2.types.domain_name_configurations.DomainNameConfigurations"
        ] = None,
        mutual_tls_authentication: Optional[
            "capo_apigatewayv2.types.mutual_tls_authentication_input.MutualTlsAuthenticationInput"
        ] = None,
        routing_mode: Optional[
            "capo_apigatewayv2.types.routing_mode.RoutingMode"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_domain_name_response.UpdateDomainNameResponse":
        """<p>Updates a domain name.</p>

        Args:
            domain_name: <p>The domain name.</p>
            domain_name_configurations: <p>The domain name configurations.</p>
            mutual_tls_authentication: <p>The mutual TLS authentication configuration for a custom domain name.</p>
            routing_mode: <p>The routing mode.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_domain_name_request.UpdateDomainNameRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_domain_name_response.UpdateDomainNameResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_domain_name

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_domain_name.update_domain_name(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_domain_name_request.UpdateDomainNameRequest = {
            "domain_name": domain_name
        }
        if domain_name_configurations is not None:
            input_["domain_name_configurations"] = domain_name_configurations
        if mutual_tls_authentication is not None:
            input_["mutual_tls_authentication"] = mutual_tls_authentication
        if routing_mode is not None:
            input_["routing_mode"] = routing_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_integration(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        connection_id: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and1024.StringWithLengthBetween1And1024"
        ] = None,
        connection_type: Optional[
            "capo_apigatewayv2.types.connection_type.ConnectionType"
        ] = None,
        content_handling_strategy: Optional[
            "capo_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        credentials_arn: Optional["capo_apigatewayv2.types.arn.Arn"] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        integration_method: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        integration_subtype: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        integration_type: Optional[
            "capo_apigatewayv2.types.integration_type.IntegrationType"
        ] = None,
        integration_uri: Optional[
            "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
        ] = None,
        passthrough_behavior: Optional[
            "capo_apigatewayv2.types.passthrough_behavior.PassthroughBehavior"
        ] = None,
        payload_format_version: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_parameters: Optional[
            "capo_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        request_templates: Optional[
            "capo_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        response_parameters: Optional[
            "capo_apigatewayv2.types.response_parameters.ResponseParameters"
        ] = None,
        template_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        timeout_in_millis: Optional[
            "capo_apigatewayv2.types.integer_with_length_between50_and30000.IntegerWithLengthBetween50And30000"
        ] = None,
        tls_config: Optional[
            "capo_apigatewayv2.types.tls_config_input.TlsConfigInput"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_integration_result.UpdateIntegrationResult":
        """<p>Updates an Integration.</p>

        Args:
            api_id: <p>The API identifier.</p>
            connection_id: <p>The ID of the VPC link for a private integration. Supported only for HTTP APIs.</p>
            connection_type: <p>The type of the network connection to the integration endpoint. Specify INTERNET for connections through the public routable internet or VPC_LINK for private connections between API Gateway and resources in a VPC. The default value is INTERNET.</p>
            content_handling_strategy: <p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            credentials_arn: <p>Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS services, specify null.</p>
            description: <p>The description of the integration</p>
            integration_id: <p>The integration ID.</p>
            integration_method: <p>Specifies the integration's HTTP method type.</p>
            integration_subtype: <p>Supported only for HTTP API AWS_PROXY integrations. Specifies the AWS service action to invoke. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html">Integration subtype reference</a>.</p>
            integration_type: <p>The integration type of an integration. One of the following:</p> <p>AWS: for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.</p> <p>AWS_PROXY: for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.</p> <p>HTTP: for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.</p> <p>HTTP_PROXY: for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an HTTP_PROXY integration.</p> <p>MOCK: for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.</p>
            integration_uri: <p>For a Lambda integration, specify the URI of a Lambda function.</p> <p>For an HTTP integration, specify a fully-qualified URL.</p> <p>For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses DiscoverInstances to identify resources. You can use query parameters to target specific resources. To learn more, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html">DiscoverInstances</a>. For private integrations, all resources must be owned by the same AWS account.</p>
            passthrough_behavior: <p>Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Supported only for WebSocket APIs.</p> <p>WHEN_NO_MATCH passes the request body for unmapped content types through to the integration backend without transformation.</p> <p>NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type response.</p> <p>WHEN_NO_TEMPLATES allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same HTTP 415 Unsupported Media Type response.</p>
            payload_format_version: <p>Specifies the format of the payload sent to an integration. Required for HTTP APIs. Supported values for Lambda proxy integrations are 1.0 and 2.0. For all other integrations, 1.0 is the only supported value. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html">Working with AWS Lambda proxy integrations for HTTP APIs</a>.</p>
            request_parameters: <p>For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of method.request.<replaceable>{location}</replaceable>.<replaceable>{name}</replaceable> , where <replaceable>{location}</replaceable> is querystring, path, or header; and <replaceable>{name}</replaceable> must be a valid and unique method request parameter name.</p> <p>For HTTP API integrations with a specified integrationSubtype, request parameters are a key-value map specifying parameters that are passed to AWS_PROXY integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html">Working with AWS service integrations for HTTP APIs</a>.</p> <p>For HTTP API integrations, without a specified integrationSubtype request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern &lt;action&gt;:&lt;header|querystring|path&gt;.&lt;location&gt; where action can be append, overwrite or remove. For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html">Transforming API requests and responses</a>.</p>
            request_templates: <p>Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.</p>
            response_parameters: <p>Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match pattern &lt;action&gt;:&lt;header&gt;.&lt;location&gt; or overwrite.statuscode. The action can be append, overwrite or remove. The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html">Transforming API requests and responses</a>.</p>
            template_selection_expression: <p>The template selection expression for the integration.</p>
            timeout_in_millis: <p>Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.</p>
            tls_config: <p>The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_integration_request.UpdateIntegrationRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_integration_result.UpdateIntegrationResult"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_integration

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_integration.update_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_integration_request.UpdateIntegrationRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
        }
        if connection_id is not None:
            input_["connection_id"] = connection_id
        if connection_type is not None:
            input_["connection_type"] = connection_type
        if content_handling_strategy is not None:
            input_["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None:
            input_["credentials_arn"] = credentials_arn
        if description is not None:
            input_["description"] = description
        if integration_method is not None:
            input_["integration_method"] = integration_method
        if integration_subtype is not None:
            input_["integration_subtype"] = integration_subtype
        if integration_type is not None:
            input_["integration_type"] = integration_type
        if integration_uri is not None:
            input_["integration_uri"] = integration_uri
        if passthrough_behavior is not None:
            input_["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None:
            input_["payload_format_version"] = payload_format_version
        if request_parameters is not None:
            input_["request_parameters"] = request_parameters
        if request_templates is not None:
            input_["request_templates"] = request_templates
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if template_selection_expression is not None:
            input_["template_selection_expression"] = template_selection_expression
        if timeout_in_millis is not None:
            input_["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            input_["tls_config"] = tls_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_integration_response(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        integration_id: "capo_apigatewayv2.types.__string.__string",
        integration_response_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        content_handling_strategy: Optional[
            "capo_apigatewayv2.types.content_handling_strategy.ContentHandlingStrategy"
        ] = None,
        integration_response_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        response_parameters: Optional[
            "capo_apigatewayv2.types.integration_parameters.IntegrationParameters"
        ] = None,
        response_templates: Optional[
            "capo_apigatewayv2.types.template_map.TemplateMap"
        ] = None,
        template_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_integration_response_response.UpdateIntegrationResponseResponse":
        """<p>Updates an IntegrationResponses.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_handling_strategy: <p>Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:</p> <p>CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the corresponding binary blob.</p> <p>CONVERT_TO_TEXT: Converts a response payload from a binary blob to a Base64-encoded string.</p> <p>If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.</p>
            integration_id: <p>The integration ID.</p>
            integration_response_id: <p>The integration response ID.</p>
            integration_response_key: <p>The integration response key.</p>
            response_parameters: <p>A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of method.response.header.<replaceable>{name}</replaceable> , where name is a valid and unique header name. The mapped non-static value must match the pattern of integration.response.header.<replaceable>{name}</replaceable> or integration.response.body.<replaceable>{JSON-expression}</replaceable> , where <replaceable>{name}</replaceable> is a valid and unique response header name and <replaceable>{JSON-expression}</replaceable> is a valid JSON expression without the $ prefix.</p>
            response_templates: <p>The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.</p>
            template_selection_expression: <p>The template selection expression for the integration response. Supported only for WebSocket APIs.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_integration_response_request.UpdateIntegrationResponseRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_integration_response_response.UpdateIntegrationResponseResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_integration_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_integration_response.update_integration_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_integration_response_request.UpdateIntegrationResponseRequest = {
            "api_id": api_id,
            "integration_id": integration_id,
            "integration_response_id": integration_response_id,
        }
        if content_handling_strategy is not None:
            input_["content_handling_strategy"] = content_handling_strategy
        if integration_response_key is not None:
            input_["integration_response_key"] = integration_response_key
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if response_templates is not None:
            input_["response_templates"] = response_templates
        if template_selection_expression is not None:
            input_["template_selection_expression"] = template_selection_expression

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_model(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        model_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        content_type: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and256.StringWithLengthBetween1And256"
        ] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
        schema: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and32_k.StringWithLengthBetween0And32K"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_model_response.UpdateModelResponse":
        """<p>Updates a Model.</p>

        Args:
            api_id: <p>The API identifier.</p>
            content_type: <p>The content-type for the model, for example, "application/json".</p>
            description: <p>The description of the model.</p>
            model_id: <p>The model ID.</p>
            name: <p>The name of the model.</p>
            schema: <p>The schema for the model. For application/json models, this should be JSON schema draft 4 model.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_model_request.UpdateModelRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_model_response.UpdateModelResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_model

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_model.update_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_model_request.UpdateModelRequest = {
            "api_id": api_id,
            "model_id": model_id,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if schema is not None:
            input_["schema"] = schema

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_portal(
        self,
        portal_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        authorization: Optional[
            "capo_apigatewayv2.types.authorization.Authorization"
        ] = None,
        endpoint_configuration: Optional[
            "capo_apigatewayv2.types.endpoint_configuration_request.EndpointConfigurationRequest"
        ] = None,
        included_portal_product_arns: Optional[
            "capo_apigatewayv2.types.__list_of__string_min20_max2048.__listOf__stringMin20Max2048"
        ] = None,
        logo_uri: Optional[
            "capo_apigatewayv2.types.__string_min0_max1092.__stringMin0Max1092"
        ] = None,
        portal_content: Optional[
            "capo_apigatewayv2.types.portal_content.PortalContent"
        ] = None,
        rum_app_monitor_name: Optional[
            "capo_apigatewayv2.types.__string_min0_max255.__stringMin0Max255"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_portal_response.UpdatePortalResponse":
        """<p>Updates a portal.</p>

        Args:
            authorization: <p>The authorization of the portal.</p>
            endpoint_configuration: <p>Represents an endpoint configuration.</p>
            included_portal_product_arns: <p>The ARNs of the portal products included in the portal.</p>
            logo_uri: <p>The logo URI.</p>
            portal_content: <p>Contains the content that is visible to portal consumers including the themes, display names, and description.</p>
            portal_id: <p>The portal identifier.</p>
            rum_app_monitor_name: <p>The CloudWatch RUM app monitor name.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_portal_request.UpdatePortalRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_portal_response.UpdatePortalResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_portal

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_portal.update_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_portal_request.UpdatePortalRequest = {
            "portal_id": portal_id
        }
        if authorization is not None:
            input_["authorization"] = authorization
        if endpoint_configuration is not None:
            input_["endpoint_configuration"] = endpoint_configuration
        if included_portal_product_arns is not None:
            input_["included_portal_product_arns"] = included_portal_product_arns
        if logo_uri is not None:
            input_["logo_uri"] = logo_uri
        if portal_content is not None:
            input_["portal_content"] = portal_content
        if rum_app_monitor_name is not None:
            input_["rum_app_monitor_name"] = rum_app_monitor_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_portal_product(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        description: Optional[
            "capo_apigatewayv2.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        display_name: Optional[
            "capo_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
        ] = None,
        display_order: Optional[
            "capo_apigatewayv2.types.display_order.DisplayOrder"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_portal_product_response.UpdatePortalProductResponse":
        """<p>Updates the portal product.</p>

        Args:
            description: <p>The description.</p>
            display_name: <p>The displayName.</p>
            display_order: <p>The display order.</p>
            portal_product_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_portal_product_request.UpdatePortalProductRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_portal_product_response.UpdatePortalProductResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_portal_product

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_portal_product.update_portal_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_portal_product_request.UpdatePortalProductRequest = {
            "portal_product_id": portal_product_id
        }
        if description is not None:
            input_["description"] = description
        if display_name is not None:
            input_["display_name"] = display_name
        if display_order is not None:
            input_["display_order"] = display_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_product_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        product_page_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "capo_apigatewayv2.types.display_content.DisplayContent"
        ] = None,
    ) -> (
        "capo_apigatewayv2.types.update_product_page_response.UpdateProductPageResponse"
    ):
        """<p>Updates a product page of a portal product.</p>

        Args:
            display_content: <p>The content of the product page.</p>
            portal_product_id: <p>The portal product identifier.</p>
            product_page_id: <p>The portal product identifier.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_product_page_request.UpdateProductPageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_product_page_response.UpdateProductPageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_product_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_product_page.update_product_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_product_page_request.UpdateProductPageRequest = {
            "portal_product_id": portal_product_id,
            "product_page_id": product_page_id,
        }
        if display_content is not None:
            input_["display_content"] = display_content

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_product_rest_endpoint_page(
        self,
        portal_product_id: "capo_apigatewayv2.types.__string.__string",
        product_rest_endpoint_page_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        display_content: Optional[
            "capo_apigatewayv2.types.endpoint_display_content.EndpointDisplayContent"
        ] = None,
        try_it_state: Optional[
            "capo_apigatewayv2.types.try_it_state.TryItState"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_product_rest_endpoint_page_response.UpdateProductRestEndpointPageResponse":
        """<p>Updates a product REST endpoint page.</p>

        Args:
            display_content: <p>The display content.</p>
            portal_product_id: <p>The portal product identifier.</p>
            product_rest_endpoint_page_id: <p>The product REST endpoint identifier.</p>
            try_it_state: <p>The try it state of a product REST endpoint page.</p>

        Raises:
            capo_apigatewayv2.errors.access_denied_exception.AccessDeniedException
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_product_rest_endpoint_page_request.UpdateProductRestEndpointPageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_product_rest_endpoint_page_response.UpdateProductRestEndpointPageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_product_rest_endpoint_page

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_product_rest_endpoint_page.update_product_rest_endpoint_page(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_product_rest_endpoint_page_request.UpdateProductRestEndpointPageRequest = {
            "portal_product_id": portal_product_id,
            "product_rest_endpoint_page_id": product_rest_endpoint_page_id,
        }
        if display_content is not None:
            input_["display_content"] = display_content
        if try_it_state is not None:
            input_["try_it_state"] = try_it_state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_route(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        api_key_required: Optional[
            "capo_apigatewayv2.types.__boolean.__boolean"
        ] = None,
        authorization_scopes: Optional[
            "capo_apigatewayv2.types.authorization_scopes.AuthorizationScopes"
        ] = None,
        authorization_type: Optional[
            "capo_apigatewayv2.types.authorization_type.AuthorizationType"
        ] = None,
        authorizer_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        model_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        operation_name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and64.StringWithLengthBetween1And64"
        ] = None,
        request_models: Optional[
            "capo_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        request_parameters: Optional[
            "capo_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
        route_response_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        target: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_route_result.UpdateRouteResult":
        """<p>Updates a Route.</p>

        Args:
            api_id: <p>The API identifier.</p>
            api_key_required: <p>Specifies whether an API key is required for the route. Supported only for WebSocket APIs.</p>
            authorization_scopes: <p>The authorization scopes supported by this route.</p>
            authorization_type: <p>The authorization type for the route. For WebSocket APIs, valid values are NONE for open access, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer For HTTP APIs, valid values are NONE for open access, JWT for using JSON Web Tokens, AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer.</p>
            authorizer_id: <p>The identifier of the Authorizer resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.</p>
            model_selection_expression: <p>The model selection expression for the route. Supported only for WebSocket APIs.</p>
            operation_name: <p>The operation name for the route.</p>
            request_models: <p>The request models for the route. Supported only for WebSocket APIs.</p>
            request_parameters: <p>The request parameters for the route. Supported only for WebSocket APIs.</p>
            route_id: <p>The route ID.</p>
            route_key: <p>The route key for the route.</p>
            route_response_selection_expression: <p>The route response selection expression for the route. Supported only for WebSocket APIs.</p>
            target: <p>The target for the route.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_route_request.UpdateRouteRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_route_result.UpdateRouteResult"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_route

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_route.update_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_route_request.UpdateRouteRequest = {
            "api_id": api_id,
            "route_id": route_id,
        }
        if api_key_required is not None:
            input_["api_key_required"] = api_key_required
        if authorization_scopes is not None:
            input_["authorization_scopes"] = authorization_scopes
        if authorization_type is not None:
            input_["authorization_type"] = authorization_type
        if authorizer_id is not None:
            input_["authorizer_id"] = authorizer_id
        if model_selection_expression is not None:
            input_["model_selection_expression"] = model_selection_expression
        if operation_name is not None:
            input_["operation_name"] = operation_name
        if request_models is not None:
            input_["request_models"] = request_models
        if request_parameters is not None:
            input_["request_parameters"] = request_parameters
        if route_key is not None:
            input_["route_key"] = route_key
        if route_response_selection_expression is not None:
            input_["route_response_selection_expression"] = (
                route_response_selection_expression
            )
        if target is not None:
            input_["target"] = target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_route_response(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        route_id: "capo_apigatewayv2.types.__string.__string",
        route_response_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        model_selection_expression: Optional[
            "capo_apigatewayv2.types.selection_expression.SelectionExpression"
        ] = None,
        response_models: Optional[
            "capo_apigatewayv2.types.route_models.RouteModels"
        ] = None,
        response_parameters: Optional[
            "capo_apigatewayv2.types.route_parameters.RouteParameters"
        ] = None,
        route_response_key: Optional[
            "capo_apigatewayv2.types.selection_key.SelectionKey"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_route_response_response.UpdateRouteResponseResponse":
        """<p>Updates a RouteResponse.</p>

        Args:
            api_id: <p>The API identifier.</p>
            model_selection_expression: <p>The model selection expression for the route response. Supported only for WebSocket APIs.</p>
            response_models: <p>The response models for the route response.</p>
            response_parameters: <p>The route response parameters.</p>
            route_id: <p>The route ID.</p>
            route_response_id: <p>The route response ID.</p>
            route_response_key: <p>The route response key.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_route_response_request.UpdateRouteResponseRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_route_response_response.UpdateRouteResponseResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_route_response

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_route_response.update_route_response(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_route_response_request.UpdateRouteResponseRequest = {
            "api_id": api_id,
            "route_id": route_id,
            "route_response_id": route_response_id,
        }
        if model_selection_expression is not None:
            input_["model_selection_expression"] = model_selection_expression
        if response_models is not None:
            input_["response_models"] = response_models
        if response_parameters is not None:
            input_["response_parameters"] = response_parameters
        if route_response_key is not None:
            input_["route_response_key"] = route_response_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stage(
        self,
        api_id: "capo_apigatewayv2.types.__string.__string",
        stage_name: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        access_log_settings: Optional[
            "capo_apigatewayv2.types.access_log_settings.AccessLogSettings"
        ] = None,
        auto_deploy: Optional["capo_apigatewayv2.types.__boolean.__boolean"] = None,
        client_certificate_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        default_route_settings: Optional[
            "capo_apigatewayv2.types.route_settings.RouteSettings"
        ] = None,
        deployment_id: Optional["capo_apigatewayv2.types.id.Id"] = None,
        description: Optional[
            "capo_apigatewayv2.types.string_with_length_between0_and1024.StringWithLengthBetween0And1024"
        ] = None,
        route_settings: Optional[
            "capo_apigatewayv2.types.route_settings_map.RouteSettingsMap"
        ] = None,
        stage_variables: Optional[
            "capo_apigatewayv2.types.stage_variables_map.StageVariablesMap"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_stage_response.UpdateStageResponse":
        """<p>Updates a Stage.</p>

        Args:
            access_log_settings: <p>Settings for logging access in this stage.</p>
            api_id: <p>The API identifier.</p>
            auto_deploy: <p>Specifies whether updates to an API automatically trigger a new deployment. The default value is false.</p>
            client_certificate_id: <p>The identifier of a client certificate for a Stage.</p>
            default_route_settings: <p>The default route settings for the stage.</p>
            deployment_id: <p>The deployment identifier for the API stage. Can't be updated if autoDeploy is enabled.</p>
            description: <p>The description for the API stage.</p>
            route_settings: <p>Route settings for the stage.</p>
            stage_name: <p>The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be $default. Maximum length is 128 characters.</p>
            stage_variables: <p>A map that defines the stage variables for a Stage. Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&amp;=,]+.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_stage_request.UpdateStageRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_stage_response.UpdateStageResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_stage

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_stage.update_stage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_stage_request.UpdateStageRequest = {
            "api_id": api_id,
            "stage_name": stage_name,
        }
        if access_log_settings is not None:
            input_["access_log_settings"] = access_log_settings
        if auto_deploy is not None:
            input_["auto_deploy"] = auto_deploy
        if client_certificate_id is not None:
            input_["client_certificate_id"] = client_certificate_id
        if default_route_settings is not None:
            input_["default_route_settings"] = default_route_settings
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id
        if description is not None:
            input_["description"] = description
        if route_settings is not None:
            input_["route_settings"] = route_settings
        if stage_variables is not None:
            input_["stage_variables"] = stage_variables

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_vpc_link(
        self,
        vpc_link_id: "capo_apigatewayv2.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayV2ClientConfig] = None,
        name: Optional[
            "capo_apigatewayv2.types.string_with_length_between1_and128.StringWithLengthBetween1And128"
        ] = None,
    ) -> "capo_apigatewayv2.types.update_vpc_link_response.UpdateVpcLinkResponse":
        """<p>Updates a VPC link.</p>

        Args:
            name: <p>The name of the VPC link.</p>
            vpc_link_id: <p>The ID of the VPC link.</p>

        Raises:
            capo_apigatewayv2.errors.bad_request_exception.BadRequestException: <p>The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.not_found_exception.NotFoundException: <p>The resource specified in the request was not found. See the message field for more information.</p>
            capo_apigatewayv2.errors.too_many_requests_exception.TooManyRequestsException: <p>A limit has been exceeded. See the accompanying error message for details.</p>
            capo_apigatewayv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewayv2.types.update_vpc_link_request.UpdateVpcLinkRequest]",
        ) -> OperationResponse[
            "capo_apigatewayv2.types.update_vpc_link_response.UpdateVpcLinkResponse"
        ]:
            import capo_apigatewayv2._operations.api_gateway_v2.update_vpc_link

            output, http_response = (
                capo_apigatewayv2._operations.api_gateway_v2.update_vpc_link.update_vpc_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewayv2.types.update_vpc_link_request.UpdateVpcLinkRequest = {
            "vpc_link_id": vpc_link_id
        }
        if name is not None:
            input_["name"] = name

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
