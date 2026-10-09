"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#SSMGuiConnect``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ssm_guiconnect._auth._signers
import capo_ssm_guiconnect._auth._sigv4
from capo_ssm_guiconnect._auth._identity import Credentials
from capo_ssm_guiconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ssm_guiconnect._auth._zapros_handler import AuthMiddleware
from capo_ssm_guiconnect._resources.ssm_gui_connect.connection import AsyncConnection
from capo_ssm_guiconnect._resources.ssm_gui_connect.connection_access import (
    AsyncConnectionAccess,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.connection_preferences import (
    AsyncConnectionPreferences,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.connections_collection import (
    AsyncConnectionsCollection,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.modify_connection_preferences import (
    AsyncModifyConnectionPreferences,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.modify_recording_preferences import (
    AsyncModifyRecordingPreferences,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.recording_preferences import (
    AsyncRecordingPreferences,
)
from capo_ssm_guiconnect._services._aws_config import aaws_config
from capo_ssm_guiconnect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.client_token
    import capo_ssm_guiconnect.types.connection_recording_preferences
    import capo_ssm_guiconnect.types.delete_connection_recording_preferences_request
    import capo_ssm_guiconnect.types.delete_connection_recording_preferences_response
    import capo_ssm_guiconnect.types.get_connection_recording_preferences_response
    import capo_ssm_guiconnect.types.update_connection_recording_preferences_request
    import capo_ssm_guiconnect.types.update_connection_recording_preferences_response


class AsyncSSMGuiConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSSMGuiConnectClient:
    """A client for the ``SSMGuiConnect`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncSSMGuiConnectClientConfig(
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
        self.connection = AsyncConnection(self)
        self.connection_access = AsyncConnectionAccess(self)
        self.connection_preferences = AsyncConnectionPreferences(self)
        self.connections_collection = AsyncConnectionsCollection(self)
        self.modify_connection_preferences = AsyncModifyConnectionPreferences(self)
        self.modify_recording_preferences = AsyncModifyRecordingPreferences(self)
        self.recording_preferences = AsyncRecordingPreferences(self)

    def operation_options(
        self, config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSSMGuiConnectClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def get_connection_recording_preferences(
        self, *, config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None
    ) -> "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse":
        """<p>Returns the preferences specified for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieves the connection recording preferences for the account

            >>> await client.get_connection_recording_preferences()
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences

            (
                output,
                http_response,
            ) = await capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences.async_get_connection_recording_preferences(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connection_recording_preferences(
        self,
        *,
        config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "capo_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse":
        """<p>Deletes the preferences for recording RDP connections.</p>

        Args:
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete the connection recording preferences for the account

            >>> await client.delete_connection_recording_preferences()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences

            (
                output,
                http_response,
            ) = await capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences.async_delete_connection_recording_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest = {}
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connection_recording_preferences(
        self,
        connection_recording_preferences: "capo_ssm_guiconnect.types.connection_recording_preferences.ConnectionRecordingPreferences",
        *,
        config_overrides: Optional[AsyncSSMGuiConnectClientConfig] = None,
        client_token: Optional[
            "capo_ssm_guiconnect.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse":
        """<p>Updates the preferences for recording RDP connections.</p>

        Args:
            connection_recording_preferences: <p>The set of preferences used for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region. This includes details such as which S3 bucket recordings are stored in.</p>
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            capo_ssm_guiconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_ssm_guiconnect.errors.conflict_exception.ConflictException: <p>An error occurred due to a conflict.</p>
            capo_ssm_guiconnect.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_ssm_guiconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_ssm_guiconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Your request exceeds a service quota.</p>
            capo_ssm_guiconnect.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_ssm_guiconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_ssm_guiconnect.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Updates the connection recording preferences for the account

            >>> await client.update_connection_recording_preferences(connection_recording_preferences={'RecordingDestinations': {'S3Buckets': [{'BucketOwner': '123456789012', 'BucketName': 'sample-connection-recording-bucket'}]}, 'KMSKeyArn': 'arn:aws:kms:region:account_id:key/sample_key_id'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences

            (
                output,
                http_response,
            ) = await capo_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences.async_update_connection_recording_preferences(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest = {
            "connection_recording_preferences": connection_recording_preferences
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

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
