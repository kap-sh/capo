from __future__ import annotations

import uuid
from collections.abc import AsyncIterator, Iterator
from typing import TYPE_CHECKING, Optional

import capo_omics._auth._signers
import capo_omics._auth._sigv4
from capo_omics._body import Body, aclosing_bodies, closing_bodies
from capo_omics._iter import ensure_async_iterator, ensure_sync_iterator
from capo_omics._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_omics.types.abort_multipart_read_set_upload_request
    import capo_omics.types.abort_multipart_read_set_upload_response
    import capo_omics.types.activate_read_set_filter
    import capo_omics.types.activate_read_set_job_item
    import capo_omics.types.activation_job_id
    import capo_omics.types.client_token
    import capo_omics.types.complete_multipart_read_set_upload_request
    import capo_omics.types.complete_multipart_read_set_upload_response
    import capo_omics.types.complete_read_set_upload_part_list
    import capo_omics.types.create_multipart_read_set_upload_request
    import capo_omics.types.create_multipart_read_set_upload_response
    import capo_omics.types.create_sequence_store_request
    import capo_omics.types.create_sequence_store_response
    import capo_omics.types.delete_sequence_store_request
    import capo_omics.types.delete_sequence_store_response
    import capo_omics.types.e_tag_algorithm_family
    import capo_omics.types.export_job_id
    import capo_omics.types.export_read_set_filter
    import capo_omics.types.export_read_set_job_detail
    import capo_omics.types.export_read_set_list
    import capo_omics.types.fallback_location
    import capo_omics.types.file_type
    import capo_omics.types.generated_from
    import capo_omics.types.get_read_set_activation_job_request
    import capo_omics.types.get_read_set_activation_job_response
    import capo_omics.types.get_read_set_export_job_request
    import capo_omics.types.get_read_set_export_job_response
    import capo_omics.types.get_read_set_import_job_request
    import capo_omics.types.get_read_set_import_job_response
    import capo_omics.types.get_sequence_store_request
    import capo_omics.types.get_sequence_store_response
    import capo_omics.types.import_job_id
    import capo_omics.types.import_read_set_filter
    import capo_omics.types.import_read_set_job_item
    import capo_omics.types.list_multipart_read_set_uploads_request
    import capo_omics.types.list_multipart_read_set_uploads_response
    import capo_omics.types.list_read_set_activation_jobs_request
    import capo_omics.types.list_read_set_activation_jobs_response
    import capo_omics.types.list_read_set_export_jobs_request
    import capo_omics.types.list_read_set_export_jobs_response
    import capo_omics.types.list_read_set_import_jobs_request
    import capo_omics.types.list_read_set_import_jobs_response
    import capo_omics.types.list_read_set_upload_parts_request
    import capo_omics.types.list_read_set_upload_parts_response
    import capo_omics.types.list_sequence_stores_request
    import capo_omics.types.list_sequence_stores_response
    import capo_omics.types.multipart_read_set_upload_list_item
    import capo_omics.types.next_token
    import capo_omics.types.propagated_set_level_tags
    import capo_omics.types.read_set_description
    import capo_omics.types.read_set_name
    import capo_omics.types.read_set_part_source
    import capo_omics.types.read_set_part_streaming_blob
    import capo_omics.types.read_set_upload_part_list_filter
    import capo_omics.types.read_set_upload_part_list_item
    import capo_omics.types.reference_arn
    import capo_omics.types.role_arn
    import capo_omics.types.s3_access_config
    import capo_omics.types.s3_destination
    import capo_omics.types.sample_id
    import capo_omics.types.sequence_store_description
    import capo_omics.types.sequence_store_detail
    import capo_omics.types.sequence_store_filter
    import capo_omics.types.sequence_store_id
    import capo_omics.types.sequence_store_name
    import capo_omics.types.sse_config
    import capo_omics.types.start_read_set_activation_job_request
    import capo_omics.types.start_read_set_activation_job_response
    import capo_omics.types.start_read_set_activation_job_source_list
    import capo_omics.types.start_read_set_export_job_request
    import capo_omics.types.start_read_set_export_job_response
    import capo_omics.types.start_read_set_import_job_request
    import capo_omics.types.start_read_set_import_job_response
    import capo_omics.types.start_read_set_import_job_source_list
    import capo_omics.types.subject_id
    import capo_omics.types.tag_map
    import capo_omics.types.update_sequence_store_request
    import capo_omics.types.update_sequence_store_response
    import capo_omics.types.upload_id
    import capo_omics.types.upload_read_set_part_request
    import capo_omics.types.upload_read_set_part_response
    from capo_omics._services.async_omics import (
        AsyncOmicsClient,
        AsyncOmicsClientConfig,
    )
    from capo_omics._services.omics import OmicsClient, OmicsClientConfig


