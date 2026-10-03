from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_proton.types.empty_next_token
    import capo_proton.types.list_component_provisioned_resources_input
    import capo_proton.types.list_component_provisioned_resources_output
    import capo_proton.types.provisioned_resource
    import capo_proton.types.resource_name
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ComponentProvisionedResourceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def list(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput":
        """<p>List provisioned resources for a component with details.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_component_provisioned_resources

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_component_provisioned_resources.list_component_provisioned_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput = {
            "component_name": component_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncComponentProvisionedResourceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def list(
        self,
        component_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput":
        """<p>List provisioned resources for a component with details.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Args:
            component_name: <p>The name of the component whose provisioned resources you want.</p>
            next_token: <p>A token that indicates the location of the next provisioned resource in the array of provisioned resources, after the list of provisioned resources that was previously requested.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_component_provisioned_resources_output.ListComponentProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_component_provisioned_resources

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_component_provisioned_resources.async_list_component_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_component_provisioned_resources_input.ListComponentProvisionedResourcesInput = {
            "component_name": component_name
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
