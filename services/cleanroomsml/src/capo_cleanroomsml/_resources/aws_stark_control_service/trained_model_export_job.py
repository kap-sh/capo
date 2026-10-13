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
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.start_trained_model_export_job_request
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_export_output_configuration
    import capo_cleanroomsml.types.uuid
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class TrainedModelExportJob:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        output_configuration: "capo_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Provides the information necessary to start a trained model export job.</p>

        Args:
            name: <p>The name of the trained model export job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>
            membership_identifier: <p>The membership ID of the member that is receiving the exported trained model artifacts.</p>
            output_configuration: <p>The output configuration information for the trained model export job.</p>
            description: <p>The description of the trained model export job.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job.start_trained_model_export_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartTrainedModelExportJob")
        )
        input_: capo_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest = {
            "name": name,
            "trained_model_arn": trained_model_arn,
            "membership_identifier": membership_identifier,
            "output_configuration": output_configuration,
        }
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTrainedModelExportJob:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_cleanroomsml.types.name_string.NameString",
        trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn",
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        output_configuration: "capo_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
        trained_model_version_identifier: Optional[
            "capo_cleanroomsml.types.uuid.UUID"
        ] = None,
        description: Optional[
            "capo_cleanroomsml.types.resource_description.ResourceDescription"
        ] = None,
    ) -> None:
        """<p>Provides the information necessary to start a trained model export job.</p>

        Args:
            name: <p>The name of the trained model export job.</p>
            trained_model_arn: <p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>
            trained_model_version_identifier: <p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>
            membership_identifier: <p>The membership ID of the member that is receiving the exported trained model artifacts.</p>
            output_configuration: <p>The output configuration information for the trained model export job.</p>
            description: <p>The description of the trained model export job.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.conflict_exception.ConflictException: <p>You can't complete this action because another resource depends on this resource.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.start_trained_model_export_job.async_start_trained_model_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartTrainedModelExportJob")
        )
        input_: capo_cleanroomsml.types.start_trained_model_export_job_request.StartTrainedModelExportJobRequest = {
            "name": name,
            "trained_model_arn": trained_model_arn,
            "membership_identifier": membership_identifier,
            "output_configuration": output_configuration,
        }
        if trained_model_version_identifier is not None:
            input_["trained_model_version_identifier"] = (
                trained_model_version_identifier
            )
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
