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
    import capo_proton.types.create_template_sync_config_input
    import capo_proton.types.create_template_sync_config_output
    import capo_proton.types.delete_template_sync_config_input
    import capo_proton.types.delete_template_sync_config_output
    import capo_proton.types.get_template_sync_config_input
    import capo_proton.types.get_template_sync_config_output
    import capo_proton.types.git_branch_name
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.resource_name
    import capo_proton.types.subdirectory
    import capo_proton.types.template_type
    import capo_proton.types.update_template_sync_config_input
    import capo_proton.types.update_template_sync_config_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class TemplateSyncConfigResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        subdirectory: Optional["capo_proton.types.subdirectory.Subdirectory"] = None,
    ) -> "capo_proton.types.create_template_sync_config_output.CreateTemplateSyncConfigOutput":
        """<p>Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>When a commit is pushed to your linked repository, Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            template_name: <p>The name of your registered template.</p>
            template_type: <p>The type of the registered template.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            branch: <p>The repository branch for your template.</p>
            subdirectory: <p>A repository subdirectory path to your template bundle directory. When included, Proton limits the template bundle search to this repository directory.</p>

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
            req: "OperationRequest[capo_proton.types.create_template_sync_config_input.CreateTemplateSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_template_sync_config_output.CreateTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_template_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_template_sync_config.create_template_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_template_sync_config_input.CreateTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

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
        template_type: "capo_proton.types.template_type.TemplateType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> (
        "capo_proton.types.get_template_sync_config_output.GetTemplateSyncConfigOutput"
    ):
        """<p>Get detail data for a template sync configuration.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_template_sync_config_input.GetTemplateSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_template_sync_config_output.GetTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_template_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_template_sync_config.get_template_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_template_sync_config_input.GetTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
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
        template_type: "capo_proton.types.template_type.TemplateType",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        subdirectory: Optional["capo_proton.types.subdirectory.Subdirectory"] = None,
    ) -> "capo_proton.types.update_template_sync_config_output.UpdateTemplateSyncConfigOutput":
        """<p>Update template sync configuration parameters, except for the <code>templateName</code> and <code>templateType</code>. Repository details (branch, name, and provider) should be of a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>

        Args:
            template_name: <p>The synced template name.</p>
            template_type: <p>The synced template type.</p>
            repository_provider: <p>The repository provider.</p>
            repository_name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            branch: <p>The repository branch for your template.</p>
            subdirectory: <p>A subdirectory path to your template bundle version. When included, limits the template bundle search to this repository directory.</p>

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
            req: "OperationRequest[capo_proton.types.update_template_sync_config_input.UpdateTemplateSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_template_sync_config_output.UpdateTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_template_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_template_sync_config.update_template_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_template_sync_config_input.UpdateTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

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
        template_type: "capo_proton.types.template_type.TemplateType",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_template_sync_config_output.DeleteTemplateSyncConfigOutput":
        """<p>Delete a template sync configuration.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>

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
            req: "OperationRequest[capo_proton.types.delete_template_sync_config_input.DeleteTemplateSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_template_sync_config_output.DeleteTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_template_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_template_sync_config.delete_template_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_template_sync_config_input.DeleteTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncTemplateSyncConfigResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        template_name: "capo_proton.types.resource_name.ResourceName",
        template_type: "capo_proton.types.template_type.TemplateType",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        subdirectory: Optional["capo_proton.types.subdirectory.Subdirectory"] = None,
    ) -> "capo_proton.types.create_template_sync_config_output.CreateTemplateSyncConfigOutput":
        """<p>Set up a template to create new template versions automatically by tracking a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>When a commit is pushed to your linked repository, Proton checks for changes to your repository template bundles. If it detects a template bundle change, a new major or minor version of its template is created, if the version doesn’t already exist. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            template_name: <p>The name of your registered template.</p>
            template_type: <p>The type of the registered template.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            branch: <p>The repository branch for your template.</p>
            subdirectory: <p>A repository subdirectory path to your template bundle directory. When included, Proton limits the template bundle search to this repository directory.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.create_template_sync_config_input.CreateTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_template_sync_config_output.CreateTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_template_sync_config.async_create_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_template_sync_config_input.CreateTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

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
        template_type: "capo_proton.types.template_type.TemplateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> (
        "capo_proton.types.get_template_sync_config_output.GetTemplateSyncConfigOutput"
    ):
        """<p>Get detail data for a template sync configuration.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_template_sync_config_input.GetTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_template_sync_config_output.GetTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_template_sync_config.async_get_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_template_sync_config_input.GetTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
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
        template_type: "capo_proton.types.template_type.TemplateType",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        subdirectory: Optional["capo_proton.types.subdirectory.Subdirectory"] = None,
    ) -> "capo_proton.types.update_template_sync_config_output.UpdateTemplateSyncConfigOutput":
        """<p>Update template sync configuration parameters, except for the <code>templateName</code> and <code>templateType</code>. Repository details (branch, name, and provider) should be of a linked repository. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>

        Args:
            template_name: <p>The synced template name.</p>
            template_type: <p>The synced template type.</p>
            repository_provider: <p>The repository provider.</p>
            repository_name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            branch: <p>The repository branch for your template.</p>
            subdirectory: <p>A subdirectory path to your template bundle version. When included, limits the template bundle search to this repository directory.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.update_template_sync_config_input.UpdateTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_template_sync_config_output.UpdateTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_template_sync_config.async_update_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_template_sync_config_input.UpdateTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
        }
        if subdirectory is not None:
            input_["subdirectory"] = subdirectory

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
        template_type: "capo_proton.types.template_type.TemplateType",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_template_sync_config_output.DeleteTemplateSyncConfigOutput":
        """<p>Delete a template sync configuration.</p>

        Args:
            template_name: <p>The template name.</p>
            template_type: <p>The template type.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_template_sync_config_input.DeleteTemplateSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_template_sync_config_output.DeleteTemplateSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_template_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_template_sync_config.async_delete_template_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_template_sync_config_input.DeleteTemplateSyncConfigInput = {
            "template_name": template_name,
            "template_type": template_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
