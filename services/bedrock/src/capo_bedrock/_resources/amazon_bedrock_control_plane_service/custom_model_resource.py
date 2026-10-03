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
    import capo_bedrock.types.create_custom_model_request
    import capo_bedrock.types.create_custom_model_response
    import capo_bedrock.types.custom_model_data_source
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.custom_model_summary
    import capo_bedrock.types.delete_custom_model_request
    import capo_bedrock.types.delete_custom_model_response
    import capo_bedrock.types.foundation_model_arn
    import capo_bedrock.types.get_custom_model_request
    import capo_bedrock.types.get_custom_model_response
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.list_custom_models_request
    import capo_bedrock.types.list_custom_models_response
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_data_source
    import capo_bedrock.types.model_identifier
    import capo_bedrock.types.model_status
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.sort_models_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.timestamp
    from capo_bedrock._services.async_bedrock import (
        AsyncBedrockClient,
        AsyncBedrockClientConfig,
    )
    from capo_bedrock._services.bedrock import BedrockClient, BedrockClientConfig


class CustomModelResource:
    def __init__(self, service: BedrockClient) -> None:
        self._service = service

    def create_custom_model(
        self,
        model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        model_source_config: Optional[
            "capo_bedrock.types.model_data_source.ModelDataSource"
        ] = None,
        custom_model_data_source: Optional[
            "capo_bedrock.types.custom_model_data_source.CustomModelDataSource"
        ] = None,
        model_kms_key_arn: Optional["capo_bedrock.types.kms_key_arn.KmsKeyArn"] = None,
        role_arn: Optional["capo_bedrock.types.role_arn.RoleArn"] = None,
        model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_custom_model_response.CreateCustomModelResponse":
        """<p>Creates a new custom model in Amazon Bedrock. After the model is active, you can use it for inference.</p> <p>You can provide the model data source in one of the following ways:</p> <ul> <li> <p> <code>customModelDataSource</code> — Specify a SageMaker AI model package ARN. Amazon Bedrock resolves the model package to retrieve the model artifacts. This is the preferred method for new SageMaker AI training outputs.</p> </li> <li> <p> <code>modelSourceConfig</code> — Specify an Amazon S3 URI pointing to the Amazon-managed Amazon S3 bucket containing your model artifacts.</p> </li> </ul> <p>To use the model for inference, you must purchase Provisioned Throughput for it. You can't use On-demand inference with these custom models. For more information about Provisioned Throughput, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a>.</p> <p>The model appears in <code>ListCustomModels</code> with a <code>customizationType</code> of <code>imported</code>. To track the status of the new model, you use the <code>GetCustomModel</code> API operation. The model can be in the following states:</p> <ul> <li> <p> <code>Creating</code> - Initial state during validation and registration</p> </li> <li> <p> <code>Active</code> - Model is ready for use in inference</p> </li> <li> <p> <code>Failed</code> - Creation process encountered an error</p> </li> </ul> <p> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html">GetCustomModel</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModels.html">ListCustomModels</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModel.html">DeleteCustomModel</a> </p> </li> </ul>

        Args:
            model_name: <p>A unique name for the custom model.</p>
            model_source_config: <p>The data source for the model. The Amazon S3 URI in the model source must be for the Amazon-managed Amazon S3 bucket containing your model artifacts.</p>
            custom_model_data_source: <p>The data source for the custom model. Use this field to specify a SageMaker AI model package ARN as the source for your custom model. Amazon Bedrock resolves the model package to retrieve the model artifacts.</p> <p>You can specify either <code>customModelDataSource</code> or <code>modelSourceConfig</code>, but not both.</p>
            model_kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer managed KMS key to encrypt the custom model. If you don't provide a KMS key, Amazon Bedrock uses an Amazon Web Services-managed KMS key to encrypt the model. </p> <p>If you provide a customer managed KMS key, your Amazon Bedrock service role must have permissions to use it. For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-import-model.html">Encryption of imported models</a>. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock assumes to perform tasks on your behalf. This role must have permissions to access the Amazon S3 bucket containing your model artifacts and the KMS key (if specified). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html">Setting up an IAM service role for importing models</a> in the Amazon Bedrock User Guide.</p> <p>This field is required when you use <code>modelSourceConfig</code> with an Amazon S3 data source. It is not required when you use <code>customModelDataSource</code> with a model package ARN, because Amazon Bedrock uses its own credentials to access the model artifacts.</p>
            model_tags: <p>A list of key-value pairs to associate with the custom model resource. You can use these tags to organize and identify your resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

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

        Examples:
            Successful CreateCustomModel API call

            >>> client.create_custom_model(model_name='SampleModel', model_source_config={'s3DataSource': {'s3Uri': 's3://my-bucket/folder'}}, role_arn='arn:aws:iam::123456789012:role/SampleRole', model_kms_key_arn='arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab', model_tags=[{'key': 'foo', 'value': 'foo'}, {'key': 'foo', 'value': 'foo'}], client_request_token='foo')
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.create_custom_model_request.CreateCustomModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.create_custom_model_response.CreateCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model.create_custom_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_custom_model_request.CreateCustomModelRequest = {
            "model_name": model_name
        }
        if model_source_config is not None:
            input_["model_source_config"] = model_source_config
        if custom_model_data_source is not None:
            input_["custom_model_data_source"] = custom_model_data_source
        if model_kms_key_arn is not None:
            input_["model_kms_key_arn"] = model_kms_key_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if model_tags is not None:
            input_["model_tags"] = model_tags
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

    def delete_custom_model(
        self,
        model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_custom_model_response.DeleteCustomModelResponse":
        """<p>Deletes a custom model that you created earlier. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            model_identifier: <p>Name of the model to delete.</p>

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
            req: "OperationRequest[capo_bedrock.types.delete_custom_model_request.DeleteCustomModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.delete_custom_model_response.DeleteCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model.delete_custom_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_custom_model_request.DeleteCustomModelRequest = {
            "model_identifier": model_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_custom_model(
        self,
        model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_custom_model_response.GetCustomModelResponse":
        """<p>Get the properties associated with a Amazon Bedrock custom model that you have created. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            model_identifier: <p>Name or Amazon Resource Name (ARN) of the custom model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.get_custom_model_request.GetCustomModelRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.get_custom_model_response.GetCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model.get_custom_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_custom_model_request.GetCustomModelRequest = {
            "model_identifier": model_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_custom_models(
        self,
        *,
        config_overrides: Optional[BedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        base_model_arn_equals: Optional["capo_bedrock.types.model_arn.ModelArn"] = None,
        foundation_model_arn_equals: Optional[
            "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        is_owned: Optional[bool] = None,
        model_status: Optional["capo_bedrock.types.model_status.ModelStatus"] = None,
    ) -> "capo_bedrock.types.list_custom_models_response.ListCustomModelsResponse":
        """<p>Returns a list of the custom models that you have created with the <code>CreateModelCustomizationJob</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_before: <p>Return custom models created before the specified time. </p>
            creation_time_after: <p>Return custom models created after the specified time. </p>
            name_contains: <p>Return custom models only if the job name contains these characters.</p>
            base_model_arn_equals: <p>Return custom models only if the base model Amazon Resource Name (ARN) matches this parameter.</p>
            foundation_model_arn_equals: <p>Return custom models only if the foundation model Amazon Resource Name (ARN) matches this parameter.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of models.</p>
            sort_order: <p>The sort order of the results.</p>
            is_owned: <p>Return custom models depending on if the current account owns them (<code>true</code>) or if they were shared with the current account (<code>false</code>).</p>
            model_status: <p>The status of them model to filter results by. Possible values include:</p> <ul> <li> <p> <code>Creating</code> - Include only models that are currently being created and validated.</p> </li> <li> <p> <code>Active</code> - Include only models that have been successfully created and are ready for use.</p> </li> <li> <p> <code>Failed</code> - Include only models where the creation process failed.</p> </li> </ul> <p>If you don't specify a status, the API returns models in all states.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock.types.list_custom_models_request.ListCustomModelsRequest]",
        ) -> OperationResponse[
            "capo_bedrock.types.list_custom_models_response.ListCustomModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_models

            output, http_response = (
                capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_models.list_custom_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_custom_models_request.ListCustomModelsRequest = {}
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if base_model_arn_equals is not None:
            input_["base_model_arn_equals"] = base_model_arn_equals
        if foundation_model_arn_equals is not None:
            input_["foundation_model_arn_equals"] = foundation_model_arn_equals
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if is_owned is not None:
            input_["is_owned"] = is_owned
        if model_status is not None:
            input_["model_status"] = model_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncCustomModelResource:
    def __init__(self, service: AsyncBedrockClient) -> None:
        self._service = service

    async def create_custom_model(
        self,
        model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        model_source_config: Optional[
            "capo_bedrock.types.model_data_source.ModelDataSource"
        ] = None,
        custom_model_data_source: Optional[
            "capo_bedrock.types.custom_model_data_source.CustomModelDataSource"
        ] = None,
        model_kms_key_arn: Optional["capo_bedrock.types.kms_key_arn.KmsKeyArn"] = None,
        role_arn: Optional["capo_bedrock.types.role_arn.RoleArn"] = None,
        model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_custom_model_response.CreateCustomModelResponse":
        """<p>Creates a new custom model in Amazon Bedrock. After the model is active, you can use it for inference.</p> <p>You can provide the model data source in one of the following ways:</p> <ul> <li> <p> <code>customModelDataSource</code> — Specify a SageMaker AI model package ARN. Amazon Bedrock resolves the model package to retrieve the model artifacts. This is the preferred method for new SageMaker AI training outputs.</p> </li> <li> <p> <code>modelSourceConfig</code> — Specify an Amazon S3 URI pointing to the Amazon-managed Amazon S3 bucket containing your model artifacts.</p> </li> </ul> <p>To use the model for inference, you must purchase Provisioned Throughput for it. You can't use On-demand inference with these custom models. For more information about Provisioned Throughput, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a>.</p> <p>The model appears in <code>ListCustomModels</code> with a <code>customizationType</code> of <code>imported</code>. To track the status of the new model, you use the <code>GetCustomModel</code> API operation. The model can be in the following states:</p> <ul> <li> <p> <code>Creating</code> - Initial state during validation and registration</p> </li> <li> <p> <code>Active</code> - Model is ready for use in inference</p> </li> <li> <p> <code>Failed</code> - Creation process encountered an error</p> </li> </ul> <p> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html">GetCustomModel</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModels.html">ListCustomModels</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModel.html">DeleteCustomModel</a> </p> </li> </ul>

        Args:
            model_name: <p>A unique name for the custom model.</p>
            model_source_config: <p>The data source for the model. The Amazon S3 URI in the model source must be for the Amazon-managed Amazon S3 bucket containing your model artifacts.</p>
            custom_model_data_source: <p>The data source for the custom model. Use this field to specify a SageMaker AI model package ARN as the source for your custom model. Amazon Bedrock resolves the model package to retrieve the model artifacts.</p> <p>You can specify either <code>customModelDataSource</code> or <code>modelSourceConfig</code>, but not both.</p>
            model_kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer managed KMS key to encrypt the custom model. If you don't provide a KMS key, Amazon Bedrock uses an Amazon Web Services-managed KMS key to encrypt the model. </p> <p>If you provide a customer managed KMS key, your Amazon Bedrock service role must have permissions to use it. For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-import-model.html">Encryption of imported models</a>. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock assumes to perform tasks on your behalf. This role must have permissions to access the Amazon S3 bucket containing your model artifacts and the KMS key (if specified). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html">Setting up an IAM service role for importing models</a> in the Amazon Bedrock User Guide.</p> <p>This field is required when you use <code>modelSourceConfig</code> with an Amazon S3 data source. It is not required when you use <code>customModelDataSource</code> with a model package ARN, because Amazon Bedrock uses its own credentials to access the model artifacts.</p>
            model_tags: <p>A list of key-value pairs to associate with the custom model resource. You can use these tags to organize and identify your resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

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

        Examples:
            Successful CreateCustomModel API call

            >>> await client.create_custom_model(model_name='SampleModel', model_source_config={'s3DataSource': {'s3Uri': 's3://my-bucket/folder'}}, role_arn='arn:aws:iam::123456789012:role/SampleRole', model_kms_key_arn='arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab', model_tags=[{'key': 'foo', 'value': 'foo'}, {'key': 'foo', 'value': 'foo'}], client_request_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_custom_model_request.CreateCustomModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_custom_model_response.CreateCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model.async_create_custom_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.create_custom_model_request.CreateCustomModelRequest = {
            "model_name": model_name
        }
        if model_source_config is not None:
            input_["model_source_config"] = model_source_config
        if custom_model_data_source is not None:
            input_["custom_model_data_source"] = custom_model_data_source
        if model_kms_key_arn is not None:
            input_["model_kms_key_arn"] = model_kms_key_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if model_tags is not None:
            input_["model_tags"] = model_tags
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

    async def delete_custom_model(
        self,
        model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_custom_model_response.DeleteCustomModelResponse":
        """<p>Deletes a custom model that you created earlier. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            model_identifier: <p>Name of the model to delete.</p>

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
            req: "AsyncOperationRequest[capo_bedrock.types.delete_custom_model_request.DeleteCustomModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_custom_model_response.DeleteCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model.async_delete_custom_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_custom_model_request.DeleteCustomModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_model(
        self,
        model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_custom_model_response.GetCustomModelResponse":
        """<p>Get the properties associated with a Amazon Bedrock custom model that you have created. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            model_identifier: <p>Name or Amazon Resource Name (ARN) of the custom model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_custom_model_request.GetCustomModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_custom_model_response.GetCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model.async_get_custom_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.get_custom_model_request.GetCustomModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        base_model_arn_equals: Optional["capo_bedrock.types.model_arn.ModelArn"] = None,
        foundation_model_arn_equals: Optional[
            "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        is_owned: Optional[bool] = None,
        model_status: Optional["capo_bedrock.types.model_status.ModelStatus"] = None,
    ) -> "capo_bedrock.types.list_custom_models_response.ListCustomModelsResponse":
        """<p>Returns a list of the custom models that you have created with the <code>CreateModelCustomizationJob</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_before: <p>Return custom models created before the specified time. </p>
            creation_time_after: <p>Return custom models created after the specified time. </p>
            name_contains: <p>Return custom models only if the job name contains these characters.</p>
            base_model_arn_equals: <p>Return custom models only if the base model Amazon Resource Name (ARN) matches this parameter.</p>
            foundation_model_arn_equals: <p>Return custom models only if the foundation model Amazon Resource Name (ARN) matches this parameter.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of models.</p>
            sort_order: <p>The sort order of the results.</p>
            is_owned: <p>Return custom models depending on if the current account owns them (<code>true</code>) or if they were shared with the current account (<code>false</code>).</p>
            model_status: <p>The status of them model to filter results by. Possible values include:</p> <ul> <li> <p> <code>Creating</code> - Include only models that are currently being created and validated.</p> </li> <li> <p> <code>Active</code> - Include only models that have been successfully created and are ready for use.</p> </li> <li> <p> <code>Failed</code> - Include only models where the creation process failed.</p> </li> </ul> <p>If you don't specify a status, the API returns models in all states.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_custom_models_request.ListCustomModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_custom_models_response.ListCustomModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_models

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_models.async_list_custom_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_bedrock.types.list_custom_models_request.ListCustomModelsRequest = {}
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if base_model_arn_equals is not None:
            input_["base_model_arn_equals"] = base_model_arn_equals
        if foundation_model_arn_equals is not None:
            input_["foundation_model_arn_equals"] = foundation_model_arn_equals
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if is_owned is not None:
            input_["is_owned"] = is_owned
        if model_status is not None:
            input_["model_status"] = model_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
