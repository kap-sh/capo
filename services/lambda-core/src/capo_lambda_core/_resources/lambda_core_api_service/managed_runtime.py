from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda_core._auth._signers
import capo_lambda_core._auth._sigv4
from capo_lambda_core._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda_core.types.create_runtime_request
    import capo_lambda_core.types.create_runtime_response
    import capo_lambda_core.types.delete_runtime_request
    import capo_lambda_core.types.delete_runtime_response
    import capo_lambda_core.types.get_runtime_request
    import capo_lambda_core.types.get_runtime_response
    import capo_lambda_core.types.list_runtimes_request
    import capo_lambda_core.types.list_runtimes_response
    import capo_lambda_core.types.restore_runtime_request
    import capo_lambda_core.types.restore_runtime_response
    import capo_lambda_core.types.runtime_alias_name
    import capo_lambda_core.types.runtime_description
    import capo_lambda_core.types.runtime_identifier
    import capo_lambda_core.types.runtime_info
    import capo_lambda_core.types.runtime_license_info
    import capo_lambda_core.types.runtime_name
    import capo_lambda_core.types.runtime_release_lifecycle
    import capo_lambda_core.types.runtime_version_name
    import capo_lambda_core.types.tag_map
    import capo_lambda_core.types.update_runtime_request
    import capo_lambda_core.types.update_runtime_response
    from capo_lambda_core._services.async_lambda_core import (
        AsyncLambdaCoreClient,
        AsyncLambdaCoreClientConfig,
    )
    from capo_lambda_core._services.lambda_core import (
        LambdaCoreClient,
        LambdaCoreClientConfig,
    )


class ManagedRuntime:
    def __init__(self, service: LambdaCoreClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_lambda_core.types.runtime_name.RuntimeName",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
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

            >>> client.create(name='php8', description='PHP 8 custom runtime', license_info='MIT', tags={'team': 'runtimes'})
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.create_runtime_request.CreateRuntimeRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.create_runtime_response.CreateRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.create_runtime

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.create_runtime.create_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
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

            >>> client.read(runtime_name='php8')
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.get_runtime_request.GetRuntimeRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.get_runtime_response.GetRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.get_runtime

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.get_runtime.get_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetRuntime")
        )
        input_: capo_lambda_core.types.get_runtime_request.GetRuntimeRequest = {
            "runtime_name": runtime_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
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

            >>> client.update(runtime_name='php8', description='PHP 8 custom runtime (updated)', release_lifecycle={'ReleaseState': 'GA'})
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.update_runtime_request.UpdateRuntimeRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.update_runtime_response.UpdateRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.update_runtime

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.update_runtime.update_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
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

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
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

            >>> client.delete(runtime_name='php8')
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.delete_runtime_request.DeleteRuntimeRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.delete_runtime_response.DeleteRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.delete_runtime

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.delete_runtime.delete_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteRuntime")
        )
        input_: capo_lambda_core.types.delete_runtime_request.DeleteRuntimeRequest = {
            "runtime_name": runtime_name
        }
        if recovery_window_in_days is not None:
            input_["recovery_window_in_days"] = recovery_window_in_days

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
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

            >>> client.list(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.list_runtimes_request.ListRuntimesRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.list_runtimes_response.ListRuntimesResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.list_runtimes

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.list_runtimes.list_runtimes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListRuntimes")
        )
        input_: capo_lambda_core.types.list_runtimes_request.ListRuntimesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_runtime(
        self,
        runtime_name: "capo_lambda_core.types.runtime_identifier.RuntimeIdentifier",
        *,
        config_overrides: Optional[LambdaCoreClientConfig] = None,
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

            >>> client.restore_runtime(runtime_name='php8', runtime_alias='release')
            Restore a customer-managed runtime that is scheduled for deletion
            Cancels a pending deletion for the runtime, returning it to ACTIVE.

            >>> client.restore_runtime(runtime_name='php8')
        """

        def _handler(
            req: "OperationRequest[capo_lambda_core.types.restore_runtime_request.RestoreRuntimeRequest]",
        ) -> OperationResponse[
            "capo_lambda_core.types.restore_runtime_response.RestoreRuntimeResponse"
        ]:
            import capo_lambda_core._operations.lambda_core_api_service.restore_runtime

            output, http_response = (
                capo_lambda_core._operations.lambda_core_api_service.restore_runtime.restore_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("RestoreRuntime")
        )
        input_: capo_lambda_core.types.restore_runtime_request.RestoreRuntimeRequest = {
            "runtime_name": runtime_name
        }
        if runtime_version is not None:
            input_["runtime_version"] = runtime_version
        if runtime_alias is not None:
            input_["runtime_alias"] = runtime_alias

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedRuntime:
    def __init__(self, service: AsyncLambdaCoreClient) -> None:
        self._service = service

    async def create(
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

            >>> await client.create(name='php8', description='PHP 8 custom runtime', license_info='MIT', tags={'team': 'runtimes'})
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

        interceptors_, options_ = self._service.operation_options(
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

    async def read(
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

            >>> await client.read(runtime_name='php8')
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

        interceptors_, options_ = self._service.operation_options(
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

    async def update(
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

            >>> await client.update(runtime_name='php8', description='PHP 8 custom runtime (updated)', release_lifecycle={'ReleaseState': 'GA'})
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

        interceptors_, options_ = self._service.operation_options(
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

    async def delete(
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

            >>> await client.delete(runtime_name='php8')
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

        interceptors_, options_ = self._service.operation_options(
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

    async def list(
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

            >>> await client.list(max_results=10)
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

        interceptors_, options_ = self._service.operation_options(
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

        interceptors_, options_ = self._service.operation_options(
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
