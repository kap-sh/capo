from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from capo_proton._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_proton.types.get_account_settings_input
    import capo_proton.types.get_account_settings_output
    import capo_proton.types.repository_branch_input
    import capo_proton.types.role_arn_or_empty_string
    import capo_proton.types.update_account_settings_input
    import capo_proton.types.update_account_settings_output
    from capo_proton._services.async_proton import (
        AsyncProtonClient,
        AsyncProtonClientConfig,
    )
    from capo_proton._services.proton import ProtonClient, ProtonClientConfig


class AccountSettingsResource:
    def __init__(self, service: ProtonClient) -> None:
        self._service = service

    def read(
        self, *, config_overrides: Optional[ProtonClientConfig] = None
    ) -> "capo_proton.types.get_account_settings_output.GetAccountSettingsOutput":
        """<p>Get detail data for Proton account-wide settings.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.get_account_settings_input.GetAccountSettingsInput]",
        ) -> OperationResponse[
            "capo_proton.types.get_account_settings_output.GetAccountSettingsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_account_settings

            output, http_response = (
                capo_proton._operations.aws_proton20200720.get_account_settings.get_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccountSettings")
        )
        input_: capo_proton.types.get_account_settings_input.GetAccountSettingsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        *,
        config_overrides: Optional[ProtonClientConfig] = None,
        pipeline_service_role_arn: Optional[
            "capo_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
        ] = None,
        pipeline_provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        delete_pipeline_provisioning_repository: Optional[bool] = None,
        pipeline_codebuild_role_arn: Optional[
            "capo_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
        ] = None,
    ) -> "capo_proton.types.update_account_settings_output.UpdateAccountSettingsOutput":
        """<p>Update Proton settings that are used for multiple services in the Amazon Web Services account.</p>

        Args:
            pipeline_service_role_arn: <p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by Proton for Amazon Web Services-managed provisioning, and by customer-owned automation for self-managed provisioning.</p> <p>To remove a previously configured ARN, specify an empty string.</p>
            pipeline_provisioning_repository: <p>A linked repository for pipeline provisioning. Specify it if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To remove a previously configured repository, set <code>deletePipelineProvisioningRepository</code> to <code>true</code>, and don't set <code>pipelineProvisioningRepository</code>.</p>
            delete_pipeline_provisioning_repository: <p>Set to <code>true</code> to remove a configured pipeline repository from the account settings. Don't set this field if you are updating the configured pipeline repository.</p>
            pipeline_codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Proton assumes this role for CodeBuild-based provisioning.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_proton.types.update_account_settings_input.UpdateAccountSettingsInput]",
        ) -> OperationResponse[
            "capo_proton.types.update_account_settings_output.UpdateAccountSettingsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_account_settings

            output, http_response = (
                capo_proton._operations.aws_proton20200720.update_account_settings.update_account_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccountSettings")
        )
        input_: capo_proton.types.update_account_settings_input.UpdateAccountSettingsInput = {}
        if pipeline_service_role_arn is not None:
            input_["pipeline_service_role_arn"] = pipeline_service_role_arn
        if pipeline_provisioning_repository is not None:
            input_["pipeline_provisioning_repository"] = (
                pipeline_provisioning_repository
            )
        if delete_pipeline_provisioning_repository is not None:
            input_["delete_pipeline_provisioning_repository"] = (
                delete_pipeline_provisioning_repository
            )
        if pipeline_codebuild_role_arn is not None:
            input_["pipeline_codebuild_role_arn"] = pipeline_codebuild_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncAccountSettingsResource:
    def __init__(self, service: AsyncProtonClient) -> None:
        self._service = service

    async def read(
        self, *, config_overrides: Optional[AsyncProtonClientConfig] = None
    ) -> "capo_proton.types.get_account_settings_output.GetAccountSettingsOutput":
        """<p>Get detail data for Proton account-wide settings.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource <i>wasn't</i> found.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.get_account_settings_input.GetAccountSettingsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.get_account_settings_output.GetAccountSettingsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.get_account_settings

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.get_account_settings.async_get_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetAccountSettings")
        )
        input_: capo_proton.types.get_account_settings_input.GetAccountSettingsInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        *,
        config_overrides: Optional[AsyncProtonClientConfig] = None,
        pipeline_service_role_arn: Optional[
            "capo_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
        ] = None,
        pipeline_provisioning_repository: Optional[
            "capo_proton.types.repository_branch_input.RepositoryBranchInput"
        ] = None,
        delete_pipeline_provisioning_repository: Optional[bool] = None,
        pipeline_codebuild_role_arn: Optional[
            "capo_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
        ] = None,
    ) -> "capo_proton.types.update_account_settings_output.UpdateAccountSettingsOutput":
        """<p>Update Proton settings that are used for multiple services in the Amazon Web Services account.</p>

        Args:
            pipeline_service_role_arn: <p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by Proton for Amazon Web Services-managed provisioning, and by customer-owned automation for self-managed provisioning.</p> <p>To remove a previously configured ARN, specify an empty string.</p>
            pipeline_provisioning_repository: <p>A linked repository for pipeline provisioning. Specify it if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To remove a previously configured repository, set <code>deletePipelineProvisioningRepository</code> to <code>true</code>, and don't set <code>pipelineProvisioningRepository</code>.</p>
            delete_pipeline_provisioning_repository: <p>Set to <code>true</code> to remove a configured pipeline repository from the account settings. Don't set this field if you are updating the configured pipeline repository.</p>
            pipeline_codebuild_role_arn: <p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Proton assumes this role for CodeBuild-based provisioning.</p>

        Raises:
            capo_proton.errors.access_denied_exception.AccessDeniedException: <p>There <i>isn't</i> sufficient access for performing this action.</p>
            capo_proton.errors.conflict_exception.ConflictException: <p>The request <i>couldn't</i> be made due to a conflicting operation or resource.</p>
            capo_proton.errors.internal_server_exception.InternalServerException: <p>The request failed to register with the service.</p>
            capo_proton.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_proton.errors.validation_exception.ValidationException: <p>The input is invalid or an out-of-range value was supplied for the input parameter.</p>
            capo_proton.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_proton.types.update_account_settings_input.UpdateAccountSettingsInput]",
        ) -> AsyncOperationResponse[
            "capo_proton.types.update_account_settings_output.UpdateAccountSettingsOutput"
        ]:
            import capo_proton._operations.aws_proton20200720.update_account_settings

            (
                output,
                http_response,
            ) = await capo_proton._operations.aws_proton20200720.update_account_settings.async_update_account_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("UpdateAccountSettings")
        )
        input_: capo_proton.types.update_account_settings_input.UpdateAccountSettingsInput = {}
        if pipeline_service_role_arn is not None:
            input_["pipeline_service_role_arn"] = pipeline_service_role_arn
        if pipeline_provisioning_repository is not None:
            input_["pipeline_provisioning_repository"] = (
                pipeline_provisioning_repository
            )
        if delete_pipeline_provisioning_repository is not None:
            input_["delete_pipeline_provisioning_repository"] = (
                delete_pipeline_provisioning_repository
            )
        if pipeline_codebuild_role_arn is not None:
            input_["pipeline_codebuild_role_arn"] = pipeline_codebuild_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
