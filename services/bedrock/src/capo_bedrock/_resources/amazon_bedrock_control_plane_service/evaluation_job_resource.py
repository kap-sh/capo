from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_bedrock.types.application_type
    import capo_bedrock.types.batch_delete_evaluation_job_request
    import capo_bedrock.types.batch_delete_evaluation_job_response
    import capo_bedrock.types.create_evaluation_job_request
    import capo_bedrock.types.create_evaluation_job_response
    import capo_bedrock.types.evaluation_config
    import capo_bedrock.types.evaluation_inference_config
    import capo_bedrock.types.evaluation_job_description
    import capo_bedrock.types.evaluation_job_identifier
    import capo_bedrock.types.evaluation_job_identifiers
    import capo_bedrock.types.evaluation_job_name
    import capo_bedrock.types.evaluation_job_status
    import capo_bedrock.types.evaluation_output_data_config
    import capo_bedrock.types.evaluation_summary
    import capo_bedrock.types.get_evaluation_job_request
    import capo_bedrock.types.get_evaluation_job_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_evaluation_jobs_request
    import capo_bedrock.types.list_evaluation_jobs_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.stop_evaluation_job_request
    import capo_bedrock.types.stop_evaluation_job_response
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class EvaluationJobResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def batch_delete_evaluation_job(
        self,
        job_identifiers: "capo_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse":
        """<p>Deletes a batch of evaluation jobs. An evaluation job can only be deleted if it has following status <code>FAILED</code>, <code>COMPLETED</code>, and <code>STOPPED</code>. You can request up to 25 model evaluation jobs be deleted in a single request.</p>

        Args:
            job_identifiers: <p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete evaluation jobs
            The following example shows a request to delete two model evaluation jobs, where one of the jobs is not found.

            >>> client.batch_delete_evaluation_job(job_identifiers=['arn:aws:bedrock:us-east-2:123456789012:evaluation-job/12rnxmplqv0v', 'arn:aws:bedrock:us-east-2:123456789012:evaluation-job/rispxmpl12rn'])
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job.batch_delete_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest = {
            "job_identifiers": job_identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_evaluation_job(
        self,
        job_name: "capo_bedrock.types.evaluation_job_name.EvaluationJobName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        evaluation_config: "capo_bedrock.types.evaluation_config.EvaluationConfig",
        inference_config: "capo_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig",
        output_data_config: "capo_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        job_description: Optional[
            "capo_bedrock.types.evaluation_job_description.EvaluationJobDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customer_encryption_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        application_type: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
    ) -> (
        "capo_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
    ):
        """<p>Creates an evaluation job.</p>

        Args:
            job_name: <p>A name for the evaluation job. Names must unique with your Amazon Web Services account, and your account's Amazon Web Services region.</p>
            job_description: <p>A description of the evaluation job.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html">Required permissions for model evaluations</a>.</p>
            customer_encryption_key_id: <p>Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.</p>
            job_tags: <p>Tags to attach to the model evaluation job.</p>
            application_type: <p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>
            evaluation_config: <p>Contains the configuration details of either an automated or human-based evaluation job.</p>
            inference_config: <p>Contains the configuration details of the inference model for the evaluation job.</p> <p>For model evaluation jobs, automated jobs support a single model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>, and jobs that use human workers support two models or inference profiles.</p>
            output_data_config: <p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job.create_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest = {
            "job_name": job_name,
            "role_arn": role_arn,
            "evaluation_config": evaluation_config,
            "inference_config": inference_config,
            "output_data_config": output_data_config,
        }
        if job_description is not None:
            input_["job_description"] = job_description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if customer_encryption_key_id is not None:
            input_["customer_encryption_key_id"] = customer_encryption_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if application_type is not None:
            input_["application_type"] = application_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_evaluation_job(
        self,
        job_identifier: "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse":
        """<p>Gets information about an evaluation job, such as the status of the job.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job.get_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_evaluation_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
        ] = None,
        application_type_equals: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
        name_contains: Optional[
            "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse":
        """<p>Lists all existing evaluation jobs.</p>

        Args:
            creation_time_after: <p>A filter to only list evaluation jobs created after a specified time.</p>
            creation_time_before: <p>A filter to only list evaluation jobs created before a specified time.</p>
            status_equals: <p>A filter to only list evaluation jobs that are of a certain status.</p>
            application_type_equals: <p>A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.</p>
            name_contains: <p>A filter to only list evaluation jobs that contain a specified string in the job name.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>
            sort_by: <p>Specifies a creation time to sort the list of evaluation jobs by when they were created.</p>
            sort_order: <p>Specifies whether to sort the list of evaluation jobs by either ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs.list_evaluation_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if application_type_equals is not None:
            input_["application_type_equals"] = application_type_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
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

    def stop_evaluation_job(
        self,
        job_identifier: "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse":
        """<p>Stops an evaluation job that is current being created or running.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>

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
            req: "OperationRequest[capo_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job.stop_evaluation_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncEvaluationJobResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def batch_delete_evaluation_job(
        self,
        job_identifiers: "capo_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse":
        """<p>Deletes a batch of evaluation jobs. An evaluation job can only be deleted if it has following status <code>FAILED</code>, <code>COMPLETED</code>, and <code>STOPPED</code>. You can request up to 25 model evaluation jobs be deleted in a single request.</p>

        Args:
            job_identifiers: <p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete evaluation jobs
            The following example shows a request to delete two model evaluation jobs, where one of the jobs is not found.

            >>> await client.batch_delete_evaluation_job(job_identifiers=['arn:aws:bedrock:us-east-2:123456789012:evaluation-job/12rnxmplqv0v', 'arn:aws:bedrock:us-east-2:123456789012:evaluation-job/rispxmpl12rn'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job.async_batch_delete_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest = {
            "job_identifiers": job_identifiers
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_evaluation_job(
        self,
        job_name: "capo_bedrock.types.evaluation_job_name.EvaluationJobName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        evaluation_config: "capo_bedrock.types.evaluation_config.EvaluationConfig",
        inference_config: "capo_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig",
        output_data_config: "capo_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_description: Optional[
            "capo_bedrock.types.evaluation_job_description.EvaluationJobDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customer_encryption_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        application_type: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
    ) -> (
        "capo_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
    ):
        """<p>Creates an evaluation job.</p>

        Args:
            job_name: <p>A name for the evaluation job. Names must unique with your Amazon Web Services account, and your account's Amazon Web Services region.</p>
            job_description: <p>A description of the evaluation job.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html">Required permissions for model evaluations</a>.</p>
            customer_encryption_key_id: <p>Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.</p>
            job_tags: <p>Tags to attach to the model evaluation job.</p>
            application_type: <p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>
            evaluation_config: <p>Contains the configuration details of either an automated or human-based evaluation job.</p>
            inference_config: <p>Contains the configuration details of the inference model for the evaluation job.</p> <p>For model evaluation jobs, automated jobs support a single model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>, and jobs that use human workers support two models or inference profiles.</p>
            output_data_config: <p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job.async_create_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest = {
            "job_name": job_name,
            "role_arn": role_arn,
            "evaluation_config": evaluation_config,
            "inference_config": inference_config,
            "output_data_config": output_data_config,
        }
        if job_description is not None:
            input_["job_description"] = job_description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if customer_encryption_key_id is not None:
            input_["customer_encryption_key_id"] = customer_encryption_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if application_type is not None:
            input_["application_type"] = application_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_evaluation_job(
        self,
        job_identifier: "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse":
        """<p>Gets information about an evaluation job, such as the status of the job.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job.async_get_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_evaluation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
        ] = None,
        application_type_equals: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
        name_contains: Optional[
            "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse":
        """<p>Lists all existing evaluation jobs.</p>

        Args:
            creation_time_after: <p>A filter to only list evaluation jobs created after a specified time.</p>
            creation_time_before: <p>A filter to only list evaluation jobs created before a specified time.</p>
            status_equals: <p>A filter to only list evaluation jobs that are of a certain status.</p>
            application_type_equals: <p>A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.</p>
            name_contains: <p>A filter to only list evaluation jobs that contain a specified string in the job name.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>
            sort_by: <p>Specifies a creation time to sort the list of evaluation jobs by when they were created.</p>
            sort_order: <p>Specifies whether to sort the list of evaluation jobs by either ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs.async_list_evaluation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if application_type_equals is not None:
            input_["application_type_equals"] = application_type_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
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

    async def stop_evaluation_job(
        self,
        job_identifier: "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse":
        """<p>Stops an evaluation job that is current being created or running.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job.async_stop_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
