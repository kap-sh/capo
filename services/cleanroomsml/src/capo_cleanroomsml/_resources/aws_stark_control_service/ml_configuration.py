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
    import capo_cleanroomsml.types.delete_ml_configuration_request
    import capo_cleanroomsml.types.get_ml_configuration_request
    import capo_cleanroomsml.types.get_ml_configuration_response
    import capo_cleanroomsml.types.ml_output_configuration
    import capo_cleanroomsml.types.put_ml_configuration_request
    import capo_cleanroomsml.types.uuid
    from capo_cleanroomsml._services.async_clean_rooms_ml import (
        AsyncCleanRoomsMLClient,
        AsyncCleanRoomsMLClientConfig,
    )
    from capo_cleanroomsml._services.clean_rooms_ml import (
        CleanRoomsMLClient,
        CleanRoomsMLClientConfig,
    )


class MLConfiguration:
    def __init__(self, service: CleanRoomsMLClient) -> None:
        self._service = service

    def put(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        default_output_location: "capo_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Assigns information about an ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is being configured.</p>
            default_output_location: <p>The default Amazon S3 location where ML output is stored for the specified member.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration.put_ml_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutMLConfiguration")
        )
        input_: capo_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest = {
            "membership_identifier": membership_identifier,
            "default_output_location": default_output_location,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse":
        """<p>Returns information about a specific ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that owns the ML configuration you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest]",
        ) -> OperationResponse[
            "capo_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration.get_ml_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMLConfiguration")
        )
        input_: capo_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest = {
            "membership_identifier": membership_identifier
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
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[CleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a ML modeling configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the of the member that is deleting the ML modeling configuration.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration

            output, http_response = (
                capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration.delete_ml_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMLConfiguration")
        )
        input_: capo_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest = {
            "membership_identifier": membership_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncMLConfiguration:
    def __init__(self, service: AsyncCleanRoomsMLClient) -> None:
        self._service = service

    async def put(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        default_output_location: "capo_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Assigns information about an ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that is being configured.</p>
            default_output_location: <p>The default Amazon S3 location where ML output is stored for the specified member.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.put_ml_configuration.async_put_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutMLConfiguration")
        )
        input_: capo_cleanroomsml.types.put_ml_configuration_request.PutMLConfigurationRequest = {
            "membership_identifier": membership_identifier,
            "default_output_location": default_output_location,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> "capo_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse":
        """<p>Returns information about a specific ML configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the member that owns the ML configuration you want to return information about.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_cleanroomsml.types.get_ml_configuration_response.GetMLConfigurationResponse"
        ]:
            import capo_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.get_ml_configuration.async_get_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetMLConfiguration")
        )
        input_: capo_cleanroomsml.types.get_ml_configuration_request.GetMLConfigurationRequest = {
            "membership_identifier": membership_identifier
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
        membership_identifier: "capo_cleanroomsml.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncCleanRoomsMLClientConfig] = None,
    ) -> None:
        """<p>Deletes a ML modeling configuration.</p>

        Args:
            membership_identifier: <p>The membership ID of the of the member that is deleting the ML modeling configuration.</p>

        Raises:
            capo_cleanroomsml.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_cleanroomsml.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource you are requesting does not exist.</p>
            capo_cleanroomsml.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_cleanroomsml.errors.validation_exception.ValidationException: <p>The request parameters for this request are incorrect.</p>
            capo_cleanroomsml.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration

            (
                output,
                http_response,
            ) = await capo_cleanroomsml._operations.aws_stark_control_service.delete_ml_configuration.async_delete_ml_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteMLConfiguration")
        )
        input_: capo_cleanroomsml.types.delete_ml_configuration_request.DeleteMLConfigurationRequest = {
            "membership_identifier": membership_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
