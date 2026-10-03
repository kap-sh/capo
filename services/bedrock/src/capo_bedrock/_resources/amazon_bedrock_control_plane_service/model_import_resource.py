from __future__ import annotations

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
    import capo_bedrock.types.create_model_import_job_request
    import capo_bedrock.types.create_model_import_job_response
    import capo_bedrock.types.delete_imported_model_request
    import capo_bedrock.types.delete_imported_model_response
    import capo_bedrock.types.get_imported_model_request
    import capo_bedrock.types.get_imported_model_response
    import capo_bedrock.types.get_model_import_job_request
    import capo_bedrock.types.get_model_import_job_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.imported_model_identifier
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.imported_model_summary
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_imported_models_request
    import capo_bedrock.types.list_imported_models_response
    import capo_bedrock.types.list_model_import_jobs_request
    import capo_bedrock.types.list_model_import_jobs_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_data_source
    import capo_bedrock.types.model_import_job_identifier
    import capo_bedrock.types.model_import_job_status
    import capo_bedrock.types.model_import_job_summary
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_models_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.vpc_config
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class ModelImportResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_model_import_job(
        self,
        job_name: "capo_bedrock.types.job_name.JobName",
        imported_model_name: "capo_bedrock.types.imported_model_name.ImportedModelName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        model_data_source: "capo_bedrock.types.model_data_source.ModelDataSource",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        imported_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        imported_model_kms_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_bedrock.types.create_model_import_job_response.CreateModelImportJobResponse":
        """<p>Creates a model import job to import model that you have customized in other environments, such as Amazon SageMaker. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> </p>

        Args:
            job_name: <p>The name of the import job.</p>
            imported_model_name: <p>The name of the imported model.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the model import job.</p>
            model_data_source: <p>The data source for the imported model.</p>
            job_tags: <p>Tags to attach to this import job. </p>
            imported_model_tags: <p>Tags to attach to the imported model.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            vpc_config: <p>VPC configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for the import job.</p>
            imported_model_kms_key_id: <p>The imported model is encrypted at rest using this key.</p>

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
            req: "OperationRequest[capo_bedrock.types.create_model_import_job_request.CreateModelImportJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_model_import_job_response.CreateModelImportJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_import_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_import_job.create_model_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_import_job_request.CreateModelImportJobRequest = {
            "job_name": job_name,
            "imported_model_name": imported_model_name,
            "role_arn": role_arn,
            "model_data_source": model_data_source,
        }
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if imported_model_tags is not None:
            input_["imported_model_tags"] = imported_model_tags
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if imported_model_kms_key_id is not None:
            input_["imported_model_kms_key_id"] = imported_model_kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_imported_model(
        self,
        model_identifier: "capo_bedrock.types.imported_model_identifier.ImportedModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> (
        "capo_bedrock.types.delete_imported_model_response.DeleteImportedModelResponse"
    ):
        """<p>Deletes a custom model that you imported earlier. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>. </p>

        Args:
            model_identifier: <p>Name of the imported model to delete.</p>

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
            req: "OperationRequest[capo_bedrock.types.delete_imported_model_request.DeleteImportedModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_imported_model_response.DeleteImportedModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_imported_model

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_imported_model.delete_imported_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_imported_model_request.DeleteImportedModelRequest = {
            "model_identifier": model_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_imported_model(
        self,
        model_identifier: "capo_bedrock.types.imported_model_identifier.ImportedModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_imported_model_response.GetImportedModelResponse":
        """<p>Gets properties associated with a customized model you imported. </p>

        Args:
            model_identifier: <p>Name or Amazon Resource Name (ARN) of the imported model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_imported_model_request.GetImportedModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_imported_model_response.GetImportedModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_imported_model

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_imported_model.get_imported_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_imported_model_request.GetImportedModelRequest = {
            "model_identifier": model_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_model_import_job(
        self,
        job_identifier: "capo_bedrock.types.model_import_job_identifier.ModelImportJobIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_import_job_response.GetModelImportJobResponse":
        """<p>Retrieves the properties associated with import model job, including the status of the job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>The identifier of the import job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_model_import_job_request.GetModelImportJobRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_model_import_job_response.GetModelImportJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_import_job

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_import_job.get_model_import_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_import_job_request.GetModelImportJobRequest = {
            "job_identifier": job_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_imported_models(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.imported_model_name.ImportedModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_imported_models_response.ListImportedModelsResponse":
        """<p>Returns a list of models you've imported. You can filter the results to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_before: <p>Return imported models that created before the specified time.</p>
            creation_time_after: <p>Return imported models that were created after the specified time.</p>
            name_contains: <p>Return imported models only if the model name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of imported models.</p>
            sort_order: <p>Specifies whetehr to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_imported_models_request.ListImportedModelsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_imported_models_response.ListImportedModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_imported_models

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_imported_models.list_imported_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_imported_models_request.ListImportedModelsRequest = {}
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
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

    def list_model_import_jobs(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> (
        "capo_bedrock.types.list_model_import_jobs_response.ListModelImportJobsResponse"
    ):
        """<p>Returns a list of import jobs you've submitted. You can filter the results to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Return import jobs that were created after the specified time.</p>
            creation_time_before: <p>Return import jobs that were created before the specified time.</p>
            status_equals: <p>Return imported jobs with the specified status.</p>
            name_contains: <p>Return imported jobs only if the job name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of imported jobs.</p>
            sort_order: <p>Specifies whether to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_model_import_jobs_request.ListModelImportJobsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_model_import_jobs_response.ListModelImportJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_import_jobs

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_import_jobs.list_model_import_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_import_jobs_request.ListModelImportJobsRequest = {}
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


class AsyncModelImportResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_model_import_job(
        self,
        job_name: "capo_bedrock.types.job_name.JobName",
        imported_model_name: "capo_bedrock.types.imported_model_name.ImportedModelName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        model_data_source: "capo_bedrock.types.model_data_source.ModelDataSource",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        imported_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        imported_model_kms_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_bedrock.types.create_model_import_job_response.CreateModelImportJobResponse":
        """<p>Creates a model import job to import model that you have customized in other environments, such as Amazon SageMaker. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> </p>

        Args:
            job_name: <p>The name of the import job.</p>
            imported_model_name: <p>The name of the imported model.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the model import job.</p>
            model_data_source: <p>The data source for the imported model.</p>
            job_tags: <p>Tags to attach to this import job. </p>
            imported_model_tags: <p>Tags to attach to the imported model.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            vpc_config: <p>VPC configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for the import job.</p>
            imported_model_kms_key_id: <p>The imported model is encrypted at rest using this key.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_import_job_request.CreateModelImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_import_job_response.CreateModelImportJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_import_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_import_job.async_create_model_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_import_job_request.CreateModelImportJobRequest = {
            "job_name": job_name,
            "imported_model_name": imported_model_name,
            "role_arn": role_arn,
            "model_data_source": model_data_source,
        }
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if imported_model_tags is not None:
            input_["imported_model_tags"] = imported_model_tags
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if imported_model_kms_key_id is not None:
            input_["imported_model_kms_key_id"] = imported_model_kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_imported_model(
        self,
        model_identifier: "capo_bedrock.types.imported_model_identifier.ImportedModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> (
        "capo_bedrock.types.delete_imported_model_response.DeleteImportedModelResponse"
    ):
        """<p>Deletes a custom model that you imported earlier. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>. </p>

        Args:
            model_identifier: <p>Name of the imported model to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.delete_imported_model_request.DeleteImportedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_imported_model_response.DeleteImportedModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_imported_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_imported_model.async_delete_imported_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_imported_model_request.DeleteImportedModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_imported_model(
        self,
        model_identifier: "capo_bedrock.types.imported_model_identifier.ImportedModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_imported_model_response.GetImportedModelResponse":
        """<p>Gets properties associated with a customized model you imported. </p>

        Args:
            model_identifier: <p>Name or Amazon Resource Name (ARN) of the imported model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_imported_model_request.GetImportedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_imported_model_response.GetImportedModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_imported_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_imported_model.async_get_imported_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_imported_model_request.GetImportedModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_import_job(
        self,
        job_identifier: "capo_bedrock.types.model_import_job_identifier.ModelImportJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_import_job_response.GetModelImportJobResponse":
        """<p>Retrieves the properties associated with import model job, including the status of the job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>The identifier of the import job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_import_job_request.GetModelImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_import_job_response.GetModelImportJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_import_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_import_job.async_get_model_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_import_job_request.GetModelImportJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_imported_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.imported_model_name.ImportedModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_imported_models_response.ListImportedModelsResponse":
        """<p>Returns a list of models you've imported. You can filter the results to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_before: <p>Return imported models that created before the specified time.</p>
            creation_time_after: <p>Return imported models that were created after the specified time.</p>
            name_contains: <p>Return imported models only if the model name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of imported models.</p>
            sort_order: <p>Specifies whetehr to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_imported_models_request.ListImportedModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_imported_models_response.ListImportedModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_imported_models

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_imported_models.async_list_imported_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_imported_models_request.ListImportedModelsRequest = {}
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
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

    async def list_model_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> (
        "capo_bedrock.types.list_model_import_jobs_response.ListModelImportJobsResponse"
    ):
        """<p>Returns a list of import jobs you've submitted. You can filter the results to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Return import jobs that were created after the specified time.</p>
            creation_time_before: <p>Return import jobs that were created before the specified time.</p>
            status_equals: <p>Return imported jobs with the specified status.</p>
            name_contains: <p>Return imported jobs only if the job name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of imported jobs.</p>
            sort_order: <p>Specifies whether to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_import_jobs_request.ListModelImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_import_jobs_response.ListModelImportJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_import_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_import_jobs.async_list_model_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_import_jobs_request.ListModelImportJobsRequest = {}
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
