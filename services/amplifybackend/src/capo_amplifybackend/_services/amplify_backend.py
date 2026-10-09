"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AmplifyBackend``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_amplifybackend._auth._signers
import capo_amplifybackend._auth._sigv4
from capo_amplifybackend._auth._identity import Credentials
from capo_amplifybackend._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_amplifybackend._auth._zapros_handler import AuthMiddleware
from capo_amplifybackend._services._aws_config import aws_config
from capo_amplifybackend._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_amplifybackend.types.__boolean
    import capo_amplifybackend.types.__integer_min1_max25
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.backend_api_resource_config
    import capo_amplifybackend.types.clone_backend_request
    import capo_amplifybackend.types.clone_backend_response
    import capo_amplifybackend.types.create_backend_api_request
    import capo_amplifybackend.types.create_backend_api_response
    import capo_amplifybackend.types.create_backend_auth_request
    import capo_amplifybackend.types.create_backend_auth_resource_config
    import capo_amplifybackend.types.create_backend_auth_response
    import capo_amplifybackend.types.create_backend_config_request
    import capo_amplifybackend.types.create_backend_config_response
    import capo_amplifybackend.types.create_backend_request
    import capo_amplifybackend.types.create_backend_response
    import capo_amplifybackend.types.create_backend_storage_request
    import capo_amplifybackend.types.create_backend_storage_resource_config
    import capo_amplifybackend.types.create_backend_storage_response
    import capo_amplifybackend.types.create_token_request
    import capo_amplifybackend.types.create_token_response
    import capo_amplifybackend.types.delete_backend_api_request
    import capo_amplifybackend.types.delete_backend_api_response
    import capo_amplifybackend.types.delete_backend_auth_request
    import capo_amplifybackend.types.delete_backend_auth_response
    import capo_amplifybackend.types.delete_backend_request
    import capo_amplifybackend.types.delete_backend_response
    import capo_amplifybackend.types.delete_backend_storage_request
    import capo_amplifybackend.types.delete_backend_storage_response
    import capo_amplifybackend.types.delete_token_request
    import capo_amplifybackend.types.delete_token_response
    import capo_amplifybackend.types.generate_backend_api_models_request
    import capo_amplifybackend.types.generate_backend_api_models_response
    import capo_amplifybackend.types.get_backend_api_models_request
    import capo_amplifybackend.types.get_backend_api_models_response
    import capo_amplifybackend.types.get_backend_api_request
    import capo_amplifybackend.types.get_backend_api_response
    import capo_amplifybackend.types.get_backend_auth_request
    import capo_amplifybackend.types.get_backend_auth_response
    import capo_amplifybackend.types.get_backend_job_request
    import capo_amplifybackend.types.get_backend_job_response
    import capo_amplifybackend.types.get_backend_request
    import capo_amplifybackend.types.get_backend_response
    import capo_amplifybackend.types.get_backend_storage_request
    import capo_amplifybackend.types.get_backend_storage_response
    import capo_amplifybackend.types.get_token_request
    import capo_amplifybackend.types.get_token_response
    import capo_amplifybackend.types.import_backend_auth_request
    import capo_amplifybackend.types.import_backend_auth_response
    import capo_amplifybackend.types.import_backend_storage_request
    import capo_amplifybackend.types.import_backend_storage_response
    import capo_amplifybackend.types.list_backend_jobs_request
    import capo_amplifybackend.types.list_backend_jobs_response
    import capo_amplifybackend.types.list_s3_buckets_request
    import capo_amplifybackend.types.list_s3_buckets_response
    import capo_amplifybackend.types.login_auth_config_req_obj
    import capo_amplifybackend.types.remove_all_backends_request
    import capo_amplifybackend.types.remove_all_backends_response
    import capo_amplifybackend.types.remove_backend_config_request
    import capo_amplifybackend.types.remove_backend_config_response
    import capo_amplifybackend.types.resource_config
    import capo_amplifybackend.types.service_name
    import capo_amplifybackend.types.update_backend_api_request
    import capo_amplifybackend.types.update_backend_api_response
    import capo_amplifybackend.types.update_backend_auth_request
    import capo_amplifybackend.types.update_backend_auth_resource_config
    import capo_amplifybackend.types.update_backend_auth_response
    import capo_amplifybackend.types.update_backend_config_request
    import capo_amplifybackend.types.update_backend_config_response
    import capo_amplifybackend.types.update_backend_job_request
    import capo_amplifybackend.types.update_backend_job_response
    import capo_amplifybackend.types.update_backend_storage_request
    import capo_amplifybackend.types.update_backend_storage_resource_config
    import capo_amplifybackend.types.update_backend_storage_response


class AmplifyBackendClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AmplifyBackendClient:
    """A client for the ``AmplifyBackend`` service.

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
        self._config = AmplifyBackendClientConfig(
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
        self, config_overrides: Optional[AmplifyBackendClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AmplifyBackendClientConfig = config_overrides or {}
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

    def clone_backend(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        target_environment_name: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "capo_amplifybackend.types.clone_backend_response.CloneBackendResponse":
        """<p>This operation clones an existing backend.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            target_environment_name: <p>The name of the destination backend environment to be created.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.clone_backend_request.CloneBackendRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.clone_backend_response.CloneBackendResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.clone_backend

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.clone_backend.clone_backend(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.clone_backend_request.CloneBackendRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if target_environment_name is not None:
            input_["target_environment_name"] = target_environment_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backend(
        self,
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        app_id: Optional["capo_amplifybackend.types.__string.__string"] = None,
        app_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
        backend_environment_name: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.resource_config.ResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.create_backend_response.CreateBackendResponse":
        """<p>This operation creates a backend for an Amplify app. Backends are automatically created at the time of app creation.</p>

        Args:
            app_id: <p>The app ID.</p>
            app_name: <p>The name of the app.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for creating a backend.</p>
            resource_name: <p>The name of the resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.create_backend_request.CreateBackendRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.create_backend_response.CreateBackendResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.create_backend

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.create_backend.create_backend(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.create_backend_request.CreateBackendRequest = {}
        if app_id is not None:
            input_["app_id"] = app_id
        if app_name is not None:
            input_["app_name"] = app_name
        if backend_environment_name is not None:
            input_["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backend_api(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        backend_environment_name: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> (
        "capo_amplifybackend.types.create_backend_api_response.CreateBackendAPIResponse"
    ):
        """<p>Creates a new backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for this request.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.create_backend_api_request.CreateBackendAPIRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.create_backend_api_response.CreateBackendAPIResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.create_backend_api

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.create_backend_api.create_backend_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.create_backend_api_request.CreateBackendAPIRequest = {
            "app_id": app_id
        }
        if backend_environment_name is not None:
            input_["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backend_auth(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        backend_environment_name: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.create_backend_auth_resource_config.CreateBackendAuthResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.create_backend_auth_response.CreateBackendAuthResponse":
        """<p>Creates a new backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for this request object.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.create_backend_auth_request.CreateBackendAuthRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.create_backend_auth_response.CreateBackendAuthResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.create_backend_auth

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.create_backend_auth.create_backend_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.create_backend_auth_request.CreateBackendAuthRequest = {
            "app_id": app_id
        }
        if backend_environment_name is not None:
            input_["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backend_config(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        backend_manager_app_id: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "capo_amplifybackend.types.create_backend_config_response.CreateBackendConfigResponse":
        """<p>Creates a config object for a backend.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_manager_app_id: <p>The app ID for the backend manager.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.create_backend_config_request.CreateBackendConfigRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.create_backend_config_response.CreateBackendConfigResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.create_backend_config

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.create_backend_config.create_backend_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.create_backend_config_request.CreateBackendConfigRequest = {
            "app_id": app_id
        }
        if backend_manager_app_id is not None:
            input_["backend_manager_app_id"] = backend_manager_app_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_backend_storage(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        backend_environment_name: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.create_backend_storage_resource_config.CreateBackendStorageResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.create_backend_storage_response.CreateBackendStorageResponse":
        """<p>Creates a backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for creating backend storage.</p>
            resource_name: <p>The name of the storage resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.create_backend_storage_request.CreateBackendStorageRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.create_backend_storage_response.CreateBackendStorageResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.create_backend_storage

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.create_backend_storage.create_backend_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.create_backend_storage_request.CreateBackendStorageRequest = {
            "app_id": app_id
        }
        if backend_environment_name is not None:
            input_["backend_environment_name"] = backend_environment_name
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_token(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
    ) -> "capo_amplifybackend.types.create_token_response.CreateTokenResponse":
        """<p>Generates a one-time challenge code to authenticate a user into your Amplify Admin UI.</p>

        Args:
            app_id: <p>The app ID.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.create_token_request.CreateTokenRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.create_token_response.CreateTokenResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.create_token

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.create_token.create_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.create_token_request.CreateTokenRequest = {
            "app_id": app_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backend(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
    ) -> "capo_amplifybackend.types.delete_backend_response.DeleteBackendResponse":
        """<p>Removes an existing environment from your Amplify project.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.delete_backend_request.DeleteBackendRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.delete_backend_response.DeleteBackendResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.delete_backend

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.delete_backend.delete_backend(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.delete_backend_request.DeleteBackendRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backend_api(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> (
        "capo_amplifybackend.types.delete_backend_api_response.DeleteBackendAPIResponse"
    ):
        """<p>Deletes an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>Defines the resource configuration for the data model in your Amplify project.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.delete_backend_api_request.DeleteBackendAPIRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.delete_backend_api_response.DeleteBackendAPIResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.delete_backend_api

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.delete_backend_api.delete_backend_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.delete_backend_api_request.DeleteBackendAPIRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backend_auth(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.delete_backend_auth_response.DeleteBackendAuthResponse":
        """<p>Deletes an existing backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.delete_backend_auth_request.DeleteBackendAuthRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.delete_backend_auth_response.DeleteBackendAuthResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.delete_backend_auth

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.delete_backend_auth.delete_backend_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.delete_backend_auth_request.DeleteBackendAuthRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_backend_storage(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
        service_name: Optional[
            "capo_amplifybackend.types.service_name.ServiceName"
        ] = None,
    ) -> "capo_amplifybackend.types.delete_backend_storage_response.DeleteBackendStorageResponse":
        """<p>Removes the specified backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of the storage resource.</p>
            service_name: <p>The name of the storage service.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.delete_backend_storage_request.DeleteBackendStorageRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.delete_backend_storage_response.DeleteBackendStorageResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.delete_backend_storage

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.delete_backend_storage.delete_backend_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.delete_backend_storage_request.DeleteBackendStorageRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name
        if service_name is not None:
            input_["service_name"] = service_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_token(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        session_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
    ) -> "capo_amplifybackend.types.delete_token_response.DeleteTokenResponse":
        """<p>Deletes the challenge token based on the given appId and sessionId.</p>

        Args:
            app_id: <p>The app ID.</p>
            session_id: <p>The session ID.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.delete_token_request.DeleteTokenRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.delete_token_response.DeleteTokenResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.delete_token

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.delete_token.delete_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.delete_token_request.DeleteTokenRequest = {
            "app_id": app_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def generate_backend_api_models(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse":
        """<p>Generates a model schema for an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.generate_backend_api_models_response.GenerateBackendAPIModelsResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.generate_backend_api_models

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.generate_backend_api_models.generate_backend_api_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.generate_backend_api_models_request.GenerateBackendAPIModelsRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backend(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        backend_environment_name: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
    ) -> "capo_amplifybackend.types.get_backend_response.GetBackendResponse":
        """<p>Provides project-level details for your Amplify UI project.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_backend_request.GetBackendRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_backend_response.GetBackendResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_backend

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_backend.get_backend(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_backend_request.GetBackendRequest = {
            "app_id": app_id
        }
        if backend_environment_name is not None:
            input_["backend_environment_name"] = backend_environment_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backend_api(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.get_backend_api_response.GetBackendAPIResponse":
        """<p>Gets the details for a backend API.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>Defines the resource configuration for the data model in your Amplify project.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_backend_api_request.GetBackendAPIRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_backend_api_response.GetBackendAPIResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_backend_api

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_backend_api.get_backend_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_backend_api_request.GetBackendAPIRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backend_api_models(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.get_backend_api_models_response.GetBackendAPIModelsResponse":
        """<p>Gets a model introspection schema for an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_backend_api_models_request.GetBackendAPIModelsRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_backend_api_models_response.GetBackendAPIModelsResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_backend_api_models

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_backend_api_models.get_backend_api_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_backend_api_models_request.GetBackendAPIModelsRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backend_auth(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.get_backend_auth_response.GetBackendAuthResponse":
        """<p>Gets a backend auth details.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_backend_auth_request.GetBackendAuthRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_backend_auth_response.GetBackendAuthResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_backend_auth

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_backend_auth.get_backend_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_backend_auth_request.GetBackendAuthRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backend_job(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        job_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
    ) -> "capo_amplifybackend.types.get_backend_job_response.GetBackendJobResponse":
        """<p>Returns information about a specific job.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            job_id: <p>The ID for the job.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_backend_job_request.GetBackendJobRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_backend_job_response.GetBackendJobResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_backend_job

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_backend_job.get_backend_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_backend_job_request.GetBackendJobRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_backend_storage(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.get_backend_storage_response.GetBackendStorageResponse":
        """<p>Gets details for a backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_name: <p>The name of the storage resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_backend_storage_request.GetBackendStorageRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_backend_storage_response.GetBackendStorageResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_backend_storage

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_backend_storage.get_backend_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_backend_storage_request.GetBackendStorageRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_token(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        session_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
    ) -> "capo_amplifybackend.types.get_token_response.GetTokenResponse":
        """<p>Gets the challenge token based on the given appId and sessionId.</p>

        Args:
            app_id: <p>The app ID.</p>
            session_id: <p>The session ID.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.get_token_request.GetTokenRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.get_token_response.GetTokenResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.get_token

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.get_token.get_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.get_token_request.GetTokenRequest = {
            "app_id": app_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_backend_auth(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        identity_pool_id: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
        native_client_id: Optional[
            "capo_amplifybackend.types.__string.__string"
        ] = None,
        user_pool_id: Optional["capo_amplifybackend.types.__string.__string"] = None,
        web_client_id: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.import_backend_auth_response.ImportBackendAuthResponse":
        """<p>Imports an existing backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            identity_pool_id: <p>The ID of the Amazon Cognito identity pool.</p>
            native_client_id: <p>The ID of the Amazon Cognito native client.</p>
            user_pool_id: <p>The ID of the Amazon Cognito user pool.</p>
            web_client_id: <p>The ID of the Amazon Cognito web client.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.import_backend_auth_request.ImportBackendAuthRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.import_backend_auth_response.ImportBackendAuthResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.import_backend_auth

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.import_backend_auth.import_backend_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.import_backend_auth_request.ImportBackendAuthRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if identity_pool_id is not None:
            input_["identity_pool_id"] = identity_pool_id
        if native_client_id is not None:
            input_["native_client_id"] = native_client_id
        if user_pool_id is not None:
            input_["user_pool_id"] = user_pool_id
        if web_client_id is not None:
            input_["web_client_id"] = web_client_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_backend_storage(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        bucket_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
        service_name: Optional[
            "capo_amplifybackend.types.service_name.ServiceName"
        ] = None,
    ) -> "capo_amplifybackend.types.import_backend_storage_response.ImportBackendStorageResponse":
        """<p>Imports an existing backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            bucket_name: <p>The name of the S3 bucket.</p>
            service_name: <p>The name of the storage service.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.import_backend_storage_request.ImportBackendStorageRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.import_backend_storage_response.ImportBackendStorageResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.import_backend_storage

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.import_backend_storage.import_backend_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.import_backend_storage_request.ImportBackendStorageRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if bucket_name is not None:
            input_["bucket_name"] = bucket_name
        if service_name is not None:
            input_["service_name"] = service_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_backend_jobs(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        job_id: Optional["capo_amplifybackend.types.__string.__string"] = None,
        max_results: Optional[
            "capo_amplifybackend.types.__integer_min1_max25.__integerMin1Max25"
        ] = None,
        next_token: Optional["capo_amplifybackend.types.__string.__string"] = None,
        operation: Optional["capo_amplifybackend.types.__string.__string"] = None,
        status: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.list_backend_jobs_response.ListBackendJobsResponse":
        """<p>Lists the jobs for the backend of an Amplify app.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            job_id: <p>The ID for the job.</p>
            max_results: <p>The maximum number of results that you want in the response.</p>
            next_token: <p>The token for the next set of results.</p>
            operation: <p>Filters the list of response objects to include only those with the specified operation name.</p>
            status: <p>Filters the list of response objects to include only those with the specified status.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.list_backend_jobs_request.ListBackendJobsRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.list_backend_jobs_response.ListBackendJobsResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.list_backend_jobs

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.list_backend_jobs.list_backend_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.list_backend_jobs_request.ListBackendJobsRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if job_id is not None:
            input_["job_id"] = job_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if operation is not None:
            input_["operation"] = operation
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_s3_buckets(
        self,
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        next_token: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.list_s3_buckets_response.ListS3BucketsResponse":
        """<p>The list of S3 buckets in your account.</p>

        Args:
            next_token: <p>Reserved for future use.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.list_s3_buckets_request.ListS3BucketsRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.list_s3_buckets_response.ListS3BucketsResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.list_s3_buckets

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.list_s3_buckets.list_s3_buckets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.list_s3_buckets_request.ListS3BucketsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_all_backends(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        clean_amplify_app: Optional[
            "capo_amplifybackend.types.__boolean.__boolean"
        ] = None,
    ) -> "capo_amplifybackend.types.remove_all_backends_response.RemoveAllBackendsResponse":
        """<p>Removes all backend environments from your Amplify project.</p>

        Args:
            app_id: <p>The app ID.</p>
            clean_amplify_app: <p>Cleans up the Amplify Console app if this value is set to true.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.remove_all_backends_request.RemoveAllBackendsRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.remove_all_backends_response.RemoveAllBackendsResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.remove_all_backends

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.remove_all_backends.remove_all_backends(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.remove_all_backends_request.RemoveAllBackendsRequest = {
            "app_id": app_id
        }
        if clean_amplify_app is not None:
            input_["clean_amplify_app"] = clean_amplify_app

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_backend_config(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
    ) -> "capo_amplifybackend.types.remove_backend_config_response.RemoveBackendConfigResponse":
        """<p>Removes the AWS resources required to access the Amplify Admin UI.</p>

        Args:
            app_id: <p>The app ID.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.remove_backend_config_request.RemoveBackendConfigRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.remove_backend_config_response.RemoveBackendConfigResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.remove_backend_config

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.remove_backend_config.remove_backend_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.remove_backend_config_request.RemoveBackendConfigRequest = {
            "app_id": app_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_backend_api(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.backend_api_resource_config.BackendAPIResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> (
        "capo_amplifybackend.types.update_backend_api_response.UpdateBackendAPIResponse"
    ):
        """<p>Updates an existing backend API resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>Defines the resource configuration for the data model in your Amplify project.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.update_backend_api_request.UpdateBackendAPIRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.update_backend_api_response.UpdateBackendAPIResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.update_backend_api

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.update_backend_api.update_backend_api(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.update_backend_api_request.UpdateBackendAPIRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_backend_auth(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.update_backend_auth_resource_config.UpdateBackendAuthResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.update_backend_auth_response.UpdateBackendAuthResponse":
        """<p>Updates an existing backend authentication resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for this request object.</p>
            resource_name: <p>The name of this resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.update_backend_auth_request.UpdateBackendAuthRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.update_backend_auth_response.UpdateBackendAuthResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.update_backend_auth

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.update_backend_auth.update_backend_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.update_backend_auth_request.UpdateBackendAuthRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_backend_config(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        login_auth_config: Optional[
            "capo_amplifybackend.types.login_auth_config_req_obj.LoginAuthConfigReqObj"
        ] = None,
    ) -> "capo_amplifybackend.types.update_backend_config_response.UpdateBackendConfigResponse":
        """<p>Updates the AWS resources required to access the Amplify Admin UI.</p>

        Args:
            app_id: <p>The app ID.</p>
            login_auth_config: <p>Describes the Amazon Cognito configuration for Admin UI access.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.update_backend_config_request.UpdateBackendConfigRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.update_backend_config_response.UpdateBackendConfigResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.update_backend_config

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.update_backend_config.update_backend_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.update_backend_config_request.UpdateBackendConfigRequest = {
            "app_id": app_id
        }
        if login_auth_config is not None:
            input_["login_auth_config"] = login_auth_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_backend_job(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        job_id: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        operation: Optional["capo_amplifybackend.types.__string.__string"] = None,
        status: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> (
        "capo_amplifybackend.types.update_backend_job_response.UpdateBackendJobResponse"
    ):
        """<p>Updates a specific job.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            job_id: <p>The ID for the job.</p>
            operation: <p>Filters the list of response objects to include only those with the specified operation name.</p>
            status: <p>Filters the list of response objects to include only those with the specified status.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.update_backend_job_request.UpdateBackendJobRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.update_backend_job_response.UpdateBackendJobResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.update_backend_job

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.update_backend_job.update_backend_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.update_backend_job_request.UpdateBackendJobRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
            "job_id": job_id,
        }
        if operation is not None:
            input_["operation"] = operation
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_backend_storage(
        self,
        app_id: "capo_amplifybackend.types.__string.__string",
        backend_environment_name: "capo_amplifybackend.types.__string.__string",
        *,
        config_overrides: Optional[AmplifyBackendClientConfig] = None,
        resource_config: Optional[
            "capo_amplifybackend.types.update_backend_storage_resource_config.UpdateBackendStorageResourceConfig"
        ] = None,
        resource_name: Optional["capo_amplifybackend.types.__string.__string"] = None,
    ) -> "capo_amplifybackend.types.update_backend_storage_response.UpdateBackendStorageResponse":
        """<p>Updates an existing backend storage resource.</p>

        Args:
            app_id: <p>The app ID.</p>
            backend_environment_name: <p>The name of the backend environment.</p>
            resource_config: <p>The resource configuration for updating backend storage.</p>
            resource_name: <p>The name of the storage resource.</p>

        Raises:
            capo_amplifybackend.errors.bad_request_exception.BadRequestException: <p>An error returned if a request is not formed properly.</p>
            capo_amplifybackend.errors.gateway_timeout_exception.GatewayTimeoutException: <p>An error returned if there's a temporary issue with the service.</p>
            capo_amplifybackend.errors.not_found_exception.NotFoundException: <p>An error returned when a specific resource type is not found.</p>
            capo_amplifybackend.errors.too_many_requests_exception.TooManyRequestsException: <p>An error that is returned when a limit of a specific type has been exceeded.</p>
            capo_amplifybackend.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_amplifybackend.types.update_backend_storage_request.UpdateBackendStorageRequest]",
        ) -> OperationResponse[
            "capo_amplifybackend.types.update_backend_storage_response.UpdateBackendStorageResponse"
        ]:
            import capo_amplifybackend._operations.amplify_backend.update_backend_storage

            output, http_response = (
                capo_amplifybackend._operations.amplify_backend.update_backend_storage.update_backend_storage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_amplifybackend.types.update_backend_storage_request.UpdateBackendStorageRequest = {
            "app_id": app_id,
            "backend_environment_name": backend_environment_name,
        }
        if resource_config is not None:
            input_["resource_config"] = resource_config
        if resource_name is not None:
            input_["resource_name"] = resource_name

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
