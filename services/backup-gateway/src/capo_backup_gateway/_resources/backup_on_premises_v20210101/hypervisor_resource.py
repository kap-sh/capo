from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

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
    import capo_backup_gateway.types.delete_hypervisor_input
    import capo_backup_gateway.types.delete_hypervisor_output
    import capo_backup_gateway.types.get_hypervisor_input
    import capo_backup_gateway.types.get_hypervisor_output
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.import_hypervisor_configuration_input
    import capo_backup_gateway.types.import_hypervisor_configuration_output
    import capo_backup_gateway.types.kms_key_arn
    import capo_backup_gateway.types.list_hypervisors_input
    import capo_backup_gateway.types.list_hypervisors_output
    import capo_backup_gateway.types.log_group_arn
    import capo_backup_gateway.types.max_results
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.next_token
    import capo_backup_gateway.types.password
    import capo_backup_gateway.types.server_arn
    import capo_backup_gateway.types.start_virtual_machines_metadata_sync_input
    import capo_backup_gateway.types.start_virtual_machines_metadata_sync_output
    import capo_backup_gateway.types.tags
    import capo_backup_gateway.types.update_hypervisor_input
    import capo_backup_gateway.types.update_hypervisor_output
    import capo_backup_gateway.types.username
    from capo_backup_gateway._services.async_backup_gateway import (
        AsyncBackupGatewayClient,
        AsyncBackupGatewayClientConfig,
    )
    from capo_backup_gateway._services.backup_gateway import (
        BackupGatewayClient,
        BackupGatewayClientConfig,
    )


