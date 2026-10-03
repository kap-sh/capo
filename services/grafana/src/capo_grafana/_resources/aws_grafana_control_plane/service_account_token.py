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
    import capo_grafana.types.create_workspace_service_account_token_request
    import capo_grafana.types.create_workspace_service_account_token_response
    import capo_grafana.types.delete_workspace_service_account_token_request
    import capo_grafana.types.delete_workspace_service_account_token_response
    import capo_grafana.types.list_workspace_service_account_tokens_request
    import capo_grafana.types.list_workspace_service_account_tokens_response
    import capo_grafana.types.pagination_token
    import capo_grafana.types.service_account_token_name
    import capo_grafana.types.service_account_token_summary
    import capo_grafana.types.workspace_id
    from capo_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from capo_grafana._services.grafana import grafanaClient, grafanaClientConfig


class ServiceAccountToken:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def create_workspace_service_account_token(
        self,
        name: "capo_grafana.types.service_account_token_name.ServiceAccountTokenName",
        seconds_to_live: int,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse":
        """<p>Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given <a href="https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html">workspace service account</a>. The service account acts as a user for the API operations, and defines the permissions that are used by the API.</p> <important> <p>When you create the service account token, you will receive a key that is used when calling Grafana APIs. Do not lose this key, as it will not be retrievable again.</p> <p>If you do lose the key, you can delete the token and recreate it to receive a new key. This will disable the initial key.</p> </important> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            name: <p>A name for the token to create.</p>
            seconds_to_live: <p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>
            service_account_id: <p>The ID of the service account for which to create a token.</p>
            workspace_id: <p>The ID of the workspace the service account resides within.</p>

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
            req: "OperationRequest[capo_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token.create_workspace_service_account_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest = {
            "name": name,
            "seconds_to_live": seconds_to_live,
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

    def delete_workspace_service_account_token(
        self,
        token_id: str,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse":
        """<p>Deletes a token for the workspace service account.</p> <p>This will disable the key associated with the token. If any automation is currently using the key, it will no longer be authenticated or authorized to perform actions with the Grafana HTTP APIs.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            token_id: <p>The ID of the token to delete.</p>
            service_account_id: <p>The ID of the service account from which to delete the token.</p>
            workspace_id: <p>The ID of the workspace from which to delete the token.</p>

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
            req: "OperationRequest[capo_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token.delete_workspace_service_account_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest = {
            "token_id": token_id,
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

    def list_workspace_service_account_tokens(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse":
        """<p>Returns a list of tokens for a workspace service account.</p> <note> <p>This does not return the key for each token. You cannot access keys after they are created. To create a new key, delete the token and recreate it.</p> </note> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of tokens to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccountTokens</code> operation.)</p>
            service_account_id: <p>The ID of the service account for which to return tokens.</p>
            workspace_id: <p>The ID of the workspace for which to return tokens.</p>

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
            req: "OperationRequest[capo_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens.list_workspace_service_account_tokens(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest = {
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
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


class AsyncServiceAccountToken:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def create_workspace_service_account_token(
        self,
        name: "capo_grafana.types.service_account_token_name.ServiceAccountTokenName",
        seconds_to_live: int,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse":
        """<p>Creates a token that can be used to authenticate and authorize Grafana HTTP API operations for the given <a href="https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html">workspace service account</a>. The service account acts as a user for the API operations, and defines the permissions that are used by the API.</p> <important> <p>When you create the service account token, you will receive a key that is used when calling Grafana APIs. Do not lose this key, as it will not be retrievable again.</p> <p>If you do lose the key, you can delete the token and recreate it to receive a new key. This will disable the initial key.</p> </important> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            name: <p>A name for the token to create.</p>
            seconds_to_live: <p>Sets how long the token will be valid, in seconds. You can set the time up to 30 days in the future.</p>
            service_account_id: <p>The ID of the service account for which to create a token.</p>
            workspace_id: <p>The ID of the workspace the service account resides within.</p>

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
            req: "AsyncOperationRequest[capo_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.create_workspace_service_account_token_response.CreateWorkspaceServiceAccountTokenResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.create_workspace_service_account_token.async_create_workspace_service_account_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.create_workspace_service_account_token_request.CreateWorkspaceServiceAccountTokenRequest = {
            "name": name,
            "seconds_to_live": seconds_to_live,
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

    async def delete_workspace_service_account_token(
        self,
        token_id: str,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse":
        """<p>Deletes a token for the workspace service account.</p> <p>This will disable the key associated with the token. If any automation is currently using the key, it will no longer be authenticated or authorized to perform actions with the Grafana HTTP APIs.</p> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            token_id: <p>The ID of the token to delete.</p>
            service_account_id: <p>The ID of the service account from which to delete the token.</p>
            workspace_id: <p>The ID of the workspace from which to delete the token.</p>

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
            req: "AsyncOperationRequest[capo_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.delete_workspace_service_account_token_response.DeleteWorkspaceServiceAccountTokenResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.delete_workspace_service_account_token.async_delete_workspace_service_account_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.delete_workspace_service_account_token_request.DeleteWorkspaceServiceAccountTokenRequest = {
            "token_id": token_id,
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

    async def list_workspace_service_account_tokens(
        self,
        service_account_id: str,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_grafana.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse":
        """<p>Returns a list of tokens for a workspace service account.</p> <note> <p>This does not return the key for each token. You cannot access keys after they are created. To create a new key, delete the token and recreate it.</p> </note> <p>Service accounts are only available for workspaces that are compatible with Grafana version 9 and above.</p>

        Args:
            max_results: <p>The maximum number of tokens to include in the results.</p>
            next_token: <p>The token for the next set of service accounts to return. (You receive this token from a previous <code>ListWorkspaceServiceAccountTokens</code> operation.)</p>
            service_account_id: <p>The ID of the service account for which to return tokens.</p>
            workspace_id: <p>The ID of the workspace for which to return tokens.</p>

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
            req: "AsyncOperationRequest[capo_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.list_workspace_service_account_tokens_response.ListWorkspaceServiceAccountTokensResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.list_workspace_service_account_tokens.async_list_workspace_service_account_tokens(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.list_workspace_service_account_tokens_request.ListWorkspaceServiceAccountTokensRequest = {
            "service_account_id": service_account_id,
            "workspace_id": workspace_id,
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
