"""Generated from Smithy shape ``com.amazonaws.lambdacore#LambdaCoreApiService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Literal, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lambda_core._auth._signers
import capo_lambda_core._auth._sigv4
from capo_lambda_core._auth._identity import Credentials
from capo_lambda_core._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lambda_core._auth._zapros_handler import AuthMiddleware
from capo_lambda_core._pagination import resolve_path as _resolve_path
from capo_lambda_core._resources.lambda_core_api_service.managed_runtime import (
    AsyncManagedRuntime,
)
from capo_lambda_core._resources.lambda_core_api_service.network_connector import (
    AsyncNetworkConnector,
)
from capo_lambda_core._services._aws_config import aaws_config
from capo_lambda_core._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    RateLimiter,
    RetryQuota,
    aexecute_pipeline,
    alog_operation,
    arate_limit,
    aretry,
)

if TYPE_CHECKING:
    import capo_lambda_core.types.aws_gir_api_string
    import capo_lambda_core.types.client_token_string
    import capo_lambda_core.types.create_network_connector_request
    import capo_lambda_core.types.create_network_connector_response
    import capo_lambda_core.types.create_runtime_alias_request
    import capo_lambda_core.types.create_runtime_alias_response
    import capo_lambda_core.types.create_runtime_request
    import capo_lambda_core.types.create_runtime_response
    import capo_lambda_core.types.create_runtime_version_request
    import capo_lambda_core.types.create_runtime_version_response
    import capo_lambda_core.types.delete_network_connector_request
    import capo_lambda_core.types.delete_network_connector_response
    import capo_lambda_core.types.delete_runtime_alias_request
    import capo_lambda_core.types.delete_runtime_alias_response
    import capo_lambda_core.types.delete_runtime_request
    import capo_lambda_core.types.delete_runtime_response
    import capo_lambda_core.types.delete_runtime_version_request
    import capo_lambda_core.types.delete_runtime_version_response
    import capo_lambda_core.types.get_network_connector_request
    import capo_lambda_core.types.get_network_connector_response
    import capo_lambda_core.types.get_runtime_alias_request
    import capo_lambda_core.types.get_runtime_alias_response
    import capo_lambda_core.types.get_runtime_request
    import capo_lambda_core.types.get_runtime_response
    import capo_lambda_core.types.get_runtime_version_request
    import capo_lambda_core.types.get_runtime_version_response
    import capo_lambda_core.types.list_network_connector_versions_request
    import capo_lambda_core.types.list_network_connector_versions_response
    import capo_lambda_core.types.list_network_connectors_request
    import capo_lambda_core.types.list_network_connectors_response
    import capo_lambda_core.types.list_runtime_aliases_request
    import capo_lambda_core.types.list_runtime_aliases_response
    import capo_lambda_core.types.list_runtime_versions_request
    import capo_lambda_core.types.list_runtime_versions_response
    import capo_lambda_core.types.list_runtimes_request
    import capo_lambda_core.types.list_runtimes_response
    import capo_lambda_core.types.max_hundred_list_items
    import capo_lambda_core.types.network_connector_configuration
    import capo_lambda_core.types.network_connector_identifier
    import capo_lambda_core.types.network_connector_name
    import capo_lambda_core.types.network_connector_role_arn
    import capo_lambda_core.types.network_connector_state
    import capo_lambda_core.types.network_connector_summary
    import capo_lambda_core.types.network_connector_tags
    import capo_lambda_core.types.network_connector_version_summary
    import capo_lambda_core.types.restore_runtime_request
    import capo_lambda_core.types.restore_runtime_response
    import capo_lambda_core.types.runtime_alias_description
    import capo_lambda_core.types.runtime_alias_info
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_description
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_info
    import capo_lambda_core.types.runtime_license_info
    import capo_lambda_core.types.runtime_name
    import capo_lambda_core.types.runtime_release_lifecycle
    import capo_lambda_core.types.runtime_version_info
    import capo_lambda_core.types.runtime_version_name
    import capo_lambda_core.types.tag_map
    import capo_lambda_core.types.update_network_connector_request
    import capo_lambda_core.types.update_network_connector_response
    import capo_lambda_core.types.update_runtime_alias_request
    import capo_lambda_core.types.update_runtime_alias_response
    import capo_lambda_core.types.update_runtime_request
    import capo_lambda_core.types.update_runtime_response
    import capo_lambda_core.types.update_runtime_version_request
    import capo_lambda_core.types.update_runtime_version_response


class AsyncLambdaCoreClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    retry_mode: Literal["standard", "adaptive"] | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLambdaCoreClient:
    """A client for the ``LambdaCore`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        retry_mode: ``"standard"`` (the default) or ``"adaptive"``, which also slows the whole client down when the service throttles it.
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
        retry_mode: Literal["standard", "adaptive"] | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        client = AsyncClient(http_handler)
        # The handler the user gave us, or the default one for this environment.
        # The SDK middlewares wrap it below, and the credential resolvers borrow
        # it for their one-off calls.
        raw_handler = client.handler
        self._client = client.wrap_with_middleware(lambda next: AuthMiddleware(next))
        # One retry quota for all of this client's operations.
        self._retry_quota = RetryQuota()
        # One send-rate limiter too, used when retry_mode is adaptive.
        self._rate_limiter = RateLimiter()
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
                AsyncClient(raw_handler)
            )
        self._config = AsyncLambdaCoreClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "retry_mode": retry_mode,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.managed_runtime = AsyncManagedRuntime(self)
        self.network_connector = AsyncNetworkConnector(self)

    def operation_options(
        self,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        operation_logging: OperationLogging | None = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLambdaCoreClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
        ]
        if operation_logging is not None:
            interceptors_.append(alog_operation(operation_logging))
        interceptors_.append(aretry())
        interceptors_.append(arate_limit())
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_quota=self._retry_quota,
            rate_limiter=self._rate_limiter,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            retry_mode=overrides.get("retry_mode", self._config.get("retry_mode")),
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

    async def create_runtime(
        self,
        name: "capo_lambda_core.types.runtime_name.RuntimeName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        tags: Optional["capo_lambda_core.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_lambda_core.types.runtime_description.RuntimeDescription"
        ] = None,
        license_info: Optional[
            "capo_lambda_core.types.runtime_license_info.RuntimeLicenseInfo"
        ] = None,
        release_lifecycle: Optional[
            "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
        ] = None,
    ) -> "capo_lambda_core.types.create_runtime_response.CreateRuntimeResponse":
        """Creates a customer-managed runtime, a resource providing a centrally managed execution environment for your Lambda functions. The runtime resource is the parent of the runtime version and runtime alias child resources.

        Args:
            name: The name of the runtime to create.
            tags: A map of tag keys and values to associate with the runtime.
            description: A description of the runtime.
            license_info: The license information for the runtime.
            release_lifecycle: The runtime lifecycle for the runtime (optional). Use this to schedule runtime deprecation.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account. Request a quota increase or reduce the number of resources in use, then retry the request.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a runtime
            Creates a customer-managed runtime resource.

            >>> await client.create_runtime(name='php8', description='PHP 8 custom runtime', license_info='MIT', tags={'team': 'runtimes'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.create_runtime_request.CreateRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.create_runtime_response.CreateRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_runtime

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.create_runtime.async_create_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateRuntime")
        )
        input_: capo_lambda_core.types.create_runtime_request.CreateRuntimeRequest = {
            "name": name
        }
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description
        if license_info is not None:
            input_["license_info"] = license_info
        if release_lifecycle is not None:
            input_["release_lifecycle"] = release_lifecycle

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_runtime(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.get_runtime_response.GetRuntimeResponse":
        """Retrieves the configuration and metadata of a runtime.

        Args:
            runtime_name: The name or ARN of the runtime to retrieve.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a runtime
            Retrieves the metadata for a runtime by name.

            >>> await client.get_runtime(runtime_name='php8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.get_runtime_request.GetRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.get_runtime_response.GetRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_runtime

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.get_runtime.async_get_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetRuntime")
        )
        input_: capo_lambda_core.types.get_runtime_request.GetRuntimeRequest = {
            "runtime_name": runtime_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_runtime(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        description: Optional[
            "capo_lambda_core.types.runtime_description.RuntimeDescription"
        ] = None,
        license_info: Optional[
            "capo_lambda_core.types.runtime_license_info.RuntimeLicenseInfo"
        ] = None,
        release_lifecycle: Optional[
            "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
        ] = None,
    ) -> "capo_lambda_core.types.update_runtime_response.UpdateRuntimeResponse":
        """Updates the properties of an existing customer-managed runtime, such as its description, license information, or lifecycle information.

        Args:
            runtime_name: The name or ARN of the runtime to update.
            description: The updated description of the runtime.
            license_info: The updated license information for the runtime.
            release_lifecycle: The runtime lifecycle for the runtime. Optional. Used to schedule runtime deprecation. Omitting or providing an empty object removes the existing lifecycle.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a runtime
            Updates a runtime's description and declares it generally available.

            >>> await client.update_runtime(runtime_name='php8', description='PHP 8 custom runtime (updated)', release_lifecycle={'ReleaseState': 'GA'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.update_runtime_request.UpdateRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.update_runtime_response.UpdateRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_runtime

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.update_runtime.async_update_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateRuntime")
        )
        input_: capo_lambda_core.types.update_runtime_request.UpdateRuntimeRequest = {
            "runtime_name": runtime_name
        }
        if description is not None:
            input_["description"] = description
        if license_info is not None:
            input_["license_info"] = license_info
        if release_lifecycle is not None:
            input_["release_lifecycle"] = release_lifecycle

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_runtime(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        recovery_window_in_days: Optional[int] = None,
    ) -> "capo_lambda_core.types.delete_runtime_response.DeleteRuntimeResponse":
        """Schedules a customer-managed runtime to be deleted. Runtimes scheduled for deletion enter the PENDING_DELETION state and can be restored during the scheduled deletion window. Runtime versions and aliases must be deleted or scheduled for deletion before deleting the runtime. Function invokes fail for functions using runtime versions or aliases that are deleted or pending deletion.

        Args:
            runtime_name: The name or ARN of the runtime to delete.
            recovery_window_in_days: Optional. The waiting period, in days (7-30), before the runtime is permanently deleted.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a runtime
            Schedules a customer-managed runtime to be deleted.

            >>> await client.delete_runtime(runtime_name='php8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.delete_runtime_request.DeleteRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.delete_runtime_response.DeleteRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_runtime

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.delete_runtime.async_delete_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteRuntime")
        )
        input_: capo_lambda_core.types.delete_runtime_request.DeleteRuntimeRequest = {
            "runtime_name": runtime_name
        }
        if recovery_window_in_days is not None:
            input_["recovery_window_in_days"] = recovery_window_in_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_runtimes(
        self,
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_lambda_core.types.list_runtimes_response.ListRuntimesResponse":
        """Returns a paginated list of runtimes in your account for the current Region.

        Args:
            next_token: The pagination token from a previous response. Use it to retrieve the next page of results.
            max_results: The maximum number of runtimes to return per page. Valid range: 1 to 100.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List runtimes
            Lists the runtimes in the account and region.

            >>> await client.list_runtimes(max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.list_runtimes_request.ListRuntimesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.list_runtimes_response.ListRuntimesResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_runtimes

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.list_runtimes.async_list_runtimes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListRuntimes")
        )
        input_: capo_lambda_core.types.list_runtimes_request.ListRuntimesRequest = {}
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

    async def iter_list_runtimes(
        self,
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_lambda_core.types.runtime_info.RuntimeInfo]":
        _token = next_token
        while True:
            _response = await self.list_runtimes(
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

    async def restore_runtime(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        runtime_version: Optional[
            "capo_lambda_core.types.runtime_version_name.RuntimeVersionName"
        ] = None,
        runtime_alias: Optional[
            "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName"
        ] = None,
    ) -> "capo_lambda_core.types.restore_runtime_response.RestoreRuntimeResponse":
        """Cancels a pending scheduled deletion, returning the resource to the ACTIVE state. Scope is determined by the RuntimeName path parameter plus an optional, mutually exclusive RuntimeVersion or RuntimeAlias query parameter: with neither, the runtime itself is restored; with RuntimeVersion, the named runtime version; with RuntimeAlias, the named runtime alias. Restoring a resource that is already ACTIVE is a no-op success. Restore only works while the target is PENDING_DELETION; once the scheduled deletion has begun executing (DELETING) or has completed, the call fails.

        Args:
            runtime_name: The name or ARN of the runtime to restore. When RuntimeVersion or RuntimeAlias is specified, the runtime that owns the runtime version or runtime alias to restore.
            runtime_version: Optional. Restores the named RuntimeVersion under RuntimeName. Mutually exclusive with RuntimeAlias; supplying both is rejected with InvalidParameterValueException.
            runtime_alias: Optional. Restores the named RuntimeAlias under RuntimeName. Mutually exclusive with RuntimeVersion; supplying both is rejected with InvalidParameterValueException.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Restore a runtime alias that is scheduled for deletion
            Cancels a pending deletion for an alias, returning it to ACTIVE.

            >>> await client.restore_runtime(runtime_name='php8', runtime_alias='release')
            Restore a customer-managed runtime that is scheduled for deletion
            Cancels a pending deletion for the runtime, returning it to ACTIVE.

            >>> await client.restore_runtime(runtime_name='php8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.restore_runtime_request.RestoreRuntimeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.restore_runtime_response.RestoreRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.restore_runtime

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.restore_runtime.async_restore_runtime(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("RestoreRuntime")
        )
        input_: capo_lambda_core.types.restore_runtime_request.RestoreRuntimeRequest = {
            "runtime_name": runtime_name
        }
        if runtime_version is not None:
            input_["runtime_version"] = runtime_version
        if runtime_alias is not None:
            input_["runtime_alias"] = runtime_alias

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_runtime_alias(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        runtime_version: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName",
        name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        description: Optional[
            "capo_lambda_core.types.runtime_alias_description.RuntimeAliasDescription"
        ] = None,
        release_lifecycle: Optional[
            "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
        ] = None,
    ) -> "capo_lambda_core.types.create_runtime_alias_response.CreateRuntimeAliasResponse":
        """Creates a new customer-managed runtime alias. The alias is a named pointer to a runtime version. Functions consume the customer-managed runtime through the runtime alias.

        Args:
            runtime_name: The name or ARN of the runtime to create an alias for.
            runtime_version: The name of the runtime version the alias points to.
            name: The name to assign to the new runtime alias.
            description: A description of the runtime alias.
            release_lifecycle: The runtime lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account. Request a quota increase or reduce the number of resources in use, then retry the request.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a runtime alias
            Creates an alias that points at a published runtime version.

            >>> await client.create_runtime_alias(runtime_name='php8', name='latest', runtime_version='v1', description='Points at the newest published version')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.create_runtime_alias_request.CreateRuntimeAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.create_runtime_alias_response.CreateRuntimeAliasResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_runtime_alias

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.create_runtime_alias.async_create_runtime_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateRuntimeAlias")
        )
        input_: capo_lambda_core.types.create_runtime_alias_request.CreateRuntimeAliasRequest = {
            "runtime_name": runtime_name,
            "runtime_version": runtime_version,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if release_lifecycle is not None:
            input_["release_lifecycle"] = release_lifecycle

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_runtime_alias(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.get_runtime_alias_response.GetRuntimeAliasResponse":
        """Retrieves the configuration, state, and metadata of a runtime alias.

        Args:
            runtime_name: The name or ARN of the runtime.
            name: The name of the runtime alias to retrieve.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a runtime alias
            Retrieves an alias, including the version it currently points at and its compatibility matrix.

            >>> await client.get_runtime_alias(runtime_name='php8', name='latest')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.get_runtime_alias_request.GetRuntimeAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.get_runtime_alias_response.GetRuntimeAliasResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_runtime_alias

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.get_runtime_alias.async_get_runtime_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetRuntimeAlias")
        )
        input_: capo_lambda_core.types.get_runtime_alias_request.GetRuntimeAliasRequest = {
            "runtime_name": runtime_name,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_runtime_alias(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName",
        runtime_version: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        description: Optional[
            "capo_lambda_core.types.runtime_alias_description.RuntimeAliasDescription"
        ] = None,
        release_lifecycle: Optional[
            "capo_lambda_core.types.runtime_release_lifecycle.RuntimeReleaseLifecycle"
        ] = None,
    ) -> "capo_lambda_core.types.update_runtime_alias_response.UpdateRuntimeAliasResponse":
        """Updates an existing runtime alias to point to a different runtime version or to change its description or lifecycle information.

        Args:
            runtime_name: The name or ARN of the runtime.
            name: The name of the runtime alias to update.
            runtime_version: The name of the runtime version the alias should point to.
            description: A description of the runtime alias.
            release_lifecycle: The lifecycle for the alias. By default, this is inherited from the runtime lifecycle. Optionally, you can override the lifecycle information at the alias level, if required. Omitting or providing an empty object removes the existing lifecycle override.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a runtime alias
            Repoints an alias at a different runtime version.

            >>> await client.update_runtime_alias(runtime_name='php8', name='latest', runtime_version='v2')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.update_runtime_alias_request.UpdateRuntimeAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.update_runtime_alias_response.UpdateRuntimeAliasResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_runtime_alias

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.update_runtime_alias.async_update_runtime_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateRuntimeAlias")
        )
        input_: capo_lambda_core.types.update_runtime_alias_request.UpdateRuntimeAliasRequest = {
            "runtime_name": runtime_name,
            "name": name,
            "runtime_version": runtime_version,
        }
        if description is not None:
            input_["description"] = description
        if release_lifecycle is not None:
            input_["release_lifecycle"] = release_lifecycle

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_runtime_alias(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        name: "capo_lambda_core.types.runtime_alias_name.RuntimeAliasName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        recovery_window_in_days: Optional[int] = None,
    ) -> "capo_lambda_core.types.delete_runtime_alias_response.DeleteRuntimeAliasResponse":
        """Schedules a runtime alias to be deleted. Runtime aliases scheduled for deletion enter the PENDING_DELETION state and can be restored during the scheduled deletion window. Function invokes fail for functions using runtime aliases that are deleted or pending deletion.

        Args:
            runtime_name: The name or ARN of the runtime.
            name: The name of the runtime alias to delete.
            recovery_window_in_days: Optional. The waiting period, in days (7-30), before the runtime alias is permanently deleted.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a runtime alias
            Schedules a runtime alias to be deleted.

            >>> await client.delete_runtime_alias(runtime_name='php8', name='latest')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.delete_runtime_alias_request.DeleteRuntimeAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.delete_runtime_alias_response.DeleteRuntimeAliasResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_runtime_alias

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.delete_runtime_alias.async_delete_runtime_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteRuntimeAlias")
        )
        input_: capo_lambda_core.types.delete_runtime_alias_request.DeleteRuntimeAliasRequest = {
            "runtime_name": runtime_name,
            "name": name,
        }
        if recovery_window_in_days is not None:
            input_["recovery_window_in_days"] = recovery_window_in_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_runtime_aliases(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_lambda_core.types.list_runtime_aliases_response.ListRuntimeAliasesResponse":
        """Returns a paginated list of aliases for the specified runtime.

        Args:
            runtime_name: The name or ARN of the runtime whose aliases to list.
            next_token: The pagination token from a previous response. Use it to retrieve the next page of results.
            max_results: The maximum number of runtime aliases to return per page. Valid range: 1 to 100.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List runtime aliases
            Lists the aliases defined on a runtime.

            >>> await client.list_runtime_aliases(runtime_name='php8', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.list_runtime_aliases_request.ListRuntimeAliasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.list_runtime_aliases_response.ListRuntimeAliasesResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_runtime_aliases

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.list_runtime_aliases.async_list_runtime_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListRuntimeAliases")
        )
        input_: capo_lambda_core.types.list_runtime_aliases_request.ListRuntimeAliasesRequest = {
            "runtime_name": runtime_name
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

    async def iter_list_runtime_aliases(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_lambda_core.types.runtime_alias_info.RuntimeAliasInfo]":
        _token = next_token
        while True:
            _response = await self.list_runtime_aliases(
                runtime_name,
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

    async def create_runtime_version(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        image_uri: str,
        name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        release_notes: Optional[str] = None,
        dry_run: Optional[bool] = None,
    ) -> "capo_lambda_core.types.create_runtime_version_response.CreateRuntimeVersionResponse":
        """Creates a new runtime version. A runtime version defines the function execution environment by referencing a container image. Runtime versions are immutable. To update the runtime, create a new runtime version and migrate functions by updating the runtime aliases to point to the new runtime version.

        Args:
            runtime_name: The name or ARN of the runtime to create a version for.
            image_uri: The URI of the container image used to define the function execution environment for this runtime version.
            name: The name to assign to the new runtime version.
            release_notes: The release notes to associate with the runtime version.
            dry_run: When set to true, the request is validated without creating a new runtime version. Use this to check that the request would succeed. No runtime version is created and no changes are made.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota for your account. Request a quota increase or reduce the number of resources in use, then retry the request.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a runtime version
            Creates a new runtime version from a container image.

            >>> await client.create_runtime_version(runtime_name='php8', name='v1', image_uri='123456789012.dkr.ecr.us-west-2.amazonaws.com/php8:latest', release_notes='Initial release')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.create_runtime_version_request.CreateRuntimeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.create_runtime_version_response.CreateRuntimeVersionResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_runtime_version

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.create_runtime_version.async_create_runtime_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateRuntimeVersion")
        )
        input_: capo_lambda_core.types.create_runtime_version_request.CreateRuntimeVersionRequest = {
            "runtime_name": runtime_name,
            "image_uri": image_uri,
            "name": name,
        }
        if release_notes is not None:
            input_["release_notes"] = release_notes
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_runtime_version(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> (
        "capo_lambda_core.types.get_runtime_version_response.GetRuntimeVersionResponse"
    ):
        """Retrieves the configuration, state, and metadata of a runtime version.

        Args:
            runtime_name: The name or ARN of the runtime.
            name: The name of the runtime version to retrieve.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a runtime version
            Retrieves a runtime version, including its resolved image URI, per-architecture platforms, and compatibility matrix.

            >>> await client.get_runtime_version(runtime_name='php8', name='v1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.get_runtime_version_request.GetRuntimeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.get_runtime_version_response.GetRuntimeVersionResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_runtime_version

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.get_runtime_version.async_get_runtime_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetRuntimeVersion")
        )
        input_: capo_lambda_core.types.get_runtime_version_request.GetRuntimeVersionRequest = {
            "runtime_name": runtime_name,
            "name": name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_runtime_version(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName",
        release_notes: str,
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.update_runtime_version_response.UpdateRuntimeVersionResponse":
        """Updates the runtime version release notes. The runtime version must be in the ACTIVE state. The runtime version image is immutable. To change the runtime contents, create a new runtime version.

        Args:
            runtime_name: The name or ARN of the runtime.
            name: The name of the runtime version to update.
            release_notes: The release notes to associate with the runtime version.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a runtime version's release notes
            Updates the release notes of an ACTIVE runtime version.

            >>> await client.update_runtime_version(runtime_name='php8', name='v1', release_notes='Patched OpenSSL to 3.0.14')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.update_runtime_version_request.UpdateRuntimeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.update_runtime_version_response.UpdateRuntimeVersionResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_runtime_version

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.update_runtime_version.async_update_runtime_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateRuntimeVersion")
        )
        input_: capo_lambda_core.types.update_runtime_version_request.UpdateRuntimeVersionRequest = {
            "runtime_name": runtime_name,
            "name": name,
            "release_notes": release_notes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_runtime_version(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        name: "capo_lambda_core.types.runtime_version_name.RuntimeVersionName",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        recovery_window_in_days: Optional[int] = None,
    ) -> "capo_lambda_core.types.delete_runtime_version_response.DeleteRuntimeVersionResponse":
        """Schedules a runtime version to be deleted. Runtime versions scheduled for deletion enter the PENDING_DELETION state and can be restored during the scheduled deletion window. Function invokes fail for functions using a runtime version that is deleted or pending deletion.

        Args:
            runtime_name: The name or ARN of the runtime.
            name: The name of the runtime version to delete.
            recovery_window_in_days: Optional. The waiting period, in days (7-30), before the runtime version is permanently deleted.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a runtime version
            Schedules a runtime version to be deleted.

            >>> await client.delete_runtime_version(runtime_name='php8', name='v1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.delete_runtime_version_request.DeleteRuntimeVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.delete_runtime_version_response.DeleteRuntimeVersionResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_runtime_version

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.delete_runtime_version.async_delete_runtime_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteRuntimeVersion")
        )
        input_: capo_lambda_core.types.delete_runtime_version_request.DeleteRuntimeVersionRequest = {
            "runtime_name": runtime_name,
            "name": name,
        }
        if recovery_window_in_days is not None:
            input_["recovery_window_in_days"] = recovery_window_in_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_runtime_versions(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_lambda_core.types.list_runtime_versions_response.ListRuntimeVersionsResponse":
        """Returns a paginated list of versions for the specified runtime.

        Args:
            runtime_name: The name or ARN of the runtime whose versions to list.
            next_token: The pagination token from a previous response. Use it to retrieve the next page of results.
            max_results: The maximum number of runtime versions to return per page. Valid range: 1 to 100.

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List runtime versions
            Lists the versions published for a runtime.

            >>> await client.list_runtime_versions(runtime_name='php8', max_results=10)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.list_runtime_versions_request.ListRuntimeVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.list_runtime_versions_response.ListRuntimeVersionsResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_runtime_versions

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.list_runtime_versions.async_list_runtime_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListRuntimeVersions")
        )
        input_: capo_lambda_core.types.list_runtime_versions_request.ListRuntimeVersionsRequest = {
            "runtime_name": runtime_name
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

    async def iter_list_runtime_versions(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "AsyncIterator[capo_lambda_core.types.runtime_version_info.RuntimeVersionInfo]"
    ):
        _token = next_token
        while True:
            _response = await self.list_runtime_versions(
                runtime_name,
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

    async def create_network_connector(
        self,
        name: "capo_lambda_core.types.network_connector_name.NetworkConnectorName",
        configuration: "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        operator_role: Optional[
            "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
        ] = None,
        client_token: Optional[
            "capo_lambda_core.types.client_token_string.ClientTokenString"
        ] = None,
        tags: Optional[
            "capo_lambda_core.types.network_connector_tags.NetworkConnectorTags"
        ] = None,
    ) -> "capo_lambda_core.types.create_network_connector_response.CreateNetworkConnectorResponse":
        """<p>Creates a network connector that enables Lambda compute resources to route outbound traffic through your Amazon VPC. The network connector provisions elastic network interfaces (ENIs) in the subnets you specify, providing a managed network path to private resources such as databases, caches, and internal APIs.</p> <p>This operation is asynchronous. The network connector starts in <code>PENDING</code> state while ENIs are provisioned in your VPC (provisioning typically takes up to 10 minutes). Use <code>GetNetworkConnector</code> to poll the connector state until it reaches <code>ACTIVE</code>. Once active, you can attach the connector to supported Lambda compute resources — such as MicroVMs and WebFunctions — at run time. For how to attach a connector, see the documentation for the specific compute type.</p> <p>This operation is idempotent when you provide a <code>ClientToken</code> — if you retry a request that completed successfully using the same client token, the operation returns the existing connector without creating a duplicate.</p>

        Args:
            name: <p>A unique name for the network connector within your account and Region. You can use the name to identify the connector in subsequent API calls.</p>
            configuration: <p>The network configuration for the connector. Specify a <code>VpcEgressConfiguration</code> to enable outbound traffic routing through your VPC.</p>
            operator_role: <p>The ARN of the IAM role that Lambda assumes to manage elastic network interfaces in your VPC. This role must have permissions for <code>ec2:CreateNetworkInterface</code>, <code>ec2:DeleteNetworkInterface</code>, and related describe operations.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the API returns the existing connector without creating a duplicate.</p>
            tags: <p>A map of key-value pairs to associate with the network connector for organization, cost allocation, or access control.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.network_connector_limit_exceeded_exception.NetworkConnectorLimitExceededException: <p>The request would exceed a network connector limit. For <code>CreateNetworkConnector</code>, the account has reached the maximum number of network connectors allowed. For <code>UpdateNetworkConnector</code>, the connector has reached the maximum number of versions allowed.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.create_network_connector_request.CreateNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.create_network_connector_response.CreateNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.create_network_connector.async_create_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("CreateNetworkConnector")
        )
        input_: capo_lambda_core.types.create_network_connector_request.CreateNetworkConnectorRequest = {
            "name": name,
            "configuration": configuration,
        }
        if operator_role is not None:
            input_["operator_role"] = operator_role
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_network_connector(
        self,
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.get_network_connector_response.GetNetworkConnectorResponse":
        """<p>Retrieves the current configuration, state, and metadata of a network connector. The <code>Identifier</code> parameter accepts the connector ID, name, or full ARN. Use this operation to poll connector state after creation or update, or to inspect the current VPC configuration and any failure reasons.</p> <p>The response includes the full connector configuration, current state, and — if the connector has been updated — the <code>LastUpdateStatus</code> and <code>LastUpdateStatusReasonCode</code> fields that indicate whether the most recent update succeeded or failed.</p>

        Args:
            identifier: <p>The identifier of the network connector to retrieve. You can specify the connector ID, name, or ARN. Provide an unqualified ARN (or an ID or name) to retrieve the connector's latest version, or a version-qualified ARN — one that includes the immutable version suffix — to retrieve a specific historical version.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.get_network_connector_request.GetNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.get_network_connector_response.GetNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.get_network_connector.async_get_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("GetNetworkConnector")
        )
        input_: capo_lambda_core.types.get_network_connector_request.GetNetworkConnectorRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_network_connector(
        self,
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        configuration: Optional[
            "capo_lambda_core.types.network_connector_configuration.NetworkConnectorConfiguration"
        ] = None,
        operator_role: Optional[
            "capo_lambda_core.types.network_connector_role_arn.NetworkConnectorRoleArn"
        ] = None,
        client_token: Optional[
            "capo_lambda_core.types.client_token_string.ClientTokenString"
        ] = None,
    ) -> "capo_lambda_core.types.update_network_connector_response.UpdateNetworkConnectorResponse":
        """<p>Updates the VPC configuration or operator role of an existing network connector. You can modify the subnet IDs, security group IDs, network protocol, or operator role. The connector must be in <code>ACTIVE</code> state to accept updates.</p> <p>This operation is asynchronous. The connector remains in <code>ACTIVE</code> state during the update — existing workloads that reference this connector are not disrupted. Use <code>GetNetworkConnector</code> to monitor the <code>LastUpdateStatus</code> field, which transitions through <code>InProgress</code> to <code>Successful</code> or <code>Failed</code>. If the update fails, the <code>LastUpdateStatusReasonCode</code> field provides a specific error code for troubleshooting. This operation is idempotent when you provide a <code>ClientToken</code>.</p> <p>Each successful configuration change creates a new immutable version. A connector can have a limited number of versions; once that limit is reached, further updates fail with <code>NetworkConnectorLimitExceededException</code> until you delete older versions.</p>

        Args:
            identifier: <p>The identifier of the network connector to update. You can specify the connector ID, name, or full ARN.</p>
            configuration: <p>The updated network configuration for the connector. Provide the full <code>VpcEgressConfiguration</code> including all subnet IDs and security group IDs — this replaces the existing configuration.</p>
            operator_role: <p>The updated ARN of the IAM role that Lambda assumes to manage ENIs. Use this to change the operator role without recreating the connector.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the update request.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.network_connector_limit_exceeded_exception.NetworkConnectorLimitExceededException: <p>The request would exceed a network connector limit. For <code>CreateNetworkConnector</code>, the account has reached the maximum number of network connectors allowed. For <code>UpdateNetworkConnector</code>, the connector has reached the maximum number of versions allowed.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.update_network_connector_request.UpdateNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.update_network_connector_response.UpdateNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.update_network_connector.async_update_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("UpdateNetworkConnector")
        )
        input_: capo_lambda_core.types.update_network_connector_request.UpdateNetworkConnectorRequest = {
            "identifier": identifier
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if operator_role is not None:
            input_["operator_role"] = operator_role
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

    async def delete_network_connector(
        self,
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
    ) -> "capo_lambda_core.types.delete_network_connector_response.DeleteNetworkConnectorResponse":
        """<p>Initiates deletion of a network connector. The connector transitions to <code>DELETING</code> state while elastic network interfaces are cleaned up asynchronously. After deletion completes, subsequent calls to <code>GetNetworkConnector</code> return <code>ResourceNotFoundException</code>.</p> <p>This operation is idempotent — calling delete on a connector that is already deleting or has been deleted succeeds without error. You can delete connectors in <code>ACTIVE</code> or <code>FAILED</code> states. Before deleting a connector, ensure that no Lambda compute resources are using it, as they will lose VPC egress connectivity immediately.</p> <p>Deleting with an unqualified identifier removes the connector and all of its versions. To remove a single historical version, supply its version-qualified ARN; the connector and its remaining versions are unaffected. You can't delete the latest version on its own — delete the connector to remove it.</p>

        Args:
            identifier: <p>The identifier of the network connector to delete. Provide an unqualified ARN (or an ID or name) to delete the entire connector and all of its versions, or a version-qualified ARN — one that includes the immutable version suffix — to delete a specific historical version. You can't delete the latest version with a version-qualified identifier; delete the connector instead.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_conflict_exception.ResourceConflictException: <p>The request could not be completed due to a conflict with the current state of the resource. For example, attempting to modify a resource that is not in a state that permits the operation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.delete_network_connector_request.DeleteNetworkConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.delete_network_connector_response.DeleteNetworkConnectorResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_network_connector

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.delete_network_connector.async_delete_network_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("DeleteNetworkConnector")
        )
        input_: capo_lambda_core.types.delete_network_connector_request.DeleteNetworkConnectorRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_network_connectors(
        self,
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        state: Optional[
            "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
        ] = None,
        marker: Optional[
            "capo_lambda_core.types.aws_gir_api_string.AwsGirApiString"
        ] = None,
        max_items: Optional[
            "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
        ] = None,
    ) -> "capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse":
        """<p>Returns a paginated list of network connectors in your account for the current Region. You can optionally filter results by connector state. Use the <code>Marker</code> parameter from a previous response to retrieve the next page of results.</p> <p>Each item in the response includes the connector ARN, name, ID, type, current state, and last modified timestamp. To retrieve full configuration details for a specific connector, use <code>GetNetworkConnector</code>.</p>

        Args:
            state: <p>Optional filter to return only connectors in the specified state (for example, <code>ACTIVE</code> or <code>FAILED</code>).</p>
            marker: <p>The pagination token from a previous <code>ListNetworkConnectors</code> response. Use this value to retrieve the next page of results.</p>
            max_items: <p>The maximum number of connectors to return per page. Valid range: 1 to 100.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.list_network_connectors_response.ListNetworkConnectorsResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_network_connectors

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.list_network_connectors.async_list_network_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListNetworkConnectors")
        )
        input_: capo_lambda_core.types.list_network_connectors_request.ListNetworkConnectorsRequest = {}
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_network_connectors(
        self,
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        state: Optional[
            "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
        ] = None,
        marker: Optional[
            "capo_lambda_core.types.aws_gir_api_string.AwsGirApiString"
        ] = None,
        max_items: Optional[
            "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
        ] = None,
    ) -> "AsyncIterator[capo_lambda_core.types.network_connector_summary.NetworkConnectorSummary]":
        _token = marker
        while True:
            _response = await self.list_network_connectors(
                config_overrides=config_overrides,
                state=state,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("network_connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def list_network_connector_versions(
        self,
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        state: Optional[
            "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
        ] = None,
        marker: Optional[
            "capo_lambda_core.types.aws_gir_api_string.AwsGirApiString"
        ] = None,
        max_items: Optional[
            "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
        ] = None,
    ) -> "capo_lambda_core.types.list_network_connector_versions_response.ListNetworkConnectorVersionsResponse":
        """<p>Returns a paginated list of the versions of a network connector. Each configuration update creates a new immutable version; this operation lists those versions for the connector you specify. You can optionally filter results by version state. Use the <code>Marker</code> parameter from a previous response to retrieve the next page of results.</p> <p>Each item in the response includes the version-qualified ARN, version number, current state, and last modified timestamp for that version. To retrieve the current (latest) configuration of the connector, use <code>GetNetworkConnector</code>; to inspect a specific version, call <code>GetNetworkConnector</code> with a version-qualified identifier.</p>

        Args:
            identifier: <p>The identifier of the network connector whose versions you want to list. You can specify the connector ID, name, or full ARN. Specify an unqualified identifier — this operation lists all versions of the connector, not a specific version.</p>
            state: <p>Optional filter to return only versions in the specified state (for example, <code>ACTIVE</code> or <code>FAILED</code>).</p>
            marker: <p>The pagination token from a previous <code>ListNetworkConnectorVersions</code> response. Use this value to retrieve the next page of results.</p>
            max_items: <p>The maximum number of versions to return per page. Valid range: 1 to 100.</p>

        Raises:
            capo_lambda_core.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid. Check the error message for details about which parameter failed validation.</p>
            capo_lambda_core.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist. Verify the identifier and Region.</p>
            capo_lambda_core.errors.service_exception.ServiceException: <p>An internal service error occurred. Retry the request with exponential backoff.</p>
            capo_lambda_core.errors.too_many_requests_exception.TooManyRequestsException: <p>The request was throttled due to exceeding the allowed request rate. Retry the request after a brief wait using exponential backoff.</p>
            capo_lambda_core.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_core.types.list_network_connector_versions_request.ListNetworkConnectorVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_core.types.list_network_connector_versions_response.ListNetworkConnectorVersionsResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_network_connector_versions

            (
                output,
                http_response,
            ) = await capo_lambda_core._operations.lambda_core_api_service.list_network_connector_versions.async_list_network_connector_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(
            config_overrides, OperationLogging("ListNetworkConnectorVersions")
        )
        input_: capo_lambda_core.types.list_network_connector_versions_request.ListNetworkConnectorVersionsRequest = {
            "identifier": identifier
        }
        if state is not None:
            input_["state"] = state
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_network_connector_versions(
        self,
        identifier: "capo_lambda_core.types.network_connector_identifier.NetworkConnectorIdentifier",
        *,
        config_overrides: Optional[AsyncLambdaCoreClientConfig] = None,
        state: Optional[
            "capo_lambda_core.types.network_connector_state.NetworkConnectorState"
        ] = None,
        marker: Optional[
            "capo_lambda_core.types.aws_gir_api_string.AwsGirApiString"
        ] = None,
        max_items: Optional[
            "capo_lambda_core.types.max_hundred_list_items.MaxHundredListItems"
        ] = None,
    ) -> "AsyncIterator[capo_lambda_core.types.network_connector_version_summary.NetworkConnectorVersionSummary]":
        _token = marker
        while True:
            _response = await self.list_network_connector_versions(
                identifier,
                config_overrides=config_overrides,
                state=state,
                marker=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("network_connector_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_marker",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
