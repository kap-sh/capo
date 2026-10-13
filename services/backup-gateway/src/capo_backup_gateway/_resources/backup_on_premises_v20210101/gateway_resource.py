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
    import capo_backup_gateway.types.activation_key
    import capo_backup_gateway.types.associate_gateway_to_server_input
    import capo_backup_gateway.types.associate_gateway_to_server_output
    import capo_backup_gateway.types.create_gateway_input
    import capo_backup_gateway.types.create_gateway_output
    import capo_backup_gateway.types.day_of_month
    import capo_backup_gateway.types.day_of_week
    import capo_backup_gateway.types.delete_gateway_input
    import capo_backup_gateway.types.delete_gateway_output
    import capo_backup_gateway.types.disassociate_gateway_from_server_input
    import capo_backup_gateway.types.disassociate_gateway_from_server_output
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.gateway_type
    import capo_backup_gateway.types.get_gateway_input
    import capo_backup_gateway.types.get_gateway_output
    import capo_backup_gateway.types.host
    import capo_backup_gateway.types.hour_of_day
    import capo_backup_gateway.types.list_gateways_input
    import capo_backup_gateway.types.list_gateways_output
    import capo_backup_gateway.types.max_results
    import capo_backup_gateway.types.minute_of_hour
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.next_token
    import capo_backup_gateway.types.password
    import capo_backup_gateway.types.put_maintenance_start_time_input
    import capo_backup_gateway.types.put_maintenance_start_time_output
    import capo_backup_gateway.types.server_arn
    import capo_backup_gateway.types.tags
    import capo_backup_gateway.types.test_hypervisor_configuration_input
    import capo_backup_gateway.types.test_hypervisor_configuration_output
    import capo_backup_gateway.types.update_gateway_information_input
    import capo_backup_gateway.types.update_gateway_information_output
    import capo_backup_gateway.types.update_gateway_software_now_input
    import capo_backup_gateway.types.update_gateway_software_now_output
    import capo_backup_gateway.types.username
    from capo_backup_gateway._services.async_backup_gateway import (
        AsyncBackupGatewayClient,
        AsyncBackupGatewayClientConfig,
    )
    from capo_backup_gateway._services.backup_gateway import (
        BackupGatewayClient,
        BackupGatewayClientConfig,
    )


