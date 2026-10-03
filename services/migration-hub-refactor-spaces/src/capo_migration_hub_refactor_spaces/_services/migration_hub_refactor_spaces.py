"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#RefactorSpaces``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_migration_hub_refactor_spaces._auth._signers
import capo_migration_hub_refactor_spaces._auth._sigv4
from capo_migration_hub_refactor_spaces._auth._identity import Credentials
from capo_migration_hub_refactor_spaces._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_migration_hub_refactor_spaces._auth._zapros_handler import AuthMiddleware
from capo_migration_hub_refactor_spaces._pagination import resolve_path as _resolve_path
from capo_migration_hub_refactor_spaces._services._aws_config import aws_config
from capo_migration_hub_refactor_spaces._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.application_name
    import capo_migration_hub_refactor_spaces.types.application_summary
    import capo_migration_hub_refactor_spaces.types.client_token
    import capo_migration_hub_refactor_spaces.types.create_application_request
    import capo_migration_hub_refactor_spaces.types.create_application_response
    import capo_migration_hub_refactor_spaces.types.create_environment_request
    import capo_migration_hub_refactor_spaces.types.create_environment_response
    import capo_migration_hub_refactor_spaces.types.create_route_request
    import capo_migration_hub_refactor_spaces.types.create_route_response
    import capo_migration_hub_refactor_spaces.types.create_service_request
    import capo_migration_hub_refactor_spaces.types.create_service_response
    import capo_migration_hub_refactor_spaces.types.default_route_input
    import capo_migration_hub_refactor_spaces.types.delete_application_request
    import capo_migration_hub_refactor_spaces.types.delete_application_response
    import capo_migration_hub_refactor_spaces.types.delete_environment_request
    import capo_migration_hub_refactor_spaces.types.delete_environment_response
    import capo_migration_hub_refactor_spaces.types.delete_resource_policy_request
    import capo_migration_hub_refactor_spaces.types.delete_resource_policy_response
    import capo_migration_hub_refactor_spaces.types.delete_route_request
    import capo_migration_hub_refactor_spaces.types.delete_route_response
    import capo_migration_hub_refactor_spaces.types.delete_service_request
    import capo_migration_hub_refactor_spaces.types.delete_service_response
    import capo_migration_hub_refactor_spaces.types.description
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.environment_name
    import capo_migration_hub_refactor_spaces.types.environment_summary
    import capo_migration_hub_refactor_spaces.types.environment_vpc
    import capo_migration_hub_refactor_spaces.types.get_application_request
    import capo_migration_hub_refactor_spaces.types.get_application_response
    import capo_migration_hub_refactor_spaces.types.get_environment_request
    import capo_migration_hub_refactor_spaces.types.get_environment_response
    import capo_migration_hub_refactor_spaces.types.get_resource_policy_request
    import capo_migration_hub_refactor_spaces.types.get_resource_policy_response
    import capo_migration_hub_refactor_spaces.types.get_route_request
    import capo_migration_hub_refactor_spaces.types.get_route_response
    import capo_migration_hub_refactor_spaces.types.get_service_request
    import capo_migration_hub_refactor_spaces.types.get_service_response
    import capo_migration_hub_refactor_spaces.types.lambda_endpoint_input
    import capo_migration_hub_refactor_spaces.types.list_applications_request
    import capo_migration_hub_refactor_spaces.types.list_applications_response
    import capo_migration_hub_refactor_spaces.types.list_environment_vpcs_request
    import capo_migration_hub_refactor_spaces.types.list_environment_vpcs_response
    import capo_migration_hub_refactor_spaces.types.list_environments_request
    import capo_migration_hub_refactor_spaces.types.list_environments_response
    import capo_migration_hub_refactor_spaces.types.list_routes_request
    import capo_migration_hub_refactor_spaces.types.list_routes_response
    import capo_migration_hub_refactor_spaces.types.list_services_request
    import capo_migration_hub_refactor_spaces.types.list_services_response
    import capo_migration_hub_refactor_spaces.types.list_tags_for_resource_request
    import capo_migration_hub_refactor_spaces.types.list_tags_for_resource_response
    import capo_migration_hub_refactor_spaces.types.max_results
    import capo_migration_hub_refactor_spaces.types.network_fabric_type
    import capo_migration_hub_refactor_spaces.types.next_token
    import capo_migration_hub_refactor_spaces.types.policy_string
    import capo_migration_hub_refactor_spaces.types.proxy_type
    import capo_migration_hub_refactor_spaces.types.put_resource_policy_request
    import capo_migration_hub_refactor_spaces.types.put_resource_policy_response
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.resource_policy_identifier
    import capo_migration_hub_refactor_spaces.types.route_activation_state
    import capo_migration_hub_refactor_spaces.types.route_id
    import capo_migration_hub_refactor_spaces.types.route_summary
    import capo_migration_hub_refactor_spaces.types.route_type
    import capo_migration_hub_refactor_spaces.types.service_endpoint_type
    import capo_migration_hub_refactor_spaces.types.service_id
    import capo_migration_hub_refactor_spaces.types.service_name
    import capo_migration_hub_refactor_spaces.types.service_summary
    import capo_migration_hub_refactor_spaces.types.string
    import capo_migration_hub_refactor_spaces.types.tag_keys
    import capo_migration_hub_refactor_spaces.types.tag_map
    import capo_migration_hub_refactor_spaces.types.tag_resource_request
    import capo_migration_hub_refactor_spaces.types.tag_resource_response
    import capo_migration_hub_refactor_spaces.types.untag_resource_request
    import capo_migration_hub_refactor_spaces.types.untag_resource_response
    import capo_migration_hub_refactor_spaces.types.update_route_request
    import capo_migration_hub_refactor_spaces.types.update_route_response
    import capo_migration_hub_refactor_spaces.types.uri_path_route_input
    import capo_migration_hub_refactor_spaces.types.url_endpoint_input
    import capo_migration_hub_refactor_spaces.types.vpc_id


class MigrationHubRefactorSpacesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MigrationHubRefactorSpacesClient:
    """A client for the ``MigrationHubRefactorSpaces`` service.

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
        self._config = MigrationHubRefactorSpacesClientConfig(
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
        self, config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MigrationHubRefactorSpacesClientConfig = config_overrides or {}
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

    def create_application(
        self,
        name: "capo_migration_hub_refactor_spaces.types.application_name.ApplicationName",
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        vpc_id: "capo_migration_hub_refactor_spaces.types.vpc_id.VpcId",
        proxy_type: "capo_migration_hub_refactor_spaces.types.proxy_type.ProxyType",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        api_gateway_proxy: Optional[
            "capo_migration_hub_refactor_spaces.types.api_gateway_proxy_input.ApiGatewayProxyInput"
        ] = None,
        tags: Optional[
            "capo_migration_hub_refactor_spaces.types.tag_map.TagMap"
        ] = None,
        client_token: Optional[
            "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an Amazon Web Services Migration Hub Refactor Spaces application. The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway, API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.</p> <p>In environments created with a <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType">CreateEnvironment:NetworkFabricType</a> of <code>NONE</code> you need to configure <a href="https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html"> VPC to VPC connectivity</a> between your service VPC and the application proxy VPC to route traffic through the application proxy to a service with a private URL endpoint. For more information, see <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-application.html"> Create an application</a> in the <i>Refactor Spaces User Guide</i>. </p>

        Args:
            name: <p>The name to use for the application. </p>
            environment_identifier: <p>The unique identifier of the environment.</p>
            vpc_id: <p>The ID of the virtual private cloud (VPC).</p>
            proxy_type: <p>The proxy type of the proxy created within the application. </p>
            api_gateway_proxy: <p>A wrapper object holding the API Gateway endpoint type and stage name for the proxy. </p>
            tags: <p>The tags to assign to the application. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_application

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.create_application_request.CreateApplicationRequest = {
            "name": name,
            "environment_identifier": environment_identifier,
            "vpc_id": vpc_id,
            "proxy_type": proxy_type,
        }
        if api_gateway_proxy is not None:
            input_["api_gateway_proxy"] = api_gateway_proxy
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_environment(
        self,
        name: "capo_migration_hub_refactor_spaces.types.environment_name.EnvironmentName",
        network_fabric_type: "capo_migration_hub_refactor_spaces.types.network_fabric_type.NetworkFabricType",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        description: Optional[
            "capo_migration_hub_refactor_spaces.types.description.Description"
        ] = None,
        tags: Optional[
            "capo_migration_hub_refactor_spaces.types.tag_map.TagMap"
        ] = None,
        client_token: Optional[
            "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.create_environment_response.CreateEnvironmentResponse":
        """<p>Creates an Amazon Web Services Migration Hub Refactor Spaces environment. The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the <i>environment owner</i>. The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with.</p> <p>When creating an environment with a <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType">CreateEnvironment:NetworkFabricType</a> of <code>TRANSIT_GATEWAY</code>, Refactor Spaces provisions a transit gateway to enable services in VPCs to communicate directly across accounts. If <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType">CreateEnvironment:NetworkFabricType</a> is <code>NONE</code>, Refactor Spaces does not create a transit gateway and you must use your network infrastructure to route traffic to services with private URL endpoints.</p>

        Args:
            name: <p>The name of the environment.</p>
            description: <p>The description of the environment.</p>
            network_fabric_type: <p>The network fabric type of the environment.</p>
            tags: <p>The tags to assign to the environment. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.create_environment_request.CreateEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.create_environment_response.CreateEnvironmentResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_environment

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_environment.create_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.create_environment_request.CreateEnvironmentRequest = {
            "name": name,
            "network_fabric_type": network_fabric_type,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_route(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        service_identifier: "capo_migration_hub_refactor_spaces.types.service_id.ServiceId",
        route_type: "capo_migration_hub_refactor_spaces.types.route_type.RouteType",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        default_route: Optional[
            "capo_migration_hub_refactor_spaces.types.default_route_input.DefaultRouteInput"
        ] = None,
        uri_path_route: Optional[
            "capo_migration_hub_refactor_spaces.types.uri_path_route_input.UriPathRouteInput"
        ] = None,
        tags: Optional[
            "capo_migration_hub_refactor_spaces.types.tag_map.TagMap"
        ] = None,
        client_token: Optional[
            "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.create_route_response.CreateRouteResponse":
        """<p>Creates an Amazon Web Services Migration Hub Refactor Spaces route. The account owner of the service resource is always the environment owner, regardless of which account creates the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a <code>DEFAULT</code> <code>RouteType</code>.</p> <p>When created, the default route defaults to an active state so state is not a required input. However, like all other state values the state of the default route can be updated after creation, but only when all other routes are also inactive. Conversely, no route can be active without the default route also being active.</p> <p>When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service as follows:</p> <ul> <li> <p> <b>URL Endpoints</b> </p> <p>If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link. If a service endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet. Services can have HTTP or HTTPS URL endpoints. For HTTPS URLs, publicly-signed certificates are supported. Private Certificate Authorities (CAs) are permitted only if the CA's domain is also publicly resolvable. </p> <p>Refactor Spaces automatically resolves the public Domain Name System (DNS) names that are set in <code>CreateService:UrlEndpoint </code>when you create a service. The DNS names resolve when the DNS time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds. This periodic DNS resolution ensures that the route configuration remains up-to-date. </p> <p/> <p> <b>One-time health check</b> </p> <p>A one-time health check is performed on the service when either the route is updated from inactive to active, or when it is created with an active state. If the health check fails, the route transitions the route state to <code>FAILED</code>, an error code of <code>SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE</code> is provided, and no traffic is sent to the service.</p> <p>For private URLs, a target group is created on the Network Load Balancer and the load balancer target group runs default target health checks. By default, the health check is run against the service endpoint URL. Optionally, the health check can be performed against a different protocol, port, and/or path using the <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html#migrationhubrefactorspaces-CreateService-request-UrlEndpoint">CreateService:UrlEndpoint</a> parameter. All other health check settings for the load balancer use the default values described in the <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html">Health checks for your target groups</a> in the <i>Elastic Load Balancing guide</i>. The health check is considered successful if at least one target within the target group transitions to a healthy state.</p> <p/> </li> <li> <p> <b>Lambda function endpoints</b> </p> <p>If the service has an Lambda function endpoint, then Refactor Spaces configures the Lambda function's resource policy to allow the application's API Gateway to invoke the function.</p> <p>The Lambda function state is checked. If the function is not active, the function configuration is updated so that Lambda resources are provisioned. If the Lambda state is <code>Failed</code>, then the route creation fails. For more information, see the <a href="https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State">GetFunctionConfiguration's State response parameter</a> in the <i>Lambda Developer Guide</i>.</p> <p>A check is performed to determine that a Lambda function with the specified ARN exists. If it does not exist, the health check fails. For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails. </p> </li> </ul> <p> <b>Environments without a network bridge</b> </p> <p>When you create environments without a network bridge (<a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType">CreateEnvironment:NetworkFabricType</a> is <code>NONE)</code> and you use your own networking infrastructure, you need to configure <a href="https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html">VPC to VPC connectivity</a> between your network and the application proxy VPC. Route creation from the application proxy to service endpoints will fail if your network is not configured to connect to the application proxy VPC. For more information, see <a href="https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-role.html"> Create a route</a> in the <i>Refactor Spaces User Guide</i>.</p> <p/>

        Args:
            environment_identifier: <p>The ID of the environment in which the route is created.</p>
            application_identifier: <p>The ID of the application within which the route is being created.</p>
            service_identifier: <p>The ID of the service in which the route is created. Traffic that matches this route is forwarded to this service.</p>
            route_type: <p>The route type of the route. <code>DEFAULT</code> indicates that all traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created. <code>URI_PATH</code> indicates a route that is based on a URI path.</p>
            default_route: <p> Configuration for the default route type. </p>
            uri_path_route: <p>The configuration for the URI path route type. </p>
            tags: <p>The tags to assign to the route. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.create_route_request.CreateRouteRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.create_route_response.CreateRouteResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_route

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_route.create_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.create_route_request.CreateRouteRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "service_identifier": service_identifier,
            "route_type": route_type,
        }
        if default_route is not None:
            input_["default_route"] = default_route
        if uri_path_route is not None:
            input_["uri_path_route"] = uri_path_route
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_service(
        self,
        name: "capo_migration_hub_refactor_spaces.types.service_name.ServiceName",
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        endpoint_type: "capo_migration_hub_refactor_spaces.types.service_endpoint_type.ServiceEndpointType",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        description: Optional[
            "capo_migration_hub_refactor_spaces.types.description.Description"
        ] = None,
        vpc_id: Optional[
            "capo_migration_hub_refactor_spaces.types.vpc_id.VpcId"
        ] = None,
        url_endpoint: Optional[
            "capo_migration_hub_refactor_spaces.types.url_endpoint_input.UrlEndpointInput"
        ] = None,
        lambda_endpoint: Optional[
            "capo_migration_hub_refactor_spaces.types.lambda_endpoint_input.LambdaEndpointInput"
        ] = None,
        tags: Optional[
            "capo_migration_hub_refactor_spaces.types.tag_map.TagMap"
        ] = None,
        client_token: Optional[
            "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.create_service_response.CreateServiceResponse":
        """<p>Creates an Amazon Web Services Migration Hub Refactor Spaces service. The account owner of the service is always the environment owner, regardless of which account in the environment creates the service. Services have either a URL endpoint in a virtual private cloud (VPC), or a Lambda function endpoint.</p> <important> <p>If an Amazon Web Services resource is launched in a service VPC, and you want it to be accessible to all of an environment’s services with VPCs and routes, apply the <code>RefactorSpacesSecurityGroup</code> to the resource. Alternatively, to add more cross-account constraints, apply your own security group.</p> </important>

        Args:
            name: <p>The name of the service.</p>
            description: <p>The description of the service.</p>
            environment_identifier: <p>The ID of the environment in which the service is created.</p>
            application_identifier: <p>The ID of the application which the service is created.</p>
            vpc_id: <p>The ID of the VPC.</p>
            endpoint_type: <p>The type of endpoint to use for the service. The type can be a URL in a VPC or an Lambda function.</p>
            url_endpoint: <p>The configuration for the URL endpoint type. When creating a route to a service, Refactor Spaces automatically resolves the address in the <code>UrlEndpointInput</code> object URL when the Domain Name System (DNS) time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds.</p>
            lambda_endpoint: <p>The configuration for the Lambda endpoint type.</p>
            tags: <p>The tags to assign to the service. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_service

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.create_service_request.CreateServiceRequest = {
            "name": name,
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "endpoint_type": endpoint_type,
        }
        if description is not None:
            input_["description"] = description
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if url_endpoint is not None:
            input_["url_endpoint"] = url_endpoint
        if lambda_endpoint is not None:
            input_["lambda_endpoint"] = lambda_endpoint
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an Amazon Web Services Migration Hub Refactor Spaces application. Before you can delete an application, you must first delete any services or routes within the application.</p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>
            application_identifier: <p>The ID of the application.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_application

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.delete_application_request.DeleteApplicationRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_environment(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.delete_environment_response.DeleteEnvironmentResponse":
        """<p>Deletes an Amazon Web Services Migration Hub Refactor Spaces environment. Before you can delete an environment, you must first delete any applications and services within the environment.</p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.delete_environment_request.DeleteEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.delete_environment_response.DeleteEnvironmentResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_environment

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_environment.delete_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.delete_environment_request.DeleteEnvironmentRequest = {
            "environment_identifier": environment_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        identifier: "capo_migration_hub_refactor_spaces.types.resource_policy_identifier.ResourcePolicyIdentifier",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the resource policy set for the environment. </p>

        Args:
            identifier: <p>Amazon Resource Name (ARN) of the resource associated with the policy. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_resource_policy

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "identifier": identifier
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
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        route_identifier: "capo_migration_hub_refactor_spaces.types.route_id.RouteId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.delete_route_response.DeleteRouteResponse":
        """<p>Deletes an Amazon Web Services Migration Hub Refactor Spaces route.</p>

        Args:
            environment_identifier: <p>The ID of the environment to delete the route from.</p>
            application_identifier: <p>The ID of the application to delete the route from.</p>
            route_identifier: <p>The ID of the route to delete.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.delete_route_request.DeleteRouteRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.delete_route_response.DeleteRouteResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_route

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_route.delete_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.delete_route_request.DeleteRouteRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "route_identifier": route_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        service_identifier: "capo_migration_hub_refactor_spaces.types.service_id.ServiceId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes an Amazon Web Services Migration Hub Refactor Spaces service. </p>

        Args:
            environment_identifier: <p>The ID of the environment that the service is in.</p>
            application_identifier: <p>Deletes a Refactor Spaces service.</p> <note> <p>The <code>RefactorSpacesSecurityGroup</code> security group must be removed from all Amazon Web Services resources in the virtual private cloud (VPC) prior to deleting a service with a URL endpoint in a VPC.</p> </note>
            service_identifier: <p>The ID of the service to delete.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_service

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.delete_service_request.DeleteServiceRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "service_identifier": service_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.get_application_response.GetApplicationResponse":
        """<p>Gets an Amazon Web Services Migration Hub Refactor Spaces application.</p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>
            application_identifier: <p>The ID of the application.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_application

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.get_application_request.GetApplicationRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_environment(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.get_environment_response.GetEnvironmentResponse":
        """<p>Gets an Amazon Web Services Migration Hub Refactor Spaces environment.</p>

        Args:
            environment_identifier: <p>The ID of the environment.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.get_environment_request.GetEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.get_environment_response.GetEnvironmentResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_environment

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_environment.get_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.get_environment_request.GetEnvironmentRequest = {
            "environment_identifier": environment_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        identifier: "capo_migration_hub_refactor_spaces.types.resource_policy_identifier.ResourcePolicyIdentifier",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets the resource-based permission policy that is set for the given environment. </p>

        Args:
            identifier: <p>The Amazon Resource Name (ARN) of the resource associated with the policy. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_resource_policy

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_route(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        route_identifier: "capo_migration_hub_refactor_spaces.types.route_id.RouteId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.get_route_response.GetRouteResponse":
        """<p>Gets an Amazon Web Services Migration Hub Refactor Spaces route.</p>

        Args:
            environment_identifier: <p>The ID of the environment.</p>
            application_identifier: <p>The ID of the application. </p>
            route_identifier: <p>The ID of the route.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.get_route_request.GetRouteRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.get_route_response.GetRouteResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_route

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_route.get_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.get_route_request.GetRouteRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "route_identifier": route_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        service_identifier: "capo_migration_hub_refactor_spaces.types.service_id.ServiceId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.get_service_response.GetServiceResponse":
        """<p>Gets an Amazon Web Services Migration Hub Refactor Spaces service. </p>

        Args:
            environment_identifier: <p>The ID of the environment.</p>
            application_identifier: <p>The ID of the application.</p>
            service_identifier: <p>The ID of the service.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.get_service_response.GetServiceResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_service

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.get_service_request.GetServiceRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "service_identifier": service_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_applications(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists all the Amazon Web Services Migration Hub Refactor Spaces applications within an environment. </p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_applications

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.list_applications_request.ListApplicationsRequest = {
            "environment_identifier": environment_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_applications(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_migration_hub_refactor_spaces.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = self.list_applications(
                environment_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("application_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_environments(
        self,
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.list_environments_response.ListEnvironmentsResponse":
        """<p>Lists Amazon Web Services Migration Hub Refactor Spaces environments owned by a caller account or shared with the caller account. </p>

        Args:
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.list_environments_request.ListEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.list_environments_response.ListEnvironmentsResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_environments

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_environments.list_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.list_environments_request.ListEnvironmentsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_environments(
        self,
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_migration_hub_refactor_spaces.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = self.list_environments(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environment_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_environment_vpcs(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.list_environment_vpcs_response.ListEnvironmentVpcsResponse":
        """<p>Lists all Amazon Web Services Migration Hub Refactor Spaces service virtual private clouds (VPCs) that are part of the environment. </p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.list_environment_vpcs_request.ListEnvironmentVpcsRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.list_environment_vpcs_response.ListEnvironmentVpcsResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_environment_vpcs

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_environment_vpcs.list_environment_vpcs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.list_environment_vpcs_request.ListEnvironmentVpcsRequest = {
            "environment_identifier": environment_identifier
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_environment_vpcs(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_migration_hub_refactor_spaces.types.environment_vpc.EnvironmentVpc]":
        _token = next_token
        while True:
            _response = self.list_environment_vpcs(
                environment_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environment_vpc_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_routes(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.list_routes_response.ListRoutesResponse":
        """<p>Lists all the Amazon Web Services Migration Hub Refactor Spaces routes within an application. </p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>
            application_identifier: <p>The ID of the application. </p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.list_routes_request.ListRoutesRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.list_routes_response.ListRoutesResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_routes

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_routes.list_routes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.list_routes_request.ListRoutesRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_routes(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "Iterator[capo_migration_hub_refactor_spaces.types.route_summary.RouteSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_routes(
                environment_identifier,
                application_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("route_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.list_services_response.ListServicesResponse":
        """<p>Lists all the Amazon Web Services Migration Hub Refactor Spaces services within an application. </p>

        Args:
            environment_identifier: <p>The ID of the environment. </p>
            application_identifier: <p>The ID of the application. </p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.list_services_response.ListServicesResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_services

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.list_services_request.ListServicesRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_services(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
        next_token: Optional[
            "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_migration_hub_refactor_spaces.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_migration_hub_refactor_spaces.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_services(
                environment_identifier,
                application_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("service_summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_migration_hub_refactor_spaces.types.string.String",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags of a resource. The caller account must be the same as the resource’s <code>OwnerAccountId</code>. Listing tags in other accounts is not supported. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_tags_for_resource

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn",
        policy: "capo_migration_hub_refactor_spaces.types.policy_string.PolicyString",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Attaches a resource-based permission policy to the Amazon Web Services Migration Hub Refactor Spaces environment. The policy must contain the same actions and condition statements as the <code>arn:aws:ram::aws:permission/AWSRAMDefaultPermissionRefactorSpacesEnvironment</code> permission in Resource Access Manager. The policy must not contain new lines or blank lines. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which the policy is being attached. </p>
            policy: <p>A JSON-formatted string for an Amazon Web Services resource-based policy. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.invalid_resource_policy_exception.InvalidResourcePolicyException: <p>The resource policy is not valid.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.put_resource_policy

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.put_resource_policy_request.PutResourcePolicyRequest = {
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
        resource_arn: "capo_migration_hub_refactor_spaces.types.string.String",
        tags: "capo_migration_hub_refactor_spaces.types.tag_map.TagMap",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.tag_resource_response.TagResourceResponse":
        """<p>Removes the tags of a given resource. Tags are metadata which can be used to manage a resource. To tag a resource, the caller account must be the same as the resource’s <code>OwnerAccountId</code>. Tagging resources in other accounts is not supported.</p> <note> <p>Amazon Web Services Migration Hub Refactor Spaces does not propagate tags to orchestrated resources, such as an environment’s transit gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The new or modified tags for the resource.</p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.tag_resource

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_migration_hub_refactor_spaces.types.string.String",
        tag_keys: "capo_migration_hub_refactor_spaces.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.untag_resource_response.UntagResourceResponse":
        """<p>Adds to or modifies the tags of the given resource. Tags are metadata which can be used to manage a resource. To untag a resource, the caller account must be the same as the resource’s <code>OwnerAccountId</code>. Untagging resources across accounts is not supported. </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource. </p>
            tag_keys: <p>The list of keys of the tags to be removed from the resource. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.untag_resource

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.untag_resource_request.UntagResourceRequest = {
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

    def update_route(
        self,
        environment_identifier: "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId",
        application_identifier: "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId",
        route_identifier: "capo_migration_hub_refactor_spaces.types.route_id.RouteId",
        activation_state: "capo_migration_hub_refactor_spaces.types.route_activation_state.RouteActivationState",
        *,
        config_overrides: Optional[MigrationHubRefactorSpacesClientConfig] = None,
    ) -> "capo_migration_hub_refactor_spaces.types.update_route_response.UpdateRouteResponse":
        """<p> Updates an Amazon Web Services Migration Hub Refactor Spaces route. </p>

        Args:
            environment_identifier: <p> The ID of the environment in which the route is being updated. </p>
            application_identifier: <p> The ID of the application within which the route is being updated. </p>
            route_identifier: <p> The unique identifier of the route to update. </p>
            activation_state: <p> If set to <code>ACTIVE</code>, traffic is forwarded to this route’s service after the route is updated. </p>

        Raises:
            capo_migration_hub_refactor_spaces.errors.access_denied_exception.AccessDeniedException: <p>The user does not have sufficient access to perform this action. </p>
            capo_migration_hub_refactor_spaces.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_migration_hub_refactor_spaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist. </p>
            capo_migration_hub_refactor_spaces.errors.throttling_exception.ThrottlingException: <p>Request was denied because the request was throttled. </p>
            capo_migration_hub_refactor_spaces.errors.validation_exception.ValidationException: <p>The input does not satisfy the constraints specified by an Amazon Web Service. </p>
            capo_migration_hub_refactor_spaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_migration_hub_refactor_spaces.types.update_route_request.UpdateRouteRequest]",
        ) -> OperationResponse[
            "capo_migration_hub_refactor_spaces.types.update_route_response.UpdateRouteResponse"
        ]:
            import capo_migration_hub_refactor_spaces._operations.refactor_spaces.update_route

            output, http_response = (
                capo_migration_hub_refactor_spaces._operations.refactor_spaces.update_route.update_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_migration_hub_refactor_spaces.types.update_route_request.UpdateRouteRequest = {
            "environment_identifier": environment_identifier,
            "application_identifier": application_identifier,
            "route_identifier": route_identifier,
            "activation_state": activation_state,
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