class SequenceStoreResource:
    def __init__(self, service: OmicsClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_omics.types.sequence_store_name.SequenceStoreName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.sequence_store_description.SequenceStoreDescription"
        ] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        fallback_location: Optional[
            "capo_omics.types.fallback_location.FallbackLocation"
        ] = None,
        e_tag_algorithm_family: Optional[
            "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
        ] = None,
        propagated_set_level_tags: Optional[
            "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
        ] = None,
        s3_access_config: Optional[
            "capo_omics.types.s3_access_config.S3AccessConfig"
        ] = None,
    ) -> "capo_omics.types.create_sequence_store_response.CreateSequenceStoreResponse":
        """<p>Creates a sequence store and returns its metadata. Sequence stores are used to store sequence data files called read sets that are saved in FASTQ, BAM, uBAM, or CRAM formats. For aligned formats (BAM and CRAM), a sequence store can only use one reference genome. For unaligned formats (FASTQ and uBAM), a reference genome is not required. You can create multiple sequence stores per region per account. </p> <p>The following are optional parameters you can specify for your sequence store:</p> <ul> <li> <p>Use <code>s3AccessConfig</code> to configure your sequence store with S3 access logs (recommended).</p> </li> <li> <p>Use <code>sseConfig</code> to define your own KMS key for encryption.</p> </li> <li> <p>Use <code>eTagAlgorithmFamily</code> to define which algorithm to use for the HealthOmics eTag on objects.</p> </li> <li> <p>Use <code>fallbackLocation</code> to define a backup location for storing files that have failed a direct upload.</p> </li> <li> <p>Use <code>propagatedSetLevelTags</code> to configure tags that propagate to all objects in your store.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html">Creating a HealthOmics sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store. You can configure up to 50 tags.</p>
            client_token: <p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>
            fallback_location: <p>An S3 location that is used to store files that have failed a direct upload. You can add or change the <code>fallbackLocation</code> after creating a sequence store. This is not required if you are uploading files from a different S3 bucket.</p>
            e_tag_algorithm_family: <p>The ETag algorithm family to use for ingested read sets. The default value is MD5up. For more information on ETags, see <a href="https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html">ETags and data provenance</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            propagated_set_level_tags: <p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store. These tags can be used as input to add metadata to your read sets.</p>
            s3_access_config: <p>S3 access configuration parameters. This specifies the parameters needed to access logs stored in S3 buckets. The S3 bucket must be in the same region and account as the sequence store. </p>

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
            req: "OperationRequest[capo_omics.types.create_sequence_store_request.CreateSequenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_sequence_store_response.CreateSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.create_sequence_store

            output, http_response = (
                capo_omics._operations.omics.create_sequence_store.create_sequence_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_sequence_store_request.CreateSequenceStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if fallback_location is not None:
            input_["fallback_location"] = fallback_location
        if e_tag_algorithm_family is not None:
            input_["e_tag_algorithm_family"] = e_tag_algorithm_family
        if propagated_set_level_tags is not None:
            input_["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_config is not None:
            input_["s3_access_config"] = s3_access_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_sequence_store_response.GetSequenceStoreResponse":
        """<p>Retrieves metadata for a sequence store using its ID and returns it in JSON format.</p>

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
            req: "OperationRequest[capo_omics.types.get_sequence_store_request.GetSequenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_sequence_store_response.GetSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.get_sequence_store

            output, http_response = (
                capo_omics._operations.omics.get_sequence_store.get_sequence_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_sequence_store_request.GetSequenceStoreRequest = {
            "id": id
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
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        name: Optional["capo_omics.types.sequence_store_name.SequenceStoreName"] = None,
        description: Optional[
            "capo_omics.types.sequence_store_description.SequenceStoreDescription"
        ] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        fallback_location: Optional[
            "capo_omics.types.fallback_location.FallbackLocation"
        ] = None,
        propagated_set_level_tags: Optional[
            "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
        ] = None,
        s3_access_config: Optional[
            "capo_omics.types.s3_access_config.S3AccessConfig"
        ] = None,
    ) -> "capo_omics.types.update_sequence_store_response.UpdateSequenceStoreResponse":
        """<p>Update one or more parameters for the sequence store.</p>

        Args:
            id: <p>The ID of the sequence store.</p>
            name: <p>A name for the sequence store.</p>
            description: <p>A description for the sequence store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>
            fallback_location: <p>The S3 URI of a bucket and folder to store Read Sets that fail to upload.</p>
            propagated_set_level_tags: <p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>
            s3_access_config: <p>S3 access configuration parameters.</p>

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
            req: "OperationRequest[capo_omics.types.update_sequence_store_request.UpdateSequenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.update_sequence_store_response.UpdateSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.update_sequence_store

            output, http_response = (
                capo_omics._operations.omics.update_sequence_store.update_sequence_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_sequence_store_request.UpdateSequenceStoreRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if fallback_location is not None:
            input_["fallback_location"] = fallback_location
        if propagated_set_level_tags is not None:
            input_["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_config is not None:
            input_["s3_access_config"] = s3_access_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.delete_sequence_store_response.DeleteSequenceStoreResponse":
        """<p>Deletes a sequence store and returns a response with no body if the operation is successful. You can only delete a sequence store when it does not contain any read sets.</p> <p>Use the <code>BatchDeleteReadSet</code> API operation to ensure that all read sets in the sequence store are deleted. When a sequence store is deleted, all tags associated with the store are also deleted.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The sequence store's ID.</p>

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
            req: "OperationRequest[capo_omics.types.delete_sequence_store_request.DeleteSequenceStoreRequest]",
        ) -> OperationResponse[
            "capo_omics.types.delete_sequence_store_response.DeleteSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_sequence_store

            output, http_response = (
                capo_omics._operations.omics.delete_sequence_store.delete_sequence_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_sequence_store_request.DeleteSequenceStoreRequest = {
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
            "capo_omics.types.sequence_store_filter.SequenceStoreFilter"
        ] = None,
    ) -> "capo_omics.types.list_sequence_stores_response.ListSequenceStoresResponse":
        """<p>Retrieves a list of sequence stores and returns each sequence store's metadata.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html">Creating a HealthOmics sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

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
            req: "OperationRequest[capo_omics.types.list_sequence_stores_request.ListSequenceStoresRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_sequence_stores_response.ListSequenceStoresResponse"
        ]:
            import capo_omics._operations.omics.list_sequence_stores

            output, http_response = (
                capo_omics._operations.omics.list_sequence_stores.list_sequence_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_sequence_stores_request.ListSequenceStoresRequest = {}
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

    def abort_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.abort_multipart_read_set_upload_response.AbortMultipartReadSetUploadResponse":
        """<p>Stops a multipart read set upload into a sequence store and returns a response with no body if the operation is successful. To confirm that a multipart read set upload has been stopped, use the <code>ListMultipartReadSetUploads</code> API operation to view all active multipart read set uploads.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store involved in the multipart upload.</p>
            upload_id: <p>The ID for the multipart upload.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.abort_multipart_read_set_upload_request.AbortMultipartReadSetUploadRequest]",
        ) -> OperationResponse[
            "capo_omics.types.abort_multipart_read_set_upload_response.AbortMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.abort_multipart_read_set_upload

            output, http_response = (
                capo_omics._operations.omics.abort_multipart_read_set_upload.abort_multipart_read_set_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.abort_multipart_read_set_upload_request.AbortMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def complete_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        parts: "capo_omics.types.complete_read_set_upload_part_list.CompleteReadSetUploadPartList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.complete_multipart_read_set_upload_response.CompleteMultipartReadSetUploadResponse":
        """<p>Completes a multipart read set upload into a sequence store after you have initiated the upload process with <code>CreateMultipartReadSetUpload</code> and uploaded all read set parts using <code>UploadReadSetPart</code>. You must specify the parts you uploaded using the parts parameter. If the operation is successful, it returns the read set ID(s) of the uploaded read set(s).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store involved in the multipart upload.</p>
            upload_id: <p>The ID for the multipart upload.</p>
            parts: <p>The individual uploads or parts of a multipart upload.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.complete_multipart_read_set_upload_request.CompleteMultipartReadSetUploadRequest]",
        ) -> OperationResponse[
            "capo_omics.types.complete_multipart_read_set_upload_response.CompleteMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.complete_multipart_read_set_upload

            output, http_response = (
                capo_omics._operations.omics.complete_multipart_read_set_upload.complete_multipart_read_set_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.complete_multipart_read_set_upload_request.CompleteMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "parts": parts,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        source_file_type: "capo_omics.types.file_type.FileType",
        subject_id: "capo_omics.types.subject_id.SubjectId",
        sample_id: "capo_omics.types.sample_id.SampleId",
        name: "capo_omics.types.read_set_name.ReadSetName",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        generated_from: Optional[
            "capo_omics.types.generated_from.GeneratedFrom"
        ] = None,
        reference_arn: Optional["capo_omics.types.reference_arn.ReferenceArn"] = None,
        description: Optional[
            "capo_omics.types.read_set_description.ReadSetDescription"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_multipart_read_set_upload_response.CreateMultipartReadSetUploadResponse":
        """<p>Initiates a multipart read set upload for uploading partitioned source files into a sequence store. You can directly import source files from an EC2 instance and other local compute, or from an S3 bucket. To separate these source files into parts, use the <code>split</code> operation. Each part cannot be larger than 100 MB. If the operation is successful, it provides an <code>uploadId</code> which is required by the <code>UploadReadSetPart</code> API operation to upload parts into a sequence store.</p> <p>To continue uploading a multipart read set into your sequence store, you must use the <code>UploadReadSetPart</code> API operation to upload each part individually following the steps below:</p> <ul> <li> <p>Specify the <code>uploadId</code> obtained from the previous call to <code>CreateMultipartReadSetUpload</code>.</p> </li> <li> <p>Upload parts for that <code>uploadId</code>.</p> </li> </ul> <p>When you have finished uploading parts, use the <code>CompleteMultipartReadSetUpload</code> API to complete the multipart read set upload and to retrieve the final read set IDs in the response.</p> <p>To learn more about creating parts and the <code>split</code> operation, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store that is the destination of the multipart uploads.</p>
            client_token: <p>An idempotency token that can be used to avoid triggering multiple multipart uploads.</p>
            source_file_type: <p>The type of file being uploaded.</p>
            subject_id: <p>The source's subject ID.</p>
            sample_id: <p>The source's sample ID.</p>
            generated_from: <p>Where the source originated.</p>
            reference_arn: <p>The ARN of the reference.</p>
            name: <p>The name of the read set.</p>
            description: <p>The description of the read set.</p>
            tags: <p>Any tags to add to the read set.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.create_multipart_read_set_upload_request.CreateMultipartReadSetUploadRequest]",
        ) -> OperationResponse[
            "capo_omics.types.create_multipart_read_set_upload_response.CreateMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.create_multipart_read_set_upload

            output, http_response = (
                capo_omics._operations.omics.create_multipart_read_set_upload.create_multipart_read_set_upload(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_multipart_read_set_upload_request.CreateMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "source_file_type": source_file_type,
            "subject_id": subject_id,
            "sample_id": sample_id,
            "name": name,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if generated_from is not None:
            input_["generated_from"] = generated_from
        if reference_arn is not None:
            input_["reference_arn"] = reference_arn
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_read_set_activation_job(
        self,
        id: "capo_omics.types.activation_job_id.ActivationJobId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.get_read_set_activation_job_response.GetReadSetActivationJobResponse":
        """<p>Returns detailed information about the status of a read set activation job in JSON format.</p>

        Args:
            id: <p>The job's ID.</p>
            sequence_store_id: <p>The job's sequence store ID.</p>

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
            req: "OperationRequest[capo_omics.types.get_read_set_activation_job_request.GetReadSetActivationJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_read_set_activation_job_response.GetReadSetActivationJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_activation_job

            output, http_response = (
                capo_omics._operations.omics.get_read_set_activation_job.get_read_set_activation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_activation_job_request.GetReadSetActivationJobRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_read_set_export_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        id: "capo_omics.types.export_job_id.ExportJobId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_read_set_export_job_response.GetReadSetExportJobResponse"
    ):
        """<p>Retrieves status information about a read set export job and returns the data in JSON format. Use this operation to actively monitor the progress of an export job.</p>

        Args:
            sequence_store_id: <p>The job's sequence store ID.</p>
            id: <p>The job's ID.</p>

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
            req: "OperationRequest[capo_omics.types.get_read_set_export_job_request.GetReadSetExportJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_read_set_export_job_response.GetReadSetExportJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_export_job

            output, http_response = (
                capo_omics._operations.omics.get_read_set_export_job.get_read_set_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_export_job_request.GetReadSetExportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "id": id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_read_set_import_job(
        self,
        id: "capo_omics.types.import_job_id.ImportJobId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_read_set_import_job_response.GetReadSetImportJobResponse"
    ):
        """<p>Gets detailed and status information about a read set import job and returns the data in JSON format.</p>

        Args:
            id: <p>The job's ID.</p>
            sequence_store_id: <p>The job's sequence store ID.</p>

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
            req: "OperationRequest[capo_omics.types.get_read_set_import_job_request.GetReadSetImportJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.get_read_set_import_job_response.GetReadSetImportJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_import_job

            output, http_response = (
                capo_omics._operations.omics.get_read_set_import_job.get_read_set_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_import_job_request.GetReadSetImportJobRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_multipart_read_set_uploads(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
    ) -> "capo_omics.types.list_multipart_read_set_uploads_response.ListMultipartReadSetUploadsResponse":
        """<p>Lists in-progress multipart read set uploads for a sequence store and returns it in a JSON formatted output. Multipart read set uploads are initiated by the <code>CreateMultipartReadSetUploads</code> API operation. This operation returns a response with no body when the upload is complete. </p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart uploads.</p>
            max_results: <p>The maximum number of multipart uploads returned in a page.</p>
            next_token: <p>Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_multipart_read_set_uploads_request.ListMultipartReadSetUploadsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_multipart_read_set_uploads_response.ListMultipartReadSetUploadsResponse"
        ]:
            import capo_omics._operations.omics.list_multipart_read_set_uploads

            output, http_response = (
                capo_omics._operations.omics.list_multipart_read_set_uploads.list_multipart_read_set_uploads(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_multipart_read_set_uploads_request.ListMultipartReadSetUploadsRequest = {
            "sequence_store_id": sequence_store_id
        }
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

    def list_read_set_activation_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.activate_read_set_filter.ActivateReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_activation_jobs_response.ListReadSetActivationJobsResponse":
        """<p>Retrieves a list of read set activation jobs and returns the metadata in a JSON formatted output. To extract metadata from a read set activation job, use the <code>GetReadSetActivationJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            max_results: <p>The maximum number of read set activation jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
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
            req: "OperationRequest[capo_omics.types.list_read_set_activation_jobs_request.ListReadSetActivationJobsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_read_set_activation_jobs_response.ListReadSetActivationJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_activation_jobs

            output, http_response = (
                capo_omics._operations.omics.list_read_set_activation_jobs.list_read_set_activation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_activation_jobs_request.ListReadSetActivationJobsRequest = {
            "sequence_store_id": sequence_store_id
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

    def list_read_set_export_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.export_read_set_filter.ExportReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_export_jobs_response.ListReadSetExportJobsResponse":
        """<p>Retrieves a list of read set export jobs in a JSON formatted response. This API operation is used to check the status of a read set export job initiated by the <code>StartReadSetExportJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The jobs' sequence store ID.</p>
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
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
            req: "OperationRequest[capo_omics.types.list_read_set_export_jobs_request.ListReadSetExportJobsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_read_set_export_jobs_response.ListReadSetExportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_export_jobs

            output, http_response = (
                capo_omics._operations.omics.list_read_set_export_jobs.list_read_set_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_export_jobs_request.ListReadSetExportJobsRequest = {
            "sequence_store_id": sequence_store_id
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

    def list_read_set_import_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_read_set_filter.ImportReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_import_jobs_response.ListReadSetImportJobsResponse":
        """<p>Retrieves a list of read set import jobs and returns the data in JSON format.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sequence_store_id: <p>The jobs' sequence store ID.</p>
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
            req: "OperationRequest[capo_omics.types.list_read_set_import_jobs_request.ListReadSetImportJobsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_read_set_import_jobs_response.ListReadSetImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_import_jobs

            output, http_response = (
                capo_omics._operations.omics.list_read_set_import_jobs.list_read_set_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_import_jobs_request.ListReadSetImportJobsRequest = {
            "sequence_store_id": sequence_store_id
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

    def list_read_set_upload_parts(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.read_set_upload_part_list_filter.ReadSetUploadPartListFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_upload_parts_response.ListReadSetUploadPartsResponse":
        """<p>Lists all parts in a multipart read set upload for a sequence store and returns the metadata in a JSON formatted output.</p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart uploads.</p>
            upload_id: <p>The ID for the initiated multipart upload.</p>
            part_source: <p>The source file for the upload part.</p>
            max_results: <p>The maximum number of read set upload parts returned in a page.</p>
            next_token: <p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>
            filter: <p>Attributes used to filter for a specific subset of read set part uploads.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.list_read_set_upload_parts_request.ListReadSetUploadPartsRequest]",
        ) -> OperationResponse[
            "capo_omics.types.list_read_set_upload_parts_response.ListReadSetUploadPartsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_upload_parts

            output, http_response = (
                capo_omics._operations.omics.list_read_set_upload_parts.list_read_set_upload_parts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_upload_parts_request.ListReadSetUploadPartsRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "part_source": part_source,
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

    def start_read_set_activation_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        sources: "capo_omics.types.start_read_set_activation_job_source_list.StartReadSetActivationJobSourceList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_activation_job_response.StartReadSetActivationJobResponse":
        """<p>Activates an archived read set and returns its metadata in a JSON formatted output. Amazon Web Services HealthOmics automatically archives unused read sets after 30 days. To monitor the status of your read set activation job, use the <code>GetReadSetActivationJob</code> operation.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/activating-read-sets.html">Activating read sets</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
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
            req: "OperationRequest[capo_omics.types.start_read_set_activation_job_request.StartReadSetActivationJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.start_read_set_activation_job_response.StartReadSetActivationJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_activation_job

            output, http_response = (
                capo_omics._operations.omics.start_read_set_activation_job.start_read_set_activation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_activation_job_request.StartReadSetActivationJobRequest = {
            "sequence_store_id": sequence_store_id,
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

    def start_read_set_export_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        destination: "capo_omics.types.s3_destination.S3Destination",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.export_read_set_list.ExportReadSetList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_export_job_response.StartReadSetExportJobResponse":
        """<p>Starts a read set export job. When the export job is finished, the read set is exported to an Amazon S3 bucket which can be retrieved using the <code>GetReadSetExportJob</code> API operation.</p> <p>To monitor the status of the export job, use the <code>ListReadSetExportJobs</code> API operation. </p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            destination: <p>A location for exported files in Amazon S3.</p>
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
            req: "OperationRequest[capo_omics.types.start_read_set_export_job_request.StartReadSetExportJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.start_read_set_export_job_response.StartReadSetExportJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_export_job

            output, http_response = (
                capo_omics._operations.omics.start_read_set_export_job.start_read_set_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_export_job_request.StartReadSetExportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "destination": destination,
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

    def start_read_set_import_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.start_read_set_import_job_source_list.StartReadSetImportJobSourceList",
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_import_job_response.StartReadSetImportJobResponse":
        """<p>Imports a read set from the sequence store. Read set import jobs support a maximum of 100 read sets of different types. Monitor the progress of your read set import job by calling the <code>GetReadSetImportJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
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
            req: "OperationRequest[capo_omics.types.start_read_set_import_job_request.StartReadSetImportJobRequest]",
        ) -> OperationResponse[
            "capo_omics.types.start_read_set_import_job_response.StartReadSetImportJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_import_job

            output, http_response = (
                capo_omics._operations.omics.start_read_set_import_job.start_read_set_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_import_job_request.StartReadSetImportJobRequest = {
            "sequence_store_id": sequence_store_id,
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

    def upload_read_set_part(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        part_number: int,
        payload: Body[Iterator[bytes]] | Iterator[bytes] | bytes,
        *,
        config_overrides: Optional[OmicsClientConfig] = None,
    ) -> "capo_omics.types.upload_read_set_part_response.UploadReadSetPartResponse":
        """<p>Uploads a specific part of a read set into a sequence store. When you a upload a read set part with a part number that already exists, the new part replaces the existing one. This operation returns a JSON formatted response containing a string identifier that is used to confirm that parts are being added to the intended upload.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart upload.</p>
            upload_id: <p>The ID for the initiated multipart upload.</p>
            part_source: <p>The source file for an upload part.</p>
            part_number: <p>The number of the part being uploaded.</p>
            payload: <p>The read set data to upload for a part.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_omics.types.upload_read_set_part_request.UploadReadSetPartRequest]",
        ) -> OperationResponse[
            "capo_omics.types.upload_read_set_part_response.UploadReadSetPartResponse"
        ]:
            import capo_omics._operations.omics.upload_read_set_part

            output, http_response = (
                capo_omics._operations.omics.upload_read_set_part.upload_read_set_part(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.upload_read_set_part_request.UploadReadSetPartRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "part_source": part_source,
            "part_number": part_number,
            "payload": ensure_sync_iterator(payload),
        }

        with closing_bodies(input_):
            response = execute_pipeline(
                OperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            response.response.close()
            return response.output


class AsyncSequenceStoreResource:
    def __init__(self, service: AsyncOmicsClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_omics.types.sequence_store_name.SequenceStoreName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        description: Optional[
            "capo_omics.types.sequence_store_description.SequenceStoreDescription"
        ] = None,
        sse_config: Optional["capo_omics.types.sse_config.SseConfig"] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        fallback_location: Optional[
            "capo_omics.types.fallback_location.FallbackLocation"
        ] = None,
        e_tag_algorithm_family: Optional[
            "capo_omics.types.e_tag_algorithm_family.ETagAlgorithmFamily"
        ] = None,
        propagated_set_level_tags: Optional[
            "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
        ] = None,
        s3_access_config: Optional[
            "capo_omics.types.s3_access_config.S3AccessConfig"
        ] = None,
    ) -> "capo_omics.types.create_sequence_store_response.CreateSequenceStoreResponse":
        """<p>Creates a sequence store and returns its metadata. Sequence stores are used to store sequence data files called read sets that are saved in FASTQ, BAM, uBAM, or CRAM formats. For aligned formats (BAM and CRAM), a sequence store can only use one reference genome. For unaligned formats (FASTQ and uBAM), a reference genome is not required. You can create multiple sequence stores per region per account. </p> <p>The following are optional parameters you can specify for your sequence store:</p> <ul> <li> <p>Use <code>s3AccessConfig</code> to configure your sequence store with S3 access logs (recommended).</p> </li> <li> <p>Use <code>sseConfig</code> to define your own KMS key for encryption.</p> </li> <li> <p>Use <code>eTagAlgorithmFamily</code> to define which algorithm to use for the HealthOmics eTag on objects.</p> </li> <li> <p>Use <code>fallbackLocation</code> to define a backup location for storing files that have failed a direct upload.</p> </li> <li> <p>Use <code>propagatedSetLevelTags</code> to configure tags that propagate to all objects in your store.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html">Creating a HealthOmics sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            name: <p>A name for the store.</p>
            description: <p>A description for the store.</p>
            sse_config: <p>Server-side encryption (SSE) settings for the store.</p>
            tags: <p>Tags for the store. You can configure up to 50 tags.</p>
            client_token: <p>An idempotency token used to dedupe retry requests so that duplicate runs are not created.</p>
            fallback_location: <p>An S3 location that is used to store files that have failed a direct upload. You can add or change the <code>fallbackLocation</code> after creating a sequence store. This is not required if you are uploading files from a different S3 bucket.</p>
            e_tag_algorithm_family: <p>The ETag algorithm family to use for ingested read sets. The default value is MD5up. For more information on ETags, see <a href="https://docs.aws.amazon.com/omics/latest/dev/etags-and-provenance.html">ETags and data provenance</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>
            propagated_set_level_tags: <p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store. These tags can be used as input to add metadata to your read sets.</p>
            s3_access_config: <p>S3 access configuration parameters. This specifies the parameters needed to access logs stored in S3 buckets. The S3 bucket must be in the same region and account as the sequence store. </p>

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
            req: "AsyncOperationRequest[capo_omics.types.create_sequence_store_request.CreateSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_sequence_store_response.CreateSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.create_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_sequence_store.async_create_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_sequence_store_request.CreateSequenceStoreRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sse_config is not None:
            input_["sse_config"] = sse_config
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if fallback_location is not None:
            input_["fallback_location"] = fallback_location
        if e_tag_algorithm_family is not None:
            input_["e_tag_algorithm_family"] = e_tag_algorithm_family
        if propagated_set_level_tags is not None:
            input_["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_config is not None:
            input_["s3_access_config"] = s3_access_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_sequence_store_response.GetSequenceStoreResponse":
        """<p>Retrieves metadata for a sequence store using its ID and returns it in JSON format.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.get_sequence_store_request.GetSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_sequence_store_response.GetSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.get_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_sequence_store.async_get_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_sequence_store_request.GetSequenceStoreRequest = {
            "id": id
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
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        name: Optional["capo_omics.types.sequence_store_name.SequenceStoreName"] = None,
        description: Optional[
            "capo_omics.types.sequence_store_description.SequenceStoreDescription"
        ] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        fallback_location: Optional[
            "capo_omics.types.fallback_location.FallbackLocation"
        ] = None,
        propagated_set_level_tags: Optional[
            "capo_omics.types.propagated_set_level_tags.PropagatedSetLevelTags"
        ] = None,
        s3_access_config: Optional[
            "capo_omics.types.s3_access_config.S3AccessConfig"
        ] = None,
    ) -> "capo_omics.types.update_sequence_store_response.UpdateSequenceStoreResponse":
        """<p>Update one or more parameters for the sequence store.</p>

        Args:
            id: <p>The ID of the sequence store.</p>
            name: <p>A name for the sequence store.</p>
            description: <p>A description for the sequence store.</p>
            client_token: <p>To ensure that requests don't run multiple times, specify a unique token for each request.</p>
            fallback_location: <p>The S3 URI of a bucket and folder to store Read Sets that fail to upload.</p>
            propagated_set_level_tags: <p>The tags keys to propagate to the S3 objects associated with read sets in the sequence store.</p>
            s3_access_config: <p>S3 access configuration parameters.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.update_sequence_store_request.UpdateSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.update_sequence_store_response.UpdateSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.update_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.update_sequence_store.async_update_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.update_sequence_store_request.UpdateSequenceStoreRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if fallback_location is not None:
            input_["fallback_location"] = fallback_location
        if propagated_set_level_tags is not None:
            input_["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_config is not None:
            input_["s3_access_config"] = s3_access_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.delete_sequence_store_response.DeleteSequenceStoreResponse":
        """<p>Deletes a sequence store and returns a response with no body if the operation is successful. You can only delete a sequence store when it does not contain any read sets.</p> <p>Use the <code>BatchDeleteReadSet</code> API operation to ensure that all read sets in the sequence store are deleted. When a sequence store is deleted, all tags associated with the store are also deleted.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/deleting-reference-and-sequence-stores.html">Deleting HealthOmics reference and sequence stores</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            id: <p>The sequence store's ID.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.delete_sequence_store_request.DeleteSequenceStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.delete_sequence_store_response.DeleteSequenceStoreResponse"
        ]:
            import capo_omics._operations.omics.delete_sequence_store

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.delete_sequence_store.async_delete_sequence_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.delete_sequence_store_request.DeleteSequenceStoreRequest = {
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
            "capo_omics.types.sequence_store_filter.SequenceStoreFilter"
        ] = None,
    ) -> "capo_omics.types.list_sequence_stores_response.ListSequenceStoresResponse":
        """<p>Retrieves a list of sequence stores and returns each sequence store's metadata.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html">Creating a HealthOmics sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.list_sequence_stores_request.ListSequenceStoresRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_sequence_stores_response.ListSequenceStoresResponse"
        ]:
            import capo_omics._operations.omics.list_sequence_stores

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_sequence_stores.async_list_sequence_stores(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_sequence_stores_request.ListSequenceStoresRequest = {}
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

    async def abort_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.abort_multipart_read_set_upload_response.AbortMultipartReadSetUploadResponse":
        """<p>Stops a multipart read set upload into a sequence store and returns a response with no body if the operation is successful. To confirm that a multipart read set upload has been stopped, use the <code>ListMultipartReadSetUploads</code> API operation to view all active multipart read set uploads.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store involved in the multipart upload.</p>
            upload_id: <p>The ID for the multipart upload.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.abort_multipart_read_set_upload_request.AbortMultipartReadSetUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.abort_multipart_read_set_upload_response.AbortMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.abort_multipart_read_set_upload

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.abort_multipart_read_set_upload.async_abort_multipart_read_set_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.abort_multipart_read_set_upload_request.AbortMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def complete_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        parts: "capo_omics.types.complete_read_set_upload_part_list.CompleteReadSetUploadPartList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.complete_multipart_read_set_upload_response.CompleteMultipartReadSetUploadResponse":
        """<p>Completes a multipart read set upload into a sequence store after you have initiated the upload process with <code>CreateMultipartReadSetUpload</code> and uploaded all read set parts using <code>UploadReadSetPart</code>. You must specify the parts you uploaded using the parts parameter. If the operation is successful, it returns the read set ID(s) of the uploaded read set(s).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store involved in the multipart upload.</p>
            upload_id: <p>The ID for the multipart upload.</p>
            parts: <p>The individual uploads or parts of a multipart upload.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.complete_multipart_read_set_upload_request.CompleteMultipartReadSetUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.complete_multipart_read_set_upload_response.CompleteMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.complete_multipart_read_set_upload

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.complete_multipart_read_set_upload.async_complete_multipart_read_set_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.complete_multipart_read_set_upload_request.CompleteMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "parts": parts,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_multipart_read_set_upload(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        source_file_type: "capo_omics.types.file_type.FileType",
        subject_id: "capo_omics.types.subject_id.SubjectId",
        sample_id: "capo_omics.types.sample_id.SampleId",
        name: "capo_omics.types.read_set_name.ReadSetName",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
        generated_from: Optional[
            "capo_omics.types.generated_from.GeneratedFrom"
        ] = None,
        reference_arn: Optional["capo_omics.types.reference_arn.ReferenceArn"] = None,
        description: Optional[
            "capo_omics.types.read_set_description.ReadSetDescription"
        ] = None,
        tags: Optional["capo_omics.types.tag_map.TagMap"] = None,
    ) -> "capo_omics.types.create_multipart_read_set_upload_response.CreateMultipartReadSetUploadResponse":
        """<p>Initiates a multipart read set upload for uploading partitioned source files into a sequence store. You can directly import source files from an EC2 instance and other local compute, or from an S3 bucket. To separate these source files into parts, use the <code>split</code> operation. Each part cannot be larger than 100 MB. If the operation is successful, it provides an <code>uploadId</code> which is required by the <code>UploadReadSetPart</code> API operation to upload parts into a sequence store.</p> <p>To continue uploading a multipart read set into your sequence store, you must use the <code>UploadReadSetPart</code> API operation to upload each part individually following the steps below:</p> <ul> <li> <p>Specify the <code>uploadId</code> obtained from the previous call to <code>CreateMultipartReadSetUpload</code>.</p> </li> <li> <p>Upload parts for that <code>uploadId</code>.</p> </li> </ul> <p>When you have finished uploading parts, use the <code>CompleteMultipartReadSetUpload</code> API to complete the multipart read set upload and to retrieve the final read set IDs in the response.</p> <p>To learn more about creating parts and the <code>split</code> operation, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The sequence store ID for the store that is the destination of the multipart uploads.</p>
            client_token: <p>An idempotency token that can be used to avoid triggering multiple multipart uploads.</p>
            source_file_type: <p>The type of file being uploaded.</p>
            subject_id: <p>The source's subject ID.</p>
            sample_id: <p>The source's sample ID.</p>
            generated_from: <p>Where the source originated.</p>
            reference_arn: <p>The ARN of the reference.</p>
            name: <p>The name of the read set.</p>
            description: <p>The description of the read set.</p>
            tags: <p>Any tags to add to the read set.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.create_multipart_read_set_upload_request.CreateMultipartReadSetUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.create_multipart_read_set_upload_response.CreateMultipartReadSetUploadResponse"
        ]:
            import capo_omics._operations.omics.create_multipart_read_set_upload

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.create_multipart_read_set_upload.async_create_multipart_read_set_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.create_multipart_read_set_upload_request.CreateMultipartReadSetUploadRequest = {
            "sequence_store_id": sequence_store_id,
            "source_file_type": source_file_type,
            "subject_id": subject_id,
            "sample_id": sample_id,
            "name": name,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if generated_from is not None:
            input_["generated_from"] = generated_from
        if reference_arn is not None:
            input_["reference_arn"] = reference_arn
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_read_set_activation_job(
        self,
        id: "capo_omics.types.activation_job_id.ActivationJobId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.get_read_set_activation_job_response.GetReadSetActivationJobResponse":
        """<p>Returns detailed information about the status of a read set activation job in JSON format.</p>

        Args:
            id: <p>The job's ID.</p>
            sequence_store_id: <p>The job's sequence store ID.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_activation_job_request.GetReadSetActivationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_activation_job_response.GetReadSetActivationJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_activation_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_activation_job.async_get_read_set_activation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_activation_job_request.GetReadSetActivationJobRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_read_set_export_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        id: "capo_omics.types.export_job_id.ExportJobId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_read_set_export_job_response.GetReadSetExportJobResponse"
    ):
        """<p>Retrieves status information about a read set export job and returns the data in JSON format. Use this operation to actively monitor the progress of an export job.</p>

        Args:
            sequence_store_id: <p>The job's sequence store ID.</p>
            id: <p>The job's ID.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_export_job_request.GetReadSetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_export_job_response.GetReadSetExportJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_export_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_export_job.async_get_read_set_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_export_job_request.GetReadSetExportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_read_set_import_job(
        self,
        id: "capo_omics.types.import_job_id.ImportJobId",
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> (
        "capo_omics.types.get_read_set_import_job_response.GetReadSetImportJobResponse"
    ):
        """<p>Gets detailed and status information about a read set import job and returns the data in JSON format.</p>

        Args:
            id: <p>The job's ID.</p>
            sequence_store_id: <p>The job's sequence store ID.</p>

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
            req: "AsyncOperationRequest[capo_omics.types.get_read_set_import_job_request.GetReadSetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.get_read_set_import_job_response.GetReadSetImportJobResponse"
        ]:
            import capo_omics._operations.omics.get_read_set_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.get_read_set_import_job.async_get_read_set_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.get_read_set_import_job_request.GetReadSetImportJobRequest = {
            "id": id,
            "sequence_store_id": sequence_store_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_multipart_read_set_uploads(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
    ) -> "capo_omics.types.list_multipart_read_set_uploads_response.ListMultipartReadSetUploadsResponse":
        """<p>Lists in-progress multipart read set uploads for a sequence store and returns it in a JSON formatted output. Multipart read set uploads are initiated by the <code>CreateMultipartReadSetUploads</code> API operation. This operation returns a response with no body when the upload is complete. </p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart uploads.</p>
            max_results: <p>The maximum number of multipart uploads returned in a page.</p>
            next_token: <p>Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_multipart_read_set_uploads_request.ListMultipartReadSetUploadsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_multipart_read_set_uploads_response.ListMultipartReadSetUploadsResponse"
        ]:
            import capo_omics._operations.omics.list_multipart_read_set_uploads

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_multipart_read_set_uploads.async_list_multipart_read_set_uploads(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_multipart_read_set_uploads_request.ListMultipartReadSetUploadsRequest = {
            "sequence_store_id": sequence_store_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_read_set_activation_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.activate_read_set_filter.ActivateReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_activation_jobs_response.ListReadSetActivationJobsResponse":
        """<p>Retrieves a list of read set activation jobs and returns the metadata in a JSON formatted output. To extract metadata from a read set activation job, use the <code>GetReadSetActivationJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            max_results: <p>The maximum number of read set activation jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_activation_jobs_request.ListReadSetActivationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_activation_jobs_response.ListReadSetActivationJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_activation_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_activation_jobs.async_list_read_set_activation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_activation_jobs_request.ListReadSetActivationJobsRequest = {
            "sequence_store_id": sequence_store_id
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

    async def list_read_set_export_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.export_read_set_filter.ExportReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_export_jobs_response.ListReadSetExportJobsResponse":
        """<p>Retrieves a list of read set export jobs in a JSON formatted response. This API operation is used to check the status of a read set export job initiated by the <code>StartReadSetExportJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The jobs' sequence store ID.</p>
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_export_jobs_request.ListReadSetExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_export_jobs_response.ListReadSetExportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_export_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_export_jobs.async_list_read_set_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_export_jobs_request.ListReadSetExportJobsRequest = {
            "sequence_store_id": sequence_store_id
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

    async def list_read_set_import_jobs(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.import_read_set_filter.ImportReadSetFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_import_jobs_response.ListReadSetImportJobsResponse":
        """<p>Retrieves a list of read set import jobs and returns the data in JSON format.</p>

        Args:
            max_results: <p>The maximum number of jobs to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            sequence_store_id: <p>The jobs' sequence store ID.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_import_jobs_request.ListReadSetImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_import_jobs_response.ListReadSetImportJobsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_import_jobs

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_import_jobs.async_list_read_set_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_import_jobs_request.ListReadSetImportJobsRequest = {
            "sequence_store_id": sequence_store_id
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

    async def list_read_set_upload_parts(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_omics.types.next_token.NextToken"] = None,
        filter: Optional[
            "capo_omics.types.read_set_upload_part_list_filter.ReadSetUploadPartListFilter"
        ] = None,
    ) -> "capo_omics.types.list_read_set_upload_parts_response.ListReadSetUploadPartsResponse":
        """<p>Lists all parts in a multipart read set upload for a sequence store and returns the metadata in a JSON formatted output.</p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart uploads.</p>
            upload_id: <p>The ID for the initiated multipart upload.</p>
            part_source: <p>The source file for the upload part.</p>
            max_results: <p>The maximum number of read set upload parts returned in a page.</p>
            next_token: <p>Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.</p>
            filter: <p>Attributes used to filter for a specific subset of read set part uploads.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.list_read_set_upload_parts_request.ListReadSetUploadPartsRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.list_read_set_upload_parts_response.ListReadSetUploadPartsResponse"
        ]:
            import capo_omics._operations.omics.list_read_set_upload_parts

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.list_read_set_upload_parts.async_list_read_set_upload_parts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.list_read_set_upload_parts_request.ListReadSetUploadPartsRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "part_source": part_source,
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

    async def start_read_set_activation_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        sources: "capo_omics.types.start_read_set_activation_job_source_list.StartReadSetActivationJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_activation_job_response.StartReadSetActivationJobResponse":
        """<p>Activates an archived read set and returns its metadata in a JSON formatted output. Amazon Web Services HealthOmics automatically archives unused read sets after 30 days. To monitor the status of your read set activation job, use the <code>GetReadSetActivationJob</code> operation.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/omics/latest/dev/activating-read-sets.html">Activating read sets</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.start_read_set_activation_job_request.StartReadSetActivationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_read_set_activation_job_response.StartReadSetActivationJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_activation_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_read_set_activation_job.async_start_read_set_activation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_activation_job_request.StartReadSetActivationJobRequest = {
            "sequence_store_id": sequence_store_id,
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

    async def start_read_set_export_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        destination: "capo_omics.types.s3_destination.S3Destination",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.export_read_set_list.ExportReadSetList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_export_job_response.StartReadSetExportJobResponse":
        """<p>Starts a read set export job. When the export job is finished, the read set is exported to an Amazon S3 bucket which can be retrieved using the <code>GetReadSetExportJob</code> API operation.</p> <p>To monitor the status of the export job, use the <code>ListReadSetExportJobs</code> API operation. </p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
            destination: <p>A location for exported files in Amazon S3.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.start_read_set_export_job_request.StartReadSetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_read_set_export_job_response.StartReadSetExportJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_export_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_read_set_export_job.async_start_read_set_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_export_job_request.StartReadSetExportJobRequest = {
            "sequence_store_id": sequence_store_id,
            "destination": destination,
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

    async def start_read_set_import_job(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        role_arn: "capo_omics.types.role_arn.RoleArn",
        sources: "capo_omics.types.start_read_set_import_job_source_list.StartReadSetImportJobSourceList",
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
        client_token: Optional["capo_omics.types.client_token.ClientToken"] = None,
    ) -> "capo_omics.types.start_read_set_import_job_response.StartReadSetImportJobResponse":
        """<p>Imports a read set from the sequence store. Read set import jobs support a maximum of 100 read sets of different types. Monitor the progress of your read set import job by calling the <code>GetReadSetImportJob</code> API operation.</p>

        Args:
            sequence_store_id: <p>The read set's sequence store ID.</p>
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
            req: "AsyncOperationRequest[capo_omics.types.start_read_set_import_job_request.StartReadSetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.start_read_set_import_job_response.StartReadSetImportJobResponse"
        ]:
            import capo_omics._operations.omics.start_read_set_import_job

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.start_read_set_import_job.async_start_read_set_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.start_read_set_import_job_request.StartReadSetImportJobRequest = {
            "sequence_store_id": sequence_store_id,
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

    async def upload_read_set_part(
        self,
        sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId",
        upload_id: "capo_omics.types.upload_id.UploadId",
        part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource",
        part_number: int,
        payload: Body[AsyncIterator[bytes]] | AsyncIterator[bytes] | bytes,
        *,
        config_overrides: Optional[AsyncOmicsClientConfig] = None,
    ) -> "capo_omics.types.upload_read_set_part_response.UploadReadSetPartResponse":
        """<p>Uploads a specific part of a read set into a sequence store. When you a upload a read set part with a part number that already exists, the new part replaces the existing one. This operation returns a JSON formatted response containing a string identifier that is used to confirm that parts are being added to the intended upload.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html">Direct upload to a sequence store</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>

        Args:
            sequence_store_id: <p>The Sequence Store ID used for the multipart upload.</p>
            upload_id: <p>The ID for the initiated multipart upload.</p>
            part_source: <p>The source file for an upload part.</p>
            part_number: <p>The number of the part being uploaded.</p>
            payload: <p>The read set data to upload for a part.</p>

        Raises:
            capo_omics.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_omics.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred. Try the request again.</p>
            capo_omics.errors.not_supported_operation_exception.NotSupportedOperationException: <p> The operation is not supported by Amazon Omics, or the API does not exist. </p>
            capo_omics.errors.request_timeout_exception.RequestTimeoutException: <p>The request timed out.</p>
            capo_omics.errors.resource_not_found_exception.ResourceNotFoundException: <p>The target resource was not found in the current Region.</p>
            capo_omics.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds a service quota.</p>
            capo_omics.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_omics.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_omics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_omics.types.upload_read_set_part_request.UploadReadSetPartRequest]",
        ) -> AsyncOperationResponse[
            "capo_omics.types.upload_read_set_part_response.UploadReadSetPartResponse"
        ]:
            import capo_omics._operations.omics.upload_read_set_part

            (
                output,
                http_response,
            ) = await capo_omics._operations.omics.upload_read_set_part.async_upload_read_set_part(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_omics.types.upload_read_set_part_request.UploadReadSetPartRequest = {
            "sequence_store_id": sequence_store_id,
            "upload_id": upload_id,
            "part_source": part_source,
            "part_number": part_number,
            "payload": ensure_async_iterator(payload),
        }

        async with aclosing_bodies(input_):
            response = await aexecute_pipeline(
                AsyncOperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            await response.response.aclose()
            return response.output
