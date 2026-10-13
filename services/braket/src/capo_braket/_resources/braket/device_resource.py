from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_braket._auth._signers
import capo_braket._auth._sigv4
from capo_braket._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_braket.types.device_arn
    import capo_braket.types.device_summary
    import capo_braket.types.get_device_request
    import capo_braket.types.get_device_response
    import capo_braket.types.search_devices_filter_list
    import capo_braket.types.search_devices_request
    import capo_braket.types.search_devices_response
    from capo_braket._services.async_braket import (
        AsyncBraketClient,
        AsyncBraketClientConfig,
    )
    from capo_braket._services.braket import BraketClient, BraketClientConfig


class DeviceResource:
    def __init__(self, service: BraketClient) -> None:
        self._service = service

    def read(
        self,
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
    ) -> "capo_braket.types.get_device_response.GetDeviceResponse":
        """<p>Retrieves the devices available in Amazon Braket.</p> <note> <p>For backwards compatibility with older versions of BraketSchemas, OpenQASM information is omitted from GetDevice API calls. To get this information the user-agent needs to present a recent version of the BraketSchemas (1.8.0 or later). The Braket SDK automatically reports this for you. If you do not see OpenQASM results in the GetDevice response when using a Braket SDK, you may need to set AWS_EXECUTION_ENV environment variable to configure user-agent. See the code examples provided below for how to do this for the AWS CLI, Boto3, and the Go, Java, and JavaScript/TypeScript SDKs.</p> </note>

        Args:
            device_arn: <p>The ARN of the device to retrieve.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_braket.types.get_device_request.GetDeviceRequest]",
        ) -> OperationResponse[
            "capo_braket.types.get_device_response.GetDeviceResponse"
        ]:
            import capo_braket._operations.braket.get_device

            output, http_response = (
                capo_braket._operations.braket.get_device.get_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDevice")
        )
        input_: capo_braket.types.get_device_request.GetDeviceRequest = {
            "device_arn": device_arn
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
        filters: "capo_braket.types.search_devices_filter_list.SearchDevicesFilterList",
        *,
        config_overrides: Optional[BraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_devices_response.SearchDevicesResponse":
        """<p>Searches for devices using the specified filters.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchDevicesFilter objects to use when searching for devices.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_braket.types.search_devices_request.SearchDevicesRequest]",
        ) -> OperationResponse[
            "capo_braket.types.search_devices_response.SearchDevicesResponse"
        ]:
            import capo_braket._operations.braket.search_devices

            output, http_response = (
                capo_braket._operations.braket.search_devices.search_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SearchDevices")
        )
        input_: capo_braket.types.search_devices_request.SearchDevicesRequest = {
            "filters": filters
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


class AsyncDeviceResource:
    def __init__(self, service: AsyncBraketClient) -> None:
        self._service = service

    async def read(
        self,
        device_arn: "capo_braket.types.device_arn.DeviceArn",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
    ) -> "capo_braket.types.get_device_response.GetDeviceResponse":
        """<p>Retrieves the devices available in Amazon Braket.</p> <note> <p>For backwards compatibility with older versions of BraketSchemas, OpenQASM information is omitted from GetDevice API calls. To get this information the user-agent needs to present a recent version of the BraketSchemas (1.8.0 or later). The Braket SDK automatically reports this for you. If you do not see OpenQASM results in the GetDevice response when using a Braket SDK, you may need to set AWS_EXECUTION_ENV environment variable to configure user-agent. See the code examples provided below for how to do this for the AWS CLI, Boto3, and the Go, Java, and JavaScript/TypeScript SDKs.</p> </note>

        Args:
            device_arn: <p>The ARN of the device to retrieve.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.get_device_request.GetDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.get_device_response.GetDeviceResponse"
        ]:
            import capo_braket._operations.braket.get_device

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.get_device.async_get_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetDevice")
        )
        input_: capo_braket.types.get_device_request.GetDeviceRequest = {
            "device_arn": device_arn
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
        filters: "capo_braket.types.search_devices_filter_list.SearchDevicesFilterList",
        *,
        config_overrides: Optional[AsyncBraketClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_braket.types.search_devices_response.SearchDevicesResponse":
        """<p>Searches for devices using the specified filters.</p>

        Args:
            next_token: <p>A token used for pagination of results returned in the response. Use the token returned from the previous request to continue search where the previous request ended.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            filters: <p>Array of SearchDevicesFilter objects to use when searching for devices.</p>

        Raises:
            capo_braket.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_braket.errors.internal_service_exception.InternalServiceException: <p>The request failed because of an unknown error.</p>
            capo_braket.errors.throttling_exception.ThrottlingException: <p>The API throttling rate limit is exceeded.</p>
            capo_braket.errors.validation_exception.ValidationException: <p>The input request failed to satisfy constraints expected by Amazon Braket.</p>
            capo_braket.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_braket.types.search_devices_request.SearchDevicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_braket.types.search_devices_response.SearchDevicesResponse"
        ]:
            import capo_braket._operations.braket.search_devices

            (
                output,
                http_response,
            ) = await capo_braket._operations.braket.search_devices.async_search_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("SearchDevices")
        )
        input_: capo_braket.types.search_devices_request.SearchDevicesRequest = {
            "filters": filters
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
