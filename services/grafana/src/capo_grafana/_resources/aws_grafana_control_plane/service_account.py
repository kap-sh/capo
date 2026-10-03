from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_grafana._auth._signers
import capo_grafana._auth._sigv4
from capo_grafana._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_grafana.types.create_workspace_service_account_request
    import capo_grafana.types.create_workspace_service_account_response
    import capo_grafana.types.delete_workspace_service_account_request
    import capo_grafana.types.delete_workspace_service_account_response
    import capo_grafana.types.list_workspace_service_accounts_request
    import capo_grafana.types.list_workspace_service_accounts_response
    import capo_grafana.types.pagination_token
    import capo_grafana.types.role
    import capo_grafana.types.service_account_name
    import capo_grafana.types.service_account_summary
    import capo_grafana.types.workspace_id
    from capo_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from capo_grafana._services.grafana import grafanaClient, grafanaClientConfig


class ServiceAccount:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def create_workspace_service_account(
        self,
        name: "capo_grafana.types.service_account_name.ServiceAccountName",
        grafana_role: "capo_grafana.types.role.Role",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse":
        """<p>Creates a service account for the workspace. A service account can be used to call Grafana HTTP APIs, and run automated workloads. After creating the service account with the correct <code>GrafanaRole</code> for your use case, use <code>CreateWorkspaceServiceAccountToken</code> to create a token that can be used to authenticate and authorize Grafana HTTP API calls.</p> <p>You can only create service accounts for workspaces that are compatible with Grafana version 9 and above.</p> <note> <p>For more information about service accounts, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html">Service accounts</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> <p>For more information about the Grafana HTTP APIs, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html">Using Grafana HTTP APIs</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>

        Args:
            name: <p>A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.</p>
            grafana_role: <p>The permission level to use for this service account.</p> <note> <p>For more information about the roles and the permissions each has, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html">User roles</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>
            workspace_id: <p>The ID of the workspace within which to create the service account.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account.create_workspace_service_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest = {
            "name": name,
            "grafana_role": grafana_role,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace_service_account(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse":
        """<p>Deletes a workspace service account from the workspace.</p> <p>This will delete any tokens created for the service account, as well. If the tokens are currently in use, the will fail to authenticate / authorize after they are deleted.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            service_account_id: <p>The ID of the service account to delete.</p>
            workspace_id: <p>The ID of the workspace where the service account resides.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account.delete_workspace_service_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest = {
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workspace_service_accounts(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse":
        """<p>Returns a list of service accounts for a workspace.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of service accounts to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccounts</code> operation.)</p>
            workspace_id: <p>The workspace for which to list service accounts.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts.list_workspace_service_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncServiceAccount:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def create_workspace_service_account(
        self,
        name: "capo_grafana.types.service_account_name.ServiceAccountName",
        grafana_role: "capo_grafana.types.role.Role",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse":
        """<p>Creates a service account for the workspace. A service account can be used to call Grafana HTTP APIs, and run automated workloads. After creating the service account with the correct <code>GrafanaRole</code> for your use case, use <code>CreateWorkspaceServiceAccountToken</code> to create a token that can be used to authenticate and authorize Grafana HTTP API calls.</p> <p>You can only create service accounts for workspaces that are compatible with Grafana version 9 and above.</p> <note> <p>For more information about service accounts, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html">Service accounts</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> <p>For more information about the Grafana HTTP APIs, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/Using-Grafana-APIs.html">Using Grafana HTTP APIs</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>

        Args:
            name: <p>A name for the service account. The name must be unique within the workspace, as it determines the ID associated with the service account.</p>
            grafana_role: <p>The permission level to use for this service account.</p> <note> <p>For more information about the roles and the permissions each has, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/Grafana-user-roles.html">User roles</a> in the <i>Amazon Managed Grafana User Guide</i>.</p> </note>
            workspace_id: <p>The ID of the workspace within which to create the service account.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota to be exceeded.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.create_workspace_service_account_response.CreateWorkspaceServiceAccountResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account.async_create_workspace_service_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_service_account_request.CreateWorkspaceServiceAccountRequest = {
            "name": name,
            "grafana_role": grafana_role,
            "workspace_id": workspace_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workspace_service_account(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse":
        """<p>Deletes a workspace service account from the workspace.</p> <p>This will delete any tokens created for the service account, as well. If the tokens are currently in use, the will fail to authenticate / authorize after they are deleted.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            service_account_id: <p>The ID of the service account to delete.</p>
            workspace_id: <p>The ID of the workspace where the service account resides.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.delete_workspace_service_account_response.DeleteWorkspaceServiceAccountResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account.async_delete_workspace_service_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_service_account_request.DeleteWorkspaceServiceAccountRequest = {
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workspace_service_accounts(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse":
        """<p>Returns a list of service accounts for a workspace.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of service accounts to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccounts</code> operation.)</p>
            workspace_id: <p>The workspace for which to list service accounts.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.conflict_exception.ConflictException: <p>A resource was in an inconsistent state during an update or a deletion.</p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.list_workspace_service_accounts_response.ListWorkspaceServiceAccountsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_accounts.async_list_workspace_service_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspace_service_accounts_request.ListWorkspaceServiceAccountsRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
