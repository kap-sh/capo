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
    import capo_proton.types.create_environment_template_version_input
    import capo_proton.types.create_environment_template_version_output
    import capo_proton.types.delete_environment_template_version_input
    import capo_proton.types.delete_environment_template_version_output
    import capo_proton.types.description
    import capo_proton.types.environment_template_version_summary
    import capo_proton.types.get_environment_template_version_input
    import capo_proton.types.get_environment_template_version_output
    import capo_proton.types.list_environment_template_versions_input
    import capo_proton.types.list_environment_template_versions_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.resource_name
    import capo_proton.types.tag_list
    import capo_proton.types.template_version_part
    import capo_proton.types.template_version_source_input
    import capo_proton.types.template_version_status
    import capo_proton.types.update_environment_template_version_input
    import capo_proton.types.update_environment_template_version_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class EnvironmentTemplateVersionResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def create(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_environment_template_version_output.CreateEnvironmentTemplateVersionOutput":
        """<p>Create a new major or minor version of an environment template. A major version of an environment template is a version that <i>isn't</i> backwards compatible. A minor version of an environment template is a version that's backwards compatible within its major version.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment template version that the first request created.</p>
            template_name: <p>The name of the environment template.</p>
            description: <p>A description of the new version of an environment template.</p>
            major_version: <p>To create a new minor version of the environment template, include <code>major Version</code>.</p> <p>To create a new major and minor version of the environment template, exclude <code>major Version</code>.</p>
            source: <p>An object that includes the template bundle S3 bucket path and name for the new version of an template.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

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
            req: "OperationRequest[capo_proton.types.create_environment_template_version_input.CreateEnvironmentTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_environment_template_version_output.CreateEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_environment_template_version.create_environment_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_template_version_input.CreateEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "source": source,
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
    ) -> "capo_proton.types.get_environment_template_version_output.GetEnvironmentTemplateVersionOutput":
        """<p>Get detailed data for a major or minor version of an environment template.</p>

        Args:
            template_name: <p>The name of the environment template a version of which you want to get detailed data for.</p>
            major_version: <p>To get environment template major version detail data, include <code>major Version</code>.</p>
            minor_version: <p>To get environment template minor version detail data, include <code>minorVersion</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_environment_template_version_input.GetEnvironmentTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_environment_template_version_output.GetEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_environment_template_version.get_environment_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_template_version_input.GetEnvironmentTemplateVersionInput = {
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
    ) -> "capo_proton.types.update_environment_template_version_output.UpdateEnvironmentTemplateVersionOutput":
        """<p>Update a major or minor version of an environment template.</p>

        Args:
            template_name: <p>The name of the environment template.</p>
            major_version: <p>To update a major version of an environment template, include <code>major Version</code>.</p>
            minor_version: <p>To update a minor version of an environment template, include <code>minorVersion</code>.</p>
            description: <p>A description of environment template version to update.</p>
            status: <p>The status of the environment template minor version to update.</p>

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
            req: "OperationRequest[capo_proton.types.update_environment_template_version_input.UpdateEnvironmentTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_environment_template_version_output.UpdateEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_environment_template_version.update_environment_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_template_version_input.UpdateEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

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
    ) -> "capo_proton.types.delete_environment_template_version_output.DeleteEnvironmentTemplateVersionOutput":
        """<p>If no other minor versions of an environment template exist, delete a major version of the environment template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the environment template if no other major versions or minor versions of the environment template exist. A major version of an environment template is a version that's not backward compatible.</p> <p>Delete a minor version of an environment template if it <i>isn't</i> the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the environment template if no other minor versions of the environment template exist. A minor version of an environment template is a version that's backward compatible.</p>

        Args:
            template_name: <p>The name of the environment template.</p>
            major_version: <p>The environment template major version to delete.</p>
            minor_version: <p>The environment template minor version to delete.</p>

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
            req: "OperationRequest[capo_proton.types.delete_environment_template_version_input.DeleteEnvironmentTemplateVersionInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_environment_template_version_output.DeleteEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_template_version

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_environment_template_version.delete_environment_template_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_template_version_input.DeleteEnvironmentTemplateVersionInput = {
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
    ) -> "capo_proton.types.list_environment_template_versions_output.ListEnvironmentTemplateVersionsOutput":
        """<p>List major or minor versions of an environment template with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next major or minor version in the array of major or minor versions of an environment template, after the list of major or minor versions that was previously requested.</p>
            max_results: <p>The maximum number of major or minor versions of an environment template to list.</p>
            template_name: <p>The name of the environment template.</p>
            major_version: <p>To view a list of minor of versions under a major version of an environment template, include <code>major Version</code>.</p> <p>To view a list of major versions of an environment template, <i>exclude</i> <code>major Version</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_environment_template_versions_input.ListEnvironmentTemplateVersionsInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_environment_template_versions_output.ListEnvironmentTemplateVersionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_template_versions

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_environment_template_versions.list_environment_template_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_template_versions_input.ListEnvironmentTemplateVersionsInput = {
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


class AsyncEnvironmentTemplateVersionResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def create(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        source: "capo_proton.types.template_version_source_input.TemplateVersionSourceInput",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        client_token: Optional["capo_proton.types.client_token.ClientToken"] = None,
        description: Optional["capo_proton.types.description.Description"] = None,
        major_version: Optional[
            "capo_proton.types.template_version_part.TemplateVersionPart"
        ] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_environment_template_version_output.CreateEnvironmentTemplateVersionOutput":
        """<p>Create a new major or minor version of an environment template. A major version of an environment template is a version that <i>isn't</i> backwards compatible. A minor version of an environment template is a version that's backwards compatible within its major version.</p>

        Args:
            client_token: <p>When included, if two identical requests are made with the same client token, Proton returns the environment template version that the first request created.</p>
            template_name: <p>The name of the environment template.</p>
            description: <p>A description of the new version of an environment template.</p>
            major_version: <p>To create a new minor version of the environment template, include <code>major Version</code>.</p> <p>To create a new major and minor version of the environment template, exclude <code>major Version</code>.</p>
            source: <p>An object that includes the template bundle S3 bucket path and name for the new version of an template.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton environment template version. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.create_environment_template_version_input.CreateEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_environment_template_version_output.CreateEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_environment_template_version.async_create_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_environment_template_version_input.CreateEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "source": source,
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
    ) -> "capo_proton.types.get_environment_template_version_output.GetEnvironmentTemplateVersionOutput":
        """<p>Get detailed data for a major or minor version of an environment template.</p>

        Args:
            template_name: <p>The name of the environment template a version of which you want to get detailed data for.</p>
            major_version: <p>To get environment template major version detail data, include <code>major Version</code>.</p>
            minor_version: <p>To get environment template minor version detail data, include <code>minorVersion</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_environment_template_version_input.GetEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_environment_template_version_output.GetEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_environment_template_version.async_get_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_environment_template_version_input.GetEnvironmentTemplateVersionInput = {
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
    ) -> "capo_proton.types.update_environment_template_version_output.UpdateEnvironmentTemplateVersionOutput":
        """<p>Update a major or minor version of an environment template.</p>

        Args:
            template_name: <p>The name of the environment template.</p>
            major_version: <p>To update a major version of an environment template, include <code>major Version</code>.</p>
            minor_version: <p>To update a minor version of an environment template, include <code>minorVersion</code>.</p>
            description: <p>A description of environment template version to update.</p>
            status: <p>The status of the environment template minor version to update.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.update_environment_template_version_input.UpdateEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_environment_template_version_output.UpdateEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_environment_template_version.async_update_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_environment_template_version_input.UpdateEnvironmentTemplateVersionInput = {
            "template_name": template_name,
            "major_version": major_version,
            "minor_version": minor_version,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status

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
    ) -> "capo_proton.types.delete_environment_template_version_output.DeleteEnvironmentTemplateVersionOutput":
        """<p>If no other minor versions of an environment template exist, delete a major version of the environment template if it's not the <code>Recommended</code> version. Delete the <code>Recommended</code> version of the environment template if no other major versions or minor versions of the environment template exist. A major version of an environment template is a version that's not backward compatible.</p> <p>Delete a minor version of an environment template if it <i>isn't</i> the <code>Recommended</code> version. Delete a <code>Recommended</code> minor version of the environment template if no other minor versions of the environment template exist. A minor version of an environment template is a version that's backward compatible.</p>

        Args:
            template_name: <p>The name of the environment template.</p>
            major_version: <p>The environment template major version to delete.</p>
            minor_version: <p>The environment template minor version to delete.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_environment_template_version_input.DeleteEnvironmentTemplateVersionInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_environment_template_version_output.DeleteEnvironmentTemplateVersionOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_environment_template_version

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_environment_template_version.async_delete_environment_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_environment_template_version_input.DeleteEnvironmentTemplateVersionInput = {
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
    ) -> "capo_proton.types.list_environment_template_versions_output.ListEnvironmentTemplateVersionsOutput":
        """<p>List major or minor versions of an environment template with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next major or minor version in the array of major or minor versions of an environment template, after the list of major or minor versions that was previously requested.</p>
            max_results: <p>The maximum number of major or minor versions of an environment template to list.</p>
            template_name: <p>The name of the environment template.</p>
            major_version: <p>To view a list of minor of versions under a major version of an environment template, include <code>major Version</code>.</p> <p>To view a list of major versions of an environment template, <i>exclude</i> <code>major Version</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_environment_template_versions_input.ListEnvironmentTemplateVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_environment_template_versions_output.ListEnvironmentTemplateVersionsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_environment_template_versions

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_environment_template_versions.async_list_environment_template_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_environment_template_versions_input.ListEnvironmentTemplateVersionsInput = {
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
