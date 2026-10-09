"""Generated from Smithy shape ``com.amazonaws.apigatewaymanagementapi#ApiGatewayManagementApi``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_apigatewaymanagementapi._auth._signers
import capo_apigatewaymanagementapi._auth._sigv4
from capo_apigatewaymanagementapi._auth._identity import Credentials
from capo_apigatewaymanagementapi._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_apigatewaymanagementapi._auth._zapros_handler import AuthMiddleware
from capo_apigatewaymanagementapi._services._aws_config import aws_config
from capo_apigatewaymanagementapi._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_apigatewaymanagementapi.types.__string
    import capo_apigatewaymanagementapi.types.data
    import capo_apigatewaymanagementapi.types.delete_connection_request
    import capo_apigatewaymanagementapi.types.get_connection_request
    import capo_apigatewaymanagementapi.types.get_connection_response
    import capo_apigatewaymanagementapi.types.post_to_connection_request


class ApiGatewayManagementApiClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class ApiGatewayManagementApiClient:
    """A client for the ``ApiGatewayManagementApi`` service.

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
        self._config = ApiGatewayManagementApiClientConfig(
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
        self, config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApiGatewayManagementApiClientConfig = config_overrides or {}
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

    def delete_connection(
        self,
        connection_id: "capo_apigatewaymanagementapi.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None,
    ) -> None:
        """<p>Delete the connection with the provided id.</p>

        Raises:
            capo_apigatewaymanagementapi.errors.forbidden_exception.ForbiddenException: <p>The caller is not authorized to invoke this operation.</p>
            capo_apigatewaymanagementapi.errors.gone_exception.GoneException: <p>The connection with the provided id no longer exists.</p>
            capo_apigatewaymanagementapi.errors.limit_exceeded_exception.LimitExceededException: <p>The client is sending more than the allowed number of requests per unit of time or the WebSocket client side buffer is full.</p>
            capo_apigatewaymanagementapi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewaymanagementapi.types.delete_connection_request.DeleteConnectionRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewaymanagementapi._operations.api_gateway_management_api.delete_connection

            output, http_response = (
                capo_apigatewaymanagementapi._operations.api_gateway_management_api.delete_connection.delete_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewaymanagementapi.types.delete_connection_request.DeleteConnectionRequest = {
            "connection_id": connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_connection(
        self,
        connection_id: "capo_apigatewaymanagementapi.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None,
    ) -> "capo_apigatewaymanagementapi.types.get_connection_response.GetConnectionResponse":
        """<p>Get information about the connection with the provided id.</p>

        Raises:
            capo_apigatewaymanagementapi.errors.forbidden_exception.ForbiddenException: <p>The caller is not authorized to invoke this operation.</p>
            capo_apigatewaymanagementapi.errors.gone_exception.GoneException: <p>The connection with the provided id no longer exists.</p>
            capo_apigatewaymanagementapi.errors.limit_exceeded_exception.LimitExceededException: <p>The client is sending more than the allowed number of requests per unit of time or the WebSocket client side buffer is full.</p>
            capo_apigatewaymanagementapi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewaymanagementapi.types.get_connection_request.GetConnectionRequest]",
        ) -> OperationResponse[
            "capo_apigatewaymanagementapi.types.get_connection_response.GetConnectionResponse"
        ]:
            import capo_apigatewaymanagementapi._operations.api_gateway_management_api.get_connection

            output, http_response = (
                capo_apigatewaymanagementapi._operations.api_gateway_management_api.get_connection.get_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewaymanagementapi.types.get_connection_request.GetConnectionRequest = {
            "connection_id": connection_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def post_to_connection(
        self,
        connection_id: "capo_apigatewaymanagementapi.types.__string.__string",
        *,
        config_overrides: Optional[ApiGatewayManagementApiClientConfig] = None,
        data: Optional["capo_apigatewaymanagementapi.types.data.Data"] = None,
    ) -> None:
        """<p>Sends the provided data to the specified connection.</p>

        Args:
            data: <p>The data to be sent to the client specified by its connection id.</p>
            connection_id: <p>The identifier of the connection that a specific client is using.</p>

        Raises:
            capo_apigatewaymanagementapi.errors.forbidden_exception.ForbiddenException: <p>The caller is not authorized to invoke this operation.</p>
            capo_apigatewaymanagementapi.errors.gone_exception.GoneException: <p>The connection with the provided id no longer exists.</p>
            capo_apigatewaymanagementapi.errors.limit_exceeded_exception.LimitExceededException: <p>The client is sending more than the allowed number of requests per unit of time or the WebSocket client side buffer is full.</p>
            capo_apigatewaymanagementapi.errors.payload_too_large_exception.PayloadTooLargeException: <p>The data has exceeded the maximum size allowed.</p>
            capo_apigatewaymanagementapi.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest]",
        ) -> OperationResponse[None]:
            import capo_apigatewaymanagementapi._operations.api_gateway_management_api.post_to_connection

            output, http_response = (
                capo_apigatewaymanagementapi._operations.api_gateway_management_api.post_to_connection.post_to_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_apigatewaymanagementapi.types.post_to_connection_request.PostToConnectionRequest = {
            "connection_id": connection_id
        }
        if data is not None:
            input_["data"] = data

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
