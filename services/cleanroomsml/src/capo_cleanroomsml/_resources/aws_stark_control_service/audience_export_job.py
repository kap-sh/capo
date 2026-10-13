from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_cleanroomsml._auth._signers
import capo_cleanroomsml._auth._sigv4
from capo_cleanroomsml._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_export_job_summary
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_size
    import capo_cleanroomsml.types.list_audience_export_jobs_request
    import capo_cleanroomsml.types.list_audience_export_jobs_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.start_audience_export_job_request
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class AudienceExportJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        audience_size: "capo_cleanroomsml.types.audience_size.AudienceSize",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Export an audience of a specified size after you have generated an audience.</p>

        Args:
            name: <p>The name of the audience export job.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to export.</p>
            description: <p>The description of the audience export job.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job.start_audience_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartAudienceExportJob")
        )
        input_: capo_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest = {
            "name": name,
            "audience_generation_job_arn": audience_generation_job_arn,
            "audience_size": audience_size,
        }
        if description is not None:
            input_["description"] = description

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
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        audience_generation_job_arn: Optional[
            "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse":
        """<p>Returns a list of the audience export jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs.list_audience_export_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAudienceExportJobs")
        )
        input_: capo_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if audience_generation_job_arn is not None:
            input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAudienceExportJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        audience_size: "capo_cleanroomsml.types.audience_size.AudienceSize",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Export an audience of a specified size after you have generated an audience.</p>

        Args:
            name: <p>The name of the audience export job.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to export.</p>
            description: <p>The description of the audience export job.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_audience_export_job.async_start_audience_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartAudienceExportJob")
        )
        input_: capo_cleanroomsml.types.start_audience_export_job_request.StartAudienceExportJobRequest = {
            "name": name,
            "audience_generation_job_arn": audience_generation_job_arn,
            "audience_size": audience_size,
        }
        if description is not None:
            input_["description"] = description

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
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        audience_generation_job_arn: Optional[
            "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
        ] = None,
    ) -> "capo_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse":
        """<p>Returns a list of the audience export jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_audience_export_jobs_response.ListAudienceExportJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_audience_export_jobs.async_list_audience_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAudienceExportJobs")
        )
        input_: capo_cleanroomsml.types.list_audience_export_jobs_request.ListAudienceExportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if audience_generation_job_arn is not None:
            input_["audience_generation_job_arn"] = audience_generation_job_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
