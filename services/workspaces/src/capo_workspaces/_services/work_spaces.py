"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_workspaces._auth._signers
import capo_workspaces._auth._sigv4
from capo_workspaces._auth._identity import Credentials
from capo_workspaces._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_workspaces._auth._zapros_handler import AuthMiddleware
from capo_workspaces._pagination import resolve_path as _resolve_path
from capo_workspaces._services._aws_config import aws_config
from capo_workspaces._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_workspaces.types.accept_account_link_invitation_request
    import capo_workspaces.types.accept_account_link_invitation_result
    import capo_workspaces.types.account_link
    import capo_workspaces.types.active_directory_config
    import capo_workspaces.types.add_in_name
    import capo_workspaces.types.add_in_url
    import capo_workspaces.types.amazon_uuid
    import capo_workspaces.types.application_associated_resource_type_list
    import capo_workspaces.types.application_list
    import capo_workspaces.types.application_settings_request
    import capo_workspaces.types.arn
    import capo_workspaces.types.associate_connection_alias_request
    import capo_workspaces.types.associate_connection_alias_result
    import capo_workspaces.types.associate_ip_groups_request
    import capo_workspaces.types.associate_ip_groups_result
    import capo_workspaces.types.associate_workspace_application_request
    import capo_workspaces.types.associate_workspace_application_result
    import capo_workspaces.types.authorize_ip_rules_request
    import capo_workspaces.types.authorize_ip_rules_result
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.bundle_associated_resource_type_list
    import capo_workspaces.types.bundle_id
    import capo_workspaces.types.bundle_id_list
    import capo_workspaces.types.bundle_owner
    import capo_workspaces.types.capacity
    import capo_workspaces.types.certificate_based_auth_properties
    import capo_workspaces.types.client_device_type_list
    import capo_workspaces.types.client_properties
    import capo_workspaces.types.client_token
    import capo_workspaces.types.compute_list
    import capo_workspaces.types.compute_type
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.connection_alias_id_list
    import capo_workspaces.types.connection_alias_permission
    import capo_workspaces.types.connection_string
    import capo_workspaces.types.copy_workspace_image_request
    import capo_workspaces.types.copy_workspace_image_result
    import capo_workspaces.types.create_account_link_invitation_request
    import capo_workspaces.types.create_account_link_invitation_result
    import capo_workspaces.types.create_connect_client_add_in_request
    import capo_workspaces.types.create_connect_client_add_in_result
    import capo_workspaces.types.create_connection_alias_request
    import capo_workspaces.types.create_connection_alias_result
    import capo_workspaces.types.create_ip_group_request
    import capo_workspaces.types.create_ip_group_result
    import capo_workspaces.types.create_standby_workspaces_request
    import capo_workspaces.types.create_standby_workspaces_result
    import capo_workspaces.types.create_tags_request
    import capo_workspaces.types.create_tags_result
    import capo_workspaces.types.create_updated_workspace_image_request
    import capo_workspaces.types.create_updated_workspace_image_result
    import capo_workspaces.types.create_workspace_bundle_request
    import capo_workspaces.types.create_workspace_bundle_result
    import capo_workspaces.types.create_workspace_image_request
    import capo_workspaces.types.create_workspace_image_result
    import capo_workspaces.types.create_workspaces_pool_request
    import capo_workspaces.types.create_workspaces_pool_result
    import capo_workspaces.types.create_workspaces_request
    import capo_workspaces.types.create_workspaces_result
    import capo_workspaces.types.custom_image_protocol
    import capo_workspaces.types.data_replication
    import capo_workspaces.types.dedicated_tenancy_management_cidr_range
    import capo_workspaces.types.dedicated_tenancy_support_enum
    import capo_workspaces.types.default_import_client_branding_attributes
    import capo_workspaces.types.deletable_certificate_based_auth_properties_list
    import capo_workspaces.types.deletable_saml_properties_list
    import capo_workspaces.types.delete_account_link_invitation_request
    import capo_workspaces.types.delete_account_link_invitation_result
    import capo_workspaces.types.delete_client_branding_request
    import capo_workspaces.types.delete_client_branding_result
    import capo_workspaces.types.delete_connect_client_add_in_request
    import capo_workspaces.types.delete_connect_client_add_in_result
    import capo_workspaces.types.delete_connection_alias_request
    import capo_workspaces.types.delete_connection_alias_result
    import capo_workspaces.types.delete_ip_group_request
    import capo_workspaces.types.delete_ip_group_result
    import capo_workspaces.types.delete_tags_request
    import capo_workspaces.types.delete_tags_result
    import capo_workspaces.types.delete_workspace_bundle_request
    import capo_workspaces.types.delete_workspace_bundle_result
    import capo_workspaces.types.delete_workspace_image_request
    import capo_workspaces.types.delete_workspace_image_result
    import capo_workspaces.types.deploy_workspace_applications_request
    import capo_workspaces.types.deploy_workspace_applications_result
    import capo_workspaces.types.deregister_workspace_directory_request
    import capo_workspaces.types.deregister_workspace_directory_result
    import capo_workspaces.types.describe_account_modifications_request
    import capo_workspaces.types.describe_account_modifications_result
    import capo_workspaces.types.describe_account_request
    import capo_workspaces.types.describe_account_result
    import capo_workspaces.types.describe_application_associations_request
    import capo_workspaces.types.describe_application_associations_result
    import capo_workspaces.types.describe_applications_request
    import capo_workspaces.types.describe_applications_result
    import capo_workspaces.types.describe_bundle_associations_request
    import capo_workspaces.types.describe_bundle_associations_result
    import capo_workspaces.types.describe_client_branding_request
    import capo_workspaces.types.describe_client_branding_result
    import capo_workspaces.types.describe_client_properties_request
    import capo_workspaces.types.describe_client_properties_result
    import capo_workspaces.types.describe_connect_client_add_ins_request
    import capo_workspaces.types.describe_connect_client_add_ins_result
    import capo_workspaces.types.describe_connection_alias_permissions_request
    import capo_workspaces.types.describe_connection_alias_permissions_result
    import capo_workspaces.types.describe_connection_aliases_request
    import capo_workspaces.types.describe_connection_aliases_result
    import capo_workspaces.types.describe_custom_workspace_image_import_request
    import capo_workspaces.types.describe_custom_workspace_image_import_result
    import capo_workspaces.types.describe_image_associations_request
    import capo_workspaces.types.describe_image_associations_result
    import capo_workspaces.types.describe_ip_groups_request
    import capo_workspaces.types.describe_ip_groups_result
    import capo_workspaces.types.describe_tags_request
    import capo_workspaces.types.describe_tags_result
    import capo_workspaces.types.describe_workspace_associations_request
    import capo_workspaces.types.describe_workspace_associations_result
    import capo_workspaces.types.describe_workspace_bundles_request
    import capo_workspaces.types.describe_workspace_bundles_result
    import capo_workspaces.types.describe_workspace_directories_filter_list
    import capo_workspaces.types.describe_workspace_directories_request
    import capo_workspaces.types.describe_workspace_directories_result
    import capo_workspaces.types.describe_workspace_image_permissions_request
    import capo_workspaces.types.describe_workspace_image_permissions_result
    import capo_workspaces.types.describe_workspace_images_request
    import capo_workspaces.types.describe_workspace_images_result
    import capo_workspaces.types.describe_workspace_snapshots_request
    import capo_workspaces.types.describe_workspace_snapshots_result
    import capo_workspaces.types.describe_workspaces_connection_status_request
    import capo_workspaces.types.describe_workspaces_connection_status_result
    import capo_workspaces.types.describe_workspaces_pool_sessions_request
    import capo_workspaces.types.describe_workspaces_pool_sessions_result
    import capo_workspaces.types.describe_workspaces_pools_filters
    import capo_workspaces.types.describe_workspaces_pools_request
    import capo_workspaces.types.describe_workspaces_pools_result
    import capo_workspaces.types.describe_workspaces_request
    import capo_workspaces.types.describe_workspaces_result
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.directory_id_list
    import capo_workspaces.types.disassociate_connection_alias_request
    import capo_workspaces.types.disassociate_connection_alias_result
    import capo_workspaces.types.disassociate_ip_groups_request
    import capo_workspaces.types.disassociate_ip_groups_result
    import capo_workspaces.types.disassociate_workspace_application_request
    import capo_workspaces.types.disassociate_workspace_application_result
    import capo_workspaces.types.ec2_image_id
    import capo_workspaces.types.endpoint_encryption_mode
    import capo_workspaces.types.get_account_link_request
    import capo_workspaces.types.get_account_link_result
    import capo_workspaces.types.image_associated_resource_type_list
    import capo_workspaces.types.image_compute_type
    import capo_workspaces.types.image_source_identifier
    import capo_workspaces.types.image_type
    import capo_workspaces.types.import_client_branding_request
    import capo_workspaces.types.import_client_branding_result
    import capo_workspaces.types.import_custom_workspace_image_request
    import capo_workspaces.types.import_custom_workspace_image_result
    import capo_workspaces.types.import_workspace_image_request
    import capo_workspaces.types.import_workspace_image_result
    import capo_workspaces.types.infrastructure_configuration_arn
    import capo_workspaces.types.ios_import_client_branding_attributes
    import capo_workspaces.types.ip_group_desc
    import capo_workspaces.types.ip_group_id
    import capo_workspaces.types.ip_group_id_list
    import capo_workspaces.types.ip_group_name
    import capo_workspaces.types.ip_revoked_rule_list
    import capo_workspaces.types.ip_rule_list
    import capo_workspaces.types.limit
    import capo_workspaces.types.limit50
    import capo_workspaces.types.link_id
    import capo_workspaces.types.link_status_filter_list
    import capo_workspaces.types.list_account_links_request
    import capo_workspaces.types.list_account_links_result
    import capo_workspaces.types.list_available_management_cidr_ranges_request
    import capo_workspaces.types.list_available_management_cidr_ranges_result
    import capo_workspaces.types.management_cidr_range_constraint
    import capo_workspaces.types.management_cidr_range_max_results
    import capo_workspaces.types.microsoft_entra_config
    import capo_workspaces.types.migrate_workspace_request
    import capo_workspaces.types.migrate_workspace_result
    import capo_workspaces.types.modify_account_request
    import capo_workspaces.types.modify_account_result
    import capo_workspaces.types.modify_certificate_based_auth_properties_request
    import capo_workspaces.types.modify_certificate_based_auth_properties_result
    import capo_workspaces.types.modify_client_properties_request
    import capo_workspaces.types.modify_client_properties_result
    import capo_workspaces.types.modify_endpoint_encryption_mode_request
    import capo_workspaces.types.modify_endpoint_encryption_mode_response
    import capo_workspaces.types.modify_saml_properties_request
    import capo_workspaces.types.modify_saml_properties_result
    import capo_workspaces.types.modify_selfservice_permissions_request
    import capo_workspaces.types.modify_selfservice_permissions_result
    import capo_workspaces.types.modify_streaming_properties_request
    import capo_workspaces.types.modify_streaming_properties_result
    import capo_workspaces.types.modify_workspace_access_properties_request
    import capo_workspaces.types.modify_workspace_access_properties_result
    import capo_workspaces.types.modify_workspace_creation_properties_request
    import capo_workspaces.types.modify_workspace_creation_properties_result
    import capo_workspaces.types.modify_workspace_properties_request
    import capo_workspaces.types.modify_workspace_properties_result
    import capo_workspaces.types.modify_workspace_state_request
    import capo_workspaces.types.modify_workspace_state_result
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.operating_system_name_list
    import capo_workspaces.types.os_version
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.platform
    import capo_workspaces.types.pools_running_mode
    import capo_workspaces.types.reboot_workspace_requests
    import capo_workspaces.types.reboot_workspaces_request
    import capo_workspaces.types.reboot_workspaces_result
    import capo_workspaces.types.rebuild_workspace_requests
    import capo_workspaces.types.rebuild_workspaces_request
    import capo_workspaces.types.rebuild_workspaces_result
    import capo_workspaces.types.region
    import capo_workspaces.types.register_workspace_directory_request
    import capo_workspaces.types.register_workspace_directory_result
    import capo_workspaces.types.reject_account_link_invitation_request
    import capo_workspaces.types.reject_account_link_invitation_result
    import capo_workspaces.types.resource_id_list
    import capo_workspaces.types.restore_workspace_request
    import capo_workspaces.types.restore_workspace_result
    import capo_workspaces.types.revoke_ip_rules_request
    import capo_workspaces.types.revoke_ip_rules_result
    import capo_workspaces.types.root_storage
    import capo_workspaces.types.saml_properties
    import capo_workspaces.types.selfservice_permissions
    import capo_workspaces.types.standby_workspaces_list
    import capo_workspaces.types.start_workspace_requests
    import capo_workspaces.types.start_workspaces_pool_request
    import capo_workspaces.types.start_workspaces_pool_result
    import capo_workspaces.types.start_workspaces_request
    import capo_workspaces.types.start_workspaces_result
    import capo_workspaces.types.stop_workspace_requests
    import capo_workspaces.types.stop_workspaces_pool_request
    import capo_workspaces.types.stop_workspaces_pool_result
    import capo_workspaces.types.stop_workspaces_request
    import capo_workspaces.types.stop_workspaces_result
    import capo_workspaces.types.streaming_properties
    import capo_workspaces.types.subnet_ids
    import capo_workspaces.types.tag_key_list
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.target_workspace_state
    import capo_workspaces.types.tenancy
    import capo_workspaces.types.terminate_workspace_requests
    import capo_workspaces.types.terminate_workspaces_pool_request
    import capo_workspaces.types.terminate_workspaces_pool_result
    import capo_workspaces.types.terminate_workspaces_pool_session_request
    import capo_workspaces.types.terminate_workspaces_pool_session_result
    import capo_workspaces.types.terminate_workspaces_request
    import capo_workspaces.types.terminate_workspaces_result
    import capo_workspaces.types.timeout_settings
    import capo_workspaces.types.update_connect_client_add_in_request
    import capo_workspaces.types.update_connect_client_add_in_result
    import capo_workspaces.types.update_connection_alias_permission_request
    import capo_workspaces.types.update_connection_alias_permission_result
    import capo_workspaces.types.update_description
    import capo_workspaces.types.update_rules_of_ip_group_request
    import capo_workspaces.types.update_rules_of_ip_group_result
    import capo_workspaces.types.update_workspace_bundle_request
    import capo_workspaces.types.update_workspace_bundle_result
    import capo_workspaces.types.update_workspace_image_permission_request
    import capo_workspaces.types.update_workspace_image_permission_result
    import capo_workspaces.types.update_workspaces_pool_request
    import capo_workspaces.types.update_workspaces_pool_result
    import capo_workspaces.types.user_identity_type
    import capo_workspaces.types.user_name
    import capo_workspaces.types.user_storage
    import capo_workspaces.types.work_space_application_id
    import capo_workspaces.types.work_space_application_id_list
    import capo_workspaces.types.work_space_application_license_type
    import capo_workspaces.types.work_space_application_owner
    import capo_workspaces.types.work_space_associated_resource_type_list
    import capo_workspaces.types.workspace
    import capo_workspaces.types.workspace_access_properties
    import capo_workspaces.types.workspace_bundle
    import capo_workspaces.types.workspace_bundle_description
    import capo_workspaces.types.workspace_bundle_name
    import capo_workspaces.types.workspace_creation_properties
    import capo_workspaces.types.workspace_directory
    import capo_workspaces.types.workspace_directory_description
    import capo_workspaces.types.workspace_directory_name
    import capo_workspaces.types.workspace_directory_name_list
    import capo_workspaces.types.workspace_id
    import capo_workspaces.types.workspace_id_list
    import capo_workspaces.types.workspace_image_description
    import capo_workspaces.types.workspace_image_id
    import capo_workspaces.types.workspace_image_id_list
    import capo_workspaces.types.workspace_image_ingestion_process
    import capo_workspaces.types.workspace_image_name
    import capo_workspaces.types.workspace_name
    import capo_workspaces.types.workspace_properties
    import capo_workspaces.types.workspace_request_list
    import capo_workspaces.types.workspace_type
    import capo_workspaces.types.workspaces_pool_id
    import capo_workspaces.types.workspaces_pool_ids
    import capo_workspaces.types.workspaces_pool_name
    import capo_workspaces.types.workspaces_pool_user_id


class WorkSpacesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class WorkSpacesClient:
    """A client for the ``WorkSpaces`` service.

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
        self._config = WorkSpacesClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[WorkSpacesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: WorkSpacesClientConfig = config_overrides or {}
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

    def accept_account_link_invitation(
        self,
        link_id: "capo_workspaces.types.link_id.LinkId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        client_token: Optional["capo_workspaces.types.client_token.ClientToken"] = None,
    ) -> "capo_workspaces.types.accept_account_link_invitation_result.AcceptAccountLinkInvitationResult":
        """<p>Accepts the account link invitation.</p> <important> <p>There's currently no unlinking capability after you accept the account linking invitation.</p> </important>

        Args:
            link_id: <p>The identifier of the account link.</p>
            client_token: <p>A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.conflict_exception.ConflictException: <p>The <code>TargetAccountId</code> is already linked or invited.</p>
            capo_workspaces.errors.internal_server_exception.InternalServerException: <p>Unexpected server error occured.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.validation_exception.ValidationException: <p>You either haven't provided a <code>TargetAccountId</code> or are using the same value for <code>TargetAccountId</code> and <code>SourceAccountId</code>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.accept_account_link_invitation_request.AcceptAccountLinkInvitationRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.accept_account_link_invitation_result.AcceptAccountLinkInvitationResult"
        ]:
            import capo_workspaces._operations.workspaces_service.accept_account_link_invitation

            output, http_response = (
                capo_workspaces._operations.workspaces_service.accept_account_link_invitation.accept_account_link_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.accept_account_link_invitation_request.AcceptAccountLinkInvitationRequest = {
            "link_id": link_id
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_connection_alias(
        self,
        alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId",
        resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.associate_connection_alias_result.AssociateConnectionAliasResult":
        """<p>Associates the specified connection alias with the specified directory to enable cross-Region redirection. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p> <note> <p>Before performing this operation, call <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html"> DescribeConnectionAliases</a> to make sure that the current state of the connection alias is <code>CREATED</code>.</p> </note>

        Args:
            alias_id: <p>The identifier of the connection alias.</p>
            resource_id: <p>The identifier of the directory to associate the connection alias with.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_associated_exception.ResourceAssociatedException: <p>The resource is associated with a directory.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.associate_connection_alias_request.AssociateConnectionAliasRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.associate_connection_alias_result.AssociateConnectionAliasResult"
        ]:
            import capo_workspaces._operations.workspaces_service.associate_connection_alias

            output, http_response = (
                capo_workspaces._operations.workspaces_service.associate_connection_alias.associate_connection_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.associate_connection_alias_request.AssociateConnectionAliasRequest = {
            "alias_id": alias_id,
            "resource_id": resource_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_ip_groups(
        self,
        directory_id: "capo_workspaces.types.directory_id.DirectoryId",
        group_ids: "capo_workspaces.types.ip_group_id_list.IpGroupIdList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.associate_ip_groups_result.AssociateIpGroupsResult":
        """<p>Associates the specified IP access control group with the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            group_ids: <p>The identifiers of one or more IP access control groups.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.associate_ip_groups_request.AssociateIpGroupsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.associate_ip_groups_result.AssociateIpGroupsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.associate_ip_groups

            output, http_response = (
                capo_workspaces._operations.workspaces_service.associate_ip_groups.associate_ip_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.associate_ip_groups_request.AssociateIpGroupsRequest = {
            "directory_id": directory_id,
            "group_ids": group_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_workspace_application(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        application_id: "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.associate_workspace_application_result.AssociateWorkspaceApplicationResult":
        """<p>Associates the specified application to the specified WorkSpace.</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>
            application_id: <p>The identifier of the application.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.application_not_supported_exception.ApplicationNotSupportedException: <p>The specified application is not supported.</p>
            capo_workspaces.errors.compute_not_compatible_exception.ComputeNotCompatibleException: <p>The compute type of the WorkSpace is not compatible with the application.</p>
            capo_workspaces.errors.incompatible_applications_exception.IncompatibleApplicationsException: <p>The specified application is not compatible with the resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operating_system_not_compatible_exception.OperatingSystemNotCompatibleException: <p>The operating system of the WorkSpace is not compatible with the application.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is currently in use.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.associate_workspace_application_request.AssociateWorkspaceApplicationRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.associate_workspace_application_result.AssociateWorkspaceApplicationResult"
        ]:
            import capo_workspaces._operations.workspaces_service.associate_workspace_application

            output, http_response = (
                capo_workspaces._operations.workspaces_service.associate_workspace_application.associate_workspace_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.associate_workspace_application_request.AssociateWorkspaceApplicationRequest = {
            "workspace_id": workspace_id,
            "application_id": application_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def authorize_ip_rules(
        self,
        group_id: "capo_workspaces.types.ip_group_id.IpGroupId",
        user_rules: "capo_workspaces.types.ip_rule_list.IpRuleList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.authorize_ip_rules_result.AuthorizeIpRulesResult":
        """<p>Adds one or more rules to the specified IP access control group.</p> <p>This action gives users permission to access their WorkSpaces from the CIDR address ranges specified in the rules.</p>

        Args:
            group_id: <p>The identifier of the group.</p>
            user_rules: <p>The rules to add to the group.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.authorize_ip_rules_request.AuthorizeIpRulesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.authorize_ip_rules_result.AuthorizeIpRulesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.authorize_ip_rules

            output, http_response = (
                capo_workspaces._operations.workspaces_service.authorize_ip_rules.authorize_ip_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.authorize_ip_rules_request.AuthorizeIpRulesRequest = {
            "group_id": group_id,
            "user_rules": user_rules,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_workspace_image(
        self,
        name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName",
        source_image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        source_region: "capo_workspaces.types.region.Region",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        description: Optional[
            "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription"
        ] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces.types.copy_workspace_image_result.CopyWorkspaceImageResult":
        """<p>Copies the specified image from the specified Region to the current Region. For more information about copying images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/copy-custom-image.html"> Copy a Custom WorkSpaces Image</a>.</p> <p>In the China (Ningxia) Region, you can copy images only within the same Region.</p> <p>In Amazon Web Services GovCloud (US), to copy images to and from other Regions, contact Amazon Web Services Support.</p> <important> <p>Before copying a shared image, be sure to verify that it has been shared from the correct Amazon Web Services account. To determine if an image has been shared and to see the ID of the Amazon Web Services account that owns an image, use the <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html">DescribeWorkSpaceImages</a> and <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImagePermissions.html">DescribeWorkspaceImagePermissions</a> API operations. </p> </important>

        Args:
            name: <p>The name of the image.</p>
            description: <p>A description of the image.</p>
            source_image_id: <p>The identifier of the source image.</p>
            source_region: <p>The identifier of the source Region.</p>
            tags: <p>The tags for the image.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.copy_workspace_image_request.CopyWorkspaceImageRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.copy_workspace_image_result.CopyWorkspaceImageResult"
        ]:
            import capo_workspaces._operations.workspaces_service.copy_workspace_image

            output, http_response = (
                capo_workspaces._operations.workspaces_service.copy_workspace_image.copy_workspace_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.copy_workspace_image_request.CopyWorkspaceImageRequest = {
            "name": name,
            "source_image_id": source_image_id,
            "source_region": source_region,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_account_link_invitation(
        self,
        target_account_id: "capo_workspaces.types.aws_account.AwsAccount",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        client_token: Optional["capo_workspaces.types.client_token.ClientToken"] = None,
    ) -> "capo_workspaces.types.create_account_link_invitation_result.CreateAccountLinkInvitationResult":
        """<p>Creates the account link invitation.</p>

        Args:
            target_account_id: <p>The identifier of the target account.</p>
            client_token: <p>A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.conflict_exception.ConflictException: <p>The <code>TargetAccountId</code> is already linked or invited.</p>
            capo_workspaces.errors.internal_server_exception.InternalServerException: <p>Unexpected server error occured.</p>
            capo_workspaces.errors.validation_exception.ValidationException: <p>You either haven't provided a <code>TargetAccountId</code> or are using the same value for <code>TargetAccountId</code> and <code>SourceAccountId</code>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_account_link_invitation_request.CreateAccountLinkInvitationRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_account_link_invitation_result.CreateAccountLinkInvitationResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_account_link_invitation

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_account_link_invitation.create_account_link_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_account_link_invitation_request.CreateAccountLinkInvitationRequest = {
            "target_account_id": target_account_id
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connect_client_add_in(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        name: "capo_workspaces.types.add_in_name.AddInName",
        url: "capo_workspaces.types.add_in_url.AddInUrl",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.create_connect_client_add_in_result.CreateConnectClientAddInResult":
        """<p>Creates a client-add-in for Connect Customer within a directory. You can create only one Connect Customer client add-in within a directory.</p> <p>This client add-in allows WorkSpaces users to seamlessly connect to Connect Customer.</p>

        Args:
            resource_id: <p>The directory identifier for which to configure the client add-in.</p>
            name: <p>The name of the client add-in.</p>
            url: <p>The endpoint URL of the Connect Customer client add-in.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_creation_failed_exception.ResourceCreationFailedException: <p>The resource could not be created.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_connect_client_add_in_request.CreateConnectClientAddInRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_connect_client_add_in_result.CreateConnectClientAddInResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_connect_client_add_in

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_connect_client_add_in.create_connect_client_add_in(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_connect_client_add_in_request.CreateConnectClientAddInRequest = {
            "resource_id": resource_id,
            "name": name,
            "url": url,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connection_alias(
        self,
        connection_string: "capo_workspaces.types.connection_string.ConnectionString",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces.types.create_connection_alias_result.CreateConnectionAliasResult":
        """<p>Creates the specified connection alias for use with cross-Region redirection. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p>

        Args:
            connection_string: <p>A connection string in the form of a fully qualified domain name (FQDN), such as <code>www.example.com</code>.</p> <important> <p>After you create a connection string, it is always associated to your Amazon Web Services account. You cannot recreate the same connection string with a different account, even if you delete all instances of it from the original account. The connection string is globally reserved for your account.</p> </important>
            tags: <p>The tags to associate with the connection alias.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_connection_alias_request.CreateConnectionAliasRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_connection_alias_result.CreateConnectionAliasResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_connection_alias

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_connection_alias.create_connection_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_connection_alias_request.CreateConnectionAliasRequest = {
            "connection_string": connection_string
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_ip_group(
        self,
        group_name: "capo_workspaces.types.ip_group_name.IpGroupName",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        group_desc: Optional["capo_workspaces.types.ip_group_desc.IpGroupDesc"] = None,
        user_rules: Optional["capo_workspaces.types.ip_rule_list.IpRuleList"] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces.types.create_ip_group_result.CreateIpGroupResult":
        """<p>Creates an IP access control group.</p> <p>An IP access control group provides you with the ability to control the IP addresses from which users are allowed to access their WorkSpaces. To specify the CIDR address ranges, add rules to your IP access control group and then associate the group with your directory. You can add rules when you create the group or at any time using <a>AuthorizeIpRules</a>.</p> <p>There is a default IP access control group associated with your directory. If you don't associate an IP access control group with your directory, the default group is used. The default group includes a default rule that allows users to access their WorkSpaces from anywhere. You cannot modify the default IP access control group for your directory.</p>

        Args:
            group_name: <p>The name of the group.</p>
            group_desc: <p>The description of the group.</p>
            user_rules: <p>The rules to add to the group.</p>
            tags: <p>The tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_creation_failed_exception.ResourceCreationFailedException: <p>The resource could not be created.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_ip_group_request.CreateIpGroupRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_ip_group_result.CreateIpGroupResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_ip_group

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_ip_group.create_ip_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_ip_group_request.CreateIpGroupRequest = {
            "group_name": group_name
        }
        if group_desc is not None:
            input_["group_desc"] = group_desc
        if user_rules is not None:
            input_["user_rules"] = user_rules
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_standby_workspaces(
        self,
        primary_region: "capo_workspaces.types.region.Region",
        standby_workspaces: "capo_workspaces.types.standby_workspaces_list.StandbyWorkspacesList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.create_standby_workspaces_result.CreateStandbyWorkspacesResult":
        """<p>Creates a standby WorkSpace in a secondary Region.</p>

        Args:
            primary_region: <p>The Region of the primary WorkSpace.</p>
            standby_workspaces: <p>Information about the standby WorkSpace to be created.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_standby_workspaces_request.CreateStandbyWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_standby_workspaces_result.CreateStandbyWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_standby_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_standby_workspaces.create_standby_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_standby_workspaces_request.CreateStandbyWorkspacesRequest = {
            "primary_region": primary_region,
            "standby_workspaces": standby_workspaces,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tags(
        self,
        resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString",
        tags: "capo_workspaces.types.tag_list.TagList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.create_tags_result.CreateTagsResult":
        """<p>Creates the specified tags for the specified WorkSpaces resource.</p>

        Args:
            resource_id: <p>The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, IP access control groups, and connection aliases.</p>
            tags: <p>The tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_tags_request.CreateTagsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_tags_result.CreateTagsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_tags

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_tags.create_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_tags_request.CreateTagsRequest = {
            "resource_id": resource_id,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_updated_workspace_image(
        self,
        name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName",
        description: "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription",
        source_image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces.types.create_updated_workspace_image_result.CreateUpdatedWorkspaceImageResult":
        """<p>Creates a new updated WorkSpace image based on the specified source image. The new updated WorkSpace image has the latest drivers and other updates required by the Amazon WorkSpaces components.</p> <p>To determine which WorkSpace images need to be updated with the latest Amazon WorkSpaces requirements, use <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceImages.html"> DescribeWorkspaceImages</a>.</p> <note> <ul> <li> <p>Only Windows 10, Windows Server 2016, and Windows Server 2019 WorkSpace images can be programmatically updated at this time.</p> </li> <li> <p>Microsoft Windows updates and other application updates are not included in the update process.</p> </li> <li> <p>The source WorkSpace image is not deleted. You can delete the source image after you've verified your new updated image and created a new bundle. </p> </li> </ul> </note>

        Args:
            name: <p>The name of the new updated WorkSpace image.</p>
            description: <p>A description of whether updates for the WorkSpace image are available.</p>
            source_image_id: <p>The identifier of the source WorkSpace image.</p>
            tags: <p>The tags that you want to add to the new updated WorkSpace image.</p> <note> <p>To add tags at the same time when you're creating the updated image, you must create an IAM policy that grants your IAM user permissions to use <code>workspaces:CreateTags</code>. </p> </note>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_updated_workspace_image_request.CreateUpdatedWorkspaceImageRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_updated_workspace_image_result.CreateUpdatedWorkspaceImageResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_updated_workspace_image

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_updated_workspace_image.create_updated_workspace_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_updated_workspace_image_request.CreateUpdatedWorkspaceImageRequest = {
            "name": name,
            "description": description,
            "source_image_id": source_image_id,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspace_bundle(
        self,
        bundle_name: "capo_workspaces.types.workspace_bundle_name.WorkspaceBundleName",
        bundle_description: "capo_workspaces.types.workspace_bundle_description.WorkspaceBundleDescription",
        image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        compute_type: "capo_workspaces.types.compute_type.ComputeType",
        user_storage: "capo_workspaces.types.user_storage.UserStorage",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        root_storage: Optional["capo_workspaces.types.root_storage.RootStorage"] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces.types.create_workspace_bundle_result.CreateWorkspaceBundleResult":
        """<p>Creates the specified WorkSpace bundle. For more information about creating WorkSpace bundles, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/create-custom-bundle.html"> Create a Custom WorkSpaces Image and Bundle</a>.</p>

        Args:
            bundle_name: <p>The name of the bundle.</p>
            bundle_description: <p>The description of the bundle.</p>
            image_id: <p>The identifier of the image that is used to create the bundle.</p>
            tags: <p>The tags associated with the bundle.</p> <note> <p>To add tags at the same time when you're creating the bundle, you must create an IAM policy that grants your IAM user permissions to use <code>workspaces:CreateTags</code>. </p> </note>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_workspace_bundle_request.CreateWorkspaceBundleRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_workspace_bundle_result.CreateWorkspaceBundleResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_workspace_bundle

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_workspace_bundle.create_workspace_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_workspace_bundle_request.CreateWorkspaceBundleRequest = {
            "bundle_name": bundle_name,
            "bundle_description": bundle_description,
            "image_id": image_id,
            "compute_type": compute_type,
            "user_storage": user_storage,
        }
        if root_storage is not None:
            input_["root_storage"] = root_storage
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspace_image(
        self,
        name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName",
        description: "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription",
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> (
        "capo_workspaces.types.create_workspace_image_result.CreateWorkspaceImageResult"
    ):
        """<p>Creates a new WorkSpace image from an existing WorkSpace.</p>

        Args:
            name: <p>The name of the new WorkSpace image.</p>
            description: <p>The description of the new WorkSpace image.</p>
            workspace_id: <p>The identifier of the source WorkSpace</p>
            tags: <p>The tags that you want to add to the new WorkSpace image. To add tags when you're creating the image, you must create an IAM policy that grants your IAM user permission to use <code>workspaces:CreateTags</code>.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_workspace_image_request.CreateWorkspaceImageRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_workspace_image_result.CreateWorkspaceImageResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_workspace_image

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_workspace_image.create_workspace_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_workspace_image_request.CreateWorkspaceImageRequest = {
            "name": name,
            "description": description,
            "workspace_id": workspace_id,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspaces(
        self,
        workspaces: "capo_workspaces.types.workspace_request_list.WorkspaceRequestList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.create_workspaces_result.CreateWorkspacesResult":
        """<p>Creates one or more WorkSpaces.</p> <p>This operation is asynchronous and returns before the WorkSpaces are created.</p> <note> <ul> <li> <p>The <code>MANUAL</code> running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see <a href="http://aws.amazon.com/workspaces/core/">Amazon WorkSpaces Core</a>.</p> </li> <li> <p>You don't need to specify the <code>PCOIP</code> protocol for Linux bundles because <code>DCV</code> (formerly WSP) is the default protocol for those bundles.</p> </li> <li> <p>User-decoupled WorkSpaces are only supported by Amazon WorkSpaces Core.</p> </li> <li> <p>Review your running mode to ensure you are using one that is optimal for your needs and budget. For more information on switching running modes, see <a href="http://aws.amazon.com/workspaces-family/workspaces/faqs/#:~:text=Can%20I%20switch%20between%20hourly%20and%20monthly%20billing%20on%20WorkSpaces%20Personal%3F"> Can I switch between hourly and monthly billing?</a> </p> </li> </ul> </note>

        Args:
            workspaces: <p>The WorkSpaces to create. You can specify up to 25 WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_workspaces_request.CreateWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_workspaces_result.CreateWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_workspaces.create_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_workspaces_request.CreateWorkspacesRequest = {
            "workspaces": workspaces
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_workspaces_pool(
        self,
        pool_name: "capo_workspaces.types.workspaces_pool_name.WorkspacesPoolName",
        description: "capo_workspaces.types.update_description.UpdateDescription",
        bundle_id: "capo_workspaces.types.bundle_id.BundleId",
        directory_id: "capo_workspaces.types.directory_id.DirectoryId",
        capacity: "capo_workspaces.types.capacity.Capacity",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
        application_settings: Optional[
            "capo_workspaces.types.application_settings_request.ApplicationSettingsRequest"
        ] = None,
        timeout_settings: Optional[
            "capo_workspaces.types.timeout_settings.TimeoutSettings"
        ] = None,
        running_mode: Optional[
            "capo_workspaces.types.pools_running_mode.PoolsRunningMode"
        ] = None,
    ) -> (
        "capo_workspaces.types.create_workspaces_pool_result.CreateWorkspacesPoolResult"
    ):
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Creates a pool of WorkSpaces.</p>

        Args:
            pool_name: <p>The name of the pool.</p>
            description: <p>The pool description.</p>
            bundle_id: <p>The identifier of the bundle for the pool.</p>
            directory_id: <p>The identifier of the directory for the pool.</p>
            capacity: <p>The user capacity of the pool.</p>
            tags: <p>The tags for the pool.</p>
            application_settings: <p>Indicates the application settings of the pool.</p>
            timeout_settings: <p>Indicates the timeout settings of the pool.</p>
            running_mode: <p>The running mode for the pool.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.create_workspaces_pool_request.CreateWorkspacesPoolRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.create_workspaces_pool_result.CreateWorkspacesPoolResult"
        ]:
            import capo_workspaces._operations.workspaces_service.create_workspaces_pool

            output, http_response = (
                capo_workspaces._operations.workspaces_service.create_workspaces_pool.create_workspaces_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.create_workspaces_pool_request.CreateWorkspacesPoolRequest = {
            "pool_name": pool_name,
            "description": description,
            "bundle_id": bundle_id,
            "directory_id": directory_id,
            "capacity": capacity,
        }
        if tags is not None:
            input_["tags"] = tags
        if application_settings is not None:
            input_["application_settings"] = application_settings
        if timeout_settings is not None:
            input_["timeout_settings"] = timeout_settings
        if running_mode is not None:
            input_["running_mode"] = running_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_account_link_invitation(
        self,
        link_id: "capo_workspaces.types.link_id.LinkId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        client_token: Optional["capo_workspaces.types.client_token.ClientToken"] = None,
    ) -> "capo_workspaces.types.delete_account_link_invitation_result.DeleteAccountLinkInvitationResult":
        """<p>Deletes the account link invitation.</p>

        Args:
            link_id: <p>The identifier of the account link.</p>
            client_token: <p>A string of up to 64 ASCII characters that Amazon WorkSpaces uses to ensure idempotent creation.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.conflict_exception.ConflictException: <p>The <code>TargetAccountId</code> is already linked or invited.</p>
            capo_workspaces.errors.internal_server_exception.InternalServerException: <p>Unexpected server error occured.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.validation_exception.ValidationException: <p>You either haven't provided a <code>TargetAccountId</code> or are using the same value for <code>TargetAccountId</code> and <code>SourceAccountId</code>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_account_link_invitation_request.DeleteAccountLinkInvitationRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_account_link_invitation_result.DeleteAccountLinkInvitationResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_account_link_invitation

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_account_link_invitation.delete_account_link_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_account_link_invitation_request.DeleteAccountLinkInvitationRequest = {
            "link_id": link_id
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_client_branding(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        platforms: "capo_workspaces.types.client_device_type_list.ClientDeviceTypeList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> (
        "capo_workspaces.types.delete_client_branding_result.DeleteClientBrandingResult"
    ):
        """<p>Deletes customized client branding. Client branding allows you to customize your WorkSpace's client login portal. You can tailor your login portal company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.</p> <p>After you delete your customized client branding, your login portal reverts to the default client branding.</p>

        Args:
            resource_id: <p>The directory identifier of the WorkSpace for which you want to delete client branding.</p>
            platforms: <p>The device type for which you want to delete client branding.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_client_branding_request.DeleteClientBrandingRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_client_branding_result.DeleteClientBrandingResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_client_branding

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_client_branding.delete_client_branding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_client_branding_request.DeleteClientBrandingRequest = {
            "resource_id": resource_id,
            "platforms": platforms,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connect_client_add_in(
        self,
        add_in_id: "capo_workspaces.types.amazon_uuid.AmazonUuid",
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.delete_connect_client_add_in_result.DeleteConnectClientAddInResult":
        """<p>Deletes a client-add-in for Connect Customer that is configured within a directory.</p>

        Args:
            add_in_id: <p>The identifier of the client add-in to delete.</p>
            resource_id: <p>The directory identifier for which the client add-in is configured.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_connect_client_add_in_request.DeleteConnectClientAddInRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_connect_client_add_in_result.DeleteConnectClientAddInResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_connect_client_add_in

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_connect_client_add_in.delete_connect_client_add_in(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_connect_client_add_in_request.DeleteConnectClientAddInRequest = {
            "add_in_id": add_in_id,
            "resource_id": resource_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connection_alias(
        self,
        alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.delete_connection_alias_result.DeleteConnectionAliasResult":
        """<p>Deletes the specified connection alias. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p> <important> <p> <b>If you will no longer be using a fully qualified domain name (FQDN) as the registration code for your WorkSpaces users, you must take certain precautions to prevent potential security issues.</b> For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html#cross-region-redirection-security-considerations"> Security Considerations if You Stop Using Cross-Region Redirection</a>.</p> </important> <note> <p>To delete a connection alias that has been shared, the shared account must first disassociate the connection alias from any directories it has been associated with. Then you must unshare the connection alias from the account it has been shared with. You can delete a connection alias only after it is no longer shared with any accounts or associated with any directories.</p> </note>

        Args:
            alias_id: <p>The identifier of the connection alias to delete.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_associated_exception.ResourceAssociatedException: <p>The resource is associated with a directory.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_connection_alias_request.DeleteConnectionAliasRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_connection_alias_result.DeleteConnectionAliasResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_connection_alias

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_connection_alias.delete_connection_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_connection_alias_request.DeleteConnectionAliasRequest = {
            "alias_id": alias_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_ip_group(
        self,
        group_id: "capo_workspaces.types.ip_group_id.IpGroupId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.delete_ip_group_result.DeleteIpGroupResult":
        """<p>Deletes the specified IP access control group.</p> <p>You cannot delete an IP access control group that is associated with a directory.</p>

        Args:
            group_id: <p>The identifier of the IP access control group.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_associated_exception.ResourceAssociatedException: <p>The resource is associated with a directory.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_ip_group_request.DeleteIpGroupRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_ip_group_result.DeleteIpGroupResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_ip_group

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_ip_group.delete_ip_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_ip_group_request.DeleteIpGroupRequest = {
            "group_id": group_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_tags(
        self,
        resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString",
        tag_keys: "capo_workspaces.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.delete_tags_result.DeleteTagsResult":
        """<p>Deletes the specified tags from the specified WorkSpaces resource.</p>

        Args:
            resource_id: <p>The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, IP access control groups, and connection aliases.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_tags_request.DeleteTagsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_tags_result.DeleteTagsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_tags

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_tags.delete_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_tags_request.DeleteTagsRequest = {
            "resource_id": resource_id,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace_bundle(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        bundle_id: Optional["capo_workspaces.types.bundle_id.BundleId"] = None,
    ) -> "capo_workspaces.types.delete_workspace_bundle_result.DeleteWorkspaceBundleResult":
        """<p>Deletes the specified WorkSpace bundle. For more information about deleting WorkSpace bundles, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/delete_bundle.html"> Delete a Custom WorkSpaces Bundle or Image</a>.</p>

        Args:
            bundle_id: <p>The identifier of the bundle.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_associated_exception.ResourceAssociatedException: <p>The resource is associated with a directory.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_workspace_bundle_request.DeleteWorkspaceBundleRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_workspace_bundle_result.DeleteWorkspaceBundleResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_workspace_bundle

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_workspace_bundle.delete_workspace_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_workspace_bundle_request.DeleteWorkspaceBundleRequest = {}
        if bundle_id is not None:
            input_["bundle_id"] = bundle_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workspace_image(
        self,
        image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> (
        "capo_workspaces.types.delete_workspace_image_result.DeleteWorkspaceImageResult"
    ):
        """<p>Deletes the specified image from your account. To delete an image, you must first delete any bundles that are associated with the image and unshare the image if it is shared with other accounts. </p>

        Args:
            image_id: <p>The identifier of the image.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.resource_associated_exception.ResourceAssociatedException: <p>The resource is associated with a directory.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.delete_workspace_image_request.DeleteWorkspaceImageRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.delete_workspace_image_result.DeleteWorkspaceImageResult"
        ]:
            import capo_workspaces._operations.workspaces_service.delete_workspace_image

            output, http_response = (
                capo_workspaces._operations.workspaces_service.delete_workspace_image.delete_workspace_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.delete_workspace_image_request.DeleteWorkspaceImageRequest = {
            "image_id": image_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deploy_workspace_applications(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        force: Optional["capo_workspaces.types.boolean_object.BooleanObject"] = None,
    ) -> "capo_workspaces.types.deploy_workspace_applications_result.DeployWorkspaceApplicationsResult":
        """<p>Deploys associated applications to the specified WorkSpace</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>
            force: <p>Indicates whether the force flag is applied for the specified WorkSpace. When the force flag is enabled, it allows previously failed deployments to be retried.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.incompatible_applications_exception.IncompatibleApplicationsException: <p>The specified application is not compatible with the resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is currently in use.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.deploy_workspace_applications_request.DeployWorkspaceApplicationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.deploy_workspace_applications_result.DeployWorkspaceApplicationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.deploy_workspace_applications

            output, http_response = (
                capo_workspaces._operations.workspaces_service.deploy_workspace_applications.deploy_workspace_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.deploy_workspace_applications_request.DeployWorkspaceApplicationsRequest = {
            "workspace_id": workspace_id
        }
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_workspace_directory(
        self,
        directory_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.deregister_workspace_directory_result.DeregisterWorkspaceDirectoryResult":
        """<p>Deregisters the specified directory. This operation is asynchronous and returns before the WorkSpace directory is deregistered. If any WorkSpaces are registered to this directory, you must remove them before you can deregister the directory.</p> <note> <p>Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the <a href="http://aws.amazon.com/directoryservice/pricing/">Directory Service pricing terms</a>.</p> <p>To delete empty directories, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html"> Delete the Directory for Your WorkSpaces</a>. If you delete your Simple AD or AD Connector directory, you can always create a new one when you want to start using WorkSpaces again.</p> </note>

        Args:
            directory_id: <p>The identifier of the directory. If any WorkSpaces are registered to this directory, you must remove them before you deregister the directory, or you will receive an OperationNotSupportedException error.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.deregister_workspace_directory_request.DeregisterWorkspaceDirectoryRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.deregister_workspace_directory_result.DeregisterWorkspaceDirectoryResult"
        ]:
            import capo_workspaces._operations.workspaces_service.deregister_workspace_directory

            output, http_response = (
                capo_workspaces._operations.workspaces_service.deregister_workspace_directory.deregister_workspace_directory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.deregister_workspace_directory_request.DeregisterWorkspaceDirectoryRequest = {
            "directory_id": directory_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account(
        self, *, config_overrides: Optional[WorkSpacesClientConfig] = None
    ) -> "capo_workspaces.types.describe_account_result.DescribeAccountResult":
        """<p>Retrieves a list that describes the configuration of Bring Your Own License (BYOL) for the specified account.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_account_request.DescribeAccountRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_account_result.DescribeAccountResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_account

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_account.describe_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_account_request.DescribeAccountRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_modifications(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_account_modifications_result.DescribeAccountModificationsResult":
        """<p>Retrieves a list that describes modifications to the configuration of Bring Your Own License (BYOL) for the specified account.</p>

        Args:
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_account_modifications_request.DescribeAccountModificationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_account_modifications_result.DescribeAccountModificationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_account_modifications

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_account_modifications.describe_account_modifications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_account_modifications_request.DescribeAccountModificationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_application_associations(
        self,
        application_id: "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId",
        associated_resource_types: "capo_workspaces.types.application_associated_resource_type_list.ApplicationAssociatedResourceTypeList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_application_associations_result.DescribeApplicationAssociationsResult":
        """<p>Describes the associations between the application and the specified associated resources.</p>

        Args:
            max_results: <p>The maximum number of associations to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            application_id: <p>The identifier of the specified application.</p>
            associated_resource_types: <p>The resource type of the associated resources.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_application_associations_request.DescribeApplicationAssociationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_application_associations_result.DescribeApplicationAssociationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_application_associations

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_application_associations.describe_application_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_application_associations_request.DescribeApplicationAssociationsRequest = {
            "application_id": application_id,
            "associated_resource_types": associated_resource_types,
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

    def iter_describe_application_associations(
        self,
        application_id: "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId",
        associated_resource_types: "capo_workspaces.types.application_associated_resource_type_list.ApplicationAssociatedResourceTypeList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_workspaces.types.describe_application_associations_result.DescribeApplicationAssociationsResult]":
        _token = next_token
        while True:
            _response = self.describe_application_associations(
                application_id,
                associated_resource_types,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_applications(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        application_ids: Optional[
            "capo_workspaces.types.work_space_application_id_list.WorkSpaceApplicationIdList"
        ] = None,
        compute_type_names: Optional[
            "capo_workspaces.types.compute_list.ComputeList"
        ] = None,
        license_type: Optional[
            "capo_workspaces.types.work_space_application_license_type.WorkSpaceApplicationLicenseType"
        ] = None,
        operating_system_names: Optional[
            "capo_workspaces.types.operating_system_name_list.OperatingSystemNameList"
        ] = None,
        owner: Optional[
            "capo_workspaces.types.work_space_application_owner.WorkSpaceApplicationOwner"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> (
        "capo_workspaces.types.describe_applications_result.DescribeApplicationsResult"
    ):
        """<p>Describes the specified applications by filtering based on their compute types, license availability, operating systems, and owners.</p>

        Args:
            application_ids: <p>The identifiers of one or more applications.</p>
            compute_type_names: <p>The compute types supported by the applications.</p>
            license_type: <p>The license availability for the applications.</p>
            operating_system_names: <p>The operating systems supported by the applications.</p>
            owner: <p>The owner of the applications.</p>
            max_results: <p>The maximum number of applications to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_applications_request.DescribeApplicationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_applications_result.DescribeApplicationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_applications

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_applications.describe_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_applications_request.DescribeApplicationsRequest = {}
        if application_ids is not None:
            input_["application_ids"] = application_ids
        if compute_type_names is not None:
            input_["compute_type_names"] = compute_type_names
        if license_type is not None:
            input_["license_type"] = license_type
        if operating_system_names is not None:
            input_["operating_system_names"] = operating_system_names
        if owner is not None:
            input_["owner"] = owner
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

    def iter_describe_applications(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        application_ids: Optional[
            "capo_workspaces.types.work_space_application_id_list.WorkSpaceApplicationIdList"
        ] = None,
        compute_type_names: Optional[
            "capo_workspaces.types.compute_list.ComputeList"
        ] = None,
        license_type: Optional[
            "capo_workspaces.types.work_space_application_license_type.WorkSpaceApplicationLicenseType"
        ] = None,
        operating_system_names: Optional[
            "capo_workspaces.types.operating_system_name_list.OperatingSystemNameList"
        ] = None,
        owner: Optional[
            "capo_workspaces.types.work_space_application_owner.WorkSpaceApplicationOwner"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_workspaces.types.describe_applications_result.DescribeApplicationsResult]":
        _token = next_token
        while True:
            _response = self.describe_applications(
                config_overrides=config_overrides,
                application_ids=application_ids,
                compute_type_names=compute_type_names,
                license_type=license_type,
                operating_system_names=operating_system_names,
                owner=owner,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_bundle_associations(
        self,
        bundle_id: "capo_workspaces.types.bundle_id.BundleId",
        associated_resource_types: "capo_workspaces.types.bundle_associated_resource_type_list.BundleAssociatedResourceTypeList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_bundle_associations_result.DescribeBundleAssociationsResult":
        """<p>Describes the associations between the applications and the specified bundle.</p>

        Args:
            bundle_id: <p>The identifier of the bundle.</p>
            associated_resource_types: <p>The resource types of the associated resource.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_bundle_associations_request.DescribeBundleAssociationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_bundle_associations_result.DescribeBundleAssociationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_bundle_associations

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_bundle_associations.describe_bundle_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_bundle_associations_request.DescribeBundleAssociationsRequest = {
            "bundle_id": bundle_id,
            "associated_resource_types": associated_resource_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_client_branding(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_client_branding_result.DescribeClientBrandingResult":
        """<p>Describes the specified client branding. Client branding allows you to customize the log in page of various device types for your users. You can add your company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.</p> <note> <p>Only device types that have branding information configured will be shown in the response.</p> </note>

        Args:
            resource_id: <p>The directory identifier of the WorkSpace for which you want to view client branding information.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_client_branding_request.DescribeClientBrandingRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_client_branding_result.DescribeClientBrandingResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_client_branding

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_client_branding.describe_client_branding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_client_branding_request.DescribeClientBrandingRequest = {
            "resource_id": resource_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_client_properties(
        self,
        resource_ids: "capo_workspaces.types.resource_id_list.ResourceIdList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_client_properties_result.DescribeClientPropertiesResult":
        """<p>Retrieves a list that describes one or more specified Amazon WorkSpaces clients.</p>

        Args:
            resource_ids: <p>The resource identifier, in the form of directory IDs.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_client_properties_request.DescribeClientPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_client_properties_result.DescribeClientPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_client_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_client_properties.describe_client_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_client_properties_request.DescribeClientPropertiesRequest = {
            "resource_ids": resource_ids
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_connect_client_add_ins(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "capo_workspaces.types.describe_connect_client_add_ins_result.DescribeConnectClientAddInsResult":
        """<p>Retrieves a list of Connect Customer client add-ins that have been created.</p>

        Args:
            resource_id: <p>The directory identifier for which the client add-in is configured.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_connect_client_add_ins_request.DescribeConnectClientAddInsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_connect_client_add_ins_result.DescribeConnectClientAddInsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_connect_client_add_ins

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_connect_client_add_ins.describe_connect_client_add_ins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_connect_client_add_ins_request.DescribeConnectClientAddInsRequest = {
            "resource_id": resource_id
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

    def describe_connection_aliases(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        alias_ids: Optional[
            "capo_workspaces.types.connection_alias_id_list.ConnectionAliasIdList"
        ] = None,
        resource_id: Optional[
            "capo_workspaces.types.non_empty_string.NonEmptyString"
        ] = None,
        limit: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_connection_aliases_result.DescribeConnectionAliasesResult":
        """<p>Retrieves a list that describes the connection aliases used for cross-Region redirection. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p>

        Args:
            alias_ids: <p>The identifiers of the connection aliases to describe.</p>
            resource_id: <p>The identifier of the directory associated with the connection alias.</p>
            limit: <p>The maximum number of connection aliases to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results. </p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_connection_aliases_request.DescribeConnectionAliasesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_connection_aliases_result.DescribeConnectionAliasesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_connection_aliases

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_connection_aliases.describe_connection_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_connection_aliases_request.DescribeConnectionAliasesRequest = {}
        if alias_ids is not None:
            input_["alias_ids"] = alias_ids
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_connection_alias_permissions(
        self,
        alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "capo_workspaces.types.describe_connection_alias_permissions_result.DescribeConnectionAliasPermissionsResult":
        """<p>Describes the permissions that the owner of a connection alias has granted to another Amazon Web Services account for the specified connection alias. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p>

        Args:
            alias_id: <p>The identifier of the connection alias.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results. </p>
            max_results: <p>The maximum number of results to return.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_connection_alias_permissions_request.DescribeConnectionAliasPermissionsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_connection_alias_permissions_result.DescribeConnectionAliasPermissionsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_connection_alias_permissions

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_connection_alias_permissions.describe_connection_alias_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_connection_alias_permissions_request.DescribeConnectionAliasPermissionsRequest = {
            "alias_id": alias_id
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

    def describe_custom_workspace_image_import(
        self,
        image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_custom_workspace_image_import_result.DescribeCustomWorkspaceImageImportResult":
        """<p>Retrieves information about a WorkSpace BYOL image being imported via ImportCustomWorkspaceImage.</p>

        Args:
            image_id: <p>The identifier of the WorkSpace image.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_custom_workspace_image_import_request.DescribeCustomWorkspaceImageImportRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_custom_workspace_image_import_result.DescribeCustomWorkspaceImageImportResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_custom_workspace_image_import

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_custom_workspace_image_import.describe_custom_workspace_image_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_custom_workspace_image_import_request.DescribeCustomWorkspaceImageImportRequest = {
            "image_id": image_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_image_associations(
        self,
        image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        associated_resource_types: "capo_workspaces.types.image_associated_resource_type_list.ImageAssociatedResourceTypeList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_image_associations_result.DescribeImageAssociationsResult":
        """<p>Describes the associations between the applications and the specified image.</p>

        Args:
            image_id: <p>The identifier of the image.</p>
            associated_resource_types: <p>The resource types of the associated resource.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_image_associations_request.DescribeImageAssociationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_image_associations_result.DescribeImageAssociationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_image_associations

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_image_associations.describe_image_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_image_associations_request.DescribeImageAssociationsRequest = {
            "image_id": image_id,
            "associated_resource_types": associated_resource_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_ip_groups(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        group_ids: Optional[
            "capo_workspaces.types.ip_group_id_list.IpGroupIdList"
        ] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "capo_workspaces.types.describe_ip_groups_result.DescribeIpGroupsResult":
        """<p>Describes one or more of your IP access control groups.</p>

        Args:
            group_ids: <p>The identifiers of one or more IP access control groups.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_ip_groups_request.DescribeIpGroupsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_ip_groups_result.DescribeIpGroupsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_ip_groups

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_ip_groups.describe_ip_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_ip_groups_request.DescribeIpGroupsRequest = {}
        if group_ids is not None:
            input_["group_ids"] = group_ids
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

    def describe_tags(
        self,
        resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_tags_result.DescribeTagsResult":
        """<p>Describes the specified tags for the specified WorkSpaces resource.</p>

        Args:
            resource_id: <p>The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, IP access control groups, and connection aliases.</p>

        Raises:
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_tags_request.DescribeTagsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_tags_result.DescribeTagsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_tags

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_tags.describe_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_tags_request.DescribeTagsRequest = {
            "resource_id": resource_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspace_associations(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        associated_resource_types: "capo_workspaces.types.work_space_associated_resource_type_list.WorkSpaceAssociatedResourceTypeList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_workspace_associations_result.DescribeWorkspaceAssociationsResult":
        """<p>Describes the associations betweens applications and the specified WorkSpace.</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>
            associated_resource_types: <p>The resource types of the associated resources.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspace_associations_request.DescribeWorkspaceAssociationsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspace_associations_result.DescribeWorkspaceAssociationsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspace_associations

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspace_associations.describe_workspace_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspace_associations_request.DescribeWorkspaceAssociationsRequest = {
            "workspace_id": workspace_id,
            "associated_resource_types": associated_resource_types,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspace_bundles(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        bundle_ids: Optional[
            "capo_workspaces.types.bundle_id_list.BundleIdList"
        ] = None,
        owner: Optional["capo_workspaces.types.bundle_owner.BundleOwner"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_workspace_bundles_result.DescribeWorkspaceBundlesResult":
        """<p>Retrieves a list that describes the available WorkSpace bundles.</p> <p>You can filter the results using either bundle ID or owner, but not both.</p>

        Args:
            bundle_ids: <p>The identifiers of the bundles. You cannot combine this parameter with any other filter.</p>
            owner: <p>The owner of the bundles. You cannot combine this parameter with any other filter.</p> <p>To describe the bundles provided by Amazon Web Services, specify <code>AMAZON</code>. To describe the bundles that belong to your account, don't specify a value.</p>
            next_token: <p>The token for the next set of results. (You received this token from a previous call.)</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspace_bundles_request.DescribeWorkspaceBundlesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspace_bundles_result.DescribeWorkspaceBundlesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspace_bundles

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspace_bundles.describe_workspace_bundles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspace_bundles_request.DescribeWorkspaceBundlesRequest = {}
        if bundle_ids is not None:
            input_["bundle_ids"] = bundle_ids
        if owner is not None:
            input_["owner"] = owner
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_workspace_bundles(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        bundle_ids: Optional[
            "capo_workspaces.types.bundle_id_list.BundleIdList"
        ] = None,
        owner: Optional["capo_workspaces.types.bundle_owner.BundleOwner"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_workspaces.types.workspace_bundle.WorkspaceBundle]":
        _token = next_token
        while True:
            _response = self.describe_workspace_bundles(
                config_overrides=config_overrides,
                bundle_ids=bundle_ids,
                owner=owner,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("bundles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_workspace_directories(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        directory_ids: Optional[
            "capo_workspaces.types.directory_id_list.DirectoryIdList"
        ] = None,
        workspace_directory_names: Optional[
            "capo_workspaces.types.workspace_directory_name_list.WorkspaceDirectoryNameList"
        ] = None,
        limit: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional[
            "capo_workspaces.types.describe_workspace_directories_filter_list.DescribeWorkspaceDirectoriesFilterList"
        ] = None,
    ) -> "capo_workspaces.types.describe_workspace_directories_result.DescribeWorkspaceDirectoriesResult":
        """<p>Describes the available directories that are registered with Amazon WorkSpaces.</p>

        Args:
            directory_ids: <p>The identifiers of the directories. If the value is null, all directories are retrieved.</p>
            workspace_directory_names: <p>The names of the WorkSpace directories.</p>
            limit: <p>The maximum number of directories to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            filters: <p>The filter condition for the WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspace_directories_request.DescribeWorkspaceDirectoriesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspace_directories_result.DescribeWorkspaceDirectoriesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspace_directories

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspace_directories.describe_workspace_directories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspace_directories_request.DescribeWorkspaceDirectoriesRequest = {}
        if directory_ids is not None:
            input_["directory_ids"] = directory_ids
        if workspace_directory_names is not None:
            input_["workspace_directory_names"] = workspace_directory_names
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_workspace_directories(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        directory_ids: Optional[
            "capo_workspaces.types.directory_id_list.DirectoryIdList"
        ] = None,
        workspace_directory_names: Optional[
            "capo_workspaces.types.workspace_directory_name_list.WorkspaceDirectoryNameList"
        ] = None,
        limit: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional[
            "capo_workspaces.types.describe_workspace_directories_filter_list.DescribeWorkspaceDirectoriesFilterList"
        ] = None,
    ) -> "Iterator[capo_workspaces.types.workspace_directory.WorkspaceDirectory]":
        _token = next_token
        while True:
            _response = self.describe_workspace_directories(
                config_overrides=config_overrides,
                directory_ids=directory_ids,
                workspace_directory_names=workspace_directory_names,
                limit=limit,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("directories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_workspace_image_permissions(
        self,
        image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "capo_workspaces.types.describe_workspace_image_permissions_result.DescribeWorkspaceImagePermissionsResult":
        """<p>Describes the permissions that the owner of an image has granted to other Amazon Web Services accounts for an image.</p>

        Args:
            image_id: <p>The identifier of the image.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspace_image_permissions_request.DescribeWorkspaceImagePermissionsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspace_image_permissions_result.DescribeWorkspaceImagePermissionsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspace_image_permissions

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspace_image_permissions.describe_workspace_image_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspace_image_permissions_request.DescribeWorkspaceImagePermissionsRequest = {
            "image_id": image_id
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

    def describe_workspace_images(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        image_ids: Optional[
            "capo_workspaces.types.workspace_image_id_list.WorkspaceImageIdList"
        ] = None,
        image_type: Optional["capo_workspaces.types.image_type.ImageType"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "capo_workspaces.types.describe_workspace_images_result.DescribeWorkspaceImagesResult":
        """<p>Retrieves a list that describes one or more specified images, if the image identifiers are provided. Otherwise, all images in the account are described. </p>

        Args:
            image_ids: <p>The identifier of the image.</p>
            image_type: <p>The type (owned or shared) of the image.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            max_results: <p>The maximum number of items to return.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspace_images_request.DescribeWorkspaceImagesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspace_images_result.DescribeWorkspaceImagesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspace_images

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspace_images.describe_workspace_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspace_images_request.DescribeWorkspaceImagesRequest = {}
        if image_ids is not None:
            input_["image_ids"] = image_ids
        if image_type is not None:
            input_["image_type"] = image_type
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

    def describe_workspaces(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        workspace_ids: Optional[
            "capo_workspaces.types.workspace_id_list.WorkspaceIdList"
        ] = None,
        directory_id: Optional["capo_workspaces.types.directory_id.DirectoryId"] = None,
        user_name: Optional["capo_workspaces.types.user_name.UserName"] = None,
        bundle_id: Optional["capo_workspaces.types.bundle_id.BundleId"] = None,
        limit: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        workspace_name: Optional[
            "capo_workspaces.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_workspaces.types.describe_workspaces_result.DescribeWorkspacesResult":
        """<p>Describes the specified WorkSpaces.</p> <p>You can filter the results by using the bundle identifier, directory identifier, or owner, but you can specify only one filter at a time.</p>

        Args:
            workspace_ids: <p>The identifiers of the WorkSpaces. You cannot combine this parameter with any other filter.</p> <p>Because the <a>CreateWorkspaces</a> operation is asynchronous, the identifier it returns is not immediately available. If you immediately call <a>DescribeWorkspaces</a> with this identifier, no information is returned.</p>
            directory_id: <p>The identifier of the directory. In addition, you can optionally specify a specific directory user (see <code>UserName</code>). You cannot combine this parameter with any other filter.</p>
            user_name: <p>The name of the directory user. You must specify this parameter with <code>DirectoryId</code>.</p>
            bundle_id: <p>The identifier of the bundle. All WorkSpaces that are created from this bundle are retrieved. You cannot combine this parameter with any other filter.</p>
            limit: <p>The maximum number of items to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>
            workspace_name: <p>The name of the user-decoupled WorkSpace.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspaces_request.DescribeWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspaces_result.DescribeWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspaces.describe_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspaces_request.DescribeWorkspacesRequest = {}
        if workspace_ids is not None:
            input_["workspace_ids"] = workspace_ids
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if user_name is not None:
            input_["user_name"] = user_name
        if bundle_id is not None:
            input_["bundle_id"] = bundle_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_workspaces(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        workspace_ids: Optional[
            "capo_workspaces.types.workspace_id_list.WorkspaceIdList"
        ] = None,
        directory_id: Optional["capo_workspaces.types.directory_id.DirectoryId"] = None,
        user_name: Optional["capo_workspaces.types.user_name.UserName"] = None,
        bundle_id: Optional["capo_workspaces.types.bundle_id.BundleId"] = None,
        limit: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        workspace_name: Optional[
            "capo_workspaces.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "Iterator[capo_workspaces.types.workspace.Workspace]":
        _token = next_token
        while True:
            _response = self.describe_workspaces(
                config_overrides=config_overrides,
                workspace_ids=workspace_ids,
                directory_id=directory_id,
                user_name=user_name,
                bundle_id=bundle_id,
                limit=limit,
                next_token=_token,
                workspace_name=workspace_name,
            )
            _page = _resolve_path(_response, ("workspaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_workspaces_connection_status(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        workspace_ids: Optional[
            "capo_workspaces.types.workspace_id_list.WorkspaceIdList"
        ] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_workspaces_connection_status_result.DescribeWorkspacesConnectionStatusResult":
        """<p>Describes the connection status of the specified WorkSpaces.</p>

        Args:
            workspace_ids: <p>The identifiers of the WorkSpaces. You can specify up to 25 WorkSpaces.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspaces_connection_status_request.DescribeWorkspacesConnectionStatusRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspaces_connection_status_result.DescribeWorkspacesConnectionStatusResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspaces_connection_status

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspaces_connection_status.describe_workspaces_connection_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspaces_connection_status_request.DescribeWorkspacesConnectionStatusRequest = {}
        if workspace_ids is not None:
            input_["workspace_ids"] = workspace_ids
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspace_snapshots(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.describe_workspace_snapshots_result.DescribeWorkspaceSnapshotsResult":
        """<p>Describes the snapshots for the specified WorkSpace.</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspace_snapshots_request.DescribeWorkspaceSnapshotsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspace_snapshots_result.DescribeWorkspaceSnapshotsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspace_snapshots

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspace_snapshots.describe_workspace_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspace_snapshots_request.DescribeWorkspaceSnapshotsRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspaces_pools(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        pool_ids: Optional[
            "capo_workspaces.types.workspaces_pool_ids.WorkspacesPoolIds"
        ] = None,
        filters: Optional[
            "capo_workspaces.types.describe_workspaces_pools_filters.DescribeWorkspacesPoolsFilters"
        ] = None,
        limit: Optional["capo_workspaces.types.limit.Limit"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_workspaces_pools_result.DescribeWorkspacesPoolsResult":
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Describes the specified WorkSpaces Pools.</p>

        Args:
            pool_ids: <p>The identifier of the WorkSpaces Pools.</p>
            filters: <p>The filter conditions for the WorkSpaces Pool to return.</p>
            limit: <p>The maximum number of items to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspaces_pools_request.DescribeWorkspacesPoolsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspaces_pools_result.DescribeWorkspacesPoolsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspaces_pools

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspaces_pools.describe_workspaces_pools(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspaces_pools_request.DescribeWorkspacesPoolsRequest = {}
        if pool_ids is not None:
            input_["pool_ids"] = pool_ids
        if filters is not None:
            input_["filters"] = filters
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_workspaces_pool_sessions(
        self,
        pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        user_id: Optional[
            "capo_workspaces.types.workspaces_pool_user_id.WorkspacesPoolUserId"
        ] = None,
        limit: Optional["capo_workspaces.types.limit50.Limit50"] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.describe_workspaces_pool_sessions_result.DescribeWorkspacesPoolSessionsResult":
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Retrieves a list that describes the streaming sessions for a specified pool.</p>

        Args:
            pool_id: <p>The identifier of the pool.</p>
            user_id: <p>The identifier of the user.</p>
            limit: <p>The maximum size of each page of results. The default value is 20 and the maximum value is 50.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.describe_workspaces_pool_sessions_request.DescribeWorkspacesPoolSessionsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.describe_workspaces_pool_sessions_result.DescribeWorkspacesPoolSessionsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.describe_workspaces_pool_sessions

            output, http_response = (
                capo_workspaces._operations.workspaces_service.describe_workspaces_pool_sessions.describe_workspaces_pool_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.describe_workspaces_pool_sessions_request.DescribeWorkspacesPoolSessionsRequest = {
            "pool_id": pool_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_connection_alias(
        self,
        alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.disassociate_connection_alias_result.DisassociateConnectionAliasResult":
        """<p>Disassociates a connection alias from a directory. Disassociating a connection alias disables cross-Region redirection between two directories in different Regions. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p> <note> <p>Before performing this operation, call <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html"> DescribeConnectionAliases</a> to make sure that the current state of the connection alias is <code>CREATED</code>.</p> </note>

        Args:
            alias_id: <p>The identifier of the connection alias to disassociate.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.disassociate_connection_alias_request.DisassociateConnectionAliasRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.disassociate_connection_alias_result.DisassociateConnectionAliasResult"
        ]:
            import capo_workspaces._operations.workspaces_service.disassociate_connection_alias

            output, http_response = (
                capo_workspaces._operations.workspaces_service.disassociate_connection_alias.disassociate_connection_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.disassociate_connection_alias_request.DisassociateConnectionAliasRequest = {
            "alias_id": alias_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_ip_groups(
        self,
        directory_id: "capo_workspaces.types.directory_id.DirectoryId",
        group_ids: "capo_workspaces.types.ip_group_id_list.IpGroupIdList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> (
        "capo_workspaces.types.disassociate_ip_groups_result.DisassociateIpGroupsResult"
    ):
        """<p>Disassociates the specified IP access control group from the specified directory.</p>

        Args:
            directory_id: <p>The identifier of the directory.</p>
            group_ids: <p>The identifiers of one or more IP access control groups.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.disassociate_ip_groups_request.DisassociateIpGroupsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.disassociate_ip_groups_result.DisassociateIpGroupsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.disassociate_ip_groups

            output, http_response = (
                capo_workspaces._operations.workspaces_service.disassociate_ip_groups.disassociate_ip_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.disassociate_ip_groups_request.DisassociateIpGroupsRequest = {
            "directory_id": directory_id,
            "group_ids": group_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_workspace_application(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        application_id: "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.disassociate_workspace_application_result.DisassociateWorkspaceApplicationResult":
        """<p>Disassociates the specified application from a WorkSpace.</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>
            application_id: <p>The identifier of the application.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_in_use_exception.ResourceInUseException: <p>The specified resource is currently in use.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.disassociate_workspace_application_request.DisassociateWorkspaceApplicationRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.disassociate_workspace_application_result.DisassociateWorkspaceApplicationResult"
        ]:
            import capo_workspaces._operations.workspaces_service.disassociate_workspace_application

            output, http_response = (
                capo_workspaces._operations.workspaces_service.disassociate_workspace_application.disassociate_workspace_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.disassociate_workspace_application_request.DisassociateWorkspaceApplicationRequest = {
            "workspace_id": workspace_id,
            "application_id": application_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_account_link(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        link_id: Optional["capo_workspaces.types.link_id.LinkId"] = None,
        linked_account_id: Optional[
            "capo_workspaces.types.aws_account.AwsAccount"
        ] = None,
    ) -> "capo_workspaces.types.get_account_link_result.GetAccountLinkResult":
        """<p>Retrieves account link information.</p>

        Args:
            link_id: <p>The identifier of the account to link.</p>
            linked_account_id: <p>The identifier of the account link</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.internal_server_exception.InternalServerException: <p>Unexpected server error occured.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.validation_exception.ValidationException: <p>You either haven't provided a <code>TargetAccountId</code> or are using the same value for <code>TargetAccountId</code> and <code>SourceAccountId</code>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.get_account_link_request.GetAccountLinkRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.get_account_link_result.GetAccountLinkResult"
        ]:
            import capo_workspaces._operations.workspaces_service.get_account_link

            output, http_response = (
                capo_workspaces._operations.workspaces_service.get_account_link.get_account_link(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.get_account_link_request.GetAccountLinkRequest = {}
        if link_id is not None:
            input_["link_id"] = link_id
        if linked_account_id is not None:
            input_["linked_account_id"] = linked_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_client_branding(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        device_type_windows: Optional[
            "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
        ] = None,
        device_type_osx: Optional[
            "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
        ] = None,
        device_type_android: Optional[
            "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
        ] = None,
        device_type_ios: Optional[
            "capo_workspaces.types.ios_import_client_branding_attributes.IosImportClientBrandingAttributes"
        ] = None,
        device_type_linux: Optional[
            "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
        ] = None,
        device_type_web: Optional[
            "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
        ] = None,
    ) -> (
        "capo_workspaces.types.import_client_branding_result.ImportClientBrandingResult"
    ):
        """<p>Imports client branding. Client branding allows you to customize your WorkSpace's client login portal. You can tailor your login portal company logo, the support email address, support link, link to reset password, and a custom message for users trying to sign in.</p> <p>After you import client branding, the default branding experience for the specified platform type is replaced with the imported experience</p> <note> <ul> <li> <p>You must specify at least one platform type when importing client branding.</p> </li> <li> <p>You can import up to 6 MB of data with each request. If your request exceeds this limit, you can import client branding for different platform types using separate requests.</p> </li> <li> <p>In each platform type, the <code>SupportEmail</code> and <code>SupportLink</code> parameters are mutually exclusive. You can specify only one parameter for each platform type, but not both.</p> </li> <li> <p>Imported data can take up to a minute to appear in the WorkSpaces client.</p> </li> </ul> </note>

        Args:
            resource_id: <p>The directory identifier of the WorkSpace for which you want to import client branding.</p>
            device_type_windows: <p>The branding information to import for Windows devices.</p>
            device_type_osx: <p>The branding information to import for macOS devices.</p>
            device_type_android: <p>The branding information to import for Android devices.</p>
            device_type_ios: <p>The branding information to import for iOS devices.</p>
            device_type_linux: <p>The branding information to import for Linux devices.</p>
            device_type_web: <p>The branding information to import for web access.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.import_client_branding_request.ImportClientBrandingRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.import_client_branding_result.ImportClientBrandingResult"
        ]:
            import capo_workspaces._operations.workspaces_service.import_client_branding

            output, http_response = (
                capo_workspaces._operations.workspaces_service.import_client_branding.import_client_branding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.import_client_branding_request.ImportClientBrandingRequest = {
            "resource_id": resource_id
        }
        if device_type_windows is not None:
            input_["device_type_windows"] = device_type_windows
        if device_type_osx is not None:
            input_["device_type_osx"] = device_type_osx
        if device_type_android is not None:
            input_["device_type_android"] = device_type_android
        if device_type_ios is not None:
            input_["device_type_ios"] = device_type_ios
        if device_type_linux is not None:
            input_["device_type_linux"] = device_type_linux
        if device_type_web is not None:
            input_["device_type_web"] = device_type_web

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_custom_workspace_image(
        self,
        image_name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName",
        image_description: "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription",
        compute_type: "capo_workspaces.types.image_compute_type.ImageComputeType",
        protocol: "capo_workspaces.types.custom_image_protocol.CustomImageProtocol",
        image_source: "capo_workspaces.types.image_source_identifier.ImageSourceIdentifier",
        infrastructure_configuration_arn: "capo_workspaces.types.infrastructure_configuration_arn.InfrastructureConfigurationArn",
        platform: "capo_workspaces.types.platform.Platform",
        os_version: "capo_workspaces.types.os_version.OSVersion",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
    ) -> "capo_workspaces.types.import_custom_workspace_image_result.ImportCustomWorkspaceImageResult":
        """<p>Imports the specified Windows 10 or 11 Bring Your Own License (BYOL) image into Amazon WorkSpaces using EC2 Image Builder. The image must be an already licensed image that is in your Amazon Web Services account, and you must own the image. For more information about creating BYOL images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html"> Bring Your Own Windows Desktop Licenses</a>. </p>

        Args:
            image_name: <p>The name of the WorkSpace image.</p>
            image_description: <p>The description of the WorkSpace image.</p>
            compute_type: <p>The supported compute type for the WorkSpace image.</p>
            protocol: <p>The supported protocol for the WorkSpace image. Windows 11 does not support PCOIP protocol.</p>
            image_source: <p>The options for image import source.</p>
            infrastructure_configuration_arn: <p>The infrastructure configuration ARN that specifies how the WorkSpace image is built.</p>
            platform: <p>The platform for the WorkSpace image source.</p>
            os_version: <p>The OS version for the WorkSpace image source.</p>
            tags: <p>The resource tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.import_custom_workspace_image_request.ImportCustomWorkspaceImageRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.import_custom_workspace_image_result.ImportCustomWorkspaceImageResult"
        ]:
            import capo_workspaces._operations.workspaces_service.import_custom_workspace_image

            output, http_response = (
                capo_workspaces._operations.workspaces_service.import_custom_workspace_image.import_custom_workspace_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.import_custom_workspace_image_request.ImportCustomWorkspaceImageRequest = {
            "image_name": image_name,
            "image_description": image_description,
            "compute_type": compute_type,
            "protocol": protocol,
            "image_source": image_source,
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "platform": platform,
            "os_version": os_version,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_workspace_image(
        self,
        ec2_image_id: "capo_workspaces.types.ec2_image_id.Ec2ImageId",
        ingestion_process: "capo_workspaces.types.workspace_image_ingestion_process.WorkspaceImageIngestionProcess",
        image_name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName",
        image_description: "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
        applications: Optional[
            "capo_workspaces.types.application_list.ApplicationList"
        ] = None,
    ) -> (
        "capo_workspaces.types.import_workspace_image_result.ImportWorkspaceImageResult"
    ):
        """<p>Imports the specified Windows 10 or 11 Bring Your Own License (BYOL) image into Amazon WorkSpaces. The image must be an already licensed Amazon EC2 image that is in your Amazon Web Services account, and you must own the image. For more information about creating BYOL images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html"> Bring Your Own Windows Desktop Licenses</a>.</p>

        Args:
            ec2_image_id: <p>The identifier of the EC2 image.</p>
            ingestion_process: <p>The ingestion process to be used when importing the image, depending on which protocol you want to use for your BYOL Workspace image, either PCoIP, WSP, or bring your own protocol (BYOP). To use DCV, specify a value that ends in <code>_WSP</code>. To use PCoIP, specify a value that does not end in <code>_WSP</code>. To use BYOP, specify a value that ends in <code>_BYOP</code>.</p> <p>For non-GPU-enabled bundles (bundles other than Graphics or GraphicsPro), specify <code>BYOL_REGULAR</code>, <code>BYOL_REGULAR_WSP</code>, or <code>BYOL_REGULAR_BYOP</code>, depending on the protocol.</p> <note> <p>The <code>BYOL_REGULAR_BYOP</code> and <code>BYOL_GRAPHICS_G4DN_BYOP</code> values are only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use these values. For more information, see <a href="http://aws.amazon.com/workspaces/core/">Amazon WorkSpaces Core</a>.</p> </note>
            image_name: <p>The name of the WorkSpace image.</p>
            image_description: <p>The description of the WorkSpace image.</p>
            tags: <p>The tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>
            applications: <p>If specified, the version of Microsoft Office to subscribe to. Valid only for Windows 10 and 11 BYOL images. For more information about subscribing to Office for BYOL images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html"> Bring Your Own Windows Desktop Licenses</a>.</p> <note> <ul> <li> <p>Although this parameter is an array, only one item is allowed at this time.</p> </li> <li> <p>During the image import process, non-GPU DCV (formerly WSP) WorkSpaces with Windows 11 support only <code>Microsoft_Office_2019</code>. GPU DCV (formerly WSP) WorkSpaces with Windows 11 do not support Office installation.</p> </li> </ul> </note>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.import_workspace_image_request.ImportWorkspaceImageRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.import_workspace_image_result.ImportWorkspaceImageResult"
        ]:
            import capo_workspaces._operations.workspaces_service.import_workspace_image

            output, http_response = (
                capo_workspaces._operations.workspaces_service.import_workspace_image.import_workspace_image(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.import_workspace_image_request.ImportWorkspaceImageRequest = {
            "ec2_image_id": ec2_image_id,
            "ingestion_process": ingestion_process,
            "image_name": image_name,
            "image_description": image_description,
        }
        if tags is not None:
            input_["tags"] = tags
        if applications is not None:
            input_["applications"] = applications

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_account_links(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        link_status_filter: Optional[
            "capo_workspaces.types.link_status_filter_list.LinkStatusFilterList"
        ] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "capo_workspaces.types.list_account_links_result.ListAccountLinksResult":
        """<p>Lists all account links.</p>

        Args:
            link_status_filter: <p>Filters the account based on their link status.</p>
            next_token: <p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>
            max_results: <p>The maximum number of accounts to return.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.internal_server_exception.InternalServerException: <p>Unexpected server error occured.</p>
            capo_workspaces.errors.validation_exception.ValidationException: <p>You either haven't provided a <code>TargetAccountId</code> or are using the same value for <code>TargetAccountId</code> and <code>SourceAccountId</code>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.list_account_links_request.ListAccountLinksRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.list_account_links_result.ListAccountLinksResult"
        ]:
            import capo_workspaces._operations.workspaces_service.list_account_links

            output, http_response = (
                capo_workspaces._operations.workspaces_service.list_account_links.list_account_links(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.list_account_links_request.ListAccountLinksRequest = {}
        if link_status_filter is not None:
            input_["link_status_filter"] = link_status_filter
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

    def iter_list_account_links(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        link_status_filter: Optional[
            "capo_workspaces.types.link_status_filter_list.LinkStatusFilterList"
        ] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_workspaces.types.limit.Limit"] = None,
    ) -> "Iterator[capo_workspaces.types.account_link.AccountLink]":
        _token = next_token
        while True:
            _response = self.list_account_links(
                config_overrides=config_overrides,
                link_status_filter=link_status_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("account_links",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_available_management_cidr_ranges(
        self,
        management_cidr_range_constraint: "capo_workspaces.types.management_cidr_range_constraint.ManagementCidrRangeConstraint",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        max_results: Optional[
            "capo_workspaces.types.management_cidr_range_max_results.ManagementCidrRangeMaxResults"
        ] = None,
        next_token: Optional[
            "capo_workspaces.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_workspaces.types.list_available_management_cidr_ranges_result.ListAvailableManagementCidrRangesResult":
        """<p>Retrieves a list of IP address ranges, specified as IPv4 CIDR blocks, that you can use for the network management interface when you enable Bring Your Own License (BYOL). </p> <p>This operation can be run only by Amazon Web Services accounts that are enabled for BYOL. If your account isn't enabled for BYOL, you'll receive an <code>AccessDeniedException</code> error.</p> <p>The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.</p>

        Args:
            management_cidr_range_constraint: <p>The IP address range to search. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block).</p>
            max_results: <p>The maximum number of items to return.</p>
            next_token: <p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.list_available_management_cidr_ranges_request.ListAvailableManagementCidrRangesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.list_available_management_cidr_ranges_result.ListAvailableManagementCidrRangesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.list_available_management_cidr_ranges

            output, http_response = (
                capo_workspaces._operations.workspaces_service.list_available_management_cidr_ranges.list_available_management_cidr_ranges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.list_available_management_cidr_ranges_request.ListAvailableManagementCidrRangesRequest = {
            "management_cidr_range_constraint": management_cidr_range_constraint
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

    def migrate_workspace(
        self,
        source_workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        bundle_id: "capo_workspaces.types.bundle_id.BundleId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.migrate_workspace_result.MigrateWorkspaceResult":
        r"""<p>Migrates a WorkSpace from one operating system or bundle type to another, while retaining the data on the user volume.</p> <p>The migration process recreates the WorkSpace by using a new root volume from the target bundle image and the user volume from the last available snapshot of the original WorkSpace. During migration, the original <code>D:\Users\%USERNAME%</code> user profile folder is renamed to <code>D:\Users\%USERNAME%MMddyyTHHmmss%.NotMigrated</code>. A new <code>D:\Users\%USERNAME%\</code> folder is generated by the new OS. Certain files in the old user profile are moved to the new user profile.</p> <p>For available migration scenarios, details about what happens during migration, and best practices, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html">Migrate a WorkSpace</a>.</p> <note> <p>If the source WorkSpace has nested virtualization enabled and the target bundle does not support nested virtualization, the migration fails.</p> </note>

        Args:
            source_workspace_id: <p>The identifier of the WorkSpace to migrate from.</p>
            bundle_id: <p>The identifier of the target bundle type to migrate the WorkSpace to.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.migrate_workspace_request.MigrateWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.migrate_workspace_result.MigrateWorkspaceResult"
        ]:
            import capo_workspaces._operations.workspaces_service.migrate_workspace

            output, http_response = (
                capo_workspaces._operations.workspaces_service.migrate_workspace.migrate_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.migrate_workspace_request.MigrateWorkspaceRequest = {
            "source_workspace_id": source_workspace_id,
            "bundle_id": bundle_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_account(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        dedicated_tenancy_support: Optional[
            "capo_workspaces.types.dedicated_tenancy_support_enum.DedicatedTenancySupportEnum"
        ] = None,
        dedicated_tenancy_management_cidr_range: Optional[
            "capo_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
        ] = None,
    ) -> "capo_workspaces.types.modify_account_result.ModifyAccountResult":
        """<p>Modifies the configuration of Bring Your Own License (BYOL) for the specified account.</p>

        Args:
            dedicated_tenancy_support: <p>The status of BYOL.</p>
            dedicated_tenancy_management_cidr_range: <p>The IP address range, specified as an IPv4 CIDR block, for the management network interface. Specify an IP address range that is compatible with your network and in CIDR notation (that is, specify the range as an IPv4 CIDR block). The CIDR block size must be /16 (for example, 203.0.113.25/16). It must also be specified as available by the <code>ListAvailableManagementCidrRanges</code> operation.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_account_request.ModifyAccountRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_account_result.ModifyAccountResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_account

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_account.modify_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_account_request.ModifyAccountRequest = {}
        if dedicated_tenancy_support is not None:
            input_["dedicated_tenancy_support"] = dedicated_tenancy_support
        if dedicated_tenancy_management_cidr_range is not None:
            input_["dedicated_tenancy_management_cidr_range"] = (
                dedicated_tenancy_management_cidr_range
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_certificate_based_auth_properties(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        certificate_based_auth_properties: Optional[
            "capo_workspaces.types.certificate_based_auth_properties.CertificateBasedAuthProperties"
        ] = None,
        properties_to_delete: Optional[
            "capo_workspaces.types.deletable_certificate_based_auth_properties_list.DeletableCertificateBasedAuthPropertiesList"
        ] = None,
    ) -> "capo_workspaces.types.modify_certificate_based_auth_properties_result.ModifyCertificateBasedAuthPropertiesResult":
        """<p>Modifies the properties of the certificate-based authentication you want to use with your WorkSpaces.</p>

        Args:
            resource_id: <p>The resource identifiers, in the form of directory IDs.</p>
            certificate_based_auth_properties: <p>The properties of the certificate-based authentication.</p>
            properties_to_delete: <p>The properties of the certificate-based authentication you want to delete.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_certificate_based_auth_properties_request.ModifyCertificateBasedAuthPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_certificate_based_auth_properties_result.ModifyCertificateBasedAuthPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_certificate_based_auth_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_certificate_based_auth_properties.modify_certificate_based_auth_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_certificate_based_auth_properties_request.ModifyCertificateBasedAuthPropertiesRequest = {
            "resource_id": resource_id
        }
        if certificate_based_auth_properties is not None:
            input_["certificate_based_auth_properties"] = (
                certificate_based_auth_properties
            )
        if properties_to_delete is not None:
            input_["properties_to_delete"] = properties_to_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_client_properties(
        self,
        resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString",
        client_properties: "capo_workspaces.types.client_properties.ClientProperties",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.modify_client_properties_result.ModifyClientPropertiesResult":
        """<p>Modifies the properties of the specified Amazon WorkSpaces clients.</p>

        Args:
            resource_id: <p>The resource identifiers, in the form of directory IDs.</p>
            client_properties: <p>Information about the Amazon WorkSpaces client.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_client_properties_request.ModifyClientPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_client_properties_result.ModifyClientPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_client_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_client_properties.modify_client_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_client_properties_request.ModifyClientPropertiesRequest = {
            "resource_id": resource_id,
            "client_properties": client_properties,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_endpoint_encryption_mode(
        self,
        directory_id: "capo_workspaces.types.directory_id.DirectoryId",
        endpoint_encryption_mode: "capo_workspaces.types.endpoint_encryption_mode.EndpointEncryptionMode",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.modify_endpoint_encryption_mode_response.ModifyEndpointEncryptionModeResponse":
        """<p>Modifies the endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode. </p>

        Args:
            directory_id: <p> The identifier of the directory.</p>
            endpoint_encryption_mode: <p>The encryption mode used for endpoint connections when streaming to WorkSpaces Personal or WorkSpace Pools.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_endpoint_encryption_mode_request.ModifyEndpointEncryptionModeRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_endpoint_encryption_mode_response.ModifyEndpointEncryptionModeResponse"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_endpoint_encryption_mode

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_endpoint_encryption_mode.modify_endpoint_encryption_mode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_endpoint_encryption_mode_request.ModifyEndpointEncryptionModeRequest = {
            "directory_id": directory_id,
            "endpoint_encryption_mode": endpoint_encryption_mode,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_saml_properties(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        saml_properties: Optional[
            "capo_workspaces.types.saml_properties.SamlProperties"
        ] = None,
        properties_to_delete: Optional[
            "capo_workspaces.types.deletable_saml_properties_list.DeletableSamlPropertiesList"
        ] = None,
    ) -> (
        "capo_workspaces.types.modify_saml_properties_result.ModifySamlPropertiesResult"
    ):
        """<p>Modifies multiple properties related to SAML 2.0 authentication, including the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.</p>

        Args:
            resource_id: <p>The directory identifier for which you want to configure SAML properties.</p>
            saml_properties: <p>The properties for configuring SAML 2.0 authentication.</p>
            properties_to_delete: <p>The SAML properties to delete as part of your request.</p> <p>Specify one of the following options:</p> <ul> <li> <p> <code>SAML_PROPERTIES_USER_ACCESS_URL</code> to delete the user access URL.</p> </li> <li> <p> <code>SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME</code> to delete the relay state parameter name.</p> </li> </ul>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_saml_properties_request.ModifySamlPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_saml_properties_result.ModifySamlPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_saml_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_saml_properties.modify_saml_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_saml_properties_request.ModifySamlPropertiesRequest = {
            "resource_id": resource_id
        }
        if saml_properties is not None:
            input_["saml_properties"] = saml_properties
        if properties_to_delete is not None:
            input_["properties_to_delete"] = properties_to_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_selfservice_permissions(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        selfservice_permissions: "capo_workspaces.types.selfservice_permissions.SelfservicePermissions",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.modify_selfservice_permissions_result.ModifySelfservicePermissionsResult":
        """<p>Modifies the self-service WorkSpace management capabilities for your users. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/enable-user-self-service-workspace-management.html">Enable Self-Service WorkSpace Management Capabilities for Your Users</a>.</p>

        Args:
            resource_id: <p>The identifier of the directory.</p>
            selfservice_permissions: <p>The permissions to enable or disable self-service capabilities.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_selfservice_permissions_request.ModifySelfservicePermissionsRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_selfservice_permissions_result.ModifySelfservicePermissionsResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_selfservice_permissions

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_selfservice_permissions.modify_selfservice_permissions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_selfservice_permissions_request.ModifySelfservicePermissionsRequest = {
            "resource_id": resource_id,
            "selfservice_permissions": selfservice_permissions,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_streaming_properties(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        streaming_properties: Optional[
            "capo_workspaces.types.streaming_properties.StreamingProperties"
        ] = None,
    ) -> "capo_workspaces.types.modify_streaming_properties_result.ModifyStreamingPropertiesResult":
        """<p>Modifies the specified streaming properties.</p>

        Args:
            resource_id: <p>The identifier of the resource.</p>
            streaming_properties: <p>The streaming properties to configure.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_streaming_properties_request.ModifyStreamingPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_streaming_properties_result.ModifyStreamingPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_streaming_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_streaming_properties.modify_streaming_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_streaming_properties_request.ModifyStreamingPropertiesRequest = {
            "resource_id": resource_id
        }
        if streaming_properties is not None:
            input_["streaming_properties"] = streaming_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_workspace_access_properties(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        workspace_access_properties: "capo_workspaces.types.workspace_access_properties.WorkspaceAccessProperties",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.modify_workspace_access_properties_result.ModifyWorkspaceAccessPropertiesResult":
        """<p>Specifies which devices and operating systems users can use to access their WorkSpaces. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html#control-device-access"> Control Device Access</a>.</p>

        Args:
            resource_id: <p>The identifier of the directory.</p>
            workspace_access_properties: <p>The device types and operating systems to enable or disable for access.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_combination_exception.InvalidParameterCombinationException: <p>Two or more of the selected parameter values cannot be used together.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_workspace_access_properties_request.ModifyWorkspaceAccessPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_workspace_access_properties_result.ModifyWorkspaceAccessPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_workspace_access_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_workspace_access_properties.modify_workspace_access_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_workspace_access_properties_request.ModifyWorkspaceAccessPropertiesRequest = {
            "resource_id": resource_id,
            "workspace_access_properties": workspace_access_properties,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_workspace_creation_properties(
        self,
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        workspace_creation_properties: "capo_workspaces.types.workspace_creation_properties.WorkspaceCreationProperties",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.modify_workspace_creation_properties_result.ModifyWorkspaceCreationPropertiesResult":
        """<p>Modify the default properties used to create WorkSpaces.</p>

        Args:
            resource_id: <p>The identifier of the directory.</p>
            workspace_creation_properties: <p>The default properties for creating WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_workspace_creation_properties_request.ModifyWorkspaceCreationPropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_workspace_creation_properties_result.ModifyWorkspaceCreationPropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_workspace_creation_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_workspace_creation_properties.modify_workspace_creation_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_workspace_creation_properties_request.ModifyWorkspaceCreationPropertiesRequest = {
            "resource_id": resource_id,
            "workspace_creation_properties": workspace_creation_properties,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_workspace_properties(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        workspace_properties: Optional[
            "capo_workspaces.types.workspace_properties.WorkspaceProperties"
        ] = None,
        data_replication: Optional[
            "capo_workspaces.types.data_replication.DataReplication"
        ] = None,
    ) -> "capo_workspaces.types.modify_workspace_properties_result.ModifyWorkspacePropertiesResult":
        """<p>Modifies the specified WorkSpace properties. For important information about how to modify the size of the root and user volumes, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html"> Modify a WorkSpace</a>. </p> <note> <p>The <code>MANUAL</code> running mode value is only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use this value. For more information, see <a href="http://aws.amazon.com/workspaces/core/">Amazon WorkSpaces Core</a>.</p> </note>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>
            workspace_properties: <p>The properties of the WorkSpace.</p>
            data_replication: <p>Indicates the data replication status.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.unsupported_workspace_configuration_exception.UnsupportedWorkspaceConfigurationException: <p>The configuration of this WorkSpace is not supported for this operation. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/required-service-components.html">Required Configuration and Service Components for WorkSpaces </a>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_workspace_properties_request.ModifyWorkspacePropertiesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_workspace_properties_result.ModifyWorkspacePropertiesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_workspace_properties

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_workspace_properties.modify_workspace_properties(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_workspace_properties_request.ModifyWorkspacePropertiesRequest = {
            "workspace_id": workspace_id
        }
        if workspace_properties is not None:
            input_["workspace_properties"] = workspace_properties
        if data_replication is not None:
            input_["data_replication"] = data_replication

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_workspace_state(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        workspace_state: "capo_workspaces.types.target_workspace_state.TargetWorkspaceState",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> (
        "capo_workspaces.types.modify_workspace_state_result.ModifyWorkspaceStateResult"
    ):
        """<p>Sets the state of the specified WorkSpace.</p> <p>To maintain a WorkSpace without being interrupted, set the WorkSpace state to <code>ADMIN_MAINTENANCE</code>. WorkSpaces in this state do not respond to requests to reboot, stop, start, rebuild, or restore. An AutoStop WorkSpace in this state is not stopped. Users cannot log into a WorkSpace in the <code>ADMIN_MAINTENANCE</code> state.</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>
            workspace_state: <p>The WorkSpace state.</p>

        Raises:
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.modify_workspace_state_request.ModifyWorkspaceStateRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.modify_workspace_state_result.ModifyWorkspaceStateResult"
        ]:
            import capo_workspaces._operations.workspaces_service.modify_workspace_state

            output, http_response = (
                capo_workspaces._operations.workspaces_service.modify_workspace_state.modify_workspace_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.modify_workspace_state_request.ModifyWorkspaceStateRequest = {
            "workspace_id": workspace_id,
            "workspace_state": workspace_state,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reboot_workspaces(
        self,
        reboot_workspace_requests: "capo_workspaces.types.reboot_workspace_requests.RebootWorkspaceRequests",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.reboot_workspaces_result.RebootWorkspacesResult":
        """<p>Reboots the specified WorkSpaces.</p> <p>You cannot reboot a WorkSpace unless its state is <code>AVAILABLE</code>, <code>UNHEALTHY</code>, or <code>REBOOTING</code>. Reboot a WorkSpace in the <code>REBOOTING</code> state only if your WorkSpace has been stuck in the <code>REBOOTING</code> state for over 20 minutes.</p> <p>This operation is asynchronous and returns before the WorkSpaces have rebooted.</p>

        Args:
            reboot_workspace_requests: <p>The WorkSpaces to reboot. You can specify up to 25 WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.reboot_workspaces_request.RebootWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.reboot_workspaces_result.RebootWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.reboot_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.reboot_workspaces.reboot_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.reboot_workspaces_request.RebootWorkspacesRequest = {
            "reboot_workspace_requests": reboot_workspace_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rebuild_workspaces(
        self,
        rebuild_workspace_requests: "capo_workspaces.types.rebuild_workspace_requests.RebuildWorkspaceRequests",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.rebuild_workspaces_result.RebuildWorkspacesResult":
        """<p>Rebuilds the specified WorkSpace.</p> <p>You cannot rebuild a WorkSpace unless its state is <code>AVAILABLE</code>, <code>ERROR</code>, <code>UNHEALTHY</code>, <code>STOPPED</code>, or <code>REBOOTING</code>.</p> <p>Rebuilding a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/reset-workspace.html">Rebuild a WorkSpace</a>.</p> <p>This operation is asynchronous and returns before the WorkSpaces have been completely rebuilt.</p>

        Args:
            rebuild_workspace_requests: <p>The WorkSpace to rebuild. You can specify a single WorkSpace.</p>

        Raises:
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.rebuild_workspaces_request.RebuildWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.rebuild_workspaces_result.RebuildWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.rebuild_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.rebuild_workspaces.rebuild_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.rebuild_workspaces_request.RebuildWorkspacesRequest = {
            "rebuild_workspace_requests": rebuild_workspace_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_workspace_directory(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        directory_id: Optional["capo_workspaces.types.directory_id.DirectoryId"] = None,
        subnet_ids: Optional["capo_workspaces.types.subnet_ids.SubnetIds"] = None,
        enable_self_service: Optional[
            "capo_workspaces.types.boolean_object.BooleanObject"
        ] = None,
        tenancy: Optional["capo_workspaces.types.tenancy.Tenancy"] = None,
        tags: Optional["capo_workspaces.types.tag_list.TagList"] = None,
        workspace_directory_name: Optional[
            "capo_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
        ] = None,
        workspace_directory_description: Optional[
            "capo_workspaces.types.workspace_directory_description.WorkspaceDirectoryDescription"
        ] = None,
        user_identity_type: Optional[
            "capo_workspaces.types.user_identity_type.UserIdentityType"
        ] = None,
        idc_instance_arn: Optional["capo_workspaces.types.arn.ARN"] = None,
        microsoft_entra_config: Optional[
            "capo_workspaces.types.microsoft_entra_config.MicrosoftEntraConfig"
        ] = None,
        workspace_type: Optional[
            "capo_workspaces.types.workspace_type.WorkspaceType"
        ] = None,
        active_directory_config: Optional[
            "capo_workspaces.types.active_directory_config.ActiveDirectoryConfig"
        ] = None,
    ) -> "capo_workspaces.types.register_workspace_directory_result.RegisterWorkspaceDirectoryResult":
        """<p>Registers the specified directory. This operation is asynchronous and returns before the WorkSpace directory is registered. If this is the first time you are registering a directory, you will need to create the workspaces_DefaultRole role before you can register a directory. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role"> Creating the workspaces_DefaultRole Role</a>.</p>

        Args:
            directory_id: <p>The identifier of the directory. You cannot register a directory if it does not have a status of Active. If the directory does not have a status of Active, you will receive an InvalidResourceStateException error. If you have already registered the maximum number of directories that you can register with Amazon WorkSpaces, you will receive a ResourceLimitExceededException error. Deregister directories that you are not using for WorkSpaces, and try again.</p>
            subnet_ids: <p>The identifiers of the subnets for your virtual private cloud (VPC). Make sure that the subnets are in supported Availability Zones. The subnets must also be in separate Availability Zones. If these conditions are not met, you will receive an OperationNotSupportedException error.</p>
            enable_self_service: <p>Indicates whether self-service capabilities are enabled or disabled.</p>
            tenancy: <p>Indicates whether your WorkSpace directory is dedicated or shared. To use Bring Your Own License (BYOL) images, this value must be set to <code>DEDICATED</code> and your Amazon Web Services account must be enabled for BYOL. If your account has not been enabled for BYOL, you will receive an InvalidParameterValuesException error. For more information about BYOL images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html">Bring Your Own Windows Desktop Images</a>.</p>
            tags: <p>The tags associated with the directory.</p>
            workspace_directory_name: <p>The name of the directory to register.</p>
            workspace_directory_description: <p>Description of the directory to register.</p>
            user_identity_type: <p>The type of identity management the user is using.</p>
            idc_instance_arn: <p>The Amazon Resource Name (ARN) of the identity center instance.</p>
            microsoft_entra_config: <p>The details about Microsoft Entra config.</p>
            workspace_type: <p>Indicates whether the directory's WorkSpace type is personal or pools.</p>
            active_directory_config: <p>The active directory config of the directory.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.unsupported_network_configuration_exception.UnsupportedNetworkConfigurationException: <p>The configuration of this network is not supported for this operation, or your network configuration conflicts with the Amazon WorkSpaces management network IP range. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html"> Configure a VPC for Amazon WorkSpaces</a>.</p>
            capo_workspaces.errors.workspaces_default_role_not_found_exception.WorkspacesDefaultRoleNotFoundException: <p>The workspaces_DefaultRole role could not be found. If this is the first time you are registering a directory, you will need to create the workspaces_DefaultRole role before you can register a directory. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role">Creating the workspaces_DefaultRole Role</a>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.register_workspace_directory_request.RegisterWorkspaceDirectoryRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.register_workspace_directory_result.RegisterWorkspaceDirectoryResult"
        ]:
            import capo_workspaces._operations.workspaces_service.register_workspace_directory

            output, http_response = (
                capo_workspaces._operations.workspaces_service.register_workspace_directory.register_workspace_directory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.register_workspace_directory_request.RegisterWorkspaceDirectoryRequest = {}
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if subnet_ids is not None:
            input_["subnet_ids"] = subnet_ids
        if enable_self_service is not None:
            input_["enable_self_service"] = enable_self_service
        if tenancy is not None:
            input_["tenancy"] = tenancy
        if tags is not None:
            input_["tags"] = tags
        if workspace_directory_name is not None:
            input_["workspace_directory_name"] = workspace_directory_name
        if workspace_directory_description is not None:
            input_["workspace_directory_description"] = workspace_directory_description
        if user_identity_type is not None:
            input_["user_identity_type"] = user_identity_type
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if microsoft_entra_config is not None:
            input_["microsoft_entra_config"] = microsoft_entra_config
        if workspace_type is not None:
            input_["workspace_type"] = workspace_type
        if active_directory_config is not None:
            input_["active_directory_config"] = active_directory_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reject_account_link_invitation(
        self,
        link_id: "capo_workspaces.types.link_id.LinkId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        client_token: Optional["capo_workspaces.types.client_token.ClientToken"] = None,
    ) -> "capo_workspaces.types.reject_account_link_invitation_result.RejectAccountLinkInvitationResult":
        """<p>Rejects the account link invitation.</p>

        Args:
            link_id: <p>The identifier of the account link</p>
            client_token: <p>The client token of the account link invitation to reject.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.conflict_exception.ConflictException: <p>The <code>TargetAccountId</code> is already linked or invited.</p>
            capo_workspaces.errors.internal_server_exception.InternalServerException: <p>Unexpected server error occured.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.validation_exception.ValidationException: <p>You either haven't provided a <code>TargetAccountId</code> or are using the same value for <code>TargetAccountId</code> and <code>SourceAccountId</code>.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.reject_account_link_invitation_request.RejectAccountLinkInvitationRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.reject_account_link_invitation_result.RejectAccountLinkInvitationResult"
        ]:
            import capo_workspaces._operations.workspaces_service.reject_account_link_invitation

            output, http_response = (
                capo_workspaces._operations.workspaces_service.reject_account_link_invitation.reject_account_link_invitation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.reject_account_link_invitation_request.RejectAccountLinkInvitationRequest = {
            "link_id": link_id
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restore_workspace(
        self,
        workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.restore_workspace_result.RestoreWorkspaceResult":
        """<p>Restores the specified WorkSpace to its last known healthy state.</p> <p>You cannot restore a WorkSpace unless its state is <code> AVAILABLE</code>, <code>ERROR</code>, <code>UNHEALTHY</code>, or <code>STOPPED</code>.</p> <p>Restoring a WorkSpace is a potentially destructive action that can result in the loss of data. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html">Restore a WorkSpace</a>.</p> <p>This operation is asynchronous and returns before the WorkSpace is completely restored.</p>

        Args:
            workspace_id: <p>The identifier of the WorkSpace.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.restore_workspace_request.RestoreWorkspaceRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.restore_workspace_result.RestoreWorkspaceResult"
        ]:
            import capo_workspaces._operations.workspaces_service.restore_workspace

            output, http_response = (
                capo_workspaces._operations.workspaces_service.restore_workspace.restore_workspace(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.restore_workspace_request.RestoreWorkspaceRequest = {
            "workspace_id": workspace_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def revoke_ip_rules(
        self,
        group_id: "capo_workspaces.types.ip_group_id.IpGroupId",
        user_rules: "capo_workspaces.types.ip_revoked_rule_list.IpRevokedRuleList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.revoke_ip_rules_result.RevokeIpRulesResult":
        """<p>Removes one or more rules from the specified IP access control group.</p>

        Args:
            group_id: <p>The identifier of the group.</p>
            user_rules: <p>The rules to remove from the group.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.revoke_ip_rules_request.RevokeIpRulesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.revoke_ip_rules_result.RevokeIpRulesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.revoke_ip_rules

            output, http_response = (
                capo_workspaces._operations.workspaces_service.revoke_ip_rules.revoke_ip_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.revoke_ip_rules_request.RevokeIpRulesRequest = {
            "group_id": group_id,
            "user_rules": user_rules,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_workspaces(
        self,
        start_workspace_requests: "capo_workspaces.types.start_workspace_requests.StartWorkspaceRequests",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.start_workspaces_result.StartWorkspacesResult":
        """<p>Starts the specified WorkSpaces.</p> <p>You cannot start a WorkSpace unless it has a running mode of <code>AutoStop</code> or <code>Manual</code> and a state of <code>STOPPED</code>.</p>

        Args:
            start_workspace_requests: <p>The WorkSpaces to start. You can specify up to 25 WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.start_workspaces_request.StartWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.start_workspaces_result.StartWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.start_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.start_workspaces.start_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.start_workspaces_request.StartWorkspacesRequest = {
            "start_workspace_requests": start_workspace_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_workspaces_pool(
        self,
        pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.start_workspaces_pool_result.StartWorkspacesPoolResult":
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Starts the specified pool.</p> <p>You cannot start a pool unless it has a running mode of <code>AutoStop</code> and a state of <code>STOPPED</code>.</p>

        Args:
            pool_id: <p>The identifier of the pool.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.start_workspaces_pool_request.StartWorkspacesPoolRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.start_workspaces_pool_result.StartWorkspacesPoolResult"
        ]:
            import capo_workspaces._operations.workspaces_service.start_workspaces_pool

            output, http_response = (
                capo_workspaces._operations.workspaces_service.start_workspaces_pool.start_workspaces_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.start_workspaces_pool_request.StartWorkspacesPoolRequest = {
            "pool_id": pool_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_workspaces(
        self,
        stop_workspace_requests: "capo_workspaces.types.stop_workspace_requests.StopWorkspaceRequests",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.stop_workspaces_result.StopWorkspacesResult":
        """<p>Stops the specified WorkSpaces.</p> <p>You cannot stop a WorkSpace unless it has a running mode of <code>AutoStop</code> or <code>Manual</code> and a state of <code>AVAILABLE</code>, <code>IMPAIRED</code>, <code>UNHEALTHY</code>, or <code>ERROR</code>.</p>

        Args:
            stop_workspace_requests: <p>The WorkSpaces to stop. You can specify up to 25 WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.stop_workspaces_request.StopWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.stop_workspaces_result.StopWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.stop_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.stop_workspaces.stop_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.stop_workspaces_request.StopWorkspacesRequest = {
            "stop_workspace_requests": stop_workspace_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_workspaces_pool(
        self,
        pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.stop_workspaces_pool_result.StopWorkspacesPoolResult":
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Stops the specified pool.</p> <p>You cannot stop a WorkSpace pool unless it has a running mode of <code>AutoStop</code> and a state of <code>AVAILABLE</code>, <code>IMPAIRED</code>, <code>UNHEALTHY</code>, or <code>ERROR</code>.</p>

        Args:
            pool_id: <p>The identifier of the pool.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.stop_workspaces_pool_request.StopWorkspacesPoolRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.stop_workspaces_pool_result.StopWorkspacesPoolResult"
        ]:
            import capo_workspaces._operations.workspaces_service.stop_workspaces_pool

            output, http_response = (
                capo_workspaces._operations.workspaces_service.stop_workspaces_pool.stop_workspaces_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.stop_workspaces_pool_request.StopWorkspacesPoolRequest = {
            "pool_id": pool_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_workspaces(
        self,
        terminate_workspace_requests: "capo_workspaces.types.terminate_workspace_requests.TerminateWorkspaceRequests",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.terminate_workspaces_result.TerminateWorkspacesResult":
        """<p>Terminates the specified WorkSpaces.</p> <important> <p>Terminating a WorkSpace is a permanent action and cannot be undone. The user's data is destroyed. If you need to archive any user data, contact Amazon Web Services Support before terminating the WorkSpace.</p> </important> <p>You can terminate a WorkSpace that is in any state except <code>SUSPENDED</code>.</p> <p>This operation is asynchronous and returns before the WorkSpaces have been completely terminated. After a WorkSpace is terminated, the <code>TERMINATED</code> state is returned only briefly before the WorkSpace directory metadata is cleaned up, so this state is rarely returned. To confirm that a WorkSpace is terminated, check for the WorkSpace ID by using <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaces.html"> DescribeWorkSpaces</a>. If the WorkSpace ID isn't returned, then the WorkSpace has been successfully terminated.</p> <note> <p>Simple AD and AD Connector are made available to you free of charge to use with WorkSpaces. If there are no WorkSpaces being used with your Simple AD or AD Connector directory for 30 consecutive days, this directory will be automatically deregistered for use with Amazon WorkSpaces, and you will be charged for this directory as per the <a href="http://aws.amazon.com/directoryservice/pricing/">Directory Service pricing terms</a>.</p> <p>To delete empty directories, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces-directory.html"> Delete the Directory for Your WorkSpaces</a>. If you delete your Simple AD or AD Connector directory, you can always create a new one when you want to start using WorkSpaces again.</p> </note>

        Args:
            terminate_workspace_requests: <p>The WorkSpaces to terminate. You can specify up to 25 WorkSpaces.</p>

        Raises:
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.terminate_workspaces_request.TerminateWorkspacesRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.terminate_workspaces_result.TerminateWorkspacesResult"
        ]:
            import capo_workspaces._operations.workspaces_service.terminate_workspaces

            output, http_response = (
                capo_workspaces._operations.workspaces_service.terminate_workspaces.terminate_workspaces(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.terminate_workspaces_request.TerminateWorkspacesRequest = {
            "terminate_workspace_requests": terminate_workspace_requests
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_workspaces_pool(
        self,
        pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.terminate_workspaces_pool_result.TerminateWorkspacesPoolResult":
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Terminates the specified pool.</p>

        Args:
            pool_id: <p>The identifier of the pool.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.terminate_workspaces_pool_request.TerminateWorkspacesPoolRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.terminate_workspaces_pool_result.TerminateWorkspacesPoolResult"
        ]:
            import capo_workspaces._operations.workspaces_service.terminate_workspaces_pool

            output, http_response = (
                capo_workspaces._operations.workspaces_service.terminate_workspaces_pool.terminate_workspaces_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.terminate_workspaces_pool_request.TerminateWorkspacesPoolRequest = {
            "pool_id": pool_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_workspaces_pool_session(
        self,
        session_id: "capo_workspaces.types.amazon_uuid.AmazonUuid",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.terminate_workspaces_pool_session_result.TerminateWorkspacesPoolSessionResult":
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Terminates the pool session.</p>

        Args:
            session_id: <p>The identifier of the pool session.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.terminate_workspaces_pool_session_request.TerminateWorkspacesPoolSessionRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.terminate_workspaces_pool_session_result.TerminateWorkspacesPoolSessionResult"
        ]:
            import capo_workspaces._operations.workspaces_service.terminate_workspaces_pool_session

            output, http_response = (
                capo_workspaces._operations.workspaces_service.terminate_workspaces_pool_session.terminate_workspaces_pool_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.terminate_workspaces_pool_session_request.TerminateWorkspacesPoolSessionRequest = {
            "session_id": session_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_connect_client_add_in(
        self,
        add_in_id: "capo_workspaces.types.amazon_uuid.AmazonUuid",
        resource_id: "capo_workspaces.types.directory_id.DirectoryId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        name: Optional["capo_workspaces.types.add_in_name.AddInName"] = None,
        url: Optional["capo_workspaces.types.add_in_url.AddInUrl"] = None,
    ) -> "capo_workspaces.types.update_connect_client_add_in_result.UpdateConnectClientAddInResult":
        """<p>Updates a Connect Customer client add-in. Use this action to update the name and endpoint URL of a Connect Customer client add-in.</p>

        Args:
            add_in_id: <p>The identifier of the client add-in to update.</p>
            resource_id: <p>The directory identifier for which the client add-in is configured.</p>
            name: <p>The name of the client add-in.</p>
            url: <p>The endpoint URL of the Connect Customer client add-in.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.update_connect_client_add_in_request.UpdateConnectClientAddInRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.update_connect_client_add_in_result.UpdateConnectClientAddInResult"
        ]:
            import capo_workspaces._operations.workspaces_service.update_connect_client_add_in

            output, http_response = (
                capo_workspaces._operations.workspaces_service.update_connect_client_add_in.update_connect_client_add_in(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.update_connect_client_add_in_request.UpdateConnectClientAddInRequest = {
            "add_in_id": add_in_id,
            "resource_id": resource_id,
        }
        if name is not None:
            input_["name"] = name
        if url is not None:
            input_["url"] = url

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_connection_alias_permission(
        self,
        alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId",
        connection_alias_permission: "capo_workspaces.types.connection_alias_permission.ConnectionAliasPermission",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.update_connection_alias_permission_result.UpdateConnectionAliasPermissionResult":
        """<p>Shares or unshares a connection alias with one account by specifying whether that account has permission to associate the connection alias with a directory. If the association permission is granted, the connection alias is shared with that account. If the association permission is revoked, the connection alias is unshared with the account. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html"> Cross-Region Redirection for Amazon WorkSpaces</a>.</p> <note> <ul> <li> <p>Before performing this operation, call <a href="https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeConnectionAliases.html"> DescribeConnectionAliases</a> to make sure that the current state of the connection alias is <code>CREATED</code>.</p> </li> <li> <p>To delete a connection alias that has been shared, the shared account must first disassociate the connection alias from any directories it has been associated with. Then you must unshare the connection alias from the account it has been shared with. You can delete a connection alias only after it is no longer shared with any accounts or associated with any directories.</p> </li> </ul> </note>

        Args:
            alias_id: <p>The identifier of the connection alias that you want to update permissions for.</p>
            connection_alias_permission: <p>Indicates whether to share or unshare the connection alias with the specified Amazon Web Services account.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_associated_exception.ResourceAssociatedException: <p>The resource is associated with a directory.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.update_connection_alias_permission_request.UpdateConnectionAliasPermissionRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.update_connection_alias_permission_result.UpdateConnectionAliasPermissionResult"
        ]:
            import capo_workspaces._operations.workspaces_service.update_connection_alias_permission

            output, http_response = (
                capo_workspaces._operations.workspaces_service.update_connection_alias_permission.update_connection_alias_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.update_connection_alias_permission_request.UpdateConnectionAliasPermissionRequest = {
            "alias_id": alias_id,
            "connection_alias_permission": connection_alias_permission,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rules_of_ip_group(
        self,
        group_id: "capo_workspaces.types.ip_group_id.IpGroupId",
        user_rules: "capo_workspaces.types.ip_rule_list.IpRuleList",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.update_rules_of_ip_group_result.UpdateRulesOfIpGroupResult":
        """<p>Replaces the current rules of the specified IP access control group with the specified rules.</p>

        Args:
            group_id: <p>The identifier of the group.</p>
            user_rules: <p>One or more rules.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.update_rules_of_ip_group_request.UpdateRulesOfIpGroupRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.update_rules_of_ip_group_result.UpdateRulesOfIpGroupResult"
        ]:
            import capo_workspaces._operations.workspaces_service.update_rules_of_ip_group

            output, http_response = (
                capo_workspaces._operations.workspaces_service.update_rules_of_ip_group.update_rules_of_ip_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.update_rules_of_ip_group_request.UpdateRulesOfIpGroupRequest = {
            "group_id": group_id,
            "user_rules": user_rules,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace_bundle(
        self,
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        bundle_id: Optional["capo_workspaces.types.bundle_id.BundleId"] = None,
        image_id: Optional[
            "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
        ] = None,
    ) -> "capo_workspaces.types.update_workspace_bundle_result.UpdateWorkspaceBundleResult":
        """<p>Updates a WorkSpace bundle with a new image. For more information about updating WorkSpace bundles, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/update-custom-bundle.html"> Update a Custom WorkSpaces Bundle</a>.</p> <important> <p>Existing WorkSpaces aren't automatically updated when you update the bundle that they're based on. To update existing WorkSpaces that are based on a bundle that you've updated, you must either rebuild the WorkSpaces or delete and recreate them.</p> </important>

        Args:
            bundle_id: <p>The identifier of the bundle.</p>
            image_id: <p>The identifier of the image.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.update_workspace_bundle_request.UpdateWorkspaceBundleRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.update_workspace_bundle_result.UpdateWorkspaceBundleResult"
        ]:
            import capo_workspaces._operations.workspaces_service.update_workspace_bundle

            output, http_response = (
                capo_workspaces._operations.workspaces_service.update_workspace_bundle.update_workspace_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.update_workspace_bundle_request.UpdateWorkspaceBundleRequest = {}
        if bundle_id is not None:
            input_["bundle_id"] = bundle_id
        if image_id is not None:
            input_["image_id"] = image_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspace_image_permission(
        self,
        image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId",
        allow_copy_image: "capo_workspaces.types.boolean_object.BooleanObject",
        shared_account_id: "capo_workspaces.types.aws_account.AwsAccount",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
    ) -> "capo_workspaces.types.update_workspace_image_permission_result.UpdateWorkspaceImagePermissionResult":
        """<p>Shares or unshares an image with one account in the same Amazon Web Services Region by specifying whether that account has permission to copy the image. If the copy image permission is granted, the image is shared with that account. If the copy image permission is revoked, the image is unshared with the account.</p> <p>After an image has been shared, the recipient account can copy the image to other Regions as needed.</p> <p>In the China (Ningxia) Region, you can copy images only within the same Region.</p> <p>In Amazon Web Services GovCloud (US), to copy images to and from other Regions, contact Amazon Web Services Support.</p> <p>For more information about sharing images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/share-custom-image.html"> Share or Unshare a Custom WorkSpaces Image</a>.</p> <note> <ul> <li> <p>To delete an image that has been shared, you must unshare the image before you delete it.</p> </li> <li> <p>Sharing Bring Your Own License (BYOL) images across Amazon Web Services accounts isn't supported at this time in Amazon Web Services GovCloud (US). To share BYOL images across accounts in Amazon Web Services GovCloud (US), contact Amazon Web Services Support.</p> </li> </ul> </note>

        Args:
            image_id: <p>The identifier of the image.</p>
            allow_copy_image: <p>The permission to copy the image. This permission can be revoked only after an image has been shared.</p>
            shared_account_id: <p>The identifier of the Amazon Web Services account to share or unshare the image with.</p> <important> <p>Before sharing the image, confirm that you are sharing to the correct Amazon Web Services account ID.</p> </important>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.resource_unavailable_exception.ResourceUnavailableException: <p>The specified resource is not available.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.update_workspace_image_permission_request.UpdateWorkspaceImagePermissionRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.update_workspace_image_permission_result.UpdateWorkspaceImagePermissionResult"
        ]:
            import capo_workspaces._operations.workspaces_service.update_workspace_image_permission

            output, http_response = (
                capo_workspaces._operations.workspaces_service.update_workspace_image_permission.update_workspace_image_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.update_workspace_image_permission_request.UpdateWorkspaceImagePermissionRequest = {
            "image_id": image_id,
            "allow_copy_image": allow_copy_image,
            "shared_account_id": shared_account_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workspaces_pool(
        self,
        pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId",
        *,
        config_overrides: Optional[WorkSpacesClientConfig] = None,
        description: Optional[
            "capo_workspaces.types.update_description.UpdateDescription"
        ] = None,
        bundle_id: Optional["capo_workspaces.types.bundle_id.BundleId"] = None,
        directory_id: Optional["capo_workspaces.types.directory_id.DirectoryId"] = None,
        capacity: Optional["capo_workspaces.types.capacity.Capacity"] = None,
        application_settings: Optional[
            "capo_workspaces.types.application_settings_request.ApplicationSettingsRequest"
        ] = None,
        timeout_settings: Optional[
            "capo_workspaces.types.timeout_settings.TimeoutSettings"
        ] = None,
        running_mode: Optional[
            "capo_workspaces.types.pools_running_mode.PoolsRunningMode"
        ] = None,
    ) -> (
        "capo_workspaces.types.update_workspaces_pool_result.UpdateWorkspacesPoolResult"
    ):
        """<note> <p>End of support notice: On December 31, 2027, Amazon Web Services will end support for Amazon WorkSpaces Pools. After December 31, 2027, you will no longer be able to access the Amazon WorkSpaces Pools console or Amazon WorkSpaces Pools resources. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/wsp-pools-end-of-support.html">Amazon WorkSpaces Pools end of support</a>. </p> </note> <p>Updates the specified pool.</p>

        Args:
            pool_id: <p>The identifier of the specified pool to update.</p>
            description: <p>Describes the specified pool to update.</p>
            bundle_id: <p>The identifier of the bundle.</p>
            directory_id: <p>The identifier of the directory.</p>
            capacity: <p>The desired capacity for the pool.</p>
            application_settings: <p>The persistent application settings for users in the pool.</p>
            timeout_settings: <p>Indicates the timeout settings of the specified pool.</p>
            running_mode: <p>The desired running mode for the pool. The running mode can only be updated when the pool is in a stopped state.</p>

        Raises:
            capo_workspaces.errors.access_denied_exception.AccessDeniedException: <p>The user is not authorized to access a resource.</p>
            capo_workspaces.errors.invalid_parameter_values_exception.InvalidParameterValuesException: <p>One or more parameter values are not valid.</p>
            capo_workspaces.errors.invalid_resource_state_exception.InvalidResourceStateException: <p>The state of the resource is not valid for this operation.</p>
            capo_workspaces.errors.operation_in_progress_exception.OperationInProgressException: <p>The properties of this WorkSpace are currently being modified. Try again in a moment.</p>
            capo_workspaces.errors.operation_not_supported_exception.OperationNotSupportedException: <p>This operation is not supported.</p>
            capo_workspaces.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Your resource limits have been exceeded.</p>
            capo_workspaces.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_workspaces.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_workspaces.types.update_workspaces_pool_request.UpdateWorkspacesPoolRequest]",
        ) -> OperationResponse[
            "capo_workspaces.types.update_workspaces_pool_result.UpdateWorkspacesPoolResult"
        ]:
            import capo_workspaces._operations.workspaces_service.update_workspaces_pool

            output, http_response = (
                capo_workspaces._operations.workspaces_service.update_workspaces_pool.update_workspaces_pool(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_workspaces.types.update_workspaces_pool_request.UpdateWorkspacesPoolRequest = {
            "pool_id": pool_id
        }
        if description is not None:
            input_["description"] = description
        if bundle_id is not None:
            input_["bundle_id"] = bundle_id
        if directory_id is not None:
            input_["directory_id"] = directory_id
        if capacity is not None:
            input_["capacity"] = capacity
        if application_settings is not None:
            input_["application_settings"] = application_settings
        if timeout_settings is not None:
            input_["timeout_settings"] = timeout_settings
        if running_mode is not None:
            input_["running_mode"] = running_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
