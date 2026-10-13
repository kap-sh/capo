from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_datazone.types.delete_environment_blueprint_configuration_input
    import capo_datazone.types.delete_environment_blueprint_configuration_output
    import capo_datazone.types.domain_id
    import capo_datazone.types.enabled_region_list
    import capo_datazone.types.environment_blueprint_configuration_item
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.get_environment_blueprint_configuration_input
    import capo_datazone.types.get_environment_blueprint_configuration_output
    import capo_datazone.types.global_parameter_map
    import capo_datazone.types.list_environment_blueprint_configurations_input
    import capo_datazone.types.list_environment_blueprint_configurations_output
    import capo_datazone.types.max_results
    import capo_datazone.types.pagination_token
    import capo_datazone.types.policy_arn
    import capo_datazone.types.provisioning_configuration_list
    import capo_datazone.types.put_environment_blueprint_configuration_input
    import capo_datazone.types.put_environment_blueprint_configuration_output
    import capo_datazone.types.put_resource_configurations
    import capo_datazone.types.regional_parameter_map
    import capo_datazone.types.role_arn
    from capo_datazone._services.async_data_zone import (
        AsyncDataZoneClient,
        AsyncDataZoneClientConfig,
    )
    from capo_datazone._services.data_zone import DataZoneClient, DataZoneClientConfig


