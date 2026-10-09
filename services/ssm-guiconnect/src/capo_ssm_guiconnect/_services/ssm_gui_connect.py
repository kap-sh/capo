"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#SSMGuiConnect``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

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
from capo_ssm_guiconnect._resources.ssm_gui_connect.connection import Connection
from capo_ssm_guiconnect._resources.ssm_gui_connect.connection_access import (
    ConnectionAccess,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.connection_preferences import (
    ConnectionPreferences,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.connections_collection import (
    ConnectionsCollection,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.modify_connection_preferences import (
    ModifyConnectionPreferences,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.modify_recording_preferences import (
    ModifyRecordingPreferences,
)
from capo_ssm_guiconnect._resources.ssm_gui_connect.recording_preferences import (
    RecordingPreferences,
)
from capo_ssm_guiconnect._services._aws_config import aws_config
from capo_ssm_guiconnect._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.client_token
    import capo_ssm_guiconnect.types.connection_recording_preferences
    import capo_ssm_guiconnect.types.delete_connection_recording_preferences_request
    import capo_ssm_guiconnect.types.delete_connection_recording_preferences_response
    import capo_ssm_guiconnect.types.get_connection_recording_preferences_response
    import capo_ssm_guiconnect.types.update_connection_recording_preferences_request
    import capo_ssm_guiconnect.types.update_connection_recording_preferences_response


class SSMGuiConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SSMGuiConnectClient:
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
        self._config = SSMGuiConnectClientConfig(
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
        self.connection = Connection(self)
        self.connection_access = ConnectionAccess(self)
        self.connection_preferences = ConnectionPreferences(self)
        self.connections_collection = ConnectionsCollection(self)
        self.modify_connection_preferences = ModifyConnectionPreferences(self)
        self.modify_recording_preferences = ModifyRecordingPreferences(self)
        self.recording_preferences = RecordingPreferences(self)

    def operation_options(
        self, config_overrides: Optional[SSMGuiConnectClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SSMGuiConnectClientConfig = config_overrides or {}
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

    def get_connection_recording_preferences(
        self, *, config_overrides: Optional[SSMGuiConnectClientConfig] = None
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

            >>> client.get_connection_recording_preferences()
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_ssm_guiconnect.types.get_connection_recording_preferences_response.GetConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences

            output, http_response = (
                capo_ssm_guiconnect._operations.ssm_gui_connect.get_connection_recording_preferences.get_connection_recording_preferences(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connection_recording_preferences(
        self,
        *,
        config_overrides: Optional[SSMGuiConnectClientConfig] = None,
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

            >>> client.delete_connection_recording_preferences()
        """

        def _handler(
            req: "OperationRequest[capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest]",
        ) -> OperationResponse[
            "capo_ssm_guiconnect.types.delete_connection_recording_preferences_response.DeleteConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences

            output, http_response = (
                capo_ssm_guiconnect._operations.ssm_gui_connect.delete_connection_recording_preferences.delete_connection_recording_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_guiconnect.types.delete_connection_recording_preferences_request.DeleteConnectionRecordingPreferencesRequest = {}
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

    def update_connection_recording_preferences(
        self,
        connection_recording_preferences: "capo_ssm_guiconnect.types.connection_recording_preferences.ConnectionRecordingPreferences",
        *,
        config_overrides: Optional[SSMGuiConnectClientConfig] = None,
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

            >>> client.update_connection_recording_preferences(connection_recording_preferences={'RecordingDestinations': {'S3Buckets': [{'BucketOwner': '123456789012', 'BucketName': 'sample-connection-recording-bucket'}]}, 'KMSKeyArn': 'arn:aws:kms:region:account_id:key/sample_key_id'})
        """

        def _handler(
            req: "OperationRequest[capo_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest]",
        ) -> OperationResponse[
            "capo_ssm_guiconnect.types.update_connection_recording_preferences_response.UpdateConnectionRecordingPreferencesResponse"
        ]:
            import capo_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences

            output, http_response = (
                capo_ssm_guiconnect._operations.ssm_gui_connect.update_connection_recording_preferences.update_connection_recording_preferences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm_guiconnect.types.update_connection_recording_preferences_request.UpdateConnectionRecordingPreferencesRequest = {
            "connection_recording_preferences": connection_recording_preferences
        }
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

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
