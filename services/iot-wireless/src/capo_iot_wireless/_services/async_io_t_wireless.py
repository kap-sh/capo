"""Generated from Smithy shape ``com.amazonaws.iotwireless#iotwireless``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iot_wireless._auth._signers
import capo_iot_wireless._auth._sigv4
from capo_iot_wireless._auth._identity import Credentials
from capo_iot_wireless._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iot_wireless._auth._zapros_handler import AuthMiddleware
from capo_iot_wireless._pagination import resolve_path as _resolve_path
from capo_iot_wireless._services._aws_config import aaws_config
from capo_iot_wireless._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_iot_wireless.types.advanced_configuration
    import capo_iot_wireless.types.amazon_resource_name
    import capo_iot_wireless.types.associate_aws_account_with_partner_account_request
    import capo_iot_wireless.types.associate_aws_account_with_partner_account_response
    import capo_iot_wireless.types.associate_multicast_group_with_fuota_task_request
    import capo_iot_wireless.types.associate_multicast_group_with_fuota_task_response
    import capo_iot_wireless.types.associate_wireless_device_with_fuota_task_request
    import capo_iot_wireless.types.associate_wireless_device_with_fuota_task_response
    import capo_iot_wireless.types.associate_wireless_device_with_multicast_group_request
    import capo_iot_wireless.types.associate_wireless_device_with_multicast_group_response
    import capo_iot_wireless.types.associate_wireless_device_with_thing_request
    import capo_iot_wireless.types.associate_wireless_device_with_thing_response
    import capo_iot_wireless.types.associate_wireless_gateway_with_certificate_request
    import capo_iot_wireless.types.associate_wireless_gateway_with_certificate_response
    import capo_iot_wireless.types.associate_wireless_gateway_with_thing_request
    import capo_iot_wireless.types.associate_wireless_gateway_with_thing_response
    import capo_iot_wireless.types.auto_create_tasks
    import capo_iot_wireless.types.cancel_multicast_group_session_request
    import capo_iot_wireless.types.cancel_multicast_group_session_response
    import capo_iot_wireless.types.cell_towers
    import capo_iot_wireless.types.client_request_token
    import capo_iot_wireless.types.connection_status_event_configuration
    import capo_iot_wireless.types.connection_status_resource_type_event_configuration
    import capo_iot_wireless.types.create_destination_request
    import capo_iot_wireless.types.create_destination_response
    import capo_iot_wireless.types.create_device_profile_request
    import capo_iot_wireless.types.create_device_profile_response
    import capo_iot_wireless.types.create_fuota_task_request
    import capo_iot_wireless.types.create_fuota_task_response
    import capo_iot_wireless.types.create_multicast_group_request
    import capo_iot_wireless.types.create_multicast_group_response
    import capo_iot_wireless.types.create_network_analyzer_configuration_request
    import capo_iot_wireless.types.create_network_analyzer_configuration_response
    import capo_iot_wireless.types.create_service_profile_request
    import capo_iot_wireless.types.create_service_profile_response
    import capo_iot_wireless.types.create_wireless_device_request
    import capo_iot_wireless.types.create_wireless_device_response
    import capo_iot_wireless.types.create_wireless_gateway_request
    import capo_iot_wireless.types.create_wireless_gateway_response
    import capo_iot_wireless.types.create_wireless_gateway_task_definition_request
    import capo_iot_wireless.types.create_wireless_gateway_task_definition_response
    import capo_iot_wireless.types.create_wireless_gateway_task_request
    import capo_iot_wireless.types.create_wireless_gateway_task_response
    import capo_iot_wireless.types.creation_date
    import capo_iot_wireless.types.delete_destination_request
    import capo_iot_wireless.types.delete_destination_response
    import capo_iot_wireless.types.delete_device_profile_request
    import capo_iot_wireless.types.delete_device_profile_response
    import capo_iot_wireless.types.delete_fuota_task_request
    import capo_iot_wireless.types.delete_fuota_task_response
    import capo_iot_wireless.types.delete_multicast_group_request
    import capo_iot_wireless.types.delete_multicast_group_response
    import capo_iot_wireless.types.delete_network_analyzer_configuration_request
    import capo_iot_wireless.types.delete_network_analyzer_configuration_response
    import capo_iot_wireless.types.delete_queued_messages_request
    import capo_iot_wireless.types.delete_queued_messages_response
    import capo_iot_wireless.types.delete_service_profile_request
    import capo_iot_wireless.types.delete_service_profile_response
    import capo_iot_wireless.types.delete_wireless_device_import_task_request
    import capo_iot_wireless.types.delete_wireless_device_import_task_response
    import capo_iot_wireless.types.delete_wireless_device_request
    import capo_iot_wireless.types.delete_wireless_device_response
    import capo_iot_wireless.types.delete_wireless_gateway_request
    import capo_iot_wireless.types.delete_wireless_gateway_response
    import capo_iot_wireless.types.delete_wireless_gateway_task_definition_request
    import capo_iot_wireless.types.delete_wireless_gateway_task_definition_response
    import capo_iot_wireless.types.delete_wireless_gateway_task_request
    import capo_iot_wireless.types.delete_wireless_gateway_task_response
    import capo_iot_wireless.types.deregister_wireless_device_request
    import capo_iot_wireless.types.deregister_wireless_device_response
    import capo_iot_wireless.types.description
    import capo_iot_wireless.types.destination_name
    import capo_iot_wireless.types.device_name
    import capo_iot_wireless.types.device_profile_id
    import capo_iot_wireless.types.device_profile_name
    import capo_iot_wireless.types.device_profile_type
    import capo_iot_wireless.types.device_registration_state_event_configuration
    import capo_iot_wireless.types.device_registration_state_resource_type_event_configuration
    import capo_iot_wireless.types.disassociate_aws_account_from_partner_account_request
    import capo_iot_wireless.types.disassociate_aws_account_from_partner_account_response
    import capo_iot_wireless.types.disassociate_multicast_group_from_fuota_task_request
    import capo_iot_wireless.types.disassociate_multicast_group_from_fuota_task_response
    import capo_iot_wireless.types.disassociate_wireless_device_from_fuota_task_request
    import capo_iot_wireless.types.disassociate_wireless_device_from_fuota_task_response
    import capo_iot_wireless.types.disassociate_wireless_device_from_multicast_group_request
    import capo_iot_wireless.types.disassociate_wireless_device_from_multicast_group_response
    import capo_iot_wireless.types.disassociate_wireless_device_from_thing_request
    import capo_iot_wireless.types.disassociate_wireless_device_from_thing_response
    import capo_iot_wireless.types.disassociate_wireless_gateway_from_certificate_request
    import capo_iot_wireless.types.disassociate_wireless_gateway_from_certificate_response
    import capo_iot_wireless.types.disassociate_wireless_gateway_from_thing_request
    import capo_iot_wireless.types.disassociate_wireless_gateway_from_thing_response
    import capo_iot_wireless.types.event_notification_partner_type
    import capo_iot_wireless.types.event_notification_resource_type
    import capo_iot_wireless.types.expression
    import capo_iot_wireless.types.expression_type
    import capo_iot_wireless.types.file_descriptor
    import capo_iot_wireless.types.firmware_update_image
    import capo_iot_wireless.types.firmware_update_role
    import capo_iot_wireless.types.fragment_interval_ms
    import capo_iot_wireless.types.fragment_size_bytes
    import capo_iot_wireless.types.fuota_task_id
    import capo_iot_wireless.types.fuota_task_log_option_list
    import capo_iot_wireless.types.fuota_task_name
    import capo_iot_wireless.types.gateway_max_eirp
    import capo_iot_wireless.types.geo_json_payload
    import capo_iot_wireless.types.get_destination_request
    import capo_iot_wireless.types.get_destination_response
    import capo_iot_wireless.types.get_device_profile_request
    import capo_iot_wireless.types.get_device_profile_response
    import capo_iot_wireless.types.get_event_configuration_by_resource_types_request
    import capo_iot_wireless.types.get_event_configuration_by_resource_types_response
    import capo_iot_wireless.types.get_fuota_task_request
    import capo_iot_wireless.types.get_fuota_task_response
    import capo_iot_wireless.types.get_log_levels_by_resource_types_request
    import capo_iot_wireless.types.get_log_levels_by_resource_types_response
    import capo_iot_wireless.types.get_metric_configuration_request
    import capo_iot_wireless.types.get_metric_configuration_response
    import capo_iot_wireless.types.get_metrics_request
    import capo_iot_wireless.types.get_metrics_response
    import capo_iot_wireless.types.get_multicast_group_request
    import capo_iot_wireless.types.get_multicast_group_response
    import capo_iot_wireless.types.get_multicast_group_session_request
    import capo_iot_wireless.types.get_multicast_group_session_response
    import capo_iot_wireless.types.get_network_analyzer_configuration_request
    import capo_iot_wireless.types.get_network_analyzer_configuration_response
    import capo_iot_wireless.types.get_partner_account_request
    import capo_iot_wireless.types.get_partner_account_response
    import capo_iot_wireless.types.get_position_configuration_request
    import capo_iot_wireless.types.get_position_configuration_response
    import capo_iot_wireless.types.get_position_estimate_request
    import capo_iot_wireless.types.get_position_estimate_response
    import capo_iot_wireless.types.get_position_request
    import capo_iot_wireless.types.get_position_response
    import capo_iot_wireless.types.get_resource_event_configuration_request
    import capo_iot_wireless.types.get_resource_event_configuration_response
    import capo_iot_wireless.types.get_resource_log_level_request
    import capo_iot_wireless.types.get_resource_log_level_response
    import capo_iot_wireless.types.get_resource_position_request
    import capo_iot_wireless.types.get_resource_position_response
    import capo_iot_wireless.types.get_service_endpoint_request
    import capo_iot_wireless.types.get_service_endpoint_response
    import capo_iot_wireless.types.get_service_profile_request
    import capo_iot_wireless.types.get_service_profile_response
    import capo_iot_wireless.types.get_wireless_device_import_task_request
    import capo_iot_wireless.types.get_wireless_device_import_task_response
    import capo_iot_wireless.types.get_wireless_device_request
    import capo_iot_wireless.types.get_wireless_device_response
    import capo_iot_wireless.types.get_wireless_device_statistics_request
    import capo_iot_wireless.types.get_wireless_device_statistics_response
    import capo_iot_wireless.types.get_wireless_gateway_certificate_request
    import capo_iot_wireless.types.get_wireless_gateway_certificate_response
    import capo_iot_wireless.types.get_wireless_gateway_firmware_information_request
    import capo_iot_wireless.types.get_wireless_gateway_firmware_information_response
    import capo_iot_wireless.types.get_wireless_gateway_request
    import capo_iot_wireless.types.get_wireless_gateway_response
    import capo_iot_wireless.types.get_wireless_gateway_statistics_request
    import capo_iot_wireless.types.get_wireless_gateway_statistics_response
    import capo_iot_wireless.types.get_wireless_gateway_task_definition_request
    import capo_iot_wireless.types.get_wireless_gateway_task_definition_response
    import capo_iot_wireless.types.get_wireless_gateway_task_request
    import capo_iot_wireless.types.get_wireless_gateway_task_response
    import capo_iot_wireless.types.gnss
    import capo_iot_wireless.types.gnss_multi_frame
    import capo_iot_wireless.types.identifier
    import capo_iot_wireless.types.identifier_type
    import capo_iot_wireless.types.import_task_id
    import capo_iot_wireless.types.iot_certificate_id
    import capo_iot_wireless.types.ip
    import capo_iot_wireless.types.join_eui_filters
    import capo_iot_wireless.types.join_event_configuration
    import capo_iot_wireless.types.join_resource_type_event_configuration
    import capo_iot_wireless.types.list_destinations_request
    import capo_iot_wireless.types.list_destinations_response
    import capo_iot_wireless.types.list_device_profiles_request
    import capo_iot_wireless.types.list_device_profiles_response
    import capo_iot_wireless.types.list_devices_for_wireless_device_import_task_request
    import capo_iot_wireless.types.list_devices_for_wireless_device_import_task_response
    import capo_iot_wireless.types.list_event_configurations_request
    import capo_iot_wireless.types.list_event_configurations_response
    import capo_iot_wireless.types.list_fuota_tasks_request
    import capo_iot_wireless.types.list_fuota_tasks_response
    import capo_iot_wireless.types.list_multicast_groups_by_fuota_task_request
    import capo_iot_wireless.types.list_multicast_groups_by_fuota_task_response
    import capo_iot_wireless.types.list_multicast_groups_request
    import capo_iot_wireless.types.list_multicast_groups_response
    import capo_iot_wireless.types.list_network_analyzer_configurations_request
    import capo_iot_wireless.types.list_network_analyzer_configurations_response
    import capo_iot_wireless.types.list_partner_accounts_request
    import capo_iot_wireless.types.list_partner_accounts_response
    import capo_iot_wireless.types.list_position_configurations_request
    import capo_iot_wireless.types.list_position_configurations_response
    import capo_iot_wireless.types.list_queued_messages_request
    import capo_iot_wireless.types.list_queued_messages_response
    import capo_iot_wireless.types.list_service_profiles_request
    import capo_iot_wireless.types.list_service_profiles_response
    import capo_iot_wireless.types.list_tags_for_resource_request
    import capo_iot_wireless.types.list_tags_for_resource_response
    import capo_iot_wireless.types.list_wireless_device_import_tasks_request
    import capo_iot_wireless.types.list_wireless_device_import_tasks_response
    import capo_iot_wireless.types.list_wireless_devices_request
    import capo_iot_wireless.types.list_wireless_devices_response
    import capo_iot_wireless.types.list_wireless_gateway_task_definitions_request
    import capo_iot_wireless.types.list_wireless_gateway_task_definitions_response
    import capo_iot_wireless.types.list_wireless_gateways_request
    import capo_iot_wireless.types.list_wireless_gateways_response
    import capo_iot_wireless.types.lo_ra_wan_device
    import capo_iot_wireless.types.lo_ra_wan_device_profile
    import capo_iot_wireless.types.lo_ra_wan_fuota_task
    import capo_iot_wireless.types.lo_ra_wan_gateway
    import capo_iot_wireless.types.lo_ra_wan_multicast
    import capo_iot_wireless.types.lo_ra_wan_multicast_session
    import capo_iot_wireless.types.lo_ra_wan_service_profile
    import capo_iot_wireless.types.lo_ra_wan_start_fuota_task
    import capo_iot_wireless.types.lo_ra_wan_update_device
    import capo_iot_wireless.types.log_level
    import capo_iot_wireless.types.max_results
    import capo_iot_wireless.types.message_delivery_status_event_configuration
    import capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration
    import capo_iot_wireless.types.message_id
    import capo_iot_wireless.types.multicast_group_id
    import capo_iot_wireless.types.multicast_group_name
    import capo_iot_wireless.types.multicast_wireless_metadata
    import capo_iot_wireless.types.net_id_filters
    import capo_iot_wireless.types.network_analyzer_configuration_name
    import capo_iot_wireless.types.network_analyzer_multicast_group_list
    import capo_iot_wireless.types.next_token
    import capo_iot_wireless.types.onboard_status
    import capo_iot_wireless.types.partner_account_id
    import capo_iot_wireless.types.partner_type
    import capo_iot_wireless.types.payload_data
    import capo_iot_wireless.types.position_coordinate
    import capo_iot_wireless.types.position_resource_identifier
    import capo_iot_wireless.types.position_resource_type
    import capo_iot_wireless.types.position_solver_configurations
    import capo_iot_wireless.types.positioning_config_status
    import capo_iot_wireless.types.proximity_event_configuration
    import capo_iot_wireless.types.proximity_resource_type_event_configuration
    import capo_iot_wireless.types.put_position_configuration_request
    import capo_iot_wireless.types.put_position_configuration_response
    import capo_iot_wireless.types.put_resource_log_level_request
    import capo_iot_wireless.types.put_resource_log_level_response
    import capo_iot_wireless.types.query_string
    import capo_iot_wireless.types.redundancy_percent
    import capo_iot_wireless.types.reset_all_resource_log_levels_request
    import capo_iot_wireless.types.reset_all_resource_log_levels_response
    import capo_iot_wireless.types.reset_resource_log_level_request
    import capo_iot_wireless.types.reset_resource_log_level_response
    import capo_iot_wireless.types.resource_identifier
    import capo_iot_wireless.types.resource_type
    import capo_iot_wireless.types.role_arn
    import capo_iot_wireless.types.send_data_to_multicast_group_request
    import capo_iot_wireless.types.send_data_to_multicast_group_response
    import capo_iot_wireless.types.send_data_to_wireless_device_request
    import capo_iot_wireless.types.send_data_to_wireless_device_response
    import capo_iot_wireless.types.service_profile_id
    import capo_iot_wireless.types.service_profile_name
    import capo_iot_wireless.types.sidewalk_account_info
    import capo_iot_wireless.types.sidewalk_create_device_profile
    import capo_iot_wireless.types.sidewalk_create_wireless_device
    import capo_iot_wireless.types.sidewalk_single_start_import_info
    import capo_iot_wireless.types.sidewalk_start_import_info
    import capo_iot_wireless.types.sidewalk_update_account
    import capo_iot_wireless.types.sidewalk_update_import_info
    import capo_iot_wireless.types.sidewalk_update_wireless_device
    import capo_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_request
    import capo_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_response
    import capo_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_request
    import capo_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_response
    import capo_iot_wireless.types.start_fuota_task_request
    import capo_iot_wireless.types.start_fuota_task_response
    import capo_iot_wireless.types.start_multicast_group_session_request
    import capo_iot_wireless.types.start_multicast_group_session_response
    import capo_iot_wireless.types.start_single_wireless_device_import_task_request
    import capo_iot_wireless.types.start_single_wireless_device_import_task_response
    import capo_iot_wireless.types.start_wireless_device_import_task_request
    import capo_iot_wireless.types.start_wireless_device_import_task_response
    import capo_iot_wireless.types.summary_metric_configuration
    import capo_iot_wireless.types.summary_metric_queries
    import capo_iot_wireless.types.tag_key_list
    import capo_iot_wireless.types.tag_list
    import capo_iot_wireless.types.tag_resource_request
    import capo_iot_wireless.types.tag_resource_response
    import capo_iot_wireless.types.test_wireless_device_request
    import capo_iot_wireless.types.test_wireless_device_response
    import capo_iot_wireless.types.thing_arn
    import capo_iot_wireless.types.trace_content
    import capo_iot_wireless.types.transmit_mode
    import capo_iot_wireless.types.untag_resource_request
    import capo_iot_wireless.types.untag_resource_response
    import capo_iot_wireless.types.update_destination_request
    import capo_iot_wireless.types.update_destination_response
    import capo_iot_wireless.types.update_event_configuration_by_resource_types_request
    import capo_iot_wireless.types.update_event_configuration_by_resource_types_response
    import capo_iot_wireless.types.update_fuota_task_request
    import capo_iot_wireless.types.update_fuota_task_response
    import capo_iot_wireless.types.update_log_levels_by_resource_types_request
    import capo_iot_wireless.types.update_log_levels_by_resource_types_response
    import capo_iot_wireless.types.update_metric_configuration_request
    import capo_iot_wireless.types.update_metric_configuration_response
    import capo_iot_wireless.types.update_multicast_group_request
    import capo_iot_wireless.types.update_multicast_group_response
    import capo_iot_wireless.types.update_network_analyzer_configuration_request
    import capo_iot_wireless.types.update_network_analyzer_configuration_response
    import capo_iot_wireless.types.update_partner_account_request
    import capo_iot_wireless.types.update_partner_account_response
    import capo_iot_wireless.types.update_position_request
    import capo_iot_wireless.types.update_position_response
    import capo_iot_wireless.types.update_resource_event_configuration_request
    import capo_iot_wireless.types.update_resource_event_configuration_response
    import capo_iot_wireless.types.update_resource_position_request
    import capo_iot_wireless.types.update_resource_position_response
    import capo_iot_wireless.types.update_wireless_device_import_task_request
    import capo_iot_wireless.types.update_wireless_device_import_task_response
    import capo_iot_wireless.types.update_wireless_device_request
    import capo_iot_wireless.types.update_wireless_device_response
    import capo_iot_wireless.types.update_wireless_gateway_request
    import capo_iot_wireless.types.update_wireless_gateway_response
    import capo_iot_wireless.types.update_wireless_gateway_task_create
    import capo_iot_wireless.types.wi_fi_access_points
    import capo_iot_wireless.types.wireless_device_id
    import capo_iot_wireless.types.wireless_device_id_type
    import capo_iot_wireless.types.wireless_device_list
    import capo_iot_wireless.types.wireless_device_log_option_list
    import capo_iot_wireless.types.wireless_device_name
    import capo_iot_wireless.types.wireless_device_type
    import capo_iot_wireless.types.wireless_gateway_id
    import capo_iot_wireless.types.wireless_gateway_id_type
    import capo_iot_wireless.types.wireless_gateway_list
    import capo_iot_wireless.types.wireless_gateway_log_option_list
    import capo_iot_wireless.types.wireless_gateway_name
    import capo_iot_wireless.types.wireless_gateway_service_type
    import capo_iot_wireless.types.wireless_gateway_task_definition_id
    import capo_iot_wireless.types.wireless_gateway_task_definition_type
    import capo_iot_wireless.types.wireless_gateway_task_name
    import capo_iot_wireless.types.wireless_metadata


class AsyncIoTWirelessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncIoTWirelessClient:
    """A client for the ``IoTWireless`` service.

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
        self._config = AsyncIoTWirelessClientConfig(
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
        self, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTWirelessClientConfig = config_overrides or {}
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

    async def associate_aws_account_with_partner_account(
        self,
        sidewalk: "capo_iot_wireless.types.sidewalk_account_info.SidewalkAccountInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "capo_iot_wireless.types.associate_aws_account_with_partner_account_response.AssociateAwsAccountWithPartnerAccountResponse":
        """<p>Associates a partner account with your AWS account.</p>

        Args:
            sidewalk: <p>The Sidewalk account credentials.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            tags: <p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_aws_account_with_partner_account_request.AssociateAwsAccountWithPartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_aws_account_with_partner_account_response.AssociateAwsAccountWithPartnerAccountResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_aws_account_with_partner_account

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_aws_account_with_partner_account.async_associate_aws_account_with_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_aws_account_with_partner_account_request.AssociateAwsAccountWithPartnerAccountRequest = {
            "sidewalk": sidewalk
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_multicast_group_with_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        multicast_group_id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.associate_multicast_group_with_fuota_task_response.AssociateMulticastGroupWithFuotaTaskResponse":
        """<p>Associate a multicast group with a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_multicast_group_with_fuota_task_request.AssociateMulticastGroupWithFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_multicast_group_with_fuota_task_response.AssociateMulticastGroupWithFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_multicast_group_with_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_multicast_group_with_fuota_task.async_associate_multicast_group_with_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_multicast_group_with_fuota_task_request.AssociateMulticastGroupWithFuotaTaskRequest = {
            "id": id,
            "multicast_group_id": multicast_group_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_wireless_device_with_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.associate_wireless_device_with_fuota_task_response.AssociateWirelessDeviceWithFuotaTaskResponse":
        """<p>Associate a wireless device with a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_wireless_device_with_fuota_task_request.AssociateWirelessDeviceWithFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_wireless_device_with_fuota_task_response.AssociateWirelessDeviceWithFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_wireless_device_with_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_wireless_device_with_fuota_task.async_associate_wireless_device_with_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_wireless_device_with_fuota_task_request.AssociateWirelessDeviceWithFuotaTaskRequest = {
            "id": id,
            "wireless_device_id": wireless_device_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_wireless_device_with_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.associate_wireless_device_with_multicast_group_response.AssociateWirelessDeviceWithMulticastGroupResponse":
        """<p>Associates a wireless device with a multicast group.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_wireless_device_with_multicast_group_request.AssociateWirelessDeviceWithMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_wireless_device_with_multicast_group_response.AssociateWirelessDeviceWithMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_wireless_device_with_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_wireless_device_with_multicast_group.async_associate_wireless_device_with_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_wireless_device_with_multicast_group_request.AssociateWirelessDeviceWithMulticastGroupRequest = {
            "id": id,
            "wireless_device_id": wireless_device_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_wireless_device_with_thing(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        thing_arn: "capo_iot_wireless.types.thing_arn.ThingArn",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.associate_wireless_device_with_thing_response.AssociateWirelessDeviceWithThingResponse":
        """<p>Associates a wireless device with a thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            thing_arn: <p>The ARN of the thing to associate with the wireless device.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_wireless_device_with_thing_request.AssociateWirelessDeviceWithThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_wireless_device_with_thing_response.AssociateWirelessDeviceWithThingResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_wireless_device_with_thing

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_wireless_device_with_thing.async_associate_wireless_device_with_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_wireless_device_with_thing_request.AssociateWirelessDeviceWithThingRequest = {
            "id": id,
            "thing_arn": thing_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_wireless_gateway_with_certificate(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        iot_certificate_id: "capo_iot_wireless.types.iot_certificate_id.IotCertificateId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.associate_wireless_gateway_with_certificate_response.AssociateWirelessGatewayWithCertificateResponse":
        """<p>Associates a wireless gateway with a certificate.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            iot_certificate_id: <p>The ID of the certificate to associate with the wireless gateway.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_wireless_gateway_with_certificate_request.AssociateWirelessGatewayWithCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_wireless_gateway_with_certificate_response.AssociateWirelessGatewayWithCertificateResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_certificate

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_certificate.async_associate_wireless_gateway_with_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_wireless_gateway_with_certificate_request.AssociateWirelessGatewayWithCertificateRequest = {
            "id": id,
            "iot_certificate_id": iot_certificate_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_wireless_gateway_with_thing(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        thing_arn: "capo_iot_wireless.types.thing_arn.ThingArn",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.associate_wireless_gateway_with_thing_response.AssociateWirelessGatewayWithThingResponse":
        """<p>Associates a wireless gateway with a thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            thing_arn: <p>The ARN of the thing to associate with the wireless gateway.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.associate_wireless_gateway_with_thing_request.AssociateWirelessGatewayWithThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.associate_wireless_gateway_with_thing_response.AssociateWirelessGatewayWithThingResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_thing

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.associate_wireless_gateway_with_thing.async_associate_wireless_gateway_with_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.associate_wireless_gateway_with_thing_request.AssociateWirelessGatewayWithThingRequest = {
            "id": id,
            "thing_arn": thing_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_multicast_group_session(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.cancel_multicast_group_session_response.CancelMulticastGroupSessionResponse":
        """<p>Cancels an existing multicast group session.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.cancel_multicast_group_session_request.CancelMulticastGroupSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.cancel_multicast_group_session_response.CancelMulticastGroupSessionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.cancel_multicast_group_session

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.cancel_multicast_group_session.async_cancel_multicast_group_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.cancel_multicast_group_session_request.CancelMulticastGroupSessionRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_destination(
        self,
        name: "capo_iot_wireless.types.destination_name.DestinationName",
        expression_type: "capo_iot_wireless.types.expression_type.ExpressionType",
        expression: "capo_iot_wireless.types.expression.Expression",
        role_arn: "capo_iot_wireless.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> (
        "capo_iot_wireless.types.create_destination_response.CreateDestinationResponse"
    ):
        """<p>Creates a new destination that maps a device message to an AWS IoT rule.</p>

        Args:
            name: <p>The name of the new resource.</p>
            expression_type: <p>The type of value in <code>Expression</code>.</p>
            expression: <p>The rule name or topic rule to send messages to.</p>
            description: <p>The description of the new resource.</p>
            role_arn: <p>The ARN of the IAM Role that authorizes the destination.</p>
            tags: <p>The tags to attach to the new destination. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_destination_request.CreateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_destination_response.CreateDestinationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_destination

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_destination.async_create_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_destination_request.CreateDestinationRequest = {
            "name": name,
            "expression_type": expression_type,
            "expression": expression,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_device_profile(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.device_profile_name.DeviceProfileName"
        ] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_device_profile.LoRaWANDeviceProfile"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        sidewalk: Optional[
            "capo_iot_wireless.types.sidewalk_create_device_profile.SidewalkCreateDeviceProfile"
        ] = None,
    ) -> "capo_iot_wireless.types.create_device_profile_response.CreateDeviceProfileResponse":
        """<p>Creates a new device profile.</p>

        Args:
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            lo_ra_wan: <p>The device profile information to use to create the device profile.</p>
            tags: <p>The tags to attach to the new device profile. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            sidewalk: <p>The Sidewalk-related information for creating the Sidewalk device profile.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_device_profile_request.CreateDeviceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_device_profile_response.CreateDeviceProfileResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_device_profile

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_device_profile.async_create_device_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_device_profile_request.CreateDeviceProfileRequest = {}
        if name is not None:
            input_["name"] = name
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if sidewalk is not None:
            input_["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_fuota_task(
        self,
        firmware_update_image: "capo_iot_wireless.types.firmware_update_image.FirmwareUpdateImage",
        firmware_update_role: "capo_iot_wireless.types.firmware_update_role.FirmwareUpdateRole",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional["capo_iot_wireless.types.fuota_task_name.FuotaTaskName"] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_fuota_task.LoRaWANFuotaTask"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        redundancy_percent: Optional[
            "capo_iot_wireless.types.redundancy_percent.RedundancyPercent"
        ] = None,
        fragment_size_bytes: Optional[
            "capo_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
        ] = None,
        fragment_interval_ms: Optional[
            "capo_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
        ] = None,
        descriptor: Optional[
            "capo_iot_wireless.types.file_descriptor.FileDescriptor"
        ] = None,
    ) -> "capo_iot_wireless.types.create_fuota_task_response.CreateFuotaTaskResponse":
        """<p>Creates a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_fuota_task_request.CreateFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_fuota_task_response.CreateFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_fuota_task.async_create_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_fuota_task_request.CreateFuotaTaskRequest = {
            "firmware_update_image": firmware_update_image,
            "firmware_update_role": firmware_update_role,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input_["tags"] = tags
        if redundancy_percent is not None:
            input_["redundancy_percent"] = redundancy_percent
        if fragment_size_bytes is not None:
            input_["fragment_size_bytes"] = fragment_size_bytes
        if fragment_interval_ms is not None:
            input_["fragment_interval_ms"] = fragment_interval_ms
        if descriptor is not None:
            input_["descriptor"] = descriptor

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_multicast_group(
        self,
        lo_ra_wan: "capo_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.multicast_group_name.MulticastGroupName"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "capo_iot_wireless.types.create_multicast_group_response.CreateMulticastGroupResponse":
        """<p>Creates a multicast group.</p>

        Args:
            description: <p>The description of the multicast group.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_multicast_group_request.CreateMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_multicast_group_response.CreateMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_multicast_group.async_create_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_multicast_group_request.CreateMulticastGroupRequest = {
            "lo_ra_wan": lo_ra_wan
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_network_analyzer_configuration(
        self,
        name: "capo_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        trace_content: Optional[
            "capo_iot_wireless.types.trace_content.TraceContent"
        ] = None,
        wireless_devices: Optional[
            "capo_iot_wireless.types.wireless_device_list.WirelessDeviceList"
        ] = None,
        wireless_gateways: Optional[
            "capo_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        multicast_groups: Optional[
            "capo_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
        ] = None,
    ) -> "capo_iot_wireless.types.create_network_analyzer_configuration_response.CreateNetworkAnalyzerConfigurationResponse":
        """<p>Creates a new network analyzer configuration.</p>

        Args:
            wireless_devices: <p>Wireless device resources to add to the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resource to add in the input array.</p>
            wireless_gateways: <p>Wireless gateway resources to add to the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resource to add in the input array.</p>
            multicast_groups: <p>Multicast Group resources to add to the network analyzer configruation. Provide the <code>MulticastGroupId</code> of the resource to add in the input array.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_network_analyzer_configuration_request.CreateNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_network_analyzer_configuration_response.CreateNetworkAnalyzerConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_network_analyzer_configuration.async_create_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_network_analyzer_configuration_request.CreateNetworkAnalyzerConfigurationRequest = {
            "name": name
        }
        if trace_content is not None:
            input_["trace_content"] = trace_content
        if wireless_devices is not None:
            input_["wireless_devices"] = wireless_devices
        if wireless_gateways is not None:
            input_["wireless_gateways"] = wireless_gateways
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if multicast_groups is not None:
            input_["multicast_groups"] = multicast_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_service_profile(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.service_profile_name.ServiceProfileName"
        ] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_service_profile.LoRaWANServiceProfile"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_iot_wireless.types.create_service_profile_response.CreateServiceProfileResponse":
        """<p>Creates a new service profile.</p>

        Args:
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            lo_ra_wan: <p>The service profile information to use to create the service profile.</p>
            tags: <p>The tags to attach to the new service profile. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_service_profile_request.CreateServiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_service_profile_response.CreateServiceProfileResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_service_profile

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_service_profile.async_create_service_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_service_profile_request.CreateServiceProfileRequest = {}
        if name is not None:
            input_["name"] = name
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_wireless_device(
        self,
        type: "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType",
        destination_name: "capo_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.wireless_device_name.WirelessDeviceName"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_device.LoRaWANDevice"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        positioning: Optional[
            "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
        sidewalk: Optional[
            "capo_iot_wireless.types.sidewalk_create_wireless_device.SidewalkCreateWirelessDevice"
        ] = None,
    ) -> "capo_iot_wireless.types.create_wireless_device_response.CreateWirelessDeviceResponse":
        """<p>Provisions a wireless device.</p>

        Args:
            type: <p>The wireless device type.</p>
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>The description of the new resource.</p>
            destination_name: <p>The name of the destination to assign to the new wireless device.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            lo_ra_wan: <p>The device configuration information to use to create the wireless device.</p>
            tags: <p>The tags to attach to the new wireless device. Tags are metadata that you can use to manage a resource.</p>
            positioning: <p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>
            sidewalk: <p>The device configuration information to use to create the Sidewalk device.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_wireless_device_request.CreateWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_wireless_device_response.CreateWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_wireless_device.async_create_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_wireless_device_request.CreateWirelessDeviceRequest = {
            "type": type,
            "destination_name": destination_name,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan
        if tags is not None:
            input_["tags"] = tags
        if positioning is not None:
            input_["positioning"] = positioning
        if sidewalk is not None:
            input_["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_wireless_gateway(
        self,
        lo_ra_wan: "capo_iot_wireless.types.lo_ra_wan_gateway.LoRaWANGateway",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_iot_wireless.types.create_wireless_gateway_response.CreateWirelessGatewayResponse":
        """<p>Provisions a wireless gateway.</p> <note> <p>When provisioning a wireless gateway, you might run into duplication errors for the following reasons.</p> <ul> <li> <p>If you specify a <code>GatewayEui</code> value that already exists.</p> </li> <li> <p>If you used a <code>ClientRequestToken</code> with the same parameters within the last 10 minutes.</p> </li> </ul> <p>To avoid this error, make sure that you use unique identifiers and parameters for each request within the specified time period.</p> </note>

        Args:
            name: <p>The name of the new resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>The description of the new resource.</p>
            lo_ra_wan: <p>The gateway configuration information to use to create the wireless gateway.</p>
            tags: <p>The tags to attach to the new wireless gateway. Tags are metadata that you can use to manage a resource.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_wireless_gateway_request.CreateWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_wireless_gateway_response.CreateWirelessGatewayResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_wireless_gateway

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_wireless_gateway.async_create_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_wireless_gateway_request.CreateWirelessGatewayRequest = {
            "lo_ra_wan": lo_ra_wan
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_wireless_gateway_task(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        wireless_gateway_task_definition_id: "capo_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.create_wireless_gateway_task_response.CreateWirelessGatewayTaskResponse":
        """<p>Creates a task for a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            wireless_gateway_task_definition_id: <p>The ID of the WirelessGatewayTaskDefinition.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_wireless_gateway_task_request.CreateWirelessGatewayTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_wireless_gateway_task_response.CreateWirelessGatewayTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_wireless_gateway_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_wireless_gateway_task.async_create_wireless_gateway_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_wireless_gateway_task_request.CreateWirelessGatewayTaskRequest = {
            "id": id,
            "wireless_gateway_task_definition_id": wireless_gateway_task_definition_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_wireless_gateway_task_definition(
        self,
        auto_create_tasks: "capo_iot_wireless.types.auto_create_tasks.AutoCreateTasks",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.wireless_gateway_task_name.WirelessGatewayTaskName"
        ] = None,
        update: Optional[
            "capo_iot_wireless.types.update_wireless_gateway_task_create.UpdateWirelessGatewayTaskCreate"
        ] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "capo_iot_wireless.types.create_wireless_gateway_task_definition_response.CreateWirelessGatewayTaskDefinitionResponse":
        """<p>Creates a gateway task definition.</p>

        Args:
            auto_create_tasks: <p>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If <code>false</code>, the task must me created by calling <code>CreateWirelessGatewayTask</code>.</p>
            name: <p>The name of the new resource.</p>
            update: <p>Information about the gateways to update.</p>
            client_request_token: <p>Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a>.</p>
            tags: <p>The tags to attach to the specified resource. Tags are metadata that you can use to manage a resource.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.create_wireless_gateway_task_definition_request.CreateWirelessGatewayTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.create_wireless_gateway_task_definition_response.CreateWirelessGatewayTaskDefinitionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.create_wireless_gateway_task_definition

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.create_wireless_gateway_task_definition.async_create_wireless_gateway_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.create_wireless_gateway_task_definition_request.CreateWirelessGatewayTaskDefinitionRequest = {
            "auto_create_tasks": auto_create_tasks
        }
        if name is not None:
            input_["name"] = name
        if update is not None:
            input_["update"] = update
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
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
        name: "capo_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> (
        "capo_iot_wireless.types.delete_destination_response.DeleteDestinationResponse"
    ):
        """<p>Deletes a destination.</p>

        Args:
            name: <p>The name of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_destination_response.DeleteDestinationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_destination

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_destination.async_delete_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_destination_request.DeleteDestinationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_device_profile(
        self,
        id: "capo_iot_wireless.types.device_profile_id.DeviceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_device_profile_response.DeleteDeviceProfileResponse":
        """<p>Deletes a device profile.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_device_profile_request.DeleteDeviceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_device_profile_response.DeleteDeviceProfileResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_device_profile

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_device_profile.async_delete_device_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_device_profile_request.DeleteDeviceProfileRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_fuota_task_response.DeleteFuotaTaskResponse":
        """<p>Deletes a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_fuota_task_request.DeleteFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_fuota_task_response.DeleteFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_fuota_task.async_delete_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_fuota_task_request.DeleteFuotaTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_multicast_group_response.DeleteMulticastGroupResponse":
        """<p>Deletes a multicast group if it is not in use by a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_multicast_group_request.DeleteMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_multicast_group_response.DeleteMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_multicast_group.async_delete_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_multicast_group_request.DeleteMulticastGroupRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_network_analyzer_configuration(
        self,
        configuration_name: "capo_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_network_analyzer_configuration_response.DeleteNetworkAnalyzerConfigurationResponse":
        """<p>Deletes a network analyzer configuration.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_network_analyzer_configuration_request.DeleteNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_network_analyzer_configuration_response.DeleteNetworkAnalyzerConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_network_analyzer_configuration.async_delete_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_network_analyzer_configuration_request.DeleteNetworkAnalyzerConfigurationRequest = {
            "configuration_name": configuration_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_queued_messages(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        message_id: "capo_iot_wireless.types.message_id.MessageId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wireless_device_type: Optional[
            "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "capo_iot_wireless.types.delete_queued_messages_response.DeleteQueuedMessagesResponse":
        """<p>Remove queued messages from the downlink queue.</p>

        Args:
            id: <p>The ID of a given wireless device for which downlink messages will be deleted.</p>
            message_id: <p>If message ID is <code>"*"</code>, it cleares the entire downlink queue for a given device, specified by the wireless device ID. Otherwise, the downlink message with the specified message ID will be deleted.</p>
            wireless_device_type: <p>The wireless device type, which can be either Sidewalk or LoRaWAN.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_queued_messages_request.DeleteQueuedMessagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_queued_messages_response.DeleteQueuedMessagesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_queued_messages

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_queued_messages.async_delete_queued_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_queued_messages_request.DeleteQueuedMessagesRequest = {
            "id": id,
            "message_id": message_id,
        }
        if wireless_device_type is not None:
            input_["wireless_device_type"] = wireless_device_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_service_profile(
        self,
        id: "capo_iot_wireless.types.service_profile_id.ServiceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_service_profile_response.DeleteServiceProfileResponse":
        """<p>Deletes a service profile.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_service_profile_request.DeleteServiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_service_profile_response.DeleteServiceProfileResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_service_profile

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_service_profile.async_delete_service_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_service_profile_request.DeleteServiceProfileRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_wireless_device(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_wireless_device_response.DeleteWirelessDeviceResponse":
        """<p>Deletes a wireless device.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_wireless_device_request.DeleteWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_wireless_device_response.DeleteWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_wireless_device.async_delete_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_wireless_device_request.DeleteWirelessDeviceRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_wireless_device_import_task(
        self,
        id: "capo_iot_wireless.types.import_task_id.ImportTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_wireless_device_import_task_response.DeleteWirelessDeviceImportTaskResponse":
        """<p>Delete an import task.</p>

        Args:
            id: <p>The unique identifier of the import task to be deleted.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_wireless_device_import_task_request.DeleteWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_wireless_device_import_task_response.DeleteWirelessDeviceImportTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_wireless_device_import_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_wireless_device_import_task.async_delete_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_wireless_device_import_task_request.DeleteWirelessDeviceImportTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_wireless_gateway(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_wireless_gateway_response.DeleteWirelessGatewayResponse":
        """<p>Deletes a wireless gateway.</p> <note> <p>When deleting a wireless gateway, you might run into duplication errors for the following reasons.</p> <ul> <li> <p>If you specify a <code>GatewayEui</code> value that already exists.</p> </li> <li> <p>If you used a <code>ClientRequestToken</code> with the same parameters within the last 10 minutes.</p> </li> </ul> <p>To avoid this error, make sure that you use unique identifiers and parameters for each request within the specified time period.</p> </note>

        Args:
            id: <p>The ID of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_wireless_gateway_request.DeleteWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_wireless_gateway_response.DeleteWirelessGatewayResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_wireless_gateway

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_wireless_gateway.async_delete_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_wireless_gateway_request.DeleteWirelessGatewayRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_wireless_gateway_task(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_wireless_gateway_task_response.DeleteWirelessGatewayTaskResponse":
        """<p>Deletes a wireless gateway task.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_wireless_gateway_task_request.DeleteWirelessGatewayTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_wireless_gateway_task_response.DeleteWirelessGatewayTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_wireless_gateway_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_wireless_gateway_task.async_delete_wireless_gateway_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_wireless_gateway_task_request.DeleteWirelessGatewayTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_wireless_gateway_task_definition(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.delete_wireless_gateway_task_definition_response.DeleteWirelessGatewayTaskDefinitionResponse":
        """<p>Deletes a wireless gateway task definition. Deleting this task definition does not affect tasks that are currently in progress.</p>

        Args:
            id: <p>The ID of the resource to delete.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.delete_wireless_gateway_task_definition_request.DeleteWirelessGatewayTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.delete_wireless_gateway_task_definition_response.DeleteWirelessGatewayTaskDefinitionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.delete_wireless_gateway_task_definition

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.delete_wireless_gateway_task_definition.async_delete_wireless_gateway_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.delete_wireless_gateway_task_definition_request.DeleteWirelessGatewayTaskDefinitionRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_wireless_device(
        self,
        identifier: "capo_iot_wireless.types.identifier.Identifier",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wireless_device_type: Optional[
            "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "capo_iot_wireless.types.deregister_wireless_device_response.DeregisterWirelessDeviceResponse":
        """<p>Deregister a wireless device from AWS IoT Wireless.</p>

        Args:
            identifier: <p>The identifier of the wireless device to deregister from AWS IoT Wireless.</p>
            wireless_device_type: <p>The type of wireless device to deregister from AWS IoT Wireless, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.deregister_wireless_device_request.DeregisterWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.deregister_wireless_device_response.DeregisterWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.deregister_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.deregister_wireless_device.async_deregister_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.deregister_wireless_device_request.DeregisterWirelessDeviceRequest = {
            "identifier": identifier
        }
        if wireless_device_type is not None:
            input_["wireless_device_type"] = wireless_device_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_aws_account_from_partner_account(
        self,
        partner_account_id: "capo_iot_wireless.types.partner_account_id.PartnerAccountId",
        partner_type: "capo_iot_wireless.types.partner_type.PartnerType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_aws_account_from_partner_account_response.DisassociateAwsAccountFromPartnerAccountResponse":
        """<p>Disassociates your AWS account from a partner account. If <code>PartnerAccountId</code> and <code>PartnerType</code> are <code>null</code>, disassociates your AWS account from all partner accounts.</p>

        Args:
            partner_account_id: <p>The partner account ID to disassociate from the AWS account.</p>
            partner_type: <p>The partner type.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_aws_account_from_partner_account_request.DisassociateAwsAccountFromPartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_aws_account_from_partner_account_response.DisassociateAwsAccountFromPartnerAccountResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_aws_account_from_partner_account

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_aws_account_from_partner_account.async_disassociate_aws_account_from_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_aws_account_from_partner_account_request.DisassociateAwsAccountFromPartnerAccountRequest = {
            "partner_account_id": partner_account_id,
            "partner_type": partner_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_multicast_group_from_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        multicast_group_id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_multicast_group_from_fuota_task_response.DisassociateMulticastGroupFromFuotaTaskResponse":
        """<p>Disassociates a multicast group from a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_multicast_group_from_fuota_task_request.DisassociateMulticastGroupFromFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_multicast_group_from_fuota_task_response.DisassociateMulticastGroupFromFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_multicast_group_from_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_multicast_group_from_fuota_task.async_disassociate_multicast_group_from_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_multicast_group_from_fuota_task_request.DisassociateMulticastGroupFromFuotaTaskRequest = {
            "id": id,
            "multicast_group_id": multicast_group_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_wireless_device_from_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_wireless_device_from_fuota_task_response.DisassociateWirelessDeviceFromFuotaTaskResponse":
        """<p>Disassociates a wireless device from a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_wireless_device_from_fuota_task_request.DisassociateWirelessDeviceFromFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_wireless_device_from_fuota_task_response.DisassociateWirelessDeviceFromFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_fuota_task.async_disassociate_wireless_device_from_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_wireless_device_from_fuota_task_request.DisassociateWirelessDeviceFromFuotaTaskRequest = {
            "id": id,
            "wireless_device_id": wireless_device_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_wireless_device_from_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_wireless_device_from_multicast_group_response.DisassociateWirelessDeviceFromMulticastGroupResponse":
        """<p>Disassociates a wireless device from a multicast group.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_wireless_device_from_multicast_group_request.DisassociateWirelessDeviceFromMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_wireless_device_from_multicast_group_response.DisassociateWirelessDeviceFromMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_multicast_group.async_disassociate_wireless_device_from_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_wireless_device_from_multicast_group_request.DisassociateWirelessDeviceFromMulticastGroupRequest = {
            "id": id,
            "wireless_device_id": wireless_device_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_wireless_device_from_thing(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_wireless_device_from_thing_response.DisassociateWirelessDeviceFromThingResponse":
        """<p>Disassociates a wireless device from its currently associated thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_wireless_device_from_thing_request.DisassociateWirelessDeviceFromThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_wireless_device_from_thing_response.DisassociateWirelessDeviceFromThingResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_thing

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_wireless_device_from_thing.async_disassociate_wireless_device_from_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_wireless_device_from_thing_request.DisassociateWirelessDeviceFromThingRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_wireless_gateway_from_certificate(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_wireless_gateway_from_certificate_response.DisassociateWirelessGatewayFromCertificateResponse":
        """<p>Disassociates a wireless gateway from its currently associated certificate.</p>

        Args:
            id: <p>The ID of the resource to update.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_wireless_gateway_from_certificate_request.DisassociateWirelessGatewayFromCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_wireless_gateway_from_certificate_response.DisassociateWirelessGatewayFromCertificateResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_certificate

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_certificate.async_disassociate_wireless_gateway_from_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_wireless_gateway_from_certificate_request.DisassociateWirelessGatewayFromCertificateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_wireless_gateway_from_thing(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.disassociate_wireless_gateway_from_thing_response.DisassociateWirelessGatewayFromThingResponse":
        """<p>Disassociates a wireless gateway from its currently associated thing.</p>

        Args:
            id: <p>The ID of the resource to update.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.disassociate_wireless_gateway_from_thing_request.DisassociateWirelessGatewayFromThingRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.disassociate_wireless_gateway_from_thing_response.DisassociateWirelessGatewayFromThingResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_thing

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.disassociate_wireless_gateway_from_thing.async_disassociate_wireless_gateway_from_thing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.disassociate_wireless_gateway_from_thing_request.DisassociateWirelessGatewayFromThingRequest = {
            "id": id
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
        name: "capo_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_destination_response.GetDestinationResponse":
        """<p>Gets information about a destination.</p>

        Args:
            name: <p>The name of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_destination_request.GetDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_destination_response.GetDestinationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_destination

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_destination.async_get_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_destination_request.GetDestinationRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_device_profile(
        self,
        id: "capo_iot_wireless.types.device_profile_id.DeviceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_device_profile_response.GetDeviceProfileResponse":
        """<p>Gets information about a device profile.</p>

        Args:
            id: <p>The ID of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_device_profile_request.GetDeviceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_device_profile_response.GetDeviceProfileResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_device_profile

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_device_profile.async_get_device_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_device_profile_request.GetDeviceProfileRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_event_configuration_by_resource_types(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "capo_iot_wireless.types.get_event_configuration_by_resource_types_response.GetEventConfigurationByResourceTypesResponse":
        """<p>Get the event configuration based on resource types.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_event_configuration_by_resource_types_request.GetEventConfigurationByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_event_configuration_by_resource_types_response.GetEventConfigurationByResourceTypesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_event_configuration_by_resource_types

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_event_configuration_by_resource_types.async_get_event_configuration_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_event_configuration_by_resource_types_request.GetEventConfigurationByResourceTypesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_fuota_task_response.GetFuotaTaskResponse":
        """<p>Gets information about a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_fuota_task_request.GetFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_fuota_task_response.GetFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_fuota_task.async_get_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_fuota_task_request.GetFuotaTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_log_levels_by_resource_types(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "capo_iot_wireless.types.get_log_levels_by_resource_types_response.GetLogLevelsByResourceTypesResponse":
        """<p>Returns current default log levels or log levels by resource types. Based on the resource type, log levels can be returned for wireless device, wireless gateway, or FUOTA task log options.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_log_levels_by_resource_types_request.GetLogLevelsByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_log_levels_by_resource_types_response.GetLogLevelsByResourceTypesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_log_levels_by_resource_types

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_log_levels_by_resource_types.async_get_log_levels_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_log_levels_by_resource_types_request.GetLogLevelsByResourceTypesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_metric_configuration(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "capo_iot_wireless.types.get_metric_configuration_response.GetMetricConfigurationResponse":
        """<p>Get the metric configuration status for this AWS account.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_metric_configuration_request.GetMetricConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_metric_configuration_response.GetMetricConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_metric_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_metric_configuration.async_get_metric_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_metric_configuration_request.GetMetricConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_metrics(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        summary_metric_queries: Optional[
            "capo_iot_wireless.types.summary_metric_queries.SummaryMetricQueries"
        ] = None,
    ) -> "capo_iot_wireless.types.get_metrics_response.GetMetricsResponse":
        """<p>Get the summary metrics for this AWS account.</p>

        Args:
            summary_metric_queries: <p>The list of queries to retrieve the summary metrics.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_metrics_request.GetMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_metrics_response.GetMetricsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_metrics

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_metrics.async_get_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_metrics_request.GetMetricsRequest = {}
        if summary_metric_queries is not None:
            input_["summary_metric_queries"] = summary_metric_queries

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> (
        "capo_iot_wireless.types.get_multicast_group_response.GetMulticastGroupResponse"
    ):
        """<p>Gets information about a multicast group.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_multicast_group_request.GetMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_multicast_group_response.GetMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_multicast_group.async_get_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_multicast_group_request.GetMulticastGroupRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_multicast_group_session(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_multicast_group_session_response.GetMulticastGroupSessionResponse":
        """<p>Gets information about a multicast group session.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_multicast_group_session_request.GetMulticastGroupSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_multicast_group_session_response.GetMulticastGroupSessionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_multicast_group_session

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_multicast_group_session.async_get_multicast_group_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_multicast_group_session_request.GetMulticastGroupSessionRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_network_analyzer_configuration(
        self,
        configuration_name: "capo_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_network_analyzer_configuration_response.GetNetworkAnalyzerConfigurationResponse":
        """<p>Get network analyzer configuration.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_network_analyzer_configuration_request.GetNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_network_analyzer_configuration_response.GetNetworkAnalyzerConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_network_analyzer_configuration.async_get_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_network_analyzer_configuration_request.GetNetworkAnalyzerConfigurationRequest = {
            "configuration_name": configuration_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_partner_account(
        self,
        partner_account_id: "capo_iot_wireless.types.partner_account_id.PartnerAccountId",
        partner_type: "capo_iot_wireless.types.partner_type.PartnerType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> (
        "capo_iot_wireless.types.get_partner_account_response.GetPartnerAccountResponse"
    ):
        """<p>Gets information about a partner account. If <code>PartnerAccountId</code> and <code>PartnerType</code> are <code>null</code>, returns all partner accounts.</p>

        Args:
            partner_account_id: <p>The partner account ID to disassociate from the AWS account.</p>
            partner_type: <p>The partner type.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_partner_account_request.GetPartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_partner_account_response.GetPartnerAccountResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_partner_account

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_partner_account.async_get_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_partner_account_request.GetPartnerAccountRequest = {
            "partner_account_id": partner_account_id,
            "partner_type": partner_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_position(
        self,
        resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_position_response.GetPositionResponse":
        """<p>Get the position information for a given resource.</p> <important> <p>This action is no longer supported. Calls to retrieve the position information should use the <a href="https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html">GetResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier used to retrieve the position information.</p>
            resource_type: <p>Resource type of the resource for which position information is retrieved.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_position_request.GetPositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_position_response.GetPositionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_position

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_position.async_get_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_position_request.GetPositionRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_position_configuration(
        self,
        resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_position_configuration_response.GetPositionConfigurationResponse":
        """<p>Get position configuration for a given resource.</p> <important> <p>This action is no longer supported. Calls to retrieve the position configuration should use the <a href="https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html">GetResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier used in a position configuration.</p>
            resource_type: <p>Resource type of the resource for which position configuration is retrieved.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_position_configuration_request.GetPositionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_position_configuration_response.GetPositionConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_position_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_position_configuration.async_get_position_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_position_configuration_request.GetPositionConfigurationRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_position_estimate(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wi_fi_access_points: Optional[
            "capo_iot_wireless.types.wi_fi_access_points.WiFiAccessPoints"
        ] = None,
        cell_towers: Optional["capo_iot_wireless.types.cell_towers.CellTowers"] = None,
        ip: Optional["capo_iot_wireless.types.ip.Ip"] = None,
        gnss: Optional["capo_iot_wireless.types.gnss.Gnss"] = None,
        gnss_multi_frame: Optional[
            "capo_iot_wireless.types.gnss_multi_frame.GnssMultiFrame"
        ] = None,
        timestamp: Optional[
            "capo_iot_wireless.types.creation_date.CreationDate"
        ] = None,
        advanced_configuration: Optional[
            "capo_iot_wireless.types.advanced_configuration.AdvancedConfiguration"
        ] = None,
    ) -> "capo_iot_wireless.types.get_position_estimate_response.GetPositionEstimateResponse":
        """<p>Get estimated position information as a payload in GeoJSON format. The payload measurement data is resolved using solvers that are provided by third-party vendors.</p>

        Args:
            wi_fi_access_points: <p>Retrieves an estimated device position by resolving WLAN measurement data. The position is resolved using HERE's Wi-Fi based solver.</p>
            cell_towers: <p>Retrieves an estimated device position by resolving measurement data from cellular radio towers. The position is resolved using HERE's cellular-based solver.</p>
            ip: <p>Retrieves an estimated device position by resolving the IP address information from the device. The position is resolved using MaxMind's IP-based solver.</p>
            gnss: <p>Retrieves an estimated device position by resolving the global navigation satellite system (GNSS) scan data. The position is resolved using the GNSS solver powered by LoRa Cloud. This field is mutually exclusive with the GnssMultiFrame field.</p>
            gnss_multi_frame: <p>Retrieves an estimated device position by resolving multiple global navigation satellite system (GNSS) scan captures. The position is resolved using the multi-frame GNSS solver powered by LoRa Cloud. This field is mutually exclusive with the Gnss field.</p>
            timestamp: <p>Optional information that specifies the time when the position information will be resolved. It uses the Unix timestamp format. If not specified, the time at which the request was received will be used.</p>
            advanced_configuration: <p>Optional configuration for customizing position measurement data.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_position_estimate_request.GetPositionEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_position_estimate_response.GetPositionEstimateResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_position_estimate

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_position_estimate.async_get_position_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_position_estimate_request.GetPositionEstimateRequest = {}
        if wi_fi_access_points is not None:
            input_["wi_fi_access_points"] = wi_fi_access_points
        if cell_towers is not None:
            input_["cell_towers"] = cell_towers
        if ip is not None:
            input_["ip"] = ip
        if gnss is not None:
            input_["gnss"] = gnss
        if gnss_multi_frame is not None:
            input_["gnss_multi_frame"] = gnss_multi_frame
        if timestamp is not None:
            input_["timestamp"] = timestamp
        if advanced_configuration is not None:
            input_["advanced_configuration"] = advanced_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_event_configuration(
        self,
        identifier: "capo_iot_wireless.types.identifier.Identifier",
        identifier_type: "capo_iot_wireless.types.identifier_type.IdentifierType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        partner_type: Optional[
            "capo_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
        ] = None,
    ) -> "capo_iot_wireless.types.get_resource_event_configuration_response.GetResourceEventConfigurationResponse":
        """<p>Get the event configuration for a particular resource identifier.</p>

        Args:
            identifier: <p>Resource identifier to opt in for event messaging.</p>
            identifier_type: <p>Identifier type of the particular resource identifier for event configuration.</p>
            partner_type: <p>Partner type of the resource if the identifier type is <code>PartnerAccountId</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_resource_event_configuration_request.GetResourceEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_resource_event_configuration_response.GetResourceEventConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_resource_event_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_resource_event_configuration.async_get_resource_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_resource_event_configuration_request.GetResourceEventConfigurationRequest = {
            "identifier": identifier,
            "identifier_type": identifier_type,
        }
        if partner_type is not None:
            input_["partner_type"] = partner_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_log_level(
        self,
        resource_identifier: "capo_iot_wireless.types.resource_identifier.ResourceIdentifier",
        resource_type: "capo_iot_wireless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_resource_log_level_response.GetResourceLogLevelResponse":
        """<p>Fetches the log-level override, if any, for a given resource ID and resource type..</p>

        Args:
            resource_type: <p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_resource_log_level_request.GetResourceLogLevelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_resource_log_level_response.GetResourceLogLevelResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_resource_log_level

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_resource_log_level.async_get_resource_log_level(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_resource_log_level_request.GetResourceLogLevelRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_position(
        self,
        resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_resource_position_response.GetResourcePositionResponse":
        """<p>Get the position information for a given wireless device or a wireless gateway resource. The position information uses the <a href="https://gisgeography.com/wgs84-world-geodetic-system/"> World Geodetic System (WGS84)</a>.</p>

        Args:
            resource_identifier: <p>The identifier of the resource for which position information is retrieved. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.</p>
            resource_type: <p>The type of resource for which position information is retrieved, which can be a wireless device or a wireless gateway.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_resource_position_request.GetResourcePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_resource_position_response.GetResourcePositionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_resource_position

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_resource_position.async_get_resource_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_resource_position_request.GetResourcePositionRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_endpoint(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        service_type: Optional[
            "capo_iot_wireless.types.wireless_gateway_service_type.WirelessGatewayServiceType"
        ] = None,
    ) -> "capo_iot_wireless.types.get_service_endpoint_response.GetServiceEndpointResponse":
        """<p>Gets the account-specific endpoint for Configuration and Update Server (CUPS) protocol or LoRaWAN Network Server (LNS) connections.</p>

        Args:
            service_type: <p>The service type for which to get endpoint information about. Can be <code>CUPS</code> for the Configuration and Update Server endpoint, or <code>LNS</code> for the LoRaWAN Network Server endpoint.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_service_endpoint_request.GetServiceEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_service_endpoint_response.GetServiceEndpointResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_service_endpoint

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_service_endpoint.async_get_service_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_service_endpoint_request.GetServiceEndpointRequest = {}
        if service_type is not None:
            input_["service_type"] = service_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_profile(
        self,
        id: "capo_iot_wireless.types.service_profile_id.ServiceProfileId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> (
        "capo_iot_wireless.types.get_service_profile_response.GetServiceProfileResponse"
    ):
        """<p>Gets information about a service profile.</p>

        Args:
            id: <p>The ID of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_service_profile_request.GetServiceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_service_profile_response.GetServiceProfileResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_service_profile

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_service_profile.async_get_service_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_service_profile_request.GetServiceProfileRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_device(
        self,
        identifier: "capo_iot_wireless.types.identifier.Identifier",
        identifier_type: "capo_iot_wireless.types.wireless_device_id_type.WirelessDeviceIdType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> (
        "capo_iot_wireless.types.get_wireless_device_response.GetWirelessDeviceResponse"
    ):
        """<p>Gets information about a wireless device.</p>

        Args:
            identifier: <p>The identifier of the wireless device to get.</p>
            identifier_type: <p>The type of identifier used in <code>identifier</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_device_request.GetWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_device_response.GetWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_device.async_get_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_device_request.GetWirelessDeviceRequest = {
            "identifier": identifier,
            "identifier_type": identifier_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_device_import_task(
        self,
        id: "capo_iot_wireless.types.import_task_id.ImportTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_device_import_task_response.GetWirelessDeviceImportTaskResponse":
        """<p>Get information about an import task and count of device onboarding summary information for the import task.</p>

        Args:
            id: <p>The identifier of the import task for which information is requested.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_device_import_task_request.GetWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_device_import_task_response.GetWirelessDeviceImportTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_device_import_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_device_import_task.async_get_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_device_import_task_request.GetWirelessDeviceImportTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_device_statistics(
        self,
        wireless_device_id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_device_statistics_response.GetWirelessDeviceStatisticsResponse":
        """<p>Gets operating information about a wireless device.</p>

        Args:
            wireless_device_id: <p>The ID of the wireless device for which to get the data.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_device_statistics_request.GetWirelessDeviceStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_device_statistics_response.GetWirelessDeviceStatisticsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_device_statistics

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_device_statistics.async_get_wireless_device_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_device_statistics_request.GetWirelessDeviceStatisticsRequest = {
            "wireless_device_id": wireless_device_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_gateway(
        self,
        identifier: "capo_iot_wireless.types.identifier.Identifier",
        identifier_type: "capo_iot_wireless.types.wireless_gateway_id_type.WirelessGatewayIdType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_gateway_response.GetWirelessGatewayResponse":
        """<p>Gets information about a wireless gateway.</p>

        Args:
            identifier: <p>The identifier of the wireless gateway to get.</p>
            identifier_type: <p>The type of identifier used in <code>identifier</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_gateway_request.GetWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_gateway_response.GetWirelessGatewayResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_gateway

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_gateway.async_get_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_gateway_request.GetWirelessGatewayRequest = {
            "identifier": identifier,
            "identifier_type": identifier_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_gateway_certificate(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_gateway_certificate_response.GetWirelessGatewayCertificateResponse":
        """<p>Gets the ID of the certificate that is currently associated with a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_gateway_certificate_request.GetWirelessGatewayCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_gateway_certificate_response.GetWirelessGatewayCertificateResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_gateway_certificate

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_gateway_certificate.async_get_wireless_gateway_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_gateway_certificate_request.GetWirelessGatewayCertificateRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_gateway_firmware_information(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_gateway_firmware_information_response.GetWirelessGatewayFirmwareInformationResponse":
        """<p>Gets the firmware version and other information about a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_gateway_firmware_information_request.GetWirelessGatewayFirmwareInformationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_gateway_firmware_information_response.GetWirelessGatewayFirmwareInformationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_gateway_firmware_information

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_gateway_firmware_information.async_get_wireless_gateway_firmware_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_gateway_firmware_information_request.GetWirelessGatewayFirmwareInformationRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_gateway_statistics(
        self,
        wireless_gateway_id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_gateway_statistics_response.GetWirelessGatewayStatisticsResponse":
        """<p>Gets operating information about a wireless gateway.</p>

        Args:
            wireless_gateway_id: <p>The ID of the wireless gateway for which to get the data.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_gateway_statistics_request.GetWirelessGatewayStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_gateway_statistics_response.GetWirelessGatewayStatisticsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_gateway_statistics

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_gateway_statistics.async_get_wireless_gateway_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_gateway_statistics_request.GetWirelessGatewayStatisticsRequest = {
            "wireless_gateway_id": wireless_gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_gateway_task(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_gateway_task_response.GetWirelessGatewayTaskResponse":
        """<p>Gets information about a wireless gateway task.</p>

        Args:
            id: <p>The ID of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_gateway_task_request.GetWirelessGatewayTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_gateway_task_response.GetWirelessGatewayTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_gateway_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_gateway_task.async_get_wireless_gateway_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_gateway_task_request.GetWirelessGatewayTaskRequest = {
            "id": id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_wireless_gateway_task_definition(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_task_definition_id.WirelessGatewayTaskDefinitionId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.get_wireless_gateway_task_definition_response.GetWirelessGatewayTaskDefinitionResponse":
        """<p>Gets information about a wireless gateway task definition.</p>

        Args:
            id: <p>The ID of the resource to get.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.get_wireless_gateway_task_definition_request.GetWirelessGatewayTaskDefinitionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.get_wireless_gateway_task_definition_response.GetWirelessGatewayTaskDefinitionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.get_wireless_gateway_task_definition

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.get_wireless_gateway_task_definition.async_get_wireless_gateway_task_definition(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.get_wireless_gateway_task_definition_request.GetWirelessGatewayTaskDefinitionRequest = {
            "id": id
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
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "capo_iot_wireless.types.list_destinations_response.ListDestinationsResponse":
        """<p>Lists the destinations registered to your AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in this operation.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_destinations_request.ListDestinationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_destinations_response.ListDestinationsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_destinations

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_destinations.async_list_destinations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_destinations_request.ListDestinationsRequest = {}
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

    async def iter_list_destinations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_destinations_response.ListDestinationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_destinations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_device_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        device_profile_type: Optional[
            "capo_iot_wireless.types.device_profile_type.DeviceProfileType"
        ] = None,
    ) -> "capo_iot_wireless.types.list_device_profiles_response.ListDeviceProfilesResponse":
        """<p>Lists the device profiles registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
            device_profile_type: <p>A filter to list only device profiles that use this type, which can be <code>LoRaWAN</code> or <code>Sidewalk</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_device_profiles_request.ListDeviceProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_device_profiles_response.ListDeviceProfilesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_device_profiles

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_device_profiles.async_list_device_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_device_profiles_request.ListDeviceProfilesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if device_profile_type is not None:
            input_["device_profile_type"] = device_profile_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_device_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        device_profile_type: Optional[
            "capo_iot_wireless.types.device_profile_type.DeviceProfileType"
        ] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_device_profiles_response.ListDeviceProfilesResponse]":
        _token = next_token
        while True:
            _response = await self.list_device_profiles(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                device_profile_type=device_profile_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_devices_for_wireless_device_import_task(
        self,
        id: "capo_iot_wireless.types.import_task_id.ImportTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        status: Optional["capo_iot_wireless.types.onboard_status.OnboardStatus"] = None,
    ) -> "capo_iot_wireless.types.list_devices_for_wireless_device_import_task_response.ListDevicesForWirelessDeviceImportTaskResponse":
        """<p>List the Sidewalk devices in an import task and their onboarding status.</p>

        Args:
            id: <p>The identifier of the import task for which wireless devices are listed.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>
            status: <p>The status of the devices in the import task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_devices_for_wireless_device_import_task_request.ListDevicesForWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_devices_for_wireless_device_import_task_response.ListDevicesForWirelessDeviceImportTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_devices_for_wireless_device_import_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_devices_for_wireless_device_import_task.async_list_devices_for_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_devices_for_wireless_device_import_task_request.ListDevicesForWirelessDeviceImportTaskRequest = {
            "id": id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_event_configurations(
        self,
        resource_type: "capo_iot_wireless.types.event_notification_resource_type.EventNotificationResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "capo_iot_wireless.types.list_event_configurations_response.ListEventConfigurationsResponse":
        """<p>List event configurations where at least one event topic has been enabled.</p>

        Args:
            resource_type: <p>Resource type to filter event configurations.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_event_configurations_request.ListEventConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_event_configurations_response.ListEventConfigurationsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_event_configurations

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_event_configurations.async_list_event_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_event_configurations_request.ListEventConfigurationsRequest = {
            "resource_type": resource_type
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

    async def list_fuota_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_wireless.types.list_fuota_tasks_response.ListFuotaTasksResponse":
        """<p>Lists the FUOTA tasks registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_fuota_tasks_request.ListFuotaTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_fuota_tasks_response.ListFuotaTasksResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_fuota_tasks

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_fuota_tasks.async_list_fuota_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_fuota_tasks_request.ListFuotaTasksRequest = {}
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

    async def iter_list_fuota_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_fuota_tasks_response.ListFuotaTasksResponse]":
        _token = next_token
        while True:
            _response = await self.list_fuota_tasks(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_multicast_groups(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_wireless.types.list_multicast_groups_response.ListMulticastGroupsResponse":
        """<p>Lists the multicast groups registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_multicast_groups_request.ListMulticastGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_multicast_groups_response.ListMulticastGroupsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_multicast_groups

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_multicast_groups.async_list_multicast_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_multicast_groups_request.ListMulticastGroupsRequest = {}
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

    async def iter_list_multicast_groups(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_multicast_groups_response.ListMulticastGroupsResponse]":
        _token = next_token
        while True:
            _response = await self.list_multicast_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_multicast_groups_by_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_wireless.types.list_multicast_groups_by_fuota_task_response.ListMulticastGroupsByFuotaTaskResponse":
        """<p>List all multicast groups associated with a FUOTA task.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_multicast_groups_by_fuota_task_request.ListMulticastGroupsByFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_multicast_groups_by_fuota_task_response.ListMulticastGroupsByFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_multicast_groups_by_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_multicast_groups_by_fuota_task.async_list_multicast_groups_by_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_multicast_groups_by_fuota_task_request.ListMulticastGroupsByFuotaTaskRequest = {
            "id": id
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

    async def iter_list_multicast_groups_by_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_multicast_groups_by_fuota_task_response.ListMulticastGroupsByFuotaTaskResponse]":
        _token = next_token
        while True:
            _response = await self.list_multicast_groups_by_fuota_task(
                id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_network_analyzer_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "capo_iot_wireless.types.list_network_analyzer_configurations_response.ListNetworkAnalyzerConfigurationsResponse":
        """<p>Lists the network analyzer configurations.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_network_analyzer_configurations_request.ListNetworkAnalyzerConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_network_analyzer_configurations_response.ListNetworkAnalyzerConfigurationsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_network_analyzer_configurations

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_network_analyzer_configurations.async_list_network_analyzer_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_network_analyzer_configurations_request.ListNetworkAnalyzerConfigurationsRequest = {}
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

    async def iter_list_network_analyzer_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_network_analyzer_configurations_response.ListNetworkAnalyzerConfigurationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_network_analyzer_configurations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_partner_accounts(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_wireless.types.list_partner_accounts_response.ListPartnerAccountsResponse":
        """<p>Lists the partner accounts associated with your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_partner_accounts_request.ListPartnerAccountsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_partner_accounts_response.ListPartnerAccountsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_partner_accounts

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_partner_accounts.async_list_partner_accounts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_partner_accounts_request.ListPartnerAccountsRequest = {}
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

    async def list_position_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        resource_type: Optional[
            "capo_iot_wireless.types.position_resource_type.PositionResourceType"
        ] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "capo_iot_wireless.types.list_position_configurations_response.ListPositionConfigurationsResponse":
        """<p>List position configurations for a given resource, such as positioning solvers.</p> <important> <p>This action is no longer supported. Calls to retrieve position information should use the <a href="https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GetResourcePosition.html">GetResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_type: <p>Resource type for which position configurations are listed.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_position_configurations_request.ListPositionConfigurationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_position_configurations_response.ListPositionConfigurationsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_position_configurations

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_position_configurations.async_list_position_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_position_configurations_request.ListPositionConfigurationsRequest = {}
        if resource_type is not None:
            input_["resource_type"] = resource_type
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

    async def iter_list_position_configurations(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        resource_type: Optional[
            "capo_iot_wireless.types.position_resource_type.PositionResourceType"
        ] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_position_configurations_response.ListPositionConfigurationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_position_configurations(
                config_overrides=config_overrides,
                resource_type=resource_type,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_queued_messages(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        wireless_device_type: Optional[
            "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "capo_iot_wireless.types.list_queued_messages_response.ListQueuedMessagesResponse":
        """<p>List queued messages in the downlink queue.</p>

        Args:
            id: <p>The ID of a given wireless device which the downlink message packets are being sent.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>
            wireless_device_type: <p>The wireless device type, whic can be either Sidewalk or LoRaWAN.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_queued_messages_request.ListQueuedMessagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_queued_messages_response.ListQueuedMessagesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_queued_messages

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_queued_messages.async_list_queued_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_queued_messages_request.ListQueuedMessagesRequest = {
            "id": id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if wireless_device_type is not None:
            input_["wireless_device_type"] = wireless_device_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_queued_messages(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        wireless_device_type: Optional[
            "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_queued_messages_response.ListQueuedMessagesResponse]":
        _token = next_token
        while True:
            _response = await self.list_queued_messages(
                id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                wireless_device_type=wireless_device_type,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_wireless.types.list_service_profiles_response.ListServiceProfilesResponse":
        """<p>Lists the service profiles registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_service_profiles_request.ListServiceProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_service_profiles_response.ListServiceProfilesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_service_profiles

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_service_profiles.async_list_service_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_service_profiles_request.ListServiceProfilesRequest = {}
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

    async def iter_list_service_profiles(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_service_profiles_response.ListServiceProfilesResponse]":
        _token = next_token
        while True:
            _response = await self.list_service_profiles(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_iot_wireless.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags (metadata) you have assigned to the resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource for which you want to list tags.</p>

        Raises:
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_wireless_device_import_tasks(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
    ) -> "capo_iot_wireless.types.list_wireless_device_import_tasks_response.ListWirelessDeviceImportTasksResponse":
        """<p>List of import tasks and summary information of onboarding status of devices in each import task.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <code>null</code> to receive the first set of results.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_wireless_device_import_tasks_request.ListWirelessDeviceImportTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_wireless_device_import_tasks_response.ListWirelessDeviceImportTasksResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_wireless_device_import_tasks

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_wireless_device_import_tasks.async_list_wireless_device_import_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_wireless_device_import_tasks_request.ListWirelessDeviceImportTasksRequest = {}
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

    async def list_wireless_devices(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        destination_name: Optional[
            "capo_iot_wireless.types.destination_name.DestinationName"
        ] = None,
        device_profile_id: Optional[
            "capo_iot_wireless.types.device_profile_id.DeviceProfileId"
        ] = None,
        service_profile_id: Optional[
            "capo_iot_wireless.types.service_profile_id.ServiceProfileId"
        ] = None,
        wireless_device_type: Optional[
            "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
        fuota_task_id: Optional[
            "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
        ] = None,
        multicast_group_id: Optional[
            "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
        ] = None,
    ) -> "capo_iot_wireless.types.list_wireless_devices_response.ListWirelessDevicesResponse":
        """<p>Lists the wireless devices registered to your AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in this operation.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            destination_name: <p>A filter to list only the wireless devices that use as uplink destination.</p>
            device_profile_id: <p>A filter to list only the wireless devices that use this device profile.</p>
            service_profile_id: <p>A filter to list only the wireless devices that use this service profile.</p>
            wireless_device_type: <p>A filter to list only the wireless devices that use this wireless device type.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_wireless_devices_request.ListWirelessDevicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_wireless_devices_response.ListWirelessDevicesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_wireless_devices

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_wireless_devices.async_list_wireless_devices(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_wireless_devices_request.ListWirelessDevicesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if destination_name is not None:
            input_["destination_name"] = destination_name
        if device_profile_id is not None:
            input_["device_profile_id"] = device_profile_id
        if service_profile_id is not None:
            input_["service_profile_id"] = service_profile_id
        if wireless_device_type is not None:
            input_["wireless_device_type"] = wireless_device_type
        if fuota_task_id is not None:
            input_["fuota_task_id"] = fuota_task_id
        if multicast_group_id is not None:
            input_["multicast_group_id"] = multicast_group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_wireless_devices(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        destination_name: Optional[
            "capo_iot_wireless.types.destination_name.DestinationName"
        ] = None,
        device_profile_id: Optional[
            "capo_iot_wireless.types.device_profile_id.DeviceProfileId"
        ] = None,
        service_profile_id: Optional[
            "capo_iot_wireless.types.service_profile_id.ServiceProfileId"
        ] = None,
        wireless_device_type: Optional[
            "capo_iot_wireless.types.wireless_device_type.WirelessDeviceType"
        ] = None,
        fuota_task_id: Optional[
            "capo_iot_wireless.types.fuota_task_id.FuotaTaskId"
        ] = None,
        multicast_group_id: Optional[
            "capo_iot_wireless.types.multicast_group_id.MulticastGroupId"
        ] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_wireless_devices_response.ListWirelessDevicesResponse]":
        _token = next_token
        while True:
            _response = await self.list_wireless_devices(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                destination_name=destination_name,
                device_profile_id=device_profile_id,
                service_profile_id=service_profile_id,
                wireless_device_type=wireless_device_type,
                fuota_task_id=fuota_task_id,
                multicast_group_id=multicast_group_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_wireless_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "capo_iot_wireless.types.list_wireless_gateways_response.ListWirelessGatewaysResponse":
        """<p>Lists the wireless gateways registered to your AWS account.</p>

        Args:
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            max_results: <p>The maximum number of results to return in this operation.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_wireless_gateways_request.ListWirelessGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_wireless_gateways_response.ListWirelessGatewaysResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_wireless_gateways

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_wireless_gateways.async_list_wireless_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_wireless_gateways_request.ListWirelessGatewaysRequest = {}
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

    async def iter_list_wireless_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iot_wireless.types.list_wireless_gateways_response.ListWirelessGatewaysResponse]":
        _token = next_token
        while True:
            _response = await self.list_wireless_gateways(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_wireless_gateway_task_definitions(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        max_results: Optional["capo_iot_wireless.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iot_wireless.types.next_token.NextToken"] = None,
        task_definition_type: Optional[
            "capo_iot_wireless.types.wireless_gateway_task_definition_type.WirelessGatewayTaskDefinitionType"
        ] = None,
    ) -> "capo_iot_wireless.types.list_wireless_gateway_task_definitions_response.ListWirelessGatewayTaskDefinitionsResponse":
        """<p>List the wireless gateway tasks definitions registered to your AWS account.</p>

        Args:
            max_results: <p>The maximum number of results to return in this operation.</p>
            next_token: <p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>
            task_definition_type: <p>A filter to list only the wireless gateway task definitions that use this task definition type.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.list_wireless_gateway_task_definitions_request.ListWirelessGatewayTaskDefinitionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.list_wireless_gateway_task_definitions_response.ListWirelessGatewayTaskDefinitionsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.list_wireless_gateway_task_definitions

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.list_wireless_gateway_task_definitions.async_list_wireless_gateway_task_definitions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.list_wireless_gateway_task_definitions_request.ListWirelessGatewayTaskDefinitionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if task_definition_type is not None:
            input_["task_definition_type"] = task_definition_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_position_configuration(
        self,
        resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        solvers: Optional[
            "capo_iot_wireless.types.position_solver_configurations.PositionSolverConfigurations"
        ] = None,
        destination: Optional[
            "capo_iot_wireless.types.destination_name.DestinationName"
        ] = None,
    ) -> "capo_iot_wireless.types.put_position_configuration_response.PutPositionConfigurationResponse":
        """<p>Put position configuration for a given resource.</p> <important> <p>This action is no longer supported. Calls to update the position configuration should use the <a href="https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html">UpdateResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier used to update the position configuration.</p>
            resource_type: <p>Resource type of the resource for which you want to update the position configuration.</p>
            solvers: <p>The positioning solvers used to update the position configuration of the resource.</p>
            destination: <p>The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.put_position_configuration_request.PutPositionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.put_position_configuration_response.PutPositionConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.put_position_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.put_position_configuration.async_put_position_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.put_position_configuration_request.PutPositionConfigurationRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }
        if solvers is not None:
            input_["solvers"] = solvers
        if destination is not None:
            input_["destination"] = destination

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_log_level(
        self,
        resource_identifier: "capo_iot_wireless.types.resource_identifier.ResourceIdentifier",
        resource_type: "capo_iot_wireless.types.resource_type.ResourceType",
        log_level: "capo_iot_wireless.types.log_level.LogLevel",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.put_resource_log_level_response.PutResourceLogLevelResponse":
        """<p>Sets the log-level override for a resource ID and resource type. A limit of 200 log level override can be set per account.</p>

        Args:
            resource_type: <p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.put_resource_log_level_request.PutResourceLogLevelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.put_resource_log_level_response.PutResourceLogLevelResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.put_resource_log_level

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.put_resource_log_level.async_put_resource_log_level(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.put_resource_log_level_request.PutResourceLogLevelRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
            "log_level": log_level,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_all_resource_log_levels(
        self, *, config_overrides: Optional[AsyncIoTWirelessClientConfig] = None
    ) -> "capo_iot_wireless.types.reset_all_resource_log_levels_response.ResetAllResourceLogLevelsResponse":
        """<p>Removes the log-level overrides for all resources; wireless devices, wireless gateways, and FUOTA tasks.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.reset_all_resource_log_levels_request.ResetAllResourceLogLevelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.reset_all_resource_log_levels_response.ResetAllResourceLogLevelsResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.reset_all_resource_log_levels

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.reset_all_resource_log_levels.async_reset_all_resource_log_levels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.reset_all_resource_log_levels_request.ResetAllResourceLogLevelsRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_resource_log_level(
        self,
        resource_identifier: "capo_iot_wireless.types.resource_identifier.ResourceIdentifier",
        resource_type: "capo_iot_wireless.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.reset_resource_log_level_response.ResetResourceLogLevelResponse":
        """<p>Removes the log-level override, if any, for a specific resource ID and resource type. It can be used for a wireless device, a wireless gateway, or a FUOTA task.</p>

        Args:
            resource_type: <p>The type of resource, which can be <code>WirelessDevice</code>, <code>WirelessGateway</code>, or <code>FuotaTask</code>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.reset_resource_log_level_request.ResetResourceLogLevelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.reset_resource_log_level_response.ResetResourceLogLevelResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.reset_resource_log_level

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.reset_resource_log_level.async_reset_resource_log_level(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.reset_resource_log_level_request.ResetResourceLogLevelRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_data_to_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        payload_data: "capo_iot_wireless.types.payload_data.PayloadData",
        wireless_metadata: "capo_iot_wireless.types.multicast_wireless_metadata.MulticastWirelessMetadata",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.send_data_to_multicast_group_response.SendDataToMulticastGroupResponse":
        """<p>Sends the specified data to a multicast group.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.send_data_to_multicast_group_request.SendDataToMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.send_data_to_multicast_group_response.SendDataToMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.send_data_to_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.send_data_to_multicast_group.async_send_data_to_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.send_data_to_multicast_group_request.SendDataToMulticastGroupRequest = {
            "id": id,
            "payload_data": payload_data,
            "wireless_metadata": wireless_metadata,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_data_to_wireless_device(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        transmit_mode: "capo_iot_wireless.types.transmit_mode.TransmitMode",
        payload_data: "capo_iot_wireless.types.payload_data.PayloadData",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        wireless_metadata: Optional[
            "capo_iot_wireless.types.wireless_metadata.WirelessMetadata"
        ] = None,
    ) -> "capo_iot_wireless.types.send_data_to_wireless_device_response.SendDataToWirelessDeviceResponse":
        """<p>Sends a decrypted application data frame to a device.</p>

        Args:
            id: <p>The ID of the wireless device to receive the data.</p>
            transmit_mode: <p>The transmit mode to use to send data to the wireless device. Can be: <code>0</code> for UM (unacknowledge mode) or <code>1</code> for AM (acknowledge mode).</p>
            wireless_metadata: <p>Metadata about the message request.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.send_data_to_wireless_device_request.SendDataToWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.send_data_to_wireless_device_response.SendDataToWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.send_data_to_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.send_data_to_wireless_device.async_send_data_to_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.send_data_to_wireless_device_request.SendDataToWirelessDeviceRequest = {
            "id": id,
            "transmit_mode": transmit_mode,
            "payload_data": payload_data,
        }
        if wireless_metadata is not None:
            input_["wireless_metadata"] = wireless_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_bulk_associate_wireless_device_with_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        query_string: Optional[
            "capo_iot_wireless.types.query_string.QueryString"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "capo_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_response.StartBulkAssociateWirelessDeviceWithMulticastGroupResponse":
        """<p>Starts a bulk association of all qualifying wireless devices with a multicast group.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_request.StartBulkAssociateWirelessDeviceWithMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_response.StartBulkAssociateWirelessDeviceWithMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.start_bulk_associate_wireless_device_with_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.start_bulk_associate_wireless_device_with_multicast_group.async_start_bulk_associate_wireless_device_with_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.start_bulk_associate_wireless_device_with_multicast_group_request.StartBulkAssociateWirelessDeviceWithMulticastGroupRequest = {
            "id": id
        }
        if query_string is not None:
            input_["query_string"] = query_string
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_bulk_disassociate_wireless_device_from_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        query_string: Optional[
            "capo_iot_wireless.types.query_string.QueryString"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
    ) -> "capo_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_response.StartBulkDisassociateWirelessDeviceFromMulticastGroupResponse":
        """<p>Starts a bulk disassociatin of all qualifying wireless devices from a multicast group.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_request.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_response.StartBulkDisassociateWirelessDeviceFromMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.start_bulk_disassociate_wireless_device_from_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.start_bulk_disassociate_wireless_device_from_multicast_group.async_start_bulk_disassociate_wireless_device_from_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.start_bulk_disassociate_wireless_device_from_multicast_group_request.StartBulkDisassociateWirelessDeviceFromMulticastGroupRequest = {
            "id": id
        }
        if query_string is not None:
            input_["query_string"] = query_string
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_start_fuota_task.LoRaWANStartFuotaTask"
        ] = None,
    ) -> "capo_iot_wireless.types.start_fuota_task_response.StartFuotaTaskResponse":
        """<p>Starts a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.start_fuota_task_request.StartFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.start_fuota_task_response.StartFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.start_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.start_fuota_task.async_start_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.start_fuota_task_request.StartFuotaTaskRequest = {
            "id": id
        }
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_multicast_group_session(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        lo_ra_wan: "capo_iot_wireless.types.lo_ra_wan_multicast_session.LoRaWANMulticastSession",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.start_multicast_group_session_response.StartMulticastGroupSessionResponse":
        """<p>Starts a multicast group session.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.start_multicast_group_session_request.StartMulticastGroupSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.start_multicast_group_session_response.StartMulticastGroupSessionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.start_multicast_group_session

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.start_multicast_group_session.async_start_multicast_group_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.start_multicast_group_session_request.StartMulticastGroupSessionRequest = {
            "id": id,
            "lo_ra_wan": lo_ra_wan,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_single_wireless_device_import_task(
        self,
        destination_name: "capo_iot_wireless.types.destination_name.DestinationName",
        sidewalk: "capo_iot_wireless.types.sidewalk_single_start_import_info.SidewalkSingleStartImportInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        device_name: Optional["capo_iot_wireless.types.device_name.DeviceName"] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        positioning: Optional[
            "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
    ) -> "capo_iot_wireless.types.start_single_wireless_device_import_task_response.StartSingleWirelessDeviceImportTaskResponse":
        """<p>Start import task for a single wireless device.</p>

        Args:
            destination_name: <p>The name of the Sidewalk destination that describes the IoT rule to route messages from the device in the import task that will be onboarded to AWS IoT Wireless.</p>
            device_name: <p>The name of the wireless device for which an import task is being started.</p>
            positioning: <p>The integration status of the Device Location feature for Sidewalk devices.</p>
            sidewalk: <p>The Sidewalk-related parameters for importing a single wireless device.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.start_single_wireless_device_import_task_request.StartSingleWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.start_single_wireless_device_import_task_response.StartSingleWirelessDeviceImportTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.start_single_wireless_device_import_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.start_single_wireless_device_import_task.async_start_single_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.start_single_wireless_device_import_task_request.StartSingleWirelessDeviceImportTaskRequest = {
            "destination_name": destination_name,
            "sidewalk": sidewalk,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if device_name is not None:
            input_["device_name"] = device_name
        if tags is not None:
            input_["tags"] = tags
        if positioning is not None:
            input_["positioning"] = positioning

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_wireless_device_import_task(
        self,
        destination_name: "capo_iot_wireless.types.destination_name.DestinationName",
        sidewalk: "capo_iot_wireless.types.sidewalk_start_import_info.SidewalkStartImportInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        client_request_token: Optional[
            "capo_iot_wireless.types.client_request_token.ClientRequestToken"
        ] = None,
        tags: Optional["capo_iot_wireless.types.tag_list.TagList"] = None,
        positioning: Optional[
            "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
    ) -> "capo_iot_wireless.types.start_wireless_device_import_task_response.StartWirelessDeviceImportTaskResponse":
        """<p>Start import task for provisioning Sidewalk devices in bulk using an S3 CSV file.</p>

        Args:
            destination_name: <p>The name of the Sidewalk destination that describes the IoT rule to route messages from the devices in the import task that are onboarded to AWS IoT Wireless.</p>
            positioning: <p>The integration status of the Device Location feature for Sidewalk devices.</p>
            sidewalk: <p>The Sidewalk-related parameters for importing wireless devices that need to be provisioned in bulk.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.start_wireless_device_import_task_request.StartWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.start_wireless_device_import_task_response.StartWirelessDeviceImportTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.start_wireless_device_import_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.start_wireless_device_import_task.async_start_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.start_wireless_device_import_task_request.StartWirelessDeviceImportTaskRequest = {
            "destination_name": destination_name,
            "sidewalk": sidewalk,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags
        if positioning is not None:
            input_["positioning"] = positioning

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_iot_wireless.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_iot_wireless.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.tag_resource_response.TagResourceResponse":
        """<p>Adds a tag to a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to add tags to.</p>
            tags: <p>Adds to or modifies the tags of the given resource. Tags are metadata that you can use to manage a resource.</p>

        Raises:
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.too_many_tags_exception.TooManyTagsException: <p>The request was denied because the resource can't have any more tags.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.tag_resource

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.tag_resource_request.TagResourceRequest = {
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

    async def test_wireless_device(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.test_wireless_device_response.TestWirelessDeviceResponse":
        """<p>Simulates a provisioned device by sending an uplink data payload of <code>Hello</code>.</p>

        Args:
            id: <p>The ID of the wireless device to test.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.test_wireless_device_request.TestWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.test_wireless_device_response.TestWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.test_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.test_wireless_device.async_test_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.test_wireless_device_request.TestWirelessDeviceRequest = {
            "id": id
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
        resource_arn: "capo_iot_wireless.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_iot_wireless.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from a resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove tags from.</p>
            tag_keys: <p>A list of the keys of the tags to remove from the resource.</p>

        Raises:
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.untag_resource

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_destination(
        self,
        name: "capo_iot_wireless.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        expression_type: Optional[
            "capo_iot_wireless.types.expression_type.ExpressionType"
        ] = None,
        expression: Optional["capo_iot_wireless.types.expression.Expression"] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        role_arn: Optional["capo_iot_wireless.types.role_arn.RoleArn"] = None,
    ) -> (
        "capo_iot_wireless.types.update_destination_response.UpdateDestinationResponse"
    ):
        """<p>Updates properties of a destination.</p>

        Args:
            name: <p>The new name of the resource.</p>
            expression_type: <p>The type of value in <code>Expression</code>.</p>
            expression: <p>The new rule name or topic rule to send messages to.</p>
            description: <p>A new description of the resource.</p>
            role_arn: <p>The ARN of the IAM Role that authorizes the destination.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_destination_request.UpdateDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_destination_response.UpdateDestinationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_destination

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_destination.async_update_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_destination_request.UpdateDestinationRequest = {
            "name": name
        }
        if expression_type is not None:
            input_["expression_type"] = expression_type
        if expression is not None:
            input_["expression"] = expression
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_event_configuration_by_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        device_registration_state: Optional[
            "capo_iot_wireless.types.device_registration_state_resource_type_event_configuration.DeviceRegistrationStateResourceTypeEventConfiguration"
        ] = None,
        proximity: Optional[
            "capo_iot_wireless.types.proximity_resource_type_event_configuration.ProximityResourceTypeEventConfiguration"
        ] = None,
        join: Optional[
            "capo_iot_wireless.types.join_resource_type_event_configuration.JoinResourceTypeEventConfiguration"
        ] = None,
        connection_status: Optional[
            "capo_iot_wireless.types.connection_status_resource_type_event_configuration.ConnectionStatusResourceTypeEventConfiguration"
        ] = None,
        message_delivery_status: Optional[
            "capo_iot_wireless.types.message_delivery_status_resource_type_event_configuration.MessageDeliveryStatusResourceTypeEventConfiguration"
        ] = None,
    ) -> "capo_iot_wireless.types.update_event_configuration_by_resource_types_response.UpdateEventConfigurationByResourceTypesResponse":
        """<p>Update the event configuration based on resource types.</p>

        Args:
            device_registration_state: <p>Device registration state resource type event configuration object for enabling and disabling wireless gateway topic.</p>
            proximity: <p>Proximity resource type event configuration object for enabling and disabling wireless gateway topic.</p>
            join: <p>Join resource type event configuration object for enabling and disabling wireless device topic.</p>
            connection_status: <p>Connection status resource type event configuration object for enabling and disabling wireless gateway topic.</p>
            message_delivery_status: <p>Message delivery status resource type event configuration object for enabling and disabling wireless device topic.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_event_configuration_by_resource_types_request.UpdateEventConfigurationByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_event_configuration_by_resource_types_response.UpdateEventConfigurationByResourceTypesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_event_configuration_by_resource_types

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_event_configuration_by_resource_types.async_update_event_configuration_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_event_configuration_by_resource_types_request.UpdateEventConfigurationByResourceTypesRequest = {}
        if device_registration_state is not None:
            input_["device_registration_state"] = device_registration_state
        if proximity is not None:
            input_["proximity"] = proximity
        if join is not None:
            input_["join"] = join
        if connection_status is not None:
            input_["connection_status"] = connection_status
        if message_delivery_status is not None:
            input_["message_delivery_status"] = message_delivery_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_fuota_task(
        self,
        id: "capo_iot_wireless.types.fuota_task_id.FuotaTaskId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional["capo_iot_wireless.types.fuota_task_name.FuotaTaskName"] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_fuota_task.LoRaWANFuotaTask"
        ] = None,
        firmware_update_image: Optional[
            "capo_iot_wireless.types.firmware_update_image.FirmwareUpdateImage"
        ] = None,
        firmware_update_role: Optional[
            "capo_iot_wireless.types.firmware_update_role.FirmwareUpdateRole"
        ] = None,
        redundancy_percent: Optional[
            "capo_iot_wireless.types.redundancy_percent.RedundancyPercent"
        ] = None,
        fragment_size_bytes: Optional[
            "capo_iot_wireless.types.fragment_size_bytes.FragmentSizeBytes"
        ] = None,
        fragment_interval_ms: Optional[
            "capo_iot_wireless.types.fragment_interval_ms.FragmentIntervalMS"
        ] = None,
        descriptor: Optional[
            "capo_iot_wireless.types.file_descriptor.FileDescriptor"
        ] = None,
    ) -> "capo_iot_wireless.types.update_fuota_task_response.UpdateFuotaTaskResponse":
        """<p>Updates properties of a FUOTA task.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_fuota_task_request.UpdateFuotaTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_fuota_task_response.UpdateFuotaTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_fuota_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_fuota_task.async_update_fuota_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_fuota_task_request.UpdateFuotaTaskRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan
        if firmware_update_image is not None:
            input_["firmware_update_image"] = firmware_update_image
        if firmware_update_role is not None:
            input_["firmware_update_role"] = firmware_update_role
        if redundancy_percent is not None:
            input_["redundancy_percent"] = redundancy_percent
        if fragment_size_bytes is not None:
            input_["fragment_size_bytes"] = fragment_size_bytes
        if fragment_interval_ms is not None:
            input_["fragment_interval_ms"] = fragment_interval_ms
        if descriptor is not None:
            input_["descriptor"] = descriptor

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_log_levels_by_resource_types(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        default_log_level: Optional[
            "capo_iot_wireless.types.log_level.LogLevel"
        ] = None,
        fuota_task_log_options: Optional[
            "capo_iot_wireless.types.fuota_task_log_option_list.FuotaTaskLogOptionList"
        ] = None,
        wireless_device_log_options: Optional[
            "capo_iot_wireless.types.wireless_device_log_option_list.WirelessDeviceLogOptionList"
        ] = None,
        wireless_gateway_log_options: Optional[
            "capo_iot_wireless.types.wireless_gateway_log_option_list.WirelessGatewayLogOptionList"
        ] = None,
    ) -> "capo_iot_wireless.types.update_log_levels_by_resource_types_response.UpdateLogLevelsByResourceTypesResponse":
        """<p>Set default log level, or log levels by resource types. This can be for wireless device, wireless gateway, or FUOTA task log options, and is used to control the log messages that'll be displayed in CloudWatch.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_log_levels_by_resource_types_request.UpdateLogLevelsByResourceTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_log_levels_by_resource_types_response.UpdateLogLevelsByResourceTypesResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_log_levels_by_resource_types

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_log_levels_by_resource_types.async_update_log_levels_by_resource_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_log_levels_by_resource_types_request.UpdateLogLevelsByResourceTypesRequest = {}
        if default_log_level is not None:
            input_["default_log_level"] = default_log_level
        if fuota_task_log_options is not None:
            input_["fuota_task_log_options"] = fuota_task_log_options
        if wireless_device_log_options is not None:
            input_["wireless_device_log_options"] = wireless_device_log_options
        if wireless_gateway_log_options is not None:
            input_["wireless_gateway_log_options"] = wireless_gateway_log_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_metric_configuration(
        self,
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        summary_metric: Optional[
            "capo_iot_wireless.types.summary_metric_configuration.SummaryMetricConfiguration"
        ] = None,
    ) -> "capo_iot_wireless.types.update_metric_configuration_response.UpdateMetricConfigurationResponse":
        """<p>Update the summary metric configuration.</p>

        Args:
            summary_metric: <p>The value to be used to set summary metric configuration.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_metric_configuration_request.UpdateMetricConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_metric_configuration_response.UpdateMetricConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_metric_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_metric_configuration.async_update_metric_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_metric_configuration_request.UpdateMetricConfigurationRequest = {}
        if summary_metric is not None:
            input_["summary_metric"] = summary_metric

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_multicast_group(
        self,
        id: "capo_iot_wireless.types.multicast_group_id.MulticastGroupId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.multicast_group_name.MulticastGroupName"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_multicast.LoRaWANMulticast"
        ] = None,
    ) -> "capo_iot_wireless.types.update_multicast_group_response.UpdateMulticastGroupResponse":
        """<p>Updates properties of a multicast group session.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_multicast_group_request.UpdateMulticastGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_multicast_group_response.UpdateMulticastGroupResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_multicast_group

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_multicast_group.async_update_multicast_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_multicast_group_request.UpdateMulticastGroupRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_network_analyzer_configuration(
        self,
        configuration_name: "capo_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        trace_content: Optional[
            "capo_iot_wireless.types.trace_content.TraceContent"
        ] = None,
        wireless_devices_to_add: Optional[
            "capo_iot_wireless.types.wireless_device_list.WirelessDeviceList"
        ] = None,
        wireless_devices_to_remove: Optional[
            "capo_iot_wireless.types.wireless_device_list.WirelessDeviceList"
        ] = None,
        wireless_gateways_to_add: Optional[
            "capo_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
        ] = None,
        wireless_gateways_to_remove: Optional[
            "capo_iot_wireless.types.wireless_gateway_list.WirelessGatewayList"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        multicast_groups_to_add: Optional[
            "capo_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
        ] = None,
        multicast_groups_to_remove: Optional[
            "capo_iot_wireless.types.network_analyzer_multicast_group_list.NetworkAnalyzerMulticastGroupList"
        ] = None,
    ) -> "capo_iot_wireless.types.update_network_analyzer_configuration_response.UpdateNetworkAnalyzerConfigurationResponse":
        """<p>Update network analyzer configuration.</p>

        Args:
            wireless_devices_to_add: <p>Wireless device resources to add to the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resource to add in the input array.</p>
            wireless_devices_to_remove: <p>Wireless device resources to remove from the network analyzer configuration. Provide the <code>WirelessDeviceId</code> of the resources to remove in the input array.</p>
            wireless_gateways_to_add: <p>Wireless gateway resources to add to the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resource to add in the input array.</p>
            wireless_gateways_to_remove: <p>Wireless gateway resources to remove from the network analyzer configuration. Provide the <code>WirelessGatewayId</code> of the resources to remove in the input array.</p>
            multicast_groups_to_add: <p>Multicast group resources to add to the network analyzer configuration. Provide the <code>MulticastGroupId</code> of the resource to add in the input array.</p>
            multicast_groups_to_remove: <p>Multicast group resources to remove from the network analyzer configuration. Provide the <code>MulticastGroupId</code> of the resources to remove in the input array.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_network_analyzer_configuration_request.UpdateNetworkAnalyzerConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_network_analyzer_configuration_response.UpdateNetworkAnalyzerConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_network_analyzer_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_network_analyzer_configuration.async_update_network_analyzer_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_network_analyzer_configuration_request.UpdateNetworkAnalyzerConfigurationRequest = {
            "configuration_name": configuration_name
        }
        if trace_content is not None:
            input_["trace_content"] = trace_content
        if wireless_devices_to_add is not None:
            input_["wireless_devices_to_add"] = wireless_devices_to_add
        if wireless_devices_to_remove is not None:
            input_["wireless_devices_to_remove"] = wireless_devices_to_remove
        if wireless_gateways_to_add is not None:
            input_["wireless_gateways_to_add"] = wireless_gateways_to_add
        if wireless_gateways_to_remove is not None:
            input_["wireless_gateways_to_remove"] = wireless_gateways_to_remove
        if description is not None:
            input_["description"] = description
        if multicast_groups_to_add is not None:
            input_["multicast_groups_to_add"] = multicast_groups_to_add
        if multicast_groups_to_remove is not None:
            input_["multicast_groups_to_remove"] = multicast_groups_to_remove

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_partner_account(
        self,
        sidewalk: "capo_iot_wireless.types.sidewalk_update_account.SidewalkUpdateAccount",
        partner_account_id: "capo_iot_wireless.types.partner_account_id.PartnerAccountId",
        partner_type: "capo_iot_wireless.types.partner_type.PartnerType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.update_partner_account_response.UpdatePartnerAccountResponse":
        """<p>Updates properties of a partner account.</p>

        Args:
            sidewalk: <p>The Sidewalk account credentials.</p>
            partner_account_id: <p>The ID of the partner account to update.</p>
            partner_type: <p>The partner type.</p>

        Raises:
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_partner_account_request.UpdatePartnerAccountRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_partner_account_response.UpdatePartnerAccountResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_partner_account

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_partner_account.async_update_partner_account(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_partner_account_request.UpdatePartnerAccountRequest = {
            "sidewalk": sidewalk,
            "partner_account_id": partner_account_id,
            "partner_type": partner_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_position(
        self,
        resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType",
        position: "capo_iot_wireless.types.position_coordinate.PositionCoordinate",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.update_position_response.UpdatePositionResponse":
        """<p>Update the position information of a resource.</p> <important> <p>This action is no longer supported. Calls to update the position information should use the <a href="https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateResourcePosition.html">UpdateResourcePosition</a> API operation instead.</p> </important>

        Args:
            resource_identifier: <p>Resource identifier of the resource for which position is updated.</p>
            resource_type: <p>Resource type of the resource for which position is updated.</p>
            position: <p>The position information of the resource.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_position_request.UpdatePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_position_response.UpdatePositionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_position

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_position.async_update_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_position_request.UpdatePositionRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
            "position": position,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resource_event_configuration(
        self,
        identifier: "capo_iot_wireless.types.identifier.Identifier",
        identifier_type: "capo_iot_wireless.types.identifier_type.IdentifierType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        partner_type: Optional[
            "capo_iot_wireless.types.event_notification_partner_type.EventNotificationPartnerType"
        ] = None,
        device_registration_state: Optional[
            "capo_iot_wireless.types.device_registration_state_event_configuration.DeviceRegistrationStateEventConfiguration"
        ] = None,
        proximity: Optional[
            "capo_iot_wireless.types.proximity_event_configuration.ProximityEventConfiguration"
        ] = None,
        join: Optional[
            "capo_iot_wireless.types.join_event_configuration.JoinEventConfiguration"
        ] = None,
        connection_status: Optional[
            "capo_iot_wireless.types.connection_status_event_configuration.ConnectionStatusEventConfiguration"
        ] = None,
        message_delivery_status: Optional[
            "capo_iot_wireless.types.message_delivery_status_event_configuration.MessageDeliveryStatusEventConfiguration"
        ] = None,
    ) -> "capo_iot_wireless.types.update_resource_event_configuration_response.UpdateResourceEventConfigurationResponse":
        """<p>Update the event configuration for a particular resource identifier.</p>

        Args:
            identifier: <p>Resource identifier to opt in for event messaging.</p>
            identifier_type: <p>Identifier type of the particular resource identifier for event configuration.</p>
            partner_type: <p>Partner type of the resource if the identifier type is <code>PartnerAccountId</code> </p>
            device_registration_state: <p>Event configuration for the device registration state event.</p>
            proximity: <p>Event configuration for the proximity event.</p>
            join: <p>Event configuration for the join event.</p>
            connection_status: <p>Event configuration for the connection status event.</p>
            message_delivery_status: <p>Event configuration for the message delivery status event.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_resource_event_configuration_request.UpdateResourceEventConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_resource_event_configuration_response.UpdateResourceEventConfigurationResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_resource_event_configuration

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_resource_event_configuration.async_update_resource_event_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_resource_event_configuration_request.UpdateResourceEventConfigurationRequest = {
            "identifier": identifier,
            "identifier_type": identifier_type,
        }
        if partner_type is not None:
            input_["partner_type"] = partner_type
        if device_registration_state is not None:
            input_["device_registration_state"] = device_registration_state
        if proximity is not None:
            input_["proximity"] = proximity
        if join is not None:
            input_["join"] = join
        if connection_status is not None:
            input_["connection_status"] = connection_status
        if message_delivery_status is not None:
            input_["message_delivery_status"] = message_delivery_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resource_position(
        self,
        resource_identifier: "capo_iot_wireless.types.position_resource_identifier.PositionResourceIdentifier",
        resource_type: "capo_iot_wireless.types.position_resource_type.PositionResourceType",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        geo_json_payload: Optional[
            "capo_iot_wireless.types.geo_json_payload.GeoJsonPayload"
        ] = None,
    ) -> "capo_iot_wireless.types.update_resource_position_response.UpdateResourcePositionResponse":
        """<p>Update the position information of a given wireless device or a wireless gateway resource. The position coordinates are based on the <a href="https://gisgeography.com/wgs84-world-geodetic-system/"> World Geodetic System (WGS84)</a>.</p>

        Args:
            resource_identifier: <p>The identifier of the resource for which position information is updated. It can be the wireless device ID or the wireless gateway ID, depending on the resource type.</p>
            resource_type: <p>The type of resource for which position information is updated, which can be a wireless device or a wireless gateway.</p>
            geo_json_payload: <p>The position information of the resource, displayed as a JSON payload. The payload uses the GeoJSON format, which a format that's used to encode geographic data structures. For more information, see <a href="https://geojson.org/">GeoJSON</a>.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_resource_position_request.UpdateResourcePositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_resource_position_response.UpdateResourcePositionResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_resource_position

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_resource_position.async_update_resource_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_resource_position_request.UpdateResourcePositionRequest = {
            "resource_identifier": resource_identifier,
            "resource_type": resource_type,
        }
        if geo_json_payload is not None:
            input_["geo_json_payload"] = geo_json_payload

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_wireless_device(
        self,
        id: "capo_iot_wireless.types.wireless_device_id.WirelessDeviceId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        destination_name: Optional[
            "capo_iot_wireless.types.destination_name.DestinationName"
        ] = None,
        name: Optional[
            "capo_iot_wireless.types.wireless_device_name.WirelessDeviceName"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        lo_ra_wan: Optional[
            "capo_iot_wireless.types.lo_ra_wan_update_device.LoRaWANUpdateDevice"
        ] = None,
        positioning: Optional[
            "capo_iot_wireless.types.positioning_config_status.PositioningConfigStatus"
        ] = None,
        sidewalk: Optional[
            "capo_iot_wireless.types.sidewalk_update_wireless_device.SidewalkUpdateWirelessDevice"
        ] = None,
    ) -> "capo_iot_wireless.types.update_wireless_device_response.UpdateWirelessDeviceResponse":
        """<p>Updates properties of a wireless device.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            destination_name: <p>The name of the new destination for the device.</p>
            name: <p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>A new description of the resource.</p>
            lo_ra_wan: <p>The updated wireless device's configuration.</p>
            positioning: <p>The integration status of the Device Location feature for LoRaWAN and Sidewalk devices.</p>
            sidewalk: <p>The updated sidewalk properties.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_wireless_device_request.UpdateWirelessDeviceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_wireless_device_response.UpdateWirelessDeviceResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_wireless_device

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_wireless_device.async_update_wireless_device(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_wireless_device_request.UpdateWirelessDeviceRequest = {
            "id": id
        }
        if destination_name is not None:
            input_["destination_name"] = destination_name
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if lo_ra_wan is not None:
            input_["lo_ra_wan"] = lo_ra_wan
        if positioning is not None:
            input_["positioning"] = positioning
        if sidewalk is not None:
            input_["sidewalk"] = sidewalk

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_wireless_device_import_task(
        self,
        id: "capo_iot_wireless.types.import_task_id.ImportTaskId",
        sidewalk: "capo_iot_wireless.types.sidewalk_update_import_info.SidewalkUpdateImportInfo",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
    ) -> "capo_iot_wireless.types.update_wireless_device_import_task_response.UpdateWirelessDeviceImportTaskResponse":
        """<p>Update an import task to add more devices to the task.</p>

        Args:
            id: <p>The identifier of the import task to be updated.</p>
            sidewalk: <p>The Sidewalk-related parameters of the import task to be updated.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.conflict_exception.ConflictException: <p>Adding, updating, or deleting the resource can cause an inconsistent state.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_wireless_device_import_task_request.UpdateWirelessDeviceImportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_wireless_device_import_task_response.UpdateWirelessDeviceImportTaskResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_wireless_device_import_task

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_wireless_device_import_task.async_update_wireless_device_import_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_wireless_device_import_task_request.UpdateWirelessDeviceImportTaskRequest = {
            "id": id,
            "sidewalk": sidewalk,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_wireless_gateway(
        self,
        id: "capo_iot_wireless.types.wireless_gateway_id.WirelessGatewayId",
        *,
        config_overrides: Optional[AsyncIoTWirelessClientConfig] = None,
        name: Optional[
            "capo_iot_wireless.types.wireless_gateway_name.WirelessGatewayName"
        ] = None,
        description: Optional["capo_iot_wireless.types.description.Description"] = None,
        join_eui_filters: Optional[
            "capo_iot_wireless.types.join_eui_filters.JoinEuiFilters"
        ] = None,
        net_id_filters: Optional[
            "capo_iot_wireless.types.net_id_filters.NetIdFilters"
        ] = None,
        max_eirp: Optional[
            "capo_iot_wireless.types.gateway_max_eirp.GatewayMaxEirp"
        ] = None,
    ) -> "capo_iot_wireless.types.update_wireless_gateway_response.UpdateWirelessGatewayResponse":
        """<p>Updates properties of a wireless gateway.</p>

        Args:
            id: <p>The ID of the resource to update.</p>
            name: <p>The new name of the resource.</p> <note> <p>The following special characters aren't accepted: <code><>^#~$</code> </p> </note>
            description: <p>A new description of the resource.</p>
            max_eirp: <p>The MaxEIRP value.</p>

        Raises:
            capo_iot_wireless.errors.access_denied_exception.AccessDeniedException: <p>User does not have permission to perform this action.</p>
            capo_iot_wireless.errors.internal_server_exception.InternalServerException: <p>An unexpected error occurred while processing a request.</p>
            capo_iot_wireless.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource does not exist.</p>
            capo_iot_wireless.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the allowed API request rate.</p>
            capo_iot_wireless.errors.validation_exception.ValidationException: <p>The input did not meet the specified constraints.</p>
            capo_iot_wireless.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iot_wireless.types.update_wireless_gateway_request.UpdateWirelessGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_iot_wireless.types.update_wireless_gateway_response.UpdateWirelessGatewayResponse"
        ]:
            import capo_iot_wireless._operations.iotwireless.update_wireless_gateway

            (
                output,
                http_response,
            ) = await capo_iot_wireless._operations.iotwireless.update_wireless_gateway.async_update_wireless_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iot_wireless.types.update_wireless_gateway_request.UpdateWirelessGatewayRequest = {
            "id": id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if join_eui_filters is not None:
            input_["join_eui_filters"] = join_eui_filters
        if net_id_filters is not None:
            input_["net_id_filters"] = net_id_filters
        if max_eirp is not None:
            input_["max_eirp"] = max_eirp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
