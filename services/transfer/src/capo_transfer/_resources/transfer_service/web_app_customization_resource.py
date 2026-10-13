from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from capo_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_transfer.types.delete_web_app_customization_request
    import capo_transfer.types.describe_web_app_customization_request
    import capo_transfer.types.describe_web_app_customization_response
    import capo_transfer.types.update_web_app_customization_request
    import capo_transfer.types.update_web_app_customization_response
    import capo_transfer.types.web_app_favicon_file
    import capo_transfer.types.web_app_id
    import capo_transfer.types.web_app_logo_file
    import capo_transfer.types.web_app_title
    from capo_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from capo_transfer._services.transfer import TransferClient, TransferClientConfig


class WebAppCustomizationResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def read(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse":
        """<p>Describes the web app customization object that's identified by <code>WebAppId</code>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_web_app_customization

            output, http_response = (
                capo_transfer._operations.transfer_service.describe_web_app_customization.describe_web_app_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse",
        ) -> dict[str, Any]:
            import capo_transfer.types.describe_web_app_customization_response

            return capo_transfer.types.describe_web_app_customization_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeWebAppCustomization", redact_output=_redact_output
            ),
        )
        input_: capo_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest = {
            "web_app_id": web_app_id
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
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        title: Optional["capo_transfer.types.web_app_title.WebAppTitle"] = None,
        logo_file: Optional[
            "capo_transfer.types.web_app_logo_file.WebAppLogoFile"
        ] = None,
        favicon_file: Optional[
            "capo_transfer.types.web_app_favicon_file.WebAppFaviconFile"
        ] = None,
    ) -> "capo_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse":
        """<p>Assigns new customization properties to a web app. You can modify the icon file, logo file, and title.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            title: <p>Provide an updated title.</p>
            logo_file: <p>Specify logo file data string (in base64 encoding).</p>
            favicon_file: <p>Specify an icon file data string (in base64 encoding).</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest]",
        ) -> OperationResponse[
            "capo_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_web_app_customization

            output, http_response = (
                capo_transfer._operations.transfer_service.update_web_app_customization.update_web_app_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest",
        ) -> dict[str, Any]:
            import capo_transfer.types.update_web_app_customization_request

            return capo_transfer.types.update_web_app_customization_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateWebAppCustomization", redact_input=_redact_input),
        )
        input_: capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }
        if title is not None:
            input_["title"] = title
        if logo_file is not None:
            input_["logo_file"] = logo_file
        if favicon_file is not None:
            input_["favicon_file"] = favicon_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the <code>WebAppCustomization</code> object that corresponds to the web app ID specified.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that contains the customizations that you are deleting.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest]",
        ) -> OperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_web_app_customization

            output, http_response = (
                capo_transfer._operations.transfer_service.delete_web_app_customization.delete_web_app_customization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWebAppCustomization")
        )
        input_: capo_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncWebAppCustomizationResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def read(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse":
        """<p>Describes the web app customization object that's identified by <code>WebAppId</code>.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse"
        ]:
            import capo_transfer._operations.transfer_service.describe_web_app_customization

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.describe_web_app_customization.async_describe_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_transfer.types.describe_web_app_customization_response.DescribeWebAppCustomizationResponse",
        ) -> dict[str, Any]:
            import capo_transfer.types.describe_web_app_customization_response

            return capo_transfer.types.describe_web_app_customization_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "DescribeWebAppCustomization", redact_output=_redact_output
            ),
        )
        input_: capo_transfer.types.describe_web_app_customization_request.DescribeWebAppCustomizationRequest = {
            "web_app_id": web_app_id
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
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        title: Optional["capo_transfer.types.web_app_title.WebAppTitle"] = None,
        logo_file: Optional[
            "capo_transfer.types.web_app_logo_file.WebAppLogoFile"
        ] = None,
        favicon_file: Optional[
            "capo_transfer.types.web_app_favicon_file.WebAppFaviconFile"
        ] = None,
    ) -> "capo_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse":
        """<p>Assigns new customization properties to a web app. You can modify the icon file, logo file, and title.</p>

        Args:
            web_app_id: <p>Provide the identifier of the web app that you are updating.</p>
            title: <p>Provide an updated title.</p>
            logo_file: <p>Specify logo file data string (in base64 encoding).</p>
            favicon_file: <p>Specify an icon file data string (in base64 encoding).</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[
            "capo_transfer.types.update_web_app_customization_response.UpdateWebAppCustomizationResponse"
        ]:
            import capo_transfer._operations.transfer_service.update_web_app_customization

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.update_web_app_customization.async_update_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest",
        ) -> dict[str, Any]:
            import capo_transfer.types.update_web_app_customization_request

            return capo_transfer.types.update_web_app_customization_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateWebAppCustomization", redact_input=_redact_input),
        )
        input_: capo_transfer.types.update_web_app_customization_request.UpdateWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }
        if title is not None:
            input_["title"] = title
        if logo_file is not None:
            input_["logo_file"] = logo_file
        if favicon_file is not None:
            input_["favicon_file"] = favicon_file

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        web_app_id: "capo_transfer.types.web_app_id.WebAppId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the <code>WebAppCustomization</code> object that corresponds to the web app ID specified.</p>

        Args:
            web_app_id: <p>Provide the unique identifier for the web app that contains the customizations that you are deleting.</p>

        Raises:
            capo_transfer.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_transfer.errors.conflict_exception.ConflictException: <p>This exception is thrown when the <code>UpdateServer</code> is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's <code>VpcEndpointID</code> is not in the available state.</p>
            capo_transfer.errors.internal_service_error.InternalServiceError: <p>This exception is thrown when an error occurs in the Transfer Family service.</p>
            capo_transfer.errors.invalid_request_exception.InvalidRequestException: <p>This exception is thrown when the client submits a malformed request.</p>
            capo_transfer.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource is not found by the Amazon Web ServicesTransfer Family service.</p>
            capo_transfer.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_transfer.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_transfer._operations.transfer_service.delete_web_app_customization

            (
                output,
                http_response,
            ) = await capo_transfer._operations.transfer_service.delete_web_app_customization.async_delete_web_app_customization(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWebAppCustomization")
        )
        input_: capo_transfer.types.delete_web_app_customization_request.DeleteWebAppCustomizationRequest = {
            "web_app_id": web_app_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
