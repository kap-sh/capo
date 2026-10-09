"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#AmazonBedrockKeystoneRuntimeService``."""

import uuid
import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bedrock_data_automation_runtime._auth._signers
import capo_bedrock_data_automation_runtime._auth._sigv4
from capo_bedrock_data_automation_runtime._auth._identity import Credentials
from capo_bedrock_data_automation_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_data_automation_runtime._auth._zapros_handler import AuthMiddleware
from capo_bedrock_data_automation_runtime._resources.amazon_bedrock_keystone_runtime_service.automation_job_resource import (
    AsyncAutomationJobResource,
)
from capo_bedrock_data_automation_runtime._services._aws_config import aaws_config
from capo_bedrock_data_automation_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.blueprint_list
    import capo_bedrock_data_automation_runtime.types.data_automation_configuration
    import capo_bedrock_data_automation_runtime.types.data_automation_profile_arn
    import capo_bedrock_data_automation_runtime.types.encryption_configuration
    import capo_bedrock_data_automation_runtime.types.get_data_automation_status_request
    import capo_bedrock_data_automation_runtime.types.get_data_automation_status_response
    import capo_bedrock_data_automation_runtime.types.idempotency_token
    import capo_bedrock_data_automation_runtime.types.input_configuration
    import capo_bedrock_data_automation_runtime.types.invocation_arn
    import capo_bedrock_data_automation_runtime.types.invoke_data_automation_async_request
    import capo_bedrock_data_automation_runtime.types.invoke_data_automation_async_response
    import capo_bedrock_data_automation_runtime.types.invoke_data_automation_request
    import capo_bedrock_data_automation_runtime.types.invoke_data_automation_response
    import capo_bedrock_data_automation_runtime.types.list_tags_for_resource_request
    import capo_bedrock_data_automation_runtime.types.list_tags_for_resource_response
    import capo_bedrock_data_automation_runtime.types.notification_configuration
    import capo_bedrock_data_automation_runtime.types.output_configuration
    import capo_bedrock_data_automation_runtime.types.sync_input_configuration
    import capo_bedrock_data_automation_runtime.types.tag_key_list
    import capo_bedrock_data_automation_runtime.types.tag_list
    import capo_bedrock_data_automation_runtime.types.tag_resource_request
    import capo_bedrock_data_automation_runtime.types.tag_resource_response
    import capo_bedrock_data_automation_runtime.types.taggable_resource_arn
    import capo_bedrock_data_automation_runtime.types.untag_resource_request
    import capo_bedrock_data_automation_runtime.types.untag_resource_response