class EnvironmentBlueprintConfiguration:
    def __init__(self, service: DataZoneClient) -> None:
        self._service = service

    def put(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        enabled_regions: "capo_datazone.types.enabled_region_list.EnabledRegionList",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        provisioning_role_arn: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        manage_access_role_arn: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        environment_role_permission_boundary: Optional[
            "capo_datazone.types.policy_arn.PolicyArn"
        ] = None,
        regional_parameters: Optional[
            "capo_datazone.types.regional_parameter_map.RegionalParameterMap"
        ] = None,
        resource_configurations: Optional[
            "capo_datazone.types.put_resource_configurations.PutResourceConfigurations"
        ] = None,
        allow_user_provided_configurations: Optional[bool] = None,
        global_parameters: Optional[
            "capo_datazone.types.global_parameter_map.GlobalParameterMap"
        ] = None,
        provisioning_configurations: Optional[
            "capo_datazone.types.provisioning_configuration_list.ProvisioningConfigurationList"
        ] = None,
    ) -> "capo_datazone.types.put_environment_blueprint_configuration_output.PutEnvironmentBlueprintConfigurationOutput":
        """<p>Writes the configuration for the specified environment blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            environment_blueprint_identifier: <p>The identifier of the environment blueprint.</p>
            provisioning_role_arn: <p>The ARN of the provisioning role.</p>
            manage_access_role_arn: <p>The ARN of the manage access role.</p>
            environment_role_permission_boundary: <p>The environment role permissions boundary.</p>
            enabled_regions: <p>Specifies the enabled Amazon Web Services Regions.</p>
            regional_parameters: <p>The regional parameters in the environment blueprint.</p>
            resource_configurations: <p>The resource configurations of the environment blueprint.</p>
            allow_user_provided_configurations: <p>Specifies whether user-provided resource configurations are allowed for the environment blueprint.</p>
            global_parameters: <p>Region-agnostic environment blueprint parameters. </p>
            provisioning_configurations: <p>The provisioning configuration of a blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.put_environment_blueprint_configuration_input.PutEnvironmentBlueprintConfigurationInput]",
        ) -> OperationResponse[
            "capo_datazone.types.put_environment_blueprint_configuration_output.PutEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.put_environment_blueprint_configuration

            output, http_response = (
                capo_datazone._operations.data_zone.put_environment_blueprint_configuration.put_environment_blueprint_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutEnvironmentBlueprintConfiguration")
        )
        input_: capo_datazone.types.put_environment_blueprint_configuration_input.PutEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
            "enabled_regions": enabled_regions,
        }
        if provisioning_role_arn is not None:
            input_["provisioning_role_arn"] = provisioning_role_arn
        if manage_access_role_arn is not None:
            input_["manage_access_role_arn"] = manage_access_role_arn
        if environment_role_permission_boundary is not None:
            input_["environment_role_permission_boundary"] = (
                environment_role_permission_boundary
            )
        if regional_parameters is not None:
            input_["regional_parameters"] = regional_parameters
        if resource_configurations is not None:
            input_["resource_configurations"] = resource_configurations
        if allow_user_provided_configurations is not None:
            input_["allow_user_provided_configurations"] = (
                allow_user_provided_configurations
            )
        if global_parameters is not None:
            input_["global_parameters"] = global_parameters
        if provisioning_configurations is not None:
            input_["provisioning_configurations"] = provisioning_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_blueprint_configuration_output.GetEnvironmentBlueprintConfigurationOutput":
        """<p>Gets the blueprint configuration in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where this blueprint exists.</p>
            environment_blueprint_identifier: <p>He ID of the blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.get_environment_blueprint_configuration_input.GetEnvironmentBlueprintConfigurationInput]",
        ) -> OperationResponse[
            "capo_datazone.types.get_environment_blueprint_configuration_output.GetEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_blueprint_configuration

            output, http_response = (
                capo_datazone._operations.data_zone.get_environment_blueprint_configuration.get_environment_blueprint_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEnvironmentBlueprintConfiguration")
        )
        input_: capo_datazone.types.get_environment_blueprint_configuration_input.GetEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_environment_blueprint_configuration_output.DeleteEnvironmentBlueprintConfigurationOutput":
        """<p>Deletes the blueprint configuration in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the blueprint configuration is deleted.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint the configuration of which is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.delete_environment_blueprint_configuration_input.DeleteEnvironmentBlueprintConfigurationInput]",
        ) -> OperationResponse[
            "capo_datazone.types.delete_environment_blueprint_configuration_output.DeleteEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_environment_blueprint_configuration

            output, http_response = (
                capo_datazone._operations.data_zone.delete_environment_blueprint_configuration.delete_environment_blueprint_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteEnvironmentBlueprintConfiguration"),
        )
        input_: capo_datazone.types.delete_environment_blueprint_configuration_input.DeleteEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[DataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_environment_blueprint_configurations_output.ListEnvironmentBlueprintConfigurationsOutput":
        """<p>Lists blueprint configurations for a Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            max_results: <p>The maximum number of blueprint configurations to return in a single call to <code>ListEnvironmentBlueprintConfigurations</code>. When the number of configurations to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>
            next_token: <p>When the number of blueprint configurations is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of configurations, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_datazone.types.list_environment_blueprint_configurations_input.ListEnvironmentBlueprintConfigurationsInput]",
        ) -> OperationResponse[
            "capo_datazone.types.list_environment_blueprint_configurations_output.ListEnvironmentBlueprintConfigurationsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environment_blueprint_configurations

            output, http_response = (
                capo_datazone._operations.data_zone.list_environment_blueprint_configurations.list_environment_blueprint_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEnvironmentBlueprintConfigurations")
        )
        input_: capo_datazone.types.list_environment_blueprint_configurations_input.ListEnvironmentBlueprintConfigurationsInput = {
            "domain_identifier": domain_identifier
        }
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


class AsyncEnvironmentBlueprintConfiguration:
    def __init__(self, service: AsyncDataZoneClient) -> None:
        self._service = service

    async def put(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        enabled_regions: "capo_datazone.types.enabled_region_list.EnabledRegionList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        provisioning_role_arn: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        manage_access_role_arn: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        environment_role_permission_boundary: Optional[
            "capo_datazone.types.policy_arn.PolicyArn"
        ] = None,
        regional_parameters: Optional[
            "capo_datazone.types.regional_parameter_map.RegionalParameterMap"
        ] = None,
        resource_configurations: Optional[
            "capo_datazone.types.put_resource_configurations.PutResourceConfigurations"
        ] = None,
        allow_user_provided_configurations: Optional[bool] = None,
        global_parameters: Optional[
            "capo_datazone.types.global_parameter_map.GlobalParameterMap"
        ] = None,
        provisioning_configurations: Optional[
            "capo_datazone.types.provisioning_configuration_list.ProvisioningConfigurationList"
        ] = None,
    ) -> "capo_datazone.types.put_environment_blueprint_configuration_output.PutEnvironmentBlueprintConfigurationOutput":
        """<p>Writes the configuration for the specified environment blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            environment_blueprint_identifier: <p>The identifier of the environment blueprint.</p>
            provisioning_role_arn: <p>The ARN of the provisioning role.</p>
            manage_access_role_arn: <p>The ARN of the manage access role.</p>
            environment_role_permission_boundary: <p>The environment role permissions boundary.</p>
            enabled_regions: <p>Specifies the enabled Amazon Web Services Regions.</p>
            regional_parameters: <p>The regional parameters in the environment blueprint.</p>
            resource_configurations: <p>The resource configurations of the environment blueprint.</p>
            allow_user_provided_configurations: <p>Specifies whether user-provided resource configurations are allowed for the environment blueprint.</p>
            global_parameters: <p>Region-agnostic environment blueprint parameters. </p>
            provisioning_configurations: <p>The provisioning configuration of a blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.put_environment_blueprint_configuration_input.PutEnvironmentBlueprintConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.put_environment_blueprint_configuration_output.PutEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.put_environment_blueprint_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.put_environment_blueprint_configuration.async_put_environment_blueprint_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("PutEnvironmentBlueprintConfiguration")
        )
        input_: capo_datazone.types.put_environment_blueprint_configuration_input.PutEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
            "enabled_regions": enabled_regions,
        }
        if provisioning_role_arn is not None:
            input_["provisioning_role_arn"] = provisioning_role_arn
        if manage_access_role_arn is not None:
            input_["manage_access_role_arn"] = manage_access_role_arn
        if environment_role_permission_boundary is not None:
            input_["environment_role_permission_boundary"] = (
                environment_role_permission_boundary
            )
        if regional_parameters is not None:
            input_["regional_parameters"] = regional_parameters
        if resource_configurations is not None:
            input_["resource_configurations"] = resource_configurations
        if allow_user_provided_configurations is not None:
            input_["allow_user_provided_configurations"] = (
                allow_user_provided_configurations
            )
        if global_parameters is not None:
            input_["global_parameters"] = global_parameters
        if provisioning_configurations is not None:
            input_["provisioning_configurations"] = provisioning_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_blueprint_configuration_output.GetEnvironmentBlueprintConfigurationOutput":
        """<p>Gets the blueprint configuration in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where this blueprint exists.</p>
            environment_blueprint_identifier: <p>He ID of the blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_blueprint_configuration_input.GetEnvironmentBlueprintConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_blueprint_configuration_output.GetEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_blueprint_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment_blueprint_configuration.async_get_environment_blueprint_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetEnvironmentBlueprintConfiguration")
        )
        input_: capo_datazone.types.get_environment_blueprint_configuration_input.GetEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_environment_blueprint_configuration_output.DeleteEnvironmentBlueprintConfigurationOutput":
        """<p>Deletes the blueprint configuration in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the blueprint configuration is deleted.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint the configuration of which is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_environment_blueprint_configuration_input.DeleteEnvironmentBlueprintConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_environment_blueprint_configuration_output.DeleteEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_environment_blueprint_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_environment_blueprint_configuration.async_delete_environment_blueprint_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteEnvironmentBlueprintConfiguration"),
        )
        input_: capo_datazone.types.delete_environment_blueprint_configuration_input.DeleteEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_environment_blueprint_configurations_output.ListEnvironmentBlueprintConfigurationsOutput":
        """<p>Lists blueprint configurations for a Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            max_results: <p>The maximum number of blueprint configurations to return in a single call to <code>ListEnvironmentBlueprintConfigurations</code>. When the number of configurations to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>
            next_token: <p>When the number of blueprint configurations is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of configurations, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_environment_blueprint_configurations_input.ListEnvironmentBlueprintConfigurationsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_environment_blueprint_configurations_output.ListEnvironmentBlueprintConfigurationsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environment_blueprint_configurations

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_environment_blueprint_configurations.async_list_environment_blueprint_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListEnvironmentBlueprintConfigurations")
        )
        input_: capo_datazone.types.list_environment_blueprint_configurations_input.ListEnvironmentBlueprintConfigurationsInput = {
            "domain_identifier": domain_identifier
        }
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
