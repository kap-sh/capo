from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
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
    import capo_sagemaker_geospatial.types.delete_earth_observation_job_input
    import capo_sagemaker_geospatial.types.delete_earth_observation_job_output
    import capo_sagemaker_geospatial.types.earth_observation_job_arn
    import capo_sagemaker_geospatial.types.earth_observation_job_status
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.export_earth_observation_job_input
    import capo_sagemaker_geospatial.types.export_earth_observation_job_output
    import capo_sagemaker_geospatial.types.get_earth_observation_job_input
    import capo_sagemaker_geospatial.types.get_earth_observation_job_output
    import capo_sagemaker_geospatial.types.get_tile_input
    import capo_sagemaker_geospatial.types.get_tile_output
    import capo_sagemaker_geospatial.types.input_config_input
    import capo_sagemaker_geospatial.types.job_config_input
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.list_earth_observation_job_input
    import capo_sagemaker_geospatial.types.list_earth_observation_job_output
    import capo_sagemaker_geospatial.types.list_earth_observation_job_output_config
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.output_config_input
    import capo_sagemaker_geospatial.types.output_type
    import capo_sagemaker_geospatial.types.sort_order
    import capo_sagemaker_geospatial.types.start_earth_observation_job_input
    import capo_sagemaker_geospatial.types.start_earth_observation_job_output
    import capo_sagemaker_geospatial.types.stop_earth_observation_job_input
    import capo_sagemaker_geospatial.types.stop_earth_observation_job_output
    import capo_sagemaker_geospatial.types.string_list_input
    import capo_sagemaker_geospatial.types.tags
    import capo_sagemaker_geospatial.types.target_options
    from capo_sagemaker_geospatial._services.async_sage_maker_geospatial import (
        AsyncSageMakerGeospatialClient,
        AsyncSageMakerGeospatialClientConfig,
    )
    from capo_sagemaker_geospatial._services.sage_maker_geospatial import (
        SageMakerGeospatialClient,
        SageMakerGeospatialClientConfig,
    )


