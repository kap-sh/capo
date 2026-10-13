from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_snow_device_management._auth._signers
import capo_snow_device_management._auth._sigv4
from capo_snow_device_management._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_snow_device_management.types.describe_device_ec2_input
    import capo_snow_device_management.types.describe_device_ec2_output
    import capo_snow_device_management.types.describe_device_input
    import capo_snow_device_management.types.describe_device_output
    import capo_snow_device_management.types.device_summary
    import capo_snow_device_management.types.instance_ids_list
    import capo_snow_device_management.types.job_id
    import capo_snow_device_management.types.list_device_resources_input
    import capo_snow_device_management.types.list_device_resources_output
    import capo_snow_device_management.types.list_devices_input
    import capo_snow_device_management.types.list_devices_output
    import capo_snow_device_management.types.managed_device_id
    import capo_snow_device_management.types.max_results
    import capo_snow_device_management.types.next_token
    import capo_snow_device_management.types.resource_summary
    from capo_snow_device_management._services.async_snow_device_management import (
        AsyncSnowDeviceManagementClient,
        AsyncSnowDeviceManagementClientConfig,
    )
    from capo_snow_device_management._services.snow_device_management import (
        SnowDeviceManagementClient,
        SnowDeviceManagementClientConfig,
    )


class ManagedDevice:
    def __init__(self, service: SnowDeviceManagementClient) -> None:
        self._service = service

    def read(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> (
        "capo_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
    ):
        """<p>Checks device-specific information, such as the device type, software version, IP addresses, and lock status.</p>

        Args:
            managed_device_id: <p>The ID of the device that you are checking the information of.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_device_input.DescribeDeviceInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_device

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_device.describe_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeDevice")
        )
        input_: capo_snow_device_management.types.describe_device_input.DescribeDeviceInput = {
            "managed_device_id": managed_device_id
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
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        job_id: Optional["capo_snow_device_management.types.job_id.JobId"] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_devices_output.ListDevicesOutput":
        """<p>Returns a list of all devices on your Amazon Web Services account that have Amazon Web Services Snow Device Management enabled in the Amazon Web Services Region where the command is run.</p>

        Args:
            job_id: <p>The ID of the job used to order the device.</p>
            max_results: <p>The maximum number of devices to list per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_devices_input.ListDevicesInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_devices_output.ListDevicesOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_devices

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_devices.list_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDevices")
        )
        input_: capo_snow_device_management.types.list_devices_input.ListDevicesInput = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_device_ec2_instances(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        instance_ids: "capo_snow_device_management.types.instance_ids_list.InstanceIdsList",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output":
        """<p>Checks the current state of the Amazon EC2 instances. The output is similar to <code>describeDevice</code>, but the results are sourced from the device cache in the Amazon Web Services Cloud and include a subset of the available fields. </p>

        Args:
            managed_device_id: <p>The ID of the managed device.</p>
            instance_ids: <p>A list of instance IDs associated with the managed device.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_device_ec2_instances

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.describe_device_ec2_instances.describe_device_ec2_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeDeviceEc2Instances")
        )
        input_: capo_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input = {
            "managed_device_id": managed_device_id,
            "instance_ids": instance_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_device_resources(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[SnowDeviceManagementClientConfig] = None,
        type: Optional[str] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput":
        """<p>Returns a list of the Amazon Web Services resources available for a device. Currently, Amazon EC2 instances are the only supported resource type.</p>

        Args:
            managed_device_id: <p>The ID of the managed device that you are listing the resources of.</p>
            type: <p>A structure used to filter the results by type of resource.</p>
            max_results: <p>The maximum number of resources per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput]",
        ) -> OperationResponse[
            "capo_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_device_resources

            output, http_response = (
                capo_snow_device_management._operations.snow_device_management.list_device_resources.list_device_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDeviceResources")
        )
        input_: capo_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput = {
            "managed_device_id": managed_device_id
        }
        if type is not None:
            input_["type"] = type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncManagedDevice:
    def __init__(self, service: AsyncSnowDeviceManagementClient) -> None:
        self._service = service

    async def read(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> (
        "capo_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
    ):
        """<p>Checks device-specific information, such as the device type, software version, IP addresses, and lock status.</p>

        Args:
            managed_device_id: <p>The ID of the device that you are checking the information of.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.describe_device_input.DescribeDeviceInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.describe_device_output.DescribeDeviceOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_device

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.describe_device.async_describe_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeDevice")
        )
        input_: capo_snow_device_management.types.describe_device_input.DescribeDeviceInput = {
            "managed_device_id": managed_device_id
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
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        job_id: Optional["capo_snow_device_management.types.job_id.JobId"] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_devices_output.ListDevicesOutput":
        """<p>Returns a list of all devices on your Amazon Web Services account that have Amazon Web Services Snow Device Management enabled in the Amazon Web Services Region where the command is run.</p>

        Args:
            job_id: <p>The ID of the job used to order the device.</p>
            max_results: <p>The maximum number of devices to list per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.list_devices_input.ListDevicesInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.list_devices_output.ListDevicesOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_devices

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.list_devices.async_list_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDevices")
        )
        input_: capo_snow_device_management.types.list_devices_input.ListDevicesInput = {}
        if job_id is not None:
            input_["job_id"] = job_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_device_ec2_instances(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        instance_ids: "capo_snow_device_management.types.instance_ids_list.InstanceIdsList",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
    ) -> "capo_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output":
        """<p>Checks the current state of the Amazon EC2 instances. The output is similar to <code>describeDevice</code>, but the results are sourced from the device cache in the Amazon Web Services Cloud and include a subset of the available fields. </p>

        Args:
            managed_device_id: <p>The ID of the managed device.</p>
            instance_ids: <p>A list of instance IDs associated with the managed device.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.describe_device_ec2_output.DescribeDeviceEc2Output"
        ]:
            import capo_snow_device_management._operations.snow_device_management.describe_device_ec2_instances

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.describe_device_ec2_instances.async_describe_device_ec2_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DescribeDeviceEc2Instances")
        )
        input_: capo_snow_device_management.types.describe_device_ec2_input.DescribeDeviceEc2Input = {
            "managed_device_id": managed_device_id,
            "instance_ids": instance_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_device_resources(
        self,
        managed_device_id: "capo_snow_device_management.types.managed_device_id.ManagedDeviceId",
        *,
        config_overrides: Optional[AsyncSnowDeviceManagementClientConfig] = None,
        type: Optional[str] = None,
        max_results: Optional[
            "capo_snow_device_management.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_snow_device_management.types.next_token.NextToken"
        ] = None,
    ) -> "capo_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput":
        """<p>Returns a list of the Amazon Web Services resources available for a device. Currently, Amazon EC2 instances are the only supported resource type.</p>

        Args:
            managed_device_id: <p>The ID of the managed device that you are listing the resources of.</p>
            type: <p>A structure used to filter the results by type of resource.</p>
            max_results: <p>The maximum number of resources per page.</p>
            next_token: <p>A pagination token to continue to the next page of results.</p>

        Raises:
            capo_snow_device_management.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_snow_device_management.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing the request.</p>
            capo_snow_device_management.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that doesn't exist.</p>
            capo_snow_device_management.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_snow_device_management.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_snow_device_management.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_snow_device_management.types.list_device_resources_output.ListDeviceResourcesOutput"
        ]:
            import capo_snow_device_management._operations.snow_device_management.list_device_resources

            (
                output,
                http_response,
            ) = await capo_snow_device_management._operations.snow_device_management.list_device_resources.async_list_device_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDeviceResources")
        )
        input_: capo_snow_device_management.types.list_device_resources_input.ListDeviceResourcesInput = {
            "managed_device_id": managed_device_id
        }
        if type is not None:
            input_["type"] = type
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
