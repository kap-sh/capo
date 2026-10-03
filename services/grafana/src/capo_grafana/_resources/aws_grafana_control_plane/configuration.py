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
    import capo_grafana.types.describe_workspace_configuration_request
    import capo_grafana.types.describe_workspace_configuration_response
    import capo_grafana.types.grafana_version
    import capo_grafana.types.overridable_configuration_json
    import capo_grafana.types.update_workspace_configuration_request
    import capo_grafana.types.update_workspace_configuration_response
    import capo_grafana.types.workspace_id
    from capo_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from capo_grafana._services.grafana import grafanaClient, grafanaClientConfig


class Configuration:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def describe_workspace_configuration(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse":
        """<p>Gets the current configuration string for the given workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to get configuration information for.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration.describe_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace_configuration(
        self,
        configuration: "capo_grafana.types.overridable_configuration_json.OverridableConfigurationJson",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        grafana_version: Optional[
            "capo_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse":
        """<p>Updates the configuration string for the given workspace</p>

        Args:
            configuration: <p>The new configuration string for the workspace. For more information about the format and configuration options available, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html">Working in your Grafana workspace</a>.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.</p> <p>Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).</p> <p>To know what versions are available to upgrade to for a specific workspace, see the <a href="https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html">ListVersions</a> operation.</p>

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
            req: "OperationRequest[capo_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace_configuration

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.update_workspace_configuration.update_workspace_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest = {
            "configuration": configuration,
            "workspace_id": workspace_id,
        }
        if grafana_version is not None:
            input_["grafana_version"] = grafana_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncConfiguration:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def describe_workspace_configuration(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse":
        """<p>Gets the current configuration string for the given workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to get configuration information for.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.describe_workspace_configuration_response.DescribeWorkspaceConfigurationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.describe_workspace_configuration.async_describe_workspace_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.describe_workspace_configuration_request.DescribeWorkspaceConfigurationRequest = {
            "workspace_id": workspace_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workspace_configuration(
        self,
        configuration: "capo_grafana.types.overridable_configuration_json.OverridableConfigurationJson",
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        grafana_version: Optional[
            "capo_grafana.types.grafana_version.GrafanaVersion"
        ] = None,
    ) -> "capo_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse":
        """<p>Updates the configuration string for the given workspace</p>

        Args:
            configuration: <p>The new configuration string for the workspace. For more information about the format and configuration options available, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/AMG-configure-workspace.html">Working in your Grafana workspace</a>.</p>
            workspace_id: <p>The ID of the workspace to update.</p>
            grafana_version: <p>Specifies the version of Grafana to support in the workspace. If not specified, keeps the current version of the workspace.</p> <p>Can only be used to upgrade (for example, from 8.4 to 9.4), not downgrade (for example, from 9.4 to 8.4).</p> <p>To know what versions are available to upgrade to for a specific workspace, see the <a href="https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html">ListVersions</a> operation.</p>

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
            req: "AsyncOperationRequest[capo_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.update_workspace_configuration_response.UpdateWorkspaceConfigurationResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.update_workspace_configuration

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.update_workspace_configuration.async_update_workspace_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.update_workspace_configuration_request.UpdateWorkspaceConfigurationRequest = {
            "configuration": configuration,
            "workspace_id": workspace_id,
        }
        if grafana_version is not None:
            input_["grafana_version"] = grafana_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
