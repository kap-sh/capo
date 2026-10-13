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
    import capo_proton.types.deployment_update_type
    import capo_proton.types.resource_name
    import capo_proton.types.spec_contents
    import capo_proton.types.template_version_part
    import capo_proton.types.update_service_pipeline_input
    import capo_proton.types.update_service_pipeline_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServicePipelineResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def update(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        spec: "capo_proton.types.spec_contents.SpecContents",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput":
        """<p>Update the service pipeline.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            service_name: <p>The name of the service to that the pipeline is associated with.</p>
            spec: <p>The spec for the service pipeline to update.</p>
            deployment_type: <p>The deployment type.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            template_major_version: <p>The major version of the service template that was used to create the service that the pipeline is associated with.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service that the pipeline is associated with.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_pipeline

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_service_pipeline.update_service_pipeline(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput",
        ) -> dict[str, Any]:
            import capo_proton.types.update_service_pipeline_input

            return capo_proton.types.update_service_pipeline_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.update_service_pipeline_output

            return capo_proton.types.update_service_pipeline_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateServicePipeline",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput = {
            "service_name": service_name,
            "spec": spec,
            "deployment_type": deployment_type,
        }
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServicePipelineResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def update(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        spec: "capo_proton.types.spec_contents.SpecContents",
        deployment_type: "capo_proton.types.deployment_update_type.DeploymentUpdateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        template_major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        template_minor_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput":
        """<p>Update the service pipeline.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>

        Args:
            service_name: <p>The name of the service to that the pipeline is associated with.</p>
            spec: <p>The spec for the service pipeline to update.</p>
            deployment_type: <p>The deployment type.</p> <p>There are four modes for updating a service pipeline. The <code>deploymentType</code> field defines the mode.</p> <dl> <dt/> <dd> <p> <code>NONE</code> </p> <p>In this mode, a deployment <i>doesn't</i> occur. Only the requested metadata parameters are updated.</p> </dd> <dt/> <dd> <p> <code>CURRENT_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the new spec that you provide. Only requested parameters are updated. <i>Don’t</i> include major or minor version parameters when you use this <code>deployment-type</code>.</p> </dd> <dt/> <dd> <p> <code>MINOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) minor version of the current major version in use, by default. You can specify a different minor version of the current major version in use.</p> </dd> <dt/> <dd> <p> <code>MAJOR_VERSION</code> </p> <p>In this mode, the service pipeline is deployed and updated with the published, recommended (latest) major and minor version of the current template, by default. You can specify a different major version that's higher than the major version in use and a minor version.</p> </dd> </dl>
            template_major_version: <p>The major version of the service template that was used to create the service that the pipeline is associated with.</p>
            template_minor_version: <p>The minor version of the service template that was used to create the service that the pipeline is associated with.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_pipeline

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_pipeline.async_update_service_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput",
        ) -> dict[str, Any]:
            import capo_proton.types.update_service_pipeline_input

            return capo_proton.types.update_service_pipeline_input.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_proton.types.update_service_pipeline_output.UpdateServicePipelineOutput",
        ) -> dict[str, Any]:
            import capo_proton.types.update_service_pipeline_output

            return capo_proton.types.update_service_pipeline_output.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateServicePipeline",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_proton.types.update_service_pipeline_input.UpdateServicePipelineInput = {
            "service_name": service_name,
            "spec": spec,
            "deployment_type": deployment_type,
        }
        if template_major_version is not None:
            input_["template_major_version"] = template_major_version
        if template_minor_version is not None:
            input_["template_minor_version"] = template_minor_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
