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
    import capo_grafana.types.authentication_providers
    import capo_grafana.types.describe_workspace_authentication_request
    import capo_grafana.types.describe_workspace_authentication_response
    import capo_grafana.types.saml_configuration
    import capo_grafana.types.update_workspace_authentication_request
    import capo_grafana.types.update_workspace_authentication_response
    import capo_grafana.types.workspace_id
    from capo_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from capo_grafana._services.grafana import grafanaClient, grafanaClientConfig


class Authentication:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def read(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_authentication_response.DescribeWorkspaceAuthenticationResponse":
        """<p>Displays information about the authentication methods used in one Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to return authentication information about.</p>

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
            req: "OperationRequest[capo_grafana.types.describe_workspace_authentication_request.DescribeWorkspaceAuthenticationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.describe_workspace_authentication_response.DescribeWorkspaceAuthenticationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace_authentication

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.describe_workspace_authentication.describe_workspace_authentication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_authentication_request.DescribeWorkspaceAuthenticationRequest = {
            "workspace_id": workspace_id
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
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        authentication_providers: "capo_grafana.types.authentication_providers.AuthenticationProviders",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        saml_configuration: Optional[
            "capo_grafana.types.saml_configuration.SamlConfiguration"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_authentication_response.UpdateWorkspaceAuthenticationResponse":
        """<p>Use this operation to define the identity provider (IdP) that this workspace authenticates users from, using SAML. You can also map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p> <note> <p>Changes to the authentication method for a workspace may take a few minutes to take effect.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to update the authentication for.</p>
            authentication_providers: <p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html">User authentication in Amazon Managed Grafana</a>.</p>
            saml_configuration: <p>If the workspace uses SAML, use this structure to map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p>

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
            req: "OperationRequest[capo_grafana.types.update_workspace_authentication_request.UpdateWorkspaceAuthenticationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_workspace_authentication_response.UpdateWorkspaceAuthenticationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace_authentication

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_workspace_authentication.update_workspace_authentication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_authentication_request.UpdateWorkspaceAuthenticationRequest = {
            "workspace_id": workspace_id,
            "authentication_providers": authentication_providers,
        }
        if saml_configuration is not None:
            input_["saml_configuration"] = saml_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAuthentication:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def read(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_authentication_response.DescribeWorkspaceAuthenticationResponse":
        """<p>Displays information about the authentication methods used in one Amazon Managed Grafana workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to return authentication information about.</p>

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
            req: "AsyncOperationRequest[capo_grafana.types.describe_workspace_authentication_request.DescribeWorkspaceAuthenticationRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.describe_workspace_authentication_response.DescribeWorkspaceAuthenticationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace_authentication

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.describe_workspace_authentication.async_describe_workspace_authentication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_authentication_request.DescribeWorkspaceAuthenticationRequest = {
            "workspace_id": workspace_id
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
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        authentication_providers: "capo_grafana.types.authentication_providers.AuthenticationProviders",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        saml_configuration: Optional[
            "capo_grafana.types.saml_configuration.SamlConfiguration"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_authentication_response.UpdateWorkspaceAuthenticationResponse":
        """<p>Use this operation to define the identity provider (IdP) that this workspace authenticates users from, using SAML. You can also map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p> <note> <p>Changes to the authentication method for a workspace may take a few minutes to take effect.</p> </note>

        Args:
            workspace_id: <p>The ID of the workspace to update the authentication for.</p>
            authentication_providers: <p>Specifies whether this workspace uses SAML 2.0, IAM Identity Center, or both to authenticate users for using the Grafana console within a workspace. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html">User authentication in Amazon Managed Grafana</a>.</p>
            saml_configuration: <p>If the workspace uses SAML, use this structure to map SAML assertion attributes to workspace user information and define which groups in the assertion attribute are to have the <code>Admin</code> and <code>Editor</code> roles in the workspace.</p>

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
            req: "AsyncOperationRequest[capo_grafana.types.update_workspace_authentication_request.UpdateWorkspaceAuthenticationRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.update_workspace_authentication_response.UpdateWorkspaceAuthenticationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace_authentication

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.update_workspace_authentication.async_update_workspace_authentication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_authentication_request.UpdateWorkspaceAuthenticationRequest = {
            "workspace_id": workspace_id,
            "authentication_providers": authentication_providers,
        }
        if saml_configuration is not None:
            input_["saml_configuration"] = saml_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
