from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application
    import capo_mgn.types.application_description
    import capo_mgn.types.application_id
    import capo_mgn.types.application_name
    import capo_mgn.types.archive_application_request
    import capo_mgn.types.associate_source_servers_request
    import capo_mgn.types.associate_source_servers_request_source_server_i_ds
    import capo_mgn.types.associate_source_servers_response
    import capo_mgn.types.create_application_request
    import capo_mgn.types.delete_application_request
    import capo_mgn.types.delete_application_response
    import capo_mgn.types.disassociate_source_servers_request
    import capo_mgn.types.disassociate_source_servers_request_source_server_i_ds
    import capo_mgn.types.disassociate_source_servers_response
    import capo_mgn.types.list_applications_request
    import capo_mgn.types.list_applications_request_filters
    import capo_mgn.types.list_applications_response
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.tags_map
    import capo_mgn.types.unarchive_application_request
    import capo_mgn.types.update_application_request
    from capo_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig
    from capo_mgn._services.mgn import mgnClient, mgnClientConfig


class ApplicationResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

    def create(
        self,
        name: "capo_mgn.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional[
            "capo_mgn.types.application_description.ApplicationDescription"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Create application.</p>

        Args:
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            tags: <p>Application tags.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.create_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_application_request.CreateApplicationRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_application_request

            return capo_mgn.types.create_application_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateApplication",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_application_request.CreateApplicationRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_application_response.DeleteApplicationResponse":
        """<p>Delete application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplication")
        )
        input_: capo_mgn.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves all applications or multiple applications by ID.</p>

        Args:
            filters: <p>Applications list filters.</p>
            max_results: <p>Maximum results to return when listing applications.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Applications list Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_applications

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_applications_response.ListApplicationsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_applications_response

            return capo_mgn.types.list_applications_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListApplications", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_applications_request.ListApplicationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def archive_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Archive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.archive_application_request.ArchiveApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.archive_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.archive_application.archive_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ArchiveApplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.archive_application_request.ArchiveApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_source_servers(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "capo_mgn.types.associate_source_servers_request_source_server_i_ds.AssociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.associate_source_servers_response.AssociateSourceServersResponse":
        """<p>Associate source servers to application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.associate_source_servers_request.AssociateSourceServersRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.associate_source_servers_response.AssociateSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.associate_source_servers

            output, http_response = (
                capo_mgn._operations.application_migration_service.associate_source_servers.associate_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateSourceServers")
        )
        input_: capo_mgn.types.associate_source_servers_request.AssociateSourceServersRequest = {
            "application_id": application_id,
            "source_server_i_ds": source_server_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_source_servers(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "capo_mgn.types.disassociate_source_servers_request_source_server_i_ds.DisassociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse":
        """<p>Disassociate source servers from application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.disassociate_source_servers

            output, http_response = (
                capo_mgn._operations.application_migration_service.disassociate_source_servers.disassociate_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateSourceServers")
        )
        input_: capo_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest = {
            "application_id": application_id,
            "source_server_i_ds": source_server_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def unarchive_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Unarchive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.unarchive_application_request.UnarchiveApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.unarchive_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.unarchive_application.unarchive_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UnarchiveApplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.unarchive_application_request.UnarchiveApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.application_name.ApplicationName"] = None,
        description: Optional[
            "capo_mgn.types.application_description.ApplicationDescription"
        ] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Update application.</p>

        Args:
            application_id: <p>Application ID.</p>
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.update_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateApplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApplicationResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service

    async def create(
        self,
        name: "capo_mgn.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        description: Optional[
            "capo_mgn.types.application_description.ApplicationDescription"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Create application.</p>

        Args:
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            tags: <p>Application tags.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.create_application

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_mgn.types.create_application_request.CreateApplicationRequest",
        ) -> dict[str, Any]:
            import capo_mgn.types.create_application_request

            return capo_mgn.types.create_application_request.redact_sensitive(input_)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "CreateApplication",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_mgn.types.create_application_request.CreateApplicationRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_application_response.DeleteApplicationResponse":
        """<p>Delete application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_application

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteApplication")
        )
        input_: capo_mgn.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves all applications or multiple applications by ID.</p>

        Args:
            filters: <p>Applications list filters.</p>
            max_results: <p>Maximum results to return when listing applications.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Applications list Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_applications

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.list_applications_response.ListApplicationsResponse",
        ) -> dict[str, Any]:
            import capo_mgn.types.list_applications_response

            return capo_mgn.types.list_applications_response.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListApplications", redact_output=_redact_output),
        )
        input_: capo_mgn.types.list_applications_request.ListApplicationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def archive_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Archive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.archive_application_request.ArchiveApplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.archive_application

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.archive_application.async_archive_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ArchiveApplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.archive_application_request.ArchiveApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_source_servers(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "capo_mgn.types.associate_source_servers_request_source_server_i_ds.AssociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.associate_source_servers_response.AssociateSourceServersResponse":
        """<p>Associate source servers to application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.associate_source_servers_request.AssociateSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.associate_source_servers_response.AssociateSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.associate_source_servers

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.associate_source_servers.async_associate_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateSourceServers")
        )
        input_: capo_mgn.types.associate_source_servers_request.AssociateSourceServersRequest = {
            "application_id": application_id,
            "source_server_i_ds": source_server_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_source_servers(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "capo_mgn.types.disassociate_source_servers_request_source_server_i_ds.DisassociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse":
        """<p>Disassociate source servers from application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest]",
        ) -> AsyncOperationResponse[
            "capo_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.disassociate_source_servers

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.disassociate_source_servers.async_disassociate_source_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateSourceServers")
        )
        input_: capo_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest = {
            "application_id": application_id,
            "source_server_i_ds": source_server_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unarchive_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Unarchive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.unarchive_application_request.UnarchiveApplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.unarchive_application

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.unarchive_application.async_unarchive_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UnarchiveApplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.unarchive_application_request.UnarchiveApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[AsyncmgnClientConfig] = None,
        name: Optional["capo_mgn.types.application_name.ApplicationName"] = None,
        description: Optional[
            "capo_mgn.types.application_description.ApplicationDescription"
        ] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Update application.</p>

        Args:
            application_id: <p>Application ID.</p>
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mgn.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.update_application

            (
                output,
                http_response,
            ) = await capo_mgn._operations.application_migration_service.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_mgn.types.application.Application",
        ) -> dict[str, Any]:
            import capo_mgn.types.application

            return capo_mgn.types.application.redact_sensitive(output)

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateApplication", redact_output=_redact_output),
        )
        input_: capo_mgn.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
