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
    import capo_bedrock.types.base_model_identifier
    import capo_bedrock.types.create_model_customization_job_request
    import capo_bedrock.types.create_model_customization_job_response
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.customization_config
    import capo_bedrock.types.customization_type
    import capo_bedrock.types.fine_tuning_job_status
    import capo_bedrock.types.get_model_customization_job_request
    import capo_bedrock.types.get_model_customization_job_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_model_customization_jobs_request
    import capo_bedrock.types.list_model_customization_jobs_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_customization_hyper_parameters
    import capo_bedrock.types.model_customization_job_identifier
    import capo_bedrock.types.model_customization_job_summary
    import capo_bedrock.types.output_data_config
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.stop_model_customization_job_request
    import capo_bedrock.types.stop_model_customization_job_response
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.training_data_config
    import capo_bedrock.types.validation_data_config
    import capo_bedrock.types.vpc_config
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class TrainingResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_model_customization_job(
        self,
        job_name: "capo_bedrock.types.job_name.JobName",
        custom_model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        base_model_identifier: "capo_bedrock.types.base_model_identifier.BaseModelIdentifier",
        training_data_config: "capo_bedrock.types.training_data_config.TrainingDataConfig",
        output_data_config: "capo_bedrock.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customization_type: Optional[
            "capo_bedrock.types.customization_type.CustomizationType"
        ] = None,
        custom_model_kms_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        custom_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        validation_data_config: Optional[
            "capo_bedrock.types.validation_data_config.ValidationDataConfig"
        ] = None,
        hyper_parameters: Optional[
            "capo_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        customization_config: Optional[
            "capo_bedrock.types.customization_config.CustomizationConfig"
        ] = None,
    ) -> "capo_bedrock.types.create_model_customization_job_response.CreateModelCustomizationJobResponse":
        """<p>Creates a fine-tuning job to customize a base model.</p> <p>You specify the base foundation model and the location of the training data. After the model-customization job completes successfully, your custom model resource will be ready to use. Amazon Bedrock returns validation loss metrics and output generations after the job completes. </p> <p>For information on the format of training and validation data, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html">Prepare the datasets</a>.</p> <p> Model-customization jobs are asynchronous and the completion time depends on the base model and the training/validation data size. To monitor a job, use the <code>GetModelCustomizationJob</code> operation to retrieve the job status.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_name: <p>A name for the fine-tuning job.</p>
            custom_model_name: <p>A name for the resulting custom model.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. For example, during model training, Amazon Bedrock needs your permission to read input data from an S3 bucket, write model artifacts to an S3 bucket. To pass this role to Amazon Bedrock, the caller of this API must have the <code>iam:PassRole</code> permission. </p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            base_model_identifier: <p>Name of the base model.</p>
            customization_type: <p>The customization type.</p>
            custom_model_kms_key_id: <p>The custom model is encrypted at rest using this key.</p>
            job_tags: <p>Tags to attach to the job.</p>
            custom_model_tags: <p>Tags to attach to the resulting custom model.</p>
            training_data_config: <p>Information about the training dataset.</p>
            validation_data_config: <p>Information about the validation dataset. </p>
            output_data_config: <p>S3 location for the output data.</p>
            hyper_parameters: <p>Parameters related to tuning the model. For details on the format for different models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html">Custom model hyperparameters</a>.</p>
            vpc_config: <p>The configuration of the Virtual Private Cloud (VPC) that contains the resources that you're using for this job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-model-customization.html">Protect your model customization jobs using a VPC</a>.</p>
            customization_config: <p>The customization configuration for the model customization job.</p>

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
            req: "OperationRequest[capo_bedrock.types.create_model_customization_job_request.CreateModelCustomizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_model_customization_job_response.CreateModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_customization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_customization_job.create_model_customization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_customization_job_request.CreateModelCustomizationJobRequest = {
            "job_name": job_name,
            "custom_model_name": custom_model_name,
            "role_arn": role_arn,
            "base_model_identifier": base_model_identifier,
            "training_data_config": training_data_config,
            "output_data_config": output_data_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if customization_type is not None:
            input_["customization_type"] = customization_type
        if custom_model_kms_key_id is not None:
            input_["custom_model_kms_key_id"] = custom_model_kms_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if custom_model_tags is not None:
            input_["custom_model_tags"] = custom_model_tags
        if validation_data_config is not None:
            input_["validation_data_config"] = validation_data_config
        if hyper_parameters is not None:
            input_["hyper_parameters"] = hyper_parameters
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if customization_config is not None:
            input_["customization_config"] = customization_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model_customization_job(
        self,
        job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_customization_job_response.GetModelCustomizationJobResponse":
        """<p>Retrieves the properties associated with a model-customization job, including the status of the job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>Identifier for the customization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_model_customization_job_request.GetModelCustomizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_model_customization_job_response.GetModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_customization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_customization_job.get_model_customization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_customization_job_request.GetModelCustomizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_model_customization_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.fine_tuning_job_status.FineTuningJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_customization_jobs_response.ListModelCustomizationJobsResponse":
        """<p>Returns a list of model customization jobs that you have submitted. You can filter the jobs to return based on one or more criteria.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Return customization jobs created after the specified time. </p>
            creation_time_before: <p>Return customization jobs created before the specified time. </p>
            status_equals: <p>Return customization jobs with the specified status. </p>
            name_contains: <p>Return customization jobs only if the job name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of jobs.</p>
            sort_order: <p>The sort order of the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_model_customization_jobs_request.ListModelCustomizationJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_model_customization_jobs_response.ListModelCustomizationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_customization_jobs

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_customization_jobs.list_model_customization_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_customization_jobs_request.ListModelCustomizationJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
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

    def stop_model_customization_job(
        self,
        job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_model_customization_job_response.StopModelCustomizationJobResponse":
        """<p>Stops an active model customization job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>Job identifier of the job to stop.</p>

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
            req: "OperationRequest[capo_bedrock.types.stop_model_customization_job_request.StopModelCustomizationJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.stop_model_customization_job_response.StopModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_customization_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_customization_job.stop_model_customization_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_model_customization_job_request.StopModelCustomizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTrainingResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_model_customization_job(
        self,
        job_name: "capo_bedrock.types.job_name.JobName",
        custom_model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        base_model_identifier: "capo_bedrock.types.base_model_identifier.BaseModelIdentifier",
        training_data_config: "capo_bedrock.types.training_data_config.TrainingDataConfig",
        output_data_config: "capo_bedrock.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customization_type: Optional[
            "capo_bedrock.types.customization_type.CustomizationType"
        ] = None,
        custom_model_kms_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        custom_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        validation_data_config: Optional[
            "capo_bedrock.types.validation_data_config.ValidationDataConfig"
        ] = None,
        hyper_parameters: Optional[
            "capo_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        customization_config: Optional[
            "capo_bedrock.types.customization_config.CustomizationConfig"
        ] = None,
    ) -> "capo_bedrock.types.create_model_customization_job_response.CreateModelCustomizationJobResponse":
        """<p>Creates a fine-tuning job to customize a base model.</p> <p>You specify the base foundation model and the location of the training data. After the model-customization job completes successfully, your custom model resource will be ready to use. Amazon Bedrock returns validation loss metrics and output generations after the job completes. </p> <p>For information on the format of training and validation data, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html">Prepare the datasets</a>.</p> <p> Model-customization jobs are asynchronous and the completion time depends on the base model and the training/validation data size. To monitor a job, use the <code>GetModelCustomizationJob</code> operation to retrieve the job status.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_name: <p>A name for the fine-tuning job.</p>
            custom_model_name: <p>A name for the resulting custom model.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. For example, during model training, Amazon Bedrock needs your permission to read input data from an S3 bucket, write model artifacts to an S3 bucket. To pass this role to Amazon Bedrock, the caller of this API must have the <code>iam:PassRole</code> permission. </p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            base_model_identifier: <p>Name of the base model.</p>
            customization_type: <p>The customization type.</p>
            custom_model_kms_key_id: <p>The custom model is encrypted at rest using this key.</p>
            job_tags: <p>Tags to attach to the job.</p>
            custom_model_tags: <p>Tags to attach to the resulting custom model.</p>
            training_data_config: <p>Information about the training dataset.</p>
            validation_data_config: <p>Information about the validation dataset. </p>
            output_data_config: <p>S3 location for the output data.</p>
            hyper_parameters: <p>Parameters related to tuning the model. For details on the format for different models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html">Custom model hyperparameters</a>.</p>
            vpc_config: <p>The configuration of the Virtual Private Cloud (VPC) that contains the resources that you're using for this job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-model-customization.html">Protect your model customization jobs using a VPC</a>.</p>
            customization_config: <p>The customization configuration for the model customization job.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_customization_job_request.CreateModelCustomizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_customization_job_response.CreateModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_customization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_customization_job.async_create_model_customization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_customization_job_request.CreateModelCustomizationJobRequest = {
            "job_name": job_name,
            "custom_model_name": custom_model_name,
            "role_arn": role_arn,
            "base_model_identifier": base_model_identifier,
            "training_data_config": training_data_config,
            "output_data_config": output_data_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if customization_type is not None:
            input_["customization_type"] = customization_type
        if custom_model_kms_key_id is not None:
            input_["custom_model_kms_key_id"] = custom_model_kms_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if custom_model_tags is not None:
            input_["custom_model_tags"] = custom_model_tags
        if validation_data_config is not None:
            input_["validation_data_config"] = validation_data_config
        if hyper_parameters is not None:
            input_["hyper_parameters"] = hyper_parameters
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if customization_config is not None:
            input_["customization_config"] = customization_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_customization_job(
        self,
        job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_customization_job_response.GetModelCustomizationJobResponse":
        """<p>Retrieves the properties associated with a model-customization job, including the status of the job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>Identifier for the customization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_customization_job_request.GetModelCustomizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_customization_job_response.GetModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_customization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_customization_job.async_get_model_customization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_customization_job_request.GetModelCustomizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_model_customization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.fine_tuning_job_status.FineTuningJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_customization_jobs_response.ListModelCustomizationJobsResponse":
        """<p>Returns a list of model customization jobs that you have submitted. You can filter the jobs to return based on one or more criteria.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Return customization jobs created after the specified time. </p>
            creation_time_before: <p>Return customization jobs created before the specified time. </p>
            status_equals: <p>Return customization jobs with the specified status. </p>
            name_contains: <p>Return customization jobs only if the job name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of jobs.</p>
            sort_order: <p>The sort order of the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_customization_jobs_request.ListModelCustomizationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_customization_jobs_response.ListModelCustomizationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_customization_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_customization_jobs.async_list_model_customization_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_customization_jobs_request.ListModelCustomizationJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
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

    async def stop_model_customization_job(
        self,
        job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_model_customization_job_response.StopModelCustomizationJobResponse":
        """<p>Stops an active model customization job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>Job identifier of the job to stop.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.stop_model_customization_job_request.StopModelCustomizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_model_customization_job_response.StopModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_customization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_customization_job.async_stop_model_customization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_model_customization_job_request.StopModelCustomizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