class AsyncBedrockDataAutomationRuntimeClientConfig(
    TypedDict, total=False, closed=True
):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncBedrockDataAutomationRuntimeClient:
    """A client for the ``BedrockDataAutomationRuntime`` service.

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
        self._config = AsyncBedrockDataAutomationRuntimeClientConfig(
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
        self.automation_job_resource = AsyncAutomationJobResource(self)

    def operation_options(
        self,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockDataAutomationRuntimeClientConfig = (
            config_overrides or {}
        )
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

    async def invoke_data_automation(
        self,
        input_configuration: "capo_bedrock_data_automation_runtime.types.sync_input_configuration.SyncInputConfiguration",
        data_automation_profile_arn: "capo_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
        data_automation_configuration: Optional[
            "capo_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
        ] = None,
        blueprints: Optional[
            "capo_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        output_configuration: Optional[
            "capo_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
        ] = None,
    ) -> "capo_bedrock_data_automation_runtime.types.invoke_data_automation_response.InvokeDataAutomationResponse":
        """Sync API: Invoke data automation.

        Args:
            input_configuration: Input configuration.
            data_automation_configuration: Data automation configuration.
            blueprints: Blueprint list.
            data_automation_profile_arn: Data automation profile ARN
            encryption_configuration: Encryption configuration.
            output_configuration: Output configuration.

        Raises:
            capo_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            capo_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            capo_bedrock_data_automation_runtime.errors.service_unavailable_exception.ServiceUnavailableException: This exception will be thrown when service is temporarily unavailable.
            capo_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            capo_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            capo_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation_runtime.types.invoke_data_automation_request.InvokeDataAutomationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation_runtime.types.invoke_data_automation_response.InvokeDataAutomationResponse"
        ]:
            import capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation.async_invoke_data_automation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation_runtime.types.invoke_data_automation_request.InvokeDataAutomationRequest = {
            "input_configuration": input_configuration,
            "data_automation_profile_arn": data_automation_profile_arn,
        }
        if data_automation_configuration is not None:
            input_["data_automation_configuration"] = data_automation_configuration
        if blueprints is not None:
            input_["blueprints"] = blueprints
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if output_configuration is not None:
            input_["output_configuration"] = output_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
    ) -> "capo_bedrock_data_automation_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """List tags for an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            capo_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            capo_bedrock_data_automation_runtime.errors.resource_not_found_exception.ResourceNotFoundException: This exception will be thrown when resource provided from customer not found.
            capo_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            capo_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            capo_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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
        resource_arn: "capo_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn",
        tags: "capo_bedrock_data_automation_runtime.types.tag_list.TagList",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
    ) -> "capo_bedrock_data_automation_runtime.types.tag_resource_response.TagResourceResponse":
        """Tag an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            capo_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            capo_bedrock_data_automation_runtime.errors.resource_not_found_exception.ResourceNotFoundException: This exception will be thrown when resource provided from customer not found.
            capo_bedrock_data_automation_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception will be thrown when service quota is exceeded.
            capo_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            capo_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            capo_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation_runtime.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation_runtime.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation_runtime.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_bedrock_data_automation_runtime.types.taggable_resource_arn.TaggableResourceArn",
        tag_keys: "capo_bedrock_data_automation_runtime.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
    ) -> "capo_bedrock_data_automation_runtime.types.untag_resource_response.UntagResourceResponse":
        """Untag an Amazon Bedrock Data Automation resource

        Raises:
            capo_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            capo_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            capo_bedrock_data_automation_runtime.errors.resource_not_found_exception.ResourceNotFoundException: This exception will be thrown when resource provided from customer not found.
            capo_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            capo_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            capo_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation_runtime.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation_runtime.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation_runtime.types.untag_resource_request.UntagResourceRequest = {
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

    async def invoke_data_automation_async(
        self,
        input_configuration: "capo_bedrock_data_automation_runtime.types.input_configuration.InputConfiguration",
        output_configuration: "capo_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration",
        data_automation_profile_arn: "capo_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
        client_token: Optional[
            "capo_bedrock_data_automation_runtime.types.idempotency_token.IdempotencyToken"
        ] = None,
        data_automation_configuration: Optional[
            "capo_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
        ] = None,
        encryption_configuration: Optional[
            "capo_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        notification_configuration: Optional[
            "capo_bedrock_data_automation_runtime.types.notification_configuration.NotificationConfiguration"
        ] = None,
        blueprints: Optional[
            "capo_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
        ] = None,
        tags: Optional[
            "capo_bedrock_data_automation_runtime.types.tag_list.TagList"
        ] = None,
    ) -> "capo_bedrock_data_automation_runtime.types.invoke_data_automation_async_response.InvokeDataAutomationAsyncResponse":
        """Async API: Invoke data automation.

        Args:
            client_token: Idempotency token.
            input_configuration: Input configuration.
            output_configuration: Output configuration.
            data_automation_configuration: Data automation configuration.
            encryption_configuration: Encryption configuration.
            notification_configuration: Notification configuration.
            blueprints: Blueprint list.
            data_automation_profile_arn: Data automation profile ARN
            tags: List of tags.

        Raises:
            capo_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            capo_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            capo_bedrock_data_automation_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: This exception will be thrown when service quota is exceeded.
            capo_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            capo_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            capo_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation_runtime.types.invoke_data_automation_async_request.InvokeDataAutomationAsyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation_runtime.types.invoke_data_automation_async_response.InvokeDataAutomationAsyncResponse"
        ]:
            import capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation_async

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.invoke_data_automation_async.async_invoke_data_automation_async(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation_runtime.types.invoke_data_automation_async_request.InvokeDataAutomationAsyncRequest = {
            "input_configuration": input_configuration,
            "output_configuration": output_configuration,
            "data_automation_profile_arn": data_automation_profile_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if data_automation_configuration is not None:
            input_["data_automation_configuration"] = data_automation_configuration
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if notification_configuration is not None:
            input_["notification_configuration"] = notification_configuration
        if blueprints is not None:
            input_["blueprints"] = blueprints
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_automation_status(
        self,
        invocation_arn: "capo_bedrock_data_automation_runtime.types.invocation_arn.InvocationArn",
        *,
        config_overrides: Optional[
            AsyncBedrockDataAutomationRuntimeClientConfig
        ] = None,
    ) -> "capo_bedrock_data_automation_runtime.types.get_data_automation_status_response.GetDataAutomationStatusResponse":
        """API used to get data automation status.

        Args:
            invocation_arn: Invocation arn.

        Raises:
            capo_bedrock_data_automation_runtime.errors.access_denied_exception.AccessDeniedException: This exception will be thrown when customer does not have access to API.
            capo_bedrock_data_automation_runtime.errors.internal_server_exception.InternalServerException: This exception is for any internal un-expected service errors.
            capo_bedrock_data_automation_runtime.errors.resource_not_found_exception.ResourceNotFoundException: This exception will be thrown when resource provided from customer not found.
            capo_bedrock_data_automation_runtime.errors.throttling_exception.ThrottlingException: This exception will be thrown when customer reached API TPS limit.
            capo_bedrock_data_automation_runtime.errors.validation_exception.ValidationException: This exception will be thrown when customer provided invalid parameters.
            capo_bedrock_data_automation_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_data_automation_runtime.types.get_data_automation_status_request.GetDataAutomationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_data_automation_runtime.types.get_data_automation_status_response.GetDataAutomationStatusResponse"
        ]:
            import capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.get_data_automation_status

            (
                output,
                http_response,
            ) = await capo_bedrock_data_automation_runtime._operations.amazon_bedrock_keystone_runtime_service.get_data_automation_status.async_get_data_automation_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_data_automation_runtime.types.get_data_automation_status_request.GetDataAutomationStatusRequest = {
            "invocation_arn": invocation_arn
        }

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
