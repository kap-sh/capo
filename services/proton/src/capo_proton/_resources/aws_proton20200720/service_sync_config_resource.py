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
    import capo_proton.types.create_service_sync_config_input
    import capo_proton.types.create_service_sync_config_output
    import capo_proton.types.delete_service_sync_config_input
    import capo_proton.types.delete_service_sync_config_output
    import capo_proton.types.get_service_sync_config_input
    import capo_proton.types.get_service_sync_config_output
    import capo_proton.types.git_branch_name
    import capo_proton.types.ops_file_path
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.resource_name
    import capo_proton.types.update_service_sync_config_input
    import capo_proton.types.update_service_sync_config_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class ServiceSyncConfigResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        file_path: "capo_proton.types.ops_file_path.OpsFilePath",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput":
        """<p>Create the Proton Ops configuration file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name.</p>
            branch: <p>The repository branch for your Proton Ops file.</p>
            file_path: <p>The path to the Proton Ops file.</p>

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
            req: "OperationRequest[capo_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_service_sync_config.create_service_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput = {
            "service_name": service_name,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
            "file_path": file_path,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput":
        """<p>Get detailed information for the service sync configuration.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync configuration for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_service_sync_config.get_service_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput = {
            "service_name": service_name
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
        service_name: "capo_proton.types.resource_name.ResourceName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        file_path: "capo_proton.types.ops_file_path.OpsFilePath",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput":
        """<p>Update the Proton Ops config file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The name of the repository provider where the Proton Ops file is found.</p>
            repository_name: <p>The name of the repository where the Proton Ops file is found.</p>
            branch: <p>The name of the code repository branch where the Proton Ops file is found.</p>
            file_path: <p>The path to the Proton Ops file.</p>

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
            req: "OperationRequest[capo_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_service_sync_config.update_service_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput = {
            "service_name": service_name,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
            "file_path": file_path,
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
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput":
        """<p>Delete the Proton Ops file.</p>

        Args:
            service_name: <p>The name of the service that you want to delete the service sync configuration for.</p>

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
            req: "OperationRequest[capo_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_sync_config

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_service_sync_config.delete_service_sync_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput = {
            "service_name": service_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceSyncConfigResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        file_path: "capo_proton.types.ops_file_path.OpsFilePath",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput":
        """<p>Create the Proton Ops configuration file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The provider type for your repository.</p>
            repository_name: <p>The repository name.</p>
            branch: <p>The repository branch for your Proton Ops file.</p>
            file_path: <p>The path to the Proton Ops file.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_service_sync_config_output.CreateServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_service_sync_config.async_create_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_service_sync_config_input.CreateServiceSyncConfigInput = {
            "service_name": service_name,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
            "file_path": file_path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput":
        """<p>Get detailed information for the service sync configuration.</p>

        Args:
            service_name: <p>The name of the service that you want to get the service sync configuration for.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_service_sync_config_output.GetServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_service_sync_config.async_get_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_service_sync_config_input.GetServiceSyncConfigInput = {
            "service_name": service_name
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
        service_name: "capo_proton.types.resource_name.ResourceName",
        repository_provider: "capo_proton.types.repository_provider.RepositoryProvider",
        repository_name: "capo_proton.types.repository_name.RepositoryName",
        branch: "capo_proton.types.git_branch_name.GitBranchName",
        file_path: "capo_proton.types.ops_file_path.OpsFilePath",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput":
        """<p>Update the Proton Ops config file.</p>

        Args:
            service_name: <p>The name of the service the Proton Ops file is for.</p>
            repository_provider: <p>The name of the repository provider where the Proton Ops file is found.</p>
            repository_name: <p>The name of the repository where the Proton Ops file is found.</p>
            branch: <p>The name of the code repository branch where the Proton Ops file is found.</p>
            file_path: <p>The path to the Proton Ops file.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_service_sync_config_output.UpdateServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_service_sync_config.async_update_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.update_service_sync_config_input.UpdateServiceSyncConfigInput = {
            "service_name": service_name,
            "repository_provider": repository_provider,
            "repository_name": repository_name,
            "branch": branch,
            "file_path": file_path,
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
        service_name: "capo_proton.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput":
        """<p>Delete the Proton Ops file.</p>

        Args:
            service_name: <p>The name of the service that you want to delete the service sync configuration for.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_service_sync_config_output.DeleteServiceSyncConfigOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_service_sync_config

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_service_sync_config.async_delete_service_sync_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_service_sync_config_input.DeleteServiceSyncConfigInput = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
