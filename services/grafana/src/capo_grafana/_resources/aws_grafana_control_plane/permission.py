from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_grafana._auth._signers
import capo_grafana._auth._sigv4
from capo_grafana._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_grafana.types.list_permissions_request
    import capo_grafana.types.list_permissions_response
    import capo_grafana.types.pagination_token
    import capo_grafana.types.permission_entry
    import capo_grafana.types.sso_id
    import capo_grafana.types.update_instruction_batch
    import capo_grafana.types.update_permissions_request
    import capo_grafana.types.update_permissions_response
    import capo_grafana.types.user_type
    import capo_grafana.types.workspace_id
    from capo_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from capo_grafana._services.grafana import grafanaClient, grafanaClientConfig


class Permission:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def read(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
        user_type: Optional["capo_grafana.types.user_type.UserType"] = None,
        user_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
        group_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
    ) -> "capo_grafana.types.list_permissions_response.ListPermissionsResponse":
        """<p>Lists the users and groups who have the Grafana <code>Admin</code> and <code>Editor</code> roles in this workspace. If you use this operation without specifying <code>userId</code> or <code>groupId</code>, the operation returns the roles of all users and groups. If you specify a <code>userId</code> or a <code>groupId</code>, only the roles for that user or group are returned. If you do this, you can specify only one <code>userId</code> or one <code>groupId</code>.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.</p>
            user_type: <p>(Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.</p>
            user_id: <p>(Optional) Limits the results to only the user that matches this ID.</p>
            group_id: <p>(Optional) Limits the results to only the group that matches this ID.</p>
            workspace_id: <p>The ID of the workspace to list permissions for. This parameter is required.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.list_permissions_request.ListPermissionsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_permissions

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_permissions.list_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPermissions")
        )
        input_: capo_grafana.types.list_permissions_request.ListPermissionsRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if user_type is not None:
            input_["user_type"] = user_type
        if user_id is not None:
            input_["user_id"] = user_id
        if group_id is not None:
            input_["group_id"] = group_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        update_instruction_batch: "capo_grafana.types.update_instruction_batch.UpdateInstructionBatch",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.update_permissions_response.UpdatePermissionsResponse":
        """<p>Updates which users in a workspace have the Grafana <code>Admin</code> or <code>Editor</code> roles.</p>

        Args:
            update_instruction_batch: <p>An array of structures that contain the permission updates to make.</p>
            workspace_id: <p>The ID of the workspace to update.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.update_permissions_request.UpdatePermissionsRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_permissions_response.UpdatePermissionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_permissions

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_permissions.update_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePermissions")
        )
        input_: capo_grafana.types.update_permissions_request.UpdatePermissionsRequest = {
            "update_instruction_batch": update_instruction_batch,
            "workspace_id": workspace_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPermission:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def read(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
        user_type: Optional["capo_grafana.types.user_type.UserType"] = None,
        user_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
        group_id: Optional["capo_grafana.types.sso_id.SsoId"] = None,
    ) -> "capo_grafana.types.list_permissions_response.ListPermissionsResponse":
        """<p>Lists the users and groups who have the Grafana <code>Admin</code> and <code>Editor</code> roles in this workspace. If you use this operation without specifying <code>userId</code> or <code>groupId</code>, the operation returns the roles of all users and groups. If you specify a <code>userId</code> or a <code>groupId</code>, only the roles for that user or group are returned. If you do this, you can specify only one <code>userId</code> or one <code>groupId</code>.</p>

        Args:
            max_results: <p>The maximum number of results to include in the response.</p>
            next_token: <p>The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.</p>
            user_type: <p>(Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.</p>
            user_id: <p>(Optional) Limits the results to only the user that matches this ID.</p>
            group_id: <p>(Optional) Limits the results to only the group that matches this ID.</p>
            workspace_id: <p>The ID of the workspace to list permissions for. This parameter is required.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.list_permissions_request.ListPermissionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.list_permissions_response.ListPermissionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_permissions

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.list_permissions.async_list_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListPermissions")
        )
        input_: capo_grafana.types.list_permissions_request.ListPermissionsRequest = {
            "workspace_id": workspace_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if user_type is not None:
            input_["user_type"] = user_type
        if user_id is not None:
            input_["user_id"] = user_id
        if group_id is not None:
            input_["group_id"] = group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        update_instruction_batch: "capo_grafana.types.update_instruction_batch.UpdateInstructionBatch",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.update_permissions_response.UpdatePermissionsResponse":
        """<p>Updates which users in a workspace have the Grafana <code>Admin</code> or <code>Editor</code> roles.</p>

        Args:
            update_instruction_batch: <p>An array of structures that contain the permission updates to make.</p>
            workspace_id: <p>The ID of the workspace to update.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.update_permissions_request.UpdatePermissionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.update_permissions_response.UpdatePermissionsResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_permissions

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.update_permissions.async_update_permissions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdatePermissions")
        )
        input_: capo_grafana.types.update_permissions_request.UpdatePermissionsRequest = {
            "update_instruction_batch": update_instruction_batch,
            "workspace_id": workspace_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
