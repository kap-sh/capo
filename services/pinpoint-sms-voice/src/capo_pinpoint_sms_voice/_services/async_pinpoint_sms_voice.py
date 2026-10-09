"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#PinpointSMSVoice``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_pinpoint_sms_voice._auth._signers
import capo_pinpoint_sms_voice._auth._sigv4
from capo_pinpoint_sms_voice._auth._identity import Credentials
from capo_pinpoint_sms_voice._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_pinpoint_sms_voice._auth._zapros_handler import AuthMiddleware
from capo_pinpoint_sms_voice._services._aws_config import aaws_config
from capo_pinpoint_sms_voice._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice.types.__string
    import capo_pinpoint_sms_voice.types.create_configuration_set_event_destination_request
    import capo_pinpoint_sms_voice.types.create_configuration_set_event_destination_response
    import capo_pinpoint_sms_voice.types.create_configuration_set_request
    import capo_pinpoint_sms_voice.types.create_configuration_set_response
    import capo_pinpoint_sms_voice.types.delete_configuration_set_event_destination_request
    import capo_pinpoint_sms_voice.types.delete_configuration_set_event_destination_response
    import capo_pinpoint_sms_voice.types.delete_configuration_set_request
    import capo_pinpoint_sms_voice.types.delete_configuration_set_response
    import capo_pinpoint_sms_voice.types.event_destination_definition
    import capo_pinpoint_sms_voice.types.get_configuration_set_event_destinations_request
    import capo_pinpoint_sms_voice.types.get_configuration_set_event_destinations_response
    import capo_pinpoint_sms_voice.types.list_configuration_sets_request
    import capo_pinpoint_sms_voice.types.list_configuration_sets_response
    import capo_pinpoint_sms_voice.types.non_empty_string
    import capo_pinpoint_sms_voice.types.send_voice_message_request
    import capo_pinpoint_sms_voice.types.send_voice_message_response
    import capo_pinpoint_sms_voice.types.string
    import capo_pinpoint_sms_voice.types.update_configuration_set_event_destination_request
    import capo_pinpoint_sms_voice.types.update_configuration_set_event_destination_response
    import capo_pinpoint_sms_voice.types.voice_message_content
    import capo_pinpoint_sms_voice.types.word_characters_with_delimiters


class AsyncPinpointSMSVoiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncPinpointSMSVoiceClient:
    """A client for the ``PinpointSMSVoice`` service.

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
        self._config = AsyncPinpointSMSVoiceClientConfig(
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
        self, config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncPinpointSMSVoiceClientConfig = config_overrides or {}
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

    async def create_configuration_set(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice.types.word_characters_with_delimiters.WordCharactersWithDelimiters"
        ] = None,
    ) -> "capo_pinpoint_sms_voice.types.create_configuration_set_response.CreateConfigurationSetResponse":
        """Create a new configuration set. After you create the configuration set, you can add one or more event destinations to it.

        Args:
            configuration_set_name: The name that you want to give the configuration set.

        Raises:
            capo_pinpoint_sms_voice.errors.already_exists_exception.AlreadyExistsException: The resource specified in your request already exists.
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.limit_exceeded_exception.LimitExceededException: There are too many instances of the specified resource type.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.create_configuration_set_request.CreateConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.create_configuration_set_response.CreateConfigurationSetResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.create_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.create_configuration_set.async_create_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.create_configuration_set_request.CreateConfigurationSetRequest = {}
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
        event_destination: Optional[
            "capo_pinpoint_sms_voice.types.event_destination_definition.EventDestinationDefinition"
        ] = None,
        event_destination_name: Optional[
            "capo_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_pinpoint_sms_voice.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse":
        """Create a new event destination in a configuration set.

        Args:
            configuration_set_name: ConfigurationSetName
            event_destination_name: A name that identifies the event destination.

        Raises:
            capo_pinpoint_sms_voice.errors.already_exists_exception.AlreadyExistsException: The resource specified in your request already exists.
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.limit_exceeded_exception.LimitExceededException: There are too many instances of the specified resource type.
            capo_pinpoint_sms_voice.errors.not_found_exception.NotFoundException: The resource you attempted to access doesn't exist.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.create_configuration_set_event_destination_response.CreateConfigurationSetEventDestinationResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.create_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.create_configuration_set_event_destination.async_create_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.create_configuration_set_event_destination_request.CreateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name
        }
        if event_destination is not None:
            input_["event_destination"] = event_destination
        if event_destination_name is not None:
            input_["event_destination_name"] = event_destination_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice.types.delete_configuration_set_response.DeleteConfigurationSetResponse":
        """Deletes an existing configuration set.

        Args:
            configuration_set_name: ConfigurationSetName

        Raises:
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.not_found_exception.NotFoundException: The resource you attempted to access doesn't exist.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.delete_configuration_set_request.DeleteConfigurationSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.delete_configuration_set_response.DeleteConfigurationSetResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.delete_configuration_set

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.delete_configuration_set.async_delete_configuration_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.delete_configuration_set_request.DeleteConfigurationSetRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string",
        event_destination_name: "capo_pinpoint_sms_voice.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse":
        """Deletes an event destination in a configuration set.

        Args:
            configuration_set_name: ConfigurationSetName
            event_destination_name: EventDestinationName

        Raises:
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.not_found_exception.NotFoundException: The resource you attempted to access doesn't exist.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.delete_configuration_set_event_destination_response.DeleteConfigurationSetEventDestinationResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.delete_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.delete_configuration_set_event_destination.async_delete_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.delete_configuration_set_event_destination_request.DeleteConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_configuration_set_event_destinations(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
    ) -> "capo_pinpoint_sms_voice.types.get_configuration_set_event_destinations_response.GetConfigurationSetEventDestinationsResponse":
        """Obtain information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination.

        Args:
            configuration_set_name: ConfigurationSetName

        Raises:
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.not_found_exception.NotFoundException: The resource you attempted to access doesn't exist.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.get_configuration_set_event_destinations_request.GetConfigurationSetEventDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.get_configuration_set_event_destinations_response.GetConfigurationSetEventDestinationsResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.get_configuration_set_event_destinations

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.get_configuration_set_event_destinations.async_get_configuration_set_event_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.get_configuration_set_event_destinations_request.GetConfigurationSetEventDestinationsRequest = {
            "configuration_set_name": configuration_set_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_configuration_sets(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
        next_token: Optional["capo_pinpoint_sms_voice.types.__string.__string"] = None,
        page_size: Optional["capo_pinpoint_sms_voice.types.__string.__string"] = None,
    ) -> "capo_pinpoint_sms_voice.types.list_configuration_sets_response.ListConfigurationSetsResponse":
        """List all of the configuration sets associated with your Amazon Pinpoint account in the current region.

        Args:
            next_token: A token returned from a previous call to the API that indicates the position in the list of results.
            page_size: Used to specify the number of items that should be returned in the response.

        Raises:
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.list_configuration_sets_request.ListConfigurationSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.list_configuration_sets_response.ListConfigurationSetsResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.list_configuration_sets

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.list_configuration_sets.async_list_configuration_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.list_configuration_sets_request.ListConfigurationSetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if page_size is not None:
            input_["page_size"] = page_size

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_voice_message(
        self,
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
        caller_id: Optional["capo_pinpoint_sms_voice.types.string.String"] = None,
        configuration_set_name: Optional[
            "capo_pinpoint_sms_voice.types.word_characters_with_delimiters.WordCharactersWithDelimiters"
        ] = None,
        content: Optional[
            "capo_pinpoint_sms_voice.types.voice_message_content.VoiceMessageContent"
        ] = None,
        destination_phone_number: Optional[
            "capo_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
        ] = None,
        origination_phone_number: Optional[
            "capo_pinpoint_sms_voice.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_pinpoint_sms_voice.types.send_voice_message_response.SendVoiceMessageResponse":
        """Create a new voice message and send it to a recipient's phone number.

        Args:
            caller_id: The phone number that appears on recipients' devices when they receive the message.
            configuration_set_name: The name of the configuration set that you want to use to send the message.
            destination_phone_number: The phone number that you want to send the voice message to.
            origination_phone_number: The phone number that Amazon Pinpoint should use to send the voice message. This isn't necessarily the phone number that appears on recipients' devices when they receive the message, because you can specify a CallerId parameter in the request.

        Raises:
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.send_voice_message_request.SendVoiceMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.send_voice_message_response.SendVoiceMessageResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.send_voice_message

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.send_voice_message.async_send_voice_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.send_voice_message_request.SendVoiceMessageRequest = {}
        if caller_id is not None:
            input_["caller_id"] = caller_id
        if configuration_set_name is not None:
            input_["configuration_set_name"] = configuration_set_name
        if content is not None:
            input_["content"] = content
        if destination_phone_number is not None:
            input_["destination_phone_number"] = destination_phone_number
        if origination_phone_number is not None:
            input_["origination_phone_number"] = origination_phone_number

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_configuration_set_event_destination(
        self,
        configuration_set_name: "capo_pinpoint_sms_voice.types.__string.__string",
        event_destination_name: "capo_pinpoint_sms_voice.types.__string.__string",
        *,
        config_overrides: Optional[AsyncPinpointSMSVoiceClientConfig] = None,
        event_destination: Optional[
            "capo_pinpoint_sms_voice.types.event_destination_definition.EventDestinationDefinition"
        ] = None,
    ) -> "capo_pinpoint_sms_voice.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse":
        """Update an event destination in a configuration set. An event destination is a location that you publish information about your voice calls to. For example, you can log an event to an Amazon CloudWatch destination when a call fails.

        Args:
            configuration_set_name: ConfigurationSetName
            event_destination_name: EventDestinationName

        Raises:
            capo_pinpoint_sms_voice.errors.bad_request_exception.BadRequestException: The input you provided is invalid.
            capo_pinpoint_sms_voice.errors.internal_service_error_exception.InternalServiceErrorException: The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
            capo_pinpoint_sms_voice.errors.not_found_exception.NotFoundException: The resource you attempted to access doesn't exist.
            capo_pinpoint_sms_voice.errors.too_many_requests_exception.TooManyRequestsException: You've issued too many requests to the resource. Wait a few minutes, and then try again.
            capo_pinpoint_sms_voice.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_pinpoint_sms_voice.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_pinpoint_sms_voice.types.update_configuration_set_event_destination_response.UpdateConfigurationSetEventDestinationResponse"
        ]:
            import capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.update_configuration_set_event_destination

            (
                output,
                http_response,
            ) = await capo_pinpoint_sms_voice._operations.pinpoint_sms_voice.update_configuration_set_event_destination.async_update_configuration_set_event_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_pinpoint_sms_voice.types.update_configuration_set_event_destination_request.UpdateConfigurationSetEventDestinationRequest = {
            "configuration_set_name": configuration_set_name,
            "event_destination_name": event_destination_name,
        }
        if event_destination is not None:
            input_["event_destination"] = event_destination

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
