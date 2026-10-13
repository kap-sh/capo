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
    import capo_cleanroomsml.types.configured_model_algorithm_arn
    import capo_cleanroomsml.types.configured_model_algorithm_summary
    import capo_cleanroomsml.types.container_config
    import capo_cleanroomsml.types.create_configured_model_algorithm_request
    import capo_cleanroomsml.types.create_configured_model_algorithm_response
    import capo_cleanroomsml.types.delete_configured_model_algorithm_request
    import capo_cleanroomsml.types.get_configured_model_algorithm_request
    import capo_cleanroomsml.types.get_configured_model_algorithm_response
    import capo_cleanroomsml.types.iam_role_arn
    import capo_cleanroomsml.types.inference_container_config
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.list_configured_model_algorithms_request
    import capo_cleanroomsml.types.list_configured_model_algorithms_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class ConfiguredModelAlgorithm:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        training_container_config: Optional[
            "capo_cleanroomsml.types.container_config.ContainerConfig"
        ] = None,
        inference_container_config: Optional[
            "capo_cleanroomsml.types.inference_container_config.InferenceContainerConfig"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse":
        """<p>Creates a configured model algorithm using a container image stored in an ECR repository.</p>

        Args:
            name: <p>The name of the configured model algorithm.</p>
            description: <p>The description of the configured model algorithm.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role that is used to access the repository.</p>
            training_container_config: <p>Configuration information for the training container, including entrypoints and arguments.</p>
            inference_container_config: <p>Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm.create_configured_model_algorithm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredModelAlgorithm")
        )
        input_: capo_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if training_container_config is not None:
            input_["training_container_config"] = training_container_config
        if inference_container_config is not None:
            input_["inference_container_config"] = inference_container_config
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse":
        """<p>Returns information about a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm.get_configured_model_algorithm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredModelAlgorithm")
        )
        input_: capo_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn
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
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm.delete_configured_model_algorithm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredModelAlgorithm")
        )
        input_: capo_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn
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
    ) -> "capo_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse":
        """<p>Returns a list of configured model algorithms.</p>

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
            req: "OperationRequest[capo_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms.list_configured_model_algorithms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredModelAlgorithms")
        )
        input_: capo_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest = {}
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


class AsyncConfiguredModelAlgorithm:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        training_container_config: Optional[
            "capo_cleanroomsml.types.container_config.ContainerConfig"
        ] = None,
        inference_container_config: Optional[
            "capo_cleanroomsml.types.inference_container_config.InferenceContainerConfig"
        ] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
    ) -> "capo_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse":
        """<p>Creates a configured model algorithm using a container image stored in an ECR repository.</p>

        Args:
            name: <p>The name of the configured model algorithm.</p>
            description: <p>The description of the configured model algorithm.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role that is used to access the repository.</p>
            training_container_config: <p>Configuration information for the training container, including entrypoints and arguments.</p>
            inference_container_config: <p>Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_configured_model_algorithm_response.CreateConfiguredModelAlgorithmResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_configured_model_algorithm.async_create_configured_model_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateConfiguredModelAlgorithm")
        )
        input_: capo_cleanroomsml.types.create_configured_model_algorithm_request.CreateConfiguredModelAlgorithmRequest = {
            "name": name,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if training_container_config is not None:
            input_["training_container_config"] = training_container_config
        if inference_container_config is not None:
            input_["inference_container_config"] = inference_container_config
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse":
        """<p>Returns information about a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_configured_model_algorithm_response.GetConfiguredModelAlgorithmResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_configured_model_algorithm.async_get_configured_model_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetConfiguredModelAlgorithm")
        )
        input_: capo_cleanroomsml.types.get_configured_model_algorithm_request.GetConfiguredModelAlgorithmRequest = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn
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
        configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a configured model algorithm.</p>

        Args:
            configured_model_algorithm_arn: <p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_configured_model_algorithm.async_delete_configured_model_algorithm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteConfiguredModelAlgorithm")
        )
        input_: capo_cleanroomsml.types.delete_configured_model_algorithm_request.DeleteConfiguredModelAlgorithmRequest = {
            "configured_model_algorithm_arn": configured_model_algorithm_arn
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
    ) -> "capo_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse":
        """<p>Returns a list of configured model algorithms.</p>

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
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_configured_model_algorithms_response.ListConfiguredModelAlgorithmsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_configured_model_algorithms.async_list_configured_model_algorithms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListConfiguredModelAlgorithms")
        )
        input_: capo_cleanroomsml.types.list_configured_model_algorithms_request.ListConfiguredModelAlgorithmsRequest = {}
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
