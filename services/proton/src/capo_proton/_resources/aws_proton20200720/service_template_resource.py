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
    import capo_proton.types.arn
    import capo_proton.types.create_service_template_input
    import capo_proton.types.create_service_template_output
    import capo_proton.types.delete_service_template_input
    import capo_proton.types.delete_service_template_output
    import capo_proton.types.description
    import capo_proton.types.display_name
    import capo_proton.types.get_service_template_input
    import capo_proton.types.get_service_template_output
    import capo_proton.types.list_service_templates_input
    import capo_proton.types.list_service_templates_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.provisioning
    import capo_proton.types.resource_name
    import capo_proton.types.service_template_summary
    import capo_proton.types.tag_list
    import capo_proton.types.update_service_template_input
    import capo_proton.types.update_service_template_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceTemplateResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        pipeline_provisioning: Optional[
            "capo_proton.types.provisioning.Provisioning"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_service_template_output.CreateServiceTemplateOutput":
        """<p>Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Proton templates</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the service template.</p>
            display_name: <p>The name of the service template as displayed in the developer interface.</p>
            description: <p>A description of the service template.</p>
            encryption_key: <p>A customer provided encryption key that's used to encrypt data.</p>
            pipeline_provisioning: <p>By default, Proton provides a service pipeline for your service. When this parameter is included, it indicates that an Proton service pipeline <i>isn't</i> provided for your service. After it's included, it <i>can't</i> be changed. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles">Template bundles</a> in the <i>Proton User Guide</i>.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.create_service_template_input.CreateServiceTemplateInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_service_template_output.CreateServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_template

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_service_template.create_service_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_service_template_input.CreateServiceTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if pipeline_provisioning is not None:
            input_["pipeline_provisioning"] = pipeline_provisioning
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
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_template_output.GetServiceTemplateOutput":
        """<p>Get detailed data for a service template.</p>

        Args:
            name: <p>The name of the service template that you want to get detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_service_template_input.GetServiceTemplateInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_service_template_output.GetServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_template

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_service_template.get_service_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_service_template_input.GetServiceTemplateInput = {
            "name": name
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
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
    ) -> "capo_proton.types.update_service_template_output.UpdateServiceTemplateOutput":
        """<p>Update a service template.</p>

        Args:
            name: <p>The name of the service template to update.</p>
            display_name: <p>The name of the service template to update that's displayed in the developer interface.</p>
            description: <p>A description of the service template update.</p>

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
            req: "OperationRequest[capo_proton.types.update_service_template_input.UpdateServiceTemplateInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_service_template_output.UpdateServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_template

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_service_template.update_service_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_service_template_input.UpdateServiceTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_template_output.DeleteServiceTemplateOutput":
        """<p>If no other major or minor versions of the service template exist, delete the service template.</p>

        Args:
            name: <p>The name of the service template to delete.</p>

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
            req: "OperationRequest[capo_proton.types.delete_service_template_input.DeleteServiceTemplateInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_service_template_output.DeleteServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_template

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_service_template.delete_service_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_template_input.DeleteServiceTemplateInput = {
            "name": name
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
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_service_templates_output.ListServiceTemplatesOutput":
        """<p>List service templates with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service template in the array of service templates, after the list of service templates previously requested.</p>
            max_results: <p>The maximum number of service templates to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_service_templates_input.ListServiceTemplatesInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_service_templates_output.ListServiceTemplatesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_templates

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_service_templates.list_service_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_service_templates_input.ListServiceTemplatesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceTemplateResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        pipeline_provisioning: Optional[
            "capo_proton.types.provisioning.Provisioning"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_service_template_output.CreateServiceTemplateOutput":
        """<p>Create a service template. The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from Proton. If the selected service template includes a service pipeline definition, they provide a link to their source code repository. Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html">Proton templates</a> in the <i>Proton User Guide</i>.</p>

        Args:
            name: <p>The name of the service template.</p>
            display_name: <p>The name of the service template as displayed in the developer interface.</p>
            description: <p>A description of the service template.</p>
            encryption_key: <p>A customer provided encryption key that's used to encrypt data.</p>
            pipeline_provisioning: <p>By default, Proton provides a service pipeline for your service. When this parameter is included, it indicates that an Proton service pipeline <i>isn't</i> provided for your service. After it's included, it <i>can't</i> be changed. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles">Template bundles</a> in the <i>Proton User Guide</i>.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service template. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_template_input.CreateServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_template_output.CreateServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_template.async_create_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_service_template_input.CreateServiceTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if pipeline_provisioning is not None:
            input_["pipeline_provisioning"] = pipeline_provisioning
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
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_template_output.GetServiceTemplateOutput":
        """<p>Get detailed data for a service template.</p>

        Args:
            name: <p>The name of the service template that you want to get detailed data for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_template_input.GetServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_template_output.GetServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_template.async_get_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_service_template_input.GetServiceTemplateInput = {
            "name": name
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
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        display_name: Optional["capo_proton.types.display_name.DisplayName"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
    ) -> "capo_proton.types.update_service_template_output.UpdateServiceTemplateOutput":
        """<p>Update a service template.</p>

        Args:
            name: <p>The name of the service template to update.</p>
            display_name: <p>The name of the service template to update that's displayed in the developer interface.</p>
            description: <p>A description of the service template update.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.update_service_template_input.UpdateServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_template_output.UpdateServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_template.async_update_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_service_template_input.UpdateServiceTemplateInput = {
            "name": name
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_template_output.DeleteServiceTemplateOutput":
        """<p>If no other major or minor versions of the service template exist, delete the service template.</p>

        Args:
            name: <p>The name of the service template to delete.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_service_template_input.DeleteServiceTemplateInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_template_output.DeleteServiceTemplateOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_template

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service_template.async_delete_service_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_template_input.DeleteServiceTemplateInput = {
            "name": name
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
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
    ) -> "capo_proton.types.list_service_templates_output.ListServiceTemplatesOutput":
        """<p>List service templates with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next service template in the array of service templates, after the list of service templates previously requested.</p>
            max_results: <p>The maximum number of service templates to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_templates_input.ListServiceTemplatesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_templates_output.ListServiceTemplatesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_templates

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_templates.async_list_service_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_service_templates_input.ListServiceTemplatesInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
