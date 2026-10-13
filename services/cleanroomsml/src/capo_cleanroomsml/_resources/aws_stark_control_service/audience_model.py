from __future__ import annotations

import datetime
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
    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.audience_model_summary
    import capo_cleanroomsml.types.create_audience_model_request
    import capo_cleanroomsml.types.create_audience_model_response
    import capo_cleanroomsml.types.delete_audience_model_request
    import capo_cleanroomsml.types.get_audience_model_request
    import capo_cleanroomsml.types.get_audience_model_response
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.list_audience_models_request
    import capo_cleanroomsml.types.list_audience_models_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.training_dataset_arn
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class AudienceModel:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        training_dataset_arn: "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        training_data_start_time: Optional[datetime.datetime] = None,
        training_data_end_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse":
        """<p>Defines the information necessary to create an audience model. An audience model is a machine learning model that Clean Rooms ML trains to measure similarity between users. Clean Rooms ML manages training and storing the audience model. The audience model can be used in multiple calls to the <a>StartAudienceGenerationJob</a> API.</p>

        Args:
            training_data_start_time: <p>The start date and time of the training window.</p>
            training_data_end_time: <p>The end date and time of the training window.</p>
            name: <p>The name of the audience model resource.</p>
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset for this audience model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the audience model.</p>

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
            req: "OperationRequest[capo_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.create_audience_model.create_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAudienceModel")
        )
        input_: capo_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest = {
            "name": name,
            "training_dataset_arn": training_dataset_arn,
        }
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse":
        """<p>Returns information about an audience model</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_audience_model.get_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAudienceModel")
        )
        input_: capo_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest = {
            "audience_model_arn": audience_model_arn
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
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies an audience model that you want to delete. You can't delete an audience model if there are any configured audience models that depend on the audience model.</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_model.delete_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAudienceModel")
        )
        input_: capo_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest = {
            "audience_model_arn": audience_model_arn
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
    ) -> "capo_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse":
        """<p>Returns a list of audience models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_models

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.list_audience_models.list_audience_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAudienceModels")
        )
        input_: capo_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest = {}
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


class AsyncAudienceModel:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        training_dataset_arn: "capo_cleanroomsml.types.training_dataset_arn.TrainingDatasetArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        training_data_start_time: Optional[datetime.datetime] = None,
        training_data_end_time: Optional[datetime.datetime] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse":
        """<p>Defines the information necessary to create an audience model. An audience model is a machine learning model that Clean Rooms ML trains to measure similarity between users. Clean Rooms ML manages training and storing the audience model. The audience model can be used in multiple calls to the <a>StartAudienceGenerationJob</a> API.</p>

        Args:
            training_data_start_time: <p>The start date and time of the training window.</p>
            training_data_end_time: <p>The end date and time of the training window.</p>
            name: <p>The name of the audience model resource.</p>
            training_dataset_arn: <p>The Amazon Resource Name (ARN) of the training dataset for this audience model.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the trained ML model and the associated data.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            description: <p>The description of the audience model.</p>

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
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_audience_model_response.CreateAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_audience_model.async_create_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateAudienceModel")
        )
        input_: capo_cleanroomsml.types.create_audience_model_request.CreateAudienceModelRequest = {
            "name": name,
            "training_dataset_arn": training_dataset_arn,
        }
        if training_data_start_time is not None:
            input_["training_data_start_time"] = training_data_start_time
        if training_data_end_time is not None:
            input_["training_data_end_time"] = training_data_end_time
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse":
        """<p>Returns information about an audience model</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_audience_model_response.GetAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_audience_model.async_get_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAudienceModel")
        )
        input_: capo_cleanroomsml.types.get_audience_model_request.GetAudienceModelRequest = {
            "audience_model_arn": audience_model_arn
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
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Specifies an audience model that you want to delete. You can't delete an audience model if there are any configured audience models that depend on the audience model.</p>

        Args:
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_audience_model.async_delete_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteAudienceModel")
        )
        input_: capo_cleanroomsml.types.delete_audience_model_request.DeleteAudienceModelRequest = {
            "audience_model_arn": audience_model_arn
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
    ) -> "capo_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse":
        """<p>Returns a list of audience models.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum size of the results that is returned per call.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_audience_models_response.ListAudienceModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_audience_models

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_audience_models.async_list_audience_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListAudienceModels")
        )
        input_: capo_cleanroomsml.types.list_audience_models_request.ListAudienceModelsRequest = {}
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
