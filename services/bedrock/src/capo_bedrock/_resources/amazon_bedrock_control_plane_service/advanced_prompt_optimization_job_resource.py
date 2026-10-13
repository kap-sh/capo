from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.advanced_prompt_optimization_input_config
    import capo_bedrock.types.advanced_prompt_optimization_job_description
    import capo_bedrock.types.advanced_prompt_optimization_job_identifier
    import capo_bedrock.types.advanced_prompt_optimization_job_identifiers
    import capo_bedrock.types.advanced_prompt_optimization_job_name
    import capo_bedrock.types.advanced_prompt_optimization_job_summary
    import capo_bedrock.types.advanced_prompt_optimization_output_config
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response
    import capo_bedrock.types.create_advanced_prompt_optimization_job_request
    import capo_bedrock.types.create_advanced_prompt_optimization_job_response
    import capo_bedrock.types.get_advanced_prompt_optimization_job_request
    import capo_bedrock.types.get_advanced_prompt_optimization_job_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.list_advanced_prompt_optimization_jobs_request
    import capo_bedrock.types.list_advanced_prompt_optimization_jobs_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_configurations
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.stop_advanced_prompt_optimization_job_request
    import capo_bedrock.types.stop_advanced_prompt_optimization_job_response
    import capo_bedrock.types.tag_list
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class AdvancedPromptOptimizationJobResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def batch_delete_advanced_prompt_optimization_job(
        self,
        job_identifiers: "capo_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse":
        """<p>Deletes one or more advanced prompt optimization jobs.</p>

        Args:
            job_identifiers: <p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job.batch_delete_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchDeleteAdvancedPromptOptimizationJob"),
        )
        input_: capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest = {
            "job_identifiers": job_identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_advanced_prompt_optimization_job(
        self,
        job_name: "capo_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName",
        input_config: "capo_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig",
        output_config: "capo_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig",
        model_configurations: "capo_bedrock.types.model_configurations.ModelConfigurations",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        job_description: Optional[
            "capo_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        encryption_key_arn: Optional["capo_bedrock.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse":
        """<p>Creates an advanced prompt optimization job. The job optimizes your prompt templates for specific models using your evaluation dataset and criteria.</p>

        Args:
            job_name: <p>A name for the advanced prompt optimization job.</p>
            job_description: <p>A description of the advanced prompt optimization job.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            input_config: <p>Specifies the S3 location of your JSONL input file containing prompt templates and evaluation samples.</p>
            output_config: <p>Specifies the S3 location where optimization results will be stored.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used for encrypting the output data. If not specified, the output is encrypted with an Amazon-owned KMS key.</p>
            tags: <p>Tags to associate with the advanced prompt optimization job.</p>
            model_configurations: <p>A list of model configurations specifying the target models for prompt optimization. You can specify up to 5 models.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job.create_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAdvancedPromptOptimizationJob")
        )
        input_: capo_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest = {
            "job_name": job_name,
            "input_config": input_config,
            "output_config": output_config,
            "model_configurations": model_configurations,
        }
        if job_description is not None:
            input_["job_description"] = job_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_advanced_prompt_optimization_job(
        self,
        job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse":
        """<p>Gets information about an advanced prompt optimization job.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job.get_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAdvancedPromptOptimizationJob")
        )
        input_: capo_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_advanced_prompt_optimization_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse":
        """<p>Lists the advanced prompt optimization jobs in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>
            sort_by: <p>The field to sort the results by.</p>
            sort_order: <p>The sort order for the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs.list_advanced_prompt_optimization_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAdvancedPromptOptimizationJobs")
        )
        input_: capo_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_advanced_prompt_optimization_job(
        self,
        job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse":
        """<p>Stops an advanced prompt optimization job that is in progress.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job to stop.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job.stop_advanced_prompt_optimization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopAdvancedPromptOptimizationJob")
        )
        input_: capo_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAdvancedPromptOptimizationJobResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def batch_delete_advanced_prompt_optimization_job(
        self,
        job_identifiers: "capo_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse":
        """<p>Deletes one or more advanced prompt optimization jobs.</p>

        Args:
            job_identifiers: <p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job.async_batch_delete_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("BatchDeleteAdvancedPromptOptimizationJob"),
        )
        input_: capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest = {
            "job_identifiers": job_identifiers
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_advanced_prompt_optimization_job(
        self,
        job_name: "capo_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName",
        input_config: "capo_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig",
        output_config: "capo_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig",
        model_configurations: "capo_bedrock.types.model_configurations.ModelConfigurations",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_description: Optional[
            "capo_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        encryption_key_arn: Optional["capo_bedrock.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse":
        """<p>Creates an advanced prompt optimization job. The job optimizes your prompt templates for specific models using your evaluation dataset and criteria.</p>

        Args:
            job_name: <p>A name for the advanced prompt optimization job.</p>
            job_description: <p>A description of the advanced prompt optimization job.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            input_config: <p>Specifies the S3 location of your JSONL input file containing prompt templates and evaluation samples.</p>
            output_config: <p>Specifies the S3 location where optimization results will be stored.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used for encrypting the output data. If not specified, the output is encrypted with an Amazon-owned KMS key.</p>
            tags: <p>Tags to associate with the advanced prompt optimization job.</p>
            model_configurations: <p>A list of model configurations specifying the target models for prompt optimization. You can specify up to 5 models.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job.async_create_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAdvancedPromptOptimizationJob")
        )
        input_: capo_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest = {
            "job_name": job_name,
            "input_config": input_config,
            "output_config": output_config,
            "model_configurations": model_configurations,
        }
        if job_description is not None:
            input_["job_description"] = job_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_advanced_prompt_optimization_job(
        self,
        job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse":
        """<p>Gets information about an advanced prompt optimization job.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job.async_get_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAdvancedPromptOptimizationJob")
        )
        input_: capo_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_advanced_prompt_optimization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse":
        """<p>Lists the advanced prompt optimization jobs in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>
            sort_by: <p>The field to sort the results by.</p>
            sort_order: <p>The sort order for the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs.async_list_advanced_prompt_optimization_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAdvancedPromptOptimizationJobs")
        )
        input_: capo_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_advanced_prompt_optimization_job(
        self,
        job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse":
        """<p>Stops an advanced prompt optimization job that is in progress.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job to stop.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job.async_stop_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StopAdvancedPromptOptimizationJob")
        )
        input_: capo_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
