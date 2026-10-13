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
    import capo_backupsearch.types.export_job_status
    import capo_backupsearch.types.export_specification
    import capo_backupsearch.types.generic_id
    import capo_backupsearch.types.get_search_result_export_job_input
    import capo_backupsearch.types.get_search_result_export_job_output
    import capo_backupsearch.types.iam_role_arn
    import capo_backupsearch.types.list_search_result_export_jobs_input
    import capo_backupsearch.types.list_search_result_export_jobs_output
    import capo_backupsearch.types.start_search_result_export_job_input
    import capo_backupsearch.types.start_search_result_export_job_output
    import capo_backupsearch.types.tag_map
    from capo_backupsearch._services.async_backup_search import (
        AsyncBackupSearchClient,
        AsyncBackupSearchClientConfig,
    )
    from capo_backupsearch._services.backup_search import (
        BackupSearchClient,
        BackupSearchClientConfig,
    )


class SearchResultExportJob:
    def __init__(self, service: BackupSearchClient) -> None:
        self._service = service

    def create(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        export_specification: "capo_backupsearch.types.export_specification.ExportSpecification",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_backupsearch.types.tag_map.TagMap"] = None,
        role_arn: Optional["capo_backupsearch.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_backupsearch.types.start_search_result_export_job_output.StartSearchResultExportJobOutput":
        """<p>This operations starts a job to export the results of search job to a designated S3 bucket.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            export_specification: <p>This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            tags: <p>Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>
            role_arn: <p>This parameter specifies the role ARN used to start the search results export jobs.</p>

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
            req: "OperationRequest[capo_backupsearch.types.start_search_result_export_job_input.StartSearchResultExportJobInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.start_search_result_export_job_output.StartSearchResultExportJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.start_search_result_export_job

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.start_search_result_export_job.start_search_result_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartSearchResultExportJob")
        )
        input_: capo_backupsearch.types.start_search_result_export_job_input.StartSearchResultExportJobInput = {
            "search_job_identifier": search_job_identifier,
            "export_specification": export_specification,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        export_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[BackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.get_search_result_export_job_output.GetSearchResultExportJobOutput":
        """<p>This operation retrieves the metadata of an export job.</p> <p>An export job is an operation that transmits the results of a search job to a specified S3 bucket in a .csv file.</p> <p>An export job allows you to retain results of a search beyond the search job's scheduled retention of 7 days.</p>

        Args:
            export_job_identifier: <p>This is the unique string that identifies a specific export job.</p> <p>Required for this operation.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backupsearch.types.get_search_result_export_job_input.GetSearchResultExportJobInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.get_search_result_export_job_output.GetSearchResultExportJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.get_search_result_export_job

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.get_search_result_export_job.get_search_result_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSearchResultExportJob")
        )
        input_: capo_backupsearch.types.get_search_result_export_job_input.GetSearchResultExportJobInput = {
            "export_job_identifier": export_job_identifier
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
        status: Optional[
            "capo_backupsearch.types.export_job_status.ExportJobStatus"
        ] = None,
        search_job_identifier: Optional[
            "capo_backupsearch.types.generic_id.GenericId"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_result_export_jobs_output.ListSearchResultExportJobsOutput":
        """<p>This operation exports search results of a search job to a specified destination S3 bucket.</p>

        Args:
            status: <p>The search jobs to be included in the export job can be filtered by including this parameter.</p>
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backupsearch.types.list_search_result_export_jobs_input.ListSearchResultExportJobsInput]",
        ) -> OperationResponse[
            "capo_backupsearch.types.list_search_result_export_jobs_output.ListSearchResultExportJobsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_result_export_jobs

            output, http_response = (
                capo_backupsearch._operations.cryo_backup_search_service.list_search_result_export_jobs.list_search_result_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSearchResultExportJobs")
        )
        input_: capo_backupsearch.types.list_search_result_export_jobs_input.ListSearchResultExportJobsInput = {}
        if status is not None:
            input_["status"] = status
        if search_job_identifier is not None:
            input_["search_job_identifier"] = search_job_identifier
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


class AsyncSearchResultExportJob:
    def __init__(self, service: AsyncBackupSearchClient) -> None:
        self._service = service

    async def create(
        self,
        search_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        export_specification: "capo_backupsearch.types.export_specification.ExportSpecification",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_backupsearch.types.tag_map.TagMap"] = None,
        role_arn: Optional["capo_backupsearch.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_backupsearch.types.start_search_result_export_job_output.StartSearchResultExportJobOutput":
        """<p>This operations starts a job to export the results of search job to a designated S3 bucket.</p>

        Args:
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            export_specification: <p>This specification contains a required string of the destination bucket; optionally, you can include the destination prefix.</p>
            client_token: <p>Include this parameter to allow multiple identical calls for idempotency.</p> <p>A client token is valid for 8 hours after the first request that uses it is completed. After this time, any request with the same token is treated as a new request.</p>
            tags: <p>Optional tags to include. A tag is a key-value pair you can use to manage, filter, and search for your resources. Allowed characters include UTF-8 letters, numbers, spaces, and the following characters: + - = . _ : /. </p>
            role_arn: <p>This parameter specifies the role ARN used to start the search results export jobs.</p>

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
            req: "AsyncOperationRequest[capo_backupsearch.types.start_search_result_export_job_input.StartSearchResultExportJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.start_search_result_export_job_output.StartSearchResultExportJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.start_search_result_export_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.start_search_result_export_job.async_start_search_result_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartSearchResultExportJob")
        )
        input_: capo_backupsearch.types.start_search_result_export_job_input.StartSearchResultExportJobInput = {
            "search_job_identifier": search_job_identifier,
            "export_specification": export_specification,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        export_job_identifier: "capo_backupsearch.types.generic_id.GenericId",
        *,
        config_overrides: Optional[AsyncBackupSearchClientConfig] = None,
    ) -> "capo_backupsearch.types.get_search_result_export_job_output.GetSearchResultExportJobOutput":
        """<p>This operation retrieves the metadata of an export job.</p> <p>An export job is an operation that transmits the results of a search job to a specified S3 bucket in a .csv file.</p> <p>An export job allows you to retain results of a search beyond the search job's scheduled retention of 7 days.</p>

        Args:
            export_job_identifier: <p>This is the unique string that identifies a specific export job.</p> <p>Required for this operation.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.get_search_result_export_job_input.GetSearchResultExportJobInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.get_search_result_export_job_output.GetSearchResultExportJobOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.get_search_result_export_job

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.get_search_result_export_job.async_get_search_result_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetSearchResultExportJob")
        )
        input_: capo_backupsearch.types.get_search_result_export_job_input.GetSearchResultExportJobInput = {
            "export_job_identifier": export_job_identifier
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
        status: Optional[
            "capo_backupsearch.types.export_job_status.ExportJobStatus"
        ] = None,
        search_job_identifier: Optional[
            "capo_backupsearch.types.generic_id.GenericId"
        ] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_backupsearch.types.list_search_result_export_jobs_output.ListSearchResultExportJobsOutput":
        """<p>This operation exports search results of a search job to a specified destination S3 bucket.</p>

        Args:
            status: <p>The search jobs to be included in the export job can be filtered by including this parameter.</p>
            search_job_identifier: <p>The unique string that specifies the search job.</p>
            next_token: <p>The next item following a partial list of returned backups included in a search job.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of backups, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>
            max_results: <p>The maximum number of resource list items to be returned.</p>

        Raises:
            capo_backupsearch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_backupsearch.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_backupsearch.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_backupsearch.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_backupsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found for this request.</p> <p>Confirm the resource information, such as the ARN or type is correct and exists, then retry the request.</p>
            capo_backupsearch.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request denied due to exceeding the quota limits permitted.</p>
            capo_backupsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backupsearch.types.list_search_result_export_jobs_input.ListSearchResultExportJobsInput]",
        ) -> AsyncOperationResponse[
            "capo_backupsearch.types.list_search_result_export_jobs_output.ListSearchResultExportJobsOutput"
        ]:
            import capo_backupsearch._operations.cryo_backup_search_service.list_search_result_export_jobs

            (
                output,
                http_response,
            ) = await capo_backupsearch._operations.cryo_backup_search_service.list_search_result_export_jobs.async_list_search_result_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListSearchResultExportJobs")
        )
        input_: capo_backupsearch.types.list_search_result_export_jobs_input.ListSearchResultExportJobsInput = {}
        if status is not None:
            input_["status"] = status
        if search_job_identifier is not None:
            input_["search_job_identifier"] = search_job_identifier
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
