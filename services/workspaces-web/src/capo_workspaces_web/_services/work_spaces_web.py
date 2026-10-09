"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AWSErmineControlPlaneService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_workspaces_web._auth._signers
import capo_workspaces_web._auth._sigv4
from capo_workspaces_web._auth._identity import Credentials
from capo_workspaces_web._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_workspaces_web._auth._zapros_handler import AuthMiddleware
from capo_workspaces_web._pagination import resolve_path as _resolve_path
from capo_workspaces_web._resources.aws_ermine_control_plane_service.browser_settings_resource import (
    BrowserSettingsResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.data_protection_settings_resource import (
    DataProtectionSettingsResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.identity_provider_resource import (
    IdentityProviderResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.ip_access_settings_resource import (
    IpAccessSettingsResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.network_settings_resource import (
    NetworkSettingsResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.portal_resource import (
    PortalResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.session_logger_resource import (
    SessionLoggerResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.trust_store_resource import (
    TrustStoreResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.user_access_logging_settings_resource import (
    UserAccessLoggingSettingsResource,
)
from capo_workspaces_web._resources.aws_ermine_control_plane_service.user_settings_resource import (
    UserSettingsResource,
)
from capo_workspaces_web._services._aws_config import aws_config
from capo_workspaces_web._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
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
    import capo_workspaces_web.types.branding_configuration_create_input
    import capo_workspaces_web.types.branding_configuration_update_input
    import capo_workspaces_web.types.browser_policy
    import capo_workspaces_web.types.certificate_list
    import capo_workspaces_web.types.certificate_thumbprint
    import capo_workspaces_web.types.certificate_thumbprint_list
    import capo_workspaces_web.types.client_token
    import capo_workspaces_web.types.cookie_synchronization_configuration
    import capo_workspaces_web.types.create_browser_settings_request
    import capo_workspaces_web.types.create_browser_settings_response
    import capo_workspaces_web.types.create_data_protection_settings_request
    import capo_workspaces_web.types.create_data_protection_settings_response
    import capo_workspaces_web.types.create_identity_provider_request
    import capo_workspaces_web.types.create_identity_provider_response
    import capo_workspaces_web.types.create_ip_access_settings_request
    import capo_workspaces_web.types.create_ip_access_settings_response
    import capo_workspaces_web.types.create_network_settings_request
    import capo_workspaces_web.types.create_network_settings_response
    import capo_workspaces_web.types.create_portal_request
    import capo_workspaces_web.types.create_portal_response
    import capo_workspaces_web.types.create_session_logger_request
    import capo_workspaces_web.types.create_session_logger_response
    import capo_workspaces_web.types.create_trust_store_request
    import capo_workspaces_web.types.create_trust_store_response
    import capo_workspaces_web.types.create_user_access_logging_settings_request
    import capo_workspaces_web.types.create_user_access_logging_settings_response
    import capo_workspaces_web.types.create_user_settings_request
    import capo_workspaces_web.types.create_user_settings_response
    import capo_workspaces_web.types.data_protection_settings_summary
    import capo_workspaces_web.types.delete_browser_settings_request
    import capo_workspaces_web.types.delete_browser_settings_response
    import capo_workspaces_web.types.delete_data_protection_settings_request
    import capo_workspaces_web.types.delete_data_protection_settings_response
    import capo_workspaces_web.types.delete_identity_provider_request
    import capo_workspaces_web.types.delete_identity_provider_response
    import capo_workspaces_web.types.delete_ip_access_settings_request
    import capo_workspaces_web.types.delete_ip_access_settings_response
    import capo_workspaces_web.types.delete_network_settings_request
    import capo_workspaces_web.types.delete_network_settings_response
    import capo_workspaces_web.types.delete_portal_request
    import capo_workspaces_web.types.delete_portal_response
    import capo_workspaces_web.types.delete_session_logger_request
    import capo_workspaces_web.types.delete_session_logger_response
    import capo_workspaces_web.types.delete_trust_store_request
    import capo_workspaces_web.types.delete_trust_store_response
    import capo_workspaces_web.types.delete_user_access_logging_settings_request
    import capo_workspaces_web.types.delete_user_access_logging_settings_response
    import capo_workspaces_web.types.delete_user_settings_request
    import capo_workspaces_web.types.delete_user_settings_response
    import capo_workspaces_web.types.description
    import capo_workspaces_web.types.description_safe
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
    import capo_workspaces_web.types.disconnect_timeout_in_minutes
    import capo_workspaces_web.types.display_name
    import capo_workspaces_web.types.display_name_safe
    import capo_workspaces_web.types.enabled_type
    import capo_workspaces_web.types.encryption_context_map
    import capo_workspaces_web.types.event_filter
    import capo_workspaces_web.types.expire_session_request
    import capo_workspaces_web.types.expire_session_response
    import capo_workspaces_web.types.get_browser_settings_request
    import capo_workspaces_web.types.get_browser_settings_response
    import capo_workspaces_web.types.get_data_protection_settings_request
    import capo_workspaces_web.types.get_data_protection_settings_response
    import capo_workspaces_web.types.get_identity_provider_request
    import capo_workspaces_web.types.get_identity_provider_response
    import capo_workspaces_web.types.get_ip_access_settings_request
    import capo_workspaces_web.types.get_ip_access_settings_response
    import capo_workspaces_web.types.get_network_settings_request
    import capo_workspaces_web.types.get_network_settings_response
    import capo_workspaces_web.types.get_portal_request
    import capo_workspaces_web.types.get_portal_response
    import capo_workspaces_web.types.get_portal_service_provider_metadata_request
    import capo_workspaces_web.types.get_portal_service_provider_metadata_response
    import capo_workspaces_web.types.get_session_logger_request
    import capo_workspaces_web.types.get_session_logger_response
    import capo_workspaces_web.types.get_session_request
    import capo_workspaces_web.types.get_session_response
    import capo_workspaces_web.types.get_trust_store_certificate_request
    import capo_workspaces_web.types.get_trust_store_certificate_response
    import capo_workspaces_web.types.get_trust_store_request
    import capo_workspaces_web.types.get_trust_store_response
    import capo_workspaces_web.types.get_user_access_logging_settings_request
    import capo_workspaces_web.types.get_user_access_logging_settings_response
    import capo_workspaces_web.types.get_user_settings_request
    import capo_workspaces_web.types.get_user_settings_response
    import capo_workspaces_web.types.identity_provider_details
    import capo_workspaces_web.types.identity_provider_name
    import capo_workspaces_web.types.identity_provider_type
    import capo_workspaces_web.types.idle_disconnect_timeout_in_minutes
    import capo_workspaces_web.types.inline_redaction_configuration
    import capo_workspaces_web.types.instance_type
    import capo_workspaces_web.types.ip_rule_list
    import capo_workspaces_web.types.key_arn
    import capo_workspaces_web.types.kinesis_stream_arn
    import capo_workspaces_web.types.list_browser_settings_request
    import capo_workspaces_web.types.list_browser_settings_response
    import capo_workspaces_web.types.list_data_protection_settings_request
    import capo_workspaces_web.types.list_data_protection_settings_response
    import capo_workspaces_web.types.list_identity_providers_request
    import capo_workspaces_web.types.list_identity_providers_response
    import capo_workspaces_web.types.list_ip_access_settings_request
    import capo_workspaces_web.types.list_ip_access_settings_response
    import capo_workspaces_web.types.list_network_settings_request
    import capo_workspaces_web.types.list_network_settings_response
    import capo_workspaces_web.types.list_portals_request
    import capo_workspaces_web.types.list_portals_response
    import capo_workspaces_web.types.list_session_loggers_request
    import capo_workspaces_web.types.list_session_loggers_response
    import capo_workspaces_web.types.list_sessions_request
    import capo_workspaces_web.types.list_sessions_response
    import capo_workspaces_web.types.list_tags_for_resource_request
    import capo_workspaces_web.types.list_tags_for_resource_response
    import capo_workspaces_web.types.list_trust_store_certificates_request
    import capo_workspaces_web.types.list_trust_store_certificates_response
    import capo_workspaces_web.types.list_trust_stores_request
    import capo_workspaces_web.types.list_trust_stores_response
    import capo_workspaces_web.types.list_user_access_logging_settings_request
    import capo_workspaces_web.types.list_user_access_logging_settings_response
    import capo_workspaces_web.types.list_user_settings_request
    import capo_workspaces_web.types.list_user_settings_response
    import capo_workspaces_web.types.log_configuration
    import capo_workspaces_web.types.max_concurrent_sessions
    import capo_workspaces_web.types.max_results
    import capo_workspaces_web.types.pagination_token
    import capo_workspaces_web.types.portal_custom_domain
    import capo_workspaces_web.types.portal_id
    import capo_workspaces_web.types.security_group_id_list
    import capo_workspaces_web.types.session_id
    import capo_workspaces_web.types.session_logger_summary
    import capo_workspaces_web.types.session_sort_by
    import capo_workspaces_web.types.session_status
    import capo_workspaces_web.types.session_summary
    import capo_workspaces_web.types.subnet_id_list
    import capo_workspaces_web.types.subresource_arn
    import capo_workspaces_web.types.tag_key_list
    import capo_workspaces_web.types.tag_list
    import capo_workspaces_web.types.tag_resource_request
    import capo_workspaces_web.types.tag_resource_response
    import capo_workspaces_web.types.toolbar_configuration
    import capo_workspaces_web.types.untag_resource_request
    import capo_workspaces_web.types.untag_resource_response
    import capo_workspaces_web.types.update_browser_settings_request
    import capo_workspaces_web.types.update_browser_settings_response
    import capo_workspaces_web.types.update_data_protection_settings_request
    import capo_workspaces_web.types.update_data_protection_settings_response
    import capo_workspaces_web.types.update_identity_provider_request
    import capo_workspaces_web.types.update_identity_provider_response
    import capo_workspaces_web.types.update_ip_access_settings_request
    import capo_workspaces_web.types.update_ip_access_settings_response
    import capo_workspaces_web.types.update_network_settings_request
    import capo_workspaces_web.types.update_network_settings_response
    import capo_workspaces_web.types.update_portal_request
    import capo_workspaces_web.types.update_portal_response
    import capo_workspaces_web.types.update_session_logger_request
    import capo_workspaces_web.types.update_session_logger_response
    import capo_workspaces_web.types.update_trust_store_request
    import capo_workspaces_web.types.update_trust_store_response
    import capo_workspaces_web.types.update_user_access_logging_settings_request
    import capo_workspaces_web.types.update_user_access_logging_settings_response
    import capo_workspaces_web.types.update_user_settings_request
    import capo_workspaces_web.types.update_user_settings_response
    import capo_workspaces_web.types.username
    import capo_workspaces_web.types.vpc_id
    import capo_workspaces_web.types.web_content_filtering_policy


class WorkSpacesWebClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class WorkSpacesWebClient:
    """A client for the ``WorkSpacesWeb`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = WorkSpacesWebClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

        # resources
        self.browser_settings_resource = BrowserSettingsResource(self)
        self.data_protection_settings_resource = DataProtectionSettingsResource(self)
        self.identity_provider_resource = IdentityProviderResource(self)
        self.ip_access_settings_resource = IpAccessSettingsResource(self)
        self.network_settings_resource = NetworkSettingsResource(self)
        self.portal_resource = PortalResource(self)
        self.session_logger_resource = SessionLoggerResource(self)
        self.trust_store_resource = TrustStoreResource(self)
        self.user_access_logging_settings_resource = UserAccessLoggingSettingsResource(
            self
        )
        self.user_settings_resource = UserSettingsResource(self)

    def operation_options(
        self, config_overrides: Optional[WorkSpacesWebClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkSpacesWebClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def expire_session(
        self,
        portal_id: "capo_workspaces_web.types.portal_id.PortalId",
        session_id: "capo_workspaces_web.types.session_id.SessionId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.expire_session_response.ExpireSessionResponse":
        """<p>Expires an active secure browser session.</p>

        Args:
            portal_id: <p>The ID of the web portal for the session.</p>
            session_id: <p>The ID of the session to expire.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.expire_session_request.ExpireSessionRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.expire_session_response.ExpireSessionResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.expire_session

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.expire_session.expire_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.expire_session_request.ExpireSessionRequest = {
            "portal_id": portal_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session(
        self,
        portal_id: "capo_workspaces_web.types.portal_id.PortalId",
        session_id: "capo_workspaces_web.types.session_id.SessionId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_session_response.GetSessionResponse":
        """<p>Gets information for a secure browser session.</p>

        Args:
            portal_id: <p>The ID of the web portal for the session.</p>
            session_id: <p>The ID of the session.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_session_response.GetSessionResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_session

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_session_request.GetSessionRequest = {
            "portal_id": portal_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_sessions(
        self,
        portal_id: "capo_workspaces_web.types.portal_id.PortalId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        username: Optional["capo_workspaces_web.types.username.Username"] = None,
        session_id: Optional["capo_workspaces_web.types.session_id.SessionId"] = None,
        sort_by: Optional[
            "capo_workspaces_web.types.session_sort_by.SessionSortBy"
        ] = None,
        status: Optional[
            "capo_workspaces_web.types.session_status.SessionStatus"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces_web.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists information for multiple secure browser sessions from a specific portal.</p>

        Args:
            portal_id: <p>The ID of the web portal for the sessions.</p>
            username: <p>The username of the session.</p>
            session_id: <p>The ID of the session.</p>
            sort_by: <p>The method in which the returned sessions should be sorted.</p>
            status: <p>The status of the session.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_sessions

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_sessions_request.ListSessionsRequest = {
            "portal_id": portal_id
        }
        if username is not None:
            input_["username"] = username
        if session_id is not None:
            input_["session_id"] = session_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if status is not None:
            input_["status"] = status
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

    def iter_list_sessions(
        self,
        portal_id: "capo_workspaces_web.types.portal_id.PortalId",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        username: Optional["capo_workspaces_web.types.username.Username"] = None,
        session_id: Optional["capo_workspaces_web.types.session_id.SessionId"] = None,
        sort_by: Optional[
            "capo_workspaces_web.types.session_sort_by.SessionSortBy"
        ] = None,
        status: Optional[
            "capo_workspaces_web.types.session_status.SessionStatus"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                portal_id,
                config_overrides=config_overrides,
                username=username,
                session_id=session_id,
                sort_by=sort_by,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves a list of tags for a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_tags_for_resource

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_workspaces_web.types.arn.ARN",
        tags: "capo_workspaces_web.types.tag_list.TagList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites one or more tags for the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tags: <p>The tags of the resource.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.too_many_tags_exception.TooManyTagsException: <p>There are too many tags.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.tag_resource

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_workspaces_web.types.arn.ARN",
        tag_keys: "capo_workspaces_web.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.untag_resource

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_browser_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        browser_policy: Optional[
            "capo_workspaces_web.types.browser_policy.BrowserPolicy"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        web_content_filtering_policy: Optional[
            "capo_workspaces_web.types.web_content_filtering_policy.WebContentFilteringPolicy"
        ] = None,
    ) -> "capo_workspaces_web.types.create_browser_settings_response.CreateBrowserSettingsResponse":
        """<p>Creates a browser settings resource that can be associated with a web portal. Once associated with a web portal, browser settings control how the browser will behave once a user starts a streaming session for the web portal. </p>

        Args:
            tags: <p>The tags to add to the browser settings resource. A tag is a key-value pair.</p>
            customer_managed_key: <p>The custom managed key of the browser settings.</p>
            additional_encryption_context: <p>Additional encryption context of the browser settings.</p>
            browser_policy: <p>A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request.</p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK. </p>
            web_content_filtering_policy: <p>The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.</p>

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
            req: "OperationRequest[capo_workspaces_web.types.create_browser_settings_request.CreateBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_browser_settings_response.CreateBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_browser_settings.create_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_browser_settings_request.CreateBrowserSettingsRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if browser_policy is not None:
            input_["browser_policy"] = browser_policy
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if web_content_filtering_policy is not None:
            input_["web_content_filtering_policy"] = web_content_filtering_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_browser_settings(
        self,
        browser_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_browser_settings_response.GetBrowserSettingsResponse":
        """<p>Gets browser settings.</p>

        Args:
            browser_settings_arn: <p>The ARN of the browser settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_browser_settings_request.GetBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_browser_settings_response.GetBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_browser_settings.get_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_browser_settings_request.GetBrowserSettingsRequest = {
            "browser_settings_arn": browser_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_browser_settings(
        self,
        browser_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        browser_policy: Optional[
            "capo_workspaces_web.types.browser_policy.BrowserPolicy"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        web_content_filtering_policy: Optional[
            "capo_workspaces_web.types.web_content_filtering_policy.WebContentFilteringPolicy"
        ] = None,
    ) -> "capo_workspaces_web.types.update_browser_settings_response.UpdateBrowserSettingsResponse":
        """<p>Updates browser settings.</p>

        Args:
            browser_settings_arn: <p>The ARN of the browser settings.</p>
            browser_policy: <p>A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions. </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            web_content_filtering_policy: <p>The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_browser_settings_request.UpdateBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_browser_settings_response.UpdateBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_browser_settings.update_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_browser_settings_request.UpdateBrowserSettingsRequest = {
            "browser_settings_arn": browser_settings_arn
        }
        if browser_policy is not None:
            input_["browser_policy"] = browser_policy
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if web_content_filtering_policy is not None:
            input_["web_content_filtering_policy"] = web_content_filtering_policy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_browser_settings(
        self,
        browser_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_browser_settings_response.DeleteBrowserSettingsResponse":
        """<p>Deletes browser settings.</p>

        Args:
            browser_settings_arn: <p>The ARN of the browser settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_browser_settings_request.DeleteBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_browser_settings_response.DeleteBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_browser_settings.delete_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_browser_settings_request.DeleteBrowserSettingsRequest = {
            "browser_settings_arn": browser_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_browser_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_browser_settings_response.ListBrowserSettingsResponse":
        """<p>Retrieves a list of browser settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_browser_settings_request.ListBrowserSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_browser_settings_response.ListBrowserSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_browser_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_browser_settings.list_browser_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_browser_settings_request.ListBrowserSettingsRequest = {}
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

    def iter_list_browser_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_browser_settings_response.ListBrowserSettingsResponse]":
        _token = next_token
        while True:
            _response = self.list_browser_settings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_data_protection_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
        ] = None,
        description: Optional[
            "capo_workspaces_web.types.description_safe.DescriptionSafe"
        ] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        inline_redaction_configuration: Optional[
            "capo_workspaces_web.types.inline_redaction_configuration.InlineRedactionConfiguration"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.create_data_protection_settings_response.CreateDataProtectionSettingsResponse":
        """<p>Creates a data protection settings resource that can be associated with a web portal.</p>

        Args:
            display_name: <p>The display name of the data protection settings.</p>
            description: <p>The description of the data protection settings.</p>
            tags: <p>The tags to add to the data protection settings resource. A tag is a key-value pair.</p>
            customer_managed_key: <p>The custom managed key of the data protection settings.</p>
            additional_encryption_context: <p>Additional encryption context of the data protection settings.</p>
            inline_redaction_configuration: <p>The inline redaction configuration of the data protection settings that will be applied to all sessions.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

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
            req: "OperationRequest[capo_workspaces_web.types.create_data_protection_settings_request.CreateDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_data_protection_settings_response.CreateDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_data_protection_settings.create_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_data_protection_settings_request.CreateDataProtectionSettingsRequest = {}
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if inline_redaction_configuration is not None:
            input_["inline_redaction_configuration"] = inline_redaction_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_protection_settings(
        self,
        data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_data_protection_settings_response.GetDataProtectionSettingsResponse":
        """<p>Gets the data protection settings.</p>

        Args:
            data_protection_settings_arn: <p>The ARN of the data protection settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_data_protection_settings_request.GetDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_data_protection_settings_response.GetDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_data_protection_settings.get_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_data_protection_settings_request.GetDataProtectionSettingsRequest = {
            "data_protection_settings_arn": data_protection_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_protection_settings(
        self,
        data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        inline_redaction_configuration: Optional[
            "capo_workspaces_web.types.inline_redaction_configuration.InlineRedactionConfiguration"
        ] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
        ] = None,
        description: Optional[
            "capo_workspaces_web.types.description_safe.DescriptionSafe"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.update_data_protection_settings_response.UpdateDataProtectionSettingsResponse":
        """<p>Updates data protection settings.</p>

        Args:
            data_protection_settings_arn: <p>The ARN of the data protection settings.</p>
            inline_redaction_configuration: <p>The inline redaction configuration of the data protection settings that will be applied to all sessions.</p>
            display_name: <p>The display name of the data protection settings.</p>
            description: <p>The description of the data protection settings.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_data_protection_settings_request.UpdateDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_data_protection_settings_response.UpdateDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_data_protection_settings.update_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_data_protection_settings_request.UpdateDataProtectionSettingsRequest = {
            "data_protection_settings_arn": data_protection_settings_arn
        }
        if inline_redaction_configuration is not None:
            input_["inline_redaction_configuration"] = inline_redaction_configuration
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_protection_settings(
        self,
        data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_data_protection_settings_response.DeleteDataProtectionSettingsResponse":
        """<p>Deletes data protection settings.</p>

        Args:
            data_protection_settings_arn: <p>The ARN of the data protection settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_data_protection_settings_request.DeleteDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_data_protection_settings_response.DeleteDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_data_protection_settings.delete_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_data_protection_settings_request.DeleteDataProtectionSettingsRequest = {
            "data_protection_settings_arn": data_protection_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_protection_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_data_protection_settings_response.ListDataProtectionSettingsResponse":
        """<p>Retrieves a list of data protection settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_data_protection_settings_request.ListDataProtectionSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_data_protection_settings_response.ListDataProtectionSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_data_protection_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_data_protection_settings.list_data_protection_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_data_protection_settings_request.ListDataProtectionSettingsRequest = {}
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

    def iter_list_data_protection_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.data_protection_settings_summary.DataProtectionSettingsSummary]":
        _token = next_token
        while True:
            _response = self.list_data_protection_settings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_protection_settings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_identity_provider(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        identity_provider_name: "capo_workspaces_web.types.identity_provider_name.IdentityProviderName",
        identity_provider_type: "capo_workspaces_web.types.identity_provider_type.IdentityProviderType",
        identity_provider_details: "capo_workspaces_web.types.identity_provider_details.IdentityProviderDetails",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces_web.types.create_identity_provider_response.CreateIdentityProviderResponse":
        """<p>Creates an identity provider resource that is then associated with a web portal.</p>

        Args:
            portal_arn: <p>The ARN of the web portal.</p>
            identity_provider_name: <p>The identity provider name.</p>
            identity_provider_type: <p>The identity provider type.</p>
            identity_provider_details: <p>The identity provider details. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request.</p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>
            tags: <p>The tags to add to the identity provider resource. A tag is a key-value pair.</p>

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
            req: "OperationRequest[capo_workspaces_web.types.create_identity_provider_request.CreateIdentityProviderRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_identity_provider_response.CreateIdentityProviderResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_identity_provider

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_identity_provider.create_identity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_identity_provider_request.CreateIdentityProviderRequest = {
            "portal_arn": portal_arn,
            "identity_provider_name": identity_provider_name,
            "identity_provider_type": identity_provider_type,
            "identity_provider_details": identity_provider_details,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_identity_provider(
        self,
        identity_provider_arn: "capo_workspaces_web.types.subresource_arn.SubresourceARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_identity_provider_response.GetIdentityProviderResponse":
        """<p>Gets the identity provider.</p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_identity_provider_request.GetIdentityProviderRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_identity_provider_response.GetIdentityProviderResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_identity_provider

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_identity_provider.get_identity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_identity_provider_request.GetIdentityProviderRequest = {
            "identity_provider_arn": identity_provider_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_identity_provider(
        self,
        identity_provider_arn: "capo_workspaces_web.types.subresource_arn.SubresourceARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        identity_provider_name: Optional[
            "capo_workspaces_web.types.identity_provider_name.IdentityProviderName"
        ] = None,
        identity_provider_type: Optional[
            "capo_workspaces_web.types.identity_provider_type.IdentityProviderType"
        ] = None,
        identity_provider_details: Optional[
            "capo_workspaces_web.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.update_identity_provider_response.UpdateIdentityProviderResponse":
        """<p>Updates the identity provider. </p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>
            identity_provider_name: <p>The name of the identity provider.</p>
            identity_provider_type: <p>The type of the identity provider.</p>
            identity_provider_details: <p>The details of the identity provider. The following list describes the provider detail keys for each identity provider type. </p> <ul> <li> <p>For Google and Login with Amazon:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For Facebook:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>api_version</code> </p> </li> </ul> </li> <li> <p>For Sign in with Apple:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>team_id</code> </p> </li> <li> <p> <code>key_id</code> </p> </li> <li> <p> <code>private_key</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> </ul> </li> <li> <p>For OIDC providers:</p> <ul> <li> <p> <code>client_id</code> </p> </li> <li> <p> <code>client_secret</code> </p> </li> <li> <p> <code>attributes_request_method</code> </p> </li> <li> <p> <code>oidc_issuer</code> </p> </li> <li> <p> <code>authorize_scopes</code> </p> </li> <li> <p> <code>authorize_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>token_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>attributes_url</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> <li> <p> <code>jwks_uri</code> <i>if not available from discovery URL specified by <code>oidc_issuer</code> key</i> </p> </li> </ul> </li> <li> <p>For SAML providers:</p> <ul> <li> <p> <code>MetadataFile</code> OR <code>MetadataURL</code> </p> </li> <li> <p> <code>IDPSignout</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>IDPInit</code> (boolean) <i>optional</i> </p> </li> <li> <p> <code>RequestSigningAlgorithm</code> (string) <i>optional</i> - Only accepts <code>rsa-sha256</code> </p> </li> <li> <p> <code>EncryptedResponses</code> (boolean) <i>optional</i> </p> </li> </ul> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_identity_provider_request.UpdateIdentityProviderRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_identity_provider_response.UpdateIdentityProviderResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_identity_provider

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_identity_provider.update_identity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_identity_provider_request.UpdateIdentityProviderRequest = {
            "identity_provider_arn": identity_provider_arn
        }
        if identity_provider_name is not None:
            input_["identity_provider_name"] = identity_provider_name
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_identity_provider(
        self,
        identity_provider_arn: "capo_workspaces_web.types.subresource_arn.SubresourceARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_identity_provider_response.DeleteIdentityProviderResponse":
        """<p>Deletes the identity provider.</p>

        Args:
            identity_provider_arn: <p>The ARN of the identity provider.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_identity_provider_request.DeleteIdentityProviderRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_identity_provider_response.DeleteIdentityProviderResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_identity_provider

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_identity_provider.delete_identity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_identity_provider_request.DeleteIdentityProviderRequest = {
            "identity_provider_arn": identity_provider_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_identity_providers(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse":
        """<p>Retrieves a list of identity providers for a specific web portal.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>
            portal_arn: <p>The ARN of the web portal.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_identity_providers_request.ListIdentityProvidersRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_identity_providers

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_identity_providers.list_identity_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_identity_providers_request.ListIdentityProvidersRequest = {
            "portal_arn": portal_arn
        }
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

    def iter_list_identity_providers(
        self,
        portal_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_identity_providers_response.ListIdentityProvidersResponse]":
        _token = next_token
        while True:
            _response = self.list_identity_providers(
                portal_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_ip_access_settings(
        self,
        ip_rules: "capo_workspaces_web.types.ip_rule_list.IpRuleList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_workspaces_web.types.description.Description"
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
    ) -> "capo_workspaces_web.types.create_ip_access_settings_response.CreateIpAccessSettingsResponse":
        """<p>Creates an IP access settings resource that can be associated with a web portal.</p>

        Args:
            display_name: <p>The display name of the IP access settings.</p>
            description: <p>The description of the IP access settings.</p>
            tags: <p>The tags to add to the IP access settings resource. A tag is a key-value pair.</p>
            customer_managed_key: <p>The custom managed key of the IP access settings.</p>
            additional_encryption_context: <p>Additional encryption context of the IP access settings.</p>
            ip_rules: <p>The IP rules of the IP access settings.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.create_ip_access_settings_request.CreateIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_ip_access_settings_response.CreateIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_ip_access_settings.create_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_ip_access_settings_request.CreateIpAccessSettingsRequest = {
            "ip_rules": ip_rules
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ip_access_settings(
        self,
        ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_ip_access_settings_response.GetIpAccessSettingsResponse":
        """<p>Gets the IP access settings.</p>

        Args:
            ip_access_settings_arn: <p>The ARN of the IP access settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_ip_access_settings_request.GetIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_ip_access_settings_response.GetIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_ip_access_settings.get_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_ip_access_settings_request.GetIpAccessSettingsRequest = {
            "ip_access_settings_arn": ip_access_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_ip_access_settings(
        self,
        ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_workspaces_web.types.description.Description"
        ] = None,
        ip_rules: Optional["capo_workspaces_web.types.ip_rule_list.IpRuleList"] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.update_ip_access_settings_response.UpdateIpAccessSettingsResponse":
        """<p>Updates IP access settings.</p>

        Args:
            ip_access_settings_arn: <p>The ARN of the IP access settings.</p>
            display_name: <p>The display name of the IP access settings.</p>
            description: <p>The description of the IP access settings.</p>
            ip_rules: <p>The updated IP rules of the IP access settings.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_ip_access_settings_request.UpdateIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_ip_access_settings_response.UpdateIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_ip_access_settings.update_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_ip_access_settings_request.UpdateIpAccessSettingsRequest = {
            "ip_access_settings_arn": ip_access_settings_arn
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if ip_rules is not None:
            input_["ip_rules"] = ip_rules
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_ip_access_settings(
        self,
        ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_ip_access_settings_response.DeleteIpAccessSettingsResponse":
        """<p>Deletes IP access settings.</p>

        Args:
            ip_access_settings_arn: <p>The ARN of the IP access settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_ip_access_settings_request.DeleteIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_ip_access_settings_response.DeleteIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_ip_access_settings.delete_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_ip_access_settings_request.DeleteIpAccessSettingsRequest = {
            "ip_access_settings_arn": ip_access_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ip_access_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_ip_access_settings_response.ListIpAccessSettingsResponse":
        """<p>Retrieves a list of IP access settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_ip_access_settings_request.ListIpAccessSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_ip_access_settings_response.ListIpAccessSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_ip_access_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_ip_access_settings.list_ip_access_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_ip_access_settings_request.ListIpAccessSettingsRequest = {}
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

    def iter_list_ip_access_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_ip_access_settings_response.ListIpAccessSettingsResponse]":
        _token = next_token
        while True:
            _response = self.list_ip_access_settings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_network_settings(
        self,
        vpc_id: "capo_workspaces_web.types.vpc_id.VpcId",
        subnet_ids: "capo_workspaces_web.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_workspaces_web.types.security_group_id_list.SecurityGroupIdList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.create_network_settings_response.CreateNetworkSettingsResponse":
        """<p>Creates a network settings resource that can be associated with a web portal. Once associated with a web portal, network settings define how streaming instances will connect with your specified VPC. </p>

        Args:
            vpc_id: <p>The VPC that streaming instances will connect to.</p>
            subnet_ids: <p>The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones.</p>
            security_group_ids: <p>One or more security groups used to control access from streaming instances to your VPC.</p>
            tags: <p>The tags to add to the network settings resource. A tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.create_network_settings_request.CreateNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_network_settings_response.CreateNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_network_settings.create_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_network_settings_request.CreateNetworkSettingsRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_network_settings(
        self,
        network_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_network_settings_response.GetNetworkSettingsResponse":
        """<p>Gets the network settings.</p>

        Args:
            network_settings_arn: <p>The ARN of the network settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_network_settings_request.GetNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_network_settings_response.GetNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_network_settings.get_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_network_settings_request.GetNetworkSettingsRequest = {
            "network_settings_arn": network_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network_settings(
        self,
        network_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        vpc_id: Optional["capo_workspaces_web.types.vpc_id.VpcId"] = None,
        subnet_ids: Optional[
            "capo_workspaces_web.types.subnet_id_list.SubnetIdList"
        ] = None,
        security_group_ids: Optional[
            "capo_workspaces_web.types.security_group_id_list.SecurityGroupIdList"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.update_network_settings_response.UpdateNetworkSettingsResponse":
        """<p>Updates network settings.</p>

        Args:
            network_settings_arn: <p>The ARN of the network settings.</p>
            vpc_id: <p>The VPC that streaming instances will connect to.</p>
            subnet_ids: <p>The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones.</p>
            security_group_ids: <p>One or more security groups used to control access from streaming instances to your VPC.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_network_settings_request.UpdateNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_network_settings_response.UpdateNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_network_settings.update_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_network_settings_request.UpdateNetworkSettingsRequest = {
            "network_settings_arn": network_settings_arn
        }
        if vpc_id is not None:
            input_["vpc_id"] = vpc_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if security_group_ids is not None:
            input_["security_group_ids"] = security_group_ids
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_network_settings(
        self,
        network_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_network_settings_response.DeleteNetworkSettingsResponse":
        """<p>Deletes network settings.</p>

        Args:
            network_settings_arn: <p>The ARN of the network settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_network_settings_request.DeleteNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_network_settings_response.DeleteNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_network_settings.delete_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_network_settings_request.DeleteNetworkSettingsRequest = {
            "network_settings_arn": network_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_network_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_network_settings_response.ListNetworkSettingsResponse":
        """<p>Retrieves a list of network settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_network_settings_request.ListNetworkSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_network_settings_response.ListNetworkSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_network_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_network_settings.list_network_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_network_settings_request.ListNetworkSettingsRequest = {}
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

    def iter_list_network_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_network_settings_response.ListNetworkSettingsResponse]":
        _token = next_token
        while True:
            _response = self.list_network_settings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_portal(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_portal(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def update_portal(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_portal(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_portals(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_portals(
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
        "Iterator[capo_workspaces_web.types.list_portals_response.ListPortalsResponse]"
    ):
        _token = next_token
        while True:
            _response = self.list_portals(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def create_session_logger(
        self,
        event_filter: "capo_workspaces_web.types.event_filter.EventFilter",
        log_configuration: "capo_workspaces_web.types.log_configuration.LogConfiguration",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
        ] = None,
        customer_managed_key: Optional[
            "capo_workspaces_web.types.key_arn.keyArn"
        ] = None,
        additional_encryption_context: Optional[
            "capo_workspaces_web.types.encryption_context_map.EncryptionContextMap"
        ] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.create_session_logger_response.CreateSessionLoggerResponse":
        """<p>Creates a session logger.</p>

        Args:
            event_filter: <p>The filter that specifies the events to monitor.</p>
            log_configuration: <p>The configuration that specifies where logs are delivered.</p>
            display_name: <p>The human-readable display name for the session logger resource.</p>
            customer_managed_key: <p>The custom managed key of the session logger.</p>
            additional_encryption_context: <p>The additional encryption context of the session logger.</p>
            tags: <p>The tags to add to the session logger.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. If you do not specify a client token, one is automatically generated by the AWS SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create Session Logger with All Events
            Creates a session logger that captures all events and stores them in S3 with JSON format and flat folder structure

            >>> client.create_session_logger(event_filter={'all': {}}, log_configuration={'s3': {'bucket': 'my-session-logs-bucket', 'keyPrefix': 'session-logs/all/events', 'bucketOwner': '123456789012', 'logFileFormat': 'Json', 'folderStructure': 'Flat'}}, display_name='Session Logger with All Events')
            Create Session Logger with Specific Events
            Creates a session logger that captures only specific events with JSONLines format and nested folder structure

            >>> client.create_session_logger(event_filter={'include': ['SessionStart', 'SessionEnd', 'UrlLoad', 'WebsiteInteract']}, log_configuration={'s3': {'bucket': 'my-session-logs-bucket', 'keyPrefix': 'session-logs/each/event', 'bucketOwner': '123456789012', 'logFileFormat': 'JSONLines', 'folderStructure': 'NestedByDate'}}, display_name='Session Logger with Each Events', customer_managed_key='arn:aws:kms:us-west-2:123456789012:key/12345678-1234-1234-1234-123456789012', additional_encryption_context={'EncryptionContextKey': 'EncryptionContextValue'}, tags=[{'Key': 'KEY-1', 'Value': 'VALUE-1'}, {'Key': 'KEY-2', 'Value': 'VALUE-2'}])
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.create_session_logger_request.CreateSessionLoggerRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_session_logger_response.CreateSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_session_logger

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_session_logger.create_session_logger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_session_logger_request.CreateSessionLoggerRequest = {
            "event_filter": event_filter,
            "log_configuration": log_configuration,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if customer_managed_key is not None:
            input_["customer_managed_key"] = customer_managed_key
        if additional_encryption_context is not None:
            input_["additional_encryption_context"] = additional_encryption_context
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session_logger(
        self,
        session_logger_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> (
        "capo_workspaces_web.types.get_session_logger_response.GetSessionLoggerResponse"
    ):
        """<p>Gets details about a specific session logger resource.</p>

        Args:
            session_logger_arn: <p>The ARN of the session logger.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get Session Logger with All Events
            Retrieves a session logger configured for all events

            >>> client.get_session_logger(session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/12345678-1234-1234-1234-123456789012')
            Get Session Logger with Specific Events
            Retrieves a session logger configured for specific events

            >>> client.get_session_logger(session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/87654321-4321-4321-4321-210987654321')
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_session_logger_request.GetSessionLoggerRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_session_logger_response.GetSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_session_logger

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_session_logger.get_session_logger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_session_logger_request.GetSessionLoggerRequest = {
            "session_logger_arn": session_logger_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_session_logger(
        self,
        session_logger_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        event_filter: Optional[
            "capo_workspaces_web.types.event_filter.EventFilter"
        ] = None,
        log_configuration: Optional[
            "capo_workspaces_web.types.log_configuration.LogConfiguration"
        ] = None,
        display_name: Optional[
            "capo_workspaces_web.types.display_name_safe.DisplayNameSafe"
        ] = None,
    ) -> "capo_workspaces_web.types.update_session_logger_response.UpdateSessionLoggerResponse":
        """<p>Updates the details of a session logger.</p>

        Args:
            session_logger_arn: <p>The ARN of the session logger to update.</p>
            event_filter: <p>The updated eventFilter.</p>
            log_configuration: <p>The updated logConfiguration.</p>
            display_name: <p>The updated display name.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update Session Logger Event Filter
            Updates a session logger to capture specific events instead of all events

            >>> client.update_session_logger(session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/12345678-1234-1234-1234-123456789012', event_filter={'include': ['SessionStart', 'SessionEnd', 'UrlLoad', 'WebsiteInteract']})
            Update Session Logger Configuration
            Updates the log configuration of a session logger

            >>> client.update_session_logger(session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/87654321-4321-4321-4321-210987654321', log_configuration={'s3': {'bucket': 'updated-my-session-logs-bucket-2', 'keyPrefix': 'updated/key/prefix', 'bucketOwner': '123456789012', 'logFileFormat': 'Json', 'folderStructure': 'Flat'}})
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_session_logger_request.UpdateSessionLoggerRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_session_logger_response.UpdateSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_session_logger

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_session_logger.update_session_logger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_session_logger_request.UpdateSessionLoggerRequest = {
            "session_logger_arn": session_logger_arn
        }
        if event_filter is not None:
            input_["event_filter"] = event_filter
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_session_logger(
        self,
        session_logger_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_session_logger_response.DeleteSessionLoggerResponse":
        """<p>Deletes a session logger resource.</p>

        Args:
            session_logger_arn: <p>The ARN of the session logger.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Session Logger
            Deletes a session logger resource

            >>> client.delete_session_logger(session_logger_arn='arn:aws:workspaces-web:us-west-2:123456789012:sessionLogger/12345678-1234-1234-1234-123456789012')
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_session_logger_request.DeleteSessionLoggerRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_session_logger_response.DeleteSessionLoggerResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_session_logger

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_session_logger.delete_session_logger(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_session_logger_request.DeleteSessionLoggerRequest = {
            "session_logger_arn": session_logger_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_session_loggers(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_session_loggers_response.ListSessionLoggersResponse":
        """<p>Lists all available session logger resources.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List All Session Loggers
            Lists all session loggers in the account without pagination

            >>> client.list_session_loggers()
            List Session Loggers with Pagination
            Lists session loggers with pagination parameters

            >>> client.list_session_loggers(max_results=1, next_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_session_loggers_request.ListSessionLoggersRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_session_loggers_response.ListSessionLoggersResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_session_loggers

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_session_loggers.list_session_loggers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_session_loggers_request.ListSessionLoggersRequest = {}
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

    def iter_list_session_loggers(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.session_logger_summary.SessionLoggerSummary]":
        _token = next_token
        while True:
            _response = self.list_session_loggers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("session_loggers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_trust_store(
        self,
        certificate_list: "capo_workspaces_web.types.certificate_list.CertificateList",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_workspaces_web.types.create_trust_store_response.CreateTrustStoreResponse"
    ):
        """<p>Creates a trust store that can be associated with a web portal. A trust store contains certificate authority (CA) certificates. Once associated with a web portal, the browser in a streaming session will recognize certificates that have been issued using any of the CAs in the trust store. If your organization has internal websites that use certificates issued by private CAs, you should add the private CA certificate to the trust store. </p>

        Args:
            certificate_list: <p>A list of CA certificates to be added to the trust store.</p>
            tags: <p>The tags to add to the trust store. A tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.create_trust_store_request.CreateTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_trust_store_response.CreateTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_trust_store

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_trust_store.create_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_trust_store_request.CreateTrustStoreRequest = {
            "certificate_list": certificate_list
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_trust_store(
        self,
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_trust_store_response.GetTrustStoreResponse":
        """<p>Gets the trust store.</p>

        Args:
            trust_store_arn: <p>The ARN of the trust store.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_trust_store_request.GetTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_trust_store_response.GetTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_trust_store

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_trust_store.get_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_trust_store_request.GetTrustStoreRequest = {
            "trust_store_arn": trust_store_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_trust_store(
        self,
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        certificates_to_add: Optional[
            "capo_workspaces_web.types.certificate_list.CertificateList"
        ] = None,
        certificates_to_delete: Optional[
            "capo_workspaces_web.types.certificate_thumbprint_list.CertificateThumbprintList"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> (
        "capo_workspaces_web.types.update_trust_store_response.UpdateTrustStoreResponse"
    ):
        """<p>Updates the trust store.</p>

        Args:
            trust_store_arn: <p>The ARN of the trust store.</p>
            certificates_to_add: <p>A list of CA certificates to add to the trust store.</p>
            certificates_to_delete: <p>A list of CA certificates to delete from a trust store.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_trust_store_request.UpdateTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_trust_store_response.UpdateTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_trust_store

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_trust_store.update_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_trust_store_request.UpdateTrustStoreRequest = {
            "trust_store_arn": trust_store_arn
        }
        if certificates_to_add is not None:
            input_["certificates_to_add"] = certificates_to_add
        if certificates_to_delete is not None:
            input_["certificates_to_delete"] = certificates_to_delete
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_trust_store(
        self,
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> (
        "capo_workspaces_web.types.delete_trust_store_response.DeleteTrustStoreResponse"
    ):
        """<p>Deletes the trust store.</p>

        Args:
            trust_store_arn: <p>The ARN of the trust store.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_trust_store_request.DeleteTrustStoreRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_trust_store_response.DeleteTrustStoreResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_trust_store

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_trust_store.delete_trust_store(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_trust_store_request.DeleteTrustStoreRequest = {
            "trust_store_arn": trust_store_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_trust_stores(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_trust_stores_response.ListTrustStoresResponse":
        """<p>Retrieves a list of trust stores.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_trust_stores_request.ListTrustStoresRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_trust_stores_response.ListTrustStoresResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_trust_stores

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_trust_stores.list_trust_stores(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_trust_stores_request.ListTrustStoresRequest = {}
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

    def iter_list_trust_stores(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_trust_stores_response.ListTrustStoresResponse]":
        _token = next_token
        while True:
            _response = self.list_trust_stores(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_trust_store_certificate(
        self,
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        thumbprint: "capo_workspaces_web.types.certificate_thumbprint.CertificateThumbprint",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_trust_store_certificate_response.GetTrustStoreCertificateResponse":
        """<p>Gets the trust store certificate.</p>

        Args:
            trust_store_arn: <p>The ARN of the trust store certificate.</p>
            thumbprint: <p>The thumbprint of the trust store certificate.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_trust_store_certificate_request.GetTrustStoreCertificateRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_trust_store_certificate_response.GetTrustStoreCertificateResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_trust_store_certificate

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_trust_store_certificate.get_trust_store_certificate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_trust_store_certificate_request.GetTrustStoreCertificateRequest = {
            "trust_store_arn": trust_store_arn,
            "thumbprint": thumbprint,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_trust_store_certificates(
        self,
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_trust_store_certificates_response.ListTrustStoreCertificatesResponse":
        """<p>Retrieves a list of trust store certificates.</p>

        Args:
            trust_store_arn: <p>The ARN of the trust store</p>
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_trust_store_certificates_request.ListTrustStoreCertificatesRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_trust_store_certificates_response.ListTrustStoreCertificatesResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_trust_store_certificates

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_trust_store_certificates.list_trust_store_certificates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_trust_store_certificates_request.ListTrustStoreCertificatesRequest = {
            "trust_store_arn": trust_store_arn
        }
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

    def iter_list_trust_store_certificates(
        self,
        trust_store_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_trust_store_certificates_response.ListTrustStoreCertificatesResponse]":
        _token = next_token
        while True:
            _response = self.list_trust_store_certificates(
                trust_store_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_user_access_logging_settings(
        self,
        kinesis_stream_arn: "capo_workspaces_web.types.kinesis_stream_arn.KinesisStreamArn",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        tags: Optional["capo_workspaces_web.types.tag_list.TagList"] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.create_user_access_logging_settings_response.CreateUserAccessLoggingSettingsResponse":
        """<p>Creates a user access logging settings resource that can be associated with a web portal.</p>

        Args:
            kinesis_stream_arn: <p>The ARN of the Kinesis stream.</p>
            tags: <p>The tags to add to the user settings resource. A tag is a key-value pair.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token returns the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.create_user_access_logging_settings_request.CreateUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.create_user_access_logging_settings_response.CreateUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.create_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.create_user_access_logging_settings.create_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.create_user_access_logging_settings_request.CreateUserAccessLoggingSettingsRequest = {
            "kinesis_stream_arn": kinesis_stream_arn
        }
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user_access_logging_settings(
        self,
        user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.get_user_access_logging_settings_response.GetUserAccessLoggingSettingsResponse":
        """<p>Gets user access logging settings.</p>

        Args:
            user_access_logging_settings_arn: <p>The ARN of the user access logging settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.get_user_access_logging_settings_request.GetUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.get_user_access_logging_settings_response.GetUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.get_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.get_user_access_logging_settings.get_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.get_user_access_logging_settings_request.GetUserAccessLoggingSettingsRequest = {
            "user_access_logging_settings_arn": user_access_logging_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user_access_logging_settings(
        self,
        user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        kinesis_stream_arn: Optional[
            "capo_workspaces_web.types.kinesis_stream_arn.KinesisStreamArn"
        ] = None,
        client_token: Optional[
            "capo_workspaces_web.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_workspaces_web.types.update_user_access_logging_settings_response.UpdateUserAccessLoggingSettingsResponse":
        """<p>Updates the user access logging settings.</p>

        Args:
            user_access_logging_settings_arn: <p>The ARN of the user access logging settings.</p>
            kinesis_stream_arn: <p>The ARN of the Kinesis stream.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, subsequent retries with the same client token return the result from the original successful request. </p> <p>If you do not specify a client token, one is automatically generated by the Amazon Web Services SDK.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource cannot be found.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.update_user_access_logging_settings_request.UpdateUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.update_user_access_logging_settings_response.UpdateUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.update_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.update_user_access_logging_settings.update_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.update_user_access_logging_settings_request.UpdateUserAccessLoggingSettingsRequest = {
            "user_access_logging_settings_arn": user_access_logging_settings_arn
        }
        if kinesis_stream_arn is not None:
            input_["kinesis_stream_arn"] = kinesis_stream_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user_access_logging_settings(
        self,
        user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN",
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
    ) -> "capo_workspaces_web.types.delete_user_access_logging_settings_response.DeleteUserAccessLoggingSettingsResponse":
        """<p>Deletes user access logging settings.</p>

        Args:
            user_access_logging_settings_arn: <p>The ARN of the user access logging settings.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.conflict_exception.ConflictException: <p>There is a conflict.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.delete_user_access_logging_settings_request.DeleteUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.delete_user_access_logging_settings_response.DeleteUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.delete_user_access_logging_settings.delete_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.delete_user_access_logging_settings_request.DeleteUserAccessLoggingSettingsRequest = {
            "user_access_logging_settings_arn": user_access_logging_settings_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_user_access_logging_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_workspaces_web.types.list_user_access_logging_settings_response.ListUserAccessLoggingSettingsResponse":
        """<p>Retrieves a list of user access logging settings.</p>

        Args:
            next_token: <p>The pagination token used to retrieve the next page of results for this operation.</p>
            max_results: <p>The maximum number of results to be included in the next page.</p>

        Raises:
            capo_workspaces_web.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_workspaces_web.errors.internal_server_exception.InternalServerException: <p>There is an internal server error.</p>
            capo_workspaces_web.errors.throttling_exception.ThrottlingException: <p>There is a throttling error.</p>
            capo_workspaces_web.errors.validation_exception.ValidationException: <p>There is a validation error.</p>
            capo_workspaces_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces_web.types.list_user_access_logging_settings_request.ListUserAccessLoggingSettingsRequest]",
        ) -> OperationResponse[
            "capo_workspaces_web.types.list_user_access_logging_settings_response.ListUserAccessLoggingSettingsResponse"
        ]:
            import capo_workspaces_web._operations.aws_ermine_control_plane_service.list_user_access_logging_settings

            output, http_response = (
                capo_workspaces_web._operations.aws_ermine_control_plane_service.list_user_access_logging_settings.list_user_access_logging_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces_web.types.list_user_access_logging_settings_request.ListUserAccessLoggingSettingsRequest = {}
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

    def iter_list_user_access_logging_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_user_access_logging_settings_response.ListUserAccessLoggingSettingsResponse]":
        _token = next_token
        while True:
            _response = self.list_user_access_logging_settings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_user_settings(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def get_user_settings(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def update_user_settings(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def delete_user_settings(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def list_user_settings(
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

        interceptors_, options_ = self.operation_options(config_overrides)
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

    def iter_list_user_settings(
        self,
        *,
        config_overrides: Optional[WorkSpacesWebClientConfig] = None,
        next_token: Optional[
            "capo_workspaces_web.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_workspaces_web.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_workspaces_web.types.list_user_settings_response.ListUserSettingsResponse]":
        _token = next_token
        while True:
            _response = self.list_user_settings(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
