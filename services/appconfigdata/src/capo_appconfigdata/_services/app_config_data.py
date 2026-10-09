"""Generated from Smithy shape ``com.amazonaws.appconfigdata#AppConfigData``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_appconfigdata._auth._signers
import capo_appconfigdata._auth._sigv4
from capo_appconfigdata._auth._identity import Credentials
from capo_appconfigdata._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_appconfigdata._auth._zapros_handler import AuthMiddleware
from capo_appconfigdata._resources.app_config_data.configuration_session import (
    ConfigurationSession,
)
from capo_appconfigdata._services._aws_config import aws_config
from capo_appconfigdata._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_appconfigdata.types.get_latest_configuration_request
    import capo_appconfigdata.types.get_latest_configuration_response
    import capo_appconfigdata.types.identifier
    import capo_appconfigdata.types.optional_poll_seconds
    import capo_appconfigdata.types.start_configuration_session_request
    import capo_appconfigdata.types.start_configuration_session_response
    import capo_appconfigdata.types.token


class AppConfigDataClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AppConfigDataClient:
    """A client for the ``AppConfigData`` service.

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
        self._config = AppConfigDataClientConfig(
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

        # resources
        self.configuration_session = ConfigurationSession(self)

    def operation_options(
        self, config_overrides: Optional[AppConfigDataClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: AppConfigDataClientConfig = config_overrides or {}
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

    def get_latest_configuration(
        self,
        configuration_token: "capo_appconfigdata.types.token.Token",
        *,
        config_overrides: Optional[AppConfigDataClientConfig] = None,
    ) -> "capo_appconfigdata.types.get_latest_configuration_response.GetLatestConfigurationResponse":
        """<p>Retrieves the latest deployed configuration. This API may return empty configuration data if the client already has the latest version. For more information about this API action and to view example CLI commands that show how to use it with the <a>StartConfigurationSession</a> API action, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration">Retrieving the configuration</a> in the <i>AppConfig User Guide</i>. </p> <important> <p>Note the following important information.</p> <ul> <li> <p>Each configuration token is only valid for one call to <code>GetLatestConfiguration</code>. The <code>GetLatestConfiguration</code> response includes a <code>NextPollConfigurationToken</code> that should always replace the token used for the just-completed call in preparation for the next one. </p> </li> <li> <p> <code>GetLatestConfiguration</code> is a priced call. For more information, see <a href="https://aws.amazon.com/systems-manager/pricing/">Pricing</a>.</p> </li> </ul> </important>

        Args:
            configuration_token: <p>Token describing the current state of the configuration session. To obtain a token, first call the <a>StartConfigurationSession</a> API. Note that every call to <code>GetLatestConfiguration</code> will return a new <code>ConfigurationToken</code> (<code>NextPollConfigurationToken</code> in the response) and <i>must</i> be provided to subsequent <code>GetLatestConfiguration</code> API calls.</p> <important> <p>This token should only be used once. To support long poll use cases, the token is valid for up to 24 hours. If a <code>GetLatestConfiguration</code> call uses an expired token, the system returns <code>BadRequestException</code>.</p> </important>

        Raises:
            capo_appconfigdata.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_appconfigdata.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the service.</p>
            capo_appconfigdata.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfigdata.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_appconfigdata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfigdata.types.get_latest_configuration_request.GetLatestConfigurationRequest]",
        ) -> OperationResponse[
            "capo_appconfigdata.types.get_latest_configuration_response.GetLatestConfigurationResponse"
        ]:
            import capo_appconfigdata._operations.app_config_data.get_latest_configuration

            output, http_response = (
                capo_appconfigdata._operations.app_config_data.get_latest_configuration.get_latest_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfigdata.types.get_latest_configuration_request.GetLatestConfigurationRequest = {
            "configuration_token": configuration_token
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_configuration_session(
        self,
        application_identifier: "capo_appconfigdata.types.identifier.Identifier",
        environment_identifier: "capo_appconfigdata.types.identifier.Identifier",
        configuration_profile_identifier: "capo_appconfigdata.types.identifier.Identifier",
        *,
        config_overrides: Optional[AppConfigDataClientConfig] = None,
        required_minimum_poll_interval_in_seconds: Optional[
            "capo_appconfigdata.types.optional_poll_seconds.OptionalPollSeconds"
        ] = None,
    ) -> "capo_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse":
        """<p>Starts a configuration session used to retrieve a deployed configuration. For more information about this API action and to view example CLI commands that show how to use it with the <a>GetLatestConfiguration</a> API action, see <a href="http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration">Retrieving the configuration</a> in the <i>AppConfig User Guide</i>. </p>

        Args:
            application_identifier: <p>The application ID or the application name.</p>
            environment_identifier: <p>The environment ID or the environment name.</p>
            configuration_profile_identifier: <p>The configuration profile ID or the configuration profile name.</p>
            required_minimum_poll_interval_in_seconds: <p>Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call <a>GetLatestConfiguration</a> more frequently than every 60 seconds.</p>

        Raises:
            capo_appconfigdata.errors.bad_request_exception.BadRequestException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_appconfigdata.errors.internal_server_exception.InternalServerException: <p>There was an internal failure in the service.</p>
            capo_appconfigdata.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_appconfigdata.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_appconfigdata.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest]",
        ) -> OperationResponse[
            "capo_appconfigdata.types.start_configuration_session_response.StartConfigurationSessionResponse"
        ]:
            import capo_appconfigdata._operations.app_config_data.start_configuration_session

            output, http_response = (
                capo_appconfigdata._operations.app_config_data.start_configuration_session.start_configuration_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_appconfigdata.types.start_configuration_session_request.StartConfigurationSessionRequest = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "configuration_profile_identifier": configuration_profile_identifier,
        }
        if required_minimum_poll_interval_in_seconds is not None:
            input_["required_minimum_poll_interval_in_seconds"] = (
                required_minimum_poll_interval_in_seconds
            )

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
