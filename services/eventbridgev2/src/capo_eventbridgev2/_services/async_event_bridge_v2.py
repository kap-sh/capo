"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#AWSEventsV2``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_eventbridgev2._auth._signers
import capo_eventbridgev2._auth._sigv4
from capo_eventbridgev2._auth._identity import Credentials
from capo_eventbridgev2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_eventbridgev2._auth._zapros_handler import AuthMiddleware
from capo_eventbridgev2._pagination import resolve_path as _resolve_path
from capo_eventbridgev2._services._aws_config import aaws_config
from capo_eventbridgev2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_eventbridgev2.types.account_id
    import capo_eventbridgev2.types.batch_configuration
    import capo_eventbridgev2.types.client_token
    import capo_eventbridgev2.types.create_event_bus_request
    import capo_eventbridgev2.types.create_event_bus_response
    import capo_eventbridgev2.types.create_event_source_request
    import capo_eventbridgev2.types.create_event_source_response
    import capo_eventbridgev2.types.create_subscriber_request
    import capo_eventbridgev2.types.create_subscriber_response
    import capo_eventbridgev2.types.deduplication_configuration
    import capo_eventbridgev2.types.delete_event_bus_request
    import capo_eventbridgev2.types.delete_event_bus_response
    import capo_eventbridgev2.types.delete_event_source_request
    import capo_eventbridgev2.types.delete_event_source_response
    import capo_eventbridgev2.types.delete_resource_policy_request
    import capo_eventbridgev2.types.delete_resource_policy_response
    import capo_eventbridgev2.types.delete_subscriber_request
    import capo_eventbridgev2.types.delete_subscriber_response
    import capo_eventbridgev2.types.describe_event_bus_request
    import capo_eventbridgev2.types.describe_event_bus_response
    import capo_eventbridgev2.types.describe_event_source_request
    import capo_eventbridgev2.types.describe_event_source_response
    import capo_eventbridgev2.types.describe_subscriber_request
    import capo_eventbridgev2.types.describe_subscriber_response
    import capo_eventbridgev2.types.description
    import capo_eventbridgev2.types.encryption_configuration
    import capo_eventbridgev2.types.event_bus_arn
    import capo_eventbridgev2.types.event_bus_name
    import capo_eventbridgev2.types.event_bus_summary
    import capo_eventbridgev2.types.event_source_arn
    import capo_eventbridgev2.types.event_source_configuration
    import capo_eventbridgev2.types.event_source_name
    import capo_eventbridgev2.types.event_source_summary
    import capo_eventbridgev2.types.filter_configuration
    import capo_eventbridgev2.types.get_resource_policy_request
    import capo_eventbridgev2.types.get_resource_policy_response
    import capo_eventbridgev2.types.invoke_configuration
    import capo_eventbridgev2.types.list_event_buses_request
    import capo_eventbridgev2.types.list_event_buses_response
    import capo_eventbridgev2.types.list_event_sources_request
    import capo_eventbridgev2.types.list_event_sources_response
    import capo_eventbridgev2.types.list_resource_policies_request
    import capo_eventbridgev2.types.list_resource_policies_response
    import capo_eventbridgev2.types.list_subscribers_request
    import capo_eventbridgev2.types.list_subscribers_response
    import capo_eventbridgev2.types.list_tags_for_resource_request
    import capo_eventbridgev2.types.list_tags_for_resource_response
    import capo_eventbridgev2.types.log_configuration
    import capo_eventbridgev2.types.max_results
    import capo_eventbridgev2.types.next_token
    import capo_eventbridgev2.types.on_failure_configuration
    import capo_eventbridgev2.types.ordering_type
    import capo_eventbridgev2.types.point_in_time_configuration
    import capo_eventbridgev2.types.policy_document
    import capo_eventbridgev2.types.policy_name
    import capo_eventbridgev2.types.policy_revision_id
    import capo_eventbridgev2.types.put_events_request
    import capo_eventbridgev2.types.put_events_request_entry_list
    import capo_eventbridgev2.types.put_events_response
    import capo_eventbridgev2.types.put_raw_events_request
    import capo_eventbridgev2.types.put_raw_events_request_entry_list
    import capo_eventbridgev2.types.put_raw_events_response
    import capo_eventbridgev2.types.put_resource_policy_request
    import capo_eventbridgev2.types.put_resource_policy_response
    import capo_eventbridgev2.types.resource_policy_summary
    import capo_eventbridgev2.types.resume_position
    import capo_eventbridgev2.types.retry_policy
    import capo_eventbridgev2.types.revocable_resource_arn
    import capo_eventbridgev2.types.revoke_resource_request
    import capo_eventbridgev2.types.revoke_resource_response
    import capo_eventbridgev2.types.schema_registry_configuration
    import capo_eventbridgev2.types.starting_position
    import capo_eventbridgev2.types.storage_configuration
    import capo_eventbridgev2.types.subscriber_arn
    import capo_eventbridgev2.types.subscriber_name
    import capo_eventbridgev2.types.subscriber_state
    import capo_eventbridgev2.types.subscriber_summary
    import capo_eventbridgev2.types.tag_key_list
    import capo_eventbridgev2.types.tag_map
    import capo_eventbridgev2.types.tag_resource_request
    import capo_eventbridgev2.types.tag_resource_response
    import capo_eventbridgev2.types.taggable_resource_arn
    import capo_eventbridgev2.types.transformer
    import capo_eventbridgev2.types.untag_resource_request
    import capo_eventbridgev2.types.untag_resource_response
    import capo_eventbridgev2.types.update_event_bus_request
    import capo_eventbridgev2.types.update_event_bus_response
    import capo_eventbridgev2.types.update_event_source_request
    import capo_eventbridgev2.types.update_event_source_response
    import capo_eventbridgev2.types.update_invoke_configuration
    import capo_eventbridgev2.types.update_subscriber_request
    import capo_eventbridgev2.types.update_subscriber_response


