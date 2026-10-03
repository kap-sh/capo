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
    import capo_bedrock.types.account_id
    import capo_bedrock.types.create_model_copy_job_request
    import capo_bedrock.types.create_model_copy_job_response
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.get_model_copy_job_request
    import capo_bedrock.types.get_model_copy_job_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_model_copy_jobs_request
    import capo_bedrock.types.list_model_copy_jobs_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_copy_job_arn
    import capo_bedrock.types.model_copy_job_status
    import capo_bedrock.types.model_copy_job_summary
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ModelCopyResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_model_copy_job(
        self,
        source_model_arn: "capo_bedrock.types.model_arn.ModelArn",
        target_model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        model_kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        target_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_model_copy_job_response.CreateModelCopyJobResponse":
        """<p>Copies a model to another region so that it can be used there. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            source_model_arn: <p>The Amazon Resource Name (ARN) of the model to be copied.</p>
            target_model_name: <p>A name for the copied model.</p>
            model_kms_key_id: <p>The ARN of the KMS key that you use to encrypt the model copy.</p>
            target_model_tags: <p>Tags to associate with the target model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tag resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_model_copy_job_request.CreateModelCopyJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_model_copy_job_response.CreateModelCopyJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_copy_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_copy_job.create_model_copy_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_copy_job_request.CreateModelCopyJobRequest = {
            "source_model_arn": source_model_arn,
            "target_model_name": target_model_name,
        }
        if model_kms_key_id is not None:
            input_["model_kms_key_id"] = model_kms_key_id
        if target_model_tags is not None:
            input_["target_model_tags"] = target_model_tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model_copy_job(
        self,
        job_arn: "capo_bedrock.types.model_copy_job_arn.ModelCopyJobArn",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_copy_job_response.GetModelCopyJobResponse":
        """<p>Retrieves information about a model copy job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_arn: <p>The Amazon Resource Name (ARN) of the model copy job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_model_copy_job_request.GetModelCopyJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_model_copy_job_response.GetModelCopyJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_copy_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_copy_job.get_model_copy_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_copy_job_request.GetModelCopyJobRequest = {
            "job_arn": job_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_model_copy_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
        ] = None,
        source_account_equals: Optional[
            "capo_bedrock.types.account_id.AccountId"
        ] = None,
        source_model_arn_equals: Optional[
            "capo_bedrock.types.model_arn.ModelArn"
        ] = None,
        target_model_name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_copy_jobs_response.ListModelCopyJobsResponse":
        """<p>Returns a list of model copy jobs that you have submitted. You can filter the jobs to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Filters for model copy jobs created after the specified time.</p>
            creation_time_before: <p>Filters for model copy jobs created before the specified time. </p>
            status_equals: <p>Filters for model copy jobs whose status matches the value that you specify.</p>
            source_account_equals: <p>Filters for model copy jobs in which the account that the source model belongs to is equal to the value that you specify.</p>
            source_model_arn_equals: <p>Filters for model copy jobs in which the Amazon Resource Name (ARN) of the source model to is equal to the value that you specify.</p>
            target_model_name_contains: <p>Filters for model copy jobs in which the name of the copied model contains the string that you specify.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of model copy jobs.</p>
            sort_order: <p>Specifies whether to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_model_copy_jobs_request.ListModelCopyJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_model_copy_jobs_response.ListModelCopyJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_copy_jobs

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_copy_jobs.list_model_copy_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_copy_jobs_request.ListModelCopyJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if source_account_equals is not None:
            input_["source_account_equals"] = source_account_equals
        if source_model_arn_equals is not None:
            input_["source_model_arn_equals"] = source_model_arn_equals
        if target_model_name_contains is not None:
            input_["target_model_name_contains"] = target_model_name_contains
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


class AsyncModelCopyResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_model_copy_job(
        self,
        source_model_arn: "capo_bedrock.types.model_arn.ModelArn",
        target_model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        model_kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        target_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_model_copy_job_response.CreateModelCopyJobResponse":
        """<p>Copies a model to another region so that it can be used there. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            source_model_arn: <p>The Amazon Resource Name (ARN) of the model to be copied.</p>
            target_model_name: <p>A name for the copied model.</p>
            model_kms_key_id: <p>The ARN of the KMS key that you use to encrypt the model copy.</p>
            target_model_tags: <p>Tags to associate with the target model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tag resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_copy_job_request.CreateModelCopyJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_copy_job_response.CreateModelCopyJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_copy_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_copy_job.async_create_model_copy_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_copy_job_request.CreateModelCopyJobRequest = {
            "source_model_arn": source_model_arn,
            "target_model_name": target_model_name,
        }
        if model_kms_key_id is not None:
            input_["model_kms_key_id"] = model_kms_key_id
        if target_model_tags is not None:
            input_["target_model_tags"] = target_model_tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_copy_job(
        self,
        job_arn: "capo_bedrock.types.model_copy_job_arn.ModelCopyJobArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_copy_job_response.GetModelCopyJobResponse":
        """<p>Retrieves information about a model copy job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_arn: <p>The Amazon Resource Name (ARN) of the model copy job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_copy_job_request.GetModelCopyJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_copy_job_response.GetModelCopyJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_copy_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_copy_job.async_get_model_copy_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_copy_job_request.GetModelCopyJobRequest = {
            "job_arn": job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_model_copy_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
        ] = None,
        source_account_equals: Optional[
            "capo_bedrock.types.account_id.AccountId"
        ] = None,
        source_model_arn_equals: Optional[
            "capo_bedrock.types.model_arn.ModelArn"
        ] = None,
        target_model_name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_copy_jobs_response.ListModelCopyJobsResponse":
        """<p>Returns a list of model copy jobs that you have submitted. You can filter the jobs to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Filters for model copy jobs created after the specified time.</p>
            creation_time_before: <p>Filters for model copy jobs created before the specified time. </p>
            status_equals: <p>Filters for model copy jobs whose status matches the value that you specify.</p>
            source_account_equals: <p>Filters for model copy jobs in which the account that the source model belongs to is equal to the value that you specify.</p>
            source_model_arn_equals: <p>Filters for model copy jobs in which the Amazon Resource Name (ARN) of the source model to is equal to the value that you specify.</p>
            target_model_name_contains: <p>Filters for model copy jobs in which the name of the copied model contains the string that you specify.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of model copy jobs.</p>
            sort_order: <p>Specifies whether to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_copy_jobs_request.ListModelCopyJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_copy_jobs_response.ListModelCopyJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_copy_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_copy_jobs.async_list_model_copy_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_copy_jobs_request.ListModelCopyJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if source_account_equals is not None:
            input_["source_account_equals"] = source_account_equals
        if source_model_arn_equals is not None:
            input_["source_model_arn_equals"] = source_model_arn_equals
        if target_model_name_contains is not None:
            input_["target_model_name_contains"] = target_model_name_contains
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
