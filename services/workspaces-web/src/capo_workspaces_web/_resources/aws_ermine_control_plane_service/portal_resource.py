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
    import capo_workspaces_web.types.associate_browser_settings_request
    import capo_workspaces_web.types.associate_browser_settings_response
    import capo_workspaces_web.types.associate_data_protection_settings_request
    import capo_workspaces_web.types.associate_data_protection_settings_response
    import capo_workspaces_web.types.associate_ip_access_settings_request
    import capo_workspaces_web.types.associate_ip_access_settings_response
    import capo_workspaces_web.types.associate_network_settings_request
    import capo_workspaces_web.types.associate_network_settings_response
    import capo_workspaces_web.types.associate_session_logger_request
    import capo_workspaces_web.types.associate_session_logger_response
    import capo_workspaces_web.types.associate_trust_store_request
    import capo_workspaces_web.types.associate_trust_store_response
    import capo_workspaces_web.types.associate_user_access_logging_settings_request
    import capo_workspaces_web.types.associate_user_access_logging_settings_response
    import capo_workspaces_web.types.associate_user_settings_request
    import capo_workspaces_web.types.associate_user_settings_response
    import capo_workspaces_web.types.authentication_type
    import capo_workspaces_web.types.client_token
    import capo_workspaces_web.types.create_portal_request
    import capo_workspaces_web.types.create_portal_response
    import capo_workspaces_web.types.delete_portal_request
    import capo_workspaces_web.types.delete_portal_response
    import capo_workspaces_web.types.disassociate_browser_settings_request
    import capo_workspaces_web.types.disassociate_browser_settings_response
    import capo_workspaces_web.types.disassociate_data_protection_settings_request
    import capo_workspaces_web.types.disassociate_data_protection_settings_response
    import capo_workspaces_web.types.disassociate_ip_access_settings_request
    import capo_workspaces_web.types.disassociate_ip_access_settings_response
    import capo_workspaces_web.types.disassociate_network_settings_request
    import capo_workspaces_web.types.disassociate_network_settings_response
    import capo_workspaces_web.types.disassociate_session_logger_request
    import capo_workspaces_web.types.disassociate_session_logger_response
    import capo_workspaces_web.types.disassociate_trust_store_request
    import capo_workspaces_web.types.disassociate_trust_store_response
    import capo_workspaces_web.types.disassociate_user_access_logging_settings_request
    import capo_workspaces_web.types.disassociate_user_access_logging_settings_response
    import capo_workspaces_web.types.disassociate_user_settings_request
    import capo_workspaces_web.types.disassociate_user_settings_response
    import capo_workspaces_web.types.display_name
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.get_portal_request
    import capo_workspaces_web.types.get_portal_response
    import capo_workspaces_web.types.get_portal_service_provider_metadata_request
    import capo_workspaces_web.types.get_portal_service_provider_metadata_response
    import capo_workspaces_web.types.instance_type
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.list_portals_request
    import capo_workspaces_web.types.list_portals_response
    import capo_workspaces_web.types.max_concurrent_sessions
    import capo_workspaces_web.types.max_results
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.portal_custom_domain
    import capo_workspaces_web.types.tag_list
    import capo_workspaces_web.types.update_portal_request
    import capo_workspaces_web.types.update_portal_response
    from capo_workspaces_web._services.async_work_spaces_web import (
        AsyncWorkSpacesWebClient,
        AsyncWorkSpacesWebClientConfig,
    )
    from capo_workspaces_web._services.work_spaces_web import (
        WorkSpacesWebClient,
        WorkSpacesWebClientConfig,
    )


