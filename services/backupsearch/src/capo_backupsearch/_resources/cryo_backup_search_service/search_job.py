from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_backupsearch._auth._signers
import capo_backupsearch._auth._sigv4
from capo_backupsearch._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_backupsearch.types.encryption_key_arn
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.get_search_job_input
    import capo_backupsearch.types.get_search_job_output
    import capo_backupsearch.types.item_filters
    import capo_backupsearch.types.list_search_jobs_input
    import capo_backupsearch.types.list_search_jobs_output
    import capo_backupsearch.types.search_job_state
    import capo_backupsearch.types.search_scope
    import capo_backupsearch.types.start_search_job_input
    import capo_backupsearch.types.start_search_job_output
    import capo_backupsearch.types.stop_search_job_input
    import capo_backupsearch.types.stop_search_job_output
    import capo_backupsearch.types.tag_map
    from capo_backupsearch._services.async_backup_search import (
        AsyncBackupSearchClient,
        AsyncBackupSearchClientConfig,
    )
    from capo_backupsearch._services.backup_search import (
        BackupSearchClient,
        BackupSearchClientConfig,
    )


class SearchJob:
    def __init__(self, service: BackupSearchClient) -> None:
        self._service = service

    def create(
        self,
        search_scope: "capo_backupsearch.types.search_scope.SearchScope",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        tags: Optional["capo_backupsearch.types.tag_map.TagMap"] = None,
        name: Optional[str] = None,
        encryption_key_arn: Optional[
            "capo_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        item_filters: Optional[
            "capo_backupsearch.types.item_filters.ItemFilters"
        ] = None,
    ) -> "capo_backupsearch.types.start_search_job_output.StartSearchJobOutput":
        """<p>This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.</p> <p>You can optionally include ClientToken, EncryptionKeyArn, Name, and/or Tags.</p>

        Args:
            tags: <p>List of tags returned by the operation.</p>
            name: <p>Include alphanumeric characters to create a name for this search job.</p>
            encryption_key_arn: <p>The encryption key for the specified search job.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            search_scope: <p>This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.</p>
            item_filters: <p>Item Filters represent all input item properties specified when the search was created.</p> <p>Contains either EBSItemFilters or S3ItemFilters</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backupsearch.types.start_search_job_input.StartSearchJobInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.start_search_job_output.StartSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.start_search_job

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.start_search_job.start_search_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartSearchJob")
        )
        input_: capo_backupsearch.types.start_search_job_input.StartSearchJobInput = {
            "search_scope": search_scope
        }
        if tags is not None:
            input_["tags"] = tags
        if name is not None:
            input_["name"] = name
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if item_filters is not None:
            input_["item_filters"] = item_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.get_search_job_output.GetSearchJobOutput":
        """<p>This operation retrieves metadata of a search job, including its progress.</p>

        Args:
            search_job_identifier: <p>Required unique string that specifies the search job.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backupsearch.types.get_search_job_input.GetSearchJobInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.get_search_job_output.GetSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.get_search_job

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.get_search_job.get_search_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSearchJob")
        )
        input_: capo_backupsearch.types.get_search_job_input.GetSearchJobInput = {
            "search_job_identifier": search_job_identifier
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
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.stop_search_job_output.StopSearchJobOutput":
        """<p>This operations ends a search job.</p> <p>Only a search job with a status of <code>RUNNING</code> can be stopped.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backupsearch.types.stop_search_job_input.StopSearchJobInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.stop_search_job_output.StopSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.stop_search_job

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.stop_search_job.stop_search_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopSearchJob")
        )
        input_: capo_backupsearch.types.stop_search_job_input.StopSearchJobInput = {
            "search_job_identifier": search_job_identifier
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
        config_overrides: Optional[BackupSearchClientConfig] = None,
        by_status: Optional[
            "capo_backupsearch.types.search_job_state.SearchJobState"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput":
        """<p>This operation returns a list of search jobs belonging to an account.</p>

        Args:
            by_status: <p>Include this parameter to filter list by search job status.</p>
            next_token: <p>The next item following a partial list of returned search jobs.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backupsearch.types.list_search_jobs_input.ListSearchJobsInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_jobs

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.list_search_jobs.list_search_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSearchJobs")
        )
        input_: capo_backupsearch.types.list_search_jobs_input.ListSearchJobsInput = {}
        if by_status is not None:
            input_["by_status"] = by_status
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


