"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#OpenSearchMemory``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_opensearchmemory._auth._signers
import capo_opensearchmemory._auth._sigv4
from capo_opensearchmemory._auth._identity import Credentials
from capo_opensearchmemory._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_opensearchmemory._auth._zapros_handler import AuthMiddleware
from capo_opensearchmemory._pagination import resolve_path as _resolve_path
from capo_opensearchmemory._resources.open_search_memory.space import Space
from capo_opensearchmemory._services._aws_config import aws_config
from capo_opensearchmemory._services._pipeline import (
    Interceptor,
    OperationLogging,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    ThreadSafeRateLimiter,
    ThreadSafeRetryQuota,
    execute_pipeline,
    log_operation,
    rate_limit,
    retry,
)

if TYPE_CHECKING:
    import capo_opensearchmemory.types.actor_id
    import capo_opensearchmemory.types.actor_id_list
    import capo_opensearchmemory.types.batch_get_event_id_list
    import capo_opensearchmemory.types.batch_get_event_input
    import capo_opensearchmemory.types.batch_get_event_output
    import capo_opensearchmemory.types.client_token
    import capo_opensearchmemory.types.create_event_input
    import capo_opensearchmemory.types.create_event_output
    import capo_opensearchmemory.types.create_memory_content
    import capo_opensearchmemory.types.create_memory_input
    import capo_opensearchmemory.types.create_memory_output
    import capo_opensearchmemory.types.create_space_request
    import capo_opensearchmemory.types.create_space_response
    import capo_opensearchmemory.types.delete_event_input
    import capo_opensearchmemory.types.delete_event_output
    import capo_opensearchmemory.types.delete_memory_input
    import capo_opensearchmemory.types.delete_memory_output
    import capo_opensearchmemory.types.delete_space_request
    import capo_opensearchmemory.types.delete_space_response
    import capo_opensearchmemory.types.encryption_configuration
    import capo_opensearchmemory.types.event_expiry_days
    import capo_opensearchmemory.types.event_id
    import capo_opensearchmemory.types.event_payload
    import capo_opensearchmemory.types.event_search_summary
    import capo_opensearchmemory.types.event_summary
    import capo_opensearchmemory.types.event_timestamp
    import capo_opensearchmemory.types.extraction_model_id
    import capo_opensearchmemory.types.get_event_input
    import capo_opensearchmemory.types.get_event_output
    import capo_opensearchmemory.types.get_memory_input
    import capo_opensearchmemory.types.get_memory_output
    import capo_opensearchmemory.types.get_space_request
    import capo_opensearchmemory.types.get_space_response
    import capo_opensearchmemory.types.list_events_input
    import capo_opensearchmemory.types.list_events_output
    import capo_opensearchmemory.types.list_memories_input
    import capo_opensearchmemory.types.list_memories_output
    import capo_opensearchmemory.types.list_spaces_request
    import capo_opensearchmemory.types.list_spaces_response
    import capo_opensearchmemory.types.list_tags_for_resource_request
    import capo_opensearchmemory.types.list_tags_for_resource_response
    import capo_opensearchmemory.types.max_results
    import capo_opensearchmemory.types.memory_expiry_days
    import capo_opensearchmemory.types.memory_id
    import capo_opensearchmemory.types.memory_list_summary
    import capo_opensearchmemory.types.memory_search_summary
    import capo_opensearchmemory.types.memory_sort_field
    import capo_opensearchmemory.types.memory_strategy_list
    import capo_opensearchmemory.types.memory_update_content
    import capo_opensearchmemory.types.metadata_map
    import capo_opensearchmemory.types.metadata_mode
    import capo_opensearchmemory.types.next_token
    import capo_opensearchmemory.types.pagination_token
    import capo_opensearchmemory.types.search_events_input
    import capo_opensearchmemory.types.search_events_output
    import capo_opensearchmemory.types.search_memories_input
    import capo_opensearchmemory.types.search_memories_output
    import capo_opensearchmemory.types.search_query
    import capo_opensearchmemory.types.search_sort
    import capo_opensearchmemory.types.session_id
    import capo_opensearchmemory.types.session_id_list
    import capo_opensearchmemory.types.sort_order
    import capo_opensearchmemory.types.space_arn
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.space_name
    import capo_opensearchmemory.types.space_summary
    import capo_opensearchmemory.types.strategy_name
    import capo_opensearchmemory.types.strategy_selector_list
    import capo_opensearchmemory.types.tag_key_list
    import capo_opensearchmemory.types.tag_list
    import capo_opensearchmemory.types.tag_resource_request
    import capo_opensearchmemory.types.tag_resource_response
    import capo_opensearchmemory.types.untag_resource_request
    import capo_opensearchmemory.types.untag_resource_response
    import capo_opensearchmemory.types.update_memory_input
    import capo_opensearchmemory.types.update_memory_output
    import capo_opensearchmemory.types.update_space_request
    import capo_opensearchmemory.types.update_space_response


class OpenSearchMemoryClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    region: str | None
    endpoint: str | None
    use_fips: bool | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class OpenSearchMemoryClient:
    """A client for the ``OpenSearchMemory`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
        region: The value of the ``AWS::Region`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        retry_mode: Literal["standard", "adaptive"] | None = None,
        region: str | None = None,
        endpoint: str | None = None,
        use_fips: bool | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = Client(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = ThreadSafeRetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = ThreadSafeRateLimiter()
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
                Client(raw_handler)
            )
        self._config = OpenSearchMemoryClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "region": region,
                "endpoint": endpoint,
                "use_fips": use_fips,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.space = Space(self)

    def operation_options(
        self,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: OpenSearchMemoryClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(log_operation(operation_logging))
        interceptors_.append(retry())
        interceptors_.append(rate_limit())
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
            region=overrides.get("region", self._config.get("region")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def list_tags_for_resource(
        self,
        resource_arn: "capo_opensearchmemory.types.space_arn.SpaceArn",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
    ) -> "capo_opensearchmemory.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified space.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the space.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.list_tags_for_resource

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListTagsForResource")
        )
        input_: capo_opensearchmemory.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_opensearchmemory.types.space_arn.SpaceArn",
        tags: "capo_opensearchmemory.types.tag_list.TagList",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
    ) -> "capo_opensearchmemory.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified space.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the space.</p>
            tags: <p>The tags to add to the space.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.tag_resource

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("TagResource")
        )
        input_: capo_opensearchmemory.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_opensearchmemory.types.space_arn.SpaceArn",
        tag_keys: "capo_opensearchmemory.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
    ) -> "capo_opensearchmemory.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified space.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the space.</p>
            tag_keys: <p>The keys of the tags to remove from the space.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.untag_resource

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UntagResource")
        )
        input_: capo_opensearchmemory.types.untag_resource_request.UntagResourceRequest = {
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

    def create_space(
        self,
        name: "capo_opensearchmemory.types.space_name.SpaceName",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        memory_strategies: Optional[
            "capo_opensearchmemory.types.memory_strategy_list.MemoryStrategyList"
        ] = None,
        event_expiry_days: Optional[
            "capo_opensearchmemory.types.event_expiry_days.EventExpiryDays"
        ] = None,
        memory_expiry_days: Optional[
            "capo_opensearchmemory.types.memory_expiry_days.MemoryExpiryDays"
        ] = None,
        extraction_model_id: Optional[
            "capo_opensearchmemory.types.extraction_model_id.ExtractionModelId"
        ] = None,
        encryption_configuration: Optional[
            "capo_opensearchmemory.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_opensearchmemory.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_opensearchmemory.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchmemory.types.create_space_response.CreateSpaceResponse":
        """<p>Creates a space. A space is an AWS resource that stores the events you send and the memories extracted from them, and defines the memory strategies that extract those memories.</p> <p>The operation returns before provisioning finishes, with <code>status</code> <code>CREATING</code>. Call <code>GetSpace</code> until the status is <code>ACTIVE</code>, and then use the space. If provisioning fails, the status becomes <code>FAILED</code> and <code>statusReason</code> says why.</p>

        Args:
            name: <p>A name for the space, unique within your account in the Region. If another space already has the name, the request fails with <code>ConflictException</code>.</p>
            memory_strategies: <p>The memory strategies that extract memories from the space's events: up to 10 strategies, each with a name that is unique within the space.</p> <p>Optional. Omit it, or send an empty list, to create a space with no memory strategies. Such a space stores the conversation events you send it and returns them through <code>SearchEvents</code> and <code>ListEvents</code>, but extracts no memories and has none to search. You can add strategies later with <code>UpdateSpace</code>.</p> <p>The serialized list can be at most 384 KiB.</p>
            event_expiry_days: <p>How many days the space keeps each event, from 1 to 365. The default is 90.</p>
            memory_expiry_days: <p>How many days the space keeps each memory, from 0 to 3650, counted from when the service writes the memory. Updating a memory with <code>UpdateMemory</code> doesn't restart the count. 0 means memories never expire. If you omit it, memories never expire.</p> <p>Searches and lists leave out a memory past its expiry, and reading, updating, or deleting it returns <code>ResourceNotFoundException</code>.</p>
            extraction_model_id: <p>The model that extracts and consolidates memories for every strategy in the space, as an Amazon Bedrock model ID without an inference-profile prefix: <code>anthropic.claude-opus-5-5</code> or <code>anthropic.claude-haiku-5-5</code>. Another value fails with <code>ValidationException</code>, and the message lists the supported IDs. Omit it to use the service default, which can change over time and isn't returned by <code>GetSpace</code>. Setting a value pins the model.</p>
            encryption_configuration: <p>The AWS KMS key that encrypts the space's data. Omit it, or omit its <code>kmsKeyArn</code>, to use an AWS owned key. You can't change the key after you create the space.</p>
            tags: <p>The tags to add to the space.</p>
            client_token: <p>A unique, case-sensitive identifier that makes the request idempotent. A retry with the same token and the same parameters within 2 hours returns the space that the first request created, instead of creating another. Reusing the token with different parameters, or while the first request is still in progress, fails with <code>ConflictException</code>.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a quota, such as the number of spaces in your account or the number of strategies in a space.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.create_space_request.CreateSpaceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.create_space_response.CreateSpaceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.create_space

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.create_space.create_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.create_space_request.CreateSpaceRequest",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.create_space_request

            return capo_opensearchmemory.types.create_space_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateSpace", redact_input=_redact_input),
        )
        input_: capo_opensearchmemory.types.create_space_request.CreateSpaceRequest = {
            "name": name
        }
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if event_expiry_days is not None:
            input_["event_expiry_days"] = event_expiry_days
        if memory_expiry_days is not None:
            input_["memory_expiry_days"] = memory_expiry_days
        if extraction_model_id is not None:
            input_["extraction_model_id"] = extraction_model_id
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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

    def get_space(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
    ) -> "capo_opensearchmemory.types.get_space_response.GetSpaceResponse":
        """<p>Returns a space's configuration and status.</p>

        Args:
            space_id: <p>The ID of the space.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.get_space_request.GetSpaceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.get_space_response.GetSpaceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.get_space

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.get_space.get_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_opensearchmemory.types.get_space_response.GetSpaceResponse",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.get_space_response

            return capo_opensearchmemory.types.get_space_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetSpace", redact_output=_redact_output)
        )
        input_: capo_opensearchmemory.types.get_space_request.GetSpaceRequest = {
            "space_id": space_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_space(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        memory_strategies: Optional[
            "capo_opensearchmemory.types.memory_strategy_list.MemoryStrategyList"
        ] = None,
        event_expiry_days: Optional[
            "capo_opensearchmemory.types.event_expiry_days.EventExpiryDays"
        ] = None,
        memory_expiry_days: Optional[
            "capo_opensearchmemory.types.memory_expiry_days.MemoryExpiryDays"
        ] = None,
        extraction_model_id: Optional[
            "capo_opensearchmemory.types.extraction_model_id.ExtractionModelId"
        ] = None,
    ) -> "capo_opensearchmemory.types.update_space_response.UpdateSpaceResponse":
        """<p>Updates a space's memory strategies, retention settings, or extraction model. Supply only the fields to change. Omitted fields keep their current values.</p> <p>If the request changes the set of strategies, a strategy's configuration, a retention setting, or the extraction model, the space moves to <code>UPDATING</code>. When the change is complete, the space returns to <code>ACTIVE</code>, or moves to <code>FAILED</code> if the change can't be applied. While the space is <code>UPDATING</code>, <code>GetSpace</code> returns the previous configuration. A request that only changes strategy descriptions or repeats the values the space has stored is applied immediately and doesn't change the status. Sending a retention value that the space never set also moves the space to <code>UPDATING</code>, even one that matches the behavior without it, such as 90 for <code>eventExpiryDays</code> or 0 for <code>memoryExpiryDays</code>. A space that is <code>CREATING</code>, <code>UPDATING</code>, or <code>DELETING</code> can't be updated: the request fails with <code>ConflictException</code>.</p>

        Args:
            space_id: <p>The ID of the space to update.</p>
            memory_strategies: <p>The complete new list of memory strategies. The service removes strategies that aren't in the list from the space. Removing a strategy stops extraction for it but doesn't delete its memories: they're kept, until they expire if the space sets <code>memoryExpiryDays</code>, and they're available again if you later add a strategy with the same <code>type</code> and <code>name</code>. To delete them, use <code>DeleteMemory</code> before you remove the strategy, or delete the space.</p> <p>To keep a strategy, include it with the same <code>type</code> and <code>name</code> that <code>GetSpace</code> returns. For a kept strategy, any <code>configuration</code> member you omit keeps its current value. It doesn't return to the default, and you can't clear a member once it's set. Omit this field to leave the strategies unchanged. The list must name at least one strategy. You can't remove every strategy from a space with <code>UpdateSpace</code>.</p> <p>The serialized list can be at most 384 KiB.</p>
            event_expiry_days: <p>How many days the space keeps each event, from 1 to 365. Omit it to leave the current value unchanged. Events already stored keep the expiry they were written with.</p>
            memory_expiry_days: <p>How many days the space keeps each memory, from 0 to 3650. 0 means memories never expire. Omit it to leave the current value unchanged. You can't clear the setting. To make memories written from then on never expire, send 0. <code>GetSpace</code> then returns 0.</p> <p>A change applies to memories written after it. Memories already stored keep the expiry they were written with. A memory the service rewrites later, such as a summary it keeps up to date, takes the setting in force at that rewrite. A change moves the space to <code>UPDATING</code>. Sending the value that the space has stored doesn't.</p>
            extraction_model_id: <p>The model that extracts and consolidates memories for every strategy in the space: <code>anthropic.claude-opus-5-5</code> or <code>anthropic.claude-haiku-5-5</code>. Omit it to leave the current value unchanged. Once set, it can't be cleared back to the service default.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a quota, such as the number of spaces in your account or the number of strategies in a space.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.update_space_request.UpdateSpaceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.update_space_response.UpdateSpaceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.update_space

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.update_space.update_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.update_space_request.UpdateSpaceRequest",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.update_space_request

            return capo_opensearchmemory.types.update_space_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("UpdateSpace", redact_input=_redact_input),
        )
        input_: capo_opensearchmemory.types.update_space_request.UpdateSpaceRequest = {
            "space_id": space_id
        }
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if event_expiry_days is not None:
            input_["event_expiry_days"] = event_expiry_days
        if memory_expiry_days is not None:
            input_["memory_expiry_days"] = memory_expiry_days
        if extraction_model_id is not None:
            input_["extraction_model_id"] = extraction_model_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_space(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
    ) -> "capo_opensearchmemory.types.delete_space_response.DeleteSpaceResponse":
        """<p>Deletes a space and its memories. Deletion can't be undone. After you delete the space, you can't retrieve its events, and the service removes them when they reach their expiry.</p> <p>The operation returns with <code>status</code> <code>DELETING</code>. When deletion finishes, <code>GetSpace</code> returns <code>ResourceNotFoundException</code>. If deletion fails, the status becomes <code>FAILED</code>. A space that is <code>CREATING</code> or <code>UPDATING</code> can't be deleted until that finishes: the request fails with <code>ConflictException</code>. Deleting a space that is already <code>DELETING</code> returns <code>DELETING</code> again.</p>

        Args:
            space_id: <p>The ID of the space to delete.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.delete_space_request.DeleteSpaceRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.delete_space_response.DeleteSpaceResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.delete_space

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.delete_space.delete_space(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteSpace")
        )
        input_: capo_opensearchmemory.types.delete_space_request.DeleteSpaceRequest = {
            "space_id": space_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_spaces(
        self,
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_opensearchmemory.types.next_token.NextToken"] = None,
    ) -> "capo_opensearchmemory.types.list_spaces_response.ListSpacesResponse":
        """<p>Lists the spaces in your account in the current Region.</p>

        Args:
            max_results: <p>The maximum number of spaces to return, from 1 to 100. The default is 100.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.list_spaces_request.ListSpacesRequest]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.list_spaces_response.ListSpacesResponse"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.list_spaces

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.list_spaces.list_spaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListSpaces")
        )
        input_: capo_opensearchmemory.types.list_spaces_request.ListSpacesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_spaces(
        self,
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_opensearchmemory.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_opensearchmemory.types.space_summary.SpaceSummary]":
        _token = next_token
        while True:
            _response = self.list_spaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("spaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def batch_get_event(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        event_ids: "capo_opensearchmemory.types.batch_get_event_id_list.BatchGetEventIdList",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        actor_id: Optional["capo_opensearchmemory.types.actor_id.ActorId"] = None,
        session_id: Optional["capo_opensearchmemory.types.session_id.SessionId"] = None,
    ) -> "capo_opensearchmemory.types.batch_get_event_output.BatchGetEventOutput":
        """<p>Gets up to 10 events by ID, each as <code>GetEvent</code> returns it, including its payload.</p> <p>If you supply <code>actorId</code> or <code>sessionId</code>, every requested event must match it. Each event has its own outcome. The operation reports an event that it can't return in <code>errors</code> instead of failing, with an error code named for the exception that <code>GetEvent</code> would return for it. The operation reports both an event that doesn't exist and an event outside the supplied scope as <code>RESOURCE_NOT_FOUND</code>.</p> <p>The exception is the space's customer managed AWS KMS key: if it is disabled, pending deletion, can't be used for decryption, or was deleted, the whole call fails with <code>ValidationException</code>, as <code>GetEvent</code> does.</p>

        Args:
            space_id: <p>The ID of the space.</p>
            actor_id: <p>The actor that every requested event must belong to. Omit it to skip this check. The operation reports an event that doesn't match in <code>errors</code> as <code>RESOURCE_NOT_FOUND</code>.</p>
            session_id: <p>The session that every requested event must belong to. Omit it to skip this check. The operation reports an event that doesn't match in <code>errors</code> as <code>RESOURCE_NOT_FOUND</code>.</p>
            event_ids: <p>The IDs of the events to get: 1 to 10, without duplicates.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.batch_get_event_input.BatchGetEventInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.batch_get_event_output.BatchGetEventOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.batch_get_event

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.batch_get_event.batch_get_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_opensearchmemory.types.batch_get_event_output.BatchGetEventOutput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.batch_get_event_output

            return capo_opensearchmemory.types.batch_get_event_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("BatchGetEvent", redact_output=_redact_output),
        )
        input_: capo_opensearchmemory.types.batch_get_event_input.BatchGetEventInput = {
            "space_id": space_id,
            "event_ids": event_ids,
        }
        if actor_id is not None:
            input_["actor_id"] = actor_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        payload: "capo_opensearchmemory.types.event_payload.EventPayload",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        session_id: Optional["capo_opensearchmemory.types.session_id.SessionId"] = None,
        event_timestamp: Optional[
            "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
        ] = None,
        metadata: Optional[
            "capo_opensearchmemory.types.metadata_map.MetadataMap"
        ] = None,
        client_token: Optional[
            "capo_opensearchmemory.types.client_token.ClientToken"
        ] = None,
        infer: Optional[bool] = None,
    ) -> "capo_opensearchmemory.types.create_event_output.CreateEventOutput":
        """<p>Submits an event (conversation turns, structured data, or a PDF document stored in Amazon S3) to a session in a space.</p> <p>The operation returns as soon as the event is saved. <code>GetEvent</code> and <code>ListEvents</code> return it immediately. <code>SearchEvents</code> returns it after it's indexed. <code>SearchMemories</code> returns memories extracted from it only after a strategy's extraction trigger fires and the memories are indexed.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space that owns the event, for example <code>sp-02864597b164</code>.</p>
            actor_id: <p>The ID of the actor (end user or agent) that the event belongs to.</p>
            session_id: <p>The session the event belongs to. Send every event of one conversation with the same session ID, so that <code>SUMMARY</code> strategies summarize the conversation as one session. If you omit it, the service generates a session ID and returns it.</p>
            event_timestamp: <p>When the event occurred. The default is the time that the service receives the request.</p>
            payload: <p>The event content. Set exactly one union member.</p>
            metadata: <p>Metadata tags to store with the event. Memories derived from the event carry the same tags. Keys that begin with <code>x-amz-</code>, the keys <code>documentS3Source</code> and <code>documentS3Url</code>, and other keys that the service uses internally are reserved: a request that sets one fails with <code>ValidationException</code>, and the message names the key.</p> <p>A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with <code>ValidationException</code>. Reuse an existing key instead.</p>
            client_token: <p>A unique, case-sensitive identifier that makes the request idempotent. Within 2 hours of the first request, a retry with the same token and the same request, including the same <code>sessionId</code>, returns the same event. If you omit <code>sessionId</code>, the service generates a new one on each attempt, so a retry fails with <code>ConflictException</code>. Reusing the token with different request content also fails with <code>ConflictException</code>. <code>eventTimestamp</code> isn't compared. After 2 hours, the token starts a new event.</p>
            infer: <p>Specifies whether to extract memories from this event. The default is <code>true</code>. Set it to <code>false</code> to store the event without extraction: the service skips strategies that infer memories, and still indexes the event's turns for <code>SearchEvents</code>. A document submitted as a <code>blob</code> is still extracted.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.create_event_input.CreateEventInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.create_event_output.CreateEventOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.create_event

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.create_event.create_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.create_event_input.CreateEventInput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.create_event_input

            return capo_opensearchmemory.types.create_event_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateEvent", redact_input=_redact_input),
        )
        input_: capo_opensearchmemory.types.create_event_input.CreateEventInput = {
            "space_id": space_id,
            "actor_id": actor_id,
            "payload": payload,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if event_timestamp is not None:
            input_["event_timestamp"] = event_timestamp
        if metadata is not None:
            input_["metadata"] = metadata
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if infer is not None:
            input_["infer"] = infer

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_memory(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        name: "capo_opensearchmemory.types.strategy_name.StrategyName",
        content: "capo_opensearchmemory.types.create_memory_content.CreateMemoryContent",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        session_id: Optional["capo_opensearchmemory.types.session_id.SessionId"] = None,
        metadata: Optional[
            "capo_opensearchmemory.types.metadata_map.MetadataMap"
        ] = None,
        client_token: Optional[
            "capo_opensearchmemory.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_opensearchmemory.types.create_memory_output.CreateMemoryOutput":
        """<p>Writes a memory that you have already formed, without extracting it from events. The service embeds the text as given and stores it as a memory of the named strategy. To have the service extract memories from conversation turns, use <code>CreateEvent</code> instead.</p> <p>The operation returns before the memory is searchable. The returned <code>memoryId</code> is final, but until the memory is indexed, <code>GetMemory</code>, <code>UpdateMemory</code>, and <code>DeleteMemory</code> return <code>ResourceNotFoundException</code> for it.</p> <p>If the request would exceed the service's rate for embedding requests, it fails with <code>ThrottlingException</code>. Retry with exponential backoff.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space that owns the memory, for example <code>sp-02864597b164</code>.</p>
            name: <p>The name of the strategy that the memory belongs to. The space must already declare the strategy, and the memory's type comes from that strategy. The name must be 1 to 64 characters: letters, digits, periods, hyphens, and underscores, starting with a letter or digit.</p>
            content: <p>The memory text, stored and embedded as provided.</p>
            actor_id: <p>The actor (end user or agent) that owns the memory.</p>
            session_id: <p>The session that the memory belongs to. If you omit it, the service generates a session ID and returns it.</p>
            metadata: <p>Metadata tags to store with the memory. Keys that begin with <code>x-amz-</code>, the key <code>documentS3Source</code>, and other keys that the service uses internally are reserved: a request that sets one fails with <code>ValidationException</code>, and the message names the key.</p> <p>A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with <code>ValidationException</code>. Reuse an existing key instead.</p>
            client_token: <p>A unique, case-sensitive identifier that makes the request idempotent. Within 2 hours of the first request, a retry with the same token returns the same <code>memoryId</code> instead of creating a second memory. Reusing the token with a different <code>name</code>, <code>content</code>, <code>metadata</code>, <code>actorId</code>, or <code>sessionId</code> fails with <code>ConflictException</code>. If you omit <code>sessionId</code>, a retry with the same token gets the same session. If you omit the token, each call creates a new memory.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.create_memory_input.CreateMemoryInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.create_memory_output.CreateMemoryOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.create_memory

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.create_memory.create_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.create_memory_input.CreateMemoryInput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.create_memory_input

            return capo_opensearchmemory.types.create_memory_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("CreateMemory", redact_input=_redact_input),
        )
        input_: capo_opensearchmemory.types.create_memory_input.CreateMemoryInput = {
            "space_id": space_id,
            "name": name,
            "content": content,
            "actor_id": actor_id,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if metadata is not None:
            input_["metadata"] = metadata
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

    def delete_event(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        event_id: "capo_opensearchmemory.types.event_id.EventId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        actor_id: Optional["capo_opensearchmemory.types.actor_id.ActorId"] = None,
        session_id: Optional["capo_opensearchmemory.types.session_id.SessionId"] = None,
    ) -> "capo_opensearchmemory.types.delete_event_output.DeleteEventOutput":
        """<p>Deletes an event. Deletion can't be undone. The event stops appearing in <code>SearchEvents</code> results shortly after you delete it. Deleting an event that doesn't exist returns <code>ResourceNotFoundException</code>.</p> <p>Deleting an event doesn't delete the memories derived from it, because a memory can combine content from several events. To remove them, use <code>DeleteMemory</code>.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space.</p>
            event_id: <p>The ID of the event to delete.</p>
            actor_id: <p>The actor that the event must belong to. Omit it to skip this check. If it doesn't match the stored event, the call fails with <code>ResourceNotFoundException</code>, as if the event did not exist.</p>
            session_id: <p>The session that the event must belong to. Omit it to skip this check. If it doesn't match the stored event, the call fails with <code>ResourceNotFoundException</code>, as if the event did not exist.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.delete_event_input.DeleteEventInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.delete_event_output.DeleteEventOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.delete_event

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.delete_event.delete_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteEvent")
        )
        input_: capo_opensearchmemory.types.delete_event_input.DeleteEventInput = {
            "space_id": space_id,
            "event_id": event_id,
        }
        if actor_id is not None:
            input_["actor_id"] = actor_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_memory(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        memory_id: "capo_opensearchmemory.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        actor_id: Optional["capo_opensearchmemory.types.actor_id.ActorId"] = None,
        strategy_name: Optional[
            "capo_opensearchmemory.types.strategy_name.StrategyName"
        ] = None,
    ) -> "capo_opensearchmemory.types.delete_memory_output.DeleteMemoryOutput":
        """<p>Deletes a memory, including its content and embedding. Deletion can't be undone. Searches stop returning the memory shortly after you delete it.</p> <p>Deleting a memory that no longer exists returns <code>ResourceNotFoundException</code>, so the operation is not idempotent. If you retry deletes, treat that error as success.</p> <p>A memory past its expiry (set from the space's <code>memoryExpiryDays</code> when the memory is written) reads as not found: the operation returns <code>ResourceNotFoundException</code>, as for a memory that was already deleted.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space that owns the memory.</p>
            memory_id: <p>The ID of the memory to delete.</p>
            actor_id: <p>The ID of the actor that the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>
            strategy_name: <p>The name of the strategy that the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.delete_memory_input.DeleteMemoryInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.delete_memory_output.DeleteMemoryOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.delete_memory

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.delete_memory.delete_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteMemory")
        )
        input_: capo_opensearchmemory.types.delete_memory_input.DeleteMemoryInput = {
            "space_id": space_id,
            "memory_id": memory_id,
        }
        if actor_id is not None:
            input_["actor_id"] = actor_id
        if strategy_name is not None:
            input_["strategy_name"] = strategy_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        event_id: "capo_opensearchmemory.types.event_id.EventId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        actor_id: Optional["capo_opensearchmemory.types.actor_id.ActorId"] = None,
        session_id: Optional["capo_opensearchmemory.types.session_id.SessionId"] = None,
    ) -> "capo_opensearchmemory.types.get_event_output.GetEventOutput":
        """<p>Gets an event by ID, including its payload.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space.</p>
            event_id: <p>The event's ID, as returned by <code>CreateEvent</code>, <code>ListEvents</code>, or <code>SearchEvents</code>.</p>
            actor_id: <p>The actor the event must belong to. Omit it to skip this check. If it doesn't match the stored event, the call fails with <code>ResourceNotFoundException</code>, as if the event did not exist.</p>
            session_id: <p>The session the event must belong to. Omit it to skip this check. If it doesn't match the stored event, the call fails with <code>ResourceNotFoundException</code>, as if the event did not exist.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.get_event_input.GetEventInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.get_event_output.GetEventOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.get_event

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.get_event.get_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_opensearchmemory.types.get_event_output.GetEventOutput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.get_event_output

            return capo_opensearchmemory.types.get_event_output.redact_sensitive(output)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetEvent", redact_output=_redact_output)
        )
        input_: capo_opensearchmemory.types.get_event_input.GetEventInput = {
            "space_id": space_id,
            "event_id": event_id,
        }
        if actor_id is not None:
            input_["actor_id"] = actor_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_memory(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        memory_id: "capo_opensearchmemory.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        actor_id: Optional["capo_opensearchmemory.types.actor_id.ActorId"] = None,
        strategy_name: Optional[
            "capo_opensearchmemory.types.strategy_name.StrategyName"
        ] = None,
    ) -> "capo_opensearchmemory.types.get_memory_output.GetMemoryOutput":
        """<p>Gets a memory by ID, as returned by <code>SearchMemories</code> or <code>ListMemories</code>. A memory that doesn't exist returns <code>ResourceNotFoundException</code>. Unlike <code>SearchMemories</code>, this operation also returns memories that consolidation has superseded.</p> <p>A memory past its expiry (set from the space's <code>memoryExpiryDays</code> when the memory is written) reads as not found: <code>ResourceNotFoundException</code>, the same answer as for an ID that does not exist.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space that holds the memory.</p>
            memory_id: <p>The memory's ID, as returned by <code>SearchMemories</code> or <code>ListMemories</code>.</p>
            actor_id: <p>The ID of the actor the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>
            strategy_name: <p>The name of the strategy the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.get_memory_input.GetMemoryInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.get_memory_output.GetMemoryOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.get_memory

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.get_memory.get_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_opensearchmemory.types.get_memory_output.GetMemoryOutput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.get_memory_output

            return capo_opensearchmemory.types.get_memory_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging("GetMemory", redact_output=_redact_output),
        )
        input_: capo_opensearchmemory.types.get_memory_input.GetMemoryInput = {
            "space_id": space_id,
            "memory_id": memory_id,
        }
        if actor_id is not None:
            input_["actor_id"] = actor_id
        if strategy_name is not None:
            input_["strategy_name"] = strategy_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_events(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        session_id: "capo_opensearchmemory.types.session_id.SessionId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        event_timestamp_before: Optional[
            "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
        ] = None,
        event_timestamp_after: Optional[
            "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
        ] = None,
        sort_order: Optional["capo_opensearchmemory.types.sort_order.SortOrder"] = None,
        metadata_filters: Optional[
            "capo_opensearchmemory.types.metadata_map.MetadataMap"
        ] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_opensearchmemory.types.list_events_output.ListEventsOutput":
        """<p>Lists the events in a session, sorted by time. Optionally limit the results to events whose <code>eventTimestamp</code> falls between <code>eventTimestampAfter</code> and <code>eventTimestampBefore</code>. Returns event metadata only. Call <code>GetEvent</code> for the payload. For full-text or relevance search, use <code>SearchEvents</code>.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space.</p>
            actor_id: <p>The actor whose events to list.</p>
            session_id: <p>The session whose events to list. To find events across sessions, use <code>SearchEvents</code>.</p>
            event_timestamp_before: <p>Inclusive upper bound on <code>eventTimestamp</code>: only events at or before this time are returned. Omit for no upper bound.</p>
            event_timestamp_after: <p>Inclusive lower bound on <code>eventTimestamp</code>: only events at or after this time are returned. Omit for no lower bound.</p> <p>If it's later than <code>eventTimestampBefore</code>, the request fails with <code>ValidationException</code>.</p>
            sort_order: <p>The order of the results by <code>eventTimestamp</code>: <code>ASC</code> or <code>DESC</code>. The default is <code>DESC</code>, most recent first.</p>
            metadata_filters: <p>Returns only events whose metadata contains every one of these key-value pairs. Omit, or leave empty, for no metadata filter. The service applies the filter after it reads events, so a page can hold fewer than <code>maxResults</code> events, or none, and still return a <code>nextToken</code>. Keep paging until <code>nextToken</code> is absent.</p>
            max_results: <p>The maximum number of events to return, from 1 to 100. The default is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.list_events_input.ListEventsInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.list_events_output.ListEventsOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.list_events

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.list_events.list_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListEvents")
        )
        input_: capo_opensearchmemory.types.list_events_input.ListEventsInput = {
            "space_id": space_id,
            "actor_id": actor_id,
            "session_id": session_id,
        }
        if event_timestamp_before is not None:
            input_["event_timestamp_before"] = event_timestamp_before
        if event_timestamp_after is not None:
            input_["event_timestamp_after"] = event_timestamp_after
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if metadata_filters is not None:
            input_["metadata_filters"] = metadata_filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_events(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        session_id: "capo_opensearchmemory.types.session_id.SessionId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        event_timestamp_before: Optional[
            "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
        ] = None,
        event_timestamp_after: Optional[
            "capo_opensearchmemory.types.event_timestamp.EventTimestamp"
        ] = None,
        sort_order: Optional["capo_opensearchmemory.types.sort_order.SortOrder"] = None,
        metadata_filters: Optional[
            "capo_opensearchmemory.types.metadata_map.MetadataMap"
        ] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_opensearchmemory.types.event_summary.EventSummary]":
        _token = next_token
        while True:
            _response = self.list_events(
                space_id,
                actor_id,
                session_id,
                config_overrides=config_overrides,
                event_timestamp_before=event_timestamp_before,
                event_timestamp_after=event_timestamp_after,
                sort_order=sort_order,
                metadata_filters=metadata_filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_memories(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        memory_strategies: Optional[
            "capo_opensearchmemory.types.strategy_selector_list.StrategySelectorList"
        ] = None,
        actor_ids: Optional[
            "capo_opensearchmemory.types.actor_id_list.ActorIdList"
        ] = None,
        session_ids: Optional[
            "capo_opensearchmemory.types.session_id_list.SessionIdList"
        ] = None,
        sort_by: Optional[
            "capo_opensearchmemory.types.memory_sort_field.MemorySortField"
        ] = None,
        sort_order: Optional["capo_opensearchmemory.types.sort_order.SortOrder"] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_opensearchmemory.types.list_memories_output.ListMemoriesOutput":
        """<p>Lists a space's memories without a query, for example the most recent memories or the memories of one strategy. Filter by strategy and optionally by owning actor or session, sort by creation or update time, and page through the results. Results have no relevance score. To query or filter by metadata, use <code>SearchMemories</code>.</p> <p>If memories are written or deleted while you page, the results can skip a memory or return it twice. You can page through only a limited number of results. A request past that limit fails with <code>ValidationException</code> (reason <code>invalidNextToken</code>), and the message gives the limit.</p> <p>Memories past their expiry (set from the space's <code>memoryExpiryDays</code> when each memory is written) are left out. Unlike <code>SearchMemories</code>, this operation also returns memories that consolidation has superseded.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The space whose memories to list.</p>
            memory_strategies: <p>The strategies to list, as selectors. A selector without <code>memoryStrategyNames</code> lists every strategy of its type, and omitting <code>memoryStrategies</code> lists every strategy in the space. A name that is not a declared strategy of that type fails with <code>ValidationException</code>.</p>
            actor_ids: <p>Lists only memories owned by one of these actors. Combined with <code>sessionIds</code> by AND: a memory must match both filters when both are given. Omit for no actor filter. An empty list fails validation. A memory stored without an actor never matches an actor filter.</p>
            session_ids: <p>Lists only memories from one of these sessions. Combined with <code>actorIds</code> by AND. Omit for no session filter. An empty list fails validation. A memory stored without a session never matches a session filter.</p>
            sort_by: <p>The timestamp to sort by, as returned in <code>systemMetadata</code>: <code>CREATED_AT</code> (the default) or <code>UPDATED_AT</code>.</p>
            sort_order: <p>The sort order: <code>ASC</code> or <code>DESC</code>. The default is <code>DESC</code>, most recent first.</p>
            max_results: <p>The maximum number of memories to return, from 1 to 100. The default is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.list_memories_input.ListMemoriesInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.list_memories_output.ListMemoriesOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.list_memories

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.list_memories.list_memories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListMemories")
        )
        input_: capo_opensearchmemory.types.list_memories_input.ListMemoriesInput = {
            "space_id": space_id
        }
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if actor_ids is not None:
            input_["actor_ids"] = actor_ids
        if session_ids is not None:
            input_["session_ids"] = session_ids
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_memories(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        memory_strategies: Optional[
            "capo_opensearchmemory.types.strategy_selector_list.StrategySelectorList"
        ] = None,
        actor_ids: Optional[
            "capo_opensearchmemory.types.actor_id_list.ActorIdList"
        ] = None,
        session_ids: Optional[
            "capo_opensearchmemory.types.session_id_list.SessionIdList"
        ] = None,
        sort_by: Optional[
            "capo_opensearchmemory.types.memory_sort_field.MemorySortField"
        ] = None,
        sort_order: Optional["capo_opensearchmemory.types.sort_order.SortOrder"] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_opensearchmemory.types.memory_list_summary.MemoryListSummary]":
        _token = next_token
        while True:
            _response = self.list_memories(
                space_id,
                config_overrides=config_overrides,
                memory_strategies=memory_strategies,
                actor_ids=actor_ids,
                session_ids=session_ids,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("memories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_events(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        query: "capo_opensearchmemory.types.search_query.SearchQuery",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        session_ids: Optional[
            "capo_opensearchmemory.types.session_id_list.SessionIdList"
        ] = None,
        sort: Optional["capo_opensearchmemory.types.search_sort.SearchSort"] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_opensearchmemory.types.search_events_output.SearchEventsOutput":
        """<p>Searches a space's events by relevance. It works like <code>SearchMemories</code> without the memory type and strategy selector. The query is a subset of the OpenSearch Query DSL. The service validates it, limits the search to the actor in <code>actorId</code> and the sessions in <code>sessionIds</code>, and returns ranked results. Each result is the matching chunk of an event, not the whole event. You can page through only a limited number of results. A request past that limit fails with <code>ValidationException</code> (reason <code>invalidNextToken</code>), and the message gives the limit.</p> <p>If the results are larger than 5 MiB, the request fails with <code>ValidationException</code> (reason <code>queryBodyTooLarge</code>). Lower <code>maxResults</code>.</p> <p>If the request would exceed the service's rate for embedding requests, it fails with <code>ThrottlingException</code>. Retry with exponential backoff.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The space whose events to search. Use <code>actorId</code> and <code>sessionIds</code> to narrow the search within it.</p>
            actor_id: <p>The actor whose events to search (exact match). Required: every search covers exactly one actor, and an event stored without an actor is never returned. Narrow the search further with <code>sessionIds</code>, combined by AND. This is the only way to filter by actor: a query that references <code>system_metadata.actor_id</code> fails with <code>ValidationException</code> (reason <code>nonFilterableField</code>).</p>
            session_ids: <p>Returns only events from one of these sessions (exact match). Combined with <code>actorId</code> by AND. Omit for no session filter. An empty list fails validation. An event stored without a session never matches a session filter. This is the only way to filter by session: a query that references <code>system_metadata.session_id</code> fails with <code>ValidationException</code> (reason <code>nonFilterableField</code>).</p>
            query: <p>The query: a subset of the OpenSearch Query DSL (see <code>SearchQuery</code>), validated by the same rules as on <code>SearchMemories</code>. Query event text as <code>text</code> and embeddings as <code>vector</code>. A search covers both conversation turns and chunks of documents submitted as a <code>blob</code>. You can't use actor and session fields here. Use the top-level <code>actorId</code> and <code>sessionIds</code>.</p> <p>To search only the content of particular events, filter on <code>event_ids</code> with <code>term</code> or <code>terms</code>, for example with the <code>sourceEventIds</code> that a <code>SearchMemories</code> result returns. A <code>terms</code> clause on <code>event_ids</code> can list up to 10 event IDs. More IDs fail with <code>ValidationException</code> (reason <code>queryBodyTooLarge</code>). You can use <code>event_ids</code> only in <code>term</code>, <code>terms</code>, and <code>exists</code> queries.</p>
            sort: <p>The sort order (see <code>SearchSort</code>). Omit to return the most relevant events first.</p>
            max_results: <p>The maximum number of events to return, from 1 to 100. The default is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.search_events_input.SearchEventsInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.search_events_output.SearchEventsOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.search_events

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.search_events.search_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.search_events_input.SearchEventsInput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.search_events_input

            return capo_opensearchmemory.types.search_events_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_opensearchmemory.types.search_events_output.SearchEventsOutput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.search_events_output

            return capo_opensearchmemory.types.search_events_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "SearchEvents", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_opensearchmemory.types.search_events_input.SearchEventsInput = {
            "space_id": space_id,
            "actor_id": actor_id,
            "query": query,
        }
        if session_ids is not None:
            input_["session_ids"] = session_ids
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_events(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        query: "capo_opensearchmemory.types.search_query.SearchQuery",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        session_ids: Optional[
            "capo_opensearchmemory.types.session_id_list.SessionIdList"
        ] = None,
        sort: Optional["capo_opensearchmemory.types.search_sort.SearchSort"] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "Iterator[capo_opensearchmemory.types.event_search_summary.EventSearchSummary]"
    ):
        _token = next_token
        while True:
            _response = self.search_events(
                space_id,
                actor_id,
                query,
                config_overrides=config_overrides,
                session_ids=session_ids,
                sort=sort,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def search_memories(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        query: "capo_opensearchmemory.types.search_query.SearchQuery",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        memory_strategies: Optional[
            "capo_opensearchmemory.types.strategy_selector_list.StrategySelectorList"
        ] = None,
        sort: Optional["capo_opensearchmemory.types.search_sort.SearchSort"] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_opensearchmemory.types.search_memories_output.SearchMemoriesOutput":
        """<p>Searches a space's memories by relevance. The query is a subset of the OpenSearch Query DSL. The service validates it, limits the search to the requested strategies and to the actor in <code>actorId</code>, and returns one ranked list of memories. You can page through only a limited number of results. A request past that limit fails with <code>ValidationException</code> (reason <code>invalidNextToken</code>), and the message gives the limit.</p> <p>Memories past their expiry (set from the space's <code>memoryExpiryDays</code> when each memory is written) are left out of the results. Only current memories are returned: a memory that consolidation has superseded (an older version of a fact that a newer memory replaced) is left out.</p> <p>If the results are larger than 5 MiB, the request fails with <code>ValidationException</code> (reason <code>queryBodyTooLarge</code>). Lower <code>maxResults</code>.</p> <p>If the request would exceed the service's rate for embedding requests, it fails with <code>ThrottlingException</code>. Retry with exponential backoff.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The space to search. Use <code>actorId</code> to narrow the search within it.</p>
            memory_strategies: <p>The strategies to search, as a list of selectors. Each selector names a memory type and, optionally, specific strategy names of that type. A space can hold several strategies of the same type. A selector without <code>memoryStrategyNames</code> searches every strategy of its type, and omitting <code>memoryStrategies</code> searches every strategy in the space. A name that is not a declared strategy of that type fails with <code>ValidationException</code>.</p>
            actor_id: <p>The actor whose memories to search (exact match). Required: every search covers exactly one actor, and a memory stored without an actor is never returned. This is the only way to filter by actor: a query that references <code>system_metadata.actor_id</code> fails with <code>ValidationException</code> (reason <code>nonFilterableField</code>).</p>
            query: <p>The query: a subset of the OpenSearch Query DSL (see <code>SearchQuery</code>). You can't use the actor and session fields <code>system_metadata.actor_id</code> and <code>system_metadata.session_id</code> here. Use the top-level <code>actorId</code> to filter by actor. Searching memories doesn't filter by session.</p>
            sort: <p>The sort order (see <code>SearchSort</code>). Omit to return the most relevant memories first.</p>
            max_results: <p>The maximum number of memories to return, from 1 to 100. The default is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.search_memories_input.SearchMemoriesInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.search_memories_output.SearchMemoriesOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.search_memories

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.search_memories.search_memories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.search_memories_input.SearchMemoriesInput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.search_memories_input

            return capo_opensearchmemory.types.search_memories_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_opensearchmemory.types.search_memories_output.SearchMemoriesOutput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.search_memories_output

            return capo_opensearchmemory.types.search_memories_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "SearchMemories",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_opensearchmemory.types.search_memories_input.SearchMemoriesInput = {
            "space_id": space_id,
            "actor_id": actor_id,
            "query": query,
        }
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if sort is not None:
            input_["sort"] = sort
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_memories(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        actor_id: "capo_opensearchmemory.types.actor_id.ActorId",
        query: "capo_opensearchmemory.types.search_query.SearchQuery",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        memory_strategies: Optional[
            "capo_opensearchmemory.types.strategy_selector_list.StrategySelectorList"
        ] = None,
        sort: Optional["capo_opensearchmemory.types.search_sort.SearchSort"] = None,
        max_results: Optional[
            "capo_opensearchmemory.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_opensearchmemory.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_opensearchmemory.types.memory_search_summary.MemorySearchSummary]":
        _token = next_token
        while True:
            _response = self.search_memories(
                space_id,
                actor_id,
                query,
                config_overrides=config_overrides,
                memory_strategies=memory_strategies,
                sort=sort,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("memories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_memory(
        self,
        space_id: "capo_opensearchmemory.types.space_id.SpaceId",
        memory_id: "capo_opensearchmemory.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[OpenSearchMemoryClientConfig] = None,
        content: Optional[
            "capo_opensearchmemory.types.memory_update_content.MemoryUpdateContent"
        ] = None,
        metadata: Optional[
            "capo_opensearchmemory.types.metadata_map.MetadataMap"
        ] = None,
        metadata_mode: Optional[
            "capo_opensearchmemory.types.metadata_mode.MetadataMode"
        ] = None,
        actor_id: Optional["capo_opensearchmemory.types.actor_id.ActorId"] = None,
        strategy_name: Optional[
            "capo_opensearchmemory.types.strategy_name.StrategyName"
        ] = None,
    ) -> "capo_opensearchmemory.types.update_memory_output.UpdateMemoryOutput":
        """<p>Updates a memory in place. Supply only the fields to change. Omitted fields keep their stored values. A request must supply <code>content</code> or <code>metadata</code>, or it fails with <code>ValidationException</code>. Supplying <code>content</code> re-embeds the memory. A change to metadata alone doesn't.</p> <p>The memory keeps its <code>memoryId</code> across updates. Shortly after an update, searches stop returning the previous content.</p> <p> <code>memoryType</code> can't be changed. To change it, delete the memory and create a new one.</p> <p>A memory past its expiry (set from the space's <code>memoryExpiryDays</code> when the memory is written) reads as not found: the operation fails with <code>ResourceNotFoundException</code> and changes nothing. An update does not move the expiry.</p> <p>Concurrent updates to one memory are last-writer-wins. There is no version check. To avoid lost updates, serialize your updates to a memory.</p> <p>If you supply <code>content</code> and the request would exceed the service's rate for embedding requests, it fails with <code>ThrottlingException</code>. Retry with exponential backoff.</p> <p>If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with <code>AccessDeniedException</code> if you aren't allowed to use the key, and with <code>ThrottlingException</code> if AWS KMS throttles the request. It fails with <code>ValidationException</code> if the key is disabled, pending deletion, or deleted.</p>

        Args:
            space_id: <p>The ID of the space that owns the memory, for example <code>sp-02864597b164</code>.</p>
            memory_id: <p>The ID of the memory to update.</p>
            content: <p>Replacement memory text. Supplying it re-embeds the memory. Omit to leave the text unchanged.</p>
            metadata: <p>The metadata tags to apply. By default this map replaces the stored metadata, and any key not present is removed. Set <code>metadataMode</code> to <code>MERGE</code> to keep the keys you don't supply. Limits apply to the resulting metadata, not to the request. Keys that begin with <code>x-amz-</code> and the key <code>documentS3Source</code> are reserved: a request that sets one fails with <code>ValidationException</code>.</p> <p>A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with <code>ValidationException</code>. Reuse an existing key instead.</p>
            metadata_mode: <p>How <code>metadata</code> combines with what is stored. The default is <code>REPLACE</code>.</p>
            actor_id: <p>The ID of the actor that the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>
            strategy_name: <p>The name of the strategy that the memory must belong to. Omit it to skip this check. If it doesn't match the stored memory, the call fails with <code>ResourceNotFoundException</code>, as if the memory did not exist.</p>

        Raises:
            capo_opensearchmemory.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.</p>
            capo_opensearchmemory.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.</p>
            capo_opensearchmemory.errors.internal_server_exception.InternalServerException: <p>The service couldn't process the request because of an internal error. Retry the request.</p>
            capo_opensearchmemory.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource doesn't exist. Check the IDs in the request.</p>
            capo_opensearchmemory.errors.throttling_exception.ThrottlingException: <p>The service throttled the request. Retry the request with exponential backoff.</p>
            capo_opensearchmemory.errors.validation_exception.ValidationException: <p>The request isn't valid. The <code>reason</code>, <code>message</code>, and <code>fieldList</code> members describe the problem. Fix the request, and then try again.</p>
            capo_opensearchmemory.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_opensearchmemory.types.update_memory_input.UpdateMemoryInput]",
        ) -> OperationResponse[
            "capo_opensearchmemory.types.update_memory_output.UpdateMemoryOutput"
        ]:
            import capo_opensearchmemory._operations.open_search_memory.update_memory

            output, http_response = (
                capo_opensearchmemory._operations.open_search_memory.update_memory.update_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_opensearchmemory.types.update_memory_input.UpdateMemoryInput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.update_memory_input

            return capo_opensearchmemory.types.update_memory_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_opensearchmemory.types.update_memory_output.UpdateMemoryOutput",
        ) -> dict[str, Any]:
            import capo_opensearchmemory.types.update_memory_output

            return capo_opensearchmemory.types.update_memory_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateMemory", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_opensearchmemory.types.update_memory_input.UpdateMemoryInput = {
            "space_id": space_id,
            "memory_id": memory_id,
        }
        if content is not None:
            input_["content"] = content
        if metadata is not None:
            input_["metadata"] = metadata
        if metadata_mode is not None:
            input_["metadata_mode"] = metadata_mode
        if actor_id is not None:
            input_["actor_id"] = actor_id
        if strategy_name is not None:
            input_["strategy_name"] = strategy_name

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
