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
    import capo_proton.types.create_repository_input
    import capo_proton.types.create_repository_output
    import capo_proton.types.delete_repository_input
    import capo_proton.types.delete_repository_output
    import capo_proton.types.get_repository_input
    import capo_proton.types.get_repository_output
    import capo_proton.types.list_repositories_input
    import capo_proton.types.list_repositories_output
    import capo_proton.types.max_page_results
    import capo_proton.types.next_token
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider
    import capo_proton.types.repository_summary
    import capo_proton.types.tag_list
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class RepositoryResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def put(
        self,
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        connection_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_repository_output.CreateRepositoryOutput":
        """<p>Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a <a href="https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html">service-linked role</a> for you.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self">Self-managed provisioning</a>, <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles">Template bundles</a>, and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            connection_arn: <p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html">Setting up for Proton</a> in the <i>Proton User Guide</i>.</p>
            encryption_key: <p>The ARN of your customer Amazon Web Services Key Management Service (Amazon Web Services KMS) key.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton repository. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

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
            req: "OperationRequest[capo_proton.types.create_repository_input.CreateRepositoryInput]",
        ) -> OperationResponse[
            "capo_proton.types.create_repository_output.CreateRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_repository

            output, http_response = (
                capo_proton._operations.aws_proton20200720.create_repository.create_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_repository_input.CreateRepositoryInput = {
            "provider": provider,
            "name": name,
            "connection_arn": connection_arn,
        }
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
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
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.get_repository_output.GetRepositoryOutput":
        """<p>Get detail data for a linked repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name, for example <code>myrepos/myrepo</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_repository_input.GetRepositoryInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_repository_output.GetRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_repository

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_repository.get_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_repository_input.GetRepositoryInput = {
            "provider": provider,
            "name": name,
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
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_repository_output.DeleteRepositoryOutput":
        """<p>De-register and unlink your repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name.</p>

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
            req: "OperationRequest[capo_proton.types.delete_repository_input.DeleteRepositoryInput]",
        ) -> OperationResponse[
            "capo_proton.types.delete_repository_output.DeleteRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_repository

            output, http_response = (
                capo_proton._operations.aws_proton20200720.delete_repository.delete_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_repository_input.DeleteRepositoryInput = {
            "provider": provider,
            "name": name,
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
    ) -> "capo_proton.types.list_repositories_output.ListRepositoriesOutput":
        """<p>List linked repositories with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.</p>
            max_results: <p>The maximum number of repositories to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.list_repositories_input.ListRepositoriesInput]",
        ) -> OperationResponse[
            "capo_proton.types.list_repositories_output.ListRepositoriesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_repositories

            output, http_response = (
                capo_proton._operations.aws_proton20200720.list_repositories.list_repositories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_repositories_input.ListRepositoriesInput = {}
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


class AsyncRepositoryResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def put(
        self,
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        connection_arn: "capo_proton.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        encryption_key: Optional["capo_proton.types.arn.Arn"] = None,
        tags: Optional["capo_proton.types.tag_list.TagList"] = None,
    ) -> "capo_proton.types.create_repository_output.CreateRepositoryOutput":
        """<p>Create and register a link to a repository. Proton uses the link to repeatedly access the repository, to either push to it (self-managed provisioning) or pull from it (template sync). You can share a linked repository across multiple resources (like environments using self-managed provisioning, or synced templates). When you create a repository link, Proton creates a <a href="https://docs.aws.amazon.com/proton/latest/userguide/using-service-linked-roles.html">service-linked role</a> for you.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-works-prov-methods.html#ag-works-prov-methods-self">Self-managed provisioning</a>, <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-authoring.html#ag-template-bundles">Template bundles</a>, and <a href="https://docs.aws.amazon.com/proton/latest/userguide/ag-template-sync-configs.html">Template sync configurations</a> in the <i>Proton User Guide</i>.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name (for example, <code>myrepos/myrepo</code>).</p>
            connection_arn: <p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/setting-up-for-service.html">Setting up for Proton</a> in the <i>Proton User Guide</i>.</p>
            encryption_key: <p>The ARN of your customer Amazon Web Services Key Management Service (Amazon Web Services KMS) key.</p>
            tags: <p>An optional list of metadata items that you can associate with the Proton repository. A tag is a key-value pair.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html">Proton resources and tagging</a> in the <i>Proton User Guide</i>.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.create_repository_input.CreateRepositoryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.create_repository_output.CreateRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.create_repository

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.create_repository.async_create_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.create_repository_input.CreateRepositoryInput = {
            "provider": provider,
            "name": name,
            "connection_arn": connection_arn,
        }
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
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
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.get_repository_output.GetRepositoryOutput":
        """<p>Get detail data for a linked repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name, for example <code>myrepos/myrepo</code>.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_repository_input.GetRepositoryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_repository_output.GetRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_repository

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_repository.async_get_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.get_repository_input.GetRepositoryInput = {
            "provider": provider,
            "name": name,
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
        provider: "capo_proton.types.repository_provider.RepositoryProvider",
        name: "capo_proton.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
    ) -> "capo_proton.types.delete_repository_output.DeleteRepositoryOutput":
        """<p>De-register and unlink your repository.</p>

        Args:
            provider: <p>The repository provider.</p>
            name: <p>The repository name.</p>

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
            req: "AsyncOperationRequest[capo_proton.types.delete_repository_input.DeleteRepositoryInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.delete_repository_output.DeleteRepositoryOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.delete_repository

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.delete_repository.async_delete_repository(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.delete_repository_input.DeleteRepositoryInput = {
            "provider": provider,
            "name": name,
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
    ) -> "capo_proton.types.list_repositories_output.ListRepositoriesOutput":
        """<p>List linked repositories with detail data.</p>

        Args:
            next_token: <p>A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.</p>
            max_results: <p>The maximum number of repositories to list.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.list_repositories_input.ListRepositoriesInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.list_repositories_output.ListRepositoriesOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.list_repositories

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.list_repositories.async_list_repositories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_proton.types.list_repositories_input.ListRepositoriesInput = {}
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