class AsyncEventBridgeV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    endpoint: str | None
    use_fips: bool | None
    use_dual_stack: bool | None
    account_id: str | None
    account_id_endpoint_mode: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncEventBridgeV2Client:
    """A client for the ``EventBridgeV2`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        account_id: The value of the ``AWS::Auth::AccountId`` endpoint parameter.
        account_id_endpoint_mode: The value of the ``AWS::Auth::AccountIdEndpointMode`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        use_fips: bool | None = None,
        use_dual_stack: bool | None = None,
        account_id: str | None = None,
        account_id_endpoint_mode: str | None = None,
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
        self._config = AsyncEventBridgeV2ClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "endpoint": endpoint,
                "use_fips": use_fips,
                "use_dual_stack": use_dual_stack,
                "account_id": account_id,
                "account_id_endpoint_mode": account_id_endpoint_mode,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncEventBridgeV2ClientConfig = config_overrides or {}
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
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            account_id=overrides.get("account_id", self._config.get("account_id")),
            account_id_endpoint_mode=overrides.get(
                "account_id_endpoint_mode", self._config.get("account_id_endpoint_mode")
            ),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def create_event_bus(
        self,
        name: "capo_eventbridgev2.types.event_bus_name.EventBusName",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        description: Optional[
            "capo_eventbridgev2.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_eventbridgev2.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_configuration: Optional[
            "capo_eventbridgev2.types.storage_configuration.StorageConfiguration"
        ] = None,
        tags: Optional["capo_eventbridgev2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_eventbridgev2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_eventbridgev2.types.create_event_bus_response.CreateEventBusResponse":
        """Creates an event bus. Provisioning is asynchronous: the bus is returned in the CREATING state and transitions to ACTIVE when ready (see the EventBusActive waiter). Retries carrying the same ClientToken are idempotent.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: The request reuses the client token of an earlier request with different parameters. Use a new client token, or resend the earlier request unchanged.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.limit_exceeded_exception.LimitExceededException: The request would exceed a service quota for the account.
            capo_eventbridgev2.errors.resource_already_exists_exception.ResourceAlreadyExistsException: A resource with the same name already exists.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.create_event_bus_request.CreateEventBusRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.create_event_bus_response.CreateEventBusResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.create_event_bus

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.create_event_bus.async_create_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.create_event_bus_request.CreateEventBusRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration
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

    async def create_event_source(
        self,
        name: "capo_eventbridgev2.types.event_source_name.EventSourceName",
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        configuration: "capo_eventbridgev2.types.event_source_configuration.EventSourceConfiguration",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        description: Optional[
            "capo_eventbridgev2.types.description.Description"
        ] = None,
        tags: Optional["capo_eventbridgev2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_eventbridgev2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_eventbridgev2.types.create_event_source_response.CreateEventSourceResponse":
        """Creates an EventSource, which forwards events from an origin (an AWS service or another account) onto an event bus. The bus must be ACTIVE. Retries carrying the same ClientToken are idempotent.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: The request reuses the client token of an earlier request with different parameters. Use a new client token, or resend the earlier request unchanged.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.limit_exceeded_exception.LimitExceededException: The request would exceed a service quota for the account.
            capo_eventbridgev2.errors.resource_already_exists_exception.ResourceAlreadyExistsException: A resource with the same name already exists.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.create_event_source_request.CreateEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.create_event_source_response.CreateEventSourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.create_event_source

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.create_event_source.async_create_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.create_event_source_request.CreateEventSourceRequest = {
            "name": name,
            "event_bus_arn": event_bus_arn,
            "configuration": configuration,
        }
        if description is not None:
            input_["description"] = description
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

    async def create_subscriber(
        self,
        name: "capo_eventbridgev2.types.subscriber_name.SubscriberName",
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        invoke_configuration: "capo_eventbridgev2.types.invoke_configuration.InvokeConfiguration",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        description: Optional[
            "capo_eventbridgev2.types.description.Description"
        ] = None,
        filter_configuration: Optional[
            "capo_eventbridgev2.types.filter_configuration.FilterConfiguration"
        ] = None,
        type: Optional["capo_eventbridgev2.types.ordering_type.OrderingType"] = None,
        starting_position: Optional[
            "capo_eventbridgev2.types.starting_position.StartingPosition"
        ] = None,
        point_in_time_configuration: Optional[
            "capo_eventbridgev2.types.point_in_time_configuration.PointInTimeConfiguration"
        ] = None,
        batch_configuration: Optional[
            "capo_eventbridgev2.types.batch_configuration.BatchConfiguration"
        ] = None,
        transformer: Optional[
            "capo_eventbridgev2.types.transformer.Transformer"
        ] = None,
        retry_policy: Optional[
            "capo_eventbridgev2.types.retry_policy.RetryPolicy"
        ] = None,
        on_failure_configuration: Optional[
            "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
        ] = None,
        log_configuration: Optional[
            "capo_eventbridgev2.types.log_configuration.LogConfiguration"
        ] = None,
        state: Optional[
            "capo_eventbridgev2.types.subscriber_state.SubscriberState"
        ] = None,
        tags: Optional["capo_eventbridgev2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_eventbridgev2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_eventbridgev2.types.create_subscriber_response.CreateSubscriberResponse":
        """Creates a subscriber on an event bus, which delivers matching events to the configured target. The bus must be ACTIVE. Retries carrying the same ClientToken are idempotent.

        Args:
            transformer: Not applicable to universal (aws-sdk) targets, whose input transformation is UniversalTargetParameters.Input; a Transformer on such a target is rejected.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: The request reuses the client token of an earlier request with different parameters. Use a new client token, or resend the earlier request unchanged.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.limit_exceeded_exception.LimitExceededException: The request would exceed a service quota for the account.
            capo_eventbridgev2.errors.resource_already_exists_exception.ResourceAlreadyExistsException: A resource with the same name already exists.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.create_subscriber_request.CreateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.create_subscriber_response.CreateSubscriberResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.create_subscriber

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.create_subscriber.async_create_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.create_subscriber_request.CreateSubscriberRequest = {
            "name": name,
            "event_bus_arn": event_bus_arn,
            "invoke_configuration": invoke_configuration,
        }
        if description is not None:
            input_["description"] = description
        if filter_configuration is not None:
            input_["filter_configuration"] = filter_configuration
        if type is not None:
            input_["type"] = type
        if starting_position is not None:
            input_["starting_position"] = starting_position
        if point_in_time_configuration is not None:
            input_["point_in_time_configuration"] = point_in_time_configuration
        if batch_configuration is not None:
            input_["batch_configuration"] = batch_configuration
        if transformer is not None:
            input_["transformer"] = transformer
        if retry_policy is not None:
            input_["retry_policy"] = retry_policy
        if on_failure_configuration is not None:
            input_["on_failure_configuration"] = on_failure_configuration
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if state is not None:
            input_["state"] = state
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

    async def delete_event_bus(
        self,
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.delete_event_bus_response.DeleteEventBusResponse":
        """Deletes an event bus. Deletion is asynchronous: the bus moves to DELETING and disappears when complete (see the EventBusDeleted waiter). A bus with subscribers or event sources cannot be deleted.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_in_use_exception.ResourceInUseException: The resource is in use and cannot be deleted. For example, an event bus with subscribers or event sources cannot be deleted until they are deleted.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.delete_event_bus_request.DeleteEventBusRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.delete_event_bus_response.DeleteEventBusResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.delete_event_bus

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.delete_event_bus.async_delete_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.delete_event_bus_request.DeleteEventBusRequest = {
            "event_bus_arn": event_bus_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event_source(
        self,
        event_source_arn: "capo_eventbridgev2.types.event_source_arn.EventSourceArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.delete_event_source_response.DeleteEventSourceResponse":
        """Deletes an EventSource. Forwarding from its origin stops.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.delete_event_source_request.DeleteEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.delete_event_source_response.DeleteEventSourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.delete_event_source

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.delete_event_source.async_delete_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.delete_event_source_request.DeleteEventSourceRequest = {
            "event_source_arn": event_source_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        policy_name: Optional["capo_eventbridgev2.types.policy_name.PolicyName"] = None,
        expected_revision_id: Optional[
            "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_eventbridgev2.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """Deletes the named resource policy attached to an event bus.

        Args:
            policy_name: Which named policy to delete. Defaults to "default" when omitted (a delete AWS Resource Access Manager makes on the owner's behalf resolves to "AWS_RAM" instead). The two writers are exclusive in both directions — only Resource Access Manager can delete "AWS_RAM", and only the bus owner can delete "default" — so naming the other party's policy fails with AccessDeniedException. A well-formed name that is neither of the two fails with InvalidInputException.
            expected_revision_id: The delete succeeds only if the named policy's current revision ID matches this value; if it differs or the policy does not exist, the operation fails with ConflictException. The "NO_POLICY" sentinel is not valid here. When omitted, deleting an absent policy is an idempotent success. Supplying this value makes the delete non-idempotent: once it succeeds the expected revision no longer exists, so retrying an unanswered request fails with ConflictException even though the policy was deleted. To establish the outcome, read the policy back: ResourceNotFoundException means the delete took effect.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.conflict_exception.ConflictException: A client-supplied precondition (e.g. ExpectedRevisionId on a resource-policy write) did not match the current state of the resource. Retrying the same request will fail again; re-read the resource and re-evaluate before retrying. A conditional request is not retry-safe on its own. If an earlier attempt committed but its response never reached the caller, retrying fails with this error, which is indistinguishable from another writer having won. Compare the resource's current contents with what the request intended: a successful attempt stores a revision ID the caller never saw, so the revision alone cannot tell the two apart, but matching contents mean the change took effect.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscriber(
        self,
        subscriber_arn: "capo_eventbridgev2.types.subscriber_arn.SubscriberArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.delete_subscriber_response.DeleteSubscriberResponse":
        """Deletes a subscriber. Events are no longer delivered to its target.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.delete_subscriber_request.DeleteSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.delete_subscriber_response.DeleteSubscriberResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.delete_subscriber

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.delete_subscriber.async_delete_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.delete_subscriber_request.DeleteSubscriberRequest = {
            "subscriber_arn": subscriber_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_event_bus(
        self,
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> (
        "capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse"
    ):
        """Returns the full configuration and lifecycle state of an event bus.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.describe_event_bus_request.DescribeEventBusRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.describe_event_bus_response.DescribeEventBusResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.describe_event_bus

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.describe_event_bus.async_describe_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.describe_event_bus_request.DescribeEventBusRequest = {
            "event_bus_arn": event_bus_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_event_source(
        self,
        event_source_arn: "capo_eventbridgev2.types.event_source_arn.EventSourceArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.describe_event_source_response.DescribeEventSourceResponse":
        """Returns the full configuration and lifecycle state of an EventSource.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.describe_event_source_request.DescribeEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.describe_event_source_response.DescribeEventSourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.describe_event_source

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.describe_event_source.async_describe_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.describe_event_source_request.DescribeEventSourceRequest = {
            "event_source_arn": event_source_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_subscriber(
        self,
        subscriber_arn: "capo_eventbridgev2.types.subscriber_arn.SubscriberArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.describe_subscriber_response.DescribeSubscriberResponse":
        """Returns the full configuration and state of a subscriber.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.describe_subscriber_request.DescribeSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.describe_subscriber_response.DescribeSubscriberResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.describe_subscriber

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.describe_subscriber.async_describe_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.describe_subscriber_request.DescribeSubscriberRequest = {
            "subscriber_arn": subscriber_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        policy_name: Optional["capo_eventbridgev2.types.policy_name.PolicyName"] = None,
    ) -> "capo_eventbridgev2.types.get_resource_policy_response.GetResourcePolicyResponse":
        """Returns the named resource policy attached to an event bus. Fails with ResourceNotFoundException when the event bus or the named policy does not exist.

        Args:
            policy_name: Which named policy to read. Defaults to "default" when omitted (a read AWS Resource Access Manager makes on the owner's behalf resolves to "AWS_RAM" instead). Unlike writing, neither name is reserved on a read: the bus owner can read both. There is no fallback between the two, so a bus shared only through Resource Access Manager fails with ResourceNotFoundException until "AWS_RAM" is named explicitly. A well-formed name that is neither of the two fails with InvalidInputException.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }
        if policy_name is not None:
            input_["policy_name"] = policy_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_event_buses(
        self,
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        name_prefix: Optional[
            "capo_eventbridgev2.types.event_bus_name.EventBusName"
        ] = None,
        event_bus_account_id: Optional[
            "capo_eventbridgev2.types.account_id.AccountId"
        ] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "capo_eventbridgev2.types.list_event_buses_response.ListEventBusesResponse":
        """Lists the event buses visible to the caller: buses the account owns and buses shared with it through AWS RAM. Shared entries carry identity fields only (Name, EventBusArn, EventBusAccountId); owned entries carry every summary field. Set EventBusAccountId to scope the list to one owner account.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.list_event_buses_request.ListEventBusesRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.list_event_buses_response.ListEventBusesResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.list_event_buses

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.list_event_buses.async_list_event_buses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.list_event_buses_request.ListEventBusesRequest = {}
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
        if event_bus_account_id is not None:
            input_["event_bus_account_id"] = event_bus_account_id
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

    async def iter_list_event_buses(
        self,
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        name_prefix: Optional[
            "capo_eventbridgev2.types.event_bus_name.EventBusName"
        ] = None,
        event_bus_account_id: Optional[
            "capo_eventbridgev2.types.account_id.AccountId"
        ] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_eventbridgev2.types.event_bus_summary.EventBusSummary]":
        _token = next_token
        while True:
            _response = await self.list_event_buses(
                config_overrides=config_overrides,
                name_prefix=name_prefix,
                event_bus_account_id=event_bus_account_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_buses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_event_sources(
        self,
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        event_bus_arn: Optional[
            "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
        ] = None,
        name_prefix: Optional[
            "capo_eventbridgev2.types.event_source_name.EventSourceName"
        ] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_eventbridgev2.types.list_event_sources_response.ListEventSourcesResponse"
    ):
        """Lists EventSources as summaries. By default the list spans the EventSources the caller account owns; set EventBusArn to scope it to one bus. Use DescribeEventSource to retrieve full configuration.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.list_event_sources_request.ListEventSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.list_event_sources_response.ListEventSourcesResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.list_event_sources

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.list_event_sources.async_list_event_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.list_event_sources_request.ListEventSourcesRequest = {}
        if event_bus_arn is not None:
            input_["event_bus_arn"] = event_bus_arn
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
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

    async def iter_list_event_sources(
        self,
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        event_bus_arn: Optional[
            "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
        ] = None,
        name_prefix: Optional[
            "capo_eventbridgev2.types.event_source_name.EventSourceName"
        ] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_eventbridgev2.types.event_source_summary.EventSourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_event_sources(
                config_overrides=config_overrides,
                event_bus_arn=event_bus_arn,
                name_prefix=name_prefix,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_policies(
        self,
        resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "capo_eventbridgev2.types.list_resource_policies_response.ListResourcePoliciesResponse":
        """Lists the resource policies attached to an event bus as summaries (policy name and revision ID). Use GetResourcePolicy to retrieve a policy document.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.list_resource_policies_request.ListResourcePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.list_resource_policies_response.ListResourcePoliciesResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.list_resource_policies

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.list_resource_policies.async_list_resource_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.list_resource_policies_request.ListResourcePoliciesRequest = {
            "resource_arn": resource_arn
        }
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

    async def iter_list_resource_policies(
        self,
        resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_eventbridgev2.types.resource_policy_summary.ResourcePolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_resource_policies(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscribers(
        self,
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        event_bus_arn: Optional[
            "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
        ] = None,
        name_prefix: Optional[
            "capo_eventbridgev2.types.subscriber_name.SubscriberName"
        ] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "capo_eventbridgev2.types.list_subscribers_response.ListSubscribersResponse":
        """Lists subscribers as summaries. By default the list spans the subscribers the caller account owns across all buses; set EventBusArn to scope it to one bus. Use DescribeSubscriber to retrieve full configuration.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.list_subscribers_request.ListSubscribersRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.list_subscribers_response.ListSubscribersResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.list_subscribers

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.list_subscribers.async_list_subscribers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.list_subscribers_request.ListSubscribersRequest = {}
        if event_bus_arn is not None:
            input_["event_bus_arn"] = event_bus_arn
        if name_prefix is not None:
            input_["name_prefix"] = name_prefix
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

    async def iter_list_subscribers(
        self,
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        event_bus_arn: Optional[
            "capo_eventbridgev2.types.event_bus_arn.EventBusArn"
        ] = None,
        name_prefix: Optional[
            "capo_eventbridgev2.types.subscriber_name.SubscriberName"
        ] = None,
        next_token: Optional["capo_eventbridgev2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_eventbridgev2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_eventbridgev2.types.subscriber_summary.SubscriberSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscribers(
                config_overrides=config_overrides,
                event_bus_arn=event_bus_arn,
                name_prefix=name_prefix,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("subscribers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_eventbridgev2.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Lists the tags on an event bus, subscriber, or event source.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_events(
        self,
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        entries: "capo_eventbridgev2.types.put_events_request_entry_list.PutEventsRequestEntryList",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        deduplication_configuration: Optional[
            "capo_eventbridgev2.types.deduplication_configuration.DeduplicationConfiguration"
        ] = None,
    ) -> "capo_eventbridgev2.types.put_events_response.PutEventsResponse":
        """Publishes events to an event bus.

        Args:
            deduplication_configuration: Request-level deduplication settings, applied to every entry in the batch.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.put_events_request.PutEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.put_events_response.PutEventsResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.put_events

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.put_events.async_put_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.put_events_request.PutEventsRequest = {
            "event_bus_arn": event_bus_arn,
            "entries": entries,
        }
        if deduplication_configuration is not None:
            input_["deduplication_configuration"] = deduplication_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_raw_events(
        self,
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        entries: "capo_eventbridgev2.types.put_raw_events_request_entry_list.PutRawEventsRequestEntryList",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        schema_registry_configuration: Optional[
            "capo_eventbridgev2.types.schema_registry_configuration.SchemaRegistryConfiguration"
        ] = None,
        deduplication_configuration: Optional[
            "capo_eventbridgev2.types.deduplication_configuration.DeduplicationConfiguration"
        ] = None,
    ) -> "capo_eventbridgev2.types.put_raw_events_response.PutRawEventsResponse":
        """Publishes pre-shaped events to an event bus.

        Args:
            schema_registry_configuration: Schema-registry settings for encoding open-format (Avro/Protobuf) events. Required for open-format entries; ignored for JSON entries. The registry is read with the caller's credentials, so the caller needs read access to the registry it references.
            deduplication_configuration: Request-level deduplication settings, applied to every entry in the batch.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.schema_registry_unavailable_exception.SchemaRegistryUnavailableException: The configured schema registry could not be reached. Retry the request.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.put_raw_events_request.PutRawEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.put_raw_events_response.PutRawEventsResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.put_raw_events

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.put_raw_events.async_put_raw_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.put_raw_events_request.PutRawEventsRequest = {
            "event_bus_arn": event_bus_arn,
            "entries": entries,
        }
        if schema_registry_configuration is not None:
            input_["schema_registry_configuration"] = schema_registry_configuration
        if deduplication_configuration is not None:
            input_["deduplication_configuration"] = deduplication_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        policy_document: "capo_eventbridgev2.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        policy_name: Optional["capo_eventbridgev2.types.policy_name.PolicyName"] = None,
        expected_revision_id: Optional[
            "capo_eventbridgev2.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_eventbridgev2.types.put_resource_policy_response.PutResourcePolicyResponse":
        """Attaches a named resource policy to an event bus — the only resource type that supports policies; other resource ARNs are rejected. Each bus holds two named policies: "default" (customer-managed, full IAM policy language including Deny) and "AWS_RAM" (written exclusively by AWS Resource Access Manager to reflect resource shares). Both policies are evaluated on cross-account authorization; an explicit Deny in either overrides an Allow in the other. Operations that omit PolicyName target "default". A "default" policy that would grant public access is rejected with PublicPolicyException and is not attached; this check is always on and cannot be disabled.

        Args:
            policy_name: Which named policy to write. Defaults to "default", the customer-managed policy, when omitted (a write AWS Resource Access Manager makes on the owner's behalf resolves to "AWS_RAM" instead). The two writers are exclusive in both directions — only Resource Access Manager can write "AWS_RAM", and only the bus owner can write "default" — so naming the other party's policy fails with AccessDeniedException. A well-formed name that is neither of the two fails with InvalidInputException.
            expected_revision_id: The write succeeds only if the named policy's current revision ID matches this value; a policy that does not exist yet matches only the sentinel "NO_POLICY" (create-only). On mismatch the operation fails with ConflictException. When omitted, the write is unconditional. Every attempt stores a newly generated revision ID, so retrying an unanswered request can conflict with the caller's own earlier attempt; read the policy back and compare it with the one you intended before treating a conflict as another writer's change.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.conflict_exception.ConflictException: A client-supplied precondition (e.g. ExpectedRevisionId on a resource-policy write) did not match the current state of the resource. Retrying the same request will fail again; re-read the resource and re-evaluate before retrying. A conditional request is not retry-safe on its own. If an earlier attempt committed but its response never reached the caller, retrying fails with this error, which is indistinguishable from another writer having won. Compare the resource's current contents with what the request intended: a successful attempt stores a revision ID the caller never saw, so the revision alone cannot tell the two apart, but matching contents mean the change took effect.
            capo_eventbridgev2.errors.policy_length_exceeded_exception.PolicyLengthExceededException: The policy document is larger than the account's resource policy size quota, or larger than the service maximum.
            capo_eventbridgev2.errors.public_policy_exception.PublicPolicyException: The policy was rejected because it would grant public access to the event bus. A statement grants public access when its principal is a wildcard and no condition limits the callers to specific AWS accounts or principals. To fix it, replace the wildcard principal with specific principals, or add a condition that limits the callers to specific AWS accounts. Conditions on event content (events:source, events:detail-type, events:Metadata/*) do not identify the caller and do not make a wildcard principal non-public. Returned only for the "default" policy; the "AWS_RAM" policy is composed by AWS Resource Access Manager and never grants public access.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy_document": policy_document,
        }
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def revoke_resource(
        self,
        arn: "capo_eventbridgev2.types.revocable_resource_arn.RevocableResourceArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.revoke_resource_response.RevokeResourceResponse":
        """Revokes a subscriber or an EventSource. The bus owner calls this to withdraw a misbehaving resource attached to their bus. Revocation is terminal: there is no operation that clears it. A revoked resource refuses mutating operations with InvalidStateException; delete stays available for cleanup.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.revoke_resource_request.RevokeResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.revoke_resource_response.RevokeResourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.revoke_resource

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.revoke_resource.async_revoke_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.revoke_resource_request.RevokeResourceRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_eventbridgev2.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_eventbridgev2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.tag_resource_response.TagResourceResponse":
        """Adds or replaces tags on an event bus, subscriber, or event source.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.limit_exceeded_exception.LimitExceededException: The request would exceed a service quota for the account.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.tag_resource

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.tag_resource_request.TagResourceRequest = {
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

    async def untag_resource(
        self,
        resource_arn: "capo_eventbridgev2.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_eventbridgev2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
    ) -> "capo_eventbridgev2.types.untag_resource_response.UntagResourceResponse":
        """Removes tags from an event bus, subscriber, or event source.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.untag_resource

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_event_bus(
        self,
        event_bus_arn: "capo_eventbridgev2.types.event_bus_arn.EventBusArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        description: Optional[
            "capo_eventbridgev2.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_eventbridgev2.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        storage_configuration: Optional[
            "capo_eventbridgev2.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_eventbridgev2.types.update_event_bus_response.UpdateEventBusResponse":
        """Updates an event bus. The update is asynchronous: the bus moves to UPDATING and returns to ACTIVE when the change is applied. Fields omitted from the request are left unchanged.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.update_event_bus_request.UpdateEventBusRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.update_event_bus_response.UpdateEventBusResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.update_event_bus

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.update_event_bus.async_update_event_bus(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.update_event_bus_request.UpdateEventBusRequest = {
            "event_bus_arn": event_bus_arn
        }
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_event_source(
        self,
        event_source_arn: "capo_eventbridgev2.types.event_source_arn.EventSourceArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        configuration: Optional[
            "capo_eventbridgev2.types.event_source_configuration.EventSourceConfiguration"
        ] = None,
        description: Optional[
            "capo_eventbridgev2.types.description.Description"
        ] = None,
    ) -> "capo_eventbridgev2.types.update_event_source_response.UpdateEventSourceResponse":
        """Updates an EventSource. Fields omitted from the request are left unchanged.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.update_event_source_request.UpdateEventSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.update_event_source_response.UpdateEventSourceResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.update_event_source

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.update_event_source.async_update_event_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.update_event_source_request.UpdateEventSourceRequest = {
            "event_source_arn": event_source_arn
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscriber(
        self,
        subscriber_arn: "capo_eventbridgev2.types.subscriber_arn.SubscriberArn",
        *,
        config_overrides: Optional[AsyncEventBridgeV2ClientConfig] = None,
        description: Optional[
            "capo_eventbridgev2.types.description.Description"
        ] = None,
        state: Optional[
            "capo_eventbridgev2.types.subscriber_state.SubscriberState"
        ] = None,
        resume_position: Optional[
            "capo_eventbridgev2.types.resume_position.ResumePosition"
        ] = None,
        invoke_configuration: Optional[
            "capo_eventbridgev2.types.update_invoke_configuration.UpdateInvokeConfiguration"
        ] = None,
        filter_configuration: Optional[
            "capo_eventbridgev2.types.filter_configuration.FilterConfiguration"
        ] = None,
        batch_configuration: Optional[
            "capo_eventbridgev2.types.batch_configuration.BatchConfiguration"
        ] = None,
        transformer: Optional[
            "capo_eventbridgev2.types.transformer.Transformer"
        ] = None,
        retry_policy: Optional[
            "capo_eventbridgev2.types.retry_policy.RetryPolicy"
        ] = None,
        on_failure_configuration: Optional[
            "capo_eventbridgev2.types.on_failure_configuration.OnFailureConfiguration"
        ] = None,
        log_configuration: Optional[
            "capo_eventbridgev2.types.log_configuration.LogConfiguration"
        ] = None,
    ) -> "capo_eventbridgev2.types.update_subscriber_response.UpdateSubscriberResponse":
        """Updates a subscriber. Fields omitted from the request are left unchanged.

        Args:
            transformer: Not applicable to universal (aws-sdk) targets, whose input transformation is UniversalTargetParameters.Input; a Transformer on such a target is rejected.

        Raises:
            capo_eventbridgev2.errors.access_denied_exception.AccessDeniedException: The caller does not have the permissions required to perform the operation. This error is also returned when the operation cannot use the AWS KMS key for the event bus.
            capo_eventbridgev2.errors.internal_exception.InternalException: The request failed because of an internal service error. Retry the request.
            capo_eventbridgev2.errors.invalid_input_exception.InvalidInputException: A request parameter is missing or not valid.
            capo_eventbridgev2.errors.throttling_exception.ThrottlingException: The request was throttled because it exceeds a request rate limit. Retry the request with backoff.
            capo_eventbridgev2.errors.concurrent_modification_exception.ConcurrentModificationException: Another change to the resource is already in progress. Retry the request.
            capo_eventbridgev2.errors.invalid_state_exception.InvalidStateException: The resource is not in a state that allows the operation. For example, an event bus that is still being created cannot accept events.
            capo_eventbridgev2.errors.limit_exceeded_exception.LimitExceededException: The request would exceed a service quota for the account.
            capo_eventbridgev2.errors.resource_not_found_exception.ResourceNotFoundException: The resource does not exist.
            capo_eventbridgev2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_eventbridgev2.types.update_subscriber_request.UpdateSubscriberRequest]",
        ) -> AsyncOperationResponse[
            "capo_eventbridgev2.types.update_subscriber_response.UpdateSubscriberResponse"
        ]:
            import capo_eventbridgev2._operations.aws_events_v2.update_subscriber

            (
                output,
                http_response,
            ) = await capo_eventbridgev2._operations.aws_events_v2.update_subscriber.async_update_subscriber(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_eventbridgev2.types.update_subscriber_request.UpdateSubscriberRequest = {
            "subscriber_arn": subscriber_arn
        }
        if description is not None:
            input_["description"] = description
        if state is not None:
            input_["state"] = state
        if resume_position is not None:
            input_["resume_position"] = resume_position
        if invoke_configuration is not None:
            input_["invoke_configuration"] = invoke_configuration
        if filter_configuration is not None:
            input_["filter_configuration"] = filter_configuration
        if batch_configuration is not None:
            input_["batch_configuration"] = batch_configuration
        if transformer is not None:
            input_["transformer"] = transformer
        if retry_policy is not None:
            input_["retry_policy"] = retry_policy
        if on_failure_configuration is not None:
            input_["on_failure_configuration"] = on_failure_configuration
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration

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
