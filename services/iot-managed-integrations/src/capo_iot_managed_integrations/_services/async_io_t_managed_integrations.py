"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#IotManagedIntegrations``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iot_managed_integrations._auth._signers
import capo_iot_managed_integrations._auth._sigv4
from capo_iot_managed_integrations._auth._identity import Credentials
from capo_iot_managed_integrations._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iot_managed_integrations._auth._zapros_handler import AuthMiddleware
from capo_iot_managed_integrations._pagination import resolve_path as _resolve_path
from capo_iot_managed_integrations._resources.iot_managed_integrations.account_association_resource import (
    AsyncAccountAssociationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.cloud_connector_resource import (
    AsyncCloudConnectorResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.connector_destination_resource import (
    AsyncConnectorDestinationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.credential_locker_resource import (
    AsyncCredentialLockerResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.destination_resource import (
    AsyncDestinationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.device_discovery_resource import (
    AsyncDeviceDiscoveryResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.event_log_configuration_resource import (
    AsyncEventLogConfigurationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.hub_configuration_resource import (
    AsyncHubConfigurationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.kms_key_association_resource import (
    AsyncKmsKeyAssociationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_association_resource import (
    AsyncManagedThingAssociationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_command_resource import (
    AsyncManagedThingCommandResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_resource import (
    AsyncManagedThingResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.managed_thing_state_resource import (
    AsyncManagedThingStateResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.notification_configuration_resource import (
    AsyncNotificationConfigurationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.ota_task_configuration_resource import (
    AsyncOtaTaskConfigurationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.ota_task_resource import (
    AsyncOtaTaskResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.provisioning_profile_resource import (
    AsyncProvisioningProfileResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.runtime_log_configuration_resource import (
    AsyncRuntimeLogConfigurationResource,
)
from capo_iot_managed_integrations._resources.iot_managed_integrations.schema_version_resource import (
    AsyncSchemaVersionResource,
)
from capo_iot_managed_integrations._services._aws_config import aaws_config
from capo_iot_managed_integrations._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_description
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.account_association_item
    import capo_iot_managed_integrations.types.account_association_name
    import capo_iot_managed_integrations.types.auth_config
    import capo_iot_managed_integrations.types.auth_config_update
    import capo_iot_managed_integrations.types.auth_material_string
    import capo_iot_managed_integrations.types.auth_material_type
    import capo_iot_managed_integrations.types.auth_type
    import capo_iot_managed_integrations.types.brand
    import capo_iot_managed_integrations.types.ca_certificate
    import capo_iot_managed_integrations.types.capabilities
    import capo_iot_managed_integrations.types.capability_id
    import capo_iot_managed_integrations.types.capability_report
    import capo_iot_managed_integrations.types.capability_schemas
    import capo_iot_managed_integrations.types.claim_certificate
    import capo_iot_managed_integrations.types.classification
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.cloud_connector_description
    import capo_iot_managed_integrations.types.cloud_connector_id
    import capo_iot_managed_integrations.types.cloud_connector_type
    import capo_iot_managed_integrations.types.command_endpoints
    import capo_iot_managed_integrations.types.connector_association_id
    import capo_iot_managed_integrations.types.connector_destination_description
    import capo_iot_managed_integrations.types.connector_destination_id
    import capo_iot_managed_integrations.types.connector_destination_name
    import capo_iot_managed_integrations.types.connector_destination_summary
    import capo_iot_managed_integrations.types.connector_device_id
    import capo_iot_managed_integrations.types.connector_device_id_list
    import capo_iot_managed_integrations.types.connector_event_message
    import capo_iot_managed_integrations.types.connector_event_operation
    import capo_iot_managed_integrations.types.connector_event_operation_version
    import capo_iot_managed_integrations.types.connector_event_status_code
    import capo_iot_managed_integrations.types.connector_id
    import capo_iot_managed_integrations.types.connector_item
    import capo_iot_managed_integrations.types.connector_policy_id
    import capo_iot_managed_integrations.types.create_account_association_request
    import capo_iot_managed_integrations.types.create_account_association_response
    import capo_iot_managed_integrations.types.create_cloud_connector_request
    import capo_iot_managed_integrations.types.create_cloud_connector_response
    import capo_iot_managed_integrations.types.create_connector_destination_request
    import capo_iot_managed_integrations.types.create_connector_destination_response
    import capo_iot_managed_integrations.types.create_credential_locker_request
    import capo_iot_managed_integrations.types.create_credential_locker_response
    import capo_iot_managed_integrations.types.create_destination_request
    import capo_iot_managed_integrations.types.create_destination_response
    import capo_iot_managed_integrations.types.create_event_log_configuration_request
    import capo_iot_managed_integrations.types.create_event_log_configuration_response
    import capo_iot_managed_integrations.types.create_managed_thing_request
    import capo_iot_managed_integrations.types.create_managed_thing_response
    import capo_iot_managed_integrations.types.create_notification_configuration_request
    import capo_iot_managed_integrations.types.create_notification_configuration_response
    import capo_iot_managed_integrations.types.create_ota_task_configuration_request
    import capo_iot_managed_integrations.types.create_ota_task_configuration_response
    import capo_iot_managed_integrations.types.create_ota_task_request
    import capo_iot_managed_integrations.types.create_ota_task_response
    import capo_iot_managed_integrations.types.create_provisioning_profile_request
    import capo_iot_managed_integrations.types.create_provisioning_profile_response
    import capo_iot_managed_integrations.types.credential_locker_id
    import capo_iot_managed_integrations.types.credential_locker_name
    import capo_iot_managed_integrations.types.credential_locker_summary
    import capo_iot_managed_integrations.types.custom_protocol_detail
    import capo_iot_managed_integrations.types.delete_account_association_request
    import capo_iot_managed_integrations.types.delete_cloud_connector_request
    import capo_iot_managed_integrations.types.delete_connector_destination_request
    import capo_iot_managed_integrations.types.delete_credential_locker_request
    import capo_iot_managed_integrations.types.delete_destination_request
    import capo_iot_managed_integrations.types.delete_event_log_configuration_request
    import capo_iot_managed_integrations.types.delete_managed_thing_request
    import capo_iot_managed_integrations.types.delete_notification_configuration_request
    import capo_iot_managed_integrations.types.delete_ota_task_configuration_request
    import capo_iot_managed_integrations.types.delete_ota_task_request
    import capo_iot_managed_integrations.types.delete_provisioning_profile_request
    import capo_iot_managed_integrations.types.delivery_destination_arn
    import capo_iot_managed_integrations.types.delivery_destination_role_arn
    import capo_iot_managed_integrations.types.delivery_destination_type
    import capo_iot_managed_integrations.types.deregister_account_association_request
    import capo_iot_managed_integrations.types.destination_description
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.destination_summary
    import capo_iot_managed_integrations.types.device_discovery_id
    import capo_iot_managed_integrations.types.device_discovery_status
    import capo_iot_managed_integrations.types.device_discovery_summary
    import capo_iot_managed_integrations.types.devices
    import capo_iot_managed_integrations.types.discovered_device_summary
    import capo_iot_managed_integrations.types.discovery_auth_material_string
    import capo_iot_managed_integrations.types.discovery_auth_material_type
    import capo_iot_managed_integrations.types.discovery_type
    import capo_iot_managed_integrations.types.display_name
    import capo_iot_managed_integrations.types.encryption_type
    import capo_iot_managed_integrations.types.endpoint_config
    import capo_iot_managed_integrations.types.endpoint_id
    import capo_iot_managed_integrations.types.endpoint_type
    import capo_iot_managed_integrations.types.event_log_configuration_summary
    import capo_iot_managed_integrations.types.event_type
    import capo_iot_managed_integrations.types.general_authorization_name
    import capo_iot_managed_integrations.types.get_account_association_request
    import capo_iot_managed_integrations.types.get_account_association_response
    import capo_iot_managed_integrations.types.get_cloud_connector_request
    import capo_iot_managed_integrations.types.get_cloud_connector_response
    import capo_iot_managed_integrations.types.get_connector_destination_request
    import capo_iot_managed_integrations.types.get_connector_destination_response
    import capo_iot_managed_integrations.types.get_credential_locker_request
    import capo_iot_managed_integrations.types.get_credential_locker_response
    import capo_iot_managed_integrations.types.get_custom_endpoint_request
    import capo_iot_managed_integrations.types.get_custom_endpoint_response
    import capo_iot_managed_integrations.types.get_default_encryption_configuration_request
    import capo_iot_managed_integrations.types.get_default_encryption_configuration_response
    import capo_iot_managed_integrations.types.get_destination_request
    import capo_iot_managed_integrations.types.get_destination_response
    import capo_iot_managed_integrations.types.get_device_discovery_request
    import capo_iot_managed_integrations.types.get_device_discovery_response
    import capo_iot_managed_integrations.types.get_event_log_configuration_request
    import capo_iot_managed_integrations.types.get_event_log_configuration_response
    import capo_iot_managed_integrations.types.get_hub_configuration_request
    import capo_iot_managed_integrations.types.get_hub_configuration_response
    import capo_iot_managed_integrations.types.get_managed_thing_capabilities_request
    import capo_iot_managed_integrations.types.get_managed_thing_capabilities_response
    import capo_iot_managed_integrations.types.get_managed_thing_certificate_request
    import capo_iot_managed_integrations.types.get_managed_thing_certificate_response
    import capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request
    import capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response
    import capo_iot_managed_integrations.types.get_managed_thing_meta_data_request
    import capo_iot_managed_integrations.types.get_managed_thing_meta_data_response
    import capo_iot_managed_integrations.types.get_managed_thing_request
    import capo_iot_managed_integrations.types.get_managed_thing_response
    import capo_iot_managed_integrations.types.get_managed_thing_state_request
    import capo_iot_managed_integrations.types.get_managed_thing_state_response
    import capo_iot_managed_integrations.types.get_notification_configuration_request
    import capo_iot_managed_integrations.types.get_notification_configuration_response
    import capo_iot_managed_integrations.types.get_ota_task_configuration_request
    import capo_iot_managed_integrations.types.get_ota_task_configuration_response
    import capo_iot_managed_integrations.types.get_ota_task_request
    import capo_iot_managed_integrations.types.get_ota_task_response
    import capo_iot_managed_integrations.types.get_provisioning_profile_request
    import capo_iot_managed_integrations.types.get_provisioning_profile_response
    import capo_iot_managed_integrations.types.get_runtime_log_configuration_request
    import capo_iot_managed_integrations.types.get_runtime_log_configuration_response
    import capo_iot_managed_integrations.types.get_schema_version_request
    import capo_iot_managed_integrations.types.get_schema_version_response
    import capo_iot_managed_integrations.types.hub_network_mode
    import capo_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds
    import capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn
    import capo_iot_managed_integrations.types.kms_key_arn
    import capo_iot_managed_integrations.types.lambda_arn
    import capo_iot_managed_integrations.types.list_account_associations_request
    import capo_iot_managed_integrations.types.list_account_associations_response
    import capo_iot_managed_integrations.types.list_cloud_connectors_request
    import capo_iot_managed_integrations.types.list_cloud_connectors_response
    import capo_iot_managed_integrations.types.list_connector_destinations_request
    import capo_iot_managed_integrations.types.list_connector_destinations_response
    import capo_iot_managed_integrations.types.list_credential_lockers_request
    import capo_iot_managed_integrations.types.list_credential_lockers_response
    import capo_iot_managed_integrations.types.list_destinations_request
    import capo_iot_managed_integrations.types.list_destinations_response
    import capo_iot_managed_integrations.types.list_device_discoveries_request
    import capo_iot_managed_integrations.types.list_device_discoveries_response
    import capo_iot_managed_integrations.types.list_discovered_devices_request
    import capo_iot_managed_integrations.types.list_discovered_devices_response
    import capo_iot_managed_integrations.types.list_event_log_configurations_request
    import capo_iot_managed_integrations.types.list_event_log_configurations_response
    import capo_iot_managed_integrations.types.list_managed_thing_account_associations_request
    import capo_iot_managed_integrations.types.list_managed_thing_account_associations_response
    import capo_iot_managed_integrations.types.list_managed_thing_schemas_request
    import capo_iot_managed_integrations.types.list_managed_thing_schemas_response
    import capo_iot_managed_integrations.types.list_managed_things_request
    import capo_iot_managed_integrations.types.list_managed_things_response
    import capo_iot_managed_integrations.types.list_notification_configurations_request
    import capo_iot_managed_integrations.types.list_notification_configurations_response
    import capo_iot_managed_integrations.types.list_ota_task_configurations_request
    import capo_iot_managed_integrations.types.list_ota_task_configurations_response
    import capo_iot_managed_integrations.types.list_ota_task_executions_request
    import capo_iot_managed_integrations.types.list_ota_task_executions_response
    import capo_iot_managed_integrations.types.list_ota_tasks_request
    import capo_iot_managed_integrations.types.list_ota_tasks_response
    import capo_iot_managed_integrations.types.list_provisioning_profiles_request
    import capo_iot_managed_integrations.types.list_provisioning_profiles_response
    import capo_iot_managed_integrations.types.list_schema_versions_request
    import capo_iot_managed_integrations.types.list_schema_versions_response
    import capo_iot_managed_integrations.types.list_tags_for_resource_request
    import capo_iot_managed_integrations.types.list_tags_for_resource_response
    import capo_iot_managed_integrations.types.log_configuration_id
    import capo_iot_managed_integrations.types.log_level
    import capo_iot_managed_integrations.types.managed_thing_association
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.managed_thing_schema_list_item
    import capo_iot_managed_integrations.types.managed_thing_summary
    import capo_iot_managed_integrations.types.matter_endpoint
    import capo_iot_managed_integrations.types.max_results
    import capo_iot_managed_integrations.types.meta_data
    import capo_iot_managed_integrations.types.model
    import capo_iot_managed_integrations.types.name
    import capo_iot_managed_integrations.types.next_token
    import capo_iot_managed_integrations.types.notification_configuration_summary
    import capo_iot_managed_integrations.types.ota_description
    import capo_iot_managed_integrations.types.ota_mechanism
    import capo_iot_managed_integrations.types.ota_next_token
    import capo_iot_managed_integrations.types.ota_protocol
    import capo_iot_managed_integrations.types.ota_target_query_string
    import capo_iot_managed_integrations.types.ota_task_configuration_id
    import capo_iot_managed_integrations.types.ota_task_configuration_name
    import capo_iot_managed_integrations.types.ota_task_configuration_summary
    import capo_iot_managed_integrations.types.ota_task_execution_retry_config
    import capo_iot_managed_integrations.types.ota_task_execution_summaries
    import capo_iot_managed_integrations.types.ota_task_id
    import capo_iot_managed_integrations.types.ota_task_scheduling_config
    import capo_iot_managed_integrations.types.ota_task_summary
    import capo_iot_managed_integrations.types.ota_type
    import capo_iot_managed_integrations.types.owner
    import capo_iot_managed_integrations.types.parent_controller_id
    import capo_iot_managed_integrations.types.protocol_type
    import capo_iot_managed_integrations.types.provisioning_profile_id
    import capo_iot_managed_integrations.types.provisioning_profile_name
    import capo_iot_managed_integrations.types.provisioning_profile_summary
    import capo_iot_managed_integrations.types.provisioning_status
    import capo_iot_managed_integrations.types.provisioning_type
    import capo_iot_managed_integrations.types.push_config
    import capo_iot_managed_integrations.types.put_default_encryption_configuration_request
    import capo_iot_managed_integrations.types.put_default_encryption_configuration_response
    import capo_iot_managed_integrations.types.put_hub_configuration_request
    import capo_iot_managed_integrations.types.put_hub_configuration_response
    import capo_iot_managed_integrations.types.put_runtime_log_configuration_request
    import capo_iot_managed_integrations.types.register_account_association_request
    import capo_iot_managed_integrations.types.register_account_association_response
    import capo_iot_managed_integrations.types.register_custom_endpoint_request
    import capo_iot_managed_integrations.types.register_custom_endpoint_response
    import capo_iot_managed_integrations.types.reset_runtime_log_configuration_request
    import capo_iot_managed_integrations.types.role
    import capo_iot_managed_integrations.types.runtime_log_configurations
    import capo_iot_managed_integrations.types.s3_url
    import capo_iot_managed_integrations.types.schema_id
    import capo_iot_managed_integrations.types.schema_version_format
    import capo_iot_managed_integrations.types.schema_version_list_item
    import capo_iot_managed_integrations.types.schema_version_namespace_name
    import capo_iot_managed_integrations.types.schema_version_type
    import capo_iot_managed_integrations.types.schema_version_version
    import capo_iot_managed_integrations.types.schema_version_visibility
    import capo_iot_managed_integrations.types.schema_versioned_id
    import capo_iot_managed_integrations.types.secrets_manager
    import capo_iot_managed_integrations.types.send_connector_event_request
    import capo_iot_managed_integrations.types.send_connector_event_response
    import capo_iot_managed_integrations.types.send_managed_thing_command_request
    import capo_iot_managed_integrations.types.send_managed_thing_command_response
    import capo_iot_managed_integrations.types.serial_number
    import capo_iot_managed_integrations.types.smart_home_resource_id
    import capo_iot_managed_integrations.types.smart_home_resource_type
    import capo_iot_managed_integrations.types.start_account_association_refresh_request
    import capo_iot_managed_integrations.types.start_account_association_refresh_response
    import capo_iot_managed_integrations.types.start_device_discovery_request
    import capo_iot_managed_integrations.types.start_device_discovery_response
    import capo_iot_managed_integrations.types.tag_key_list
    import capo_iot_managed_integrations.types.tag_resource_request
    import capo_iot_managed_integrations.types.tag_resource_response
    import capo_iot_managed_integrations.types.tags_map
    import capo_iot_managed_integrations.types.target
    import capo_iot_managed_integrations.types.third_party_user_id
    import capo_iot_managed_integrations.types.trace_id
    import capo_iot_managed_integrations.types.untag_resource_request
    import capo_iot_managed_integrations.types.untag_resource_response
    import capo_iot_managed_integrations.types.update_account_association_request
    import capo_iot_managed_integrations.types.update_cloud_connector_request
    import capo_iot_managed_integrations.types.update_connector_destination_request
    import capo_iot_managed_integrations.types.update_destination_request
    import capo_iot_managed_integrations.types.update_event_log_configuration_request
    import capo_iot_managed_integrations.types.update_managed_thing_request
    import capo_iot_managed_integrations.types.update_notification_configuration_request
    import capo_iot_managed_integrations.types.update_ota_task_request
    import capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration


class AsyncIoTManagedIntegrationsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncIoTManagedIntegrationsClient:
    """A client for the ``IoTManagedIntegrations`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = AsyncIoTManagedIntegrationsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.account_association_resource = AsyncAccountAssociationResource(self)
        self.cloud_connector_resource = AsyncCloudConnectorResource(self)
        self.connector_destination_resource = AsyncConnectorDestinationResource(self)
        self.credential_locker_resource = AsyncCredentialLockerResource(self)
        self.destination_resource = AsyncDestinationResource(self)
        self.device_discovery_resource = AsyncDeviceDiscoveryResource(self)
        self.event_log_configuration_resource = AsyncEventLogConfigurationResource(self)
        self.hub_configuration_resource = AsyncHubConfigurationResource(self)
        self.kms_key_association_resource = AsyncKmsKeyAssociationResource(self)
        self.managed_thing_association_resource = AsyncManagedThingAssociationResource(
            self
        )
        self.managed_thing_command_resource = AsyncManagedThingCommandResource(self)
        self.managed_thing_resource = AsyncManagedThingResource(self)
        self.managed_thing_state_resource = AsyncManagedThingStateResource(self)
        self.notification_configuration_resource = (
            AsyncNotificationConfigurationResource(self)
        )
        self.ota_task_configuration_resource = AsyncOtaTaskConfigurationResource(self)
        self.ota_task_resource = AsyncOtaTaskResource(self)
        self.provisioning_profile_resource = AsyncProvisioningProfileResource(self)
        self.runtime_log_configuration_resource = AsyncRuntimeLogConfigurationResource(
            self
        )
        self.schema_version_resource = AsyncSchemaVersionResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTManagedIntegrationsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def get_custom_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_custom_endpoint_response.GetCustomEndpointResponse":
        """<p>Returns the IoT managed integrations custom endpoint.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_custom_endpoint_request.GetCustomEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_custom_endpoint_response.GetCustomEndpointResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_custom_endpoint

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_custom_endpoint.async_get_custom_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_custom_endpoint_request.GetCustomEndpointRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_iot_managed_integrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_custom_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.register_custom_endpoint_response.RegisterCustomEndpointResponse":
        """<p>Customers can request IoT managed integrations to manage the server trust for them or bring their own external server trusts for the custom domain. Returns an IoT managed integrations endpoint.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.register_custom_endpoint_request.RegisterCustomEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.register_custom_endpoint_response.RegisterCustomEndpointResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.register_custom_endpoint

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.register_custom_endpoint.async_register_custom_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.register_custom_endpoint_request.RegisterCustomEndpointRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_connector_event(
        self,
        connector_id: "capo_iot_managed_integrations.types.connector_id.ConnectorId",
        operation: "capo_iot_managed_integrations.types.connector_event_operation.ConnectorEventOperation",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        user_id: Optional[
            "capo_iot_managed_integrations.types.third_party_user_id.ThirdPartyUserId"
        ] = None,
        operation_version: Optional[
            "capo_iot_managed_integrations.types.connector_event_operation_version.ConnectorEventOperationVersion"
        ] = None,
        status_code: Optional[
            "capo_iot_managed_integrations.types.connector_event_status_code.ConnectorEventStatusCode"
        ] = None,
        message: Optional[
            "capo_iot_managed_integrations.types.connector_event_message.ConnectorEventMessage"
        ] = None,
        device_discovery_id: Optional[
            "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId"
        ] = None,
        connector_device_id: Optional[
            "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
        ] = None,
        trace_id: Optional[
            "capo_iot_managed_integrations.types.trace_id.TraceId"
        ] = None,
        devices: Optional["capo_iot_managed_integrations.types.devices.Devices"] = None,
        matter_endpoint: Optional[
            "capo_iot_managed_integrations.types.matter_endpoint.MatterEndpoint"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.send_connector_event_response.SendConnectorEventResponse":
        r"""<p>Relays third-party device events for a connector such as a new device or a device state change event.</p>

        Args:
            connector_id: <p>The id of the connector between the third-party cloud provider and IoT managed integrations.</p>
            user_id: <p>The id of the third-party cloud provider.</p>
            operation: <p>The Open Connectivity Foundation (OCF) operation requested to be performed on the managed thing.</p> <note> <p>The field op can have a value of \"I\" or \"U\". The field \"cn\" will contain the capability types.</p> </note>
            operation_version: <p>The Open Connectivity Foundation (OCF) security specification version for the operation being requested on the managed thing. For more information, see <a href=\"https://openconnectivity.org/specs/OCF_Security_Specification_v1.0.0.pdf\">OCF Security Specification</a>.</p>
            status_code: <p>The status code of the Open Connectivity Foundation (OCF) operation being performed on the managed thing.</p>
            message: <p>The device state change event payload.</p> <p>This parameter will include the following three fields:</p> <ul> <li> <p> <code>uri</code>: <code>schema auc://&lt;PARTNER-DEVICE-ID&gt;/ResourcePath</code> (The <code>Resourcepath</code> corresponds to an OCF resource.)</p> </li> <li> <p> <code>op</code>: For device state changes, this field must populate as <code>n+d</code>.</p> </li> <li> <p> <code>cn</code>: The content depends on the OCF resource referenced in <code>ResourcePath</code>.</p> </li> </ul>
            device_discovery_id: <p>The id for the device discovery job.</p>
            connector_device_id: <p>The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>
            trace_id: <p>The trace request identifier. This is generated by IoT managed integrations and can be used to trace this command and its related operations in CloudWatch.</p>
            devices: <p>The list of devices.</p>
            matter_endpoint: <p>The device endpoint.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            SendConnectorEvent happy path for device discovery

            >>> await client.send_connector_event(connector_id='MockConnectorId', user_id='MockThirdPartyUserId', operation='DEVICE_DISCOVERY', operation_version='1.0', status_code=200, message='Sample ConnectorEventMessage', device_discovery_id='358275hbk3qr', devices=[{'ConnectorDeviceId': 'Mock-Connector-DeviceId-1', 'ConnectorDeviceName': 'Sample-User-device-1', 'CapabilityReport': {'version': '1.0.0', 'nodeId': '1', 'endpoints': [{'id': 'EP1', 'deviceTypes': ['Refrigerator'], 'clusters': [{'id': '0x0201', 'revision': 1, 'attributes': [{'id': '0x0000', 'value': 'exampleString'}, {'id': '0x0001'}, {'id': '0x0002'}], 'commands': ['0x00', '0x01'], 'events': []}]}]}}])
            SendConnectorEvent happy path for device command response

            >>> await client.send_connector_event(connector_id='MockConnectorId', user_id='MockThirdPartyUserId', operation='DEVICE_COMMAND_RESPONSE', operation_version='1.0', status_code=200, message='Sample ConnectorEventMessage', trace_id='9b75f3839b6140f=_1', matter_endpoint={'id': '1', 'clusters': [{'id': '0x1003', 'attributes': {'0x0000': [73], '0x15570003': 'exampleString'}, 'commands': {'0x03': {}}}]})
            SendConnectorEvent happy path for device event

            >>> await client.send_connector_event(connector_id='MockConnectorId', user_id='MockThirdPartyUserId', operation='DEVICE_EVENT', operation_version='1.0', status_code=200, message='Sample ConnectorEventMessage', trace_id='TraceId-Sample', matter_endpoint={'id': '1', 'clusters': [{'id': '0x1003', 'attributes': {'0x0000': 73}}]})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.send_connector_event_request.SendConnectorEventRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.send_connector_event_response.SendConnectorEventResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.send_connector_event

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.send_connector_event.async_send_connector_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.send_connector_event_request.SendConnectorEventRequest = {
            "connector_id": connector_id,
            "operation": operation,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if operation_version is not None:
            input_["operation_version"] = operation_version
        if status_code is not None:
            input_["status_code"] = status_code
        if message is not None:
            input_["message"] = message
        if device_discovery_id is not None:
            input_["device_discovery_id"] = device_discovery_id
        if connector_device_id is not None:
            input_["connector_device_id"] = connector_device_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if devices is not None:
            input_["devices"] = devices
        if matter_endpoint is not None:
            input_["matter_endpoint"] = matter_endpoint

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN",
        tags: "capo_iot_managed_integrations.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> (
        "capo_iot_managed_integrations.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Adds tags to a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>
            tags: <p>A set of key/value pairs that are used to manage the resource.</p>

        Raises:
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.tag_resource

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_iot_managed_integrations.types.io_t_managed_integrations_resource_arn.IoTManagedIntegrationsResourceARN",
        tag_keys: "capo_iot_managed_integrations.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of tag keys to remove from the resource.</p>

        Raises:
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.invalid_request_exception.InvalidRequestException: <p>The request is not valid.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.untag_resource

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_account_association(
        self,
        connector_destination_id: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        general_authorization: Optional[
            "capo_iot_managed_integrations.types.general_authorization_name.GeneralAuthorizationName"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse":
        """<p>Creates a new account association via the destination id.</p>

        Args:
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            connector_destination_id: <p>The identifier of the connector destination.</p>
            name: <p>The name of the destination for the new account association.</p>
            description: <p>A description of the account association request.</p>
            tags: <p>A set of key/value pairs that are used to manage the account association.</p>
            general_authorization: <p>The General Authorization reference by authorization material name.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_account_association_response.CreateAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_account_association.async_create_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_account_association_request.CreateAccountAssociationRequest = {
            "connector_destination_id": connector_destination_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if general_authorization is not None:
            input_["general_authorization"] = general_authorization

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_association(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse":
        """<p>Get an account association for an Amazon Web Services account linked to a customer-managed destination.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to retrieve.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_account_association_response.GetAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_account_association.async_get_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_account_association_request.GetAccountAssociationRequest = {
            "account_association_id": account_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_account_association(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.account_association_name.AccountAssociationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.account_association_description.AccountAssociationDescription"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing account association.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to update.</p>
            name: <p>The new name to assign to the account association.</p>
            description: <p>The new description to assign to the account association.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_account_association.async_update_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_account_association_request.UpdateAccountAssociationRequest = {
            "account_association_id": account_association_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_account_association(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Remove a third-party account association for an end user.</p> <note> <p>You must first call the <code>DeregisterAccountAssociation</code> to remove the connection between the managed thing and the third-party account before calling the <code>DeleteAccountAssociation</code> API.</p> </note>

        Args:
            account_association_id: <p>The unique identifier of the account association to be deleted.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_account_association.async_delete_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_account_association_request.DeleteAccountAssociationRequest = {
            "account_association_id": account_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        connector_destination_id: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse":
        """<p>Lists all account associations, with optional filtering by connector destination ID.</p>

        Args:
            connector_destination_id: <p>The identifier of the connector destination to filter account associations by.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_account_associations_response.ListAccountAssociationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_account_associations.async_list_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_account_associations_request.ListAccountAssociationsRequest = {}
        if connector_destination_id is not None:
            input_["connector_destination_id"] = connector_destination_id
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

    async def iter_list_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        connector_destination_id: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.account_association_item.AccountAssociationItem]":
        _token = next_token
        while True:
            _response = await self.list_account_associations(
                config_overrides=config_overrides,
                connector_destination_id=connector_destination_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_account_association_refresh(
        self,
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse":
        """<p>Initiates a refresh of an existing account association to update its authorization and connection status.</p>

        Args:
            account_association_id: <p>The unique identifier of the account association to refresh.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.start_account_association_refresh_response.StartAccountAssociationRefreshResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.start_account_association_refresh.async_start_account_association_refresh(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.start_account_association_refresh_request.StartAccountAssociationRefreshRequest = {
            "account_association_id": account_association_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cloud_connector(
        self,
        name: "capo_iot_managed_integrations.types.display_name.DisplayName",
        endpoint_config: "capo_iot_managed_integrations.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
        endpoint_type: Optional[
            "capo_iot_managed_integrations.types.endpoint_type.EndpointType"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_cloud_connector_response.CreateCloudConnectorResponse":
        """<p>Creates a C2C (cloud-to-cloud) connector.</p>

        Args:
            name: <p>The display name of the C2C connector.</p>
            endpoint_config: <p>The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.</p>
            description: <p>A description of the C2C connector.</p>
            endpoint_type: <p>The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            CreateCloudConnector happy path for TP Link

            >>> await client.create_cloud_connector(name='Connector for TP Link Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion'}}, client_token='1234567890')
            CreateCloudConnector happy path for Ring

            >>> await client.create_cloud_connector(name='Connector for Ring Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion'}}, client_token='12312321')
            CreateCloudConnector error path for Ring connector which already exists

            >>> await client.create_cloud_connector(name='Connector for Ring Cloud', endpoint_type='LAMBDA', endpoint_config={'lambda': {'arn': 'arn:aws:lambda:us-east-1:111122223333:function:my-function:myVersion2'}}, client_token='1213123123')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_cloud_connector_request.CreateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_cloud_connector_response.CreateCloudConnectorResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_cloud_connector.async_create_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_cloud_connector_request.CreateCloudConnectorRequest = {
            "name": name,
            "endpoint_config": endpoint_config,
        }
        if description is not None:
            input_["description"] = description
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
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

    async def get_cloud_connector(
        self,
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_cloud_connector_response.GetCloudConnectorResponse":
        """<p>Get configuration details for a cloud connector.</p>

        Args:
            identifier: <p>The identifier of the C2C connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetCloudConnector happy path for TP Link to get connector resource

            >>> await client.get_cloud_connector(identifier='123456789012')
            GetCloudConnector happy path for Ring to pending status

            >>> await client.get_cloud_connector(identifier='123456789012')
            GetCloudConnector error Id for Ring connector which does not exist

            >>> await client.get_cloud_connector(identifier='123456789012')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_cloud_connector_request.GetCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_cloud_connector_response.GetCloudConnectorResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_cloud_connector.async_get_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_cloud_connector_request.GetCloudConnectorRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cloud_connector(
        self,
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
    ) -> None:
        """<p>Update an existing cloud connector.</p>

        Args:
            identifier: <p>The unique identifier of the cloud connector to update.</p>
            name: <p>The new display name to assign to the cloud connector.</p>
            description: <p>The new description to assign to the cloud connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            UpdateCloudConnector happy path for TP Link to update display name

            >>> await client.update_cloud_connector(identifier='123456789012', name='Connector for TP Link Cloud V2')
            UpdateCloudConnector error Id for Ring connector which does not exist

            >>> await client.update_cloud_connector(identifier='123456789012', name='Connector for Ring Cloud')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_cloud_connector.async_update_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_cloud_connector_request.UpdateCloudConnectorRequest = {
            "identifier": identifier
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cloud_connector(
        self,
        identifier: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a cloud connector.</p>

        Args:
            identifier: <p>The identifier of the cloud connector.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_cloud_connector_request.DeleteCloudConnectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_cloud_connector

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_cloud_connector.async_delete_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_cloud_connector_request.DeleteCloudConnectorRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_cloud_connectors(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        type: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
        ] = None,
        lambda_arn: Optional[
            "capo_iot_managed_integrations.types.lambda_arn.LambdaArn"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_cloud_connectors_response.ListCloudConnectorsResponse":
        """<p>Returns a list of connectors filtered by its Lambda Amazon Resource Name (ARN) and <code>type</code>.</p>

        Args:
            type: <p>The type of cloud connectors to filter by when listing available connectors.</p>
            lambda_arn: <p>The Amazon Resource Name (ARN) of the Lambda function to filter cloud connectors by.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListCloudConnectors happy path to get a list of connector resources

            >>> await client.list_cloud_connectors(max_results=5)
            ListCloudConnectors error path for unauthorized user

            >>> await client.list_cloud_connectors(max_results=5)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_cloud_connectors_request.ListCloudConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_cloud_connectors_response.ListCloudConnectorsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_cloud_connectors

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_cloud_connectors.async_list_cloud_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_cloud_connectors_request.ListCloudConnectorsRequest = {}
        if type is not None:
            input_["type"] = type
        if lambda_arn is not None:
            input_["lambda_arn"] = lambda_arn
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

    async def iter_list_cloud_connectors(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        type: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
        ] = None,
        lambda_arn: Optional[
            "capo_iot_managed_integrations.types.lambda_arn.LambdaArn"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.connector_item.ConnectorItem]":
        _token = next_token
        while True:
            _response = await self.list_cloud_connectors(
                config_overrides=config_overrides,
                type=type,
                lambda_arn=lambda_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_connector_destination(
        self,
        cloud_connector_id: "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId",
        auth_config: "capo_iot_managed_integrations.types.auth_config.AuthConfig",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
        ] = None,
        auth_type: Optional[
            "capo_iot_managed_integrations.types.auth_type.AuthType"
        ] = None,
        secrets_manager: Optional[
            "capo_iot_managed_integrations.types.secrets_manager.SecretsManager"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_connector_destination_response.CreateConnectorDestinationResponse":
        """<p>Create a connector destination for connecting a cloud-to-cloud (C2C) connector to the customer's Amazon Web Services account.</p>

        Args:
            name: <p>The display name of the connector destination.</p>
            description: <p>A description of the connector destination.</p>
            cloud_connector_id: <p>The identifier of the C2C connector.</p>
            auth_type: <p>The authentication type used for the connector destination, which determines how credentials and access are managed.</p>
            auth_config: <p>The authentication configuration details for the connector destination, including OAuth settings and other authentication parameters.</p>
            secrets_manager: <p>The AWS Secrets Manager configuration used to securely store and manage sensitive information for the connector destination.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_connector_destination_request.CreateConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_connector_destination_response.CreateConnectorDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_connector_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_connector_destination.async_create_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_connector_destination_request.CreateConnectorDestinationRequest = {
            "cloud_connector_id": cloud_connector_id,
            "auth_config": auth_config,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if secrets_manager is not None:
            input_["secrets_manager"] = secrets_manager
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

    async def get_connector_destination(
        self,
        identifier: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_connector_destination_response.GetConnectorDestinationResponse":
        """<p>Get connector destination details linked to a cloud-to-cloud (C2C) connector.</p>

        Args:
            identifier: <p>The identifier of the C2C connector destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_connector_destination_request.GetConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_connector_destination_response.GetConnectorDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_connector_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_connector_destination.async_get_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_connector_destination_request.GetConnectorDestinationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connector_destination(
        self,
        identifier: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.connector_destination_description.ConnectorDestinationDescription"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.connector_destination_name.ConnectorDestinationName"
        ] = None,
        auth_type: Optional[
            "capo_iot_managed_integrations.types.auth_type.AuthType"
        ] = None,
        auth_config: Optional[
            "capo_iot_managed_integrations.types.auth_config_update.AuthConfigUpdate"
        ] = None,
        secrets_manager: Optional[
            "capo_iot_managed_integrations.types.secrets_manager.SecretsManager"
        ] = None,
    ) -> None:
        """<p>Updates the properties of an existing connector destination.</p>

        Args:
            identifier: <p>The unique identifier of the connector destination to update.</p>
            description: <p>The new description to assign to the connector destination.</p>
            name: <p>The new display name to assign to the connector destination.</p>
            auth_type: <p>The new authentication type to use for the connector destination.</p>
            auth_config: <p>The updated authentication configuration details for the connector destination.</p>
            secrets_manager: <p>The updated AWS Secrets Manager configuration for the connector destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_connector_destination_request.UpdateConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_connector_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_connector_destination.async_update_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_connector_destination_request.UpdateConnectorDestinationRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if auth_type is not None:
            input_["auth_type"] = auth_type
        if auth_config is not None:
            input_["auth_config"] = auth_config
        if secrets_manager is not None:
            input_["secrets_manager"] = secrets_manager

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connector_destination(
        self,
        identifier: "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a connector destination linked to a cloud-to-cloud (C2C) connector.</p> <note> <p>Deletion can't be done if the account association has used this connector destination.</p> </note>

        Args:
            identifier: <p>The identifier of the connector destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_connector_destination_request.DeleteConnectorDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_connector_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_connector_destination.async_delete_connector_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_connector_destination_request.DeleteConnectorDestinationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_connector_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        cloud_connector_id: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_connector_destinations_response.ListConnectorDestinationsResponse":
        """<p>Lists all connector destinations, with optional filtering by cloud connector ID.</p>

        Args:
            cloud_connector_id: <p>The identifier of the cloud connector to filter connector destinations by.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of connector destinations to return in a single response.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_connector_destinations_request.ListConnectorDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_connector_destinations_response.ListConnectorDestinationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_connector_destinations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_connector_destinations.async_list_connector_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_connector_destinations_request.ListConnectorDestinationsRequest = {}
        if cloud_connector_id is not None:
            input_["cloud_connector_id"] = cloud_connector_id
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

    async def iter_list_connector_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        cloud_connector_id: Optional[
            "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.connector_destination_summary.ConnectorDestinationSummary]":
        _token = next_token
        while True:
            _response = await self.list_connector_destinations(
                config_overrides=config_overrides,
                cloud_connector_id=cloud_connector_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("connector_destination_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_credential_locker(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.credential_locker_name.CredentialLockerName"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse":
        """<p>Create a credential locker.</p> <note> <p>This operation will not trigger the creation of all the manufacturing resources.</p> </note>

        Args:
            name: <p>The name of the credential locker.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_credential_locker_response.CreateCredentialLockerResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_credential_locker.async_create_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_credential_locker_request.CreateCredentialLockerRequest = {}
        if name is not None:
            input_["name"] = name
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

    async def get_credential_locker(
        self,
        identifier: "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse":
        """<p>Get information on an existing credential locker</p>

        Args:
            identifier: <p>The identifier of the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_credential_locker_response.GetCredentialLockerResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_credential_locker.async_get_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_credential_locker_request.GetCredentialLockerRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_credential_locker(
        self,
        identifier: "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a credential locker. </p> <note> <p>This operation can't be undone and any existing device won't be able to use IoT managed integrations.</p> </note>

        Args:
            identifier: <p>The identifier of the credential locker.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_credential_locker.async_delete_credential_locker(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_credential_locker_request.DeleteCredentialLockerRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_credential_lockers(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse":
        """<p>List information on an existing credential locker.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_credential_lockers_response.ListCredentialLockersResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_credential_lockers.async_list_credential_lockers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_credential_lockers_request.ListCredentialLockersRequest = {}
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

    async def iter_list_credential_lockers(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.credential_locker_summary.CredentialLockerSummary]":
        _token = next_token
        while True:
            _response = await self.list_credential_lockers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_destination(
        self,
        delivery_destination_arn: "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn",
        delivery_destination_type: "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType",
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        role_arn: "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse":
        """<p> Create a notification destination such as Kinesis Data Streams that receive events and notifications from Managed integrations. Managed integrations uses the destination to determine where to deliver notifications.</p>

        Args:
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            name: <p>The name of the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            description: <p>The description of the customer-managed destination.</p>
            tags: <p>A set of key/value pairs that are used to manage the destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_destination_response.CreateDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_destination.async_create_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_destination_request.CreateDestinationRequest = {
            "delivery_destination_arn": delivery_destination_arn,
            "delivery_destination_type": delivery_destination_type,
            "name": name,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification destination specified by name. </p>

        Args:
            name: <p>The id of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_destination.async_delete_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_destination_request.DeleteDestinationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse":
        """<p>Gets a destination by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_destination_request.GetDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_destination_response.GetDestinationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_destination.async_get_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_destination_request.GetDestinationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse":
        """<p> List all notification destinations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_destinations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_destinations.async_list_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_destinations_request.ListDestinationsRequest = {}
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

    async def iter_list_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.destination_summary.DestinationSummary]":
        _token = next_token
        while True:
            _response = await self.list_destinations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("destination_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_destination(
        self,
        name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        delivery_destination_arn: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_arn.DeliveryDestinationArn"
        ] = None,
        delivery_destination_type: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_type.DeliveryDestinationType"
        ] = None,
        role_arn: Optional[
            "capo_iot_managed_integrations.types.delivery_destination_role_arn.DeliveryDestinationRoleArn"
        ] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.destination_description.DestinationDescription"
        ] = None,
    ) -> None:
        """<p> Update a destination specified by name. </p>

        Args:
            name: <p>The name of the customer-managed destination.</p>
            delivery_destination_arn: <p>The Amazon Resource Name (ARN) of the customer-managed destination.</p>
            delivery_destination_type: <p>The destination type for the customer-managed destination.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the delivery destination role.</p>
            description: <p>The description of the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_destination

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_destination.async_update_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_destination_request.UpdateDestinationRequest = {
            "name": name
        }
        if delivery_destination_arn is not None:
            input_["delivery_destination_arn"] = delivery_destination_arn
        if delivery_destination_type is not None:
            input_["delivery_destination_type"] = delivery_destination_type
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_device_discovery(
        self,
        discovery_type: "capo_iot_managed_integrations.types.discovery_type.DiscoveryType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        custom_protocol_detail: Optional[
            "capo_iot_managed_integrations.types.custom_protocol_detail.CustomProtocolDetail"
        ] = None,
        controller_identifier: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        connector_association_identifier: Optional[
            "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        authentication_material: Optional[
            "capo_iot_managed_integrations.types.discovery_auth_material_string.DiscoveryAuthMaterialString"
        ] = None,
        authentication_material_type: Optional[
            "capo_iot_managed_integrations.types.discovery_auth_material_type.DiscoveryAuthMaterialType"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        connector_device_id_list: Optional[
            "capo_iot_managed_integrations.types.connector_device_id_list.ConnectorDeviceIdList"
        ] = None,
        protocol: Optional[
            "capo_iot_managed_integrations.types.protocol_type.ProtocolType"
        ] = None,
        end_device_identifier: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse":
        """<p> This API is used to start device discovery for hub-connected and third-party-connected devices. The authentication material (install code) is delivered as a message to the controller instructing it to start the discovery.</p>

        Args:
            discovery_type: <p>The discovery type supporting the type of device to be discovered in the device discovery task request.</p>
            custom_protocol_detail: <p>Additional protocol-specific details required for device discovery, which vary based on the discovery type.</p> <note> <p>For a <code>DiscoveryType</code> of <code>CUSTOM</code>, the string-to-string map must have a key value of <code>Name</code> set to a non-empty-string.</p> </note>
            controller_identifier: <p>The id of the end-user's IoT hub.</p>
            connector_association_identifier: <p>The id of the connector association.</p>
            account_association_id: <p>The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.</p>
            authentication_material: <p>The authentication material required to start the local device discovery job request.</p>
            authentication_material_type: <p>The type of authentication material used for device discovery jobs.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the device discovery request.</p>
            connector_device_id_list: <p>Used as a filter for PLA discoveries.</p>
            protocol: <p>The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>
            end_device_identifier: <p>The unique id of the end device for capability rediscovery.</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.start_device_discovery_response.StartDeviceDiscoveryResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.start_device_discovery.async_start_device_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.start_device_discovery_request.StartDeviceDiscoveryRequest = {
            "discovery_type": discovery_type
        }
        if custom_protocol_detail is not None:
            input_["custom_protocol_detail"] = custom_protocol_detail
        if controller_identifier is not None:
            input_["controller_identifier"] = controller_identifier
        if connector_association_identifier is not None:
            input_["connector_association_identifier"] = (
                connector_association_identifier
            )
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
        if authentication_material is not None:
            input_["authentication_material"] = authentication_material
        if authentication_material_type is not None:
            input_["authentication_material_type"] = authentication_material_type
        if client_token is not None:
            input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if connector_device_id_list is not None:
            input_["connector_device_id_list"] = connector_device_id_list
        if protocol is not None:
            input_["protocol"] = protocol
        if end_device_identifier is not None:
            input_["end_device_identifier"] = end_device_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_device_discovery(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse":
        """<p> Get the current state of a device discovery.</p>

        Args:
            identifier: <p>The id of the device discovery job request.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_device_discovery_response.GetDeviceDiscoveryResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_device_discovery.async_get_device_discovery(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_device_discovery_request.GetDeviceDiscoveryRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_device_discoveries(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        type_filter: Optional[
            "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
        ] = None,
        status_filter: Optional[
            "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse":
        """<p>Lists all device discovery tasks, with optional filtering by type and status.</p>

        Args:
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of device discovery jobs to return in a single response.</p>
            type_filter: <p>The discovery type to filter device discovery jobs by.</p>
            status_filter: <p>The status to filter device discovery jobs by.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_device_discoveries_response.ListDeviceDiscoveriesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_device_discoveries.async_list_device_discoveries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_device_discoveries_request.ListDeviceDiscoveriesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_device_discoveries(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        type_filter: Optional[
            "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
        ] = None,
        status_filter: Optional[
            "capo_iot_managed_integrations.types.device_discovery_status.DeviceDiscoveryStatus"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.device_discovery_summary.DeviceDiscoverySummary]":
        _token = next_token
        while True:
            _response = await self.list_device_discoveries(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                type_filter=type_filter,
                status_filter=status_filter,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_discovered_devices(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse":
        """<p>Lists all devices discovered during a specific device discovery task.</p>

        Args:
            identifier: <p>The identifier of the device discovery job to list discovered devices for.</p>
            next_token: <p>A token used for pagination of results.</p>
            max_results: <p>The maximum number of discovered devices to return in a single response.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_discovered_devices_response.ListDiscoveredDevicesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_discovered_devices.async_list_discovered_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_discovered_devices_request.ListDiscoveredDevicesRequest = {
            "identifier": identifier
        }
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

    async def iter_list_discovered_devices(
        self,
        identifier: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.discovered_device_summary.DiscoveredDeviceSummary]":
        _token = next_token
        while True:
            _response = await self.list_discovered_devices(
                identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_event_log_configuration(
        self,
        resource_type: "capo_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType",
        event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        resource_id: Optional[
            "capo_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse":
        """<p>Set the event log configuration for the account, resource type, or specific resource.</p>

        Args:
            resource_type: <p>The type of resource for the event log configuration.</p>
            resource_id: <p>The identifier of the resource for the event log configuration.</p>
            event_log_level: <p>The logging level for the event log configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The service quota has been exceeded for this request.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_event_log_configuration_response.CreateEventLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_event_log_configuration.async_create_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_event_log_configuration_request.CreateEventLogConfigurationRequest = {
            "resource_type": resource_type,
            "event_log_level": event_log_level,
        }
        if resource_id is not None:
            input_["resource_id"] = resource_id
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

    async def delete_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_event_log_configuration.async_delete_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_event_log_configuration_request.DeleteEventLogConfigurationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse":
        """<p>Get an event log configuration.</p>

        Args:
            id: <p>The identifier of the event log configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_event_log_configuration_response.GetEventLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_event_log_configuration.async_get_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_event_log_configuration_request.GetEventLogConfigurationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_event_log_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse":
        """<p>List all event log configurations for an account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_event_log_configurations_response.ListEventLogConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_event_log_configurations.async_list_event_log_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_event_log_configurations_request.ListEventLogConfigurationsRequest = {}
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

    async def iter_list_event_log_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.event_log_configuration_summary.EventLogConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_event_log_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("event_log_configuration_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_event_log_configuration(
        self,
        id: "capo_iot_managed_integrations.types.log_configuration_id.LogConfigurationId",
        event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Update an event log configuration by log configuration ID.</p>

        Args:
            id: <p>The log configuration id.</p>
            event_log_level: <p>The log level for the event in terms of severity.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_event_log_configuration.async_update_event_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_event_log_configuration_request.UpdateEventLogConfigurationRequest = {
            "id": id,
            "event_log_level": event_log_level,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_hub_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_hub_configuration_response.GetHubConfigurationResponse":
        """<p>Get a hub configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_hub_configuration_request.GetHubConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_hub_configuration_response.GetHubConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_hub_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_hub_configuration.async_get_hub_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_hub_configuration_request.GetHubConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_hub_configuration(
        self,
        hub_token_timer_expiry_setting_in_seconds: "capo_iot_managed_integrations.types.hub_token_timer_expiry_setting_in_seconds.HubTokenTimerExpirySettingInSeconds",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.put_hub_configuration_response.PutHubConfigurationResponse":
        """<p>Update a hub configuration.</p>

        Args:
            hub_token_timer_expiry_setting_in_seconds: <p>A user-defined integer value that represents the hub token timer expiry setting in seconds.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.put_hub_configuration_request.PutHubConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.put_hub_configuration_response.PutHubConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_hub_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.put_hub_configuration.async_put_hub_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.put_hub_configuration_request.PutHubConfigurationRequest = {
            "hub_token_timer_expiry_setting_in_seconds": hub_token_timer_expiry_setting_in_seconds
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_default_encryption_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse":
        r"""<p> Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified region. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the <i>AWS IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_default_encryption_configuration_response.GetDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_default_encryption_configuration.async_get_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_default_encryption_configuration_request.GetDefaultEncryptionConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_default_encryption_configuration(
        self,
        encryption_type: "capo_iot_managed_integrations.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        kms_key_arn: Optional[
            "capo_iot_managed_integrations.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        r"""<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\">Key management</a> in the AWS IoT SiteWise User Guide.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_arn: <p>The Key Amazon Resource Name (ARN) of the AWS KMS key used for KMS encryption if you use <code>KMS_BASED_ENCRYPTION</code>.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.put_default_encryption_configuration.async_put_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {
            "encryption_type": encryption_type
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_account_association(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deregister an account association from a managed thing.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to be deregistered from the account association.</p>
            account_association_id: <p>The unique identifier of the account association to be deregistered.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.deregister_account_association_request.DeregisterAccountAssociationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.deregister_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.deregister_account_association.async_deregister_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.deregister_account_association_request.DeregisterAccountAssociationRequest = {
            "managed_thing_id": managed_thing_id,
            "account_association_id": account_association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_thing_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        managed_thing_id: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_thing_account_associations_response.ListManagedThingAccountAssociationsResponse":
        """<p>Lists all account associations for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to list account associations for.</p>
            account_association_id: <p>The identifier of the account association to filter results by. When specified, only associations with this account association ID will be returned.</p>
            max_results: <p>The maximum number of account associations to return in a single response.</p>
            next_token: <p>A token used for pagination of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_managed_thing_account_associations_request.ListManagedThingAccountAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_managed_thing_account_associations_response.ListManagedThingAccountAssociationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_account_associations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_account_associations.async_list_managed_thing_account_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_thing_account_associations_request.ListManagedThingAccountAssociationsRequest = {}
        if managed_thing_id is not None:
            input_["managed_thing_id"] = managed_thing_id
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id
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

    async def iter_list_managed_thing_account_associations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        managed_thing_id: Optional[
            "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.managed_thing_association.ManagedThingAssociation]":
        _token = next_token
        while True:
            _response = await self.list_managed_thing_account_associations(
                config_overrides=config_overrides,
                managed_thing_id=managed_thing_id,
                account_association_id=account_association_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def register_account_association(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        account_association_id: "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId",
        device_discovery_id: "capo_iot_managed_integrations.types.device_discovery_id.DeviceDiscoveryId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.register_account_association_response.RegisterAccountAssociationResponse":
        """<p>Registers an account association with a managed thing, establishing a connection between a device and a third-party account.</p>

        Args:
            managed_thing_id: <p>The identifier of the managed thing to register with the account association.</p>
            account_association_id: <p>The identifier of the account association to register with the managed thing.</p>
            device_discovery_id: <p>The identifier of the device discovery job associated with this registration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.register_account_association_request.RegisterAccountAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.register_account_association_response.RegisterAccountAssociationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.register_account_association

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.register_account_association.async_register_account_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.register_account_association_request.RegisterAccountAssociationRequest = {
            "managed_thing_id": managed_thing_id,
            "account_association_id": account_association_id,
            "device_discovery_id": device_discovery_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_managed_thing_command(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        endpoints: "capo_iot_managed_integrations.types.command_endpoints.CommandEndpoints",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        connector_association_id: Optional[
            "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
        ] = None,
        account_association_id: Optional[
            "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.send_managed_thing_command_response.SendManagedThingCommandResponse":
        """<p>Send the command to the device represented by the managed thing. </p>

        Args:
            managed_thing_id: <p>The id of the device.</p>
            endpoints: <p>The device endpoint.</p>
            connector_association_id: <p>The ID tracking the current discovery process for one connector association.</p>
            account_association_id: <p>The identifier of the account association to use when sending a command to a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.send_managed_thing_command_request.SendManagedThingCommandRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.send_managed_thing_command_response.SendManagedThingCommandResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.send_managed_thing_command

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.send_managed_thing_command.async_send_managed_thing_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.send_managed_thing_command_request.SendManagedThingCommandRequest = {
            "managed_thing_id": managed_thing_id,
            "endpoints": endpoints,
        }
        if connector_association_id is not None:
            input_["connector_association_id"] = connector_association_id
        if account_association_id is not None:
            input_["account_association_id"] = account_association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_managed_thing(
        self,
        role: "capo_iot_managed_integrations.types.role.Role",
        authentication_material: "capo_iot_managed_integrations.types.auth_material_string.AuthMaterialString",
        authentication_material_type: "capo_iot_managed_integrations.types.auth_material_type.AuthMaterialType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        owner: Optional["capo_iot_managed_integrations.types.owner.Owner"] = None,
        credential_locker_id: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        wi_fi_simple_setup_configuration: Optional[
            "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
        ] = None,
        serial_number: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        brand: Optional["capo_iot_managed_integrations.types.brand.Brand"] = None,
        model: Optional["capo_iot_managed_integrations.types.model.Model"] = None,
        name: Optional["capo_iot_managed_integrations.types.name.Name"] = None,
        capability_report: Optional[
            "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
        ] = None,
        capability_schemas: Optional[
            "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
        ] = None,
        capabilities: Optional[
            "capo_iot_managed_integrations.types.capabilities.Capabilities"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        classification: Optional[
            "capo_iot_managed_integrations.types.classification.Classification"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
        meta_data: Optional[
            "capo_iot_managed_integrations.types.meta_data.MetaData"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_managed_thing_response.CreateManagedThingResponse":
        """<p>Creates a managed thing. A managed thing contains the device identifier, protocol supported, and capabilities of the device in a data model format defined by Managed integrations.</p>

        Args:
            role: <p>The type of device used. This will be the hub controller, cloud device, or AWS IoT device.</p>
            owner: <p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>
            credential_locker_id: <p>The identifier of the credential for the managed thing.</p>
            authentication_material: <p>The authentication material defining the device connectivity setup requests. The authorization materials used are the device bar code.</p>
            authentication_material_type: <p>The type of authentication material used for device connectivity setup requests.</p>
            wi_fi_simple_setup_configuration: <p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>
            serial_number: <p>The serial number of the device.</p>
            brand: <p>The brand of the device.</p>
            model: <p>The model of the device.</p>
            name: <p>The name of the managed thing representing the physical device.</p>
            capability_report: <p>A report of the capabilities for the managed thing.</p>
            capability_schemas: <p>The capability schemas that define the functionality and features supported by the managed thing, including device capabilities and their associated properties.</p>
            capabilities: <p>The capabilities of the device such as light bulb.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            classification: <p>The classification of the managed thing such as light bulb or thermostat.</p>
            tags: <p>A set of key/value pairs that are used to manage the managed thing.</p>
            meta_data: <p>The metadata for the managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_managed_thing_request.CreateManagedThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_managed_thing_response.CreateManagedThingResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_managed_thing.async_create_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_managed_thing_request.CreateManagedThingRequest = {
            "role": role,
            "authentication_material": authentication_material,
            "authentication_material_type": authentication_material_type,
        }
        if owner is not None:
            input_["owner"] = owner
        if credential_locker_id is not None:
            input_["credential_locker_id"] = credential_locker_id
        if wi_fi_simple_setup_configuration is not None:
            input_["wi_fi_simple_setup_configuration"] = (
                wi_fi_simple_setup_configuration
            )
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if brand is not None:
            input_["brand"] = brand
        if model is not None:
            input_["model"] = model
        if name is not None:
            input_["name"] = name
        if capability_report is not None:
            input_["capability_report"] = capability_report
        if capability_schemas is not None:
            input_["capability_schemas"] = capability_schemas
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if classification is not None:
            input_["classification"] = classification
        if tags is not None:
            input_["tags"] = tags
        if meta_data is not None:
            input_["meta_data"] = meta_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_response.GetManagedThingResponse":
        """<p> Get details of a managed thing including its attributes and capabilities.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_request.GetManagedThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_response.GetManagedThingResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing.async_get_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_request.GetManagedThingRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_managed_thing(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        owner: Optional["capo_iot_managed_integrations.types.owner.Owner"] = None,
        credential_locker_id: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        serial_number: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        wi_fi_simple_setup_configuration: Optional[
            "capo_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
        ] = None,
        brand: Optional["capo_iot_managed_integrations.types.brand.Brand"] = None,
        model: Optional["capo_iot_managed_integrations.types.model.Model"] = None,
        name: Optional["capo_iot_managed_integrations.types.name.Name"] = None,
        capability_report: Optional[
            "capo_iot_managed_integrations.types.capability_report.CapabilityReport"
        ] = None,
        capability_schemas: Optional[
            "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
        ] = None,
        capabilities: Optional[
            "capo_iot_managed_integrations.types.capabilities.Capabilities"
        ] = None,
        classification: Optional[
            "capo_iot_managed_integrations.types.classification.Classification"
        ] = None,
        hub_network_mode: Optional[
            "capo_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
        ] = None,
        meta_data: Optional[
            "capo_iot_managed_integrations.types.meta_data.MetaData"
        ] = None,
    ) -> None:
        """<p>Update the attributes and capabilities associated with a managed thing.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>
            owner: <p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>
            credential_locker_id: <p>The identifier of the credential for the managed thing.</p>
            serial_number: <p>The serial number of the device.</p>
            wi_fi_simple_setup_configuration: <p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>
            brand: <p>The brand of the device.</p>
            model: <p>The model of the device.</p>
            name: <p>The name of the managed thing representing the physical device.</p>
            capability_report: <p>A report of the capabilities for the managed thing.</p>
            capability_schemas: <p>The updated capability schemas that define the functionality and features supported by the managed thing.</p>
            capabilities: <p>The capabilities of the device such as light bulb.</p>
            classification: <p>The classification of the managed thing such as light bulb or thermostat.</p>
            hub_network_mode: <p>The network mode for the hub-connected device.</p>
            meta_data: <p>The metadata for the managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_managed_thing_request.UpdateManagedThingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_managed_thing.async_update_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_managed_thing_request.UpdateManagedThingRequest = {
            "identifier": identifier
        }
        if owner is not None:
            input_["owner"] = owner
        if credential_locker_id is not None:
            input_["credential_locker_id"] = credential_locker_id
        if serial_number is not None:
            input_["serial_number"] = serial_number
        if wi_fi_simple_setup_configuration is not None:
            input_["wi_fi_simple_setup_configuration"] = (
                wi_fi_simple_setup_configuration
            )
        if brand is not None:
            input_["brand"] = brand
        if model is not None:
            input_["model"] = model
        if name is not None:
            input_["name"] = name
        if capability_report is not None:
            input_["capability_report"] = capability_report
        if capability_schemas is not None:
            input_["capability_schemas"] = capability_schemas
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if classification is not None:
            input_["classification"] = classification
        if hub_network_mode is not None:
            input_["hub_network_mode"] = hub_network_mode
        if meta_data is not None:
            input_["meta_data"] = meta_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_managed_thing(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        force: Optional[bool] = None,
    ) -> None:
        """<p>Delete a managed thing. For direct-connected and hub-connected devices connecting with Managed integrations via a controller, all of the devices connected to it will have their status changed to <code>PENDING</code>. It is not possible to remove a cloud-to-cloud device.</p>

        Args:
            identifier: <p>The id of the managed thing.</p>
            force: <p>When set to <code>TRUE</code>, a forceful deteletion of the managed thing will occur. When set to <code>FALSE</code>, a non-forceful deletion of the managed thing will occur.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_managed_thing_request.DeleteManagedThingRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_managed_thing

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_managed_thing.async_delete_managed_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_managed_thing_request.DeleteManagedThingRequest = {
            "identifier": identifier
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_things(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        owner_filter: Optional[
            "capo_iot_managed_integrations.types.owner.Owner"
        ] = None,
        credential_locker_filter: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        role_filter: Optional["capo_iot_managed_integrations.types.role.Role"] = None,
        parent_controller_identifier_filter: Optional[
            "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
        ] = None,
        connector_policy_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
        ] = None,
        connector_destination_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        connector_device_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
        ] = None,
        serial_number_filter: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        provisioning_status_filter: Optional[
            "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse":
        r"""<p>Listing all managed things with provision for filters.</p>

        Args:
            owner_filter: <p>Filter on device owners when listing managed things.</p>
            credential_locker_filter: <p>Filter on a credential locker for a managed thing.</p>
            role_filter: <p>Filter on the type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>
            parent_controller_identifier_filter: <p>Filter on a parent controller id for a managed thing.</p>
            connector_policy_id_filter: <p>Filter on a connector policy id for a managed thing.</p>
            connector_destination_id_filter: <p>Filter managed things by the connector destination ID they are associated with.</p>
            connector_device_id_filter: <p>Filter managed things by the connector device ID they are associated with. When specified, only managed things with this connector device ID will be returned.</p>
            serial_number_filter: <p>Filter on the serial number of the device.</p>
            provisioning_status_filter: <p>Filter on the status of the device. For more information, see <a href=\"https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html\">Device Provisioning</a>.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_managed_things_response.ListManagedThingsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_things

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_things.async_list_managed_things(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_things_request.ListManagedThingsRequest = {}
        if owner_filter is not None:
            input_["owner_filter"] = owner_filter
        if credential_locker_filter is not None:
            input_["credential_locker_filter"] = credential_locker_filter
        if role_filter is not None:
            input_["role_filter"] = role_filter
        if parent_controller_identifier_filter is not None:
            input_["parent_controller_identifier_filter"] = (
                parent_controller_identifier_filter
            )
        if connector_policy_id_filter is not None:
            input_["connector_policy_id_filter"] = connector_policy_id_filter
        if connector_destination_id_filter is not None:
            input_["connector_destination_id_filter"] = connector_destination_id_filter
        if connector_device_id_filter is not None:
            input_["connector_device_id_filter"] = connector_device_id_filter
        if serial_number_filter is not None:
            input_["serial_number_filter"] = serial_number_filter
        if provisioning_status_filter is not None:
            input_["provisioning_status_filter"] = provisioning_status_filter
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

    async def iter_list_managed_things(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        owner_filter: Optional[
            "capo_iot_managed_integrations.types.owner.Owner"
        ] = None,
        credential_locker_filter: Optional[
            "capo_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
        ] = None,
        role_filter: Optional["capo_iot_managed_integrations.types.role.Role"] = None,
        parent_controller_identifier_filter: Optional[
            "capo_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
        ] = None,
        connector_policy_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
        ] = None,
        connector_destination_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
        ] = None,
        connector_device_id_filter: Optional[
            "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
        ] = None,
        serial_number_filter: Optional[
            "capo_iot_managed_integrations.types.serial_number.SerialNumber"
        ] = None,
        provisioning_status_filter: Optional[
            "capo_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.managed_thing_summary.ManagedThingSummary]":
        _token = next_token
        while True:
            _response = await self.list_managed_things(
                config_overrides=config_overrides,
                owner_filter=owner_filter,
                credential_locker_filter=credential_locker_filter,
                role_filter=role_filter,
                parent_controller_identifier_filter=parent_controller_identifier_filter,
                connector_policy_id_filter=connector_policy_id_filter,
                connector_destination_id_filter=connector_destination_id_filter,
                connector_device_id_filter=connector_device_id_filter,
                serial_number_filter=serial_number_filter,
                provisioning_status_filter=provisioning_status_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_managed_thing_capabilities(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_capabilities_response.GetManagedThingCapabilitiesResponse":
        """<p>Get the capabilities for a managed thing using the device ID.</p>

        Args:
            identifier: <p>The id of the device.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_capabilities_request.GetManagedThingCapabilitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_capabilities_response.GetManagedThingCapabilitiesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_capabilities

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_capabilities.async_get_managed_thing_capabilities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_capabilities_request.GetManagedThingCapabilitiesRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing_certificate(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_certificate_response.GetManagedThingCertificateResponse":
        """<p>Retrieves the certificate PEM for a managed IoT thing.</p>

        Args:
            identifier: <p>The identifier of the managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get managed thing certificate

            >>> await client.get_managed_thing_certificate(identifier='example-managed-thing-id')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_certificate_request.GetManagedThingCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_certificate_response.GetManagedThingCertificateResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_certificate

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_certificate.async_get_managed_thing_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_certificate_request.GetManagedThingCertificateRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing_connectivity_data(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response.GetManagedThingConnectivityDataResponse":
        """<p>Get the connectivity status of a managed thing.</p>

        Args:
            identifier: <p>The identifier of a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request.GetManagedThingConnectivityDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_response.GetManagedThingConnectivityDataResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_connectivity_data

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_connectivity_data.async_get_managed_thing_connectivity_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_connectivity_data_request.GetManagedThingConnectivityDataRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_managed_thing_meta_data(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_meta_data_response.GetManagedThingMetaDataResponse":
        """<p>Get the metadata information for a managed thing.</p> <note> <p>The <code>managedThing</code> <code>metadata</code> parameter is used for associating attributes with a <code>managedThing</code> that can be used for grouping over-the-air (OTA) tasks. Name value pairs in <code>metadata</code> can be used in the <code>OtaTargetQueryString</code> parameter for the <code>CreateOtaTask</code> API operation.</p> </note>

        Args:
            identifier: <p>The managed thing id.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_meta_data_request.GetManagedThingMetaDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_meta_data_response.GetManagedThingMetaDataResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_meta_data

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_meta_data.async_get_managed_thing_meta_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_meta_data_request.GetManagedThingMetaDataRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_managed_thing_schemas(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        endpoint_id_filter: Optional[
            "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
        ] = None,
        capability_id_filter: Optional[
            "capo_iot_managed_integrations.types.capability_id.CapabilityId"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_managed_thing_schemas_response.ListManagedThingSchemasResponse":
        """<p>List schemas associated with a managed thing.</p>

        Args:
            identifier: <p>The managed thing id.</p>
            endpoint_id_filter: <p>Filter on an endpoint id.</p>
            capability_id_filter: <p>Filter on a capability id.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_managed_thing_schemas_request.ListManagedThingSchemasRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_managed_thing_schemas_response.ListManagedThingSchemasResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_schemas

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_managed_thing_schemas.async_list_managed_thing_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_managed_thing_schemas_request.ListManagedThingSchemasRequest = {
            "identifier": identifier
        }
        if endpoint_id_filter is not None:
            input_["endpoint_id_filter"] = endpoint_id_filter
        if capability_id_filter is not None:
            input_["capability_id_filter"] = capability_id_filter
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

    async def iter_list_managed_thing_schemas(
        self,
        identifier: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        endpoint_id_filter: Optional[
            "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
        ] = None,
        capability_id_filter: Optional[
            "capo_iot_managed_integrations.types.capability_id.CapabilityId"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.managed_thing_schema_list_item.ManagedThingSchemaListItem]":
        _token = next_token
        while True:
            _response = await self.list_managed_thing_schemas(
                identifier,
                config_overrides=config_overrides,
                endpoint_id_filter=endpoint_id_filter,
                capability_id_filter=capability_id_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_managed_thing_state(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse":
        """<p> Returns the managed thing state for the given device Id.</p>

        Args:
            managed_thing_id: <p>The id of the device.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_failure_exception.InternalFailureException: <p>An unexpected error has occurred.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_managed_thing_state_response.GetManagedThingStateResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_managed_thing_state.async_get_managed_thing_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_managed_thing_state_request.GetManagedThingStateRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        destination_name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse":
        """<p>Creates a notification configuration. A configuration is a connection between an event type and a destination that you have already created. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the notification configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_notification_configuration_response.CreateNotificationConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_notification_configuration.async_create_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_notification_configuration_request.CreateNotificationConfigurationRequest = {
            "event_type": event_type,
            "destination_name": destination_name,
        }
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

    async def delete_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Deletes a notification configuration. </p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_notification_configuration.async_delete_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_notification_configuration_request.DeleteNotificationConfigurationRequest = {
            "event_type": event_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p> Get a notification configuration for a specified event type.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_notification_configuration.async_get_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {
            "event_type": event_type
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_notification_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse":
        """<p> List all notification configurations.</p>

        Args:
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_notification_configurations_response.ListNotificationConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_notification_configurations.async_list_notification_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_notification_configurations_request.ListNotificationConfigurationsRequest = {}
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

    async def iter_list_notification_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.notification_configuration_summary.NotificationConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_notification_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("notification_configuration_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_notification_configuration(
        self,
        event_type: "capo_iot_managed_integrations.types.event_type.EventType",
        destination_name: "capo_iot_managed_integrations.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p> Update a notification configuration.</p>

        Args:
            event_type: <p>The type of event triggering a device notification to the customer-managed destination.</p>
            destination_name: <p>The name of the destination for the notification configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_notification_configuration.async_update_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_notification_configuration_request.UpdateNotificationConfigurationRequest = {
            "event_type": event_type,
            "destination_name": destination_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ota_task_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.ota_task_configuration_name.OtaTaskConfigurationName"
        ] = None,
        push_config: Optional[
            "capo_iot_managed_integrations.types.push_config.PushConfig"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse":
        """<p>Create a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            description: <p>A description of the over-the-air (OTA) task configuration.</p>
            name: <p>The name of the over-the-air (OTA) task.</p>
            push_config: <p>Describes the type of configuration used for the over-the-air (OTA) task.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_ota_task_configuration_response.CreateOtaTaskConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task_configuration.async_create_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_ota_task_configuration_request.CreateOtaTaskConfigurationRequest = {}
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if push_config is not None:
            input_["push_config"] = push_config
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

    async def delete_ota_task_configuration(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task configuration.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task_configuration.async_delete_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_ota_task_configuration_request.DeleteOtaTaskConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ota_task_configuration(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse":
        """<p>Get a configuraiton for the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task configuration id.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_ota_task_configuration_response.GetOtaTaskConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task_configuration.async_get_ota_task_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_ota_task_configuration_request.GetOtaTaskConfigurationRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ota_task_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse":
        """<p>List all of the over-the-air (OTA) task configurations.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_ota_task_configurations_response.ListOtaTaskConfigurationsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_configurations.async_list_ota_task_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_ota_task_configurations_request.ListOtaTaskConfigurationsRequest = {}
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

    async def iter_list_ota_task_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.ota_task_configuration_summary.OtaTaskConfigurationSummary]":
        _token = next_token
        while True:
            _response = await self.list_ota_task_configurations(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ota_task(
        self,
        s3_url: "capo_iot_managed_integrations.types.s3_url.S3Url",
        ota_type: "capo_iot_managed_integrations.types.ota_type.OtaType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        protocol: Optional[
            "capo_iot_managed_integrations.types.ota_protocol.OtaProtocol"
        ] = None,
        target: Optional["capo_iot_managed_integrations.types.target.Target"] = None,
        task_configuration_id: Optional[
            "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
        ] = None,
        ota_mechanism: Optional[
            "capo_iot_managed_integrations.types.ota_mechanism.OtaMechanism"
        ] = None,
        ota_target_query_string: Optional[
            "capo_iot_managed_integrations.types.ota_target_query_string.OtaTargetQueryString"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        ota_scheduling_config: Optional[
            "capo_iot_managed_integrations.types.ota_task_scheduling_config.OtaTaskSchedulingConfig"
        ] = None,
        ota_task_execution_retry_config: Optional[
            "capo_iot_managed_integrations.types.ota_task_execution_retry_config.OtaTaskExecutionRetryConfig"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_ota_task_response.CreateOtaTaskResponse":
        """<p>Create an over-the-air (OTA) task to target a device.</p>

        Args:
            description: <p>The description of the over-the-air (OTA) task.</p>
            s3_url: <p>The URL to the Amazon S3 bucket where the over-the-air (OTA) task is stored.</p>
            protocol: <p>The connection protocol the over-the-air (OTA) task uses to update the device.</p>
            target: <p>The device targeted for the over-the-air (OTA) task.</p>
            task_configuration_id: <p>The identifier for the over-the-air (OTA) task configuration.</p>
            ota_mechanism: <p>The deployment mechanism for the over-the-air (OTA) task.</p>
            ota_type: <p>The frequency type for the over-the-air (OTA) task.</p>
            ota_target_query_string: <p>The query string to add things to the thing group.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the over-the-air (OTA) task.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_ota_task_request.CreateOtaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_ota_task_response.CreateOtaTaskResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_ota_task.async_create_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_ota_task_request.CreateOtaTaskRequest = {
            "s3_url": s3_url,
            "ota_type": ota_type,
        }
        if description is not None:
            input_["description"] = description
        if protocol is not None:
            input_["protocol"] = protocol
        if target is not None:
            input_["target"] = target
        if task_configuration_id is not None:
            input_["task_configuration_id"] = task_configuration_id
        if ota_mechanism is not None:
            input_["ota_mechanism"] = ota_mechanism
        if ota_target_query_string is not None:
            input_["ota_target_query_string"] = ota_target_query_string
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ota_scheduling_config is not None:
            input_["ota_scheduling_config"] = ota_scheduling_config
        if ota_task_execution_retry_config is not None:
            input_["ota_task_execution_retry_config"] = ota_task_execution_retry_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ota_task(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_ota_task_response.GetOtaTaskResponse":
        """<p>Get details of the over-the-air (OTA) task by its task id.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_ota_task_request.GetOtaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_ota_task_response.GetOtaTaskResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_ota_task.async_get_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_ota_task_request.GetOtaTaskRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ota_task(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        description: Optional[
            "capo_iot_managed_integrations.types.ota_description.OtaDescription"
        ] = None,
        task_configuration_id: Optional[
            "capo_iot_managed_integrations.types.ota_task_configuration_id.OtaTaskConfigurationId"
        ] = None,
    ) -> None:
        """<p>Update an over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
            description: <p>The description of the over-the-air (OTA) task.</p>
            task_configuration_id: <p>The identifier for the over-the-air (OTA) task configuration.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.update_ota_task_request.UpdateOtaTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.update_ota_task

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.update_ota_task.async_update_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.update_ota_task_request.UpdateOtaTaskRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if task_configuration_id is not None:
            input_["task_configuration_id"] = task_configuration_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ota_task(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete the over-the-air (OTA) task.</p>

        Args:
            identifier: <p>The identifier of the over-the-air (OTA) task.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.limit_exceeded_exception.LimitExceededException: <p>The request exceeds a service limit or quota. Adjust your request parameters and try again.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_ota_task_request.DeleteOtaTaskRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_ota_task.async_delete_ota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_ota_task_request.DeleteOtaTaskRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ota_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_ota_tasks_response.ListOtaTasksResponse":
        """<p>List all of the over-the-air (OTA) tasks.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_ota_tasks_request.ListOtaTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_ota_tasks_response.ListOtaTasksResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_tasks

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_tasks.async_list_ota_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_ota_tasks_request.ListOtaTasksRequest = {}
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

    async def iter_list_ota_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.ota_task_summary.OtaTaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_ota_tasks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ota_task_executions(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_ota_task_executions_response.ListOtaTaskExecutionsResponse":
        """<p>List all of the over-the-air (OTA) task executions.</p>

        Args:
            identifier: <p>The over-the-air (OTA) task id.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_ota_task_executions_request.ListOtaTaskExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_ota_task_executions_response.ListOtaTaskExecutionsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_executions

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_ota_task_executions.async_list_ota_task_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_ota_task_executions_request.ListOtaTaskExecutionsRequest = {
            "identifier": identifier
        }
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

    async def iter_list_ota_task_executions(
        self,
        identifier: "capo_iot_managed_integrations.types.ota_task_id.OtaTaskId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.ota_next_token.OtaNextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.ota_task_execution_summaries.OtaTaskExecutionSummaries]":
        _token = next_token
        while True:
            _response = await self.list_ota_task_executions(
                identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("execution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_provisioning_profile(
        self,
        provisioning_type: "capo_iot_managed_integrations.types.provisioning_type.ProvisioningType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        ca_certificate: Optional[
            "capo_iot_managed_integrations.types.ca_certificate.CaCertificate"
        ] = None,
        claim_certificate: Optional[
            "capo_iot_managed_integrations.types.claim_certificate.ClaimCertificate"
        ] = None,
        name: Optional[
            "capo_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
        ] = None,
        client_token: Optional[
            "capo_iot_managed_integrations.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iot_managed_integrations.types.tags_map.TagsMap"] = None,
    ) -> "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse":
        """<p>Create a provisioning profile for executing device provisioning flows. The provisioning profile is a document that defines the set of resources and policies applied to a device during the provisioning process.</p>

        Args:
            provisioning_type: <p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>
            ca_certificate: <p>The body of the PEM-encoded certificate authority (CA) certificate.</p>
            claim_certificate: <p>The body of the PEM-encoded claim certificate. If a claim certificate is provided, it will be used for the provisioning profile. Otherwise, a claim certificate will be generated.</p>
            name: <p>The name of the provisioning profile.</p>
            client_token: <p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>
            tags: <p>A set of key/value pairs that are used to manage the provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.create_provisioning_profile_response.CreateProvisioningProfileResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.create_provisioning_profile.async_create_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.create_provisioning_profile_request.CreateProvisioningProfileRequest = {
            "provisioning_type": provisioning_type
        }
        if ca_certificate is not None:
            input_["ca_certificate"] = ca_certificate
        if claim_certificate is not None:
            input_["claim_certificate"] = claim_certificate
        if name is not None:
            input_["name"] = name
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

    async def get_provisioning_profile(
        self,
        identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse":
        """<p>Get details of a provisioning profile.</p>

        Args:
            identifier: <p>The id of a provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_provisioning_profile_response.GetProvisioningProfileResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_provisioning_profile.async_get_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_provisioning_profile_request.GetProvisioningProfileRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_provisioning_profile(
        self,
        identifier: "capo_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Delete a provisioning profile.</p>

        Args:
            identifier: <p>The id of the provisioning profile.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.delete_provisioning_profile.async_delete_provisioning_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.delete_provisioning_profile_request.DeleteProvisioningProfileRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_provisioning_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse":
        """<p>List the provisioning profiles within the Amazon Web Services account.</p>

        Args:
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized to perform this operation.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_provisioning_profiles_response.ListProvisioningProfilesResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_provisioning_profiles.async_list_provisioning_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_provisioning_profiles_request.ListProvisioningProfilesRequest = {}
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

    async def iter_list_provisioning_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.provisioning_profile_summary.ProvisioningProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_provisioning_profiles(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> "capo_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse":
        """<p>Get the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_runtime_log_configuration_response.GetRuntimeLogConfigurationResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_runtime_log_configuration.async_get_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_runtime_log_configuration_request.GetRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        runtime_log_configurations: "capo_iot_managed_integrations.types.runtime_log_configurations.RuntimeLogConfigurations",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Set the runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id for a managed thing.</p>
            runtime_log_configurations: <p>The runtime log configuration for a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.put_runtime_log_configuration.async_put_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.put_runtime_log_configuration_request.PutRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id,
            "runtime_log_configurations": runtime_log_configurations,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_runtime_log_configuration(
        self,
        managed_thing_id: "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
    ) -> None:
        """<p>Reset a runtime log configuration for a specific managed thing.</p>

        Args:
            managed_thing_id: <p>The id of a managed thing.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.reset_runtime_log_configuration.async_reset_runtime_log_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.reset_runtime_log_configuration_request.ResetRuntimeLogConfigurationRequest = {
            "managed_thing_id": managed_thing_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_schema_version(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        schema_versioned_id: "capo_iot_managed_integrations.types.schema_versioned_id.SchemaVersionedId",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        format: Optional[
            "capo_iot_managed_integrations.types.schema_version_format.SchemaVersionFormat"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.get_schema_version_response.GetSchemaVersionResponse":
        """<p>Gets a schema version with the provided information.</p>

        Args:
            type: <p>The type of schema version.</p>
            schema_versioned_id: <p>Schema id with a version specified. If the version is missing, it defaults to latest version.</p>
            format: <p>The format of the schema version.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            GetSchemaVersion happy path for an example schema version.

            >>> await client.get_schema_version(schema_versioned_id='matter.ColorControl@1.4', type='capability')
            GetSchemaVersion happy path for an example schema version.

            >>> await client.get_schema_version(schema_versioned_id='matter.ColorControl@1.4', type='capability', format='ZCL')
            GetSchemaVersion error path for an example schema version that does not exist.

            >>> await client.get_schema_version(schema_versioned_id='matter.ColorControl@$latest', type='capability')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.get_schema_version_request.GetSchemaVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.get_schema_version_response.GetSchemaVersionResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.get_schema_version

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.get_schema_version.async_get_schema_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.get_schema_version_request.GetSchemaVersionRequest = {
            "type": type,
            "schema_versioned_id": schema_versioned_id,
        }
        if format is not None:
            input_["format"] = format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_schema_versions(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        schema_id: Optional[
            "capo_iot_managed_integrations.types.schema_id.SchemaId"
        ] = None,
        namespace: Optional[
            "capo_iot_managed_integrations.types.schema_version_namespace_name.SchemaVersionNamespaceName"
        ] = None,
        visibility: Optional[
            "capo_iot_managed_integrations.types.schema_version_visibility.SchemaVersionVisibility"
        ] = None,
        semantic_version: Optional[
            "capo_iot_managed_integrations.types.schema_version_version.SchemaVersionVersion"
        ] = None,
    ) -> "capo_iot_managed_integrations.types.list_schema_versions_response.ListSchemaVersionsResponse":
        """<p>Lists schema versions with the provided information.</p>

        Args:
            type: <p>Filter on the type of schema version.</p>
            max_results: <p>The maximum number of results to return at one time.</p>
            next_token: <p>A token that can be used to retrieve the next set of results.</p>
            schema_id: <p>Filter on the id of the schema version.</p>
            namespace: <p>Filter on the name of the schema version.</p>
            visibility: <p>The visibility of the schema version.</p>
            semantic_version: <p>The schema version. If this is left blank, it defaults to the latest version.</p>

        Raises:
            capo_iot_managed_integrations.errors.access_denied_exception.AccessDeniedException: <p>User is not authorized.</p>
            capo_iot_managed_integrations.errors.conflict_exception.ConflictException: <p>There is a conflict with the request.</p>
            capo_iot_managed_integrations.errors.internal_server_exception.InternalServerException: <p>Internal error from the service that indicates an unexpected error or that the service is unavailable.</p>
            capo_iot_managed_integrations.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable.</p>
            capo_iot_managed_integrations.errors.throttling_exception.ThrottlingException: <p>The rate exceeds the limit.</p>
            capo_iot_managed_integrations.errors.validation_exception.ValidationException: <p>A validation error occurred when performing the API request.</p>
            capo_iot_managed_integrations.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListSchemaVersions happy path for an example schema version.

            >>> await client.list_schema_versions(schema_id='example.ColorControl', type='capability')
            ListSchemaVersions by version.

            >>> await client.list_schema_versions(type='capability', semantic_version='34.56')
            ListSchemaVersions error  for invalid input.

            >>> await client.list_schema_versions(schema_id='example.ColorControl', type='capability', namespace='matter')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_managed_integrations.types.list_schema_versions_request.ListSchemaVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_managed_integrations.types.list_schema_versions_response.ListSchemaVersionsResponse"
        ]:
            import capo_iot_managed_integrations._operations.iot_managed_integrations.list_schema_versions

            (
                output,
                http_response,
            ) = await capo_iot_managed_integrations._operations.iot_managed_integrations.list_schema_versions.async_list_schema_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_managed_integrations.types.list_schema_versions_request.ListSchemaVersionsRequest = {
            "type": type
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if schema_id is not None:
            input_["schema_id"] = schema_id
        if namespace is not None:
            input_["namespace"] = namespace
        if visibility is not None:
            input_["visibility"] = visibility
        if semantic_version is not None:
            input_["semantic_version"] = semantic_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_schema_versions(
        self,
        type: "capo_iot_managed_integrations.types.schema_version_type.SchemaVersionType",
        *,
        config_overrides: Optional[AsyncIoTManagedIntegrationsClientConfig] = None,
        max_results: Optional[
            "capo_iot_managed_integrations.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_iot_managed_integrations.types.next_token.NextToken"
        ] = None,
        schema_id: Optional[
            "capo_iot_managed_integrations.types.schema_id.SchemaId"
        ] = None,
        namespace: Optional[
            "capo_iot_managed_integrations.types.schema_version_namespace_name.SchemaVersionNamespaceName"
        ] = None,
        visibility: Optional[
            "capo_iot_managed_integrations.types.schema_version_visibility.SchemaVersionVisibility"
        ] = None,
        semantic_version: Optional[
            "capo_iot_managed_integrations.types.schema_version_version.SchemaVersionVersion"
        ] = None,
    ) -> "AsyncIterator[capo_iot_managed_integrations.types.schema_version_list_item.SchemaVersionListItem]":
        _token = next_token
        while True:
            _response = await self.list_schema_versions(
                type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                schema_id=schema_id,
                namespace=namespace,
                visibility=visibility,
                semantic_version=semantic_version,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
