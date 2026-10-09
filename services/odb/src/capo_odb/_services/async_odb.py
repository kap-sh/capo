"""Generated from Smithy shape ``com.amazonaws.odb#Odb``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_odb._auth._signers
import capo_odb._auth._sigv4
from capo_odb._auth._identity import Credentials
from capo_odb._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_odb._auth._zapros_handler import AuthMiddleware
from capo_odb._pagination import resolve_path as _resolve_path
from capo_odb._resources.odb.autonomous_database_backup_resource import (
    AsyncAutonomousDatabaseBackupResource,
)
from capo_odb._resources.odb.autonomous_database_resource import (
    AsyncAutonomousDatabaseResource,
)
from capo_odb._resources.odb.cloud_autonomous_vm_cluster_resource import (
    AsyncCloudAutonomousVmClusterResource,
)
from capo_odb._resources.odb.cloud_exadata_infrastructure_resource import (
    AsyncCloudExadataInfrastructureResource,
)
from capo_odb._resources.odb.cloud_vm_cluster_resource import (
    AsyncCloudVmClusterResource,
)
from capo_odb._resources.odb.db_node_resource import AsyncDbNodeResource
from capo_odb._resources.odb.exadb_vm_cluster_resource import (
    AsyncExadbVmClusterResource,
)
from capo_odb._resources.odb.exascale_db_storage_vault_resource import (
    AsyncExascaleDbStorageVaultResource,
)
from capo_odb._resources.odb.odb_network_resource import AsyncOdbNetworkResource
from capo_odb._resources.odb.odb_peering_connection_resource import (
    AsyncOdbPeeringConnectionResource,
)
from capo_odb._services._aws_config import aaws_config
from capo_odb._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_odb.types.accept_marketplace_registration_input
    import capo_odb.types.accept_marketplace_registration_output
    import capo_odb.types.access
    import capo_odb.types.admin_password_source
    import capo_odb.types.admin_password_source_configuration_input
    import capo_odb.types.arn
    import capo_odb.types.associate_iam_role_to_resource_input
    import capo_odb.types.associate_iam_role_to_resource_output
    import capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input
    import capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output
    import capo_odb.types.autonomous_database_backup_status
    import capo_odb.types.autonomous_database_backup_summary
    import capo_odb.types.autonomous_database_backup_type
    import capo_odb.types.autonomous_database_character_set_summary
    import capo_odb.types.autonomous_database_peer_summary
    import capo_odb.types.autonomous_database_summary
    import capo_odb.types.autonomous_database_version_summary
    import capo_odb.types.autonomous_maintenance_schedule_type
    import capo_odb.types.autonomous_virtual_machine_summary
    import capo_odb.types.character_set_type
    import capo_odb.types.cloud_autonomous_vm_cluster_summary
    import capo_odb.types.cloud_exadata_infrastructure_summary
    import capo_odb.types.cloud_vm_cluster_summary
    import capo_odb.types.cluster_name
    import capo_odb.types.create_autonomous_database_backup_input
    import capo_odb.types.create_autonomous_database_backup_output
    import capo_odb.types.create_autonomous_database_input
    import capo_odb.types.create_autonomous_database_output
    import capo_odb.types.create_autonomous_database_wallet_input
    import capo_odb.types.create_autonomous_database_wallet_output
    import capo_odb.types.create_cloud_autonomous_vm_cluster_input
    import capo_odb.types.create_cloud_autonomous_vm_cluster_output
    import capo_odb.types.create_cloud_exadata_infrastructure_input
    import capo_odb.types.create_cloud_exadata_infrastructure_output
    import capo_odb.types.create_cloud_vm_cluster_input
    import capo_odb.types.create_cloud_vm_cluster_output
    import capo_odb.types.create_exadb_vm_cluster_input
    import capo_odb.types.create_exadb_vm_cluster_output
    import capo_odb.types.create_exascale_db_storage_vault_input
    import capo_odb.types.create_exascale_db_storage_vault_output
    import capo_odb.types.create_odb_network_input
    import capo_odb.types.create_odb_network_output
    import capo_odb.types.create_odb_peering_connection_input
    import capo_odb.types.create_odb_peering_connection_output
    import capo_odb.types.customer_contacts
    import capo_odb.types.data_collection_options
    import capo_odb.types.database_edition
    import capo_odb.types.database_tool_list
    import capo_odb.types.db_node_summary
    import capo_odb.types.db_server_summary
    import capo_odb.types.db_system_shape_summary
    import capo_odb.types.db_workload
    import capo_odb.types.delete_autonomous_database_backup_input
    import capo_odb.types.delete_autonomous_database_backup_output
    import capo_odb.types.delete_autonomous_database_input
    import capo_odb.types.delete_autonomous_database_output
    import capo_odb.types.delete_cloud_autonomous_vm_cluster_input
    import capo_odb.types.delete_cloud_autonomous_vm_cluster_output
    import capo_odb.types.delete_cloud_exadata_infrastructure_input
    import capo_odb.types.delete_cloud_exadata_infrastructure_output
    import capo_odb.types.delete_cloud_vm_cluster_input
    import capo_odb.types.delete_cloud_vm_cluster_output
    import capo_odb.types.delete_exadb_vm_cluster_input
    import capo_odb.types.delete_exadb_vm_cluster_output
    import capo_odb.types.delete_exascale_db_storage_vault_input
    import capo_odb.types.delete_exascale_db_storage_vault_output
    import capo_odb.types.delete_odb_network_input
    import capo_odb.types.delete_odb_network_output
    import capo_odb.types.delete_odb_peering_connection_input
    import capo_odb.types.delete_odb_peering_connection_output
    import capo_odb.types.disassociate_iam_role_from_resource_input
    import capo_odb.types.disassociate_iam_role_from_resource_output
    import capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input
    import capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output
    import capo_odb.types.encryption_key_configuration_input
    import capo_odb.types.encryption_key_provider_input
    import capo_odb.types.exadb_vm_cluster_summary
    import capo_odb.types.exascale_db_storage_vault_summary
    import capo_odb.types.failover_autonomous_database_input
    import capo_odb.types.failover_autonomous_database_output
    import capo_odb.types.flex_component_summary
    import capo_odb.types.general_input_string
    import capo_odb.types.get_autonomous_database_backup_input
    import capo_odb.types.get_autonomous_database_backup_output
    import capo_odb.types.get_autonomous_database_input
    import capo_odb.types.get_autonomous_database_output
    import capo_odb.types.get_autonomous_database_wallet_details_input
    import capo_odb.types.get_autonomous_database_wallet_details_output
    import capo_odb.types.get_cloud_autonomous_vm_cluster_input
    import capo_odb.types.get_cloud_autonomous_vm_cluster_output
    import capo_odb.types.get_cloud_exadata_infrastructure_input
    import capo_odb.types.get_cloud_exadata_infrastructure_output
    import capo_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input
    import capo_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output
    import capo_odb.types.get_cloud_vm_cluster_input
    import capo_odb.types.get_cloud_vm_cluster_output
    import capo_odb.types.get_db_node_input
    import capo_odb.types.get_db_node_output
    import capo_odb.types.get_db_server_input
    import capo_odb.types.get_db_server_output
    import capo_odb.types.get_exadb_vm_cluster_input
    import capo_odb.types.get_exadb_vm_cluster_output
    import capo_odb.types.get_exascale_db_storage_vault_input
    import capo_odb.types.get_exascale_db_storage_vault_output
    import capo_odb.types.get_oci_onboarding_status_input
    import capo_odb.types.get_oci_onboarding_status_output
    import capo_odb.types.get_odb_network_input
    import capo_odb.types.get_odb_network_output
    import capo_odb.types.get_odb_peering_connection_input
    import capo_odb.types.get_odb_peering_connection_output
    import capo_odb.types.gi_minor_version_summary
    import capo_odb.types.gi_version_summary
    import capo_odb.types.hostname
    import capo_odb.types.initialize_service_input
    import capo_odb.types.initialize_service_output
    import capo_odb.types.license_model
    import capo_odb.types.list_autonomous_database_backups_input
    import capo_odb.types.list_autonomous_database_backups_output
    import capo_odb.types.list_autonomous_database_character_sets_input
    import capo_odb.types.list_autonomous_database_character_sets_output
    import capo_odb.types.list_autonomous_database_clones_input
    import capo_odb.types.list_autonomous_database_clones_output
    import capo_odb.types.list_autonomous_database_peers_input
    import capo_odb.types.list_autonomous_database_peers_output
    import capo_odb.types.list_autonomous_database_versions_input
    import capo_odb.types.list_autonomous_database_versions_output
    import capo_odb.types.list_autonomous_databases_input
    import capo_odb.types.list_autonomous_databases_output
    import capo_odb.types.list_autonomous_virtual_machines_input
    import capo_odb.types.list_autonomous_virtual_machines_output
    import capo_odb.types.list_cloud_autonomous_vm_clusters_input
    import capo_odb.types.list_cloud_autonomous_vm_clusters_output
    import capo_odb.types.list_cloud_exadata_infrastructures_input
    import capo_odb.types.list_cloud_exadata_infrastructures_output
    import capo_odb.types.list_cloud_vm_clusters_input
    import capo_odb.types.list_cloud_vm_clusters_output
    import capo_odb.types.list_db_nodes_input
    import capo_odb.types.list_db_nodes_output
    import capo_odb.types.list_db_servers_input
    import capo_odb.types.list_db_servers_output
    import capo_odb.types.list_db_system_shapes_input
    import capo_odb.types.list_db_system_shapes_output
    import capo_odb.types.list_exadb_vm_clusters_input
    import capo_odb.types.list_exadb_vm_clusters_output
    import capo_odb.types.list_exascale_db_storage_vaults_input
    import capo_odb.types.list_exascale_db_storage_vaults_output
    import capo_odb.types.list_flex_components_input
    import capo_odb.types.list_flex_components_output
    import capo_odb.types.list_gi_minor_versions_input
    import capo_odb.types.list_gi_minor_versions_output
    import capo_odb.types.list_gi_versions_input
    import capo_odb.types.list_gi_versions_output
    import capo_odb.types.list_odb_networks_input
    import capo_odb.types.list_odb_networks_output
    import capo_odb.types.list_odb_peering_connections_input
    import capo_odb.types.list_odb_peering_connections_output
    import capo_odb.types.list_system_versions_input
    import capo_odb.types.list_system_versions_output
    import capo_odb.types.list_tags_for_resource_request
    import capo_odb.types.list_tags_for_resource_response
    import capo_odb.types.long_term_backup_schedule
    import capo_odb.types.maintenance_window
    import capo_odb.types.odb_network_summary
    import capo_odb.types.odb_peering_connection_summary
    import capo_odb.types.open_mode
    import capo_odb.types.peer_network_route_table_id_list
    import capo_odb.types.peered_cidr_list
    import capo_odb.types.permission_level
    import capo_odb.types.policy_document
    import capo_odb.types.reboot_autonomous_database_input
    import capo_odb.types.reboot_autonomous_database_output
    import capo_odb.types.reboot_db_node_input
    import capo_odb.types.reboot_db_node_output
    import capo_odb.types.refreshable_mode
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_arn
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id
    import capo_odb.types.resource_id_list
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_pool_summary
    import capo_odb.types.restore_autonomous_database_input
    import capo_odb.types.restore_autonomous_database_output
    import capo_odb.types.role_arn
    import capo_odb.types.scheduled_operation_details_list
    import capo_odb.types.sensitive_string
    import capo_odb.types.shape_attribute
    import capo_odb.types.shrink_autonomous_database_input
    import capo_odb.types.shrink_autonomous_database_output
    import capo_odb.types.source_configuration
    import capo_odb.types.source_type
    import capo_odb.types.standby_allowlisted_ips_source
    import capo_odb.types.start_autonomous_database_input
    import capo_odb.types.start_autonomous_database_output
    import capo_odb.types.start_db_node_input
    import capo_odb.types.start_db_node_output
    import capo_odb.types.stop_autonomous_database_input
    import capo_odb.types.stop_autonomous_database_output
    import capo_odb.types.stop_db_node_input
    import capo_odb.types.stop_db_node_output
    import capo_odb.types.string_list
    import capo_odb.types.supported_aws_integration
    import capo_odb.types.switchover_autonomous_database_input
    import capo_odb.types.switchover_autonomous_database_output
    import capo_odb.types.system_version_summary
    import capo_odb.types.tag_keys
    import capo_odb.types.tag_resource_request
    import capo_odb.types.tag_resource_response
    import capo_odb.types.transportable_tablespace
    import capo_odb.types.untag_resource_request
    import capo_odb.types.untag_resource_response
    import capo_odb.types.update_action
    import capo_odb.types.update_autonomous_database_backup_input
    import capo_odb.types.update_autonomous_database_backup_output
    import capo_odb.types.update_autonomous_database_input
    import capo_odb.types.update_autonomous_database_output
    import capo_odb.types.update_cloud_exadata_infrastructure_input
    import capo_odb.types.update_cloud_exadata_infrastructure_output
    import capo_odb.types.update_exadb_vm_cluster_input
    import capo_odb.types.update_exadb_vm_cluster_output
    import capo_odb.types.update_exascale_db_storage_vault_input
    import capo_odb.types.update_exascale_db_storage_vault_output
    import capo_odb.types.update_odb_network_input
    import capo_odb.types.update_odb_network_output
    import capo_odb.types.update_odb_peering_connection_input
    import capo_odb.types.update_odb_peering_connection_output
    import capo_odb.types.wallet_password_source
    import capo_odb.types.wallet_password_source_configuration_input
    import capo_odb.types.wallet_type


class AsyncodbClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncodbClient:
    """A client for the ``odb`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncodbClientConfig(
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
        self.autonomous_database_backup_resource = (
            AsyncAutonomousDatabaseBackupResource(self)
        )
        self.autonomous_database_resource = AsyncAutonomousDatabaseResource(self)
        self.cloud_autonomous_vm_cluster_resource = (
            AsyncCloudAutonomousVmClusterResource(self)
        )
        self.cloud_exadata_infrastructure_resource = (
            AsyncCloudExadataInfrastructureResource(self)
        )
        self.cloud_vm_cluster_resource = AsyncCloudVmClusterResource(self)
        self.db_node_resource = AsyncDbNodeResource(self)
        self.exadb_vm_cluster_resource = AsyncExadbVmClusterResource(self)
        self.exascale_db_storage_vault_resource = AsyncExascaleDbStorageVaultResource(
            self
        )
        self.odb_network_resource = AsyncOdbNetworkResource(self)
        self.odb_peering_connection_resource = AsyncOdbPeeringConnectionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncodbClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncodbClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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

    async def accept_marketplace_registration(
        self,
        marketplace_registration_token: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.accept_marketplace_registration_output.AcceptMarketplaceRegistrationOutput":
        """<p>Registers the Amazon Web Services Marketplace token for your Amazon Web Services account to activate your Oracle Database@Amazon Web Services subscription.</p>

        Args:
            marketplace_registration_token: <p>The registration token that's generated by Amazon Web Services Marketplace and sent to Oracle Database@Amazon Web Services.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.accept_marketplace_registration_input.AcceptMarketplaceRegistrationInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.accept_marketplace_registration_output.AcceptMarketplaceRegistrationOutput"
        ]:
            import capo_odb._operations.odb.accept_marketplace_registration

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.accept_marketplace_registration.async_accept_marketplace_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.accept_marketplace_registration_input.AcceptMarketplaceRegistrationInput = {
            "marketplace_registration_token": marketplace_registration_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_iam_role_to_resource(
        self,
        iam_role_arn: "capo_odb.types.role_arn.RoleArn",
        aws_integration: "capo_odb.types.supported_aws_integration.SupportedAwsIntegration",
        resource_arn: "capo_odb.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.associate_iam_role_to_resource_output.AssociateIamRoleToResourceOutput":
        """<p>Associates an Amazon Web Services Identity and Access Management (IAM) service role with a specified resource to enable Amazon Web Services service integration.</p>

        Args:
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role to associate with the resource.</p>
            aws_integration: <p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role association.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the target resource to associate with the Amazon Web Services Identity and Access Management (IAM) service role.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.associate_iam_role_to_resource_input.AssociateIamRoleToResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.associate_iam_role_to_resource_output.AssociateIamRoleToResourceOutput"
        ]:
            import capo_odb._operations.odb.associate_iam_role_to_resource

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.associate_iam_role_to_resource.async_associate_iam_role_to_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.associate_iam_role_to_resource_input.AssociateIamRoleToResourceInput = {
            "iam_role_arn": iam_role_arn,
            "aws_integration": aws_integration,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_iam_role_from_resource(
        self,
        iam_role_arn: "capo_odb.types.role_arn.RoleArn",
        aws_integration: "capo_odb.types.supported_aws_integration.SupportedAwsIntegration",
        resource_arn: "capo_odb.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.disassociate_iam_role_from_resource_output.DisassociateIamRoleFromResourceOutput":
        """<p>Disassociates an Amazon Web Services Identity and Access Management (IAM) service role from a specified resource to disable Amazon Web Services service integration.</p>

        Args:
            iam_role_arn: <p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role to disassociate from the resource.</p>
            aws_integration: <p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role disassociation.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the target resource to disassociate from the Amazon Web Services Identity and Access Management (IAM) service role.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.disassociate_iam_role_from_resource_input.DisassociateIamRoleFromResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.disassociate_iam_role_from_resource_output.DisassociateIamRoleFromResourceOutput"
        ]:
            import capo_odb._operations.odb.disassociate_iam_role_from_resource

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.disassociate_iam_role_from_resource.async_disassociate_iam_role_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.disassociate_iam_role_from_resource_input.DisassociateIamRoleFromResourceInput = {
            "iam_role_arn": iam_role_arn,
            "aws_integration": aws_integration,
            "resource_arn": resource_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_oci_onboarding_status(
        self, *, config_overrides: Optional[AsyncodbClientConfig] = None
    ) -> "capo_odb.types.get_oci_onboarding_status_output.GetOciOnboardingStatusOutput":
        """<p>Returns the tenancy activation link and onboarding status for your Amazon Web Services account.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_oci_onboarding_status_input.GetOciOnboardingStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_oci_onboarding_status_output.GetOciOnboardingStatusOutput"
        ]:
            import capo_odb._operations.odb.get_oci_onboarding_status

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_oci_onboarding_status.async_get_oci_onboarding_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_oci_onboarding_status_input.GetOciOnboardingStatusInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def initialize_service(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        oci_identity_domain: Optional[bool] = None,
        autonomous_database_oci_aws_secrets_manager_integration: Optional[
            "capo_odb.types.access.Access"
        ] = None,
    ) -> "capo_odb.types.initialize_service_output.InitializeServiceOutput":
        """<p>Initializes the ODB service for the first time in an account.</p>

        Args:
            oci_identity_domain: <p>The Oracle Cloud Infrastructure (OCI) identity domain configuration for service initialization.</p>
            autonomous_database_oci_aws_secrets_manager_integration: <p>Specifies whether to enable or disable the OCI service-account role for Amazon Web Services Secrets Manager integration with Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.initialize_service_input.InitializeServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.initialize_service_output.InitializeServiceOutput"
        ]:
            import capo_odb._operations.odb.initialize_service

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.initialize_service.async_initialize_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.initialize_service_input.InitializeServiceInput = {}
        if oci_identity_domain is not None:
            input_["oci_identity_domain"] = oci_identity_domain
        if autonomous_database_oci_aws_secrets_manager_integration is not None:
            input_["autonomous_database_oci_aws_secrets_manager_integration"] = (
                autonomous_database_oci_aws_secrets_manager_integration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_autonomous_database_character_sets(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        character_set_type: Optional[
            "capo_odb.types.character_set_type.characterSetType"
        ] = None,
    ) -> "capo_odb.types.list_autonomous_database_character_sets_output.ListAutonomousDatabaseCharacterSetsOutput":
        """<p>Lists the available character sets for Autonomous Databases.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            character_set_type: <p>The type of character set to return results for, either the database character set or the national character set.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_character_sets_input.ListAutonomousDatabaseCharacterSetsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_character_sets_output.ListAutonomousDatabaseCharacterSetsOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_character_sets

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_character_sets.async_list_autonomous_database_character_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_database_character_sets_input.ListAutonomousDatabaseCharacterSetsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if character_set_type is not None:
            input_["character_set_type"] = character_set_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_autonomous_database_character_sets(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        character_set_type: Optional[
            "capo_odb.types.character_set_type.characterSetType"
        ] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_database_character_set_summary.AutonomousDatabaseCharacterSetSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_database_character_sets(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                character_set_type=character_set_type,
            )
            _page = _resolve_path(_response, ("autonomous_database_character_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_autonomous_database_versions(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
    ) -> "capo_odb.types.list_autonomous_database_versions_output.ListAutonomousDatabaseVersionsOutput":
        """<p>Lists the available Oracle Database software versions for Autonomous Databases.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            db_workload: <p>The intended use of the Autonomous Database to return versions for, such as transaction processing, data warehouse, JSON database, or APEX.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_versions_input.ListAutonomousDatabaseVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_versions_output.ListAutonomousDatabaseVersionsOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_versions

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_versions.async_list_autonomous_database_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_database_versions_input.ListAutonomousDatabaseVersionsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if db_workload is not None:
            input_["db_workload"] = db_workload

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_autonomous_database_versions(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_database_version_summary.AutonomousDatabaseVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_database_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                db_workload=db_workload,
            )
            _page = _resolve_path(_response, ("autonomous_database_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_db_system_shapes(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        shape_family: Optional[str] = None,
    ) -> "capo_odb.types.list_db_system_shapes_output.ListDbSystemShapesOutput":
        """<p>Returns information about the shapes that are available for an Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            availability_zone: <p>The logical name of the AZ, for example, us-east-1a. This name varies depending on the account.</p>
            availability_zone_id: <p>The physical ID of the AZ, for example, use1-az4. This ID persists across accounts.</p>
            shape_family: <p>The shape family to filter results by.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_db_system_shapes_input.ListDbSystemShapesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_db_system_shapes_output.ListDbSystemShapesOutput"
        ]:
            import capo_odb._operations.odb.list_db_system_shapes

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_db_system_shapes.async_list_db_system_shapes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_db_system_shapes_input.ListDbSystemShapesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if shape_family is not None:
            input_["shape_family"] = shape_family

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_db_system_shapes(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        shape_family: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.db_system_shape_summary.DbSystemShapeSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_system_shapes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                shape_family=shape_family,
            )
            _page = _resolve_path(_response, ("db_system_shapes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_flex_components(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape: Optional[str] = None,
    ) -> "capo_odb.types.list_flex_components_output.ListFlexComponentsOutput":
        """<p>Returns information about the flex components that are available for an Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            shape: <p>The shape to return flex components for. For a list of valid shapes, use the <code>ListDbSystemShapes</code> operation.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_flex_components_input.ListFlexComponentsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_flex_components_output.ListFlexComponentsOutput"
        ]:
            import capo_odb._operations.odb.list_flex_components

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_flex_components.async_list_flex_components(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_flex_components_input.ListFlexComponentsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if shape is not None:
            input_["shape"] = shape

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_flex_components(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.flex_component_summary.FlexComponentSummary]":
        _token = next_token
        while True:
            _response = await self.list_flex_components(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                shape=shape,
            )
            _page = _resolve_path(_response, ("flex_components",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_gi_minor_versions(
        self,
        gi_version: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape_family: Optional[str] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
    ) -> "capo_odb.types.list_gi_minor_versions_output.ListGiMinorVersionsOutput":
        """<p>Returns a list of the Oracle Grid Infrastructure (GI) minor versions for the specified major version.</p>

        Args:
            gi_version: <p>The Oracle Grid Infrastructure (GI) major version.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            shape_family: <p>The shape family for the GI minor version.</p>
            availability_zone: <p>The Availability Zone to filter GI minor versions.</p>
            availability_zone_id: <p>The Availability Zone ID to filter GI minor versions.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_gi_minor_versions_input.ListGiMinorVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_gi_minor_versions_output.ListGiMinorVersionsOutput"
        ]:
            import capo_odb._operations.odb.list_gi_minor_versions

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_gi_minor_versions.async_list_gi_minor_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_gi_minor_versions_input.ListGiMinorVersionsInput = {
            "gi_version": gi_version
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if shape_family is not None:
            input_["shape_family"] = shape_family
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_gi_minor_versions(
        self,
        gi_version: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape_family: Optional[str] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.gi_minor_version_summary.GiMinorVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_gi_minor_versions(
                gi_version,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                shape_family=shape_family,
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
            )
            _page = _resolve_path(_response, ("gi_minor_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_gi_versions(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape: Optional[str] = None,
    ) -> "capo_odb.types.list_gi_versions_output.ListGiVersionsOutput":
        """<p>Returns information about Oracle Grid Infrastructure (GI) software versions that are available for a VM cluster for the specified shape.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            shape: <p>The shape to return GI versions for. For a list of valid shapes, use the <code>ListDbSystemShapes</code> operation..</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_gi_versions_input.ListGiVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_gi_versions_output.ListGiVersionsOutput"
        ]:
            import capo_odb._operations.odb.list_gi_versions

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_gi_versions.async_list_gi_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_gi_versions_input.ListGiVersionsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if shape is not None:
            input_["shape"] = shape

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_gi_versions(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        shape: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.gi_version_summary.GiVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_gi_versions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                shape=shape,
            )
            _page = _resolve_path(_response, ("gi_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_system_versions(
        self,
        gi_version: str,
        shape: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_system_versions_output.ListSystemVersionsOutput":
        """<p>Returns information about the system versions that are available for a VM cluster for the specified <code>giVersion</code> and <code>shape</code>.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            gi_version: <p>The software version of the Exadata Grid Infrastructure (GI).</p>
            shape: <p>The Exadata hardware system model.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_system_versions_input.ListSystemVersionsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_system_versions_output.ListSystemVersionsOutput"
        ]:
            import capo_odb._operations.odb.list_system_versions

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_system_versions.async_list_system_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_system_versions_input.ListSystemVersionsInput = {
            "gi_version": gi_version,
            "shape": shape,
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

    async def iter_list_system_versions(
        self,
        gi_version: str,
        shape: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.system_version_summary.SystemVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_system_versions(
                gi_version,
                shape,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("system_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_odb.types.resource_arn.ResourceArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns information about the tags applied to this resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>

        Raises:
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_odb._operations.odb.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_odb.types.resource_arn.ResourceArn",
        tags: "capo_odb.types.request_tag_map.RequestTagMap",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.tag_resource_response.TagResourceResponse":
        """<p>Applies tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to apply tags to.</p>
            tags: <p>The list of tags to apply to the resource.</p>

        Raises:
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_odb._operations.odb.tag_resource

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_odb.types.resource_arn.ResourceArn",
        tag_keys: "capo_odb.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>
            tag_keys: <p>The names (keys) of the tags to remove from the resource.</p>

        Raises:
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_odb._operations.odb.untag_resource

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_autonomous_database_backup(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        retention_period_in_days: Optional[int] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_autonomous_database_backup_output.CreateAutonomousDatabaseBackupOutput":
        """<p>Creates a new backup of the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to back up.</p>
            display_name: <p>The user-friendly name for the Autonomous Database backup.</p>
            retention_period_in_days: <p>The retention period, in days, for the Autonomous Database backup.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>
            tags: <p>The list of resource tags to apply to the Autonomous Database backup. Each tag is a key-value pair with no predefined name, type, or namespace.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_autonomous_database_backup_input.CreateAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_autonomous_database_backup_output.CreateAutonomousDatabaseBackupOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database_backup

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_autonomous_database_backup.async_create_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_autonomous_database_backup_input.CreateAutonomousDatabaseBackupInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_autonomous_database_backup(
        self,
        autonomous_database_backup_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_backup_output.GetAutonomousDatabaseBackupOutput":
        """<p>Gets information about a specific Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_autonomous_database_backup_input.GetAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_autonomous_database_backup_output.GetAutonomousDatabaseBackupOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database_backup

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_autonomous_database_backup.async_get_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_autonomous_database_backup_input.GetAutonomousDatabaseBackupInput = {
            "autonomous_database_backup_id": autonomous_database_backup_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_autonomous_database_backup(
        self,
        autonomous_database_backup_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        retention_period_in_days: Optional[int] = None,
    ) -> "capo_odb.types.update_autonomous_database_backup_output.UpdateAutonomousDatabaseBackupOutput":
        """<p>Updates the properties of an Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to update.</p>
            retention_period_in_days: <p>The retention period, in days, for the Autonomous Database backup.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_autonomous_database_backup_input.UpdateAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_autonomous_database_backup_output.UpdateAutonomousDatabaseBackupOutput"
        ]:
            import capo_odb._operations.odb.update_autonomous_database_backup

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_autonomous_database_backup.async_update_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_autonomous_database_backup_input.UpdateAutonomousDatabaseBackupInput = {
            "autonomous_database_backup_id": autonomous_database_backup_id
        }
        if retention_period_in_days is not None:
            input_["retention_period_in_days"] = retention_period_in_days

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_autonomous_database_backup(
        self,
        autonomous_database_backup_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput":
        """<p>Deletes the specified Autonomous Database backup.</p>

        Args:
            autonomous_database_backup_id: <p>The unique identifier of the Autonomous Database backup to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput"
        ]:
            import capo_odb._operations.odb.delete_autonomous_database_backup

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_autonomous_database_backup.async_delete_autonomous_database_backup(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput = {
            "autonomous_database_backup_id": autonomous_database_backup_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_autonomous_database_backups(
        self,
        autonomous_database_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "capo_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
        ] = None,
        type: Optional[
            "capo_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
        ] = None,
    ) -> "capo_odb.types.list_autonomous_database_backups_output.ListAutonomousDatabaseBackupsOutput":
        """<p>Lists the backups of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the Autonomous Database whose backups you want to list.</p>
            status: <p>The status of the Autonomous Database backups to return results for.</p>
            type: <p>The type of the Autonomous Database backups to return results for.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_backups_input.ListAutonomousDatabaseBackupsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_backups_output.ListAutonomousDatabaseBackupsOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_backups

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_backups.async_list_autonomous_database_backups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_database_backups_input.ListAutonomousDatabaseBackupsInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_autonomous_database_backups(
        self,
        autonomous_database_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        status: Optional[
            "capo_odb.types.autonomous_database_backup_status.AutonomousDatabaseBackupStatus"
        ] = None,
        type: Optional[
            "capo_odb.types.autonomous_database_backup_type.AutonomousDatabaseBackupType"
        ] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_database_backup_summary.AutonomousDatabaseBackupSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_database_backups(
                autonomous_database_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
                type=type,
            )
            _page = _resolve_path(_response, ("autonomous_database_backups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_autonomous_database(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        db_name: Optional[str] = None,
        admin_password: Optional[
            "capo_odb.types.sensitive_string.SensitiveString"
        ] = None,
        compute_count: Optional[float] = None,
        data_storage_size_in_t_bs: Optional[int] = None,
        data_storage_size_in_g_bs: Optional[int] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
        is_auto_scaling_enabled: Optional[bool] = None,
        is_auto_scaling_for_storage_enabled: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        character_set: Optional[str] = None,
        ncharacter_set: Optional[str] = None,
        db_version: Optional[str] = None,
        database_edition: Optional[
            "capo_odb.types.database_edition.DatabaseEdition"
        ] = None,
        standby_allowlisted_ips_source: Optional[
            "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
        ] = None,
        autonomous_maintenance_schedule_type: Optional[
            "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
        ] = None,
        backup_retention_period_in_days: Optional[int] = None,
        byol_compute_count_limit: Optional[float] = None,
        cpu_core_count: Optional[int] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        private_endpoint_ip: Optional[str] = None,
        private_endpoint_label: Optional[str] = None,
        resource_pool_leader_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_summary: Optional[
            "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
        ] = None,
        scheduled_operations: Optional[
            "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
        ] = None,
        standby_allowlisted_ips: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        allowlisted_ips: Optional["capo_odb.types.string_list.StringList"] = None,
        transportable_tablespace: Optional[
            "capo_odb.types.transportable_tablespace.TransportableTablespace"
        ] = None,
        is_backup_retention_locked: Optional[bool] = None,
        is_local_data_guard_enabled: Optional[bool] = None,
        is_mtls_connection_required: Optional[bool] = None,
        db_tools_details: Optional[
            "capo_odb.types.database_tool_list.DatabaseToolList"
        ] = None,
        source: Optional["capo_odb.types.source_type.SourceType"] = None,
        source_configuration: Optional[
            "capo_odb.types.source_configuration.SourceConfiguration"
        ] = None,
        encryption_key_provider: Optional[
            "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
        ] = None,
        encryption_key_configuration: Optional[
            "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
        ] = None,
        admin_password_source: Optional[
            "capo_odb.types.admin_password_source.AdminPasswordSource"
        ] = None,
        admin_password_source_configuration: Optional[
            "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_autonomous_database_output.CreateAutonomousDatabaseOutput":
        """<p>Creates a new Autonomous Database.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to be used for the Autonomous Database.</p>
            display_name: <p>The user-friendly name for the Autonomous Database. The name does not have to be unique.</p>
            db_name: <p>The name of the Autonomous Database. The name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters. Special characters are not permitted. The name must be unique in the Amazon Web Services account.</p>
            admin_password: <p>The password for the <code>ADMIN</code> user of the Autonomous Database.</p>
            compute_count: <p>The compute capacity, in number of Elastic CPUs (ECPUs) or Oracle CPUs (OCPUs), to assign to the Autonomous Database.</p>
            data_storage_size_in_t_bs: <p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>
            data_storage_size_in_g_bs: <p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>
            db_workload: <p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>
            is_auto_scaling_enabled: <p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>
            is_auto_scaling_for_storage_enabled: <p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous Database.</p>
            character_set: <p>The character set to use for the Autonomous Database.</p>
            ncharacter_set: <p>The national character set to use for the Autonomous Database.</p>
            db_version: <p>The Oracle Database software version to use for the Autonomous Database.</p>
            database_edition: <p>The Oracle Database edition to apply to the Autonomous Database.</p>
            standby_allowlisted_ips_source: <p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>
            autonomous_maintenance_schedule_type: <p>The maintenance schedule type for the Autonomous Database.</p>
            backup_retention_period_in_days: <p>The retention period, in days, for automatic backups of the Autonomous Database.</p>
            byol_compute_count_limit: <p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>
            cpu_core_count: <p>The number of CPU cores to allocate to the Autonomous Database.</p>
            customer_contacts_to_send_to_oci: <p>The list of customer contacts to receive operational notifications from Oracle Cloud Infrastructure (OCI) for the Autonomous Database.</p>
            private_endpoint_ip: <p>The private endpoint IP address for the Autonomous Database.</p>
            private_endpoint_label: <p>The private endpoint label for the Autonomous Database.</p>
            resource_pool_leader_id: <p>The unique identifier of the resource pool leader Autonomous Database.</p>
            resource_pool_summary: <p>The configuration of the resource pool for the Autonomous Database.</p>
            scheduled_operations: <p>The list of scheduled start and stop times for the Autonomous Database.</p>
            standby_allowlisted_ips: <p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>
            allowlisted_ips: <p>The list of IP addresses that are allowed to access the Autonomous Database.</p>
            transportable_tablespace: <p>The transportable tablespace configuration to use when creating the Autonomous Database.</p>
            is_backup_retention_locked: <p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>
            is_local_data_guard_enabled: <p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>
            is_mtls_connection_required: <p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>
            db_tools_details: <p>The list of database management tools to enable for the Autonomous Database.</p>
            source: <p>The source from which to create the Autonomous Database, such as a clone, backup, or cross-Region copy.</p>
            source_configuration: <p>The configuration details for the source used to create the Autonomous Database.</p>
            encryption_key_provider: <p>The provider of the encryption key to use for the Autonomous Database.</p>
            encryption_key_configuration: <p>The configuration of the encryption key to use for the Autonomous Database.</p>
            admin_password_source: <p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            admin_password_source_configuration: <p>The configuration of the admin password source for the Autonomous Database.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>
            tags: <p>The list of resource tags to apply to the Autonomous Database. Each tag is a key-value pair with no predefined name, type, or namespace.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_autonomous_database_output.CreateAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_autonomous_database.async_create_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_autonomous_database_input.CreateAutonomousDatabaseInput = {}
        if odb_network_id is not None:
            input_["odb_network_id"] = odb_network_id
        if display_name is not None:
            input_["display_name"] = display_name
        if db_name is not None:
            input_["db_name"] = db_name
        if admin_password is not None:
            input_["admin_password"] = admin_password
        if compute_count is not None:
            input_["compute_count"] = compute_count
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if data_storage_size_in_g_bs is not None:
            input_["data_storage_size_in_g_bs"] = data_storage_size_in_g_bs
        if db_workload is not None:
            input_["db_workload"] = db_workload
        if is_auto_scaling_enabled is not None:
            input_["is_auto_scaling_enabled"] = is_auto_scaling_enabled
        if is_auto_scaling_for_storage_enabled is not None:
            input_["is_auto_scaling_for_storage_enabled"] = (
                is_auto_scaling_for_storage_enabled
            )
        if license_model is not None:
            input_["license_model"] = license_model
        if character_set is not None:
            input_["character_set"] = character_set
        if ncharacter_set is not None:
            input_["ncharacter_set"] = ncharacter_set
        if db_version is not None:
            input_["db_version"] = db_version
        if database_edition is not None:
            input_["database_edition"] = database_edition
        if standby_allowlisted_ips_source is not None:
            input_["standby_allowlisted_ips_source"] = standby_allowlisted_ips_source
        if autonomous_maintenance_schedule_type is not None:
            input_["autonomous_maintenance_schedule_type"] = (
                autonomous_maintenance_schedule_type
            )
        if backup_retention_period_in_days is not None:
            input_["backup_retention_period_in_days"] = backup_retention_period_in_days
        if byol_compute_count_limit is not None:
            input_["byol_compute_count_limit"] = byol_compute_count_limit
        if cpu_core_count is not None:
            input_["cpu_core_count"] = cpu_core_count
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if private_endpoint_ip is not None:
            input_["private_endpoint_ip"] = private_endpoint_ip
        if private_endpoint_label is not None:
            input_["private_endpoint_label"] = private_endpoint_label
        if resource_pool_leader_id is not None:
            input_["resource_pool_leader_id"] = resource_pool_leader_id
        if resource_pool_summary is not None:
            input_["resource_pool_summary"] = resource_pool_summary
        if scheduled_operations is not None:
            input_["scheduled_operations"] = scheduled_operations
        if standby_allowlisted_ips is not None:
            input_["standby_allowlisted_ips"] = standby_allowlisted_ips
        if allowlisted_ips is not None:
            input_["allowlisted_ips"] = allowlisted_ips
        if transportable_tablespace is not None:
            input_["transportable_tablespace"] = transportable_tablespace
        if is_backup_retention_locked is not None:
            input_["is_backup_retention_locked"] = is_backup_retention_locked
        if is_local_data_guard_enabled is not None:
            input_["is_local_data_guard_enabled"] = is_local_data_guard_enabled
        if is_mtls_connection_required is not None:
            input_["is_mtls_connection_required"] = is_mtls_connection_required
        if db_tools_details is not None:
            input_["db_tools_details"] = db_tools_details
        if source is not None:
            input_["source"] = source
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if encryption_key_provider is not None:
            input_["encryption_key_provider"] = encryption_key_provider
        if encryption_key_configuration is not None:
            input_["encryption_key_configuration"] = encryption_key_configuration
        if admin_password_source is not None:
            input_["admin_password_source"] = admin_password_source
        if admin_password_source_configuration is not None:
            input_["admin_password_source_configuration"] = (
                admin_password_source_configuration
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput":
        """<p>Gets information about a specific Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_autonomous_database_input.GetAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_autonomous_database_output.GetAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_autonomous_database.async_get_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_autonomous_database_input.GetAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        admin_password: Optional[
            "capo_odb.types.sensitive_string.SensitiveString"
        ] = None,
        compute_count: Optional[float] = None,
        cpu_core_count: Optional[int] = None,
        data_storage_size_in_t_bs: Optional[int] = None,
        data_storage_size_in_g_bs: Optional[int] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        db_name: Optional[str] = None,
        db_version: Optional[str] = None,
        db_workload: Optional["capo_odb.types.db_workload.DbWorkload"] = None,
        db_tools_details: Optional[
            "capo_odb.types.database_tool_list.DatabaseToolList"
        ] = None,
        database_edition: Optional[
            "capo_odb.types.database_edition.DatabaseEdition"
        ] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        is_auto_scaling_enabled: Optional[bool] = None,
        is_auto_scaling_for_storage_enabled: Optional[bool] = None,
        is_backup_retention_locked: Optional[bool] = None,
        is_local_data_guard_enabled: Optional[bool] = None,
        is_mtls_connection_required: Optional[bool] = None,
        is_refreshable_clone: Optional[bool] = None,
        is_disconnect_peer: Optional[bool] = None,
        backup_retention_period_in_days: Optional[int] = None,
        byol_compute_count_limit: Optional[float] = None,
        local_adg_auto_failover_max_data_loss_limit: Optional[int] = None,
        autonomous_maintenance_schedule_type: Optional[
            "capo_odb.types.autonomous_maintenance_schedule_type.AutonomousMaintenanceScheduleType"
        ] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        scheduled_operations: Optional[
            "capo_odb.types.scheduled_operation_details_list.ScheduledOperationDetailsList"
        ] = None,
        long_term_backup_schedule: Optional[
            "capo_odb.types.long_term_backup_schedule.LongTermBackupSchedule"
        ] = None,
        open_mode: Optional["capo_odb.types.open_mode.OpenMode"] = None,
        permission_level: Optional[
            "capo_odb.types.permission_level.PermissionLevel"
        ] = None,
        refreshable_mode: Optional[
            "capo_odb.types.refreshable_mode.RefreshableMode"
        ] = None,
        private_endpoint_ip: Optional[str] = None,
        private_endpoint_label: Optional[str] = None,
        peer_db_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_leader_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        resource_pool_summary: Optional[
            "capo_odb.types.resource_pool_summary.ResourcePoolSummary"
        ] = None,
        standby_allowlisted_ips_source: Optional[
            "capo_odb.types.standby_allowlisted_ips_source.StandbyAllowlistedIpsSource"
        ] = None,
        standby_allowlisted_ips: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        allowlisted_ips: Optional["capo_odb.types.string_list.StringList"] = None,
        auto_refresh_frequency_in_seconds: Optional[int] = None,
        auto_refresh_point_lag_in_seconds: Optional[int] = None,
        time_of_auto_refresh_start: Optional[datetime.datetime] = None,
        encryption_key_provider: Optional[
            "capo_odb.types.encryption_key_provider_input.EncryptionKeyProviderInput"
        ] = None,
        encryption_key_configuration: Optional[
            "capo_odb.types.encryption_key_configuration_input.EncryptionKeyConfigurationInput"
        ] = None,
        admin_password_source: Optional[
            "capo_odb.types.admin_password_source.AdminPasswordSource"
        ] = None,
        admin_password_source_configuration: Optional[
            "capo_odb.types.admin_password_source_configuration_input.AdminPasswordSourceConfigurationInput"
        ] = None,
    ) -> "capo_odb.types.update_autonomous_database_output.UpdateAutonomousDatabaseOutput":
        """<p>Updates the properties of an Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to update.</p>
            admin_password: <p>The new password for the <code>ADMIN</code> user of the Autonomous Database.</p>
            compute_count: <p>The compute capacity, in number of ECPUs or OCPUs, to assign to the Autonomous Database.</p>
            cpu_core_count: <p>The number of CPU cores to allocate to the Autonomous Database.</p>
            data_storage_size_in_t_bs: <p>The size, in terabytes (TB), of the data volume to allocate for the Autonomous Database.</p>
            data_storage_size_in_g_bs: <p>The size, in gigabytes (GB), of the data volume to allocate for the Autonomous Database.</p>
            display_name: <p>The new user-friendly name for the Autonomous Database.</p>
            db_name: <p>The new name of the Autonomous Database.</p>
            db_version: <p>The Oracle Database software version to use for the Autonomous Database.</p>
            db_workload: <p>The intended use of the Autonomous Database, such as transaction processing, data warehouse, JSON database, or APEX.</p>
            db_tools_details: <p>The list of database management tools to enable for the Autonomous Database.</p>
            database_edition: <p>The Oracle Database edition to apply to the Autonomous Database.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous Database.</p>
            is_auto_scaling_enabled: <p>Specifies whether to enable automatic scaling of the compute resources for the Autonomous Database.</p>
            is_auto_scaling_for_storage_enabled: <p>Specifies whether to enable automatic scaling of the storage for the Autonomous Database.</p>
            is_backup_retention_locked: <p>Specifies whether to lock the backup retention period of the Autonomous Database to prevent it from being shortened.</p>
            is_local_data_guard_enabled: <p>Specifies whether to enable local Oracle Data Guard for the Autonomous Database.</p>
            is_mtls_connection_required: <p>Specifies whether mutual TLS (mTLS) authentication is required to connect to the Autonomous Database.</p>
            is_refreshable_clone: <p>Specifies whether the Autonomous Database is a refreshable clone.</p>
            is_disconnect_peer: <p>Specifies whether to disconnect the Autonomous Database from its peer database.</p>
            backup_retention_period_in_days: <p>The retention period, in days, for automatic backups of the Autonomous Database.</p>
            byol_compute_count_limit: <p>The maximum number of compute resources that you can allocate to the Autonomous Database under the bring-your-own-license (BYOL) model.</p>
            local_adg_auto_failover_max_data_loss_limit: <p>The maximum data loss limit, in seconds, for automatic failover to the local Oracle Data Guard standby database.</p>
            autonomous_maintenance_schedule_type: <p>The maintenance schedule type for the Autonomous Database.</p>
            customer_contacts_to_send_to_oci: <p>The list of customer contacts to receive operational notifications from OCI for the Autonomous Database.</p>
            scheduled_operations: <p>The list of scheduled start and stop times for the Autonomous Database.</p>
            long_term_backup_schedule: <p>The long-term backup schedule for the Autonomous Database.</p>
            open_mode: <p>The mode in which to open the Autonomous Database, either read-only or read/write.</p>
            permission_level: <p>The permission level of the Autonomous Database.</p>
            refreshable_mode: <p>The refresh mode of the refreshable clone Autonomous Database.</p>
            private_endpoint_ip: <p>The private endpoint IP address for the Autonomous Database.</p>
            private_endpoint_label: <p>The private endpoint label for the Autonomous Database.</p>
            peer_db_id: <p>The unique identifier of the peer Autonomous Database.</p>
            resource_pool_leader_id: <p>The unique identifier of the resource pool leader Autonomous Database.</p>
            resource_pool_summary: <p>The configuration of the resource pool for the Autonomous Database.</p>
            standby_allowlisted_ips_source: <p>The source of the allowlisted IP addresses for the standby Autonomous Database.</p>
            standby_allowlisted_ips: <p>The list of IP addresses that are allowed to access the standby Autonomous Database.</p>
            allowlisted_ips: <p>The list of IP addresses that are allowed to access the Autonomous Database.</p>
            auto_refresh_frequency_in_seconds: <p>The frequency, in seconds, at which the refreshable clone Autonomous Database is automatically refreshed.</p>
            auto_refresh_point_lag_in_seconds: <p>The time lag, in seconds, between the refreshable clone and its source Autonomous Database.</p>
            time_of_auto_refresh_start: <p>The date and time at which the automatic refresh of the refreshable clone Autonomous Database starts.</p>
            encryption_key_provider: <p>The provider of the encryption key to use for the Autonomous Database.</p>
            encryption_key_configuration: <p>The configuration of the encryption key to use for the Autonomous Database.</p>
            admin_password_source: <p>The source of the admin password for the Autonomous Database. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the admin password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            admin_password_source_configuration: <p>The configuration of the admin password source for the Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_autonomous_database_output.UpdateAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.update_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_autonomous_database.async_update_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_autonomous_database_input.UpdateAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if admin_password is not None:
            input_["admin_password"] = admin_password
        if compute_count is not None:
            input_["compute_count"] = compute_count
        if cpu_core_count is not None:
            input_["cpu_core_count"] = cpu_core_count
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if data_storage_size_in_g_bs is not None:
            input_["data_storage_size_in_g_bs"] = data_storage_size_in_g_bs
        if display_name is not None:
            input_["display_name"] = display_name
        if db_name is not None:
            input_["db_name"] = db_name
        if db_version is not None:
            input_["db_version"] = db_version
        if db_workload is not None:
            input_["db_workload"] = db_workload
        if db_tools_details is not None:
            input_["db_tools_details"] = db_tools_details
        if database_edition is not None:
            input_["database_edition"] = database_edition
        if license_model is not None:
            input_["license_model"] = license_model
        if is_auto_scaling_enabled is not None:
            input_["is_auto_scaling_enabled"] = is_auto_scaling_enabled
        if is_auto_scaling_for_storage_enabled is not None:
            input_["is_auto_scaling_for_storage_enabled"] = (
                is_auto_scaling_for_storage_enabled
            )
        if is_backup_retention_locked is not None:
            input_["is_backup_retention_locked"] = is_backup_retention_locked
        if is_local_data_guard_enabled is not None:
            input_["is_local_data_guard_enabled"] = is_local_data_guard_enabled
        if is_mtls_connection_required is not None:
            input_["is_mtls_connection_required"] = is_mtls_connection_required
        if is_refreshable_clone is not None:
            input_["is_refreshable_clone"] = is_refreshable_clone
        if is_disconnect_peer is not None:
            input_["is_disconnect_peer"] = is_disconnect_peer
        if backup_retention_period_in_days is not None:
            input_["backup_retention_period_in_days"] = backup_retention_period_in_days
        if byol_compute_count_limit is not None:
            input_["byol_compute_count_limit"] = byol_compute_count_limit
        if local_adg_auto_failover_max_data_loss_limit is not None:
            input_["local_adg_auto_failover_max_data_loss_limit"] = (
                local_adg_auto_failover_max_data_loss_limit
            )
        if autonomous_maintenance_schedule_type is not None:
            input_["autonomous_maintenance_schedule_type"] = (
                autonomous_maintenance_schedule_type
            )
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if scheduled_operations is not None:
            input_["scheduled_operations"] = scheduled_operations
        if long_term_backup_schedule is not None:
            input_["long_term_backup_schedule"] = long_term_backup_schedule
        if open_mode is not None:
            input_["open_mode"] = open_mode
        if permission_level is not None:
            input_["permission_level"] = permission_level
        if refreshable_mode is not None:
            input_["refreshable_mode"] = refreshable_mode
        if private_endpoint_ip is not None:
            input_["private_endpoint_ip"] = private_endpoint_ip
        if private_endpoint_label is not None:
            input_["private_endpoint_label"] = private_endpoint_label
        if peer_db_id is not None:
            input_["peer_db_id"] = peer_db_id
        if resource_pool_leader_id is not None:
            input_["resource_pool_leader_id"] = resource_pool_leader_id
        if resource_pool_summary is not None:
            input_["resource_pool_summary"] = resource_pool_summary
        if standby_allowlisted_ips_source is not None:
            input_["standby_allowlisted_ips_source"] = standby_allowlisted_ips_source
        if standby_allowlisted_ips is not None:
            input_["standby_allowlisted_ips"] = standby_allowlisted_ips
        if allowlisted_ips is not None:
            input_["allowlisted_ips"] = allowlisted_ips
        if auto_refresh_frequency_in_seconds is not None:
            input_["auto_refresh_frequency_in_seconds"] = (
                auto_refresh_frequency_in_seconds
            )
        if auto_refresh_point_lag_in_seconds is not None:
            input_["auto_refresh_point_lag_in_seconds"] = (
                auto_refresh_point_lag_in_seconds
            )
        if time_of_auto_refresh_start is not None:
            input_["time_of_auto_refresh_start"] = time_of_auto_refresh_start
        if encryption_key_provider is not None:
            input_["encryption_key_provider"] = encryption_key_provider
        if encryption_key_configuration is not None:
            input_["encryption_key_configuration"] = encryption_key_configuration
        if admin_password_source is not None:
            input_["admin_password_source"] = admin_password_source
        if admin_password_source_configuration is not None:
            input_["admin_password_source_configuration"] = (
                admin_password_source_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_autonomous_database_output.DeleteAutonomousDatabaseOutput":
        """<p>Deletes the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_autonomous_database_input.DeleteAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_autonomous_database_output.DeleteAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.delete_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_autonomous_database.async_delete_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_autonomous_database_input.DeleteAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_autonomous_databases(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> (
        "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput"
    ):
        """<p>Returns information about the Autonomous Databases owned by your Amazon Web Services account in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_databases_input.ListAutonomousDatabasesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_databases_output.ListAutonomousDatabasesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_databases

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_databases.async_list_autonomous_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_databases_input.ListAutonomousDatabasesInput = {}
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

    async def iter_list_autonomous_databases(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_database_summary.AutonomousDatabaseSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_databases(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("autonomous_databases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_autonomous_database_wallet(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        wallet_type: Optional["capo_odb.types.wallet_type.WalletType"] = None,
        password: Optional["capo_odb.types.sensitive_string.SensitiveString"] = None,
        password_source: Optional[
            "capo_odb.types.wallet_password_source.WalletPasswordSource"
        ] = None,
        password_source_configuration: Optional[
            "capo_odb.types.wallet_password_source_configuration_input.WalletPasswordSourceConfigurationInput"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput":
        """<p>Creates a new wallet for the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to create a wallet for.</p>
            wallet_type: <p>The type of wallet to create, either a regional wallet or an instance wallet.</p>
            password: <p>The password to encrypt the keys inside the wallet.</p>
            password_source: <p>The source of the password for encrypting the wallet. When set to <code>CUSTOMER_MANAGED_AWS_SECRET</code>, the password is retrieved from an Amazon Web Services Secrets Manager secret.</p>
            password_source_configuration: <p>The configuration of the password source for the Autonomous Database wallet.</p>
            client_token: <p>A client-provided token to ensure the idempotency of the request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_autonomous_database_wallet_output.CreateAutonomousDatabaseWalletOutput"
        ]:
            import capo_odb._operations.odb.create_autonomous_database_wallet

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_autonomous_database_wallet.async_create_autonomous_database_wallet(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_autonomous_database_wallet_input.CreateAutonomousDatabaseWalletInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if wallet_type is not None:
            input_["wallet_type"] = wallet_type
        if password is not None:
            input_["password"] = password
        if password_source is not None:
            input_["password_source"] = password_source
        if password_source_configuration is not None:
            input_["password_source_configuration"] = password_source_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def failover_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        peer_db_arn: Optional["capo_odb.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_odb.types.failover_autonomous_database_output.FailoverAutonomousDatabaseOutput":
        """<p>Initiates a failover of the specified Autonomous Database to a standby peer database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to fail over.</p>
            peer_db_arn: <p>The Amazon Resource Name (ARN) of the peer Autonomous Database to fail over to.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.failover_autonomous_database_input.FailoverAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.failover_autonomous_database_output.FailoverAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.failover_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.failover_autonomous_database.async_failover_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.failover_autonomous_database_input.FailoverAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if peer_db_arn is not None:
            input_["peer_db_arn"] = peer_db_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_autonomous_database_wallet_details(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_autonomous_database_wallet_details_output.GetAutonomousDatabaseWalletDetailsOutput":
        """<p>Gets the wallet details for the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to retrieve wallet details for.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_autonomous_database_wallet_details_input.GetAutonomousDatabaseWalletDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_autonomous_database_wallet_details_output.GetAutonomousDatabaseWalletDetailsOutput"
        ]:
            import capo_odb._operations.odb.get_autonomous_database_wallet_details

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_autonomous_database_wallet_details.async_get_autonomous_database_wallet_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_autonomous_database_wallet_details_input.GetAutonomousDatabaseWalletDetailsInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_autonomous_database_clones(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput":
        """<p>Lists the clones of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the source Autonomous Database whose clones you want to list.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_clones_input.ListAutonomousDatabaseClonesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_clones_output.ListAutonomousDatabaseClonesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_clones

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_clones.async_list_autonomous_database_clones(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_database_clones_input.ListAutonomousDatabaseClonesInput = {
            "autonomous_database_id": autonomous_database_id
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

    async def iter_list_autonomous_database_clones(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_database_summary.AutonomousDatabaseSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_database_clones(
                autonomous_database_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("autonomous_database_clones",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_autonomous_database_peers(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_database_peers_output.ListAutonomousDatabasePeersOutput":
        """<p>Lists the peer databases of the specified Autonomous Database.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            autonomous_database_id: <p>The unique identifier of the Autonomous Database whose peer databases you want to list.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_database_peers_input.ListAutonomousDatabasePeersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_database_peers_output.ListAutonomousDatabasePeersOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_database_peers

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_database_peers.async_list_autonomous_database_peers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_database_peers_input.ListAutonomousDatabasePeersInput = {
            "autonomous_database_id": autonomous_database_id
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

    async def iter_list_autonomous_database_peers(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_database_peer_summary.AutonomousDatabasePeerSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_database_peers(
                autonomous_database_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("autonomous_database_peers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reboot_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        is_online_reboot: Optional[bool] = None,
    ) -> "capo_odb.types.reboot_autonomous_database_output.RebootAutonomousDatabaseOutput":
        """<p>Reboots the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to reboot.</p>
            is_online_reboot: <p>Specifies whether to perform an online reboot of the Autonomous Database without interrupting active connections.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.reboot_autonomous_database_input.RebootAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.reboot_autonomous_database_output.RebootAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.reboot_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.reboot_autonomous_database.async_reboot_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.reboot_autonomous_database_input.RebootAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if is_online_reboot is not None:
            input_["is_online_reboot"] = is_online_reboot

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def restore_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        timestamp: datetime.datetime,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.restore_autonomous_database_output.RestoreAutonomousDatabaseOutput":
        """<p>Restores the specified Autonomous Database to a point in time.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to restore.</p>
            timestamp: <p>The date and time to which to restore the Autonomous Database.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.restore_autonomous_database_input.RestoreAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.restore_autonomous_database_output.RestoreAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.restore_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.restore_autonomous_database.async_restore_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.restore_autonomous_database_input.RestoreAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id,
            "timestamp": timestamp,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def shrink_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.shrink_autonomous_database_output.ShrinkAutonomousDatabaseOutput":
        """<p>Shrinks the storage of the specified Autonomous Database to reclaim unused space.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to shrink.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.shrink_autonomous_database_input.ShrinkAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.shrink_autonomous_database_output.ShrinkAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.shrink_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.shrink_autonomous_database.async_shrink_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.shrink_autonomous_database_input.ShrinkAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> (
        "capo_odb.types.start_autonomous_database_output.StartAutonomousDatabaseOutput"
    ):
        """<p>Starts the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to start.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.start_autonomous_database_input.StartAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.start_autonomous_database_output.StartAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.start_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.start_autonomous_database.async_start_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.start_autonomous_database_input.StartAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.stop_autonomous_database_output.StopAutonomousDatabaseOutput":
        """<p>Stops the specified Autonomous Database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to stop.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.stop_autonomous_database_input.StopAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.stop_autonomous_database_output.StopAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.stop_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.stop_autonomous_database.async_stop_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.stop_autonomous_database_input.StopAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def switchover_autonomous_database(
        self,
        autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        peer_db_arn: Optional["capo_odb.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_odb.types.switchover_autonomous_database_output.SwitchoverAutonomousDatabaseOutput":
        """<p>Performs a switchover of the specified Autonomous Database to a standby peer database.</p>

        Args:
            autonomous_database_id: <p>The unique identifier of the Autonomous Database to switch over.</p>
            peer_db_arn: <p>The Amazon Resource Name (ARN) of the peer Autonomous Database to switch over to.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.switchover_autonomous_database_input.SwitchoverAutonomousDatabaseInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.switchover_autonomous_database_output.SwitchoverAutonomousDatabaseOutput"
        ]:
            import capo_odb._operations.odb.switchover_autonomous_database

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.switchover_autonomous_database.async_switchover_autonomous_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.switchover_autonomous_database_input.SwitchoverAutonomousDatabaseInput = {
            "autonomous_database_id": autonomous_database_id
        }
        if peer_db_arn is not None:
            input_["peer_db_arn"] = peer_db_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cloud_autonomous_vm_cluster(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        autonomous_data_storage_size_in_t_bs: float,
        cpu_core_count_per_node: int,
        memory_per_oracle_compute_unit_in_g_bs: int,
        total_container_databases: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
        description: Optional[str] = None,
        is_mtls_enabled_vm_cluster: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        maintenance_window: Optional[
            "capo_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
        scan_listener_port_non_tls: Optional[int] = None,
        scan_listener_port_tls: Optional[int] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
    ) -> "capo_odb.types.create_cloud_autonomous_vm_cluster_output.CreateCloudAutonomousVmClusterOutput":
        """<p>Creates a new Autonomous VM cluster in the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure where the VM cluster will be created.</p>
            odb_network_id: <p>The unique identifier of the ODB network to be used for the VM cluster.</p>
            display_name: <p>The display name for the Autonomous VM cluster. The name does not need to be unique.</p>
            client_token: <p>A client-provided token to ensure idempotency of the request.</p>
            autonomous_data_storage_size_in_t_bs: <p>The data disk group size to be allocated for Autonomous Databases, in terabytes (TB).</p>
            cpu_core_count_per_node: <p>The number of CPU cores to be enabled per VM cluster node.</p>
            db_servers: <p>The list of database servers to be used for the Autonomous VM cluster.</p>
            description: <p>A user-provided description of the Autonomous VM cluster.</p>
            is_mtls_enabled_vm_cluster: <p>Specifies whether to enable mutual TLS (mTLS) authentication for the Autonomous VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Autonomous VM cluster.</p>
            maintenance_window: <p>The scheduling details for the maintenance window. Patching and system updates take place during the maintenance window.</p>
            memory_per_oracle_compute_unit_in_g_bs: <p>The amount of memory to be allocated per OCPU, in GB.</p>
            scan_listener_port_non_tls: <p>The SCAN listener port for non-TLS (TCP) protocol.</p>
            scan_listener_port_tls: <p>The SCAN listener port for TLS (TCP) protocol.</p>
            tags: <p>Free-form tags for this resource. Each tag is a key-value pair with no predefined name, type, or namespace.</p>
            time_zone: <p>The time zone to use for the Autonomous VM cluster.</p>
            total_container_databases: <p>The total number of Autonomous CDBs that you can create in the Autonomous VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_cloud_autonomous_vm_cluster_input.CreateCloudAutonomousVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_cloud_autonomous_vm_cluster_output.CreateCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_autonomous_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_cloud_autonomous_vm_cluster.async_create_cloud_autonomous_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_cloud_autonomous_vm_cluster_input.CreateCloudAutonomousVmClusterInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "odb_network_id": odb_network_id,
            "display_name": display_name,
            "autonomous_data_storage_size_in_t_bs": autonomous_data_storage_size_in_t_bs,
            "cpu_core_count_per_node": cpu_core_count_per_node,
            "memory_per_oracle_compute_unit_in_g_bs": memory_per_oracle_compute_unit_in_g_bs,
            "total_container_databases": total_container_databases,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if db_servers is not None:
            input_["db_servers"] = db_servers
        if description is not None:
            input_["description"] = description
        if is_mtls_enabled_vm_cluster is not None:
            input_["is_mtls_enabled_vm_cluster"] = is_mtls_enabled_vm_cluster
        if license_model is not None:
            input_["license_model"] = license_model
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if scan_listener_port_non_tls is not None:
            input_["scan_listener_port_non_tls"] = scan_listener_port_non_tls
        if scan_listener_port_tls is not None:
            input_["scan_listener_port_tls"] = scan_listener_port_tls
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cloud_autonomous_vm_cluster(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_autonomous_vm_cluster_output.GetCloudAutonomousVmClusterOutput":
        """<p>Gets information about a specific Autonomous VM cluster.</p>

        Args:
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_cloud_autonomous_vm_cluster_input.GetCloudAutonomousVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_cloud_autonomous_vm_cluster_output.GetCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_autonomous_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_cloud_autonomous_vm_cluster.async_get_cloud_autonomous_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_cloud_autonomous_vm_cluster_input.GetCloudAutonomousVmClusterInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cloud_autonomous_vm_cluster(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_autonomous_vm_cluster_output.DeleteCloudAutonomousVmClusterOutput":
        """<p>Deletes an Autonomous VM cluster.</p>

        Args:
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_cloud_autonomous_vm_cluster_input.DeleteCloudAutonomousVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_cloud_autonomous_vm_cluster_output.DeleteCloudAutonomousVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_autonomous_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_cloud_autonomous_vm_cluster.async_delete_cloud_autonomous_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_cloud_autonomous_vm_cluster_input.DeleteCloudAutonomousVmClusterInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_cloud_autonomous_vm_clusters(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_exadata_infrastructure_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_cloud_autonomous_vm_clusters_output.ListCloudAutonomousVmClustersOutput":
        """<p>Lists all Autonomous VM clusters in a specified Cloud Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return per page.</p>
            next_token: <p>The pagination token to continue listing from.</p>
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Cloud Exadata Infrastructure that hosts the Autonomous VM clusters to be listed.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_cloud_autonomous_vm_clusters_input.ListCloudAutonomousVmClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_cloud_autonomous_vm_clusters_output.ListCloudAutonomousVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_autonomous_vm_clusters

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_cloud_autonomous_vm_clusters.async_list_cloud_autonomous_vm_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_cloud_autonomous_vm_clusters_input.ListCloudAutonomousVmClustersInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_exadata_infrastructure_id is not None:
            input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_cloud_autonomous_vm_clusters(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_exadata_infrastructure_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "AsyncIterator[capo_odb.types.cloud_autonomous_vm_cluster_summary.CloudAutonomousVmClusterSummary]":
        _token = next_token
        while True:
            _response = await self.list_cloud_autonomous_vm_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                cloud_exadata_infrastructure_id=cloud_exadata_infrastructure_id,
            )
            _page = _resolve_path(_response, ("cloud_autonomous_vm_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_autonomous_virtual_machines(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_autonomous_virtual_machines_output.ListAutonomousVirtualMachinesOutput":
        """<p>Lists all Autonomous VMs in an Autonomous VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return per page.</p>
            next_token: <p>The pagination token to continue listing from.</p>
            cloud_autonomous_vm_cluster_id: <p>The unique identifier of the Autonomous VM cluster whose virtual machines you're listing.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_autonomous_virtual_machines_input.ListAutonomousVirtualMachinesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_autonomous_virtual_machines_output.ListAutonomousVirtualMachinesOutput"
        ]:
            import capo_odb._operations.odb.list_autonomous_virtual_machines

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_autonomous_virtual_machines.async_list_autonomous_virtual_machines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_autonomous_virtual_machines_input.ListAutonomousVirtualMachinesInput = {
            "cloud_autonomous_vm_cluster_id": cloud_autonomous_vm_cluster_id
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

    async def iter_list_autonomous_virtual_machines(
        self,
        cloud_autonomous_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.autonomous_virtual_machine_summary.AutonomousVirtualMachineSummary]":
        _token = next_token
        while True:
            _response = await self.list_autonomous_virtual_machines(
                cloud_autonomous_vm_cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("autonomous_virtual_machines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_cloud_exadata_infrastructure(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        shape: "capo_odb.types.general_input_string.GeneralInputString",
        compute_count: int,
        storage_count: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        customer_contacts_to_send_to_oci: Optional[
            "capo_odb.types.customer_contacts.CustomerContacts"
        ] = None,
        maintenance_window: Optional[
            "capo_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        database_server_type: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        storage_server_type: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_cloud_exadata_infrastructure_output.CreateCloudExadataInfrastructureOutput":
        """<p>Creates an Exadata infrastructure.</p>

        Args:
            display_name: <p>A user-friendly name for the Exadata infrastructure.</p>
            shape: <p>The model name of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
            availability_zone: <p>The name of the Availability Zone (AZ) where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>us-east-1a</code> </p>
            availability_zone_id: <p>The AZ ID of the AZ where the Exadata infrastructure is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p> <p>Example: <code>use1-az1</code> </p>
            tags: <p>The list of resource tags to apply to the Exadata infrastructure.</p>
            compute_count: <p>The number of database servers for the Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>
            customer_contacts_to_send_to_oci: <p>The email addresses of contacts to receive notification from Oracle about maintenance updates for the Exadata infrastructure.</p>
            maintenance_window: <p>The maintenance window configuration for the Exadata Cloud infrastructure.</p> <p>This allows you to define when maintenance operations such as patching and updates can be performed on the infrastructure.</p>
            storage_count: <p>The number of storage servers to activate for this Exadata infrastructure. Valid values for this parameter depend on the shape. To get information about the minimum and maximum values, use the <code>ListDbSystemShapes</code> operation.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            database_server_type: <p>The database server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>
            storage_server_type: <p>The storage server model type of the Exadata infrastructure. For the list of valid model names, use the <code>ListDbSystemShapes</code> operation.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_cloud_exadata_infrastructure_input.CreateCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_cloud_exadata_infrastructure_output.CreateCloudExadataInfrastructureOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_cloud_exadata_infrastructure.async_create_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_cloud_exadata_infrastructure_input.CreateCloudExadataInfrastructureInput = {
            "display_name": display_name,
            "shape": shape,
            "compute_count": compute_count,
            "storage_count": storage_count,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if tags is not None:
            input_["tags"] = tags
        if customer_contacts_to_send_to_oci is not None:
            input_["customer_contacts_to_send_to_oci"] = (
                customer_contacts_to_send_to_oci
            )
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if database_server_type is not None:
            input_["database_server_type"] = database_server_type
        if storage_server_type is not None:
            input_["storage_server_type"] = storage_server_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cloud_exadata_infrastructure(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_exadata_infrastructure_output.GetCloudExadataInfrastructureOutput":
        """<p>Returns information about the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_cloud_exadata_infrastructure_input.GetCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_cloud_exadata_infrastructure_output.GetCloudExadataInfrastructureOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_cloud_exadata_infrastructure.async_get_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_cloud_exadata_infrastructure_input.GetCloudExadataInfrastructureInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cloud_exadata_infrastructure(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        maintenance_window: Optional[
            "capo_odb.types.maintenance_window.MaintenanceWindow"
        ] = None,
    ) -> "capo_odb.types.update_cloud_exadata_infrastructure_output.UpdateCloudExadataInfrastructureOutput":
        """<p>Updates the properties of an Exadata infrastructure resource.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure to update.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_cloud_exadata_infrastructure_input.UpdateCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_cloud_exadata_infrastructure_output.UpdateCloudExadataInfrastructureOutput"
        ]:
            import capo_odb._operations.odb.update_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_cloud_exadata_infrastructure.async_update_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_cloud_exadata_infrastructure_input.UpdateCloudExadataInfrastructureInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id
        }
        if maintenance_window is not None:
            input_["maintenance_window"] = maintenance_window

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cloud_exadata_infrastructure(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_exadata_infrastructure_output.DeleteCloudExadataInfrastructureOutput":
        """<p>Deletes the specified Exadata infrastructure. Before you use this operation, make sure to delete all of the VM clusters that are hosted on this Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_cloud_exadata_infrastructure_input.DeleteCloudExadataInfrastructureInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_cloud_exadata_infrastructure_output.DeleteCloudExadataInfrastructureOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_exadata_infrastructure

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_cloud_exadata_infrastructure.async_delete_cloud_exadata_infrastructure(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_cloud_exadata_infrastructure_input.DeleteCloudExadataInfrastructureInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_cloud_exadata_infrastructures(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_cloud_exadata_infrastructures_output.ListCloudExadataInfrastructuresOutput":
        """<p>Returns information about the Exadata infrastructures owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_cloud_exadata_infrastructures_input.ListCloudExadataInfrastructuresInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_cloud_exadata_infrastructures_output.ListCloudExadataInfrastructuresOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_exadata_infrastructures

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_cloud_exadata_infrastructures.async_list_cloud_exadata_infrastructures(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_cloud_exadata_infrastructures_input.ListCloudExadataInfrastructuresInput = {}
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

    async def iter_list_cloud_exadata_infrastructures(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.cloud_exadata_infrastructure_summary.CloudExadataInfrastructureSummary]":
        _token = next_token
        while True:
            _response = await self.list_cloud_exadata_infrastructures(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cloud_exadata_infrastructures",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_cloud_exadata_infrastructure_unallocated_resources(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
    ) -> "capo_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output.GetCloudExadataInfrastructureUnallocatedResourcesOutput":
        """<p>Retrieves information about unallocated resources in a specified Cloud Exadata Infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Cloud Exadata infrastructure for which to retrieve unallocated resources.</p>
            db_servers: <p>The database servers to include in the unallocated resources query.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input.GetCloudExadataInfrastructureUnallocatedResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_output.GetCloudExadataInfrastructureUnallocatedResourcesOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_exadata_infrastructure_unallocated_resources

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_cloud_exadata_infrastructure_unallocated_resources.async_get_cloud_exadata_infrastructure_unallocated_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_cloud_exadata_infrastructure_unallocated_resources_input.GetCloudExadataInfrastructureUnallocatedResourcesInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id
        }
        if db_servers is not None:
            input_["db_servers"] = db_servers

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_db_server(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        db_server_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_db_server_output.GetDbServerOutput":
        """<p>Returns information about the specified database server.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure that contains the database server.</p>
            db_server_id: <p>The unique identifier of the database server to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_db_server_input.GetDbServerInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_db_server_output.GetDbServerOutput"
        ]:
            import capo_odb._operations.odb.get_db_server

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_db_server.async_get_db_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_db_server_input.GetDbServerInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "db_server_id": db_server_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_db_servers(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_db_servers_output.ListDbServersOutput":
        """<p>Returns information about the database servers that belong to the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_db_servers_input.ListDbServersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_db_servers_output.ListDbServersOutput"
        ]:
            import capo_odb._operations.odb.list_db_servers

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_db_servers.async_list_db_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_db_servers_input.ListDbServersInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id
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

    async def iter_list_db_servers(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.db_server_summary.DbServerSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_servers(
                cloud_exadata_infrastructure_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("db_servers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_cloud_vm_cluster(
        self,
        cloud_exadata_infrastructure_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        cpu_core_count: int,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        gi_version: str,
        hostname: "capo_odb.types.hostname.Hostname",
        ssh_public_keys: "capo_odb.types.string_list.StringList",
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cluster_name: Optional["capo_odb.types.cluster_name.ClusterName"] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        data_storage_size_in_t_bs: Optional[float] = None,
        db_node_storage_size_in_g_bs: Optional[int] = None,
        db_servers: Optional["capo_odb.types.string_list.StringList"] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        is_local_backup_enabled: Optional[bool] = None,
        is_sparse_diskgroup_enabled: Optional[bool] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        memory_size_in_g_bs: Optional[int] = None,
        system_version: Optional[str] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        scan_listener_port_tcp: Optional[int] = None,
    ) -> "capo_odb.types.create_cloud_vm_cluster_output.CreateCloudVmClusterOutput":
        """<p>Creates a VM cluster on the specified Exadata infrastructure.</p>

        Args:
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Exadata infrastructure for this VM cluster.</p>
            cpu_core_count: <p>The number of CPU cores to enable on the VM cluster.</p>
            display_name: <p>A user-friendly name for the VM cluster.</p>
            gi_version: <p>A valid software version of Oracle Grid Infrastructure (GI). To get the list of valid values, use the <code>ListGiVersions</code> operation and specify the shape of the Exadata infrastructure.</p> <p>Example: <code>19.0.0.0</code> </p>
            hostname: <p>The host name for the VM cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be "localhost" or "hostname".</p> </li> <li> <p>Can't contain "-version".</p> </li> <li> <p>The maximum length of the combined hostname and domain is 63 characters.</p> </li> <li> <p>The hostname must be unique within the subnet.</p> </li> </ul>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the VM cluster.</p>
            odb_network_id: <p>The unique identifier of the ODB network for the VM cluster.</p>
            cluster_name: <p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the VM cluster.</p>
            data_storage_size_in_t_bs: <p>The size of the data disk group, in terabytes (TBs), to allocate for the VM cluster.</p>
            db_node_storage_size_in_g_bs: <p>The amount of local node storage, in gigabytes (GB), to allocate for the VM cluster.</p>
            db_servers: <p>The list of database servers for the VM cluster.</p>
            tags: <p>The list of resource tags to apply to the VM cluster.</p>
            is_local_backup_enabled: <p>Specifies whether to enable database backups to local Exadata storage for the VM cluster.</p>
            is_sparse_diskgroup_enabled: <p>Specifies whether to create a sparse disk group for the VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the VM cluster.</p> <p>Default: <code>LICENSE_INCLUDED</code> </p>
            memory_size_in_g_bs: <p>The amount of memory, in gigabytes (GB), to allocate for the VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the VM cluster.</p>
            time_zone: <p>The time zone for the VM cluster. For a list of valid values for time zone, you can check the options in the console.</p> <p>Default: UTC</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            scan_listener_port_tcp: <p>The port number for TCP connections to the single client access name (SCAN) listener. </p> <p>Valid values: <code>1024–8999</code> with the following exceptions: <code>2484</code>, <code>6100</code>, <code>6200</code>, <code>7060</code>, <code>7070</code>, <code>7085</code>, and <code>7879</code> </p> <p>Default: <code>1521</code> </p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_cloud_vm_cluster_input.CreateCloudVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_cloud_vm_cluster_output.CreateCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_cloud_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_cloud_vm_cluster.async_create_cloud_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_cloud_vm_cluster_input.CreateCloudVmClusterInput = {
            "cloud_exadata_infrastructure_id": cloud_exadata_infrastructure_id,
            "cpu_core_count": cpu_core_count,
            "display_name": display_name,
            "gi_version": gi_version,
            "hostname": hostname,
            "ssh_public_keys": ssh_public_keys,
            "odb_network_id": odb_network_id,
        }
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if data_storage_size_in_t_bs is not None:
            input_["data_storage_size_in_t_bs"] = data_storage_size_in_t_bs
        if db_node_storage_size_in_g_bs is not None:
            input_["db_node_storage_size_in_g_bs"] = db_node_storage_size_in_g_bs
        if db_servers is not None:
            input_["db_servers"] = db_servers
        if tags is not None:
            input_["tags"] = tags
        if is_local_backup_enabled is not None:
            input_["is_local_backup_enabled"] = is_local_backup_enabled
        if is_sparse_diskgroup_enabled is not None:
            input_["is_sparse_diskgroup_enabled"] = is_sparse_diskgroup_enabled
        if license_model is not None:
            input_["license_model"] = license_model
        if memory_size_in_g_bs is not None:
            input_["memory_size_in_g_bs"] = memory_size_in_g_bs
        if system_version is not None:
            input_["system_version"] = system_version
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scan_listener_port_tcp is not None:
            input_["scan_listener_port_tcp"] = scan_listener_port_tcp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cloud_vm_cluster(
        self,
        cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_cloud_vm_cluster_output.GetCloudVmClusterOutput":
        """<p>Returns information about the specified VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_cloud_vm_cluster_input.GetCloudVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_cloud_vm_cluster_output.GetCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_cloud_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_cloud_vm_cluster.async_get_cloud_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_cloud_vm_cluster_input.GetCloudVmClusterInput = {
            "cloud_vm_cluster_id": cloud_vm_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cloud_vm_cluster(
        self,
        cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_cloud_vm_cluster_output.DeleteCloudVmClusterOutput":
        """<p>Deletes the specified VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_cloud_vm_cluster_input.DeleteCloudVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_cloud_vm_cluster_output.DeleteCloudVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_cloud_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_cloud_vm_cluster.async_delete_cloud_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_cloud_vm_cluster_input.DeleteCloudVmClusterInput = {
            "cloud_vm_cluster_id": cloud_vm_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_cloud_vm_clusters(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_exadata_infrastructure_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_cloud_vm_clusters_output.ListCloudVmClustersOutput":
        """<p>Returns information about the VM clusters owned by your Amazon Web Services account or only the ones on the specified Exadata infrastructure.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_exadata_infrastructure_id: <p>The unique identifier of the Oracle Exadata infrastructure.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_cloud_vm_clusters_input.ListCloudVmClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_cloud_vm_clusters_output.ListCloudVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_cloud_vm_clusters

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_cloud_vm_clusters.async_list_cloud_vm_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_cloud_vm_clusters_input.ListCloudVmClustersInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_exadata_infrastructure_id is not None:
            input_["cloud_exadata_infrastructure_id"] = cloud_exadata_infrastructure_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_cloud_vm_clusters(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_exadata_infrastructure_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "AsyncIterator[capo_odb.types.cloud_vm_cluster_summary.CloudVmClusterSummary]":
        _token = next_token
        while True:
            _response = await self.list_cloud_vm_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                cloud_exadata_infrastructure_id=cloud_exadata_infrastructure_id,
            )
            _page = _resolve_path(_response, ("cloud_vm_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.get_db_node_output.GetDbNodeOutput":
        """<p>Returns information about the specified DB node.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_db_node_input.GetDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_db_node_output.GetDbNodeOutput"
        ]:
            import capo_odb._operations.odb.get_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_db_node.async_get_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_db_node_input.GetDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_db_nodes(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.list_db_nodes_output.ListDbNodesOutput":
        """<p>Returns information about the DB nodes for the specified VM cluster.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_db_nodes_input.ListDbNodesInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_db_nodes_output.ListDbNodesOutput"
        ]:
            import capo_odb._operations.odb.list_db_nodes

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_db_nodes.async_list_db_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_db_nodes_input.ListDbNodesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_db_nodes(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "AsyncIterator[capo_odb.types.db_node_summary.DbNodeSummary]":
        _token = next_token
        while True:
            _response = await self.list_db_nodes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                cloud_vm_cluster_id=cloud_vm_cluster_id,
                exadb_vm_cluster_id=exadb_vm_cluster_id,
            )
            _page = _resolve_path(_response, ("db_nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reboot_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.reboot_db_node_output.RebootDbNodeOutput":
        """<p>Reboots the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to reboot. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to reboot. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to reboot.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.reboot_db_node_input.RebootDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.reboot_db_node_output.RebootDbNodeOutput"
        ]:
            import capo_odb._operations.odb.reboot_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.reboot_db_node.async_reboot_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.reboot_db_node_input.RebootDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.start_db_node_output.StartDbNodeOutput":
        """<p>Starts the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to start. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to start. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to start.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.start_db_node_input.StartDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.start_db_node_output.StartDbNodeOutput"
        ]:
            import capo_odb._operations.odb.start_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.start_db_node.async_start_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.start_db_node_input.StartDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_db_node(
        self,
        db_node_id: "capo_odb.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cloud_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
        exadb_vm_cluster_id: Optional["capo_odb.types.resource_id.ResourceId"] = None,
    ) -> "capo_odb.types.stop_db_node_output.StopDbNodeOutput":
        """<p>Stops the specified DB node in a VM cluster.</p>

        Args:
            cloud_vm_cluster_id: <p>The unique identifier of the VM cluster that contains the DB node to stop. You must specify either this parameter or <code>exadbVmClusterId</code>.</p>
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster that contains the DB node to stop. You must specify either this parameter or <code>cloudVmClusterId</code>.</p>
            db_node_id: <p>The unique identifier of the DB node to stop.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.stop_db_node_input.StopDbNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.stop_db_node_output.StopDbNodeOutput"
        ]:
            import capo_odb._operations.odb.stop_db_node

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.stop_db_node.async_stop_db_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.stop_db_node_input.StopDbNodeInput = {
            "db_node_id": db_node_id
        }
        if cloud_vm_cluster_id is not None:
            input_["cloud_vm_cluster_id"] = cloud_vm_cluster_id
        if exadb_vm_cluster_id is not None:
            input_["exadb_vm_cluster_id"] = exadb_vm_cluster_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_exadb_vm_cluster(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        enabled_ecpu_count: int,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        grid_image_id: str,
        hostname: "capo_odb.types.hostname.Hostname",
        node_count: int,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        shape: str,
        ssh_public_keys: "capo_odb.types.string_list.StringList",
        total_ecpu_count: int,
        vm_file_system_storage_total_size_in_g_bs: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        cluster_name: Optional["capo_odb.types.cluster_name.ClusterName"] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        scan_listener_port_tcp: Optional[int] = None,
        scan_listener_port_tcp_ssl: Optional[int] = None,
        shape_attribute: Optional[
            "capo_odb.types.shape_attribute.ShapeAttribute"
        ] = None,
        system_version: Optional[str] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_exadb_vm_cluster_output.CreateExadbVmClusterOutput":
        """<p>Creates an Exascale VM cluster.</p>

        Args:
            display_name: <p>A user-friendly name for the Exascale VM cluster.</p>
            enabled_ecpu_count: <p>The number of ECPUs to enable for the Exascale VM cluster.</p>
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault for this Exascale VM cluster.</p>
            grid_image_id: <p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>
            hostname: <p>The host name for the Exascale VM cluster.</p>
            node_count: <p>The number of nodes in the Exascale VM cluster.</p>
            odb_network_id: <p>The unique identifier of the ODB network for the Exascale VM cluster.</p>
            shape: <p>The shape of the Exascale VM cluster.</p>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>
            total_ecpu_count: <p>The total number of ECPUs for the Exascale VM cluster.</p>
            vm_file_system_storage_total_size_in_g_bs: <p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>
            cluster_name: <p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Exascale VM cluster.</p>
            scan_listener_port_tcp: <p>The port number for TCP connections to the Single Client Access Name (SCAN) listener.</p>
            scan_listener_port_tcp_ssl: <p>The port number for TCP connections with SSL to the Single Client Access Name (SCAN) listener.</p>
            shape_attribute: <p>The shape attribute for the Exascale VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the Exascale VM cluster.</p>
            tags: <p>The list of resource tags to apply to the Exascale VM cluster.</p>
            time_zone: <p>The time zone for the Exascale VM cluster.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_exadb_vm_cluster_input.CreateExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_exadb_vm_cluster_output.CreateExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.create_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_exadb_vm_cluster.async_create_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_exadb_vm_cluster_input.CreateExadbVmClusterInput = {
            "display_name": display_name,
            "enabled_ecpu_count": enabled_ecpu_count,
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id,
            "grid_image_id": grid_image_id,
            "hostname": hostname,
            "node_count": node_count,
            "odb_network_id": odb_network_id,
            "shape": shape,
            "ssh_public_keys": ssh_public_keys,
            "total_ecpu_count": total_ecpu_count,
            "vm_file_system_storage_total_size_in_g_bs": vm_file_system_storage_total_size_in_g_bs,
        }
        if cluster_name is not None:
            input_["cluster_name"] = cluster_name
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if license_model is not None:
            input_["license_model"] = license_model
        if scan_listener_port_tcp is not None:
            input_["scan_listener_port_tcp"] = scan_listener_port_tcp
        if scan_listener_port_tcp_ssl is not None:
            input_["scan_listener_port_tcp_ssl"] = scan_listener_port_tcp_ssl
        if shape_attribute is not None:
            input_["shape_attribute"] = shape_attribute
        if system_version is not None:
            input_["system_version"] = system_version
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_exadb_vm_cluster_output.GetExadbVmClusterOutput":
        """<p>Returns information about the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_exadb_vm_cluster_input.GetExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_exadb_vm_cluster_output.GetExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.get_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_exadb_vm_cluster.async_get_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_exadb_vm_cluster_input.GetExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        data_collection_options: Optional[
            "capo_odb.types.data_collection_options.DataCollectionOptions"
        ] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        enabled_ecpu_count: Optional[int] = None,
        grid_image_id: Optional[str] = None,
        license_model: Optional["capo_odb.types.license_model.LicenseModel"] = None,
        ssh_public_keys: Optional["capo_odb.types.string_list.StringList"] = None,
        system_version: Optional[str] = None,
        total_ecpu_count: Optional[int] = None,
        update_action: Optional["capo_odb.types.update_action.UpdateAction"] = None,
        vm_file_system_storage_total_size_in_g_bs: Optional[int] = None,
    ) -> "capo_odb.types.update_exadb_vm_cluster_output.UpdateExadbVmClusterOutput":
        """<p>Updates the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to update.</p>
            data_collection_options: <p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>
            display_name: <p>A new user-friendly name for the Exascale VM cluster.</p>
            enabled_ecpu_count: <p>The number of ECPUs to enable for the Exascale VM cluster.</p>
            grid_image_id: <p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>
            license_model: <p>The Oracle license model to apply to the Exascale VM cluster.</p>
            ssh_public_keys: <p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>
            system_version: <p>The version of the operating system of the image for the Exascale VM cluster.</p>
            total_ecpu_count: <p>The total number of ECPUs for the Exascale VM cluster.</p>
            update_action: <p>The update action to perform on the Exascale VM cluster.</p>
            vm_file_system_storage_total_size_in_g_bs: <p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_exadb_vm_cluster_input.UpdateExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_exadb_vm_cluster_output.UpdateExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.update_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_exadb_vm_cluster.async_update_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_exadb_vm_cluster_input.UpdateExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
        }
        if data_collection_options is not None:
            input_["data_collection_options"] = data_collection_options
        if display_name is not None:
            input_["display_name"] = display_name
        if enabled_ecpu_count is not None:
            input_["enabled_ecpu_count"] = enabled_ecpu_count
        if grid_image_id is not None:
            input_["grid_image_id"] = grid_image_id
        if license_model is not None:
            input_["license_model"] = license_model
        if ssh_public_keys is not None:
            input_["ssh_public_keys"] = ssh_public_keys
        if system_version is not None:
            input_["system_version"] = system_version
        if total_ecpu_count is not None:
            input_["total_ecpu_count"] = total_ecpu_count
        if update_action is not None:
            input_["update_action"] = update_action
        if vm_file_system_storage_total_size_in_g_bs is not None:
            input_["vm_file_system_storage_total_size_in_g_bs"] = (
                vm_file_system_storage_total_size_in_g_bs
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_exadb_vm_cluster_output.DeleteExadbVmClusterOutput":
        """<p>Deletes the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_exadb_vm_cluster_input.DeleteExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_exadb_vm_cluster_output.DeleteExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.delete_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_exadb_vm_cluster.async_delete_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_exadb_vm_cluster_input.DeleteExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_exadb_vm_clusters(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        exascale_db_storage_vault_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_exadb_vm_clusters_output.ListExadbVmClustersOutput":
        """<p>Returns information about the Exascale VM clusters owned by your Amazon Web Services account.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to list the associated Exascale VM clusters.</p>
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_exadb_vm_clusters_input.ListExadbVmClustersInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_exadb_vm_clusters_output.ListExadbVmClustersOutput"
        ]:
            import capo_odb._operations.odb.list_exadb_vm_clusters

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_exadb_vm_clusters.async_list_exadb_vm_clusters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_exadb_vm_clusters_input.ListExadbVmClustersInput = {}
        if exascale_db_storage_vault_id is not None:
            input_["exascale_db_storage_vault_id"] = exascale_db_storage_vault_id
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

    async def iter_list_exadb_vm_clusters(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        exascale_db_storage_vault_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.exadb_vm_cluster_summary.ExadbVmClusterSummary]":
        _token = next_token
        while True:
            _response = await self.list_exadb_vm_clusters(
                config_overrides=config_overrides,
                exascale_db_storage_vault_id=exascale_db_storage_vault_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exadb_vm_clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_virtual_machines_to_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        desired_node_count: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output.AssociateVirtualMachinesToExadbVmClusterOutput":
        """<p>Adds virtual machines to the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to add virtual machines to.</p>
            desired_node_count: <p>The desired number of nodes in the Exascale VM cluster after the association.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input.AssociateVirtualMachinesToExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_output.AssociateVirtualMachinesToExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.associate_virtual_machines_to_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.associate_virtual_machines_to_exadb_vm_cluster.async_associate_virtual_machines_to_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.associate_virtual_machines_to_exadb_vm_cluster_input.AssociateVirtualMachinesToExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id,
            "desired_node_count": desired_node_count,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_virtual_machines_from_exadb_vm_cluster(
        self,
        exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        db_node_ids: "capo_odb.types.resource_id_list.ResourceIdList",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output.DisassociateVirtualMachinesFromExadbVmClusterOutput":
        """<p>Removes virtual machines from the specified Exascale VM cluster.</p>

        Args:
            exadb_vm_cluster_id: <p>The unique identifier of the Exascale VM cluster to remove virtual machines from.</p>
            db_node_ids: <p>The list of DB node IDs to remove from the Exascale VM cluster.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input.DisassociateVirtualMachinesFromExadbVmClusterInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_output.DisassociateVirtualMachinesFromExadbVmClusterOutput"
        ]:
            import capo_odb._operations.odb.disassociate_virtual_machines_from_exadb_vm_cluster

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.disassociate_virtual_machines_from_exadb_vm_cluster.async_disassociate_virtual_machines_from_exadb_vm_cluster(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.disassociate_virtual_machines_from_exadb_vm_cluster_input.DisassociateVirtualMachinesFromExadbVmClusterInput = {
            "exadb_vm_cluster_id": exadb_vm_cluster_id,
            "db_node_ids": db_node_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_exascale_db_storage_vault(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        high_capacity_database_storage_total_size_in_g_bs: int,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        additional_flash_cache_in_percent: Optional[int] = None,
        autoscale_limit_in_g_bs: Optional[int] = None,
        availability_zone_id: Optional[str] = None,
        availability_zone: Optional[str] = None,
        description: Optional[str] = None,
        is_autoscale_enabled: Optional[bool] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
        time_zone: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
    ) -> "capo_odb.types.create_exascale_db_storage_vault_output.CreateExascaleDbStorageVaultOutput":
        """<p>Creates an Exascale storage vault.</p>

        Args:
            display_name: <p>A user-friendly name for the Exascale storage vault.</p>
            high_capacity_database_storage_total_size_in_g_bs: <p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>
            additional_flash_cache_in_percent: <p>The additional flash cache percentage for the Exascale storage vault.</p>
            autoscale_limit_in_g_bs: <p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>
            availability_zone_id: <p>The Availability Zone ID for the Exascale storage vault.</p>
            availability_zone: <p>The Availability Zone for the Exascale storage vault.</p>
            description: <p>A description of the Exascale storage vault.</p>
            is_autoscale_enabled: <p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>
            tags: <p>The list of resource tags to apply to the Exascale storage vault.</p>
            time_zone: <p>The time zone for the Exascale storage vault.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_exascale_db_storage_vault_input.CreateExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_exascale_db_storage_vault_output.CreateExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.create_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_exascale_db_storage_vault.async_create_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_exascale_db_storage_vault_input.CreateExascaleDbStorageVaultInput = {
            "display_name": display_name,
            "high_capacity_database_storage_total_size_in_g_bs": high_capacity_database_storage_total_size_in_g_bs,
        }
        if additional_flash_cache_in_percent is not None:
            input_["additional_flash_cache_in_percent"] = (
                additional_flash_cache_in_percent
            )
        if autoscale_limit_in_g_bs is not None:
            input_["autoscale_limit_in_g_bs"] = autoscale_limit_in_g_bs
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if description is not None:
            input_["description"] = description
        if is_autoscale_enabled is not None:
            input_["is_autoscale_enabled"] = is_autoscale_enabled
        if tags is not None:
            input_["tags"] = tags
        if time_zone is not None:
            input_["time_zone"] = time_zone
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_exascale_db_storage_vault(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_exascale_db_storage_vault_output.GetExascaleDbStorageVaultOutput":
        """<p>Returns information about the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_exascale_db_storage_vault_input.GetExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_exascale_db_storage_vault_output.GetExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.get_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_exascale_db_storage_vault.async_get_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_exascale_db_storage_vault_input.GetExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_exascale_db_storage_vault(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        additional_flash_cache_in_percent: Optional[int] = None,
        autoscale_limit_in_g_bs: Optional[int] = None,
        description: Optional[str] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        high_capacity_database_storage_total_size_in_g_bs: Optional[int] = None,
        is_autoscale_enabled: Optional[bool] = None,
    ) -> "capo_odb.types.update_exascale_db_storage_vault_output.UpdateExascaleDbStorageVaultOutput":
        """<p>Updates the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to update.</p>
            additional_flash_cache_in_percent: <p>The additional flash cache percentage for the Exascale storage vault.</p>
            autoscale_limit_in_g_bs: <p>The autoscale limit in gigabytes (GB) for the Exascale storage vault.</p>
            description: <p>A new description for the Exascale storage vault.</p>
            display_name: <p>A new user-friendly name for the Exascale storage vault.</p>
            high_capacity_database_storage_total_size_in_g_bs: <p>The total size of the high-capacity database storage, in gigabytes (GB), for the Exascale storage vault.</p>
            is_autoscale_enabled: <p>Specifies whether autoscaling is enabled for the Exascale storage vault.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_exascale_db_storage_vault_input.UpdateExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_exascale_db_storage_vault_output.UpdateExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.update_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_exascale_db_storage_vault.async_update_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_exascale_db_storage_vault_input.UpdateExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
        }
        if additional_flash_cache_in_percent is not None:
            input_["additional_flash_cache_in_percent"] = (
                additional_flash_cache_in_percent
            )
        if autoscale_limit_in_g_bs is not None:
            input_["autoscale_limit_in_g_bs"] = autoscale_limit_in_g_bs
        if description is not None:
            input_["description"] = description
        if display_name is not None:
            input_["display_name"] = display_name
        if high_capacity_database_storage_total_size_in_g_bs is not None:
            input_["high_capacity_database_storage_total_size_in_g_bs"] = (
                high_capacity_database_storage_total_size_in_g_bs
            )
        if is_autoscale_enabled is not None:
            input_["is_autoscale_enabled"] = is_autoscale_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_exascale_db_storage_vault(
        self,
        exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_exascale_db_storage_vault_output.DeleteExascaleDbStorageVaultOutput":
        """<p>Deletes the specified Exascale storage vault.</p>

        Args:
            exascale_db_storage_vault_id: <p>The unique identifier of the Exascale storage vault to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_exascale_db_storage_vault_input.DeleteExascaleDbStorageVaultInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_exascale_db_storage_vault_output.DeleteExascaleDbStorageVaultOutput"
        ]:
            import capo_odb._operations.odb.delete_exascale_db_storage_vault

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_exascale_db_storage_vault.async_delete_exascale_db_storage_vault(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_exascale_db_storage_vault_input.DeleteExascaleDbStorageVaultInput = {
            "exascale_db_storage_vault_id": exascale_db_storage_vault_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_exascale_db_storage_vaults(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_exascale_db_storage_vaults_output.ListExascaleDbStorageVaultsOutput":
        """<p>Returns information about the Exascale storage vaults owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_exascale_db_storage_vaults_input.ListExascaleDbStorageVaultsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_exascale_db_storage_vaults_output.ListExascaleDbStorageVaultsOutput"
        ]:
            import capo_odb._operations.odb.list_exascale_db_storage_vaults

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_exascale_db_storage_vaults.async_list_exascale_db_storage_vaults(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_exascale_db_storage_vaults_input.ListExascaleDbStorageVaultsInput = {}
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

    async def iter_list_exascale_db_storage_vaults(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.exascale_db_storage_vault_summary.ExascaleDbStorageVaultSummary]":
        _token = next_token
        while True:
            _response = await self.list_exascale_db_storage_vaults(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exascale_db_storage_vaults",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_odb_network(
        self,
        display_name: "capo_odb.types.resource_display_name.ResourceDisplayName",
        client_subnet_cidr: str,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        availability_zone: Optional[str] = None,
        availability_zone_id: Optional[str] = None,
        backup_subnet_cidr: Optional[str] = None,
        custom_domain_name: Optional[str] = None,
        default_dns_prefix: Optional[str] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        s3_access: Optional["capo_odb.types.access.Access"] = None,
        zero_etl_access: Optional["capo_odb.types.access.Access"] = None,
        sts_access: Optional["capo_odb.types.access.Access"] = None,
        kms_access: Optional["capo_odb.types.access.Access"] = None,
        s3_policy_document: Optional[
            "capo_odb.types.policy_document.PolicyDocument"
        ] = None,
        sts_policy_document: Optional[
            "capo_odb.types.policy_document.PolicyDocument"
        ] = None,
        kms_policy_document: Optional[
            "capo_odb.types.policy_document.PolicyDocument"
        ] = None,
        cross_region_s3_restore_sources_to_enable: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_odb_network_output.CreateOdbNetworkOutput":
        """<p>Creates an ODB network.</p>

        Args:
            display_name: <p>A user-friendly name for the ODB network.</p>
            availability_zone: <p>The Amazon Web Services Availability Zone (AZ) where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>
            availability_zone_id: <p>The AZ ID of the AZ where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>
            client_subnet_cidr: <p>The CIDR range of the client subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the backup subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>
            backup_subnet_cidr: <p>The CIDR range of the backup subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the client subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>
            custom_domain_name: <p>The domain name to use for the resources in the ODB network.</p>
            default_dns_prefix: <p>The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>
            s3_access: <p>Specifies the configuration for Amazon S3 access from the ODB network.</p>
            zero_etl_access: <p>Specifies the configuration for Zero-ETL access from the ODB network.</p>
            sts_access: <p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>
            kms_access: <p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>
            s3_policy_document: <p>Specifies the endpoint policy for Amazon S3 access from the ODB network.</p>
            sts_policy_document: <p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>
            kms_policy_document: <p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>
            cross_region_s3_restore_sources_to_enable: <p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>
            tags: <p>The list of resource tags to apply to the ODB network.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the service quota.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_odb_network_input.CreateOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_odb_network_output.CreateOdbNetworkOutput"
        ]:
            import capo_odb._operations.odb.create_odb_network

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_odb_network.async_create_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_odb_network_input.CreateOdbNetworkInput = {
            "display_name": display_name,
            "client_subnet_cidr": client_subnet_cidr,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if availability_zone_id is not None:
            input_["availability_zone_id"] = availability_zone_id
        if backup_subnet_cidr is not None:
            input_["backup_subnet_cidr"] = backup_subnet_cidr
        if custom_domain_name is not None:
            input_["custom_domain_name"] = custom_domain_name
        if default_dns_prefix is not None:
            input_["default_dns_prefix"] = default_dns_prefix
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if s3_access is not None:
            input_["s3_access"] = s3_access
        if zero_etl_access is not None:
            input_["zero_etl_access"] = zero_etl_access
        if sts_access is not None:
            input_["sts_access"] = sts_access
        if kms_access is not None:
            input_["kms_access"] = kms_access
        if s3_policy_document is not None:
            input_["s3_policy_document"] = s3_policy_document
        if sts_policy_document is not None:
            input_["sts_policy_document"] = sts_policy_document
        if kms_policy_document is not None:
            input_["kms_policy_document"] = kms_policy_document
        if cross_region_s3_restore_sources_to_enable is not None:
            input_["cross_region_s3_restore_sources_to_enable"] = (
                cross_region_s3_restore_sources_to_enable
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_odb_network(
        self,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.get_odb_network_output.GetOdbNetworkOutput":
        """<p>Returns information about the specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_odb_network_input.GetOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_odb_network_output.GetOdbNetworkOutput"
        ]:
            import capo_odb._operations.odb.get_odb_network

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_odb_network.async_get_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_odb_network_input.GetOdbNetworkInput = {
            "odb_network_id": odb_network_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_odb_network(
        self,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peered_cidrs_to_be_added: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        peered_cidrs_to_be_removed: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        s3_access: Optional["capo_odb.types.access.Access"] = None,
        zero_etl_access: Optional["capo_odb.types.access.Access"] = None,
        sts_access: Optional["capo_odb.types.access.Access"] = None,
        kms_access: Optional["capo_odb.types.access.Access"] = None,
        s3_policy_document: Optional[
            "capo_odb.types.policy_document.PolicyDocument"
        ] = None,
        sts_policy_document: Optional[
            "capo_odb.types.policy_document.PolicyDocument"
        ] = None,
        kms_policy_document: Optional[
            "capo_odb.types.policy_document.PolicyDocument"
        ] = None,
        cross_region_s3_restore_sources_to_enable: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
        cross_region_s3_restore_sources_to_disable: Optional[
            "capo_odb.types.string_list.StringList"
        ] = None,
    ) -> "capo_odb.types.update_odb_network_output.UpdateOdbNetworkOutput":
        """<p>Updates properties of a specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to update.</p>
            display_name: <p>The new user-friendly name of the ODB network.</p>
            peered_cidrs_to_be_added: <p>The list of CIDR ranges from the peered VPC that allow access to the ODB network.</p>
            peered_cidrs_to_be_removed: <p>The list of CIDR ranges from the peered VPC to remove from the ODB network.</p>
            s3_access: <p>Specifies the updated configuration for Amazon S3 access from the ODB network.</p>
            zero_etl_access: <p>Specifies the updated configuration for Zero-ETL access from the ODB network.</p>
            sts_access: <p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>
            kms_access: <p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>
            s3_policy_document: <p>Specifies the updated endpoint policy for Amazon S3 access from the ODB network.</p>
            sts_policy_document: <p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>
            kms_policy_document: <p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>
            cross_region_s3_restore_sources_to_enable: <p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>
            cross_region_s3_restore_sources_to_disable: <p>The cross-Region Amazon S3 restore sources to disable for the ODB network.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_odb_network_input.UpdateOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_odb_network_output.UpdateOdbNetworkOutput"
        ]:
            import capo_odb._operations.odb.update_odb_network

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_odb_network.async_update_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_odb_network_input.UpdateOdbNetworkInput = {
            "odb_network_id": odb_network_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peered_cidrs_to_be_added is not None:
            input_["peered_cidrs_to_be_added"] = peered_cidrs_to_be_added
        if peered_cidrs_to_be_removed is not None:
            input_["peered_cidrs_to_be_removed"] = peered_cidrs_to_be_removed
        if s3_access is not None:
            input_["s3_access"] = s3_access
        if zero_etl_access is not None:
            input_["zero_etl_access"] = zero_etl_access
        if sts_access is not None:
            input_["sts_access"] = sts_access
        if kms_access is not None:
            input_["kms_access"] = kms_access
        if s3_policy_document is not None:
            input_["s3_policy_document"] = s3_policy_document
        if sts_policy_document is not None:
            input_["sts_policy_document"] = sts_policy_document
        if kms_policy_document is not None:
            input_["kms_policy_document"] = kms_policy_document
        if cross_region_s3_restore_sources_to_enable is not None:
            input_["cross_region_s3_restore_sources_to_enable"] = (
                cross_region_s3_restore_sources_to_enable
            )
        if cross_region_s3_restore_sources_to_disable is not None:
            input_["cross_region_s3_restore_sources_to_disable"] = (
                cross_region_s3_restore_sources_to_disable
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_odb_network(
        self,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        delete_associated_resources: bool,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_odb_network_output.DeleteOdbNetworkOutput":
        """<p>Deletes the specified ODB network.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network to delete.</p>
            delete_associated_resources: <p>Specifies whether to delete associated OCI networking resources along with the ODB network.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_odb_network_input.DeleteOdbNetworkInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_odb_network_output.DeleteOdbNetworkOutput"
        ]:
            import capo_odb._operations.odb.delete_odb_network

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_odb_network.async_delete_odb_network(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_odb_network_input.DeleteOdbNetworkInput = {
            "odb_network_id": odb_network_id,
            "delete_associated_resources": delete_associated_resources,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_odb_networks(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_odb.types.list_odb_networks_output.ListOdbNetworksOutput":
        """<p>Returns information about the ODB networks owned by your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>
            next_token: <p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_odb_networks_input.ListOdbNetworksInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_odb_networks_output.ListOdbNetworksOutput"
        ]:
            import capo_odb._operations.odb.list_odb_networks

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_odb_networks.async_list_odb_networks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_odb_networks_input.ListOdbNetworksInput = {}
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

    async def iter_list_odb_networks(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_odb.types.odb_network_summary.OdbNetworkSummary]":
        _token = next_token
        while True:
            _response = await self.list_odb_networks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("odb_networks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_odb_peering_connection(
        self,
        odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        peer_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peer_network_cidrs_to_be_added: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
        peer_network_route_table_ids: Optional[
            "capo_odb.types.peer_network_route_table_id_list.PeerNetworkRouteTableIdList"
        ] = None,
        client_token: Optional[
            "capo_odb.types.general_input_string.GeneralInputString"
        ] = None,
        tags: Optional["capo_odb.types.request_tag_map.RequestTagMap"] = None,
    ) -> "capo_odb.types.create_odb_peering_connection_output.CreateOdbPeeringConnectionOutput":
        """<p>Creates a peering connection between an ODB network and a VPC.</p> <p>A peering connection enables private connectivity between the networks for application-tier communication.</p>

        Args:
            odb_network_id: <p>The unique identifier of the ODB network that initiates the peering connection.</p>
            peer_network_id: <p>The unique identifier of the peer network. This can be either a VPC ID or another ODB network ID.</p>
            display_name: <p>The display name for the ODB peering connection.</p>
            peer_network_cidrs_to_be_added: <p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.</p>
            peer_network_route_table_ids: <p>The unique identifier of the VPC route table for which a route to the ODB network is automatically created during peering connection establishment.</p>
            client_token: <p>The client token for the ODB peering connection request.</p> <p>Constraints:</p> <ul> <li> <p>Must be unique for each request.</p> </li> </ul>
            tags: <p>The tags to assign to the ODB peering connection.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.create_odb_peering_connection_input.CreateOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.create_odb_peering_connection_output.CreateOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.create_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.create_odb_peering_connection.async_create_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.create_odb_peering_connection_input.CreateOdbPeeringConnectionInput = {
            "odb_network_id": odb_network_id,
            "peer_network_id": peer_network_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peer_network_cidrs_to_be_added is not None:
            input_["peer_network_cidrs_to_be_added"] = peer_network_cidrs_to_be_added
        if peer_network_route_table_ids is not None:
            input_["peer_network_route_table_ids"] = peer_network_route_table_ids
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_odb_peering_connection(
        self,
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> (
        "capo_odb.types.get_odb_peering_connection_output.GetOdbPeeringConnectionOutput"
    ):
        """<p>Retrieves information about an ODB peering connection.</p>

        Args:
            odb_peering_connection_id: <p>The unique identifier of the ODB peering connection to retrieve information about.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.get_odb_peering_connection_input.GetOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.get_odb_peering_connection_output.GetOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.get_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.get_odb_peering_connection.async_get_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.get_odb_peering_connection_input.GetOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_odb_peering_connection(
        self,
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        display_name: Optional[
            "capo_odb.types.resource_display_name.ResourceDisplayName"
        ] = None,
        peer_network_cidrs_to_be_added: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
        peer_network_cidrs_to_be_removed: Optional[
            "capo_odb.types.peered_cidr_list.PeeredCidrList"
        ] = None,
    ) -> "capo_odb.types.update_odb_peering_connection_output.UpdateOdbPeeringConnectionOutput":
        """<p>Modifies the settings of an Oracle Database@Amazon Web Services peering connection. You can update the display name and add or remove CIDR blocks from the peering connection.</p>

        Args:
            odb_peering_connection_id: <p>The identifier of the Oracle Database@Amazon Web Services peering connection to update.</p>
            display_name: <p>A new display name for the peering connection.</p>
            peer_network_cidrs_to_be_added: <p>A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection. The CIDR blocks must not overlap with existing CIDR blocks in the Oracle Database@Amazon Web Services network.</p>
            peer_network_cidrs_to_be_removed: <p>A list of CIDR blocks to remove from the peering connection. The CIDR blocks must currently exist in the peering connection.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.update_odb_peering_connection_input.UpdateOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.update_odb_peering_connection_output.UpdateOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.update_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.update_odb_peering_connection.async_update_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.update_odb_peering_connection_input.UpdateOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if peer_network_cidrs_to_be_added is not None:
            input_["peer_network_cidrs_to_be_added"] = peer_network_cidrs_to_be_added
        if peer_network_cidrs_to_be_removed is not None:
            input_["peer_network_cidrs_to_be_removed"] = (
                peer_network_cidrs_to_be_removed
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_odb_peering_connection(
        self,
        odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn",
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
    ) -> "capo_odb.types.delete_odb_peering_connection_output.DeleteOdbPeeringConnectionOutput":
        """<p>Deletes an ODB peering connection.</p> <p>When you delete an ODB peering connection, the underlying VPC peering connection is also deleted.</p>

        Args:
            odb_peering_connection_id: <p>The unique identifier of the ODB peering connection to delete.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.delete_odb_peering_connection_input.DeleteOdbPeeringConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.delete_odb_peering_connection_output.DeleteOdbPeeringConnectionOutput"
        ]:
            import capo_odb._operations.odb.delete_odb_peering_connection

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.delete_odb_peering_connection.async_delete_odb_peering_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.delete_odb_peering_connection_input.DeleteOdbPeeringConnectionInput = {
            "odb_peering_connection_id": odb_peering_connection_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_odb_peering_connections(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "capo_odb.types.list_odb_peering_connections_output.ListOdbPeeringConnectionsOutput":
        """<p>Lists all ODB peering connections or those associated with a specific ODB network.</p>

        Args:
            max_results: <p>The maximum number of ODB peering connections to return in the response.</p> <p>Default: <code>20</code> </p> <p>Constraints:</p> <ul> <li> <p>Must be between 1 and 100.</p> </li> </ul>
            next_token: <p>The pagination token for the next page of ODB peering connections.</p>
            odb_network_id: <p>The identifier of the ODB network to list peering connections for.</p> <p>If not specified, lists all ODB peering connections in the account.</p>

        Raises:
            capo_odb.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.</p>
            capo_odb.errors.internal_server_exception.InternalServerException: <p>Occurs when there is an internal failure in the Oracle Database@Amazon Web Services service. Wait and try again.</p>
            capo_odb.errors.resource_not_found_exception.ResourceNotFoundException: <p>The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.</p>
            capo_odb.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_odb.errors.validation_exception.ValidationException: <p>The request has failed validation because it is missing required fields or has invalid inputs.</p>
            capo_odb.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_odb.types.list_odb_peering_connections_input.ListOdbPeeringConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_odb.types.list_odb_peering_connections_output.ListOdbPeeringConnectionsOutput"
        ]:
            import capo_odb._operations.odb.list_odb_peering_connections

            (
                output,
                http_response,
            ) = await capo_odb._operations.odb.list_odb_peering_connections.async_list_odb_peering_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_odb.types.list_odb_peering_connections_input.ListOdbPeeringConnectionsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if odb_network_id is not None:
            input_["odb_network_id"] = odb_network_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_odb_peering_connections(
        self,
        *,
        config_overrides: Optional[AsyncodbClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
        odb_network_id: Optional[
            "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
        ] = None,
    ) -> "AsyncIterator[capo_odb.types.odb_peering_connection_summary.OdbPeeringConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_odb_peering_connections(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                odb_network_id=odb_network_id,
            )
            _page = _resolve_path(_response, ("odb_peering_connections",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
