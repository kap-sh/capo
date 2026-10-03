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
    import capo_grafana.types.associate_license_request
    import capo_grafana.types.associate_license_response
    import capo_grafana.types.disassociate_license_request
    import capo_grafana.types.disassociate_license_response
    import capo_grafana.types.grafana_token
    import capo_grafana.types.license_type
    import capo_grafana.types.workspace_id
    from capo_grafana._services.async_grafana import (
        AsyncgrafanaClient,
        AsyncgrafanaClientConfig,
    )
    from capo_grafana._services.grafana import grafanaClient, grafanaClientConfig


class License:
    def __init__(self, service: grafanaClient) -> None:
        self._service = service

    def associate_license(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        license_type: "capo_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
        grafana_token: Optional["capo_grafana.types.grafana_token.GrafanaToken"] = None,
    ) -> "capo_grafana.types.associate_license_response.AssociateLicenseResponse":
        """<p>Assigns a Grafana Enterprise license to a workspace. To upgrade, you must use <code>ENTERPRISE</code> for the <code>licenseType</code>, and pass in a valid Grafana Labs token for the <code>grafanaToken</code>. Upgrading to Grafana Enterprise incurs additional fees. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html">Upgrade a workspace to Grafana Enterprise</a>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to associate the license with.</p>
            license_type: <p>The type of license to associate with the workspace.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>
            grafana_token: <p>A token from Grafana Labs that ties your Amazon Web Services account with a Grafana Labs account. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise">Link your account with Grafana Labs</a>.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.associate_license_request.AssociateLicenseRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.associate_license_response.AssociateLicenseResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.associate_license

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.associate_license.associate_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.associate_license_request.AssociateLicenseRequest = {
            "workspace_id": workspace_id,
            "license_type": license_type,
        }
        if grafana_token is not None:
            input_["grafana_token"] = grafana_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_license(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        license_type: "capo_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[grafanaClientConfig] = None,
    ) -> "capo_grafana.types.disassociate_license_response.DisassociateLicenseResponse":
        """<p>Removes the Grafana Enterprise license from a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to remove the Grafana Enterprise license from.</p>
            license_type: <p>The type of license to remove from the workspace.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_grafana.types.disassociate_license_request.DisassociateLicenseRequest]",
        ) -> OperationResponse[
            "capo_grafana.types.disassociate_license_response.DisassociateLicenseResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.disassociate_license

            output, http_response = (
                capo_grafana._operations.aws_grafana_control_plane.disassociate_license.disassociate_license(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.disassociate_license_request.DisassociateLicenseRequest = {
            "workspace_id": workspace_id,
            "license_type": license_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncLicense:
    def __init__(self, service: AsyncgrafanaClient) -> None:
        self._service = service

    async def associate_license(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        license_type: "capo_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
        grafana_token: Optional["capo_grafana.types.grafana_token.GrafanaToken"] = None,
    ) -> "capo_grafana.types.associate_license_response.AssociateLicenseResponse":
        """<p>Assigns a Grafana Enterprise license to a workspace. To upgrade, you must use <code>ENTERPRISE</code> for the <code>licenseType</code>, and pass in a valid Grafana Labs token for the <code>grafanaToken</code>. Upgrading to Grafana Enterprise incurs additional fees. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html">Upgrade a workspace to Grafana Enterprise</a>.</p>

        Args:
            workspace_id: <p>The ID of the workspace to associate the license with.</p>
            license_type: <p>The type of license to associate with the workspace.</p> <note> <p>Amazon Managed Grafana workspaces no longer support Grafana Enterprise free trials.</p> </note>
            grafana_token: <p>A token from Grafana Labs that ties your Amazon Web Services account with a Grafana Labs account. For more information, see <a href="https://docs.aws.amazon.com/grafana/latest/userguide/upgrade-to-Grafana-Enterprise.html#AMG-workspace-register-enterprise">Link your account with Grafana Labs</a>.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.associate_license_request.AssociateLicenseRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.associate_license_response.AssociateLicenseResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.associate_license

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.associate_license.async_associate_license(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.associate_license_request.AssociateLicenseRequest = {
            "workspace_id": workspace_id,
            "license_type": license_type,
        }
        if grafana_token is not None:
            input_["grafana_token"] = grafana_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_license(
        self,
        workspace_id: "capo_grafana.types.workspace_id.WorkspaceId",
        license_type: "capo_grafana.types.license_type.LicenseType",
        *,
        config_overrides: Optional[AsyncgrafanaClientConfig] = None,
    ) -> "capo_grafana.types.disassociate_license_response.DisassociateLicenseResponse":
        """<p>Removes the Grafana Enterprise license from a workspace.</p>

        Args:
            workspace_id: <p>The ID of the workspace to remove the Grafana Enterprise license from.</p>
            license_type: <p>The type of license to remove from the workspace.</p>

        Raises:
            capo_grafana.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action. </p>
            capo_grafana.errors.internal_server_exception.InternalServerException: <p>Unexpected error while processing the request. Retry the request.</p>
            capo_grafana.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource that does not exist.</p>
            capo_grafana.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Retry the request.</p>
            capo_grafana.errors.validation_exception.ValidationException: <p>The value of a parameter in the request caused an error.</p>
            capo_grafana.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_grafana.types.disassociate_license_request.DisassociateLicenseRequest]",
        ) -> AsyncOperationResponse[
            "capo_grafana.types.disassociate_license_response.DisassociateLicenseResponse"
        ]:
            import capo_grafana._operations.aws_grafana_control_plane.disassociate_license

            (
                output,
                http_response,
            ) = await capo_grafana._operations.aws_grafana_control_plane.disassociate_license.async_disassociate_license(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_grafana.types.disassociate_license_request.DisassociateLicenseRequest = {
            "workspace_id": workspace_id,
            "license_type": license_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
