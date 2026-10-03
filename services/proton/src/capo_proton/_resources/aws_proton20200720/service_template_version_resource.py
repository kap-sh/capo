from __future__ import annotations

import uuid
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
    import capo_proton.types.client_token
    import capo_proton.types.compatible_environment_template_input_list
    import capo_proton.types.create_service_template_version_input
    import capo_proton.types.create_service_template_version_output
    import capo_proton.types.delete_service_template_version_input
    import capo_proton.types.delete_service_template_version_output
    import capo_proton.types.description
    import capo_proton.types.get_service_template_version_input
    import capo_proton.types.get_service_template_version_output
    import capo_proton.types.list_service_template_versions_input
    import capo_proton.types.list_service_template_versions_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.resource_name
    import capo_proton.types.service_template_supported_component_source_input_list
    import capo_proton.types.service_template_version_summary
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_source_input
    import capo_proton.types.template_version_status
    import capo_proton.types.update_service_template_version_input
    import capo_proton.types.update_service_template_version_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceTemplateVersionResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def create(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput",
        compatible_environment_templates: "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        supported_component_sources: Optional[
            "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
        ] = None,
    ) -> "capo_proton.types.create_service_template_version_output.CreateServiceTemplateVersionOutput":
        """<p>Create a new major or minor version of a service template. A major version of a service template is a version that <i>isn't</i> backward compatible. A minor version of a service template is a version that's backward compatible within its major version.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the service template version that the first request created.</p>
            template_name: <p>The name of the service template.</p>
            description: <p>A description of the new version of a service template.</p>
            major_version: <p>To create a new minor version of the service template, include a <code>major Version</code>.</p> <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>
            source: <p>An object that includes the template bundle S3 bucket path and name for the new version of a service template.</p>
            compatible_environment_templates: <p>An array of environment template objects that are compatible with the new service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            supported_component_sources: <p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.create_service_template_version_input.CreateServiceTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_service_template_version_output.CreateServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_service_template_version.create_service_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_service_template_version_input.CreateServiceTemplateVersionInput = {
            "template_name": template_name,
            "source": source,
            "compatible_environment_templates": compatible_environment_templates,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if major_version is not None:
            input_["major_version"] = major_version
        if tags is not None:
            input_["tags"] = tags
        if supported_component_sources is not None:
            input_["supported_component_sources"] = supported_component_sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_template_version_output.GetServiceTemplateVersionOutput":
        """<p>Get detailed data for a major or minor version of a service template.</p>

        Args:
            template_name: <p>The name of the service template a version of which you want to get detailed data for.</p>
            major_version: <p>To get service template major version detail data, include <code>major Version</code>.</p>
            minor_version: <p>To get service template minor version detail data, include <code>minorVersion</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_service_template_version_input.GetServiceTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_service_template_version_output.GetServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_service_template_version.get_service_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_service_template_version_input.GetServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
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
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        status: Optional[
            "capo_proton.types.template_version_status.TemplateVersionStatus"
        ] = None,
        compatible_environment_templates: Optional[
            "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList"
        ] = None,
        supported_component_sources: Optional[
            "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
        ] = None,
    ) -> "capo_proton.types.update_service_template_version_output.UpdateServiceTemplateVersionOutput":
        """<p>Update a major or minor version of a service template.</p>

        Args:
            template_name: <p>The name of the service template.</p>
            major_version: <p>To update a major version of a service template, include <code>major Version</code>.</p>
            minor_version: <p>To update a minor version of a service template, include <code>minorVersion</code>.</p>
            description: <p>A description of a service template version to update.</p>
            status: <p>The status of the service template minor version to update.</p>
            compatible_environment_templates: <p>An array of environment template objects that are compatible with this service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>
            supported_component_sources: <p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <note> <p>A change to <code>supportedComponentSources</code> doesn't impact existing component attachments to instances based on this template version. A change only affects later associations.</p> </note> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

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
            req: "OperationRequest[capo_proton.types.update_service_template_version_input.UpdateServiceTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_service_template_version_output.UpdateServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_service_template_version.update_service_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_service_template_version_input.UpdateServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if compatible_environment_templates is not None:
            input_["compatible_environment_templates"] = (
                compatible_environment_templates
            )
        if supported_component_sources is not None:
            input_["supported_component_sources"] = supported_component_sources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_template_version_output.DeleteServiceTemplateVersionOutput":
        """<p>If no other minor versions of a service template exist, delete a major version of the service template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that <i>isn't</i> backwards compatible.</p> <p>Delete a minor version of a service template if it's not the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that's backwards compatible.</p>

        Args:
            template_name: <p>The name of the service template.</p>
            major_version: <p>The service template major version to delete.</p>
            minor_version: <p>The service template minor version to delete.</p>

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
            req: "OperationRequest[capo_proton.types.delete_service_template_version_input.DeleteServiceTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_service_template_version_output.DeleteServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_service_template_version.delete_service_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_template_version_input.DeleteServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
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
        template_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.list_service_template_versions_output.ListServiceTemplateVersionsOutput":
        """<p>List major or minor versions of a service template with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the list of major or minor versions that was previously requested.</p>
            max_results: <p>The maximum number of major or minor versions of a service template to list.</p>
            template_name: <p>The name of the service template.</p>
            major_version: <p>To view a list of minor of versions under a major version of a service template, include <code>major Version</code>.</p> <p>To view a list of major versions of a service template, <i>exclude</i> <code>major Version</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_service_template_versions_input.ListServiceTemplateVersionsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_service_template_versions_output.ListServiceTemplateVersionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_template_versions

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_service_template_versions.list_service_template_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_service_template_versions_input.ListServiceTemplateVersionsInput = {
            "template_name": template_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if major_version is not None:
            input_["major_version"] = major_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceTemplateVersionResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def create(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput",
        compatible_environment_templates: "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
        supported_component_sources: Optional[
            "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
        ] = None,
    ) -> "capo_proton.types.create_service_template_version_output.CreateServiceTemplateVersionOutput":
        """<p>Create a new major or minor version of a service template. A major version of a service template is a version that <i>isn't</i> backward compatible. A minor version of a service template is a version that's backward compatible within its major version.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the service template version that the first request created.</p>
            template_name: <p>The name of the service template.</p>
            description: <p>A description of the new version of a service template.</p>
            major_version: <p>To create a new minor version of the service template, include a <code>major Version</code>.</p> <p>To create a new major and minor version of the service template, <i>exclude</i> <code>major Version</code>.</p>
            source: <p>An object that includes the template bundle S3 bucket path and name for the new version of a service template.</p>
            compatible_environment_templates: <p>An array of environment template objects that are compatible with the new service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton service template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>
            supported_component_sources: <p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>A quota was exceeded. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html">Proton Quotas</a> in the <i>Proton User Guide</i>.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.create_service_template_version_input.CreateServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_template_version_output.CreateServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_template_version.async_create_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_service_template_version_input.CreateServiceTemplateVersionInput = {
            "template_name": template_name,
            "source": source,
            "compatible_environment_templates": compatible_environment_templates,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if major_version is not None:
            input_["major_version"] = major_version
        if tags is not None:
            input_["tags"] = tags
        if supported_component_sources is not None:
            input_["supported_component_sources"] = supported_component_sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_template_version_output.GetServiceTemplateVersionOutput":
        """<p>Get detailed data for a major or minor version of a service template.</p>

        Args:
            template_name: <p>The name of the service template a version of which you want to get detailed data for.</p>
            major_version: <p>To get service template major version detail data, include <code>major Version</code>.</p>
            minor_version: <p>To get service template minor version detail data, include <code>minorVersion</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_template_version_input.GetServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_template_version_output.GetServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_template_version.async_get_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_service_template_version_input.GetServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
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
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        status: Optional[
            "capo_proton.types.template_version_status.TemplateVersionStatus"
        ] = None,
        compatible_environment_templates: Optional[
            "capo_proton.types.compatible_environment_template_input_list.CompatibleEnvironmentTemplateInputList"
        ] = None,
        supported_component_sources: Optional[
            "capo_proton.types.service_template_supported_component_source_input_list.ServiceTemplateSupportedComponentSourceInputList"
        ] = None,
    ) -> "capo_proton.types.update_service_template_version_output.UpdateServiceTemplateVersionOutput":
        """<p>Update a major or minor version of a service template.</p>

        Args:
            template_name: <p>The name of the service template.</p>
            major_version: <p>To update a major version of a service template, include <code>major Version</code>.</p>
            minor_version: <p>To update a minor version of a service template, include <code>minorVersion</code>.</p>
            description: <p>A description of a service template version to update.</p>
            status: <p>The status of the service template minor version to update.</p>
            compatible_environment_templates: <p>An array of environment template objects that are compatible with this service template version. A service instance based on this service template version can run in environments based on compatible templates.</p>
            supported_component_sources: <p>An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.</p> <note> <p>A change to <code>supportedComponentSources</code> doesn't impact existing component attachments to instances based on this template version. A change only affects later associations.</p> </note> <p>For more information about components, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html">Proton components</a> in the <i>Proton User Guide</i>.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.update_service_template_version_input.UpdateServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_template_version_output.UpdateServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_template_version.async_update_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_service_template_version_input.UpdateServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if compatible_environment_templates is not None:
            input_["compatible_environment_templates"] = (
                compatible_environment_templates
            )
        if supported_component_sources is not None:
            input_["supported_component_sources"] = supported_component_sources

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        major_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        minor_version: "capo_proton.types.template_version_part.TemplateVersionPart",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_template_version_output.DeleteServiceTemplateVersionOutput":
        """<p>If no other minor versions of a service template exist, delete a major version of the service template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that <i>isn't</i> backwards compatible.</p> <p>Delete a minor version of a service template if it's not the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that's backwards compatible.</p>

        Args:
            template_name: <p>The name of the service template.</p>
            major_version: <p>The service template major version to delete.</p>
            minor_version: <p>The service template minor version to delete.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_service_template_version_input.DeleteServiceTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_template_version_output.DeleteServiceTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service_template_version.async_delete_service_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_template_version_input.DeleteServiceTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
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
        template_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        next_token: Optional["capo_proton.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_proton.types.max_page_results.MaxPageResults"
        ] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
    ) -> "capo_proton.types.list_service_template_versions_output.ListServiceTemplateVersionsOutput":
        """<p>List major or minor versions of a service template with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the list of major or minor versions that was previously requested.</p>
            max_results: <p>The maximum number of major or minor versions of a service template to list.</p>
            template_name: <p>The name of the service template.</p>
            major_version: <p>To view a list of minor of versions under a major version of a service template, include <code>major Version</code>.</p> <p>To view a list of major versions of a service template, <i>exclude</i> <code>major Version</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_service_template_versions_input.ListServiceTemplateVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_service_template_versions_output.ListServiceTemplateVersionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_service_template_versions

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_service_template_versions.async_list_service_template_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_service_template_versions_input.ListServiceTemplateVersionsInput = {
            "template_name": template_name
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if major_version is not None:
            input_["major_version"] = major_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