class GatewayResource:
    def __init__(self, service: BackupGatewayClient) -> None:
        self._service = service

    def create(
        self,
        activation_key: "capo_backup_gateway.types.activation_key.ActivationKey",
        gateway_display_name: "capo_backup_gateway.types.name.Name",
        gateway_type: "capo_backup_gateway.types.gateway_type.GatewayType",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        tags: Optional["capo_backup_gateway.types.tags.Tags"] = None,
    ) -> "capo_backup_gateway.types.create_gateway_output.CreateGatewayOutput":
        """<p>Creates a backup gateway. After you create a gateway, you can associate it with a server using the <code>AssociateGatewayToServer</code> operation.</p>

        Args:
            activation_key: <p>The activation key of the created gateway.</p>
            gateway_display_name: <p>The display name of the created gateway.</p>
            gateway_type: <p>The type of created gateway.</p>
            tags: <p>A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.create_gateway_input.CreateGatewayInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.create_gateway_output.CreateGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.create_gateway

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGateway")
        )
        input_: capo_backup_gateway.types.create_gateway_input.CreateGatewayInput = {
            "activation_key": activation_key,
            "gateway_display_name": gateway_display_name,
            "gateway_type": gateway_type,
        }
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
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_gateway_output.GetGatewayOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.get_gateway_input.GetGatewayInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.get_gateway_output.GetGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_gateway

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.get_gateway.get_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetGateway")
        )
        input_: capo_backup_gateway.types.get_gateway_input.GetGatewayInput = {
            "gateway_arn": gateway_arn
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
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        gateway_display_name: Optional["capo_backup_gateway.types.name.Name"] = None,
    ) -> "capo_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput":
        """<p>Updates a gateway's name. Specify which gateway to update using the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to update.</p>
            gateway_display_name: <p>The updated display name of the gateway.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information.update_gateway_information(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGatewayInformation")
        )
        input_: capo_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput = {
            "gateway_arn": gateway_arn
        }
        if gateway_display_name is not None:
            input_["gateway_display_name"] = gateway_display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput":
        """<p>Deletes a backup gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to delete.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.delete_gateway_input.DeleteGatewayInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGateway")
        )
        input_: capo_backup_gateway.types.delete_gateway_input.DeleteGatewayInput = {
            "gateway_arn": gateway_arn
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
    ) -> "capo_backup_gateway.types.list_gateways_output.ListGatewaysOutput":
        """<p>Lists backup gateways owned by an Amazon Web Services account in an Amazon Web Services Region. The returned list is ordered by gateway Amazon Resource Name (ARN).</p>

        Args:
            max_results: <p>The maximum number of gateways to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.list_gateways_input.ListGatewaysInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.list_gateways_output.ListGatewaysOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_gateways

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGateways")
        )
        input_: capo_backup_gateway.types.list_gateways_input.ListGatewaysInput = {}
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

    def associate_gateway_to_server(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        server_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput":
        """<p>Associates a backup gateway with your server. After you complete the association process, you can back up and restore your VMs through the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            server_arn: <p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server.associate_gateway_to_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateGatewayToServer")
        )
        input_: capo_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput = {
            "gateway_arn": gateway_arn,
            "server_arn": server_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_gateway_from_server(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput":
        """<p>Disassociates a backup gateway from the specified server. After the disassociation process finishes, the gateway can no longer access the virtual machines on the server.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to disassociate.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server.disassociate_gateway_from_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateGatewayFromServer")
        )
        input_: capo_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_maintenance_start_time(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        hour_of_day: "capo_backup_gateway.types.hour_of_day.HourOfDay",
        minute_of_hour: "capo_backup_gateway.types.minute_of_hour.MinuteOfHour",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        day_of_week: Optional["capo_backup_gateway.types.day_of_week.DayOfWeek"] = None,
        day_of_month: Optional[
            "capo_backup_gateway.types.day_of_month.DayOfMonth"
        ] = None,
    ) -> "capo_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput":
        """<p>Set the maintenance start time for a gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.</p>
            hour_of_day: <p>The hour of the day to start maintenance on a gateway.</p>
            minute_of_hour: <p>The minute of the hour to start maintenance on a gateway.</p>
            day_of_week: <p>The day of the week to start maintenance on a gateway.</p>
            day_of_month: <p>The day of the month start maintenance on a gateway.</p> <p>Valid values range from <code>Sunday</code> to <code>Saturday</code>.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time.put_maintenance_start_time(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutMaintenanceStartTime")
        )
        input_: capo_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput = {
            "gateway_arn": gateway_arn,
            "hour_of_day": hour_of_day,
            "minute_of_hour": minute_of_hour,
        }
        if day_of_week is not None:
            input_["day_of_week"] = day_of_week
        if day_of_month is not None:
            input_["day_of_month"] = day_of_month

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_hypervisor_configuration(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        host: "capo_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
    ) -> "capo_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput":
        """<p>Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration.test_hypervisor_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput",
        ) -> dict[str, Any]:
            import capo_backup_gateway.types.test_hypervisor_configuration_input

            return capo_backup_gateway.types.test_hypervisor_configuration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("TestHypervisorConfiguration", redact_input=_redact_input),
        )
        input_: capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput = {
            "gateway_arn": gateway_arn,
            "host": host,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_software_now(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[BackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput":
        """<p>Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.</p> <note> <p>When you make this request, you get a <code>200 OK</code> success response immediately. However, it might take some time for the update to complete.</p> </note>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to be updated.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput]",
        ) -> OperationResponse[
            "capo_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now

            output, http_response = (
                capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now.update_gateway_software_now(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGatewaySoftwareNow")
        )
        input_: capo_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput = {
            "gateway_arn": gateway_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncGatewayResource:
    def __init__(self, service: AsyncBackupGatewayClient) -> None:
        self._service = service

    async def create(
        self,
        activation_key: "capo_backup_gateway.types.activation_key.ActivationKey",
        gateway_display_name: "capo_backup_gateway.types.name.Name",
        gateway_type: "capo_backup_gateway.types.gateway_type.GatewayType",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        tags: Optional["capo_backup_gateway.types.tags.Tags"] = None,
    ) -> "capo_backup_gateway.types.create_gateway_output.CreateGatewayOutput":
        """<p>Creates a backup gateway. After you create a gateway, you can associate it with a server using the <code>AssociateGatewayToServer</code> operation.</p>

        Args:
            activation_key: <p>The activation key of the created gateway.</p>
            gateway_display_name: <p>The display name of the created gateway.</p>
            gateway_type: <p>The type of created gateway.</p>
            tags: <p>A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.create_gateway_input.CreateGatewayInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.create_gateway_output.CreateGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.create_gateway

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("CreateGateway")
        )
        input_: capo_backup_gateway.types.create_gateway_input.CreateGatewayInput = {
            "activation_key": activation_key,
            "gateway_display_name": gateway_display_name,
            "gateway_type": gateway_type,
        }
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
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.get_gateway_output.GetGatewayOutput":
        """<p>By providing the ARN (Amazon Resource Name), this API returns the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.get_gateway_input.GetGatewayInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.get_gateway_output.GetGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.get_gateway

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.get_gateway.async_get_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetGateway")
        )
        input_: capo_backup_gateway.types.get_gateway_input.GetGatewayInput = {
            "gateway_arn": gateway_arn
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
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        gateway_display_name: Optional["capo_backup_gateway.types.name.Name"] = None,
    ) -> "capo_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput":
        """<p>Updates a gateway's name. Specify which gateway to update using the Amazon Resource Name (ARN) of the gateway in your request.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to update.</p>
            gateway_display_name: <p>The updated display name of the gateway.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.update_gateway_information_output.UpdateGatewayInformationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_information.async_update_gateway_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGatewayInformation")
        )
        input_: capo_backup_gateway.types.update_gateway_information_input.UpdateGatewayInformationInput = {
            "gateway_arn": gateway_arn
        }
        if gateway_display_name is not None:
            input_["gateway_display_name"] = gateway_display_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput":
        """<p>Deletes a backup gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to delete.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.delete_gateway_input.DeleteGatewayInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.delete_gateway_output.DeleteGatewayOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteGateway")
        )
        input_: capo_backup_gateway.types.delete_gateway_input.DeleteGatewayInput = {
            "gateway_arn": gateway_arn
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
    ) -> "capo_backup_gateway.types.list_gateways_output.ListGatewaysOutput":
        """<p>Lists backup gateways owned by an Amazon Web Services account in an Amazon Web Services Region. The returned list is ordered by gateway Amazon Resource Name (ARN).</p>

        Args:
            max_results: <p>The maximum number of gateways to list.</p>
            next_token: <p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.list_gateways_input.ListGatewaysInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.list_gateways_output.ListGatewaysOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.list_gateways

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListGateways")
        )
        input_: capo_backup_gateway.types.list_gateways_input.ListGatewaysInput = {}
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

    async def associate_gateway_to_server(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        server_arn: "capo_backup_gateway.types.server_arn.ServerArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput":
        """<p>Associates a backup gateway with your server. After you complete the association process, you can back up and restore your VMs through the gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>
            server_arn: <p>The Amazon Resource Name (ARN) of the server that hosts your virtual machines.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.associate_gateway_to_server_output.AssociateGatewayToServerOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.associate_gateway_to_server.async_associate_gateway_to_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateGatewayToServer")
        )
        input_: capo_backup_gateway.types.associate_gateway_to_server_input.AssociateGatewayToServerInput = {
            "gateway_arn": gateway_arn,
            "server_arn": server_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_gateway_from_server(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput":
        """<p>Disassociates a backup gateway from the specified server. After the disassociation process finishes, the gateway can no longer access the virtual machines on the server.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to disassociate.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.disassociate_gateway_from_server_output.DisassociateGatewayFromServerOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.disassociate_gateway_from_server.async_disassociate_gateway_from_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateGatewayFromServer")
        )
        input_: capo_backup_gateway.types.disassociate_gateway_from_server_input.DisassociateGatewayFromServerInput = {
            "gateway_arn": gateway_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_maintenance_start_time(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        hour_of_day: "capo_backup_gateway.types.hour_of_day.HourOfDay",
        minute_of_hour: "capo_backup_gateway.types.minute_of_hour.MinuteOfHour",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        day_of_week: Optional["capo_backup_gateway.types.day_of_week.DayOfWeek"] = None,
        day_of_month: Optional[
            "capo_backup_gateway.types.day_of_month.DayOfMonth"
        ] = None,
    ) -> "capo_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput":
        """<p>Set the maintenance start time for a gateway.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.</p>
            hour_of_day: <p>The hour of the day to start maintenance on a gateway.</p>
            minute_of_hour: <p>The minute of the hour to start maintenance on a gateway.</p>
            day_of_week: <p>The day of the week to start maintenance on a gateway.</p>
            day_of_month: <p>The day of the month start maintenance on a gateway.</p> <p>Valid values range from <code>Sunday</code> to <code>Saturday</code>.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.put_maintenance_start_time_output.PutMaintenanceStartTimeOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.put_maintenance_start_time.async_put_maintenance_start_time(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutMaintenanceStartTime")
        )
        input_: capo_backup_gateway.types.put_maintenance_start_time_input.PutMaintenanceStartTimeInput = {
            "gateway_arn": gateway_arn,
            "hour_of_day": hour_of_day,
            "minute_of_hour": minute_of_hour,
        }
        if day_of_week is not None:
            input_["day_of_week"] = day_of_week
        if day_of_month is not None:
            input_["day_of_month"] = day_of_month

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_hypervisor_configuration(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        host: "capo_backup_gateway.types.host.Host",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
        username: Optional["capo_backup_gateway.types.username.Username"] = None,
        password: Optional["capo_backup_gateway.types.password.Password"] = None,
    ) -> "capo_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput":
        """<p>Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.</p>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.</p>
            host: <p>The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).</p>
            username: <p>The username for the hypervisor.</p>
            password: <p>The password for the hypervisor.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.conflict_exception.ConflictException: <p>The operation cannot proceed because it is not supported.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.test_hypervisor_configuration_output.TestHypervisorConfigurationOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.test_hypervisor_configuration.async_test_hypervisor_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput",
        ) -> dict[str, Any]:
            import capo_backup_gateway.types.test_hypervisor_configuration_input

            return capo_backup_gateway.types.test_hypervisor_configuration_input.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("TestHypervisorConfiguration", redact_input=_redact_input),
        )
        input_: capo_backup_gateway.types.test_hypervisor_configuration_input.TestHypervisorConfigurationInput = {
            "gateway_arn": gateway_arn,
            "host": host,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_gateway_software_now(
        self,
        gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn",
        *,
        config_overrides: Optional[AsyncBackupGatewayClientConfig] = None,
    ) -> "capo_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput":
        """<p>Updates the gateway virtual machine (VM) software. The request immediately triggers the software update.</p> <note> <p>When you make this request, you get a <code>200 OK</code> success response immediately. However, it might take some time for the update to complete.</p> </note>

        Args:
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to be updated.</p>

        Raises:
            capo_backup_gateway.errors.internal_server_exception.InternalServerException: <p>The operation did not succeed because an internal error occurred. Try again later.</p>
            capo_backup_gateway.errors.throttling_exception.ThrottlingException: <p>TPS has been limited to protect against intentional or unintentional high request volumes.</p>
            capo_backup_gateway.errors.validation_exception.ValidationException: <p>The operation did not succeed because a validation error occurred.</p>
            capo_backup_gateway.errors.resource_not_found_exception.ResourceNotFoundException: <p>A resource that is required for the action wasn't found.</p>
            capo_backup_gateway.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput]",
        ) -> AsyncOperationResponse[
            "capo_backup_gateway.types.update_gateway_software_now_output.UpdateGatewaySoftwareNowOutput"
        ]:
            import capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now

            (
                output,
                http_response,
            ) = await capo_backup_gateway._operations.backup_on_premises_v20210101.update_gateway_software_now.async_update_gateway_software_now(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateGatewaySoftwareNow")
        )
        input_: capo_backup_gateway.types.update_gateway_software_now_input.UpdateGatewaySoftwareNowInput = {
            "gateway_arn": gateway_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
