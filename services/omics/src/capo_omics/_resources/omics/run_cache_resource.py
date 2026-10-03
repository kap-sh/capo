from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.aws_account_id
    import capo_omics.types.cache_behavior
    import capo_omics.types.create_run_cache_request
    import capo_omics.types.create_run_cache_response
    import capo_omics.types.delete_run_cache_request
    import capo_omics.types.get_run_cache_request
    import capo_omics.types.get_run_cache_response
    import capo_omics.types.list_run_caches_request
    import capo_omics.types.list_run_caches_response
    import capo_omics.types.list_token
    import capo_omics.types.run_cache_id
    import capo_omics.types.run_cache_list_item
    import capo_omics.types.run_cache_request_id
    import capo_omics.types.s3_uri_for_bucket_or_object
    import capo_omics.types.tag_map
    import capo_omics.types.update_run_cache_request
    import capo_omics.types.user_custom_description
    import capo_omics.types.user_custom_name
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class RunCacheResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        cache_s3_location: "capo_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject",
        request_id: "capo_omics.types.run_cache_request_id.RunCacheRequestId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        description: Optional[
            "capo_omics.types.user_custom_description.UserCustomDescription"
        ] = None,
        name: Optional["capo_omics.types.user_custom_name.UserCustomName"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        cache_bucket_owner_id: Optional[
            "capo_omics.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "capo_omics.types.create_run_cache_response.CreateRunCacheResponse":
        """<p>Creates a run cache to store and reference task outputs from completed private runs. Specify an Amazon S3 location where Amazon Web Services HealthOmics saves the cached data. This data must be immediately accessible and not in an archived state. You can save intermediate task files to a run cache if they are declared as task outputs in the workflow definition file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html">Call caching</a> and <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-create.html">Creating a run cache</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            cache_behavior: <p>Default cache behavior for runs that use this cache. Supported values are:</p> <p> <code>CACHE_ON_FAILURE</code>: Caches task outputs from completed tasks for runs that fail. This setting is useful if you're debugging a workflow that fails after several tasks completed successfully. The subsequent run uses the cache outputs for previously-completed tasks if the task definition, inputs, and container in ECR are identical to the prior run.</p> <p> <code>CACHE_ALWAYS</code>: Caches task outputs from completed tasks for all runs. This setting is useful in development mode, but do not use it in a production setting.</p> <p>If you don't specify a value, the default behavior is CACHE_ON_FAILURE. When you start a run that uses this cache, you can override the default cache behavior.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            cache_s3_location: <p>Specify the S3 location for storing the cached task outputs. This data must be immediately accessible (not in an archived state).</p>
            description: <p>Enter a description of the run cache.</p>
            name: <p>Enter a user-friendly name for the run cache.</p>
            request_id: <p>A unique request token, to ensure idempotency. If you don't specify a token, Amazon Web Services HealthOmics automatically generates a universally unique identifier (UUID) for the request.</p>
            tags: <p>Specify one or more tags to associate with this run cache.</p>
            cache_bucket_owner_id: <p>The Amazon Web Services account ID of the expected owner of the S3 bucket for the run cache. If not provided, your account ID is set as the owner of the bucket.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_run_cache_request.CreateRunCacheRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_run_cache_response.CreateRunCacheResponse"
        ]:
            import capo_omics._operations.omics.create_run_cache

            output, http_response = (
                capo_omics._operations.omics.create_run_cache.create_run_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_run_cache_request.CreateRunCacheRequest = {
            "cache_s3_location": cache_s3_location,
            "request_id": request_id,
        }
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if cache_bucket_owner_id is not None:
            input_["cache_bucket_owner_id"] = cache_bucket_owner_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_cache_response.GetRunCacheResponse":
        """<p>Retrieves detailed information about the specified run cache using its ID.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html">Call caching for Amazon Web Services HealthOmics runs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The identifier of the run cache to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_run_cache_request.GetRunCacheRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_run_cache_response.GetRunCacheResponse"
        ]:
            import capo_omics._operations.omics.get_run_cache

            output, http_response = (
                capo_omics._operations.omics.get_run_cache.get_run_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_run_cache_request.GetRunCacheRequest = {"id": id}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        description: Optional[
            "capo_omics.types.user_custom_description.UserCustomDescription"
        ] = None,
        name: Optional["capo_omics.types.user_custom_name.UserCustomName"] = None,
    ) -> None:
        """<p>Updates a run cache using its ID and returns a response with no body if the operation is successful. You can update the run cache description, name, or the default run cache behavior with <code>CACHE_ON_FAILURE</code> or <code>CACHE_ALWAYS</code>. To confirm that your run cache settings have been properly updated, use the <code>GetRunCache</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html">How call caching works</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            cache_behavior: <p>Update the default run cache behavior.</p>
            description: <p>Update the run cache description.</p>
            id: <p>The identifier of the run cache you want to update.</p>
            name: <p>Update the name of the run cache.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.update_run_cache_request.UpdateRunCacheRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.update_run_cache

            output, http_response = (
                capo_omics._operations.omics.update_run_cache.update_run_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_run_cache_request.UpdateRunCacheRequest = {
            "id": id
        }
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run cache and returns a response with no body if the operation is successful. This action removes the cache metadata stored in the service account, but does not delete the data in Amazon S3. You can access the cache data in Amazon S3, for inspection or to troubleshoot issues. You can remove old cache data using standard S3 <code>Delete</code> operations. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-delete.html">Deleting a run cache</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>Run cache identifier for the cache you want to delete.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_run_cache_request.DeleteRunCacheRequest]",
        ) -> OperationResponse[None]:
            import capo_omics._operations.omics.delete_run_cache

            output, http_response = (
                capo_omics._operations.omics.delete_run_cache.delete_run_cache(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_cache_request.DeleteRunCacheRequest = {
            "id": id
        }

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
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
    ) -> "capo_omics.types.list_run_caches_response.ListRunCachesResponse":
        """<p>Retrieves a list of your run caches and the metadata for each cache.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            starting_token: <p>Optional pagination token returned from a prior call to the <code>ListRunCaches</code> API operation.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_run_caches_request.ListRunCachesRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_run_caches_response.ListRunCachesResponse"
        ]:
            import capo_omics._operations.omics.list_run_caches

            output, http_response = (
                capo_omics._operations.omics.list_run_caches.list_run_caches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_run_caches_request.ListRunCachesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_token is not None:
            input_["starting_token"] = starting_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRunCacheResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        cache_s3_location: "capo_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject",
        request_id: "capo_omics.types.run_cache_request_id.RunCacheRequestId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        description: Optional[
            "capo_omics.types.user_custom_description.UserCustomDescription"
        ] = None,
        name: Optional["capo_omics.types.user_custom_name.UserCustomName"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        cache_bucket_owner_id: Optional[
            "capo_omics.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "capo_omics.types.create_run_cache_response.CreateRunCacheResponse":
        """<p>Creates a run cache to store and reference task outputs from completed private runs. Specify an Amazon S3 location where Amazon Web Services HealthOmics saves the cached data. This data must be immediately accessible and not in an archived state. You can save intermediate task files to a run cache if they are declared as task outputs in the workflow definition file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html">Call caching</a> and <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-create.html">Creating a run cache</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            cache_behavior: <p>Default cache behavior for runs that use this cache. Supported values are:</p> <p> <code>CACHE_ON_FAILURE</code>: Caches task outputs from completed tasks for runs that fail. This setting is useful if you're debugging a workflow that fails after several tasks completed successfully. The subsequent run uses the cache outputs for previously-completed tasks if the task definition, inputs, and container in ECR are identical to the prior run.</p> <p> <code>CACHE_ALWAYS</code>: Caches task outputs from completed tasks for all runs. This setting is useful in development mode, but do not use it in a production setting.</p> <p>If you don't specify a value, the default behavior is CACHE_ON_FAILURE. When you start a run that uses this cache, you can override the default cache behavior.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior">Run cache behavior</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            cache_s3_location: <p>Specify the S3 location for storing the cached task outputs. This data must be immediately accessible (not in an archived state).</p>
            description: <p>Enter a description of the run cache.</p>
            name: <p>Enter a user-friendly name for the run cache.</p>
            request_id: <p>A unique request token, to ensure idempotency. If you don't specify a token, Amazon Web Services HealthOmics automatically generates a universally unique identifier (UUID) for the request.</p>
            tags: <p>Specify one or more tags to associate with this run cache.</p>
            cache_bucket_owner_id: <p>The Amazon Web Services account ID of the expected owner of the S3 bucket for the run cache. If not provided, your account ID is set as the owner of the bucket.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_run_cache_request.CreateRunCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_run_cache_response.CreateRunCacheResponse"
        ]:
            import capo_omics._operations.omics.create_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_run_cache.async_create_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_run_cache_request.CreateRunCacheRequest = {
            "cache_s3_location": cache_s3_location,
            "request_id": request_id,
        }
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if cache_bucket_owner_id is not None:
            input_["cache_bucket_owner_id"] = cache_bucket_owner_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_run_cache_response.GetRunCacheResponse":
        """<p>Retrieves detailed information about the specified run cache using its ID.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-call-caching.html">Call caching for Amazon Web Services HealthOmics runs</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The identifier of the run cache to retrieve.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_run_cache_request.GetRunCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_run_cache_response.GetRunCacheResponse"
        ]:
            import capo_omics._operations.omics.get_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_run_cache.async_get_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_run_cache_request.GetRunCacheRequest = {"id": id}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        cache_behavior: Optional[
            "capo_omics.types.cache_behavior.CacheBehavior"
        ] = None,
        description: Optional[
            "capo_omics.types.user_custom_description.UserCustomDescription"
        ] = None,
        name: Optional["capo_omics.types.user_custom_name.UserCustomName"] = None,
    ) -> None:
        """<p>Updates a run cache using its ID and returns a response with no body if the operation is successful. You can update the run cache description, name, or the default run cache behavior with <code>CACHE_ON_FAILURE</code> or <code>CACHE_ALWAYS</code>. To confirm that your run cache settings have been properly updated, use the <code>GetRunCache</code> API operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html">How call caching works</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            cache_behavior: <p>Update the default run cache behavior.</p>
            description: <p>Update the run cache description.</p>
            id: <p>The identifier of the run cache you want to update.</p>
            name: <p>Update the name of the run cache.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.update_run_cache_request.UpdateRunCacheRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.update_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_run_cache.async_update_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_run_cache_request.UpdateRunCacheRequest = {
            "id": id
        }
        if cache_behavior is not None:
            input_["cache_behavior"] = cache_behavior
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_omics.types.run_cache_id.RunCacheId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> None:
        """<p>Deletes a run cache and returns a response with no body if the operation is successful. This action removes the cache metadata stored in the service account, but does not delete the data in Amazon S3. You can access the cache data in Amazon S3, for inspection or to troubleshoot issues. You can remove old cache data using standard S3 <code>Delete</code> operations. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-delete.html">Deleting a run cache</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>Run cache identifier for the cache you want to delete.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_run_cache_request.DeleteRunCacheRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_omics._operations.omics.delete_run_cache

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_run_cache.async_delete_run_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_run_cache_request.DeleteRunCacheRequest = {
            "id": id
        }

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
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        starting_token: Optional["capo_omics.types.list_token.ListToken"] = None,
    ) -> "capo_omics.types.list_run_caches_response.ListRunCachesResponse":
        """<p>Retrieves a list of your run caches and the metadata for each cache.</p>

        Args:
            max_results: <p>The maximum number of results to return.</p>
            starting_token: <p>Optional pagination token returned from a prior call to the <code>ListRunCaches</code> API operation.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_run_caches_request.ListRunCachesRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_run_caches_response.ListRunCachesResponse"
        ]:
            import capo_omics._operations.omics.list_run_caches

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_run_caches.async_list_run_caches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_run_caches_request.ListRunCachesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if starting_token is not None:
            input_["starting_token"] = starting_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
