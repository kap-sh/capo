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
    import capo_omics.types.client_token
    import capo_omics.types.create_reference_store_request
    import capo_omics.types.create_reference_store_response
    import capo_omics.types.delete_reference_store_request
    import capo_omics.types.delete_reference_store_response
    import capo_omics.types.get_reference_import_job_request
    import capo_omics.types.get_reference_import_job_response
    import capo_omics.types.get_reference_store_request
    import capo_omics.types.get_reference_store_response
    import capo_omics.types.import_job_id
    import capo_omics.types.import_reference_filter
    import capo_omics.types.import_reference_job_item
    import capo_omics.types.list_reference_import_jobs_request
    import capo_omics.types.list_reference_import_jobs_response
    import capo_omics.types.list_reference_stores_request
    import capo_omics.types.list_reference_stores_response
    import capo_omics.types.next_token
    import capo_omics.types.reference_store_description
    import capo_omics.types.reference_store_detail
    import capo_omics.types.reference_store_filter
    import capo_omics.types.reference_store_id
    import capo_omics.types.reference_store_name
    import capo_omics.types.role_arn
    import capo_omics.types.sse_config
    import capo_omics.types.start_reference_import_job_request
    import capo_omics.types.start_reference_import_job_response
    import capo_omics.types.start_reference_import_job_source_list
    import capo_omics.types.tag_map
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class ReferenceStoreResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_omics.types.reference_store_name.ReferenceStoreName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.reference_store_description.ReferenceStoreDescription"
        ] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
    ):
        """<p>Creates a reference store and returns metadata in JSON format. Reference stores are used to store reference genomes in FASTA format. A reference store is created when the first reference genome is imported. To import additional reference genomes from an Amazon S3 bucket, use the <code>StartReferenceImportJob</code> API operation. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a HealthOmics reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_reference_store_request.CreateReferenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.create_reference_store

            output, http_response = (
                capo_omics._operations.omics.create_reference_store.create_reference_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_reference_store_request.CreateReferenceStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_reference_store_response.GetReferenceStoreResponse":
        """<p>Gets information about a reference store.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_reference_store_request.GetReferenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_reference_store_response.GetReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.get_reference_store

            output, http_response = (
                capo_omics._operations.omics.get_reference_store.get_reference_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_store_request.GetReferenceStoreRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
    ):
        """<p>Deletes a reference store and returns a response with no body if the operation is successful. You can only delete a reference store when it does not contain any reference genomes. To empty a reference store, use <code>DeleteReference</code>.</p> <p>For more information about your workflow status, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_reference_store

            output, http_response = (
                capo_omics._operations.omics.delete_reference_store.delete_reference_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest = {
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
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.reference_store_filter.ReferenceStoreFilter"
        ] = None,
    ) -> "capo_omics.types.list_reference_stores_response.ListReferenceStoresResponse":
        """<p>Retrieves a list of reference stores linked to your account and returns their metadata in JSON format.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_reference_stores_request.ListReferenceStoresRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
        ]:
            import capo_omics._operations.omics.list_reference_stores

            output, http_response = (
                capo_omics._operations.omics.list_reference_stores.list_reference_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_reference_stores_request.ListReferenceStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_reference_import_job(
        self,
        id: "capo_omics.types.import_job_id.ImportJobId",
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse":
        """<p>Monitors the status of a reference import job. This operation can be called after calling the <code>StartReferenceImportJob</code> operation.</p>

        Args:
            id: <p>The job's ID.</p>
            reference_store_id: <p>The job's reference store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse"
        ]:
            import capo_omics._operations.omics.get_reference_import_job

            output, http_response = (
                capo_omics._operations.omics.get_reference_import_job.get_reference_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest = {
            "id": id,
            "reference_store_id": reference_store_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_reference_import_jobs(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_reference_filter.ImportReferenceFilter"
        ] = None,
    ) -> "capo_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse":
        """<p>Retrieves the metadata of one or more reference import jobs for a reference store.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            reference_store_id: <p>The job's reference store ID.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_reference_import_jobs

            output, http_response = (
                capo_omics._operations.omics.list_reference_import_jobs.list_reference_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest = {
            "reference_store_id": reference_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_reference_import_job(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.start_reference_import_job_source_list.StartReferenceImportJobSourceList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse":
        """<p>Imports a reference genome from Amazon S3 into a specified reference store. You can have multiple reference genomes in a reference store. You can only import reference genomes one at a time into each reference store. Monitor the status of your reference import job by using the <code>GetReferenceImportJob</code> API operation.</p>

        Args:
            reference_store_id: <p>The job's reference store ID.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse"
        ]:
            import capo_omics._operations.omics.start_reference_import_job

            output, http_response = (
                capo_omics._operations.omics.start_reference_import_job.start_reference_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest = {
            "reference_store_id": reference_store_id,
            "role_arn": role_arn,
            "sources": sources,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncReferenceStoreResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_omics.types.reference_store_name.ReferenceStoreName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.reference_store_description.ReferenceStoreDescription"
        ] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> (
        "capo_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
    ):
        """<p>Creates a reference store and returns metadata in JSON format. Reference stores are used to store reference genomes in FASTA format. A reference store is created when the first reference genome is imported. To import additional reference genomes from an Amazon S3 bucket, use the <code>StartReferenceImportJob</code> API operation. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a HealthOmics reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_reference_store_request.CreateReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_reference_store_response.CreateReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.create_reference_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_reference_store.async_create_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_reference_store_request.CreateReferenceStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_reference_store_response.GetReferenceStoreResponse":
        """<p>Gets information about a reference store.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_reference_store_request.GetReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_reference_store_response.GetReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.get_reference_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_reference_store.async_get_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_store_request.GetReferenceStoreRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
    ):
        """<p>Deletes a reference store and returns a response with no body if the operation is successful. You can only delete a reference store when it does not contain any reference genomes. To empty a reference store, use <code>DeleteReference</code>.</p> <p>For more information about your workflow status, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The store's ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.conflict_exception.ConflictException: <p>The request cannot be applied to the target resource in its current state.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_reference_store_response.DeleteReferenceStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_reference_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_reference_store.async_delete_reference_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_reference_store_request.DeleteReferenceStoreRequest = {
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
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.reference_store_filter.ReferenceStoreFilter"
        ] = None,
    ) -> "capo_omics.types.list_reference_stores_response.ListReferenceStoresResponse":
        """<p>Retrieves a list of reference stores linked to your account and returns their metadata in JSON format.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-reference-store.html">Creating a reference store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of stores to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_reference_stores_request.ListReferenceStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_reference_stores_response.ListReferenceStoresResponse"
        ]:
            import capo_omics._operations.omics.list_reference_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_reference_stores.async_list_reference_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_reference_stores_request.ListReferenceStoresRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_reference_import_job(
        self,
        id: "capo_omics.types.import_job_id.ImportJobId",
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse":
        """<p>Monitors the status of a reference import job. This operation can be called after calling the <code>StartReferenceImportJob</code> operation.</p>

        Args:
            id: <p>The job's ID.</p>
            reference_store_id: <p>The job's reference store ID.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_reference_import_job_response.GetReferenceImportJobResponse"
        ]:
            import capo_omics._operations.omics.get_reference_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_reference_import_job.async_get_reference_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_reference_import_job_request.GetReferenceImportJobRequest = {
            "id": id,
            "reference_store_id": reference_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_reference_import_jobs(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_reference_filter.ImportReferenceFilter"
        ] = None,
    ) -> "capo_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse":
        """<p>Retrieves the metadata of one or more reference import jobs for a reference store.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            reference_store_id: <p>The job's reference store ID.</p>
            filter: <p>A filter to apply to the list.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_reference_import_jobs_response.ListReferenceImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_reference_import_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_reference_import_jobs.async_list_reference_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_reference_import_jobs_request.ListReferenceImportJobsRequest = {
            "reference_store_id": reference_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_reference_import_job(
        self,
        reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.start_reference_import_job_source_list.StartReferenceImportJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse":
        """<p>Imports a reference genome from Amazon S3 into a specified reference store. You can have multiple reference genomes in a reference store. You can only import reference genomes one at a time into each reference store. Monitor the status of your reference import job by using the <code>GetReferenceImportJob</code> API operation.</p>

        Args:
            reference_store_id: <p>The job's reference store ID.</p>
            role_arn: <p>A service role for the job.</p>
            client_token: <p>To ensure that jobs don't run multiple times, specify a unique token for each job.</p>
            sources: <p>The job's source files.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_reference_import_job_response.StartReferenceImportJobResponse"
        ]:
            import capo_omics._operations.omics.start_reference_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_reference_import_job.async_start_reference_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_reference_import_job_request.StartReferenceImportJobRequest = {
            "reference_store_id": reference_store_id,
            "role_arn": role_arn,
            "sources": sources,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
