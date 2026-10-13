from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

import capo_workspaces_web._auth._signers
import capo_workspaces_web._auth._sigv4
from capo_workspaces_web._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.branding_configuration_create_input
    import capo_workspaces_web.types.branding_configuration_update_input
    import capo_workspaces_web.types.client_token
    import capo_workspaces_web.types.cookie_synchronization_configuration
    import capo_workspaces_web.types.create_user_settings_request
    import capo_workspaces_web.types.create_user_settings_response
    import capo_workspaces_web.types.delete_user_settings_request
    import capo_workspaces_web.types.delete_user_settings_response
    import capo_workspaces_web.types.disconnect_timeout_in_minutes
    import capo_workspaces_web.types.enabled_type
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.get_user_settings_request
    import capo_workspaces_web.types.get_user_settings_response
    import capo_workspaces_web.types.idle_disconnect_timeout_in_minutes
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.list_user_settings_request
    import capo_workspaces_web.types.list_user_settings_response
    import capo_workspaces_web.types.max_results
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.tag_list
    import capo_workspaces_web.types.toolbar_configuration
    import capo_workspaces_web.types.update_user_settings_request
    import capo_workspaces_web.types.update_user_settings_response
    from capo_workspaces_web._services.async_work_spaces_web import (
        AsyncWorkSpacesWebClient,
        AsyncWorkSpacesWebClientConfig,
    )
    from capo_workspaces_web._services.work_spaces_web import (
        WorkSpacesWebClient,
        WorkSpacesWebClientConfig,
    )