class PortalResource:
    def __init__(self, service: WorkSpacesWebClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name.DisplayName"
        ] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        authentication_type: Optional[
            "capo_workspaces_web.types.authentication_type.AuthenticationType"
        ] = None,
        instance_type: Optional[
            "capo_workspaces_web.types.instance_type.InstanceType"
        ] = None,
        max_concurrent_sessions: Optional[
            "capo_workspaces_web.types.max_concurrent_sessions.MaxConcurrentSessions"
        ] = None,
        portal_custom_domain: Optional[
            "capo_workspaces_web.types.portal_custom_domain.PortalCustomDomain"
        ] = None,
    ) -> "capo_workspaces_web.types.create_portal_response.CreatePortalResponse":
        """<p>Creates a web portal.</p>

        Args:
            display_name: <p>The name of the web portal. This is not visible to users who log into the web portal.</p>
            tags: <p>The tags to add to the web portal. A tag is a key-value pair.</p>
            customer_managed_key: <p>The customer managed key of the web portal.</p>
            additional_encryption_context: <p>The additional encryption context of the portal.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            authentication_type: <p>The type of authentication integration points used when signing into the web portal. Defaults to <code>Standard</code>.</p> <p> <code>Standard</code> web portals are authenticated directly through your identity provider. You need to call <code>CreateIdentityProvider</code> to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.</p> <p> <code>IAM Identity Center</code> web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.</p>
            instance_type: <p>The type and resources of the underlying instance.</p>
            max_concurrent_sessions: <p>The maximum number of concurrent sessions for the portal.</p>
            portal_custom_domain: <p>The custom domain of the web portal that users access in order to start streaming sessions.</p>

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
            req: "OperationRequest[capo_workspaces_web.types.create_portal_request.CreatePortalRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_portal_response.CreatePortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_portal

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_portal.create_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.create_portal_request.CreatePortalRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.create_portal_request

            return capo_workspaces_web.types.create_portal_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePortal", redact_input=_redact_input),
        )
        input_: capo_workspaces_web.types.create_portal_request.CreatePortalRequest = {}
        if display_name is not None:
            input_["display_name"] = display_name
        if tags is not None:
            input_["tags"] = tags
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if max_concurrent_sessions is not None:
            input_["max_concurrent_sessions"] = max_concurrent_sessions
        if portal_custom_domain is not None:
            input_["portal_custom_domain"] = portal_custom_domain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_portal_response.GetPortalResponse":
        """<p>Gets the web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_portal_request.GetPortalRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_portal_response.GetPortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal.get_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.get_portal_response.GetPortalResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.get_portal_response

            return capo_workspaces_web.types.get_portal_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPortal", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.get_portal_request.GetPortalRequest = {
            "portal_arn": portal_arn
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
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name.DisplayName"
        ] = None,
        authentication_type: Optional[
            "capo_workspaces_web.types.authentication_type.AuthenticationType"
        ] = None,
        instance_type: Optional[
            "capo_workspaces_web.types.instance_type.InstanceType"
        ] = None,
        max_concurrent_sessions: Optional[
            "capo_workspaces_web.types.max_concurrent_sessions.MaxConcurrentSessions"
        ] = None,
        portal_custom_domain: Optional[
            "capo_workspaces_web.types.portal_custom_domain.PortalCustomDomain"
        ] = None,
    ) -> "capo_workspaces_web.types.update_portal_response.UpdatePortalResponse":
        """<p>Updates a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            display_name: <p>The name of the web portal. This is not visible to users who log into the web portal.</p>
            authentication_type: <p>The type of authentication integration points used when signing into the web portal. Defaults to <code>Standard</code>.</p> <p> <code>Standard</code> web portals are authenticated directly through your identity provider. You need to call <code>CreateIdentityProvider</code> to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.</p> <p> <code>IAM Identity Center</code> web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.</p>
            instance_type: <p>The type and resources of the underlying instance.</p>
            max_concurrent_sessions: <p>The maximum number of concurrent sessions for the portal.</p>
            portal_custom_domain: <p>The custom domain of the web portal that users access in order to start streaming sessions. </p>

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
            req: "OperationRequest[capo_workspaces_web.types.update_portal_request.UpdatePortalRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_portal_response.UpdatePortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_portal

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_portal.update_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.update_portal_request.UpdatePortalRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_portal_request

            return capo_workspaces_web.types.update_portal_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_workspaces_web.types.update_portal_response.UpdatePortalResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_portal_response

            return capo_workspaces_web.types.update_portal_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePortal", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_workspaces_web.types.update_portal_request.UpdatePortalRequest = {
            "portal_arn": portal_arn
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if max_concurrent_sessions is not None:
            input_["max_concurrent_sessions"] = max_concurrent_sessions
        if portal_custom_domain is not None:
            input_["portal_custom_domain"] = portal_custom_domain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_portal_response.DeletePortalResponse":
        """<p>Deletes a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_portal_request.DeletePortalRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_portal_response.DeletePortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_portal

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_portal.delete_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePortal")
        )
        input_: capo_workspaces_web.types.delete_portal_request.DeletePortalRequest = {
            "portal_arn": portal_arn
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
    ) -> "capo_workspaces_web.types.list_portals_response.ListPortalsResponse":
        """<p>Retrieves a list or web portals.</p>

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
            req: "OperationRequest[capo_workspaces_web.types.list_portals_request.ListPortalsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_portals_response.ListPortalsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_portals

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_portals.list_portals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.list_portals_response.ListPortalsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.list_portals_response

            return capo_workspaces_web.types.list_portals_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPortals", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.list_portals_request.ListPortalsRequest = {}
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

    def associate_browser_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        browser_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_browser_settings_response.AssociateBrowserSettingsResponse":
        """<p>Associates a browser settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            browser_settings_arn: <p>The ARN of the browser settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_browser_settings_request.AssociateBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_browser_settings_response.AssociateBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_browser_settings.associate_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateBrowserSettings")
        )
        input_: capo_workspaces_web.types.associate_browser_settings_request.AssociateBrowserSettingsRequest = {
            "portal_arn": portal_arn,
            "browser_settings_arn": browser_settings_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_data_protection_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_data_protection_settings_response.AssociateDataProtectionSettingsResponse":
        """<p>Associates a data protection settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            data_protection_settings_arn: <p>The ARN of the data protection settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_data_protection_settings_request.AssociateDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_data_protection_settings_response.AssociateDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_data_protection_settings.associate_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateDataProtectionSettings")
        )
        input_: capo_workspaces_web.types.associate_data_protection_settings_request.AssociateDataProtectionSettingsRequest = {
            "portal_arn": portal_arn,
            "data_protection_settings_arn": data_protection_settings_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_ip_access_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_ip_access_settings_response.AssociateIpAccessSettingsResponse":
        """<p>Associates an IP access settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            ip_access_settings_arn: <p>The ARN of the IP access settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_ip_access_settings_request.AssociateIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_ip_access_settings_response.AssociateIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_ip_access_settings.associate_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateIpAccessSettings")
        )
        input_: capo_workspaces_web.types.associate_ip_access_settings_request.AssociateIpAccessSettingsRequest = {
            "portal_arn": portal_arn,
            "ip_access_settings_arn": ip_access_settings_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_network_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        network_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_network_settings_response.AssociateNetworkSettingsResponse":
        """<p>Associates a network settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            network_settings_arn: <p>The ARN of the network settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_network_settings_request.AssociateNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_network_settings_response.AssociateNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_network_settings.associate_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateNetworkSettings")
        )
        input_: capo_workspaces_web.types.associate_network_settings_request.AssociateNetworkSettingsRequest = {
            "portal_arn": portal_arn,
            "network_settings_arn": network_settings_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_session_logger(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        session_logger_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_session_logger_response.AssociateSessionLoggerResponse":
        """<p>Associates a session logger with a portal.</p>

        Args:
            portal_arn: <p>The ARN of the portal to associate to the session logger ARN.</p>
            session_logger_arn: <p>The ARN of the session logger to associate to the portal ARN.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate Session Logger with Portal
            Associates a session logger with a portal

            >>> client.associate_session_logger(portal_arn='arn:aws:workspaces-web:us-west-2:123456789012:portal/12345678-1234-1234-1234-123456789012', session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/11111111-1111-1111-1111-111111111111')
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_session_logger_request.AssociateSessionLoggerRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_session_logger_response.AssociateSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_session_logger

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_session_logger.associate_session_logger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateSessionLogger")
        )
        input_: capo_workspaces_web.types.associate_session_logger_request.AssociateSessionLoggerRequest = {
            "portal_arn": portal_arn,
            "session_logger_arn": session_logger_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_trust_store(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_trust_store_response.AssociateTrustStoreResponse":
        """<p>Associates a trust store with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            trust_store_arn: <p>The ARN of the trust store.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_trust_store_request.AssociateTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_trust_store_response.AssociateTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_trust_store

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_trust_store.associate_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateTrustStore")
        )
        input_: capo_workspaces_web.types.associate_trust_store_request.AssociateTrustStoreRequest = {
            "portal_arn": portal_arn,
            "trust_store_arn": trust_store_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_user_access_logging_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_user_access_logging_settings_response.AssociateUserAccessLoggingSettingsResponse":
        """<p>Associates a user access logging settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            user_access_logging_settings_arn: <p>The ARN of the user access logging settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_user_access_logging_settings_request.AssociateUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_user_access_logging_settings_response.AssociateUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_access_logging_settings.associate_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateUserAccessLoggingSettings")
        )
        input_: capo_workspaces_web.types.associate_user_access_logging_settings_request.AssociateUserAccessLoggingSettingsRequest = {
            "portal_arn": portal_arn,
            "user_access_logging_settings_arn": user_access_logging_settings_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_user_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_user_settings_response.AssociateUserSettingsResponse":
        """<p>Associates a user settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            user_settings_arn: <p>The ARN of the user settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.associate_user_settings_request.AssociateUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.associate_user_settings_response.AssociateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_settings.associate_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateUserSettings")
        )
        input_: capo_workspaces_web.types.associate_user_settings_request.AssociateUserSettingsRequest = {
            "portal_arn": portal_arn,
            "user_settings_arn": user_settings_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_browser_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_browser_settings_response.DisassociateBrowserSettingsResponse":
        """<p>Disassociates browser settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_browser_settings_request.DisassociateBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_browser_settings_response.DisassociateBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_browser_settings.disassociate_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateBrowserSettings")
        )
        input_: capo_workspaces_web.types.disassociate_browser_settings_request.DisassociateBrowserSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_data_protection_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_data_protection_settings_response.DisassociateDataProtectionSettingsResponse":
        """<p>Disassociates data protection settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_data_protection_settings_request.DisassociateDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_data_protection_settings_response.DisassociateDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_data_protection_settings.disassociate_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateDataProtectionSettings")
        )
        input_: capo_workspaces_web.types.disassociate_data_protection_settings_request.DisassociateDataProtectionSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_ip_access_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_ip_access_settings_response.DisassociateIpAccessSettingsResponse":
        """<p>Disassociates IP access settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_ip_access_settings_request.DisassociateIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_ip_access_settings_response.DisassociateIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_ip_access_settings.disassociate_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateIpAccessSettings")
        )
        input_: capo_workspaces_web.types.disassociate_ip_access_settings_request.DisassociateIpAccessSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_network_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_network_settings_response.DisassociateNetworkSettingsResponse":
        """<p>Disassociates network settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_network_settings_request.DisassociateNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_network_settings_response.DisassociateNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_network_settings.disassociate_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateNetworkSettings")
        )
        input_: capo_workspaces_web.types.disassociate_network_settings_request.DisassociateNetworkSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_session_logger(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_session_logger_response.DisassociateSessionLoggerResponse":
        """<p>Disassociates a session logger from a portal.</p>

        Args:
            portal_arn: <p>The ARN of the portal to disassociate from the a session logger.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Disassociate Session Logger from Portal
            Removes the association between a session logger and a portal

            >>> client.disassociate_session_logger(portal_arn='arn:aws:workspaces-web:us-west-2:123456789012:portal/12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_session_logger_request.DisassociateSessionLoggerRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_session_logger_response.DisassociateSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_session_logger

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_session_logger.disassociate_session_logger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateSessionLogger")
        )
        input_: capo_workspaces_web.types.disassociate_session_logger_request.DisassociateSessionLoggerRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_trust_store(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse":
        """<p>Disassociates a trust store from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_trust_store

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_trust_store.disassociate_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateTrustStore")
        )
        input_: capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_user_access_logging_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_user_access_logging_settings_response.DisassociateUserAccessLoggingSettingsResponse":
        """<p>Disassociates user access logging settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_user_access_logging_settings_request.DisassociateUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_user_access_logging_settings_response.DisassociateUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_access_logging_settings.disassociate_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateUserAccessLoggingSettings")
        )
        input_: capo_workspaces_web.types.disassociate_user_access_logging_settings_request.DisassociateUserAccessLoggingSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_user_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_user_settings_response.DisassociateUserSettingsResponse":
        """<p>Disassociates user settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.disassociate_user_settings_request.DisassociateUserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.disassociate_user_settings_response.DisassociateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_settings.disassociate_user_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateUserSettings")
        )
        input_: capo_workspaces_web.types.disassociate_user_settings_request.DisassociateUserSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_portal_service_provider_metadata(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_portal_service_provider_metadata_response.GetPortalServiceProviderMetadataResponse":
        """<p>Gets the service provider metadata.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_portal_service_provider_metadata_request.GetPortalServiceProviderMetadataRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_portal_service_provider_metadata_response.GetPortalServiceProviderMetadataResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal_service_provider_metadata

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal_service_provider_metadata.get_portal_service_provider_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPortalServiceProviderMetadata")
        )
        input_: capo_workspaces_web.types.get_portal_service_provider_metadata_request.GetPortalServiceProviderMetadataRequest = {
            "portal_arn": portal_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPortalResource:
    def __init__(self, service: AsyncWorkSpacesWebClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name.DisplayName"
        ] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        authentication_type: Optional[
            "capo_workspaces_web.types.authentication_type.AuthenticationType"
        ] = None,
        instance_type: Optional[
            "capo_workspaces_web.types.instance_type.InstanceType"
        ] = None,
        max_concurrent_sessions: Optional[
            "capo_workspaces_web.types.max_concurrent_sessions.MaxConcurrentSessions"
        ] = None,
        portal_custom_domain: Optional[
            "capo_workspaces_web.types.portal_custom_domain.PortalCustomDomain"
        ] = None,
    ) -> "capo_workspaces_web.types.create_portal_response.CreatePortalResponse":
        """<p>Creates a web portal.</p>

        Args:
            display_name: <p>The name of the web portal. This is not visible to users who log into the web portal.</p>
            tags: <p>The tags to add to the web portal. A tag is a key-value pair.</p>
            customer_managed_key: <p>The customer managed key of the web portal.</p>
            additional_encryption_context: <p>The additional encryption context of the portal.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            authentication_type: <p>The type of authentication integration points used when signing into the web portal. Defaults to <code>Standard</code>.</p> <p> <code>Standard</code> web portals are authenticated directly through your identity provider. You need to call <code>CreateIdentityProvider</code> to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.</p> <p> <code>IAM Identity Center</code> web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.</p>
            instance_type: <p>The type and resources of the underlying instance.</p>
            max_concurrent_sessions: <p>The maximum number of concurrent sessions for the portal.</p>
            portal_custom_domain: <p>The custom domain of the web portal that users access in order to start streaming sessions.</p>

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
            req: "AsyncOperationRequest[capo_workspaces_web.types.create_portal_request.CreatePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.create_portal_response.CreatePortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_portal

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.create_portal.async_create_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.create_portal_request.CreatePortalRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.create_portal_request

            return capo_workspaces_web.types.create_portal_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreatePortal", redact_input=_redact_input),
        )
        input_: capo_workspaces_web.types.create_portal_request.CreatePortalRequest = {}
        if display_name is not None:
            input_["display_name"] = display_name
        if tags is not None:
            input_["tags"] = tags
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if max_concurrent_sessions is not None:
            input_["max_concurrent_sessions"] = max_concurrent_sessions
        if portal_custom_domain is not None:
            input_["portal_custom_domain"] = portal_custom_domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_portal_response.GetPortalResponse":
        """<p>Gets the web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.get_portal_request.GetPortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.get_portal_response.GetPortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal.async_get_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.get_portal_response.GetPortalResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.get_portal_response

            return capo_workspaces_web.types.get_portal_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetPortal", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.get_portal_request.GetPortalRequest = {
            "portal_arn": portal_arn
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
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name.DisplayName"
        ] = None,
        authentication_type: Optional[
            "capo_workspaces_web.types.authentication_type.AuthenticationType"
        ] = None,
        instance_type: Optional[
            "capo_workspaces_web.types.instance_type.InstanceType"
        ] = None,
        max_concurrent_sessions: Optional[
            "capo_workspaces_web.types.max_concurrent_sessions.MaxConcurrentSessions"
        ] = None,
        portal_custom_domain: Optional[
            "capo_workspaces_web.types.portal_custom_domain.PortalCustomDomain"
        ] = None,
    ) -> "capo_workspaces_web.types.update_portal_response.UpdatePortalResponse":
        """<p>Updates a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            display_name: <p>The name of the web portal. This is not visible to users who log into the web portal.</p>
            authentication_type: <p>The type of authentication integration points used when signing into the web portal. Defaults to <code>Standard</code>.</p> <p> <code>Standard</code> web portals are authenticated directly through your identity provider. You need to call <code>CreateIdentityProvider</code> to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.</p> <p> <code>IAM Identity Center</code> web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.</p>
            instance_type: <p>The type and resources of the underlying instance.</p>
            max_concurrent_sessions: <p>The maximum number of concurrent sessions for the portal.</p>
            portal_custom_domain: <p>The custom domain of the web portal that users access in order to start streaming sessions. </p>

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
            req: "AsyncOperationRequest[capo_workspaces_web.types.update_portal_request.UpdatePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.update_portal_response.UpdatePortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_portal

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.update_portal.async_update_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_workspaces_web.types.update_portal_request.UpdatePortalRequest",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_portal_request

            return capo_workspaces_web.types.update_portal_request.redact_sensitive(
                input_
            )

        def _redact_output(
            output: "capo_workspaces_web.types.update_portal_response.UpdatePortalResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.update_portal_response

            return capo_workspaces_web.types.update_portal_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging(
                "UpdatePortal", redact_input=_redact_input, redact_output=_redact_output
            ),
        )
        input_: capo_workspaces_web.types.update_portal_request.UpdatePortalRequest = {
            "portal_arn": portal_arn
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if authentication_type is not None:
            input_["authentication_type"] = authentication_type
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if max_concurrent_sessions is not None:
            input_["max_concurrent_sessions"] = max_concurrent_sessions
        if portal_custom_domain is not None:
            input_["portal_custom_domain"] = portal_custom_domain

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_portal_response.DeletePortalResponse":
        """<p>Deletes a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.delete_portal_request.DeletePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.delete_portal_response.DeletePortalResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_portal

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_portal.async_delete_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeletePortal")
        )
        input_: capo_workspaces_web.types.delete_portal_request.DeletePortalRequest = {
            "portal_arn": portal_arn
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
    ) -> "capo_workspaces_web.types.list_portals_response.ListPortalsResponse":
        """<p>Retrieves a list or web portals.</p>

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
            req: "AsyncOperationRequest[capo_workspaces_web.types.list_portals_request.ListPortalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.list_portals_response.ListPortalsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_portals

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.list_portals.async_list_portals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_workspaces_web.types.list_portals_response.ListPortalsResponse",
        ) -> dict[str, Any]:
            import capo_workspaces_web.types.list_portals_response

            return capo_workspaces_web.types.list_portals_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("ListPortals", redact_output=_redact_output),
        )
        input_: capo_workspaces_web.types.list_portals_request.ListPortalsRequest = {}
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

    async def associate_browser_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        browser_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_browser_settings_response.AssociateBrowserSettingsResponse":
        """<p>Associates a browser settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            browser_settings_arn: <p>The ARN of the browser settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_browser_settings_request.AssociateBrowserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_browser_settings_response.AssociateBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_browser_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_browser_settings.async_associate_browser_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateBrowserSettings")
        )
        input_: capo_workspaces_web.types.associate_browser_settings_request.AssociateBrowserSettingsRequest = {
            "portal_arn": portal_arn,
            "browser_settings_arn": browser_settings_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_data_protection_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_data_protection_settings_response.AssociateDataProtectionSettingsResponse":
        """<p>Associates a data protection settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            data_protection_settings_arn: <p>The ARN of the data protection settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_data_protection_settings_request.AssociateDataProtectionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_data_protection_settings_response.AssociateDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_data_protection_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_data_protection_settings.async_associate_data_protection_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateDataProtectionSettings")
        )
        input_: capo_workspaces_web.types.associate_data_protection_settings_request.AssociateDataProtectionSettingsRequest = {
            "portal_arn": portal_arn,
            "data_protection_settings_arn": data_protection_settings_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_ip_access_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_ip_access_settings_response.AssociateIpAccessSettingsResponse":
        """<p>Associates an IP access settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            ip_access_settings_arn: <p>The ARN of the IP access settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_ip_access_settings_request.AssociateIpAccessSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_ip_access_settings_response.AssociateIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_ip_access_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_ip_access_settings.async_associate_ip_access_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateIpAccessSettings")
        )
        input_: capo_workspaces_web.types.associate_ip_access_settings_request.AssociateIpAccessSettingsRequest = {
            "portal_arn": portal_arn,
            "ip_access_settings_arn": ip_access_settings_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_network_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        network_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_network_settings_response.AssociateNetworkSettingsResponse":
        """<p>Associates a network settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            network_settings_arn: <p>The ARN of the network settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_network_settings_request.AssociateNetworkSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_network_settings_response.AssociateNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_network_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_network_settings.async_associate_network_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateNetworkSettings")
        )
        input_: capo_workspaces_web.types.associate_network_settings_request.AssociateNetworkSettingsRequest = {
            "portal_arn": portal_arn,
            "network_settings_arn": network_settings_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_session_logger(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        session_logger_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_session_logger_response.AssociateSessionLoggerResponse":
        """<p>Associates a session logger with a portal.</p>

        Args:
            portal_arn: <p>The ARN of the portal to associate to the session logger ARN.</p>
            session_logger_arn: <p>The ARN of the session logger to associate to the portal ARN.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Associate Session Logger with Portal
            Associates a session logger with a portal

            >>> await client.associate_session_logger(portal_arn='arn:aws:workspaces-web:us-west-2:123456789012:portal/12345678-1234-1234-1234-123456789012', session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/11111111-1111-1111-1111-111111111111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_session_logger_request.AssociateSessionLoggerRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_session_logger_response.AssociateSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_session_logger

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_session_logger.async_associate_session_logger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateSessionLogger")
        )
        input_: capo_workspaces_web.types.associate_session_logger_request.AssociateSessionLoggerRequest = {
            "portal_arn": portal_arn,
            "session_logger_arn": session_logger_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_trust_store(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_trust_store_response.AssociateTrustStoreResponse":
        """<p>Associates a trust store with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            trust_store_arn: <p>The ARN of the trust store.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_trust_store_request.AssociateTrustStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_trust_store_response.AssociateTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_trust_store

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_trust_store.async_associate_trust_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateTrustStore")
        )
        input_: capo_workspaces_web.types.associate_trust_store_request.AssociateTrustStoreRequest = {
            "portal_arn": portal_arn,
            "trust_store_arn": trust_store_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_user_access_logging_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_user_access_logging_settings_response.AssociateUserAccessLoggingSettingsResponse":
        """<p>Associates a user access logging settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            user_access_logging_settings_arn: <p>The ARN of the user access logging settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_user_access_logging_settings_request.AssociateUserAccessLoggingSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_user_access_logging_settings_response.AssociateUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_access_logging_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_access_logging_settings.async_associate_user_access_logging_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateUserAccessLoggingSettings")
        )
        input_: capo_workspaces_web.types.associate_user_access_logging_settings_request.AssociateUserAccessLoggingSettingsRequest = {
            "portal_arn": portal_arn,
            "user_access_logging_settings_arn": user_access_logging_settings_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_user_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        user_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.associate_user_settings_response.AssociateUserSettingsResponse":
        """<p>Associates a user settings resource with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            user_settings_arn: <p>The ARN of the user settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.associate_user_settings_request.AssociateUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.associate_user_settings_response.AssociateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.associate_user_settings.async_associate_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("AssociateUserSettings")
        )
        input_: capo_workspaces_web.types.associate_user_settings_request.AssociateUserSettingsRequest = {
            "portal_arn": portal_arn,
            "user_settings_arn": user_settings_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_browser_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_browser_settings_response.DisassociateBrowserSettingsResponse":
        """<p>Disassociates browser settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_browser_settings_request.DisassociateBrowserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_browser_settings_response.DisassociateBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_browser_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_browser_settings.async_disassociate_browser_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateBrowserSettings")
        )
        input_: capo_workspaces_web.types.disassociate_browser_settings_request.DisassociateBrowserSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_data_protection_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_data_protection_settings_response.DisassociateDataProtectionSettingsResponse":
        """<p>Disassociates data protection settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_data_protection_settings_request.DisassociateDataProtectionSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_data_protection_settings_response.DisassociateDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_data_protection_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_data_protection_settings.async_disassociate_data_protection_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateDataProtectionSettings")
        )
        input_: capo_workspaces_web.types.disassociate_data_protection_settings_request.DisassociateDataProtectionSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_ip_access_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_ip_access_settings_response.DisassociateIpAccessSettingsResponse":
        """<p>Disassociates IP access settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_ip_access_settings_request.DisassociateIpAccessSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_ip_access_settings_response.DisassociateIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_ip_access_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_ip_access_settings.async_disassociate_ip_access_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateIpAccessSettings")
        )
        input_: capo_workspaces_web.types.disassociate_ip_access_settings_request.DisassociateIpAccessSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_network_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_network_settings_response.DisassociateNetworkSettingsResponse":
        """<p>Disassociates network settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_network_settings_request.DisassociateNetworkSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_network_settings_response.DisassociateNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_network_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_network_settings.async_disassociate_network_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateNetworkSettings")
        )
        input_: capo_workspaces_web.types.disassociate_network_settings_request.DisassociateNetworkSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_session_logger(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_session_logger_response.DisassociateSessionLoggerResponse":
        """<p>Disassociates a session logger from a portal.</p>

        Args:
            portal_arn: <p>The ARN of the portal to disassociate from the a session logger.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Disassociate Session Logger from Portal
            Removes the association between a session logger and a portal

            >>> await client.disassociate_session_logger(portal_arn='arn:aws:workspaces-web:us-west-2:123456789012:portal/12345678-1234-1234-1234-123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_session_logger_request.DisassociateSessionLoggerRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_session_logger_response.DisassociateSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_session_logger

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_session_logger.async_disassociate_session_logger(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateSessionLogger")
        )
        input_: capo_workspaces_web.types.disassociate_session_logger_request.DisassociateSessionLoggerRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_trust_store(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse":
        """<p>Disassociates a trust store from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_trust_store_response.DisassociateTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_trust_store

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_trust_store.async_disassociate_trust_store(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateTrustStore")
        )
        input_: capo_workspaces_web.types.disassociate_trust_store_request.DisassociateTrustStoreRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_user_access_logging_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_user_access_logging_settings_response.DisassociateUserAccessLoggingSettingsResponse":
        """<p>Disassociates user access logging settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_user_access_logging_settings_request.DisassociateUserAccessLoggingSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_user_access_logging_settings_response.DisassociateUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_access_logging_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_access_logging_settings.async_disassociate_user_access_logging_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateUserAccessLoggingSettings")
        )
        input_: capo_workspaces_web.types.disassociate_user_access_logging_settings_request.DisassociateUserAccessLoggingSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_user_settings(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.disassociate_user_settings_response.DisassociateUserSettingsResponse":
        """<p>Disassociates user settings from a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.disassociate_user_settings_request.DisassociateUserSettingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.disassociate_user_settings_response.DisassociateUserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_settings

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.disassociate_user_settings.async_disassociate_user_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DisassociateUserSettings")
        )
        input_: capo_workspaces_web.types.disassociate_user_settings_request.DisassociateUserSettingsRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_portal_service_provider_metadata(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[AsyncWorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_portal_service_provider_metadata_response.GetPortalServiceProviderMetadataResponse":
        """<p>Gets the service provider metadata.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_workspaces_web.types.get_portal_service_provider_metadata_request.GetPortalServiceProviderMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_workspaces_web.types.get_portal_service_provider_metadata_response.GetPortalServiceProviderMetadataResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal_service_provider_metadata

            (
                output,
                http_response,
            ) = await capo_workspaces_web._operations.aws_ermine_control_plane_service.get_portal_service_provider_metadata.async_get_portal_service_provider_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetPortalServiceProviderMetadata")
        )
        input_: capo_workspaces_web.types.get_portal_service_provider_metadata_request.GetPortalServiceProviderMetadataRequest = {
            "portal_arn": portal_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
