"""Generated from Smithy shape ``com.amazonaws.appmesh#AppMesh``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_app_mesh._auth._signers
import capo_app_mesh._auth._sigv4
from capo_app_mesh._auth._identity import Credentials
from capo_app_mesh._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_app_mesh._auth._zapros_handler import AuthMiddleware
from capo_app_mesh._pagination import resolve_path as _resolve_path
from capo_app_mesh._resources.app_mesh.mesh import Mesh
from capo_app_mesh._services._aws_config import aws_config
from capo_app_mesh._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_app_mesh.types.account_id
    import capo_app_mesh.types.arn
    import capo_app_mesh.types.create_gateway_route_input
    import capo_app_mesh.types.create_gateway_route_output
    import capo_app_mesh.types.create_mesh_input
    import capo_app_mesh.types.create_mesh_output
    import capo_app_mesh.types.create_route_input
    import capo_app_mesh.types.create_route_output
    import capo_app_mesh.types.create_virtual_gateway_input
    import capo_app_mesh.types.create_virtual_gateway_output
    import capo_app_mesh.types.create_virtual_node_input
    import capo_app_mesh.types.create_virtual_node_output
    import capo_app_mesh.types.create_virtual_router_input
    import capo_app_mesh.types.create_virtual_router_output
    import capo_app_mesh.types.create_virtual_service_input
    import capo_app_mesh.types.create_virtual_service_output
    import capo_app_mesh.types.delete_gateway_route_input
    import capo_app_mesh.types.delete_gateway_route_output
    import capo_app_mesh.types.delete_mesh_input
    import capo_app_mesh.types.delete_mesh_output
    import capo_app_mesh.types.delete_route_input
    import capo_app_mesh.types.delete_route_output
    import capo_app_mesh.types.delete_virtual_gateway_input
    import capo_app_mesh.types.delete_virtual_gateway_output
    import capo_app_mesh.types.delete_virtual_node_input
    import capo_app_mesh.types.delete_virtual_node_output
    import capo_app_mesh.types.delete_virtual_router_input
    import capo_app_mesh.types.delete_virtual_router_output
    import capo_app_mesh.types.delete_virtual_service_input
    import capo_app_mesh.types.delete_virtual_service_output
    import capo_app_mesh.types.describe_gateway_route_input
    import capo_app_mesh.types.describe_gateway_route_output
    import capo_app_mesh.types.describe_mesh_input
    import capo_app_mesh.types.describe_mesh_output
    import capo_app_mesh.types.describe_route_input
    import capo_app_mesh.types.describe_route_output
    import capo_app_mesh.types.describe_virtual_gateway_input
    import capo_app_mesh.types.describe_virtual_gateway_output
    import capo_app_mesh.types.describe_virtual_node_input
    import capo_app_mesh.types.describe_virtual_node_output
    import capo_app_mesh.types.describe_virtual_router_input
    import capo_app_mesh.types.describe_virtual_router_output
    import capo_app_mesh.types.describe_virtual_service_input
    import capo_app_mesh.types.describe_virtual_service_output
    import capo_app_mesh.types.gateway_route_ref
    import capo_app_mesh.types.gateway_route_spec
    import capo_app_mesh.types.list_gateway_routes_input
    import capo_app_mesh.types.list_gateway_routes_limit
    import capo_app_mesh.types.list_gateway_routes_output
    import capo_app_mesh.types.list_meshes_input
    import capo_app_mesh.types.list_meshes_limit
    import capo_app_mesh.types.list_meshes_output
    import capo_app_mesh.types.list_routes_input
    import capo_app_mesh.types.list_routes_limit
    import capo_app_mesh.types.list_routes_output
    import capo_app_mesh.types.list_tags_for_resource_input
    import capo_app_mesh.types.list_tags_for_resource_output
    import capo_app_mesh.types.list_virtual_gateways_input
    import capo_app_mesh.types.list_virtual_gateways_limit
    import capo_app_mesh.types.list_virtual_gateways_output
    import capo_app_mesh.types.list_virtual_nodes_input
    import capo_app_mesh.types.list_virtual_nodes_limit
    import capo_app_mesh.types.list_virtual_nodes_output
    import capo_app_mesh.types.list_virtual_routers_input
    import capo_app_mesh.types.list_virtual_routers_limit
    import capo_app_mesh.types.list_virtual_routers_output
    import capo_app_mesh.types.list_virtual_services_input
    import capo_app_mesh.types.list_virtual_services_limit
    import capo_app_mesh.types.list_virtual_services_output
    import capo_app_mesh.types.mesh_ref
    import capo_app_mesh.types.mesh_spec
    import capo_app_mesh.types.resource_name
    import capo_app_mesh.types.route_ref
    import capo_app_mesh.types.route_spec
    import capo_app_mesh.types.service_name
    import capo_app_mesh.types.tag_key_list
    import capo_app_mesh.types.tag_list
    import capo_app_mesh.types.tag_ref
    import capo_app_mesh.types.tag_resource_input
    import capo_app_mesh.types.tag_resource_output
    import capo_app_mesh.types.tags_limit
    import capo_app_mesh.types.untag_resource_input
    import capo_app_mesh.types.untag_resource_output
    import capo_app_mesh.types.update_gateway_route_input
    import capo_app_mesh.types.update_gateway_route_output
    import capo_app_mesh.types.update_mesh_input
    import capo_app_mesh.types.update_mesh_output
    import capo_app_mesh.types.update_route_input
    import capo_app_mesh.types.update_route_output
    import capo_app_mesh.types.update_virtual_gateway_input
    import capo_app_mesh.types.update_virtual_gateway_output
    import capo_app_mesh.types.update_virtual_node_input
    import capo_app_mesh.types.update_virtual_node_output
    import capo_app_mesh.types.update_virtual_router_input
    import capo_app_mesh.types.update_virtual_router_output
    import capo_app_mesh.types.update_virtual_service_input
    import capo_app_mesh.types.update_virtual_service_output
    import capo_app_mesh.types.virtual_gateway_ref
    import capo_app_mesh.types.virtual_gateway_spec
    import capo_app_mesh.types.virtual_node_ref
    import capo_app_mesh.types.virtual_node_spec
    import capo_app_mesh.types.virtual_router_ref
    import capo_app_mesh.types.virtual_router_spec
    import capo_app_mesh.types.virtual_service_ref
    import capo_app_mesh.types.virtual_service_spec


class AppMeshClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AppMeshClient:
    """A client for the ``AppMesh`` service.

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
        self._config = AppMeshClientConfig(
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

        # resources
        self.mesh = Mesh(self)

    def operation_options(
        self, config_overrides: Optional[AppMeshClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppMeshClientConfig = config_overrides or {}
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_app_mesh.types.arn.Arn",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.tags_limit.TagsLimit"] = None,
    ) -> "capo_app_mesh.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List the tags for an App Mesh resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListTagsForResource</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of tag results returned by <code>ListTagsForResource</code> in paginated output. When this parameter is used, <code>ListTagsForResource</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListTagsForResource</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListTagsForResource</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_tags_for_resource

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_app_mesh.types.arn.Arn",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.tags_limit.TagsLimit"] = None,
    ) -> "Iterator[capo_app_mesh.types.tag_ref.TagRef]":
        _token = next_token
        while True:
            _response = self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def tag_resource(
        self,
        resource_arn: "capo_app_mesh.types.arn.Arn",
        tags: "capo_app_mesh.types.tag_list.TagList",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.tag_resource_output.TagResourceOutput":
        """<p>Associates the specified tags to a resource with the specified <code>resourceArn</code>. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags associated with that resource are also deleted.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to add tags to.</p>
            tags: <p>The tags to add to the resource. A tag is an array of key-value pairs. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.too_many_tags_exception.TooManyTagsException: <p>The request exceeds the maximum allowed number of tags allowed per resource. The current limit is 50 user tags per resource. You must reduce the number of tags in the request. None of the tags in this request were applied.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.tag_resource

            output, http_response = (
                capo_app_mesh._operations.app_mesh.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.tag_resource_input.TagResourceInput = {
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
        resource_arn: "capo_app_mesh.types.arn.Arn",
        tag_keys: "capo_app_mesh.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.untag_resource_output.UntagResourceOutput":
        """<p>Deletes specified tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to delete tags from.</p>
            tag_keys: <p>The keys of the tags to be removed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.untag_resource

            output, http_response = (
                capo_app_mesh._operations.app_mesh.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.untag_resource_input.UntagResourceInput = {
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

    def create_mesh(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        spec: Optional["capo_app_mesh.types.mesh_spec.MeshSpec"] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_app_mesh.types.create_mesh_output.CreateMeshOutput":
        """<p>Creates a service mesh.</p> <p> A service mesh is a logical boundary for network traffic between services that are represented by resources within the mesh. After you create your service mesh, you can create virtual services, virtual nodes, virtual routers, and routes to distribute traffic between the applications in your mesh.</p> <p>For more information about service meshes, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html">Service meshes</a>.</p>

        Args:
            mesh_name: <p>The name to use for the service mesh.</p>
            spec: <p>The service mesh specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_mesh_input.CreateMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_mesh_output.CreateMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_mesh.create_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_mesh_input.CreateMeshInput = {
            "mesh_name": mesh_name
        }
        if spec is not None:
            input_["spec"] = spec
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

    def describe_mesh(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_mesh_output.DescribeMeshOutput":
        """<p>Describes an existing service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to describe.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_mesh_input.DescribeMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_mesh_output.DescribeMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_mesh.describe_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_mesh_input.DescribeMeshInput = {
            "mesh_name": mesh_name
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_mesh(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        spec: Optional["capo_app_mesh.types.mesh_spec.MeshSpec"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_app_mesh.types.update_mesh_output.UpdateMeshOutput":
        """<p>Updates an existing service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to update.</p>
            spec: <p>The service mesh specification to apply.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_mesh_input.UpdateMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_mesh_output.UpdateMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_mesh.update_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_mesh_input.UpdateMeshInput = {
            "mesh_name": mesh_name
        }
        if spec is not None:
            input_["spec"] = spec
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

    def delete_mesh(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
    ) -> "capo_app_mesh.types.delete_mesh_output.DeleteMeshOutput":
        """<p>Deletes an existing service mesh.</p> <p>You must delete all resources (virtual services, routes, virtual routers, and virtual nodes) in the service mesh before you can delete the mesh itself.</p>

        Args:
            mesh_name: <p>The name of the service mesh to delete.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_mesh_input.DeleteMeshInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_mesh_output.DeleteMeshOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_mesh

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_mesh.delete_mesh(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_mesh_input.DeleteMeshInput = {
            "mesh_name": mesh_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_meshes(
        self,
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.list_meshes_limit.ListMeshesLimit"] = None,
    ) -> "capo_app_mesh.types.list_meshes_output.ListMeshesOutput":
        """<p>Returns a list of existing service meshes.</p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListMeshes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            limit: <p>The maximum number of results returned by <code>ListMeshes</code> in paginated output. When you use this parameter, <code>ListMeshes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListMeshes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_meshes_input.ListMeshesInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_meshes_output.ListMeshesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_meshes

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_meshes.list_meshes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_meshes_input.ListMeshesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_meshes(
        self,
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.list_meshes_limit.ListMeshesLimit"] = None,
    ) -> "Iterator[capo_app_mesh.types.mesh_ref.MeshRef]":
        _token = next_token
        while True:
            _response = self.list_meshes(
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("meshes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_virtual_gateway(
        self,
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_gateway_spec.VirtualGatewaySpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.create_virtual_gateway_output.CreateVirtualGatewayOutput":
        """<p>Creates a virtual gateway.</p> <p>A virtual gateway allows resources outside your mesh to communicate to resources that are inside your mesh. The virtual gateway represents an Envoy proxy running in an Amazon ECS task, in a Kubernetes service, or on an Amazon EC2 instance. Unlike a virtual node, which represents an Envoy running with an application, a virtual gateway represents Envoy deployed by itself.</p> <p>For more information about virtual gateways, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html">Virtual gateways</a>. </p>

        Args:
            virtual_gateway_name: <p>The name to use for the virtual gateway.</p>
            mesh_name: <p>The name of the service mesh to create the virtual gateway in.</p>
            spec: <p>The virtual gateway specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the virtual gateway to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_virtual_gateway_input.CreateVirtualGatewayInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_virtual_gateway_output.CreateVirtualGatewayOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_virtual_gateway

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_virtual_gateway.create_virtual_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_virtual_gateway_input.CreateVirtualGatewayInput = {
            "virtual_gateway_name": virtual_gateway_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_virtual_gateway(
        self,
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_virtual_gateway_output.DescribeVirtualGatewayOutput":
        """<p>Describes an existing virtual gateway.</p>

        Args:
            virtual_gateway_name: <p>The name of the virtual gateway to describe.</p>
            mesh_name: <p>The name of the service mesh that the gateway route resides in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_virtual_gateway_input.DescribeVirtualGatewayInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_virtual_gateway_output.DescribeVirtualGatewayOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_virtual_gateway

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_virtual_gateway.describe_virtual_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_virtual_gateway_input.DescribeVirtualGatewayInput = {
            "virtual_gateway_name": virtual_gateway_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_virtual_gateway(
        self,
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_gateway_spec.VirtualGatewaySpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.update_virtual_gateway_output.UpdateVirtualGatewayOutput":
        """<p>Updates an existing virtual gateway in a specified service mesh.</p>

        Args:
            virtual_gateway_name: <p>The name of the virtual gateway to update.</p>
            mesh_name: <p>The name of the service mesh that the virtual gateway resides in.</p>
            spec: <p>The new virtual gateway specification to apply. This overwrites the existing data.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_virtual_gateway_input.UpdateVirtualGatewayInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_virtual_gateway_output.UpdateVirtualGatewayOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_virtual_gateway

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_virtual_gateway.update_virtual_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_virtual_gateway_input.UpdateVirtualGatewayInput = {
            "virtual_gateway_name": virtual_gateway_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_virtual_gateway(
        self,
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.delete_virtual_gateway_output.DeleteVirtualGatewayOutput":
        """<p>Deletes an existing virtual gateway. You cannot delete a virtual gateway if any gateway routes are associated to it.</p>

        Args:
            virtual_gateway_name: <p>The name of the virtual gateway to delete.</p>
            mesh_name: <p>The name of the service mesh to delete the virtual gateway from.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_virtual_gateway_input.DeleteVirtualGatewayInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_virtual_gateway_output.DeleteVirtualGatewayOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_virtual_gateway

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_virtual_gateway.delete_virtual_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_virtual_gateway_input.DeleteVirtualGatewayInput = {
            "virtual_gateway_name": virtual_gateway_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_virtual_gateways(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_gateways_limit.ListVirtualGatewaysLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.list_virtual_gateways_output.ListVirtualGatewaysOutput":
        """<p>Returns a list of existing virtual gateways in a service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to list virtual gateways in.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualGateways</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of results returned by <code>ListVirtualGateways</code> in paginated output. When you use this parameter, <code>ListVirtualGateways</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualGateways</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualGateways</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_virtual_gateways_input.ListVirtualGatewaysInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_virtual_gateways_output.ListVirtualGatewaysOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_virtual_gateways

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_virtual_gateways.list_virtual_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_virtual_gateways_input.ListVirtualGatewaysInput = {
            "mesh_name": mesh_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_virtual_gateways(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_gateways_limit.ListVirtualGatewaysLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_app_mesh.types.virtual_gateway_ref.VirtualGatewayRef]":
        _token = next_token
        while True:
            _response = self.list_virtual_gateways(
                mesh_name,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
                mesh_owner=mesh_owner,
            )
            _page = _resolve_path(_response, ("virtual_gateways",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_gateway_route(
        self,
        gateway_route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.gateway_route_spec.GatewayRouteSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.create_gateway_route_output.CreateGatewayRouteOutput":
        """<p>Creates a gateway route.</p> <p>A gateway route is attached to a virtual gateway and routes traffic to an existing virtual service. If a route matches a request, it can distribute traffic to a target virtual service.</p> <p>For more information about gateway routes, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/gateway-routes.html">Gateway routes</a>.</p>

        Args:
            gateway_route_name: <p>The name to use for the gateway route.</p>
            mesh_name: <p>The name of the service mesh to create the gateway route in.</p>
            virtual_gateway_name: <p>The name of the virtual gateway to associate the gateway route with. If the virtual gateway is in a shared mesh, then you must be the owner of the virtual gateway resource.</p>
            spec: <p>The gateway route specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the gateway route to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_gateway_route_input.CreateGatewayRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_gateway_route_output.CreateGatewayRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_gateway_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_gateway_route.create_gateway_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_gateway_route_input.CreateGatewayRouteInput = {
            "gateway_route_name": gateway_route_name,
            "mesh_name": mesh_name,
            "virtual_gateway_name": virtual_gateway_name,
            "spec": spec,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_gateway_route(
        self,
        gateway_route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_gateway_route_output.DescribeGatewayRouteOutput":
        """<p>Describes an existing gateway route.</p>

        Args:
            gateway_route_name: <p>The name of the gateway route to describe.</p>
            mesh_name: <p>The name of the service mesh that the gateway route resides in.</p>
            virtual_gateway_name: <p>The name of the virtual gateway that the gateway route is associated with.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_gateway_route_input.DescribeGatewayRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_gateway_route_output.DescribeGatewayRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_gateway_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_gateway_route.describe_gateway_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_gateway_route_input.DescribeGatewayRouteInput = {
            "gateway_route_name": gateway_route_name,
            "mesh_name": mesh_name,
            "virtual_gateway_name": virtual_gateway_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_route(
        self,
        gateway_route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.gateway_route_spec.GatewayRouteSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.update_gateway_route_output.UpdateGatewayRouteOutput":
        """<p>Updates an existing gateway route that is associated to a specified virtual gateway in a service mesh.</p>

        Args:
            gateway_route_name: <p>The name of the gateway route to update.</p>
            mesh_name: <p>The name of the service mesh that the gateway route resides in.</p>
            virtual_gateway_name: <p>The name of the virtual gateway that the gateway route is associated with.</p>
            spec: <p>The new gateway route specification to apply. This overwrites the existing data.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_gateway_route_input.UpdateGatewayRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_gateway_route_output.UpdateGatewayRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_gateway_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_gateway_route.update_gateway_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_gateway_route_input.UpdateGatewayRouteInput = {
            "gateway_route_name": gateway_route_name,
            "mesh_name": mesh_name,
            "virtual_gateway_name": virtual_gateway_name,
            "spec": spec,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_route(
        self,
        gateway_route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.delete_gateway_route_output.DeleteGatewayRouteOutput":
        """<p>Deletes an existing gateway route.</p>

        Args:
            gateway_route_name: <p>The name of the gateway route to delete.</p>
            mesh_name: <p>The name of the service mesh to delete the gateway route from.</p>
            virtual_gateway_name: <p>The name of the virtual gateway to delete the route from.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_gateway_route_input.DeleteGatewayRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_gateway_route_output.DeleteGatewayRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_gateway_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_gateway_route.delete_gateway_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_gateway_route_input.DeleteGatewayRouteInput = {
            "gateway_route_name": gateway_route_name,
            "mesh_name": mesh_name,
            "virtual_gateway_name": virtual_gateway_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_routes(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_gateway_routes_limit.ListGatewayRoutesLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.list_gateway_routes_output.ListGatewayRoutesOutput":
        """<p>Returns a list of existing gateway routes that are associated to a virtual gateway.</p>

        Args:
            mesh_name: <p>The name of the service mesh to list gateway routes in.</p>
            virtual_gateway_name: <p>The name of the virtual gateway to list gateway routes in.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListGatewayRoutes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of results returned by <code>ListGatewayRoutes</code> in paginated output. When you use this parameter, <code>ListGatewayRoutes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListGatewayRoutes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListGatewayRoutes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_gateway_routes_input.ListGatewayRoutesInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_gateway_routes_output.ListGatewayRoutesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_gateway_routes

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_gateway_routes.list_gateway_routes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_gateway_routes_input.ListGatewayRoutesInput = {
            "mesh_name": mesh_name,
            "virtual_gateway_name": virtual_gateway_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_gateway_routes(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_gateway_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_gateway_routes_limit.ListGatewayRoutesLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_app_mesh.types.gateway_route_ref.GatewayRouteRef]":
        _token = next_token
        while True:
            _response = self.list_gateway_routes(
                mesh_name,
                virtual_gateway_name,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
                mesh_owner=mesh_owner,
            )
            _page = _resolve_path(_response, ("gateway_routes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_virtual_node(
        self,
        virtual_node_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_node_spec.VirtualNodeSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.create_virtual_node_output.CreateVirtualNodeOutput":
        """<p>Creates a virtual node within a service mesh.</p> <p> A virtual node acts as a logical pointer to a particular task group, such as an Amazon ECS service or a Kubernetes deployment. When you create a virtual node, you can specify the service discovery information for your task group, and whether the proxy running in a task group will communicate with other proxies using Transport Layer Security (TLS).</p> <p>You define a <code>listener</code> for any inbound traffic that your virtual node expects. Any virtual service that your virtual node expects to communicate to is specified as a <code>backend</code>.</p> <p>The response metadata for your new virtual node contains the <code>arn</code> that is associated with the virtual node. Set this value to the full ARN; for example, <code>arn:aws:appmesh:us-west-2:123456789012:myMesh/default/virtualNode/myApp</code>) as the <code>APPMESH_RESOURCE_ARN</code> environment variable for your task group's Envoy proxy container in your task definition or pod spec. This is then mapped to the <code>node.id</code> and <code>node.cluster</code> Envoy parameters.</p> <note> <p>By default, App Mesh uses the name of the resource you specified in <code>APPMESH_RESOURCE_ARN</code> when Envoy is referring to itself in metrics and traces. You can override this behavior by setting the <code>APPMESH_RESOURCE_CLUSTER</code> environment variable with your own name.</p> </note> <p>For more information about virtual nodes, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html">Virtual nodes</a>. You must be using <code>1.15.0</code> or later of the Envoy image when setting these variables. For more information aboutApp Mesh Envoy variables, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy.html">Envoy image</a> in the App Mesh User Guide.</p>

        Args:
            virtual_node_name: <p>The name to use for the virtual node.</p>
            mesh_name: <p>The name of the service mesh to create the virtual node in.</p>
            spec: <p>The virtual node specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the virtual node to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_virtual_node_input.CreateVirtualNodeInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_virtual_node_output.CreateVirtualNodeOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_virtual_node

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_virtual_node.create_virtual_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_virtual_node_input.CreateVirtualNodeInput = {
            "virtual_node_name": virtual_node_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_virtual_node(
        self,
        virtual_node_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_virtual_node_output.DescribeVirtualNodeOutput":
        """<p>Describes an existing virtual node.</p>

        Args:
            virtual_node_name: <p>The name of the virtual node to describe.</p>
            mesh_name: <p>The name of the service mesh that the virtual node resides in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_virtual_node_input.DescribeVirtualNodeInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_virtual_node_output.DescribeVirtualNodeOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_virtual_node

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_virtual_node.describe_virtual_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_virtual_node_input.DescribeVirtualNodeInput = {
            "virtual_node_name": virtual_node_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_virtual_node(
        self,
        virtual_node_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_node_spec.VirtualNodeSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.update_virtual_node_output.UpdateVirtualNodeOutput":
        """<p>Updates an existing virtual node in a specified service mesh.</p>

        Args:
            virtual_node_name: <p>The name of the virtual node to update.</p>
            mesh_name: <p>The name of the service mesh that the virtual node resides in.</p>
            spec: <p>The new virtual node specification to apply. This overwrites the existing data.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_virtual_node_input.UpdateVirtualNodeInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_virtual_node_output.UpdateVirtualNodeOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_virtual_node

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_virtual_node.update_virtual_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_virtual_node_input.UpdateVirtualNodeInput = {
            "virtual_node_name": virtual_node_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_virtual_node(
        self,
        virtual_node_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.delete_virtual_node_output.DeleteVirtualNodeOutput":
        """<p>Deletes an existing virtual node.</p> <p>You must delete any virtual services that list a virtual node as a service provider before you can delete the virtual node itself.</p>

        Args:
            virtual_node_name: <p>The name of the virtual node to delete.</p>
            mesh_name: <p>The name of the service mesh to delete the virtual node in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_virtual_node_input.DeleteVirtualNodeInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_virtual_node_output.DeleteVirtualNodeOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_virtual_node

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_virtual_node.delete_virtual_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_virtual_node_input.DeleteVirtualNodeInput = {
            "virtual_node_name": virtual_node_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_virtual_nodes(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_nodes_limit.ListVirtualNodesLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.list_virtual_nodes_output.ListVirtualNodesOutput":
        """<p>Returns a list of existing virtual nodes.</p>

        Args:
            mesh_name: <p>The name of the service mesh to list virtual nodes in.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualNodes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of results returned by <code>ListVirtualNodes</code> in paginated output. When you use this parameter, <code>ListVirtualNodes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualNodes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualNodes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_virtual_nodes_input.ListVirtualNodesInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_virtual_nodes_output.ListVirtualNodesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_virtual_nodes

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_virtual_nodes.list_virtual_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_virtual_nodes_input.ListVirtualNodesInput = {
            "mesh_name": mesh_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_virtual_nodes(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_nodes_limit.ListVirtualNodesLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_app_mesh.types.virtual_node_ref.VirtualNodeRef]":
        _token = next_token
        while True:
            _response = self.list_virtual_nodes(
                mesh_name,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
                mesh_owner=mesh_owner,
            )
            _page = _resolve_path(_response, ("virtual_nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_virtual_router(
        self,
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_router_spec.VirtualRouterSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.create_virtual_router_output.CreateVirtualRouterOutput":
        """<p>Creates a virtual router within a service mesh.</p> <p>Specify a <code>listener</code> for any inbound traffic that your virtual router receives. Create a virtual router for each protocol and port that you need to route. Virtual routers handle traffic for one or more virtual services within your mesh. After you create your virtual router, create and associate routes for your virtual router that direct incoming requests to different virtual nodes.</p> <p>For more information about virtual routers, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html">Virtual routers</a>.</p>

        Args:
            virtual_router_name: <p>The name to use for the virtual router.</p>
            mesh_name: <p>The name of the service mesh to create the virtual router in.</p>
            spec: <p>The virtual router specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the virtual router to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_virtual_router_input.CreateVirtualRouterInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_virtual_router_output.CreateVirtualRouterOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_virtual_router

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_virtual_router.create_virtual_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_virtual_router_input.CreateVirtualRouterInput = {
            "virtual_router_name": virtual_router_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_virtual_router(
        self,
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> (
        "capo_app_mesh.types.describe_virtual_router_output.DescribeVirtualRouterOutput"
    ):
        """<p>Describes an existing virtual router.</p>

        Args:
            virtual_router_name: <p>The name of the virtual router to describe.</p>
            mesh_name: <p>The name of the service mesh that the virtual router resides in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_virtual_router_input.DescribeVirtualRouterInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_virtual_router_output.DescribeVirtualRouterOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_virtual_router

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_virtual_router.describe_virtual_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_virtual_router_input.DescribeVirtualRouterInput = {
            "virtual_router_name": virtual_router_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_virtual_router(
        self,
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_router_spec.VirtualRouterSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.update_virtual_router_output.UpdateVirtualRouterOutput":
        """<p>Updates an existing virtual router in a specified service mesh.</p>

        Args:
            virtual_router_name: <p>The name of the virtual router to update.</p>
            mesh_name: <p>The name of the service mesh that the virtual router resides in.</p>
            spec: <p>The new virtual router specification to apply. This overwrites the existing data.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_virtual_router_input.UpdateVirtualRouterInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_virtual_router_output.UpdateVirtualRouterOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_virtual_router

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_virtual_router.update_virtual_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_virtual_router_input.UpdateVirtualRouterInput = {
            "virtual_router_name": virtual_router_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_virtual_router(
        self,
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.delete_virtual_router_output.DeleteVirtualRouterOutput":
        """<p>Deletes an existing virtual router.</p> <p>You must delete any routes associated with the virtual router before you can delete the router itself.</p>

        Args:
            virtual_router_name: <p>The name of the virtual router to delete.</p>
            mesh_name: <p>The name of the service mesh to delete the virtual router in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_virtual_router_input.DeleteVirtualRouterInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_virtual_router_output.DeleteVirtualRouterOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_virtual_router

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_virtual_router.delete_virtual_router(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_virtual_router_input.DeleteVirtualRouterInput = {
            "virtual_router_name": virtual_router_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_virtual_routers(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_routers_limit.ListVirtualRoutersLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.list_virtual_routers_output.ListVirtualRoutersOutput":
        """<p>Returns a list of existing virtual routers in a service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to list virtual routers in.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualRouters</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of results returned by <code>ListVirtualRouters</code> in paginated output. When you use this parameter, <code>ListVirtualRouters</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualRouters</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualRouters</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_virtual_routers_input.ListVirtualRoutersInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_virtual_routers_output.ListVirtualRoutersOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_virtual_routers

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_virtual_routers.list_virtual_routers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_virtual_routers_input.ListVirtualRoutersInput = {
            "mesh_name": mesh_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_virtual_routers(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_routers_limit.ListVirtualRoutersLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_app_mesh.types.virtual_router_ref.VirtualRouterRef]":
        _token = next_token
        while True:
            _response = self.list_virtual_routers(
                mesh_name,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
                mesh_owner=mesh_owner,
            )
            _page = _resolve_path(_response, ("virtual_routers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_route(
        self,
        route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.route_spec.RouteSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.create_route_output.CreateRouteOutput":
        """<p>Creates a route that is associated with a virtual router.</p> <p> You can route several different protocols and define a retry policy for a route. Traffic can be routed to one or more virtual nodes.</p> <p>For more information about routes, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html">Routes</a>.</p>

        Args:
            route_name: <p>The name to use for the route.</p>
            mesh_name: <p>The name of the service mesh to create the route in.</p>
            virtual_router_name: <p>The name of the virtual router in which to create the route. If the virtual router is in a shared mesh, then you must be the owner of the virtual router resource.</p>
            spec: <p>The route specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the route to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_route_input.CreateRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_route_output.CreateRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_route.create_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_route_input.CreateRouteInput = {
            "route_name": route_name,
            "mesh_name": mesh_name,
            "virtual_router_name": virtual_router_name,
            "spec": spec,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_route(
        self,
        route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_route_output.DescribeRouteOutput":
        """<p>Describes an existing route.</p>

        Args:
            route_name: <p>The name of the route to describe.</p>
            mesh_name: <p>The name of the service mesh that the route resides in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>
            virtual_router_name: <p>The name of the virtual router that the route is associated with.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_route_input.DescribeRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_route_output.DescribeRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_route.describe_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_route_input.DescribeRouteInput = {
            "route_name": route_name,
            "mesh_name": mesh_name,
            "virtual_router_name": virtual_router_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_route(
        self,
        route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.route_spec.RouteSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.update_route_output.UpdateRouteOutput":
        """<p>Updates an existing route for a specified service mesh and virtual router.</p>

        Args:
            route_name: <p>The name of the route to update.</p>
            mesh_name: <p>The name of the service mesh that the route resides in.</p>
            virtual_router_name: <p>The name of the virtual router that the route is associated with.</p>
            spec: <p>The new route specification to apply. This overwrites the existing data.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_route_input.UpdateRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_route_output.UpdateRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_route.update_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_route_input.UpdateRouteInput = {
            "route_name": route_name,
            "mesh_name": mesh_name,
            "virtual_router_name": virtual_router_name,
            "spec": spec,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_route(
        self,
        route_name: "capo_app_mesh.types.resource_name.ResourceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.delete_route_output.DeleteRouteOutput":
        """<p>Deletes an existing route.</p>

        Args:
            route_name: <p>The name of the route to delete.</p>
            mesh_name: <p>The name of the service mesh to delete the route in.</p>
            virtual_router_name: <p>The name of the virtual router to delete the route in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_route_input.DeleteRouteInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_route_output.DeleteRouteOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_route

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_route.delete_route(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_route_input.DeleteRouteInput = {
            "route_name": route_name,
            "mesh_name": mesh_name,
            "virtual_router_name": virtual_router_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_routes(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.list_routes_limit.ListRoutesLimit"] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.list_routes_output.ListRoutesOutput":
        """<p>Returns a list of existing routes in a service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to list routes in.</p>
            virtual_router_name: <p>The name of the virtual router to list routes in.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListRoutes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of results returned by <code>ListRoutes</code> in paginated output. When you use this parameter, <code>ListRoutes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListRoutes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListRoutes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_routes_input.ListRoutesInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_routes_output.ListRoutesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_routes

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_routes.list_routes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_routes_input.ListRoutesInput = {
            "mesh_name": mesh_name,
            "virtual_router_name": virtual_router_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_routes(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        virtual_router_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional["capo_app_mesh.types.list_routes_limit.ListRoutesLimit"] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_app_mesh.types.route_ref.RouteRef]":
        _token = next_token
        while True:
            _response = self.list_routes(
                mesh_name,
                virtual_router_name,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
                mesh_owner=mesh_owner,
            )
            _page = _resolve_path(_response, ("routes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_virtual_service(
        self,
        virtual_service_name: "capo_app_mesh.types.service_name.ServiceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_service_spec.VirtualServiceSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        tags: Optional["capo_app_mesh.types.tag_list.TagList"] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.create_virtual_service_output.CreateVirtualServiceOutput":
        """<p>Creates a virtual service within a service mesh.</p> <p>A virtual service is an abstraction of a real service that is provided by a virtual node directly or indirectly by means of a virtual router. Dependent services call your virtual service by its <code>virtualServiceName</code>, and those requests are routed to the virtual node or virtual router that is specified as the provider for the virtual service.</p> <p>For more information about virtual services, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html">Virtual services</a>.</p>

        Args:
            virtual_service_name: <p>The name to use for the virtual service.</p>
            mesh_name: <p>The name of the service mesh to create the virtual service in.</p>
            spec: <p>The virtual service specification to apply.</p>
            tags: <p>Optional metadata that you can apply to the virtual service to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then the account that you specify must share the mesh with your account before you can create the resource in the service mesh. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.create_virtual_service_input.CreateVirtualServiceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.create_virtual_service_output.CreateVirtualServiceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.create_virtual_service

            output, http_response = (
                capo_app_mesh._operations.app_mesh.create_virtual_service.create_virtual_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.create_virtual_service_input.CreateVirtualServiceInput = {
            "virtual_service_name": virtual_service_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_virtual_service(
        self,
        virtual_service_name: "capo_app_mesh.types.service_name.ServiceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.describe_virtual_service_output.DescribeVirtualServiceOutput":
        """<p>Describes an existing virtual service.</p>

        Args:
            virtual_service_name: <p>The name of the virtual service to describe.</p>
            mesh_name: <p>The name of the service mesh that the virtual service resides in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.describe_virtual_service_input.DescribeVirtualServiceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.describe_virtual_service_output.DescribeVirtualServiceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.describe_virtual_service

            output, http_response = (
                capo_app_mesh._operations.app_mesh.describe_virtual_service.describe_virtual_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.describe_virtual_service_input.DescribeVirtualServiceInput = {
            "virtual_service_name": virtual_service_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_virtual_service(
        self,
        virtual_service_name: "capo_app_mesh.types.service_name.ServiceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        spec: "capo_app_mesh.types.virtual_service_spec.VirtualServiceSpec",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        client_token: Optional[str] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.update_virtual_service_output.UpdateVirtualServiceOutput":
        """<p>Updates an existing virtual service in a specified service mesh.</p>

        Args:
            virtual_service_name: <p>The name of the virtual service to update.</p>
            mesh_name: <p>The name of the service mesh that the virtual service resides in.</p>
            spec: <p>The new virtual service specification to apply. This overwrites the existing data.</p>
            client_token: <p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.conflict_exception.ConflictException: <p>The request contains a client token that was used for a previous update resource call with different specifications. Try the request again with a new client token.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.limit_exceeded_exception.LimitExceededException: <p>You have exceeded a service limit for your account. For more information, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/service-quotas.html">Service Limits</a> in the <i>App Mesh User Guide</i>.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.update_virtual_service_input.UpdateVirtualServiceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.update_virtual_service_output.UpdateVirtualServiceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.update_virtual_service

            output, http_response = (
                capo_app_mesh._operations.app_mesh.update_virtual_service.update_virtual_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.update_virtual_service_input.UpdateVirtualServiceInput = {
            "virtual_service_name": virtual_service_name,
            "mesh_name": mesh_name,
            "spec": spec,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_virtual_service(
        self,
        virtual_service_name: "capo_app_mesh.types.service_name.ServiceName",
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.delete_virtual_service_output.DeleteVirtualServiceOutput":
        """<p>Deletes an existing virtual service.</p>

        Args:
            virtual_service_name: <p>The name of the virtual service to delete.</p>
            mesh_name: <p>The name of the service mesh to delete the virtual service in.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.resource_in_use_exception.ResourceInUseException: <p>You can't delete the specified resource because it's in use or required by another resource.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.delete_virtual_service_input.DeleteVirtualServiceInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.delete_virtual_service_output.DeleteVirtualServiceOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.delete_virtual_service

            output, http_response = (
                capo_app_mesh._operations.app_mesh.delete_virtual_service.delete_virtual_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.delete_virtual_service_input.DeleteVirtualServiceInput = {
            "virtual_service_name": virtual_service_name,
            "mesh_name": mesh_name,
        }
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_virtual_services(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_services_limit.ListVirtualServicesLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "capo_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput":
        """<p>Returns a list of existing virtual services in a service mesh.</p>

        Args:
            mesh_name: <p>The name of the service mesh to list virtual services in.</p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListVirtualServices</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p>
            limit: <p>The maximum number of results returned by <code>ListVirtualServices</code> in paginated output. When you use this parameter, <code>ListVirtualServices</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListVirtualServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListVirtualServices</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>
            mesh_owner: <p>The Amazon Web Services IAM account ID of the service mesh owner. If the account ID is not your own, then it's the ID of the account that shared the mesh with your account. For more information about mesh sharing, see <a href="https://docs.aws.amazon.com/app-mesh/latest/userguide/sharing.html">Working with shared meshes</a>.</p>

        Raises:
            capo_app_mesh.errors.bad_request_exception.BadRequestException: <p>The request syntax was malformed. Check your request syntax and try again.</p>
            capo_app_mesh.errors.forbidden_exception.ForbiddenException: <p>You don't have permissions to perform this action.</p>
            capo_app_mesh.errors.internal_server_error_exception.InternalServerErrorException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_app_mesh.errors.not_found_exception.NotFoundException: <p>The specified resource doesn't exist. Check your request syntax and try again.</p>
            capo_app_mesh.errors.service_unavailable_exception.ServiceUnavailableException: <p>The request has failed due to a temporary failure of the service.</p>
            capo_app_mesh.errors.too_many_requests_exception.TooManyRequestsException: <p>The maximum request rate permitted by the App Mesh APIs has been exceeded for your account. For best results, use an increasing or variable sleep interval between requests.</p>
            capo_app_mesh.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_app_mesh.types.list_virtual_services_input.ListVirtualServicesInput]",
        ) -> OperationResponse[
            "capo_app_mesh.types.list_virtual_services_output.ListVirtualServicesOutput"
        ]:
            import capo_app_mesh._operations.app_mesh.list_virtual_services

            output, http_response = (
                capo_app_mesh._operations.app_mesh.list_virtual_services.list_virtual_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_app_mesh.types.list_virtual_services_input.ListVirtualServicesInput = {
            "mesh_name": mesh_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if mesh_owner is not None:
            input_["mesh_owner"] = mesh_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_virtual_services(
        self,
        mesh_name: "capo_app_mesh.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AppMeshClientConfig] = None,
        next_token: Optional[str] = None,
        limit: Optional[
            "capo_app_mesh.types.list_virtual_services_limit.ListVirtualServicesLimit"
        ] = None,
        mesh_owner: Optional["capo_app_mesh.types.account_id.AccountId"] = None,
    ) -> "Iterator[capo_app_mesh.types.virtual_service_ref.VirtualServiceRef]":
        _token = next_token
        while True:
            _response = self.list_virtual_services(
                mesh_name,
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
                mesh_owner=mesh_owner,
            )
            _page = _resolve_path(_response, ("virtual_services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
