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
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import capo_cleanroomsml.types.create_ml_input_channel_request
    import capo_cleanroomsml.types.create_ml_input_channel_response
    import capo_cleanroomsml.types.delete_ml_input_channel_data_request
    import capo_cleanroomsml.types.get_collaboration_ml_input_channel_request
    import capo_cleanroomsml.types.get_collaboration_ml_input_channel_response
    import capo_cleanroomsml.types.get_ml_input_channel_request
    import capo_cleanroomsml.types.get_ml_input_channel_response
    import capo_cleanroomsml.types.input_channel
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.list_ml_input_channels_request
    import capo_cleanroomsml.types.list_ml_input_channels_response
    import capo_cleanroomsml.types.max_results
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.ml_input_channel_summary
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.next_token
    import capo_cleanroomsml.types.payer_configuration
    import capo_cleanroomsml.types.resource_description
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


class MLInputChannel:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList",
        input_channel: "capo_cleanroomsml.types.input_channel.InputChannel",
        name: "capo_cleanroomsml.types.name_string.NameString",
        retention_in_days: int,
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        payer_configuration: Optional[
            "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse":
        """<p>Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the ML input channel.</p>
            configured_model_algorithm_associations: <p>The associated configured model algorithms that are necessary to create this ML input channel.</p>
            input_channel: <p>The input data that is used to create this ML input channel.</p>
            name: <p>The name of the ML input channel.</p>
            retention_in_days: <p>The number of days that the data in the ML input channel is retained.</p>
            description: <p>The description of the ML input channel.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            payer_configuration: <p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>

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
            req: "OperationRequest[capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel.create_ml_input_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.create_ml_input_channel_request

            return capo_cleanroomsml.types.create_ml_input_channel_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateMLInputChannel", redact_input=_redact_input),
        )
        input_: capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest = {
            "membership_identifier": membership_identifier,
            "configured_model_algorithm_associations": configured_model_algorithm_associations,
            "input_channel": input_channel,
            "name": name,
            "retention_in_days": retention_in_days,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if payer_configuration is not None:
            input_["payer_configuration"] = payer_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse":
        """<p>Returns information about an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel that you want to get.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel.get_ml_input_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.get_ml_input_channel_response

            return (
                capo_cleanroomsml.types.get_ml_input_channel_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetMLInputChannel", redact_output=_redact_output),
        )
        input_: capo_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "membership_identifier": membership_identifier,
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
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Provides the information necessary to delete an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to delete.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data.delete_ml_input_channel_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMLInputChannelData")
        )
        input_: capo_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "membership_identifier": membership_identifier,
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
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse":
        """<p>Returns a list of ML input channels.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of ML input channels to return.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channels that you want to list.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels.list_ml_input_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMLInputChannels")
        )
        input_: capo_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest = {
            "membership_identifier": membership_identifier
        }
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

    def get_collaboration_ml_input_channel(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse":
        """<p>Returns information about a specific ML input channel in a collaboration.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channel that you want to get.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel.get_collaboration_ml_input_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationMLInputChannel")
        )
        input_: capo_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "collaboration_identifier": collaboration_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMLInputChannel:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList",
        input_channel: "capo_cleanroomsml.types.input_channel.InputChannel",
        name: "capo_cleanroomsml.types.name_string.NameString",
        retention_in_days: int,
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
        kms_key_arn: Optional["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_cleanroomsml.types.tag_map.TagMap"] = None,
        payer_configuration: Optional[
            "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
        ] = None,
    ) -> "capo_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse":
        """<p>Provides the information to create an ML input channel. An ML input channel is the result of a query that can be used for ML modeling.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is creating the ML input channel.</p>
            configured_model_algorithm_associations: <p>The associated configured model algorithms that are necessary to create this ML input channel.</p>
            input_channel: <p>The input data that is used to create this ML input channel.</p>
            name: <p>The name of the ML input channel.</p>
            retention_in_days: <p>The number of days that the data in the ML input channel is retained.</p>
            description: <p>The description of the ML input channel.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>
            tags: <p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>
            payer_configuration: <p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>

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
            req: "AsyncOperationRequest[capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.create_ml_input_channel_response.CreateMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.create_ml_input_channel.async_create_ml_input_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.create_ml_input_channel_request

            return capo_cleanroomsml.types.create_ml_input_channel_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateMLInputChannel", redact_input=_redact_input),
        )
        input_: capo_cleanroomsml.types.create_ml_input_channel_request.CreateMLInputChannelRequest = {
            "membership_identifier": membership_identifier,
            "configured_model_algorithm_associations": configured_model_algorithm_associations,
            "input_channel": input_channel,
            "name": name,
            "retention_in_days": retention_in_days,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags
        if payer_configuration is not None:
            input_["payer_configuration"] = payer_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse":
        """<p>Returns information about an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel that you want to get.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_ml_input_channel.async_get_ml_input_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_cleanroomsml.types.get_ml_input_channel_response.GetMLInputChannelResponse",
        ) -> dict[str, Any]:
            import capo_cleanroomsml.types.get_ml_input_channel_response

            return (
                capo_cleanroomsml.types.get_ml_input_channel_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetMLInputChannel", redact_output=_redact_output),
        )
        input_: capo_cleanroomsml.types.get_ml_input_channel_request.GetMLInputChannelRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "membership_identifier": membership_identifier,
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
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Provides the information necessary to delete an ML input channel.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to delete.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channel you want to delete.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_input_channel_data.async_delete_ml_input_channel_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMLInputChannelData")
        )
        input_: capo_cleanroomsml.types.delete_ml_input_channel_data_request.DeleteMLInputChannelDataRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "membership_identifier": membership_identifier,
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
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        next_token: Optional["capo_cleanroomsml.types.next_token.NextToken"] = None,
        max_results: Optional["capo_cleanroomsml.types.max_results.MaxResults"] = None,
    ) -> "capo_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse":
        """<p>Returns a list of ML input channels.</p>

        Args:
            next_token: <p>The token value retrieved from a previous call to access the next page of results.</p>
            max_results: <p>The maximum number of ML input channels to return.</p>
            membership_identifier: <p>The membership ID of the membership that contains the ML input channels that you want to list.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.list_ml_input_channels_response.ListMLInputChannelsResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.list_ml_input_channels.async_list_ml_input_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListMLInputChannels")
        )
        input_: capo_cleanroomsml.types.list_ml_input_channels_request.ListMLInputChannelsRequest = {
            "membership_identifier": membership_identifier
        }
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

    async def get_collaboration_ml_input_channel(
        self,
        ml_input_channel_arn: "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn",
        collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse":
        """<p>Returns information about a specific ML input channel in a collaboration.</p>

        Args:
            ml_input_channel_arn: <p>The Amazon Resource Name (ARN) of the ML input channel that you want to get.</p>
            collaboration_identifier: <p>The collaboration ID of the collaboration that contains the ML input channel that you want to get.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_collaboration_ml_input_channel_response.GetCollaborationMLInputChannelResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_collaboration_ml_input_channel.async_get_collaboration_ml_input_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCollaborationMLInputChannel")
        )
        input_: capo_cleanroomsml.types.get_collaboration_ml_input_channel_request.GetCollaborationMLInputChannelRequest = {
            "ml_input_channel_arn": ml_input_channel_arn,
            "collaboration_identifier": collaboration_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