class AsyncSearchJob:
    def __init__(self, service: AsyncBackupSearchClient) -> None:
        self._service = service

    async def create(
        self,
        search_scope: "capo_backupsearch.types.search_scope.SearchScope",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        tags: Optional["capo_backupsearch.types.tag_map.TagMap"] = None,
        name: Optional[str] = None,
        encryption_key_arn: Optional[
            "capo_backupsearch.types.encryption_key_arn.EncryptionKeyArn"
        ] = None,
        client_token: Optional[str] = None,
        item_filters: Optional[
            "capo_backupsearch.types.item_filters.ItemFilters"
        ] = None,
    ) -> "capo_backupsearch.types.start_search_job_output.StartSearchJobOutput":
        """<p>This operation creates a search job which returns recovery points filtered by SearchScope and items filtered by ItemFilters.</p> <p>You can optionally include ClientToken, EncryptionKeyArn, Name, and/or Tags.</p>

        Args:
            tags: <p>List of tags returned by the operation.</p>
            name: <p>Include alphanumeric characters to create a name for this search job.</p>
            encryption_key_arn: <p>The encryption key for the specified search job.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            search_scope: <p>This object can contain BackupResourceTypes, BackupResourceArns, BackupResourceCreationTime, BackupResourceTags, and SourceResourceArns to filter the recovery points returned by the search job.</p>
            item_filters: <p>Item Filters represent all input item properties specified when the search was created.</p> <p>Contains either EBSItemFilters or S3ItemFilters</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.start_search_job_input.StartSearchJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.start_search_job_output.StartSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.start_search_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.start_search_job.async_start_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartSearchJob")
        )
        input_: capo_backupsearch.types.start_search_job_input.StartSearchJobInput = {
            "search_scope": search_scope
        }
        if tags is not None:
            input_["tags"] = tags
        if name is not None:
            input_["name"] = name
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if client_token is not None:
            input_["client_token"] = client_token
        if item_filters is not None:
            input_["item_filters"] = item_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.get_search_job_output.GetSearchJobOutput":
        """<p>This operation retrieves metadata of a search job, including its progress.</p>

        Args:
            search_job_identifier: <p>Required unique string that specifies the search job.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.get_search_job_input.GetSearchJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.get_search_job_output.GetSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.get_search_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.get_search_job.async_get_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSearchJob")
        )
        input_: capo_backupsearch.types.get_search_job_input.GetSearchJobInput = {
            "search_job_identifier": search_job_identifier
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
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.stop_search_job_output.StopSearchJobOutput":
        """<p>This operations ends a search job.</p> <p>Only a search job with a status of <code>RUNNING</code> can be stopped.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.conflict_exception.ConflictException: <p>This exception occurs when a conflict with a previous successful operation is detected. This generally occurs when the previous operation did not have time to propagate to the host serving the current request.</p> <p>A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.stop_search_job_input.StopSearchJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.stop_search_job_output.StopSearchJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.stop_search_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.stop_search_job.async_stop_search_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopSearchJob")
        )
        input_: capo_backupsearch.types.stop_search_job_input.StopSearchJobInput = {
            "search_job_identifier": search_job_identifier
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
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        by_status: Optional[
            "capo_backupsearch.types.search_job_state.SearchJobState"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput":
        """<p>This operation returns a list of search jobs belonging to an account.</p>

        Args:
            by_status: <p>Include this parameter to filter list by search job status.</p>
            next_token: <p>The next item following a partial list of returned search jobs.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_jobs_input.ListSearchJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_jobs_output.ListSearchJobsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_jobs

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_jobs.async_list_search_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSearchJobs")
        )
        input_: capo_backupsearch.types.list_search_jobs_input.ListSearchJobsInput = {}
        if by_status is not None:
            input_["by_status"] = by_status
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
