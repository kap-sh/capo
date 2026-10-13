from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

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
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_generation_job_data_source
    import capo_cleanroomsml.types.audience_generation_job_summary
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.delete_audience_generation_job_request
    import capo_cleanroomsml.types.get_audience_generation_job_request
    import capo_cleanroomsml.types.get_audience_generation_job_response
    import capo_cleanroomsml.types.list_audience_generation_jobs_request
    import capo_cleanroomsml.types.list_audience_generation_jobs_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.start_audience_generation_job_request
    import capo_cleanroomsml.types.start_audience_generation_job_response
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class AudienceGenerationJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        seed_audience: "capo_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        include_seed_in_output: Optional[bool] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse":
        """<p>Information necessary to start the audience generation job.</p>

        Args:
            name: <p>The name of the audience generation job.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.</p>
            seed_audience: <p>The seed audience that is used to generate the audience.</p>
            include_seed_in_output: <p>Whether the seed audience is included in the audience generation output.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation job.</p>
            description: <p>The description of the audience generation job.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>

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
            req: "OperationRequest[capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job.start_audience_generation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.start_audience_generation_job_request

            return capo_cleanroomsml.types.start_audience_generation_job_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartAudienceGenerationJob", redact_input=_redact_input),
        )
        input_: capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest = {
            "name": name,
            "configured_audience_model_arn": configured_audience_model_arn,
            "seed_audience": seed_audience,
        }
        if include_seed_in_output is not None:
            input_["include_seed_in_output"] = include_seed_in_output
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id
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

    def read(
        self,
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse":
        """<p>Returns information about an audience generation job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job.get_audience_generation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.get_audience_generation_job_response

            return capo_cleanroomsml.types.get_audience_generation_job_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAudienceGenerationJob", redact_output=_redact_output),
        )
        input_: capo_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest = {
            "audience_generation_job_arn": audience_generation_job_arn
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
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified audience generation job, and removes all data associated with the job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job.delete_audience_generation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAudienceGenerationJob")
        )
        input_: capo_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest = {
            "audience_generation_job_arn": audience_generation_job_arn
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
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        configured_audience_model_arn: Optional[
            "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
        ] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "capo_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse":
        """<p>Returns a list of audience generation jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation jobs that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs.list_audience_generation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAudienceGenerationJobs")
        )
        input_: capo_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if configured_audience_model_arn is not None:
            input_["configured_audience_model_arn"] = configured_audience_model_arn
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAudienceGenerationJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        seed_audience: "capo_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        include_seed_in_output: Optional[bool] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
    ) -> "capo_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse":
        """<p>Information necessary to start the audience generation job.</p>

        Args:
            name: <p>The name of the audience generation job.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.</p>
            seed_audience: <p>The seed audience that is used to generate the audience.</p>
            include_seed_in_output: <p>Whether the seed audience is included in the audience generation output.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation job.</p>
            description: <p>The description of the audience generation job.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>

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
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.start_audience_generation_job_response.StartAudienceGenerationJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_audience_generation_job.async_start_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.start_audience_generation_job_request

            return capo_cleanroomsml.types.start_audience_generation_job_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("StartAudienceGenerationJob", redact_input=_redact_input),
        )
        input_: capo_cleanroomsml.types.start_audience_generation_job_request.StartAudienceGenerationJobRequest = {
            "name": name,
            "configured_audience_model_arn": configured_audience_model_arn,
            "seed_audience": seed_audience,
        }
        if include_seed_in_output is not None:
            input_["include_seed_in_output"] = include_seed_in_output
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id
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

    async def read(
        self,
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse":
        """<p>Returns information about an audience generation job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_audience_generation_job.async_get_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanroomsml.types.get_audience_generation_job_response.GetAudienceGenerationJobResponse",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.get_audience_generation_job_response

            return capo_cleanroomsml.types.get_audience_generation_job_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetAudienceGenerationJob", redact_output=_redact_output),
        )
        input_: capo_cleanroomsml.types.get_audience_generation_job_request.GetAudienceGenerationJobRequest = {
            "audience_generation_job_arn": audience_generation_job_arn
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
        audience_generation_job_arn: "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified audience generation job, and removes all data associated with the job.</p>

        Args:
            audience_generation_job_arn: <p>The Amazon Resource Name (ARN) of the audience generation job that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_generation_job.async_delete_audience_generation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAudienceGenerationJob")
        )
        input_: capo_cleanroomsml.types.delete_audience_generation_job_request.DeleteAudienceGenerationJobRequest = {
            "audience_generation_job_arn": audience_generation_job_arn
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
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
        configured_audience_model_arn: Optional[
            "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
        ] = None,
        collaboration_id: Optional["capo_cleanroomsml.types.uuid.UUID"] = None,
    ) -> "capo_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse":
        """<p>Returns a list of audience generation jobs.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that was used for the audience generation jobs that you are interested in.</p>
            collaboration_id: <p>The identifier of the collaboration that contains the audience generation jobs that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_audience_generation_jobs_response.ListAudienceGenerationJobsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_audience_generation_jobs.async_list_audience_generation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAudienceGenerationJobs")
        )
        input_: capo_cleanroomsml.types.list_audience_generation_jobs_request.ListAudienceGenerationJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if configured_audience_model_arn is not None:
            input_["configured_audience_model_arn"] = configured_audience_model_arn
        if collaboration_id is not None:
            input_["collaboration_id"] = collaboration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
