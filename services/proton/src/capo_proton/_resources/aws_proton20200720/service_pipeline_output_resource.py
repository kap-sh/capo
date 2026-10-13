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
    import capo_proton.types.deployment_id
    import capo_proton.types.empty_next_token
    import capo_proton.types.list_service_pipeline_outputs_input
    import capo_proton.types.list_service_pipeline_outputs_output
    import capo_proton.types.output
    import capo_proton.types.resource_name
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServicePipelineOutputResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def list(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput":
        """<p>Get a list of service pipeline Infrastructure as Code (IaC) outputs.</p>

        Args:
            service_name: <p>The name of the service whose pipeline's outputs you want.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment you want the outputs for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_service_pipeline_outputs_input.ListServicePipelineOutputsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_pipeline_outputs

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_service_pipeline_outputs.list_service_pipeline_outputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.list_service_pipeline_outputs_output

            return (
                capo_proton.types.list_service_pipeline_outputs_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListServicePipelineOutputs", redact_output=_redact_output
            ),
        )
        input_: capo_proton.types.list_service_pipeline_outputs_input.ListServicePipelineOutputsInput = {
            "service_name": service_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServicePipelineOutputResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def list(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional[
            "capo_proton.types.empty_next_token.EmptyNextToken"
        ] = None,
        deployment_id: Optional["capo_proton.types.deployment_id.DeploymentId"] = None,
    ) -> "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput":
        """<p>Get a list of service pipeline Infrastructure as Code (IaC) outputs.</p>

        Args:
            service_name: <p>The name of the service whose pipeline's outputs you want.</p>
            next_token: <p>A token that indicates the location of the next output in the array of outputs, after the list of outputs that was previously requested.</p>
            deployment_id: <p>The ID of the deployment you want the outputs for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_pipeline_outputs_input.ListServicePipelineOutputsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_pipeline_outputs

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_pipeline_outputs.async_list_service_pipeline_outputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_proton.types.list_service_pipeline_outputs_output.ListServicePipelineOutputsOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.list_service_pipeline_outputs_output

            return (
                capo_proton.types.list_service_pipeline_outputs_output.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "ListServicePipelineOutputs", redact_output=_redact_output
            ),
        )
        input_: capo_proton.types.list_service_pipeline_outputs_input.ListServicePipelineOutputsInput = {
            "service_name": service_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
