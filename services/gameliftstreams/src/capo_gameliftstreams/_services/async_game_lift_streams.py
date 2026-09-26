"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#GameLiftStreams``."""

import time
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_gameliftstreams._auth._signers
import capo_gameliftstreams._auth._sigv4
from capo_gameliftstreams._async import anysleep
from capo_gameliftstreams._auth._identity import Credentials
from capo_gameliftstreams._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_gameliftstreams._auth._zapros_handler import AuthMiddleware
from capo_gameliftstreams._pagination import resolve_path as _resolve_path
from capo_gameliftstreams._resources.game_lift_streams.application_resource import (
    AsyncApplicationResource,
)
from capo_gameliftstreams._resources.game_lift_streams.stream_group_resource import (
    AsyncStreamGroupResource,
)
from capo_gameliftstreams._services._aws_config import aaws_config
from capo_gameliftstreams._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from capo_gameliftstreams.errors import (
    ServiceError,
    WaiterTimeoutError,
)

if TYPE_CHECKING:
    import capo_gameliftstreams.types.add_stream_group_locations_input
    import capo_gameliftstreams.types.add_stream_group_locations_output
    import capo_gameliftstreams.types.application_log_output_uri
    import capo_gameliftstreams.types.application_source_uri
    import capo_gameliftstreams.types.application_summary
    import capo_gameliftstreams.types.arn
    import capo_gameliftstreams.types.associate_applications_input
    import capo_gameliftstreams.types.associate_applications_output
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.connection_timeout_seconds
    import capo_gameliftstreams.types.create_application_input
    import capo_gameliftstreams.types.create_application_output
    import capo_gameliftstreams.types.create_stream_group_input
    import capo_gameliftstreams.types.create_stream_group_output
    import capo_gameliftstreams.types.create_stream_session_connection_input
    import capo_gameliftstreams.types.create_stream_session_connection_output
    import capo_gameliftstreams.types.delete_application_input
    import capo_gameliftstreams.types.delete_stream_group_input
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.disassociate_applications_input
    import capo_gameliftstreams.types.disassociate_applications_output
    import capo_gameliftstreams.types.environment_variables
    import capo_gameliftstreams.types.executable_path
    import capo_gameliftstreams.types.export_files_status
    import capo_gameliftstreams.types.export_stream_session_files_input
    import capo_gameliftstreams.types.export_stream_session_files_output
    import capo_gameliftstreams.types.file_paths
    import capo_gameliftstreams.types.game_launch_arg_list
    import capo_gameliftstreams.types.get_application_input
    import capo_gameliftstreams.types.get_application_output
    import capo_gameliftstreams.types.get_stream_group_input
    import capo_gameliftstreams.types.get_stream_group_output
    import capo_gameliftstreams.types.get_stream_session_input
    import capo_gameliftstreams.types.get_stream_session_output
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.identifiers
    import capo_gameliftstreams.types.list_applications_input
    import capo_gameliftstreams.types.list_applications_output
    import capo_gameliftstreams.types.list_stream_groups_input
    import capo_gameliftstreams.types.list_stream_groups_output
    import capo_gameliftstreams.types.list_stream_sessions_by_account_input
    import capo_gameliftstreams.types.list_stream_sessions_by_account_output
    import capo_gameliftstreams.types.list_stream_sessions_input
    import capo_gameliftstreams.types.list_stream_sessions_output
    import capo_gameliftstreams.types.list_tags_for_resource_request
    import capo_gameliftstreams.types.list_tags_for_resource_response
    import capo_gameliftstreams.types.location_configurations
    import capo_gameliftstreams.types.location_list
    import capo_gameliftstreams.types.locations_list
    import capo_gameliftstreams.types.max_results
    import capo_gameliftstreams.types.next_token
    import capo_gameliftstreams.types.output_uri
    import capo_gameliftstreams.types.performance_stats_configuration
    import capo_gameliftstreams.types.protocol
    import capo_gameliftstreams.types.remove_stream_group_locations_input
    import capo_gameliftstreams.types.runtime_environment
    import capo_gameliftstreams.types.session_length_seconds
    import capo_gameliftstreams.types.signal_request
    import capo_gameliftstreams.types.start_stream_session_input
    import capo_gameliftstreams.types.start_stream_session_output
    import capo_gameliftstreams.types.stream_class
    import capo_gameliftstreams.types.stream_group_summary
    import capo_gameliftstreams.types.stream_session_status
    import capo_gameliftstreams.types.stream_session_summary
    import capo_gameliftstreams.types.tag_key_list
    import capo_gameliftstreams.types.tag_resource_request
    import capo_gameliftstreams.types.tag_resource_response
    import capo_gameliftstreams.types.tags
    import capo_gameliftstreams.types.terminate_stream_session_input
    import capo_gameliftstreams.types.untag_resource_request
    import capo_gameliftstreams.types.untag_resource_response
    import capo_gameliftstreams.types.update_application_input
    import capo_gameliftstreams.types.update_application_output
    import capo_gameliftstreams.types.update_stream_group_input
    import capo_gameliftstreams.types.update_stream_group_output
    import capo_gameliftstreams.types.user_id


class AsyncGameLiftStreamsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncGameLiftStreamsClient:
    """A client for the ``GameLiftStreams`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncGameLiftStreamsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.application_resource = AsyncApplicationResource(self)
        self.stream_group_resource = AsyncStreamGroupResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncGameLiftStreamsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def add_stream_group_locations(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        location_configurations: "capo_gameliftstreams.types.location_configurations.LocationConfigurations",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.add_stream_group_locations_output.AddStreamGroupLocationsOutput":
        r"""<p> Add locations that can host stream sessions. To add a location, the stream group must be in <code>ACTIVE</code> status. You configure locations and their corresponding capacity for each stream group. Creating a stream group in a location that's nearest to your end users can help minimize latency and improve quality. </p> <p> This operation provisions stream capacity at the specified locations. By default, all locations have 1 or 2 capacity, depending on the stream class option: 2 for 'High' and 1 for 'Ultra' and 'Win2022'. This operation also copies the content files of all associated applications to an internal S3 bucket at each location. This allows Amazon GameLift Streams to host performant stream sessions. </p>

        Args:
            identifier: <p> A stream group to add the specified locations to. </p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.add_stream_group_locations_input.AddStreamGroupLocationsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.add_stream_group_locations_output.AddStreamGroupLocationsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.add_stream_group_locations

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.add_stream_group_locations.async_add_stream_group_locations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.add_stream_group_locations_input.AddStreamGroupLocationsInput = {
            "identifier": identifier,
            "location_configurations": location_configurations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_applications(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        application_identifiers: "capo_gameliftstreams.types.identifiers.Identifiers",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.associate_applications_output.AssociateApplicationsOutput":
        r"""<p>When you associate, or link, an application with a stream group, then Amazon GameLift Streams can launch the application using the stream group's allocated compute resources. The stream group must be in <code>ACTIVE</code> status. You can reverse this action by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html\">DisassociateApplications</a>.</p> <p>If a stream group does not already have a linked application, Amazon GameLift Streams will automatically assign the first application provided in <code>ApplicationIdentifiers</code> as the default.</p>

        Args:
            identifier: <p>A stream group to associate to the applications.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            application_identifiers: <p>A set of applications to associate with the stream group.</p> <p>This value is a set of either <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Names (ARN)</a> or IDs that uniquely identify application resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.associate_applications_input.AssociateApplicationsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.associate_applications_output.AssociateApplicationsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.associate_applications

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.associate_applications.async_associate_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.associate_applications_input.AssociateApplicationsInput = {
            "identifier": identifier,
            "application_identifiers": application_identifiers,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_stream_session_connection(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier",
        signal_request: "capo_gameliftstreams.types.signal_request.SignalRequest",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        client_token: Optional[
            "capo_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_gameliftstreams.types.create_stream_session_connection_output.CreateStreamSessionConnectionOutput":
        r"""<p>Enables clients to reconnect to a stream session while preserving all session state and data in the disconnected session. This reconnection process can be initiated when a stream session is in either <code>PENDING_CLIENT_RECONNECTION</code> or <code>ACTIVE</code> status. The process works as follows: </p> <ol> <li> <p>Initial disconnect:</p> <ul> <li> <p>When a client disconnects or loses connection, the stream session transitions from <code>CONNECTED</code> to <code>PENDING_CLIENT_RECONNECTION</code> </p> </li> </ul> </li> <li> <p>Reconnection time window:</p> <ul> <li> <p>Clients have <code>ConnectionTimeoutSeconds</code> (defined in <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html\">StartStreamSession</a>) to reconnect before session termination</p> </li> <li> <p>Your backend server must call <b>CreateStreamSessionConnection</b> to initiate reconnection</p> </li> <li> <p>Session transitions to <code>RECONNECTING</code> status</p> </li> </ul> </li> <li> <p>Reconnection completion:</p> <ul> <li> <p>On successful <b>CreateStreamSessionConnection</b>, session status changes to <code>ACTIVE</code> </p> </li> <li> <p>Provide the new connection information to the requesting client</p> </li> <li> <p>Client must establish connection within <code>ConnectionTimeoutSeconds</code> </p> </li> <li> <p>Session terminates automatically if client fails to connect in time</p> </li> </ul> </li> </ol> <p>For more information about the stream session lifecycle, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-sessions.html\">Stream sessions</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> <p>To begin re-connecting to an existing stream session, specify the stream group ID and stream session ID that you want to reconnect to, and the signal request to use with the stream.</p>

        Args:
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>
            identifier: <p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p> <p> The stream group that you want to run this stream session with. The stream group must be in <code>ACTIVE</code> status. </p>
            stream_session_identifier: <p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p> <p> The stream session must be in <code>PENDING_CLIENT_RECONNECTION</code> or <code>ACTIVE</code> status. </p>
            signal_request: <p>A WebRTC ICE offer string to use when initializing a WebRTC connection. The offer is a very long JSON string. Provide the string as a text value in quotes. The offer must be newly generated, not the same offer provided to <code>StartStreamSession</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.create_stream_session_connection_input.CreateStreamSessionConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.create_stream_session_connection_output.CreateStreamSessionConnectionOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.create_stream_session_connection

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.create_stream_session_connection.async_create_stream_session_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.create_stream_session_connection_input.CreateStreamSessionConnectionInput = {
            "identifier": identifier,
            "stream_session_identifier": stream_session_identifier,
            "signal_request": signal_request,
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

    async def disassociate_applications(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        application_identifiers: "capo_gameliftstreams.types.identifiers.Identifiers",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.disassociate_applications_output.DisassociateApplicationsOutput":
        r"""<p> When you disassociate, or unlink, an application from a stream group, you can no longer stream this application by using that stream group's allocated compute resources. Any streams in process will continue until they terminate, which helps avoid interrupting an end-user's stream. Amazon GameLift Streams will not initiate new streams in the stream group using the disassociated application. The disassociate action does not affect the stream capacity of a stream group. To disassociate an application, the stream group must be in <code>ACTIVE</code> status. </p> <p> If you disassociate the default application, Amazon GameLift Streams will automatically choose a new default application from the remaining associated applications. To change which application is the default application, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html\">UpdateStreamGroup</a> and specify a new <code>DefaultApplicationIdentifier</code>. </p>

        Args:
            identifier: <p>A stream group to disassociate these applications from.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            application_identifiers: <p>A set of applications that you want to disassociate from the stream group.</p> <p>This value is a set of either <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Names (ARN)</a> or IDs that uniquely identify application resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.disassociate_applications_input.DisassociateApplicationsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.disassociate_applications_output.DisassociateApplicationsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.disassociate_applications

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.disassociate_applications.async_disassociate_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.disassociate_applications_input.DisassociateApplicationsInput = {
            "identifier": identifier,
            "application_identifiers": application_identifiers,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_stream_session_files(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier",
        output_uri: "capo_gameliftstreams.types.output_uri.OutputUri",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.export_stream_session_files_output.ExportStreamSessionFilesOutput":
        r"""<p> Export the files that your application modifies or generates in a stream session, which can help you debug or verify your application. When your application runs, it generates output files such as logs, diagnostic information, crash dumps, save files, user data, screenshots, and so on. The files can be defined by the engine or frameworks that your application uses, or information that you've programmed your application to output. </p> <p> You can only call this action on a stream session that is in progress, specifically in one of the following statuses <code>ACTIVE</code>, <code>CONNECTED</code>, <code>PENDING_CLIENT_RECONNECTION</code>, and <code>RECONNECTING</code>. You must provide an Amazon Simple Storage Service (Amazon S3) bucket to store the files in. When the session ends, Amazon GameLift Streams produces a compressed folder that contains all of the files and directories that were modified or created by the application during the stream session. AWS uses your security credentials to authenticate and authorize access to your Amazon S3 bucket. </p> <p>Amazon GameLift Streams collects the following generated and modified files. Find them in the corresponding folders in the <code>.zip</code> archive.</p> <ul> <li> <p> <code>application/</code>: The folder where your application or game is stored. </p> </li> </ul> <ul> <li> <p> <code>profile/</code>: The user profile folder.</p> </li> <li> <p> <code>temp/</code>: The system temp folder.</p> </li> </ul> <p/> <p>To verify the status of the exported files, use GetStreamSession. </p> <p>To delete the files, delete the object in the S3 bucket. </p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            stream_session_identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p>
            output_uri: <p> The S3 bucket URI where Amazon GameLift Streams uploads the set of compressed exported files for this stream session. Amazon GameLift Streams generates a ZIP file name based on the stream session metadata. Alternatively, you can provide a custom file name with a <code>.zip</code> file extension.</p> <p> Example 1: If you provide an S3 URI called <code>s3://amzn-s3-demo-destination-bucket/MyGame_Session1.zip</code>, then Amazon GameLift Streams will save the files at that location. </p> <p> Example 2: If you provide an S3 URI called <code>s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/</code>, then Amazon GameLift Streams will save the files at <code>s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/YYYYMMDD-HHMMSS-appId-sg-Id-sessionId.zip</code> or another similar name. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.export_stream_session_files_input.ExportStreamSessionFilesInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.export_stream_session_files_output.ExportStreamSessionFilesOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.export_stream_session_files

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.export_stream_session_files.async_export_stream_session_files(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.export_stream_session_files_input.ExportStreamSessionFilesInput = {
            "identifier": identifier,
            "stream_session_identifier": stream_session_identifier,
            "output_uri": output_uri,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_stream_session(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.get_stream_session_output.GetStreamSessionOutput":
        r"""<p>Retrieves properties for a Amazon GameLift Streams stream session resource. Specify the Amazon Resource Name (ARN) of the stream session that you want to retrieve and its stream group ARN. If the operation is successful, it returns properties for the requested resource.</p>

        Args:
            identifier: <p>The stream group that runs this stream session.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            stream_session_identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.get_stream_session_input.GetStreamSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.get_stream_session_output.GetStreamSessionOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.get_stream_session

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.get_stream_session.async_get_stream_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.get_stream_session_input.GetStreamSessionInput = {
            "identifier": identifier,
            "stream_session_identifier": stream_session_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_stream_sessions(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        status: Optional[
            "capo_gameliftstreams.types.stream_session_status.StreamSessionStatus"
        ] = None,
        export_files_status: Optional[
            "capo_gameliftstreams.types.export_files_status.ExportFilesStatus"
        ] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_gameliftstreams.types.list_stream_sessions_output.ListStreamSessionsOutput":
        r"""<p>Retrieves a list of Amazon GameLift Streams stream sessions that a stream group is hosting.</p> <p>To retrieve stream sessions, specify the stream group, and optionally filter by stream session status. You can paginate the results as needed.</p> <p>This operation returns the requested stream sessions in no particular order.</p>

        Args:
            status: <p>Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.</p>
            export_files_status: <p>Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.</p> <p> Exported files can be in one of the following states: </p> <ul> <li> <p> <code>SUCCEEDED</code>: The exported files are successfully stored in an S3 bucket.</p> </li> <li> <p> <code>FAILED</code>: The session ended but Amazon GameLift Streams couldn't collect and upload the files to S3.</p> </li> <li> <p> <code>PENDING</code>: Either the stream session is still in progress, or uploading the exported files to the S3 bucket is in progress.</p> </li> </ul>
            next_token: <p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>. </p>
            identifier: <p>The unique identifier of a Amazon GameLift Streams stream group to retrieve the stream session for. You can use either the stream group ID or the <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a>.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.list_stream_sessions_input.ListStreamSessionsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.list_stream_sessions_output.ListStreamSessionsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_stream_sessions

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.list_stream_sessions.async_list_stream_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_stream_sessions_input.ListStreamSessionsInput = {
            "identifier": identifier
        }
        if status is not None:
            input_["status"] = status
        if export_files_status is not None:
            input_["export_files_status"] = export_files_status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_stream_sessions(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        status: Optional[
            "capo_gameliftstreams.types.stream_session_status.StreamSessionStatus"
        ] = None,
        export_files_status: Optional[
            "capo_gameliftstreams.types.export_files_status.ExportFilesStatus"
        ] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_gameliftstreams.types.stream_session_summary.StreamSessionSummary]":
        _token = next_token
        while True:
            _response = await self.list_stream_sessions(
                identifier,
                config_overrides=config_overrides,
                status=status,
                export_files_status=export_files_status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_stream_sessions_by_account(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        status: Optional[
            "capo_gameliftstreams.types.stream_session_status.StreamSessionStatus"
        ] = None,
        export_files_status: Optional[
            "capo_gameliftstreams.types.export_files_status.ExportFilesStatus"
        ] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_gameliftstreams.types.list_stream_sessions_by_account_output.ListStreamSessionsByAccountOutput":
        r"""<p>Retrieves a list of Amazon GameLift Streams stream sessions that this user account has access to.</p> <p>In the returned list of stream sessions, the <code>ExportFilesMetadata</code> property only shows the <code>Status</code> value. To get the <code>OutpurUri</code> and <code>StatusReason</code> values, use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a>.</p> <p>We don't recommend using this operation to regularly check stream session statuses because it's costly. Instead, to check status updates for a specific stream session, use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a>.</p>

        Args:
            status: <p>Filter by the stream session status. You can specify one status in each request to retrieve only sessions that are currently in that status.</p>
            export_files_status: <p>Filter by the exported files status. You can specify one status in each request to retrieve only sessions that currently have that exported files status.</p>
            next_token: <p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.list_stream_sessions_by_account_input.ListStreamSessionsByAccountInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.list_stream_sessions_by_account_output.ListStreamSessionsByAccountOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_stream_sessions_by_account

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.list_stream_sessions_by_account.async_list_stream_sessions_by_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_stream_sessions_by_account_input.ListStreamSessionsByAccountInput = {}
        if status is not None:
            input_["status"] = status
        if export_files_status is not None:
            input_["export_files_status"] = export_files_status
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_stream_sessions_by_account(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        status: Optional[
            "capo_gameliftstreams.types.stream_session_status.StreamSessionStatus"
        ] = None,
        export_files_status: Optional[
            "capo_gameliftstreams.types.export_files_status.ExportFilesStatus"
        ] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_gameliftstreams.types.stream_session_summary.StreamSessionSummary]":
        _token = next_token
        while True:
            _response = await self.list_stream_sessions_by_account(
                config_overrides=config_overrides,
                status=status,
                export_files_status=export_files_status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_gameliftstreams.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        r"""<p>Retrieves all tags assigned to a Amazon GameLift Streams resource. To list tags for a resource, specify the ARN value for the resource.</p> <p> <b>Learn more</b> </p> <p> <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i> </p> <p> <a href=\"http://aws.amazon.com/answers/account-management/aws-tagging-strategies/\"> Amazon Web Services Tagging Strategies</a> </p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> that you want to retrieve tags for. To get an Amazon GameLift Streams resource ARN, call a List or Get operation for the resource.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_stream_group_locations(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        locations: "capo_gameliftstreams.types.locations_list.LocationsList",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> None:
        r"""<p> Removes a set of remote locations from this stream group. To remove a location, the stream group must be in <code>ACTIVE</code> status. When you remove a location, Amazon GameLift Streams releases allocated compute resources in that location. Stream sessions can no longer start from removed locations in a stream group. Amazon GameLift Streams also deletes the content files of all associated applications that were in Amazon GameLift Streams's internal Amazon S3 bucket at this location. </p> <p> You cannot remove the Amazon Web Services Region location where you initially created this stream group, known as the primary location. However, you can set the stream capacity to zero to avoid incurring costs for allocated compute resources in that location. </p>

        Args:
            identifier: <p> A stream group to remove the specified locations from. </p> <p> This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            locations: <p> A set of locations to remove this stream group. For example, <code>us-east-1</code>.</p> <p> For a complete list of locations that Amazon GameLift Streams supports, refer to <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html\">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.remove_stream_group_locations_input.RemoveStreamGroupLocationsInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_gameliftstreams._operations.game_lift_streams.remove_stream_group_locations

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.remove_stream_group_locations.async_remove_stream_group_locations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.remove_stream_group_locations_input.RemoveStreamGroupLocationsInput = {
            "identifier": identifier,
            "locations": locations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_stream_session(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        protocol: "capo_gameliftstreams.types.protocol.Protocol",
        signal_request: "capo_gameliftstreams.types.signal_request.SignalRequest",
        application_identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        client_token: Optional[
            "capo_gameliftstreams.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_gameliftstreams.types.description.Description"
        ] = None,
        user_id: Optional["capo_gameliftstreams.types.user_id.UserId"] = None,
        locations: Optional[
            "capo_gameliftstreams.types.location_list.LocationList"
        ] = None,
        connection_timeout_seconds: Optional[
            "capo_gameliftstreams.types.connection_timeout_seconds.ConnectionTimeoutSeconds"
        ] = None,
        session_length_seconds: Optional[
            "capo_gameliftstreams.types.session_length_seconds.SessionLengthSeconds"
        ] = None,
        additional_launch_args: Optional[
            "capo_gameliftstreams.types.game_launch_arg_list.GameLaunchArgList"
        ] = None,
        additional_environment_variables: Optional[
            "capo_gameliftstreams.types.environment_variables.EnvironmentVariables"
        ] = None,
        performance_stats_configuration: Optional[
            "capo_gameliftstreams.types.performance_stats_configuration.PerformanceStatsConfiguration"
        ] = None,
    ) -> "capo_gameliftstreams.types.start_stream_session_output.StartStreamSessionOutput":
        r"""<p> This action initiates a new stream session and outputs connection information that clients can use to access the stream. A stream session refers to an instance of a stream that Amazon GameLift Streams transmits from the server to the end-user. A stream session runs on a compute resource that a stream group has allocated. The start stream session process works as follows: </p> <ol> <li> <p>Prerequisites:</p> <ul> <li> <p>You must have a stream group in <code>ACTIVE</code> status</p> </li> <li> <p>You must have idle or on-demand capacity in a stream group in the location you want to stream from</p> </li> <li> <p>You must have at least one application associated to the stream group (use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html\">AssociateApplications</a> if needed)</p> </li> </ul> </li> <li> <p>Start stream request:</p> <ul> <li> <p>Your backend server calls <b>StartStreamSession</b> to initiate connection</p> </li> <li> <p>Amazon GameLift Streams creates the stream session resource, assigns an Amazon Resource Name (ARN) value, and begins searching for available stream capacity to run the stream</p> </li> <li> <p>Session transitions to <code>ACTIVATING</code> status</p> </li> </ul> </li> <li> <p>Placement completion:</p> <ul> <li> <p>If Amazon GameLift Streams is successful in finding capacity for the stream, the stream session status changes to <code>ACTIVE</code> status and <b>StartStreamSession</b> returns stream connection information</p> </li> <li> <p>If Amazon GameLift Streams was not successful in finding capacity within the placement timeout period (defined according to the capacity type and platform type), the stream session status changes to <code>ERROR</code> status and <b>StartStreamSession</b> returns a <code>StatusReason</code> of <code>placementTimeout</code> </p> </li> </ul> </li> <li> <p>Connection completion:</p> <ul> <li> <p>Provide the new connection information to the requesting client</p> </li> <li> <p>Client must establish connection within <code>ConnectionTimeoutSeconds</code> (specified in <b>StartStreamSession</b> parameters)</p> </li> <li> <p>Session terminates automatically if client fails to connect in time</p> </li> </ul> </li> </ol> <p>For more information about the stream session lifecycle, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/stream-sessions.html\">Stream sessions</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> <p>Timeouts to be aware of that affect a stream session:</p> <ul> <li> <p> <b>Placement timeout</b>: The amount of time that Amazon GameLift Streams has to find capacity for a stream request. Placement timeout varies based on the capacity type used to fulfill your stream request:</p> <ul> <li> <p> <b>Always-on capacity</b>: 75 seconds</p> </li> <li> <p> <b>On-demand capacity</b>:</p> <ul> <li> <p>Linux/Proton runtimes: 90 seconds</p> </li> <li> <p>Windows runtime: 10 minutes</p> </li> </ul> </li> </ul> </li> <li> <p> <b>Connection timeout</b>: The amount of time that Amazon GameLift Streams waits for a client to connect to a stream session in <code>ACTIVE</code> status, or reconnect to a stream session in <code>PENDING_CLIENT_RECONNECTION</code> status, the latter of which occurs when a client disconnects or loses connection from a stream session. If no client connects before the timeout, Amazon GameLift Streams terminates the stream session. This value is specified by <code>ConnectionTimeoutSeconds</code> in the <code>StartStreamSession</code> parameters.</p> </li> <li> <p> <b>Maximum session length</b>: A stream session will be terminated after this amount of time has elapsed since it started, regardless of any existing client connections. This value is specified by <code>SessionLengthSeconds</code> in the <code>StartStreamSession</code> parameters.</p> </li> </ul> <p>To start a new stream session, specify a stream group ID and application ID, along with the transport protocol and signal request to use with the stream session.</p> <p>For stream groups that have multiple locations, provide a set of locations ordered by priority using a <code>Locations</code> parameter. Amazon GameLift Streams will start a single stream session in the next available location. An application must be finished replicating to a remote location before the remote location can host a stream.</p> <p>To reconnect to a stream session after a client disconnects or loses connection, use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html\">CreateStreamSessionConnection</a>.</p>

        Args:
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>
            description: <p>A human-readable label for the stream session. You can update this value later.</p>
            identifier: <p>The stream group to run this stream session with.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            protocol: <p>The data transport protocol to use for the stream session.</p>
            signal_request: <p>A WebRTC ICE offer string to use when initializing a WebRTC connection. Typically, the offer is a very long JSON string. Provide the string as a text value in quotes.</p> <p>Amazon GameLift Streams also supports setting the field to \"NO_CLIENT_CONNECTION\". This will create a session without needing any browser request or Web SDK integration. The session starts up as usual and waits for a reconnection from a browser, which is accomplished using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateStreamSessionConnection.html\">CreateStreamSessionConnection</a>.</p>
            application_identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            user_id: <p> An opaque, unique identifier for an end-user, defined by the developer. </p>
            locations: <p> A list of locations, in order of priority, where you want Amazon GameLift Streams to start a stream from. For example, <code>us-east-1</code>. Amazon GameLift Streams selects the location with the next available capacity to start a single stream session in. If this value is empty, Amazon GameLift Streams attempts to start a stream session in the primary location. </p> <p> For a complete list of locations that Amazon GameLift Streams supports, refer to <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html\">Regions, quotas, and limitations</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p>
            connection_timeout_seconds: <p>Length of time (in seconds) that Amazon GameLift Streams should wait for a client to connect or reconnect to the stream session. Applies to both connection and reconnection scenarios. This time span starts when the stream session reaches <code>ACTIVE</code> state. If no client connects before the timeout, Amazon GameLift Streams terminates the stream session. Default value is 120.</p>
            session_length_seconds: <p>The maximum duration of a session. Amazon GameLift Streams will automatically terminate a session after this amount of time has elapsed, regardless of any existing client connections. Default value is 43200 (12 hours).</p>
            additional_launch_args: <p>A list of CLI arguments that are sent to the streaming server when a stream session launches. You can use this to configure the application or stream session details. You can also provide custom arguments that Amazon GameLift Streams passes to your game client.</p> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>
            additional_environment_variables: <p>A set of options that you can use to control the stream session runtime environment, expressed as a set of key-value pairs. You can use this to configure the application or stream session details. You can also provide custom environment variables that Amazon GameLift Streams passes to your game client.</p> <note> <p>If you want to debug your application with environment variables, we recommend that you do so in a local environment outside of Amazon GameLift Streams. For more information, refer to the Compatibility Guidance in the troubleshooting section of the Developer Guide.</p> </note> <p> <code>AdditionalEnvironmentVariables</code> and <code>AdditionalLaunchArgs</code> have similar purposes. <code>AdditionalEnvironmentVariables</code> passes data using environment variables; while <code>AdditionalLaunchArgs</code> passes data using command-line arguments.</p>
            performance_stats_configuration: <p>Configuration settings for sharing the stream session's performance stats with the client</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.start_stream_session_input.StartStreamSessionInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.start_stream_session_output.StartStreamSessionOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.start_stream_session

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.start_stream_session.async_start_stream_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.start_stream_session_input.StartStreamSessionInput = {
            "identifier": identifier,
            "protocol": protocol,
            "signal_request": signal_request,
            "application_identifier": application_identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if user_id is not None:
            input_["user_id"] = user_id
        if locations is not None:
            input_["locations"] = locations
        if connection_timeout_seconds is not None:
            input_["connection_timeout_seconds"] = connection_timeout_seconds
        if session_length_seconds is not None:
            input_["session_length_seconds"] = session_length_seconds
        if additional_launch_args is not None:
            input_["additional_launch_args"] = additional_launch_args
        if additional_environment_variables is not None:
            input_["additional_environment_variables"] = (
                additional_environment_variables
            )
        if performance_stats_configuration is not None:
            input_["performance_stats_configuration"] = performance_stats_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_gameliftstreams.types.arn.Arn",
        tags: "capo_gameliftstreams.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.tag_resource_response.TagResourceResponse":
        r"""<p>Assigns one or more tags to a Amazon GameLift Streams resource. Use tags to organize Amazon Web Services resources for a range of purposes. You can assign tags to the following Amazon GameLift Streams resource types:</p> <ul> <li> <p>Application</p> </li> <li> <p>StreamGroup</p> </li> </ul> <p> <b>Learn more</b> </p> <p> <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i> </p> <p> <a href=\"http://aws.amazon.com/answers/account-management/aws-tagging-strategies/\"> Amazon Web Services Tagging Strategies</a> </p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> of the Amazon GameLift Streams resource that you want to apply tags to.</p>
            tags: <p>A list of tags, in the form of key-value pairs, to assign to the specified Amazon GameLift Streams resource.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.tag_resource

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.tag_resource_request.TagResourceRequest = {
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

    async def terminate_stream_session(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> None:
        r"""<p>Permanently terminates an active stream session. When called, the stream session status changes to <code>TERMINATING</code>. You can terminate a stream session in any status except <code>ACTIVATING</code>. If the stream session is in <code>ACTIVATING</code> status, an exception is thrown.</p>

        Args:
            identifier: <p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p> <p>The stream group that runs this stream session.</p>
            stream_session_identifier: <p> <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.terminate_stream_session_input.TerminateStreamSessionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_gameliftstreams._operations.game_lift_streams.terminate_stream_session

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.terminate_stream_session.async_terminate_stream_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.terminate_stream_session_input.TerminateStreamSessionInput = {
            "identifier": identifier,
            "stream_session_identifier": stream_session_identifier,
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
        resource_arn: "capo_gameliftstreams.types.arn.Arn",
        tag_keys: "capo_gameliftstreams.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.untag_resource_response.UntagResourceResponse":
        r"""<p>Removes one or more tags from a Amazon GameLift Streams resource. To remove tags, specify the Amazon GameLift Streams resource and a list of one or more tags to remove.</p>

        Args:
            resource_arn: <p>The <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> of the Amazon GameLift Streams resource that you want to remove tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the specified Amazon GameLift Streams resource.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.untag_resource

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_application(
        self,
        description: "capo_gameliftstreams.types.description.Description",
        runtime_environment: "capo_gameliftstreams.types.runtime_environment.RuntimeEnvironment",
        executable_path: "capo_gameliftstreams.types.executable_path.ExecutablePath",
        application_source_uri: "capo_gameliftstreams.types.application_source_uri.ApplicationSourceUri",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        application_log_paths: Optional[
            "capo_gameliftstreams.types.file_paths.FilePaths"
        ] = None,
        application_log_output_uri: Optional[
            "capo_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
        ] = None,
        tags: Optional["capo_gameliftstreams.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_gameliftstreams.types.create_application_output.CreateApplicationOutput":
        r"""<p>Creates an application resource in Amazon GameLift Streams, which specifies the application content you want to stream, such as a game build or other software, and configures the settings to run it.</p> <p> Before you create an application, upload your application content files to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see <b>Getting Started</b> in the Amazon GameLift Streams Developer Guide. </p> <important> <p> Make sure that your files in the Amazon S3 bucket are the correct version you want to use. If you change the files at a later time, you will need to create a new Amazon GameLift Streams application. </p> </important> <p> If the request is successful, Amazon GameLift Streams begins to create an application and sets the status to <code>INITIALIZED</code>. When an application reaches <code>READY</code> status, you can use the application to set up stream groups and start streams. To track application status, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html\">GetApplication</a>. </p>

        Args:
            description: <p>A human-readable label for the application. You can update this value later.</p>
            runtime_environment: <p>Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.</p> <p>A runtime environment can be one of the following:</p> <ul> <li> <p> For Linux applications </p> <ul> <li> <p> Ubuntu 22.04 LTS (<code>Type=UBUNTU, Version=22_04_LTS</code>) </p> </li> </ul> </li> <li> <p> For Windows applications </p> <ul> <li> <p>Microsoft Windows Server 2022 Base (<code>Type=WINDOWS, Version=2022</code>)</p> </li> <li> <p>Proton 10.0-4 (<code>Type=PROTON, Version=20260204</code>)</p> </li> <li> <p>Proton 9.0-2 (<code>Type=PROTON, Version=20250516</code>)</p> </li> <li> <p>Proton 8.0-5 (<code>Type=PROTON, Version=20241007</code>)</p> </li> <li> <p>Proton 8.0-2c (<code>Type=PROTON, Version=20230704</code>)</p> </li> </ul> </li> </ul>
            executable_path: <p>The relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the location set in <code>ApplicationSourceUri</code>. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('<code>#!</code>').</p>
            application_source_uri: <p>The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.</p> <p>This value is immutable. To designate a different content location, create a new application.</p> <note> <p>The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same Amazon Web Services Region.</p> </note>
            application_log_paths: <p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>
            application_log_output_uri: <p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template\">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> </note>
            tags: <p>A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html\">TagResource</a> to add tags, <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html\">UntagResource</a> to remove tags, and <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html\">ListTagsForResource</a> to view tags on existing resources.</p>
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.create_application_input.CreateApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.create_application_output.CreateApplicationOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.create_application

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.create_application_input.CreateApplicationInput = {
            "description": description,
            "runtime_environment": runtime_environment,
            "executable_path": executable_path,
            "application_source_uri": application_source_uri,
        }
        if application_log_paths is not None:
            input_["application_log_paths"] = application_log_paths
        if application_log_output_uri is not None:
            input_["application_log_output_uri"] = application_log_output_uri
        if tags is not None:
            input_["tags"] = tags
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

    async def get_application(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.get_application_output.GetApplicationOutput":
        r"""<p>Retrieves properties for an Amazon GameLift Streams application resource. Specify the ID of the application that you want to retrieve. If the operation is successful, it returns properties for the requested application.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.get_application_input.GetApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.get_application_output.GetApplicationOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.get_application

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.get_application_input.GetApplicationInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_application_deleted(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        max_wait_time: float,
        min_delay: float = 2,
        max_delay: float = 120,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> ServiceError:
        r"""Waits until an application is deleted

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_gameliftstreams.types.get_application_output.GetApplicationOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.get_application(  # noqa: F841
                    identifier, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("application_deleted", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def update_application(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        description: Optional[
            "capo_gameliftstreams.types.description.Description"
        ] = None,
        application_log_paths: Optional[
            "capo_gameliftstreams.types.file_paths.FilePaths"
        ] = None,
        application_log_output_uri: Optional[
            "capo_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
        ] = None,
    ) -> "capo_gameliftstreams.types.update_application_output.UpdateApplicationOutput":
        r"""<p> Updates the mutable configuration settings for a Amazon GameLift Streams application resource. You can change the <code>Description</code>, <code>ApplicationLogOutputUri</code>, and <code>ApplicationLogPaths</code>. </p> <p>To update application settings, specify the application ID and provide the new values. If the operation is successful, it returns the complete updated set of settings for the application.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            description: <p>A human-readable label for the application.</p>
            application_log_paths: <p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html\">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>
            application_log_output_uri: <p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template\">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p> </note>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.update_application_input.UpdateApplicationInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.update_application_output.UpdateApplicationOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.update_application

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.update_application_input.UpdateApplicationInput = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if application_log_paths is not None:
            input_["application_log_paths"] = application_log_paths
        if application_log_output_uri is not None:
            input_["application_log_output_uri"] = application_log_output_uri

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_application(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> None:
        r"""<p>Permanently deletes an Amazon GameLift Streams application resource. This also deletes the application content files stored with Amazon GameLift Streams. However, this does not delete the original files that you uploaded to your Amazon S3 bucket; you can delete these any time after Amazon GameLift Streams creates an application, which is the only time Amazon GameLift Streams accesses your Amazon S3 bucket.</p> <p> You can only delete an application that meets the following conditions: </p> <ul> <li> <p>The application is in <code>READY</code> or <code>ERROR</code> status. You cannot delete an application that's in <code>PROCESSING</code> or <code>INITIALIZED</code> status.</p> </li> <li> <p>The application is not the default application of any stream groups. You must first delete the stream group by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html\">DeleteStreamGroup</a>.</p> </li> <li> <p>The application is not linked to any stream groups. You must first unlink the stream group by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html\">DisassociateApplications</a>.</p> </li> <li> <p> An application is not streaming in any ongoing stream session. You must wait until the client ends the stream session or call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html\">TerminateStreamSession</a> to end the stream. </p> </li> </ul> <p>If any active stream groups exist for this application, this request returns a <code>ValidationException</code>. </p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.delete_application_input.DeleteApplicationInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_gameliftstreams._operations.game_lift_streams.delete_application

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.delete_application_input.DeleteApplicationInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_gameliftstreams.types.list_applications_output.ListApplicationsOutput":
        """<p>Retrieves a list of all Amazon GameLift Streams applications that are associated with the Amazon Web Services account in use. This operation returns applications in all statuses, in no particular order. You can paginate the results as needed.</p>

        Args:
            next_token: <p>The token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.list_applications_input.ListApplicationsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.list_applications_output.ListApplicationsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_applications

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_applications_input.ListApplicationsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_gameliftstreams.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_stream_group(
        self,
        description: "capo_gameliftstreams.types.description.Description",
        stream_class: "capo_gameliftstreams.types.stream_class.StreamClass",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        default_application_identifier: Optional[
            "capo_gameliftstreams.types.identifier.Identifier"
        ] = None,
        location_configurations: Optional[
            "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
        ] = None,
        tags: Optional["capo_gameliftstreams.types.tags.Tags"] = None,
        client_token: Optional[
            "capo_gameliftstreams.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_gameliftstreams.types.create_stream_group_output.CreateStreamGroupOutput"
    ):
        r"""<p> Stream groups manage how Amazon GameLift Streams allocates resources and handles concurrent streams, allowing you to effectively manage capacity and costs. Within a stream group, you specify an application to stream, streaming locations and their capacity, and the stream class you want to use when streaming applications to your end-users. A stream class defines the hardware configuration of the compute resources that Amazon GameLift Streams will use when streaming, such as the CPU, GPU, and memory. </p> <p> Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available: </p> <ul> <li> <p> <b>Always-on capacity</b>: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle. </p> </li> <li> <p> <b>Maximum capacity</b>: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released. </p> </li> <li> <p> <b>Target-idle capacity</b>: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state. </p> </li> </ul> <p>Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.</p> <p> To adjust the capacity of any <code>ACTIVE</code> stream group, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html\">UpdateStreamGroup</a>. </p> <p> If the <code>CreateStreamGroup</code> request is successful, Amazon GameLift Streams assigns a unique ID to the stream group resource and sets the status to <code>ACTIVATING</code>. It can take a few minutes for Amazon GameLift Streams to finish creating the stream group while it searches for unallocated compute resources and provisions them. When complete, the stream group status will be <code>ACTIVE</code> and you can start stream sessions by using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_StartStreamSession.html\">StartStreamSession</a>. To check the stream group's status, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamGroup.html\">GetStreamGroup</a>. </p> <p>Stream groups should be recreated every 3-4 weeks to pick up important service updates and fixes. Stream groups that are older than 180 days can no longer be updated with new application associations. Stream groups expire when they are 365 days old, at which point they can no longer stream sessions. The exact expiration date is indicated by the date value in the <code>ExpiresAt</code> field.</p>

        Args:
            description: <p>A descriptive label for the stream group.</p>
            stream_class: <p>The target stream quality for sessions that are hosted in this stream group. Set a stream class that is appropriate to the type of content that you're streaming. Stream class determines the type of computing resources Amazon GameLift Streams uses and impacts the cost of streaming. The following options are available: </p> <p>A stream class can be one of the following:</p> <ul> <li> <p> <b> <code>gen6n_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 64 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra_win2022</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium</code> (NVIDIA, medium)</b> Supports applications with moderate 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 4 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small</code> (NVIDIA, small)</b> Supports applications with lightweight 3D scene complexity and low CPU usage. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 1 vCPUs, 4 GB RAM, 2 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 12 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_medium_win2022</code> (NVIDIA, medium)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 6 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6n_small_win2022</code> (NVIDIA, small)</b> Supports applications with low 3D scene complexity. Powered by NVIDIA L4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 2 vCPUs, 8 GB RAM, 3 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro_win2022</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen6e_pro</code> (NVIDIA, pro)</b> Supports applications with extremely high 3D scene complexity which require maximum resources. Powered by NVIDIA L40S Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 16 vCPUs, 128 GB RAM, 48 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 12 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen5n_ultra</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Powered by NVIDIA A10G Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 24 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_win2022</code> (NVIDIA, ultra)</b> Supports applications with extremely high 3D scene complexity. Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12. Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_high</code> (NVIDIA, high)</b> Supports applications with moderate to high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 4 vCPUs, 16 GB RAM, 8 GB VRAM</p> </li> <li> <p>Tenancy: Supports up to 2 concurrent stream sessions</p> </li> </ul> </li> <li> <p> <b> <code>gen4n_ultra</code> (NVIDIA, ultra)</b> Supports applications with high 3D scene complexity. Powered by NVIDIA T4 Tensor Core GPUs.</p> <ul> <li> <p>Reference resolution: 1080p</p> </li> <li> <p>Reference frame rate: 60 fps</p> </li> <li> <p>Workload specifications: 8 vCPUs, 32 GB RAM, 16 GB VRAM</p> </li> <li> <p>Tenancy: Supports 1 concurrent stream session</p> </li> </ul> </li> </ul>
            default_application_identifier: <p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>If you do not link an application when you create a stream group, you will need to link one later, before you can start streaming, using <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html\">AssociateApplications</a>.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>
            tags: <p>A list of labels to assign to the new stream group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html\">TagResource</a> to add tags, <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html\">UntagResource</a> to remove tags, and <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html\">ListTagsForResource</a> to view tags on existing resources.</p>
            client_token: <p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.create_stream_group_input.CreateStreamGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.create_stream_group_output.CreateStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.create_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.create_stream_group.async_create_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.create_stream_group_input.CreateStreamGroupInput = {
            "description": description,
            "stream_class": stream_class,
        }
        if default_application_identifier is not None:
            input_["default_application_identifier"] = default_application_identifier
        if location_configurations is not None:
            input_["location_configurations"] = location_configurations
        if tags is not None:
            input_["tags"] = tags
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

    async def get_stream_group(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput":
        r"""<p>Retrieves properties for a Amazon GameLift Streams stream group resource. Specify the ID of the stream group that you want to retrieve. If the operation is successful, it returns properties for the requested stream group.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.get_stream_group_input.GetStreamGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.get_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.get_stream_group.async_get_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.get_stream_group_input.GetStreamGroupInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_stream_group_deleted(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        max_wait_time: float,
        min_delay: float = 30,
        max_delay: float = 1800,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> ServiceError:
        r"""Waits until a stream group is deleted

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_gameliftstreams.types.get_stream_group_output.GetStreamGroupOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.get_stream_group(  # noqa: F841
                    identifier, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("stream_group_deleted", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def update_stream_group(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        location_configurations: Optional[
            "capo_gameliftstreams.types.location_configurations.LocationConfigurations"
        ] = None,
        description: Optional[
            "capo_gameliftstreams.types.description.Description"
        ] = None,
        default_application_identifier: Optional[
            "capo_gameliftstreams.types.identifier.Identifier"
        ] = None,
    ) -> (
        "capo_gameliftstreams.types.update_stream_group_output.UpdateStreamGroupOutput"
    ):
        r"""<p> Updates the configuration settings for an Amazon GameLift Streams stream group resource. To update a stream group, it must be in <code>ACTIVE</code> status. You can change the description, the set of locations, and the requested capacity of a stream group per location. If you want to change the stream class, create a new stream group. </p> <p> Stream capacity represents the number of concurrent streams that can be active at a time. You set stream capacity per location, per stream group. The following capacity settings are available: </p> <ul> <li> <p> <b>Always-on capacity</b>: This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle. </p> </li> <li> <p> <b>Maximum capacity</b>: This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released. </p> </li> <li> <p> <b>Target-idle capacity</b>: This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state. </p> </li> </ul> <p>Values for capacity must be whole number multiples of the tenancy value of the stream group's stream class.</p> <p>To update a stream group, specify the stream group's Amazon Resource Name (ARN) and provide the new values. If the request is successful, Amazon GameLift Streams returns the complete updated metadata for the stream group. Expired stream groups cannot be updated.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>
            location_configurations: <p> A set of one or more locations and the streaming capacity for each location. </p>
            description: <p>A descriptive label for the stream group.</p>
            default_application_identifier: <p>The unique identifier of the Amazon GameLift Streams application that you want to set as the default application in a stream group. The application that you specify must be in <code>READY</code> status. The default application is pre-cached on always-on compute resources, reducing stream startup times. Other applications are automatically cached as needed.</p> <p>Note that this parameter only sets the default application in a stream group. To associate a new application to an existing stream group, you must use <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_AssociateApplications.html\">AssociateApplications</a>.</p> <p>When you switch default applications in a stream group, it can take up to a few hours for the new default application to be pre-cached.</p> <p>This value is an <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.update_stream_group_input.UpdateStreamGroupInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.update_stream_group_output.UpdateStreamGroupOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.update_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.update_stream_group.async_update_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.update_stream_group_input.UpdateStreamGroupInput = {
            "identifier": identifier
        }
        if location_configurations is not None:
            input_["location_configurations"] = location_configurations
        if description is not None:
            input_["description"] = description
        if default_application_identifier is not None:
            input_["default_application_identifier"] = default_application_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_stream_group(
        self,
        identifier: "capo_gameliftstreams.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
    ) -> None:
        r"""<p>Permanently deletes all compute resources and information related to a stream group. To delete a stream group, specify the unique stream group identifier. During the deletion process, the stream group's status is <code>DELETING</code>. This operation stops streams in progress and prevents new streams from starting. As a best practice, before deleting the stream group, call <a href=\"https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListStreamSessions.html\">ListStreamSessions</a> to check for streams in progress and take action to stop them. When you delete a stream group, any application associations referring to that stream group are automatically removed.</p>

        Args:
            identifier: <p>An <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html\">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request was not found. Correct the request before you try again.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.delete_stream_group_input.DeleteStreamGroupInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_gameliftstreams._operations.game_lift_streams.delete_stream_group

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.delete_stream_group.async_delete_stream_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.delete_stream_group_input.DeleteStreamGroupInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_stream_groups(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_gameliftstreams.types.list_stream_groups_output.ListStreamGroupsOutput":
        """<p>Retrieves a list of all Amazon GameLift Streams stream groups that are associated with the Amazon Web Services account in use. This operation returns stream groups in all statuses, in no particular order. You can paginate the results as needed.</p>

        Args:
            next_token: <p>A token that marks the start of the next set of results. Use this token when you retrieve results as sequential pages. To get the first page of results, omit a token value. To get the remaining pages, provide the token returned with the previous result set. </p>
            max_results: <p>The number of results to return. Use this parameter with <code>NextToken</code> to return results in sequential pages. Default value is <code>25</code>.</p>

        Raises:
            capo_gameliftstreams.errors.access_denied_exception.AccessDeniedException: <p>You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.</p>
            capo_gameliftstreams.errors.internal_server_exception.InternalServerException: <p>The service encountered an internal error and is unable to complete the request.</p>
            capo_gameliftstreams.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling. Retry the request after the suggested wait time.</p>
            capo_gameliftstreams.errors.validation_exception.ValidationException: <p>One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.</p>
            capo_gameliftstreams.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_gameliftstreams.types.list_stream_groups_input.ListStreamGroupsInput]",
        ) -> AsyncOperationResponse[
            "capo_gameliftstreams.types.list_stream_groups_output.ListStreamGroupsOutput"
        ]:
            import capo_gameliftstreams._operations.game_lift_streams.list_stream_groups

            (
                output,
                http_response,
            ) = await capo_gameliftstreams._operations.game_lift_streams.list_stream_groups.async_list_stream_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gameliftstreams.types.list_stream_groups_input.ListStreamGroupsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_stream_groups(
        self,
        *,
        config_overrides: Optional[AsyncGameLiftStreamsClientConfig] = None,
        next_token: Optional["capo_gameliftstreams.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_gameliftstreams.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_gameliftstreams.types.stream_group_summary.StreamGroupSummary]":
        _token = next_token
        while True:
            _response = await self.list_stream_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
