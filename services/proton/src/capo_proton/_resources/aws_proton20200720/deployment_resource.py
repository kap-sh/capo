from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from capo_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_proton.types.delete_deployment_input
    import capo_proton.types.delete_deployment_output
    import capo_proton.types.deployment_id
    import capo_proton.types.deployment_summary
    import capo_proton.types.get_deployment_input
    import capo_proton.types.get_deployment_output
    import capo_proton.types.list_deployments_input
    import capo_proton.types.list_deployments_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.resource_name
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class DeploymentResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def read(
        self,
        id: "capo_proton.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
    ) -> "capo_proton.types.get_deployment_output.GetDeploymentOutput":
        """<p>Get detailed data for a deployment.</p>

        Args:
            id: <p>The ID of the deployment that you want to get the detailed data for.</p>
            environment_name: <p>The name of a environment that you want to get the detailed data for.</p>
            service_name: <p>The name of the service associated with the given deployment ID.</p>
            service_instance_name: <p>The name of the service instance associated with the given deployment ID. <code>serviceName</code> must be specified to identify the service instance.</p>
            component_name: <p>The name of a component that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_deployment_input.GetDeploymentInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_deployment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_proton.types.get_deployment_output.GetDeploymentOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.get_deployment_output

            return capo_proton.types.get_deployment_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDeployment", redact_output=_redact_output),
        )
        input_: capo_proton.types.get_deployment_input.GetDeploymentInput = {"id": id}
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if component_name is not None:
            input_["component_name"] = component_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        id: "capo_proton.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput":
        """<p>Delete the deployment.</p>

        Args:
            id: <p>The ID of the deployment to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_deployment

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_deployment.delete_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.delete_deployment_output

            return capo_proton.types.delete_deployment_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteDeployment", redact_output=_redact_output),
        )
        input_: capo_proton.types.delete_deployment_input.DeleteDeploymentInput = {
            "id": id
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
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_deployments_output.ListDeploymentsOutput":
        """<p>List deployments. You can filter the result list by environment, service, or a single service instance.</p>

        Args:
            next_token: <p>A token that indicates the location of the next deployment in the array of deployment, after the list of deployment that was previously requested.</p>
            environment_name: <p>The name of an environment for result list filtering. Proton returns deployments associated with the environment.</p>
            service_name: <p>The name of a service for result list filtering. Proton returns deployments associated with service instances of the service.</p>
            service_instance_name: <p>The name of a service instance for result list filtering. Proton returns the deployments associated with the service instance.</p>
            component_name: <p>The name of a component for result list filtering. Proton returns deployments associated with that component.</p>
            max_results: <p>The maximum number of deployments to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_deployments_input.ListDeploymentsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_deployments

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDeployments")
        )
        input_: capo_proton.types.list_deployments_input.ListDeploymentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if component_name is not None:
            input_["component_name"] = component_name
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDeploymentResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def read(
        self,
        id: "capo_proton.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
    ) -> "capo_proton.types.get_deployment_output.GetDeploymentOutput":
        """<p>Get detailed data for a deployment.</p>

        Args:
            id: <p>The ID of the deployment that you want to get the detailed data for.</p>
            environment_name: <p>The name of a environment that you want to get the detailed data for.</p>
            service_name: <p>The name of the service associated with the given deployment ID.</p>
            service_instance_name: <p>The name of the service instance associated with the given deployment ID. <code>serviceName</code> must be specified to identify the service instance.</p>
            component_name: <p>The name of a component that you want to get the detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_deployment_input.GetDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_deployment.async_get_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_proton.types.get_deployment_output.GetDeploymentOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.get_deployment_output

            return capo_proton.types.get_deployment_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetDeployment", redact_output=_redact_output),
        )
        input_: capo_proton.types.get_deployment_input.GetDeploymentInput = {"id": id}
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if component_name is not None:
            input_["component_name"] = component_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        id: "capo_proton.types.deployment_id.DeploymentId",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput":
        """<p>Delete the deployment.</p>

        Args:
            id: <p>The ID of the deployment to delete.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_deployment

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_deployment.async_delete_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_proton.types.delete_deployment_output.DeleteDeploymentOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.delete_deployment_output

            return capo_proton.types.delete_deployment_output.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("DeleteDeployment", redact_output=_redact_output),
        )
        input_: capo_proton.types.delete_deployment_input.DeleteDeploymentInput = {
            "id": id
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
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        environment_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        service_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        service_instance_name: Optional[
            "capo_proton.types.resource_name.ResourceName"
        ] = None,
        component_name: Optional["capo_proton.types.resource_name.ResourceName"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_deployments_output.ListDeploymentsOutput":
        """<p>List deployments. You can filter the result list by environment, service, or a single service instance.</p>

        Args:
            next_token: <p>A token that indicates the location of the next deployment in the array of deployment, after the list of deployment that was previously requested.</p>
            environment_name: <p>The name of an environment for result list filtering. Proton returns deployments associated with the environment.</p>
            service_name: <p>The name of a service for result list filtering. Proton returns deployments associated with service instances of the service.</p>
            service_instance_name: <p>The name of a service instance for result list filtering. Proton returns the deployments associated with the service instance.</p>
            component_name: <p>The name of a component for result list filtering. Proton returns deployments associated with that component.</p>
            max_results: <p>The maximum number of deployments to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_deployments_input.ListDeploymentsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_deployments

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_deployments.async_list_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListDeployments")
        )
        input_: capo_proton.types.list_deployments_input.ListDeploymentsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if environment_name is not None:
            input_["environment_name"] = environment_name
        if service_name is not None:
            input_["service_name"] = service_name
        if service_instance_name is not None:
            input_["service_instance_name"] = service_instance_name
        if component_name is not None:
            input_["component_name"] = component_name
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
