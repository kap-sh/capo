from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_sagemaker_geospatial._auth._signers
import capo_sagemaker_geospatial._auth._sigv4
from capo_sagemaker_geospatial._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config
    import capo_sagemaker_geospatial.types.get_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.get_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.list_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.list_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.list_vector_enrichment_job_output_config
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.sort_order
    import capo_sagemaker_geospatial.types.start_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.start_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input
    import capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.vector_enrichment_job_arn
    import capo_sagemaker_geospatial.types.vector_enrichment_job_config
    import capo_sagemaker_geospatial.types.vector_enrichment_job_input_config
    from capo_sagemaker_geospatial._services.async_sage_maker_geospatial import (
        AsyncSageMakerGeospatialClient,
        AsyncSageMakerGeospatialClientConfig,
    )
    from capo_sagemaker_geospatial._services.sage_maker_geospatial import (
        SageMakerGeospatialClient,
        SageMakerGeospatialClientConfig,
    )


class VectorEnrichmentJob:
    def __init__(self, service: SageMakerGeospatialClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        input_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig",
        job_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional["capo_sagemaker_geospatial.types.kms_key.KmsKey"] = None,
        tags: Optional["capo_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "capo_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput":
        """<p>Creates a Vector Enrichment job for the supplied job type. Currently, there are two supported job types: reverse geocoding and map matching.</p>

        Args:
            name: <p>The name of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Vector Enrichment job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job.start_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput = {
            "name": name,
            "input_config": input_config,
            "job_config": job_config,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput":
        """<p>Retrieves details of a Vector Enrichment Job for a given job Amazon Resource Name (ARN).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job.get_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput = {
            "arn": arn
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
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput":
        """<p>Use this operation to delete a Vector Enrichment job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job being deleted.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job.delete_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput = {
            "arn": arn
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
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        status_equals: Optional[str] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput":
        """<p>Retrieves a list of vector enrichment jobs.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs.list_vector_enrichment_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_vector_enrichment_job_input

            return capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_vector_enrichment_job_output

            return capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListVectorEnrichmentJobs",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput = {}
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    def export_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput":
        """<p>Use this operation to copy results of a Vector Enrichment job to an Amazon S3 location.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.</p>
            output_config: <p>Output location information for exporting Vector Enrichment Job results. </p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job.export_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput = {
            "arn": arn,
            "execution_role_arn": execution_role_arn,
            "output_config": output_config,
        }
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

    def stop_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput":
        """<p>Stops the Vector Enrichment job for a given job ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job.stop_vector_enrichment_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncVectorEnrichmentJob:
    def __init__(self, service: AsyncSageMakerGeospatialClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        input_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_input_config.VectorEnrichmentJobInputConfig",
        job_config: "capo_sagemaker_geospatial.types.vector_enrichment_job_config.VectorEnrichmentJobConfig",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional["capo_sagemaker_geospatial.types.kms_key.KmsKey"] = None,
        tags: Optional["capo_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "capo_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput":
        """<p>Creates a Vector Enrichment job for the supplied job type. Currently, there are two supported job types: reverse geocoding and map matching.</p>

        Args:
            name: <p>The name of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Vector Enrichment job.</p>
            job_config: <p>An object containing information about the job configuration.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            tags: <p>Each tag consists of a key and a value.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.start_vector_enrichment_job_output.StartVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_vector_enrichment_job.async_start_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.start_vector_enrichment_job_input.StartVectorEnrichmentJobInput = {
            "name": name,
            "input_config": input_config,
            "job_config": job_config,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput":
        """<p>Retrieves details of a Vector Enrichment Job for a given job Amazon Resource Name (ARN).</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.get_vector_enrichment_job_output.GetVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_vector_enrichment_job.async_get_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.get_vector_enrichment_job_input.GetVectorEnrichmentJobInput = {
            "arn": arn
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
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput":
        """<p>Use this operation to delete a Vector Enrichment job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job being deleted.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.delete_vector_enrichment_job_output.DeleteVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_vector_enrichment_job.async_delete_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.delete_vector_enrichment_job_input.DeleteVectorEnrichmentJobInput = {
            "arn": arn
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
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        status_equals: Optional[str] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput":
        """<p>Retrieves a list of vector enrichment jobs.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_vector_enrichment_jobs.async_list_vector_enrichment_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_vector_enrichment_job_input

            return capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.ListVectorEnrichmentJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_vector_enrichment_job_output

            return capo_sagemaker_geospatial.types.list_vector_enrichment_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListVectorEnrichmentJobs",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_geospatial.types.list_vector_enrichment_job_input.ListVectorEnrichmentJobInput = {}
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def export_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output_config.ExportVectorEnrichmentJobOutputConfig",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput":
        """<p>Use this operation to copy results of a Vector Enrichment job to an Amazon S3 location.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM rolewith permission to upload to the location in OutputConfig.</p>
            output_config: <p>Output location information for exporting Vector Enrichment Job results. </p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.export_vector_enrichment_job_output.ExportVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_vector_enrichment_job.async_export_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.export_vector_enrichment_job_input.ExportVectorEnrichmentJobInput = {
            "arn": arn,
            "execution_role_arn": execution_role_arn,
            "output_config": output_config,
        }
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

    async def stop_vector_enrichment_job(
        self,
        arn: "capo_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput":
        """<p>Stops the Vector Enrichment job for a given job ARN.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Vector Enrichment job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.conflict_exception.ConflictException: <p>Updating or deleting a resource can cause an inconsistent state.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.stop_vector_enrichment_job_output.StopVectorEnrichmentJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_vector_enrichment_job.async_stop_vector_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopVectorEnrichmentJob")
        )
        input_: capo_sagemaker_geospatial.types.stop_vector_enrichment_job_input.StopVectorEnrichmentJobInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