class HypervisorResource:
    def __init__(self, service: BackupGatewayClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_backup_gateway.types.name.Name",
        host: "capo_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
        kms_key_arn: Optional["capo_backup_gateway.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_backup_gateway.types.tags.Tags"] = None,
    ) -> "capo_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput":
        """<p>Connect to a hypervisor by importing its configuration.</p>

        Args:
            name: <p>The name of the hypervisor.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
            kms_key_arn: <p>The Key Management Service for the hypervisor.</p>
            tags: <p>The tags of the hypervisor configuration to import.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration.import_hypervisor_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput",
        ) -> dict[str, Any]:
            import capo_backup_gateway.types.import_hypervisor_configuration_input

            return capo_backup_gateway.types.import_hypervisor_configuration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ImportHypervisorConfiguration", redact_input=_redact_input
            ),
        )
        input_: capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput = {
            "name": name,
            "host": host,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput":
        """<p>This action requests information about the specified hypervisor to which the gateway will connect. A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_hypervisor_input.GetHypervisorInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor.get_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetHypervisor")
        )
        input_: capo_backup_gateway.types.get_hypervisor_input.GetHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
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
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        host: Optional["capo_backup_gateway.types.host.Host"] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
        name: Optional["capo_backup_gateway.types.name.Name"] = None,
        log_group_arn: Optional[
            "capo_backup_gateway.types.log_group_arn.LogGroupArn"
        ] = None,
    ) -> "capo_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput":
        """<p>Updates a hypervisor metadata, including its host, username, and password. Specify which hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your request.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to update.</p>
            host: <p>The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The updated username for the hypervisor.</p>
            password: <p>The updated password for the hypervisor.</p>
            name: <p>The updated name for the hypervisor</p>
            log_group_arn: <p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor.update_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput",
        ) -> dict[str, Any]:
            import capo_backup_gateway.types.update_hypervisor_input

            return capo_backup_gateway.types.update_hypervisor_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateHypervisor", redact_input=_redact_input),
        )
        input_: capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
        }
        if host is not None:
            input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if name is not None:
            input_["name"] = name
        if log_group_arn is not None:
            input_["log_group_arn"] = log_group_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput":
        """<p>Deletes a hypervisor.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to delete.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor.delete_hypervisor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteHypervisor")
        )
        input_: capo_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
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
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput":
        """<p>Lists your hypervisors.</p>

        Args:
            max_results: <p>The maximum number of hypervisors to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors.list_hypervisors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHypervisors")
        )
        input_: capo_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput = {}
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

    def start_virtual_machines_metadata_sync(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput":
        """<p>This action sends a request to sync metadata across the specified virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync.start_virtual_machines_metadata_sync(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartVirtualMachinesMetadataSync")
        )
        input_: capo_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput = {
            "hypervisor_arn": hypervisor_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncHypervisorResource:
    def __init__(self, service: AsyncBackupGatewayClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_backup_gateway.types.name.Name",
        host: "capo_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
        kms_key_arn: Optional["capo_backup_gateway.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_backup_gateway.types.tags.Tags"] = None,
    ) -> "capo_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput":
        """<p>Connect to a hypervisor by importing its configuration.</p>

        Args:
            name: <p>The name of the hypervisor.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>
            kms_key_arn: <p>The Key Management Service for the hypervisor.</p>
            tags: <p>The tags of the hypervisor configuration to import.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.import_hypervisor_configuration_output.ImportHypervisorConfigurationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.import_hypervisor_configuration.async_import_hypervisor_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput",
        ) -> dict[str, Any]:
            import capo_backup_gateway.types.import_hypervisor_configuration_input

            return capo_backup_gateway.types.import_hypervisor_configuration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ImportHypervisorConfiguration", redact_input=_redact_input
            ),
        )
        input_: capo_backup_gateway.types.import_hypervisor_configuration_input.ImportHypervisorConfigurationInput = {
            "name": name,
            "host": host,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput":
        """<p>This action requests information about the specified hypervisor to which the gateway will connect. A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.get_hypervisor_input.GetHypervisorInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.get_hypervisor_output.GetHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.get_hypervisor.async_get_hypervisor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetHypervisor")
        )
        input_: capo_backup_gateway.types.get_hypervisor_input.GetHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
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
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        host: Optional["capo_backup_gateway.types.host.Host"] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
        name: Optional["capo_backup_gateway.types.name.Name"] = None,
        log_group_arn: Optional[
            "capo_backup_gateway.types.log_group_arn.LogGroupArn"
        ] = None,
    ) -> "capo_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput":
        """<p>Updates a hypervisor metadata, including its host, username, and password. Specify which hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your request.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to update.</p>
            host: <p>The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The updated username for the hypervisor.</p>
            password: <p>The updated password for the hypervisor.</p>
            name: <p>The updated name for the hypervisor</p>
            log_group_arn: <p>The Amazon Resource Name (ARN) of the group of gateways within the requested log.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.update_hypervisor_output.UpdateHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.update_hypervisor.async_update_hypervisor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput",
        ) -> dict[str, Any]:
            import capo_backup_gateway.types.update_hypervisor_input

            return capo_backup_gateway.types.update_hypervisor_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateHypervisor", redact_input=_redact_input),
        )
        input_: capo_backup_gateway.types.update_hypervisor_input.UpdateHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
        }
        if host is not None:
            input_["host"] = host
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if name is not None:
            input_["name"] = name
        if log_group_arn is not None:
            input_["log_group_arn"] = log_group_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput":
        """<p>Deletes a hypervisor.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor to delete.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.delete_hypervisor_output.DeleteHypervisorOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.delete_hypervisor.async_delete_hypervisor(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteHypervisor")
        )
        input_: capo_backup_gateway.types.delete_hypervisor_input.DeleteHypervisorInput = {
            "hypervisor_arn": hypervisor_arn
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
        max_results: Optional[
            "capo_backup_gateway.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_backup_gateway.types.next_token.NextToken"] = None,
    ) -> "capo_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput":
        """<p>Lists your hypervisors.</p>

        Args:
            max_results: <p>The maximum number of hypervisors to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>maxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.list_hypervisors_output.ListHypervisorsOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.list_hypervisors.async_list_hypervisors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListHypervisors")
        )
        input_: capo_backup_gateway.types.list_hypervisors_input.ListHypervisorsInput = {}
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

    async def start_virtual_machines_metadata_sync(
        self,
        hypervisor_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput":
        """<p>This action sends a request to sync metadata across the specified virtual machines.</p>

        Args:
            hypervisor_arn: <p>The Amazon Resource Name (ARN) of the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.access_denied_exception.AccessDeniedException: <p>The operation cannot proceed because you have insufficient permissions.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.start_virtual_machines_metadata_sync_output.StartVirtualMachinesMetadataSyncOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.start_virtual_machines_metadata_sync.async_start_virtual_machines_metadata_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartVirtualMachinesMetadataSync")
        )
        input_: capo_backup_gateway.types.start_virtual_machines_metadata_sync_input.StartVirtualMachinesMetadataSyncInput = {
            "hypervisor_arn": hypervisor_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
