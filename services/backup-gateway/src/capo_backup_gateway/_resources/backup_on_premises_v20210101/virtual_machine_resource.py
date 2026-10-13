from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_backup_gateway._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_backup_gateway.types.get_virtual_machine_input
    import capo_backup_gateway.types.get_virtual_machine_output
    import capo_backup_gateway.types.list_virtual_machines_input
    import capo_backup_gateway.types.list_virtual_machines_output
    import capo_backup_gateway.types.max_results
    import capo_backup_gateway.types.next_token
    import capo_backup_gateway.types.resource_arn
    import capo_backup_gateway.types.server_arn
    from capo_backup_gateway._services.async_backup_gateway import (
        AsyncBackupGatewayClient,
        AsyncBackupGatewayClientConfig,
    )
    from capo_backup_gateway._services.backup_gateway import (
        BackupGatewayClient,
        BackupGatewayClientConfig,
    )


class VirtualMachineResource:
    def __init__(self, service: BackupGatewayClient) -> None:
        self._service = service

    def read(
        self,
        resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the virtual machine.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the virtual machine.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine.get_virtual_machine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetVirtualMachine")
        )
        input_: capo_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput = {
            "resource_arn": resource_arn
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
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        hypervisor_arn: Optional[
            "capo_backup_gateway.types.server_arn.ServerArn"
        ] = None,
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput":
        """<p>Lists your virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor connected to your virtual machine.</p>
            max_results: <p>The maximum number of virtual machines to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines.list_virtual_machines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListVirtualMachines")
        )
        input_: capo_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput = {}
        if hypervisor_arn is not None:
            input_["hypervisor_arn"] = hypervisor_arn
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


class AsyncVirtualMachineResource:
    def __init__(self, service: AsyncBackupGatewayClient) -> None:
        self._service = service

    async def read(
        self,
        resource_arn: "capo_backup_gateway.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the virtual machine.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the virtual machine.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.get_virtual_machine_output.GetVirtualMachineOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.get_virtual_machine.async_get_virtual_machine(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetVirtualMachine")
        )
        input_: capo_backup_gateway.types.get_virtual_machine_input.GetVirtualMachineInput = {
            "resource_arn": resource_arn
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
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        hypervisor_arn: Optional[
            "capo_backup_gateway.types.server_arn.ServerArn"
        ] = None,
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput":
        """<p>Lists your virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor connected to your virtual machine.</p>
            max_results: <p>The maximum number of virtual machines to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.list_virtual_machines_output.ListVirtualMachinesOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.list_virtual_machines.async_list_virtual_machines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListVirtualMachines")
        )
        input_: capo_backup_gateway.types.list_virtual_machines_input.ListVirtualMachinesInput = {}
        if hypervisor_arn is not None:
            input_["hypervisor_arn"] = hypervisor_arn
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
