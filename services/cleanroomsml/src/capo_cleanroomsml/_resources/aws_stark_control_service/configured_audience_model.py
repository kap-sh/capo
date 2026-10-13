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
    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.audience_size_config
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.configured_audience_model_output_config
    import capo_cleanroomsml.types.configured_audience_model_summary
    import capo_cleanroomsml.types.create_configured_audience_model_request
    import capo_cleanroomsml.types.create_configured_audience_model_response
    import capo_cleanroomsml.types.delete_configured_audience_model_request
    import capo_cleanroomsml.types.get_configured_audience_model_request
    import capo_cleanroomsml.types.get_configured_audience_model_response
    import capo_cleanroomsml.types.list_configured_audience_models_request
    import capo_cleanroomsml.types.list_configured_audience_models_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.metrics_list
    import capo_cleanroomsml.types.min_matching_seed_size
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.tag_on_create_policy
    import capo_cleanroomsml.types.update_configured_audience_model_request
    import capo_cleanroomsml.types.update_configured_audience_model_response
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class ConfiguredAudienceModel:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        output_config: "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig",
        shared_audience_metrics: "capo_cleanroomsml.types.metrics_list.MetricsList",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        min_matching_seed_size: Optional[
            "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
        ] = None,
        audience_size_config: Optional[
            "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        child_resource_tag_on_create_policy: Optional[
            "capo_cleanroomsml.types.tag_on_create_policy.TagOnCreatePolicy"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_configured_audience_model_response.CreateConfiguredAudienceModelResponse":
        """<p>Defines the information necessary to create a configured audience model.</p>

        Args:
            name: <p>The name of the configured audience model.</p>
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model to use for the configured audience model.</p>
            output_config: <p>Configure the Amazon S3 location and IAM Role for audiences created using this configured audience model. Each audience will have a unique location. The IAM Role must have <code>s3:PutObject</code> permission on the destination Amazon S3 location. If the destination is protected with Amazon S3 KMS-SSE, then the Role must also have the required KMS permissions.</p>
            description: <p>The description of the configured audience model.</p>
            shared_audience_metrics: <p>Whether audience metrics are shared.</p>
            min_matching_seed_size: <p>The minimum number of users from the seed audience that must match with users in the training data of the audience model. The default value is 500.</p>
            audience_size_config: <p>Configure the list of output sizes of audiences that can be created using this configured audience model. A request to <a>StartAudienceGenerationJob</a> that uses this configured audience model must have an <code>audienceSize</code> selected from this list. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            child_resource_tag_on_create_policy: <p>Configure how the service tags audience generation jobs created using this configured audience model. If you specify <code>NONE</code>, the tags from the <a>StartAudienceGenerationJob</a> request determine the tags of the audience generation job. If you specify <code>FROM_PARENT_RESOURCE</code>, the audience generation job inherits the tags from the configured audience model, by default. Tags in the <a>StartAudienceGenerationJob</a> will override the default.</p> <p>When the client is in a different account than the configured audience model, the tags from the client are never applied to a resource in the caller's account.</p>

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
            req: "OperationRequest[capo_cleanroomsml.types.create_configured_audience_model_request.CreateConfiguredAudienceModelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.create_configured_audience_model_response.CreateConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.create_configured_audience_model.create_configured_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.create_configured_audience_model_request.CreateConfiguredAudienceModelRequest = {
            "name": name,
            "audience_model_arn": audience_model_arn,
            "output_config": output_config,
            "shared_audience_metrics": shared_audience_metrics,
        }
        if description is not None:
            input_["description"] = description
        if min_matching_seed_size is not None:
            input_["min_matching_seed_size"] = min_matching_seed_size
        if audience_size_config is not None:
            input_["audience_size_config"] = audience_size_config
        if tags is not None:
            input_["tags"] = tags
        if child_resource_tag_on_create_policy is not None:
            input_["child_resource_tag_on_create_policy"] = (
                child_resource_tag_on_create_policy
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_audience_model_response.GetConfiguredAudienceModelResponse":
        """<p>Returns information about a specified configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_configured_audience_model_request.GetConfiguredAudienceModelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_configured_audience_model_response.GetConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model.get_configured_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.get_configured_audience_model_request.GetConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        output_config: Optional[
            "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
        ] = None,
        audience_model_arn: Optional[
            "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
        ] = None,
        shared_audience_metrics: Optional[
            "capo_cleanroomsml.types.metrics_list.MetricsList"
        ] = None,
        min_matching_seed_size: Optional[
            "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
        ] = None,
        audience_size_config: Optional[
            "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.update_configured_audience_model_response.UpdateConfiguredAudienceModelResponse":
        """<p>Provides the information necessary to update a configured audience model. Updates that impact audience generation jobs take effect when a new job starts, but do not impact currently running jobs.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you want to update.</p>
            output_config: <p>The new output configuration.</p>
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the new audience model that you want to use.</p>
            shared_audience_metrics: <p>The new value for whether to share audience metrics.</p>
            min_matching_seed_size: <p>The minimum number of users from the seed audience that must match with users in the training data of the audience model.</p>
            audience_size_config: <p>The new audience size configuration.</p>
            description: <p>The new description of the configured audience model.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.update_configured_audience_model_request.UpdateConfiguredAudienceModelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.update_configured_audience_model_response.UpdateConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.update_configured_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.update_configured_audience_model.update_configured_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.update_configured_audience_model_request.UpdateConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }
        if output_config is not None:
            input_["output_config"] = output_config
        if audience_model_arn is not None:
            input_["audience_model_arn"] = audience_model_arn
        if shared_audience_metrics is not None:
            input_["shared_audience_metrics"] = shared_audience_metrics
        if min_matching_seed_size is not None:
            input_["min_matching_seed_size"] = min_matching_seed_size
        if audience_size_config is not None:
            input_["audience_size_config"] = audience_size_config
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configured audience model. You can't delete a configured audience model if there are any lookalike models that use the configured audience model. If you delete a configured audience model, it will be removed from any collaborations that it is associated to.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_configured_audience_model_request.DeleteConfiguredAudienceModelRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model.delete_configured_audience_model(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.delete_configured_audience_model_request.DeleteConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
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
    ) -> "capo_cleanroomsml.types.list_configured_audience_models_response.ListConfiguredAudienceModelsResponse":
        """<p>Returns a list of the configured audience models.</p>

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
            req: "OperationRequest[capo_cleanroomsml.types.list_configured_audience_models_request.ListConfiguredAudienceModelsRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.list_configured_audience_models_response.ListConfiguredAudienceModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_audience_models

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.list_configured_audience_models.list_configured_audience_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredAudienceModels")
        )
        input_: capo_cleanroomsml.types.list_configured_audience_models_request.ListConfiguredAudienceModelsRequest = {}
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


class AsyncConfiguredAudienceModel:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn",
        output_config: "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig",
        shared_audience_metrics: "capo_cleanroomsml.types.metrics_list.MetricsList",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        min_matching_seed_size: Optional[
            "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
        ] = None,
        audience_size_config: Optional[
            "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        child_resource_tag_on_create_policy: Optional[
            "capo_cleanroomsml.types.tag_on_create_policy.TagOnCreatePolicy"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_configured_audience_model_response.CreateConfiguredAudienceModelResponse":
        """<p>Defines the information necessary to create a configured audience model.</p>

        Args:
            name: <p>The name of the configured audience model.</p>
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the audience model to use for the configured audience model.</p>
            output_config: <p>Configure the Amazon S3 location and IAM Role for audiences created using this configured audience model. Each audience will have a unique location. The IAM Role must have <code>s3:PutObject</code> permission on the destination Amazon S3 location. If the destination is protected with Amazon S3 KMS-SSE, then the Role must also have the required KMS permissions.</p>
            description: <p>The description of the configured audience model.</p>
            shared_audience_metrics: <p>Whether audience metrics are shared.</p>
            min_matching_seed_size: <p>The minimum number of users from the seed audience that must match with users in the training data of the audience model. The default value is 500.</p>
            audience_size_config: <p>Configure the list of output sizes of audiences that can be created using this configured audience model. A request to <a>StartAudienceGenerationJob</a> that uses this configured audience model must have an <code>audienceSize</code> selected from this list. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            child_resource_tag_on_create_policy: <p>Configure how the service tags audience generation jobs created using this configured audience model. If you specify <code>NONE</code>, the tags from the <a>StartAudienceGenerationJob</a> request determine the tags of the audience generation job. If you specify <code>FROM_PARENT_RESOURCE</code>, the audience generation job inherits the tags from the configured audience model, by default. Tags in the <a>StartAudienceGenerationJob</a> will override the default.</p> <p>When the client is in a different account than the configured audience model, the tags from the client are never applied to a resource in the caller's account.</p>

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
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_configured_audience_model_request.CreateConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_configured_audience_model_response.CreateConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_configured_audience_model.async_create_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.create_configured_audience_model_request.CreateConfiguredAudienceModelRequest = {
            "name": name,
            "audience_model_arn": audience_model_arn,
            "output_config": output_config,
            "shared_audience_metrics": shared_audience_metrics,
        }
        if description is not None:
            input_["description"] = description
        if min_matching_seed_size is not None:
            input_["min_matching_seed_size"] = min_matching_seed_size
        if audience_size_config is not None:
            input_["audience_size_config"] = audience_size_config
        if tags is not None:
            input_["tags"] = tags
        if child_resource_tag_on_create_policy is not None:
            input_["child_resource_tag_on_create_policy"] = (
                child_resource_tag_on_create_policy
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_audience_model_response.GetConfiguredAudienceModelResponse":
        """<p>Returns information about a specified configured audience model.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_audience_model_request.GetConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_audience_model_response.GetConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_audience_model.async_get_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.get_configured_audience_model_request.GetConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        output_config: Optional[
            "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
        ] = None,
        audience_model_arn: Optional[
            "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
        ] = None,
        shared_audience_metrics: Optional[
            "capo_cleanroomsml.types.metrics_list.MetricsList"
        ] = None,
        min_matching_seed_size: Optional[
            "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
        ] = None,
        audience_size_config: Optional[
            "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> "capo_cleanroomsml.types.update_configured_audience_model_response.UpdateConfiguredAudienceModelResponse":
        """<p>Provides the information necessary to update a configured audience model. Updates that impact audience generation jobs take effect when a new job starts, but do not impact currently running jobs.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you want to update.</p>
            output_config: <p>The new output configuration.</p>
            audience_model_arn: <p>The Amazon Resource Name (ARN) of the new audience model that you want to use.</p>
            shared_audience_metrics: <p>The new value for whether to share audience metrics.</p>
            min_matching_seed_size: <p>The minimum number of users from the seed audience that must match with users in the training data of the audience model.</p>
            audience_size_config: <p>The new audience size configuration.</p>
            description: <p>The new description of the configured audience model.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.update_configured_audience_model_request.UpdateConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.update_configured_audience_model_response.UpdateConfiguredAudienceModelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.update_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.update_configured_audience_model.async_update_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.update_configured_audience_model_request.UpdateConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
        }
        if output_config is not None:
            input_["output_config"] = output_config
        if audience_model_arn is not None:
            input_["audience_model_arn"] = audience_model_arn
        if shared_audience_metrics is not None:
            input_["shared_audience_metrics"] = shared_audience_metrics
        if min_matching_seed_size is not None:
            input_["min_matching_seed_size"] = min_matching_seed_size
        if audience_size_config is not None:
            input_["audience_size_config"] = audience_size_config
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified configured audience model. You can't delete a configured audience model if there are any lookalike models that use the configured audience model. If you delete a configured audience model, it will be removed from any collaborations that it is associated to.</p>

        Args:
            configured_audience_model_arn: <p>The Amazon Resource Name (ARN) of the configured audience model that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_audience_model_request.DeleteConfiguredAudienceModelRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_audience_model.async_delete_configured_audience_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredAudienceModel")
        )
        input_: capo_cleanroomsml.types.delete_configured_audience_model_request.DeleteConfiguredAudienceModelRequest = {
            "configured_audience_model_arn": configured_audience_model_arn
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
    ) -> "capo_cleanroomsml.types.list_configured_audience_models_response.ListConfiguredAudienceModelsResponse":
        """<p>Returns a list of the configured audience models.</p>

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
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_configured_audience_models_request.ListConfiguredAudienceModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_configured_audience_models_response.ListConfiguredAudienceModelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_audience_models

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_configured_audience_models.async_list_configured_audience_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredAudienceModels")
        )
        input_: capo_cleanroomsml.types.list_configured_audience_models_request.ListConfiguredAudienceModelsRequest = {}
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
