from __future__ import annotations

from typing import TYPE_CHECKING, Optional

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
    import capo_proton.types.empty_next_token
    import capo_proton.types.list_service_instance_provisioned_resources_input
    import capo_proton.types.list_service_instance_provisioned_resources_output
    import capo_proton.types.provisioned_resource
    import capo_proton.types.resource_name
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceInstanceProvisionedResourceResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def list(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput":
        """<p>List provisioned resources for a service instance with details.</p>

        Args:
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>
            service_instance_name: <p>The name of the service instance whose provisioned resources you want.</p>
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
            req: "OperationRequest[capo_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources.list_service_instance_provisioned_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListServiceInstanceProvisionedResources"),
        )
        input_: capo_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput = {
            "service_name": service_name,
            "service_instance_name": service_instance_name,
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


class AsyncServiceInstanceProvisionedResourceResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def list(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        service_instance_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
    ) -> "capo_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput":
        """<p>List provisioned resources for a service instance with details.</p>

        Args:
            service_name: <p>The name of the service that <code>serviceInstanceName</code> is associated to.</p>
            service_instance_name: <p>The name of the service instance whose provisioned resources you want.</p>
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
            req: "AsyncOperationRequest[capo_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_instance_provisioned_resources_output.ListServiceInstanceProvisionedResourcesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_instance_provisioned_resources.async_list_service_instance_provisioned_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListServiceInstanceProvisionedResources"),
        )
        input_: capo_proton.types.list_service_instance_provisioned_resources_input.ListServiceInstanceProvisionedResourcesInput = {
            "service_name": service_name,
            "service_instance_name": service_instance_name,
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