class UserSettingsResource:
    def __init__(self, service: WorkSpacesWebClient) -> None:
        self._service = service

    def create(
        self,
        copy_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        paste_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        download_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        upload_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        print_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"
        ] = None,
        idle_disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        cookie_synchronization_configuration: Optional[
            "capo_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"
        ] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        deep_link_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        toolbar_configuration: Optional[
            "capo_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"
        ] = None,
        branding_configuration_input: Optional[
            "capo_workspaces_web.types.branding_configuration_create_input.BrandingConfigurationCreateInput"
        ] = None,
        web_authn_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
    ) -> "capo_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse":
        """<p>Creates a user settings resource that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices. </p>

        Args:
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            tags: <p>The tags to add to the user settings resource. A tag is a key-value pair.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p>
            customer_managed_key: <p>The customer managed key used to encrypt sensitive information in the user settings.</p>
            additional_encryption_context: <p>The additional encryption context of the user settings.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration input that customizes the appearance of the web portal for end users. This includes a custom logo, favicon, localized strings, color theme, and optionally a wallpaper and terms of service.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings.create_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.create_user_settings_request

            return (
                capo_workspaces_web.types.create_user_settings_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateUserSettings", redact_input=_redact_input),
        )
        input_: capo_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest = {
            "copy_allowed": copy_allowed,
            "paste_allowed": paste_allowed,
            "download_allowed": download_allowed,
            "upload_allowed": upload_allowed,
            "print_allowed": print_allowed,
        }
        if tags is not None:
            input_["tags"] = tags
        if disconnect_timeout_in_minutes is not None:
            input_["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input_["idle_disconnect_timeout_in_minutes"] = (
                idle_disconnect_timeout_in_minutes
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input_["cookie_synchronization_configuration"] = (
                cookie_synchronization_configuration
            )
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if deep_link_allowed is not None:
            input_["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input_["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input_["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input_["web_authn_allowed"] = web_authn_allowed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse":
        """<p>Gets user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings.get_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.get_user_settings_response

            return (
                capo_workspaces_web.types.get_user_settings_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetUserSettings", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest = {
            "user_settings_arn": user_settings_arn
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
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        copy_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        paste_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        download_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        upload_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        print_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"
        ] = None,
        idle_disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        cookie_synchronization_configuration: Optional[
            "capo_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"
        ] = None,
        deep_link_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        toolbar_configuration: Optional[
            "capo_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"
        ] = None,
        branding_configuration_input: Optional[
            "capo_workspaces_web.types.branding_configuration_update_input.BrandingConfigurationUpdateInput"
        ] = None,
        web_authn_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
    ) -> "capo_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse":
        """<p>Updates the user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p> <p>If the allowlist and blocklist are empty, the configuration becomes null.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration that customizes the appearance of the web portal for end users. When updating user settings without an existing branding configuration, all fields (logo, favicon, localized strings, and color theme) are required except for wallpaper and terms of service. When updating user settings with an existing branding configuration, all fields are optional.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings.update_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_user_settings_request

            return (
                capo_workspaces_web.types.update_user_settings_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_user_settings_response

            return capo_workspaces_web.types.update_user_settings_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateUserSettings",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest = {
            "user_settings_arn": user_settings_arn
        }
        if copy_allowed is not None:
            input_["copy_allowed"] = copy_allowed
        if paste_allowed is not None:
            input_["paste_allowed"] = paste_allowed
        if download_allowed is not None:
            input_["download_allowed"] = download_allowed
        if upload_allowed is not None:
            input_["upload_allowed"] = upload_allowed
        if print_allowed is not None:
            input_["print_allowed"] = print_allowed
        if disconnect_timeout_in_minutes is not None:
            input_["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input_["idle_disconnect_timeout_in_minutes"] = (
                idle_disconnect_timeout_in_minutes
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input_["cookie_synchronization_configuration"] = (
                cookie_synchronization_configuration
            )
        if deep_link_allowed is not None:
            input_["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input_["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input_["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input_["web_authn_allowed"] = web_authn_allowed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse":
        """<p>Deletes user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings.delete_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteUserSettings")
        )
        input_: capo_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest = {
            "user_settings_arn": user_settings_arn
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
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse"
    ):
        """<p>Retrieves a list of user settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation. </p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings.list_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.list_user_settings_response

            return (
                capo_workspaces_web.types.list_user_settings_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListUserSettings", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest = {}
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


class AsyncUserSettingsResource:
    def __init__(self, service: AsyncWorkSpacesWebClient) -> None:
        self._service = service

    async def create(
        self,
        copy_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        paste_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        download_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        upload_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        print_allowed: "capo_workspaces_web.types.enabled_type.EnabledType",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"
        ] = None,
        idle_disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        cookie_synchronization_configuration: Optional[
            "capo_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"
        ] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        deep_link_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        toolbar_configuration: Optional[
            "capo_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"
        ] = None,
        branding_configuration_input: Optional[
            "capo_workspaces_web.types.branding_configuration_create_input.BrandingConfigurationCreateInput"
        ] = None,
        web_authn_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
    ) -> "capo_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse":
        """<p>Creates a user settings resource that can be associated with a web portal. Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices. </p>

        Args:
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            tags: <p>The tags to add to the user settings resource. A tag is a key-value pair.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p>
            customer_managed_key: <p>The customer managed key used to encrypt sensitive information in the user settings.</p>
            additional_encryption_context: <p>The additional encryption context of the user settings.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration input that customizes the appearance of the web portal for end users. This includes a custom logo, favicon, localized strings, color theme, and optionally a wallpaper and terms of service.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.create_user_settings_response.CreateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.create_user_settings.async_create_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.create_user_settings_request

            return (
                capo_workspaces_web.types.create_user_settings_request.redact_sensitive(
                    input_
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateUserSettings", redact_input=_redact_input),
        )
        input_: capo_workspaces_web.types.create_user_settings_request.CreateUserSettingsRequest = {
            "copy_allowed": copy_allowed,
            "paste_allowed": paste_allowed,
            "download_allowed": download_allowed,
            "upload_allowed": upload_allowed,
            "print_allowed": print_allowed,
        }
        if tags is not None:
            input_["tags"] = tags
        if disconnect_timeout_in_minutes is not None:
            input_["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input_["idle_disconnect_timeout_in_minutes"] = (
                idle_disconnect_timeout_in_minutes
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input_["cookie_synchronization_configuration"] = (
                cookie_synchronization_configuration
            )
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if deep_link_allowed is not None:
            input_["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input_["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input_["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input_["web_authn_allowed"] = web_authn_allowed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse":
        """<p>Gets user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.get_user_settings.async_get_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.get_user_settings_response.GetUserSettingsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.get_user_settings_response

            return (
                capo_workspaces_web.types.get_user_settings_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetUserSettings", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.get_user_settings_request.GetUserSettingsRequest = {
            "user_settings_arn": user_settings_arn
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
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
        copy_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        paste_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        download_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        upload_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        print_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"
        ] = None,
        idle_disconnect_timeout_in_minutes: Optional[
            "capo_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        cookie_synchronization_configuration: Optional[
            "capo_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"
        ] = None,
        deep_link_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
        toolbar_configuration: Optional[
            "capo_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"
        ] = None,
        branding_configuration_input: Optional[
            "capo_workspaces_web.types.branding_configuration_update_input.BrandingConfigurationUpdateInput"
        ] = None,
        web_authn_allowed: Optional[
            "capo_workspaces_web.types.enabled_type.EnabledType"
        ] = None,
    ) -> "capo_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse":
        """<p>Updates the user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>
            copy_allowed: <p>Specifies whether the user can copy text from the streaming session to the local device.</p>
            paste_allowed: <p>Specifies whether the user can paste text from the local device to the streaming session.</p>
            download_allowed: <p>Specifies whether the user can download files from the streaming session to the local device.</p>
            upload_allowed: <p>Specifies whether the user can upload files from the local device to the streaming session.</p>
            print_allowed: <p>Specifies whether the user can print to the local device.</p>
            disconnect_timeout_in_minutes: <p>The amount of time that a streaming session remains active after users disconnect.</p>
            idle_disconnect_timeout_in_minutes: <p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            cookie_synchronization_configuration: <p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p> <p>If the allowlist and blocklist are empty, the configuration becomes null.</p>
            deep_link_allowed: <p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>
            toolbar_configuration: <p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>
            branding_configuration_input: <p>The branding configuration that customizes the appearance of the web portal for end users. When updating user settings without an existing branding configuration, all fields (logo, favicon, localized strings, and color theme) are required except for wallpaper and terms of service. When updating user settings with an existing branding configuration, all fields are optional.</p>
            web_authn_allowed: <p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.update_user_settings.async_update_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_user_settings_request

            return (
                capo_workspaces_web.types.update_user_settings_request.redact_sensitive(
                    input_
                )
            )

        def _redact_output(
            output: "capo_workspaces_web.types.update_user_settings_response.UpdateUserSettingsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_user_settings_response

            return capo_workspaces_web.types.update_user_settings_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdateUserSettings",
                redact_input=_redact_input,
                redact_output=_redact_output,
            ),
        )
        input_: capo_workspaces_web.types.update_user_settings_request.UpdateUserSettingsRequest = {
            "user_settings_arn": user_settings_arn
        }
        if copy_allowed is not None:
            input_["copy_allowed"] = copy_allowed
        if paste_allowed is not None:
            input_["paste_allowed"] = paste_allowed
        if download_allowed is not None:
            input_["download_allowed"] = download_allowed
        if upload_allowed is not None:
            input_["upload_allowed"] = upload_allowed
        if print_allowed is not None:
            input_["print_allowed"] = print_allowed
        if disconnect_timeout_in_minutes is not None:
            input_["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            input_["idle_disconnect_timeout_in_minutes"] = (
                idle_disconnect_timeout_in_minutes
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cookie_synchronization_configuration is not None:
            input_["cookie_synchronization_configuration"] = (
                cookie_synchronization_configuration
            )
        if deep_link_allowed is not None:
            input_["deep_link_allowed"] = deep_link_allowed
        if toolbar_configuration is not None:
            input_["toolbar_configuration"] = toolbar_configuration
        if branding_configuration_input is not None:
            input_["branding_configuration_input"] = branding_configuration_input
        if web_authn_allowed is not None:
            input_["web_authn_allowed"] = web_authn_allowed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse":
        """<p>Deletes user settings.</p>

        Args:
            user_settings_arn: <p>The ARN of the user settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.delete_user_settings_response.DeleteUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_settings.async_delete_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteUserSettings")
        )
        input_: capo_workspaces_web.types.delete_user_settings_request.DeleteUserSettingsRequest = {
            "user_settings_arn": user_settings_arn
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
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse"
    ):
        """<p>Retrieves a list of user settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation. </p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.list_user_settings.async_list_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.list_user_settings_response

            return (
                capo_workspaces_web.types.list_user_settings_response.redact_sensitive(
                    output
                )
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListUserSettings", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.list_user_settings_request.ListUserSettingsRequest = {}
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