class EarthObservationJob:
    def __init__(self, service: SageMakerGeospatialClient) -> None:
        self._service = service

    def create(
        self,
        name: str,
        input_config: "capo_sagemaker_geospatial.types.input_config_input.InputConfigInput",
        job_config: "capo_sagemaker_geospatial.types.job_config_input.JobConfigInput",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional["capo_sagemaker_geospatial.types.kms_key.KmsKey"] = None,
        tags: Optional["capo_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput":
        """<p>Use this operation to create an Earth observation job.</p>

        Args:
            name: <p>The name of the Earth Observation job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Earth Observation job.</p>
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
            req: "OperationRequest[capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job.start_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.start_earth_observation_job_input

            return capo_sagemaker_geospatial.types.start_earth_observation_job_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.start_earth_observation_job_output

            return capo_sagemaker_geospatial.types.start_earth_observation_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartEarthObservationJob",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput = {
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
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput":
        """<p>Get the details for a previously initiated Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job.get_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.get_earth_observation_job_output

            return capo_sagemaker_geospatial.types.get_earth_observation_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetEarthObservationJob", redact_output=_redact_output),
        )
        input_: capo_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput = {
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
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput":
        """<p>Use this operation to delete an Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being deleted.</p>

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
            req: "OperationRequest[capo_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job.delete_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEarthObservationJob")
        )
        input_: capo_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput = {
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
        status_equals: Optional[
            "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
        ] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput":
        """<p>Use this operation to get a list of the Earth Observation jobs associated with the calling Amazon Web Services account.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs.list_earth_observation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_earth_observation_job_input

            return capo_sagemaker_geospatial.types.list_earth_observation_job_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_earth_observation_job_output

            return capo_sagemaker_geospatial.types.list_earth_observation_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListEarthObservationJobs",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput = {}
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

    def export_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "capo_sagemaker_geospatial.types.output_config_input.OutputConfigInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        export_source_images: Optional[bool] = None,
    ) -> "capo_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput":
        """<p>Use this operation to export results of an Earth Observation job and optionally source images used as input to the EOJ to an Amazon S3 location.</p>

        Args:
            arn: <p>The input Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            output_config: <p>An object containing information about the output file.</p>
            export_source_images: <p>The source images provided to the Earth Observation job being exported.</p>

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
            req: "OperationRequest[capo_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job.export_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportEarthObservationJob")
        )
        input_: capo_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput = {
            "arn": arn,
            "execution_role_arn": execution_role_arn,
            "output_config": output_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if export_source_images is not None:
            input_["export_source_images"] = export_source_images

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_tile(
        self,
        x: int,
        y: int,
        z: int,
        image_assets: "capo_sagemaker_geospatial.types.string_list_input.StringListInput",
        target: "capo_sagemaker_geospatial.types.target_options.TargetOptions",
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        image_mask: Optional[bool] = None,
        output_format: Optional[str] = None,
        time_range_filter: Optional[str] = None,
        property_filters: Optional[str] = None,
        output_data_type: Optional[
            "capo_sagemaker_geospatial.types.output_type.OutputType"
        ] = None,
        execution_role_arn: Optional[
            "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
    ) -> "Generator[capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput]":
        """<p>Gets a web mercator tile for the given Earth Observation job.</p>

        Args:
            x: <p>The x coordinate of the tile input.</p>
            y: <p>The y coordinate of the tile input.</p>
            z: <p>The z coordinate of the tile input.</p>
            image_assets: <p>The particular assets or bands to tile.</p>
            target: <p>Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.</p>
            arn: <p>The Amazon Resource Name (ARN) of the tile operation.</p>
            image_mask: <p>Determines whether or not to return a valid data mask.</p>
            output_format: <p>The data format of the output tile. The formats include .npy, .png and .jpg.</p>
            time_range_filter: <p>Time range filter applied to imagery to find the images to tile.</p>
            property_filters: <p>Property filters for the imagery to tile.</p>
            output_data_type: <p>The output data type of the tile operation.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specify.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_tile_input.GetTileInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile.get_tile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.get_tile_output

            return capo_sagemaker_geospatial.types.get_tile_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTile", redact_output=_redact_output)
        )
        input_: capo_sagemaker_geospatial.types.get_tile_input.GetTileInput = {
            "x": x,
            "y": y,
            "z": z,
            "image_assets": image_assets,
            "target": target,
            "arn": arn,
        }
        if image_mask is not None:
            input_["image_mask"] = image_mask
        if output_format is not None:
            input_["output_format"] = output_format
        if time_range_filter is not None:
            input_["time_range_filter"] = time_range_filter
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if output_data_type is not None:
            input_["output_data_type"] = output_data_type
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def stop_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput":
        """<p>Use this operation to stop an existing earth observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>

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
            req: "OperationRequest[capo_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job.stop_earth_observation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopEarthObservationJob")
        )
        input_: capo_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput = {
            "arn": arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEarthObservationJob:
    def __init__(self, service: AsyncSageMakerGeospatialClient) -> None:
        self._service = service

    async def create(
        self,
        name: str,
        input_config: "capo_sagemaker_geospatial.types.input_config_input.InputConfigInput",
        job_config: "capo_sagemaker_geospatial.types.job_config_input.JobConfigInput",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        kms_key_id: Optional["capo_sagemaker_geospatial.types.kms_key.KmsKey"] = None,
        tags: Optional["capo_sagemaker_geospatial.types.tags.Tags"] = None,
    ) -> "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput":
        """<p>Use this operation to create an Earth observation job.</p>

        Args:
            name: <p>The name of the Earth Observation job.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            kms_key_id: <p>The Key Management Service key ID for server-side encryption.</p>
            input_config: <p>Input configuration information for the Earth Observation job.</p>
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
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.start_earth_observation_job.async_start_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.start_earth_observation_job_input

            return capo_sagemaker_geospatial.types.start_earth_observation_job_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.start_earth_observation_job_output.StartEarthObservationJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.start_earth_observation_job_output

            return capo_sagemaker_geospatial.types.start_earth_observation_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "StartEarthObservationJob",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_geospatial.types.start_earth_observation_job_input.StartEarthObservationJobInput = {
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
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput":
        """<p>Get the details for a previously initiated Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_earth_observation_job.async_get_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.get_earth_observation_job_output.GetEarthObservationJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.get_earth_observation_job_output

            return capo_sagemaker_geospatial.types.get_earth_observation_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetEarthObservationJob", redact_output=_redact_output),
        )
        input_: capo_sagemaker_geospatial.types.get_earth_observation_job_input.GetEarthObservationJobInput = {
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
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput":
        """<p>Use this operation to delete an Earth Observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being deleted.</p>

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
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.delete_earth_observation_job_output.DeleteEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.delete_earth_observation_job.async_delete_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteEarthObservationJob")
        )
        input_: capo_sagemaker_geospatial.types.delete_earth_observation_job_input.DeleteEarthObservationJobInput = {
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
        status_equals: Optional[
            "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
        ] = None,
        sort_order: Optional[
            "capo_sagemaker_geospatial.types.sort_order.SortOrder"
        ] = None,
        sort_by: Optional[str] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput":
        """<p>Use this operation to get a list of the Earth Observation jobs associated with the calling Amazon Web Services account.</p>

        Args:
            status_equals: <p>A filter that retrieves only jobs with a specific status.</p>
            sort_order: <p>An optional value that specifies whether you want the results sorted in <code>Ascending</code> or <code>Descending</code> order.</p>
            sort_by: <p>The parameter by which to sort the results.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_earth_observation_jobs.async_list_earth_observation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_earth_observation_job_input

            return capo_sagemaker_geospatial.types.list_earth_observation_job_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.list_earth_observation_job_output.ListEarthObservationJobOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.list_earth_observation_job_output

            return capo_sagemaker_geospatial.types.list_earth_observation_job_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListEarthObservationJobs",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_sagemaker_geospatial.types.list_earth_observation_job_input.ListEarthObservationJobInput = {}
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

    async def export_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        execution_role_arn: "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn",
        output_config: "capo_sagemaker_geospatial.types.output_config_input.OutputConfigInput",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        client_token: Optional[str] = None,
        export_source_images: Optional[bool] = None,
    ) -> "capo_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput":
        """<p>Use this operation to export results of an Earth Observation job and optionally source images used as input to the EOJ to an Amazon S3 location.</p>

        Args:
            arn: <p>The input Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>
            client_token: <p>A unique token that guarantees that the call to this API is idempotent.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>
            output_config: <p>An object containing information about the output file.</p>
            export_source_images: <p>The source images provided to the Earth Observation job being exported.</p>

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
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.export_earth_observation_job_output.ExportEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.export_earth_observation_job.async_export_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ExportEarthObservationJob")
        )
        input_: capo_sagemaker_geospatial.types.export_earth_observation_job_input.ExportEarthObservationJobInput = {
            "arn": arn,
            "execution_role_arn": execution_role_arn,
            "output_config": output_config,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if export_source_images is not None:
            input_["export_source_images"] = export_source_images

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def get_tile(
        self,
        x: int,
        y: int,
        z: int,
        image_assets: "capo_sagemaker_geospatial.types.string_list_input.StringListInput",
        target: "capo_sagemaker_geospatial.types.target_options.TargetOptions",
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        image_mask: Optional[bool] = None,
        output_format: Optional[str] = None,
        time_range_filter: Optional[str] = None,
        property_filters: Optional[str] = None,
        output_data_type: Optional[
            "capo_sagemaker_geospatial.types.output_type.OutputType"
        ] = None,
        execution_role_arn: Optional[
            "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
        ] = None,
    ) -> (
        "AsyncGenerator[capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput]"
    ):
        """<p>Gets a web mercator tile for the given Earth Observation job.</p>

        Args:
            x: <p>The x coordinate of the tile input.</p>
            y: <p>The y coordinate of the tile input.</p>
            z: <p>The z coordinate of the tile input.</p>
            image_assets: <p>The particular assets or bands to tile.</p>
            target: <p>Determines what part of the Earth Observation job to tile. 'INPUT' or 'OUTPUT' are the valid options.</p>
            arn: <p>The Amazon Resource Name (ARN) of the tile operation.</p>
            image_mask: <p>Determines whether or not to return a valid data mask.</p>
            output_format: <p>The data format of the output tile. The formats include .npy, .png and .jpg.</p>
            time_range_filter: <p>Time range filter applied to imagery to find the images to tile.</p>
            property_filters: <p>Property filters for the imagery to tile.</p>
            output_data_type: <p>The output data type of the tile operation.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that you specify.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.get_tile_input.GetTileInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_tile.async_get_tile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_sagemaker_geospatial.types.get_tile_output.GetTileOutput",
        ) -> dict[str, Any]:
            import capo_sagemaker_geospatial.types.get_tile_output

            return capo_sagemaker_geospatial.types.get_tile_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTile", redact_output=_redact_output)
        )
        input_: capo_sagemaker_geospatial.types.get_tile_input.GetTileInput = {
            "x": x,
            "y": y,
            "z": z,
            "image_assets": image_assets,
            "target": target,
            "arn": arn,
        }
        if image_mask is not None:
            input_["image_mask"] = image_mask
        if output_format is not None:
            input_["output_format"] = output_format
        if time_range_filter is not None:
            input_["time_range_filter"] = time_range_filter
        if property_filters is not None:
            input_["property_filters"] = property_filters
        if output_data_type is not None:
            input_["output_data_type"] = output_data_type
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def stop_earth_observation_job(
        self,
        arn: "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput":
        """<p>Use this operation to stop an existing earth observation job.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Earth Observation job being stopped.</p>

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
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.stop_earth_observation_job_output.StopEarthObservationJobOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.stop_earth_observation_job.async_stop_earth_observation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopEarthObservationJob")
        )
        input_: capo_sagemaker_geospatial.types.stop_earth_observation_job_input.StopEarthObservationJobInput = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
