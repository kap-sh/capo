"""Generated from Smithy shape ``com.amazonaws.medialive#MediaLive``."""

import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_medialive._auth._signers
import capo_medialive._auth._sigv4
from capo_medialive._auth._identity import Credentials
from capo_medialive._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_medialive._auth._zapros_handler import AuthMiddleware
from capo_medialive._pagination import resolve_path as _resolve_path
from capo_medialive._services._aws_config import aws_config
from capo_medialive._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_medialive.types.__boolean
    import capo_medialive.types.__double
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.__integer_min10_max86400
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__list_of__string_pattern_s
    import capo_medialive.types.__list_of_channel_pipeline_id_to_restart
    import capo_medialive.types.__list_of_event_bridge_rule_template_target
    import capo_medialive.types.__list_of_input_attachment
    import capo_medialive.types.__list_of_input_destination_request
    import capo_medialive.types.__list_of_input_device_request
    import capo_medialive.types.__list_of_input_device_settings
    import capo_medialive.types.__list_of_input_source_request
    import capo_medialive.types.__list_of_input_whitelist_rule_cidr
    import capo_medialive.types.__list_of_ip_pool_create_request
    import capo_medialive.types.__list_of_ip_pool_update_request
    import capo_medialive.types.__list_of_media_connect_flow_request
    import capo_medialive.types.__list_of_node_interface_mapping
    import capo_medialive.types.__list_of_node_interface_mapping_create_request
    import capo_medialive.types.__list_of_output_destination
    import capo_medialive.types.__list_of_route_create_request
    import capo_medialive.types.__list_of_route_update_request
    import capo_medialive.types.__string
    import capo_medialive.types.__string_max64
    import capo_medialive.types.__string_min0_max1024
    import capo_medialive.types.__string_min1_max255_pattern_s
    import capo_medialive.types.__string_min1_max256_pattern_s
    import capo_medialive.types.__string_min1_max2048
    import capo_medialive.types.__string_pattern_s
    import capo_medialive.types.accept_header
    import capo_medialive.types.accept_input_device_transfer_request
    import capo_medialive.types.accept_input_device_transfer_response
    import capo_medialive.types.account_configuration
    import capo_medialive.types.anywhere_settings
    import capo_medialive.types.batch_delete_request
    import capo_medialive.types.batch_delete_response
    import capo_medialive.types.batch_schedule_action_create_request
    import capo_medialive.types.batch_schedule_action_delete_request
    import capo_medialive.types.batch_start_request
    import capo_medialive.types.batch_start_response
    import capo_medialive.types.batch_stop_request
    import capo_medialive.types.batch_stop_response
    import capo_medialive.types.batch_update_schedule_request
    import capo_medialive.types.batch_update_schedule_response
    import capo_medialive.types.cancel_input_device_transfer_request
    import capo_medialive.types.cancel_input_device_transfer_response
    import capo_medialive.types.cdi_input_specification
    import capo_medialive.types.channel_alert
    import capo_medialive.types.channel_class
    import capo_medialive.types.channel_engine_version_request
    import capo_medialive.types.channel_summary
    import capo_medialive.types.claim_device_request
    import capo_medialive.types.claim_device_response
    import capo_medialive.types.cloud_watch_alarm_template_comparison_operator
    import capo_medialive.types.cloud_watch_alarm_template_group_summary
    import capo_medialive.types.cloud_watch_alarm_template_statistic
    import capo_medialive.types.cloud_watch_alarm_template_summary
    import capo_medialive.types.cloud_watch_alarm_template_target_resource_type
    import capo_medialive.types.cloud_watch_alarm_template_treat_missing_data
    import capo_medialive.types.cluster_alert
    import capo_medialive.types.cluster_network_settings_create_request
    import capo_medialive.types.cluster_network_settings_update_request
    import capo_medialive.types.cluster_type
    import capo_medialive.types.create_channel_placement_group_request
    import capo_medialive.types.create_channel_placement_group_response
    import capo_medialive.types.create_channel_request
    import capo_medialive.types.create_channel_response
    import capo_medialive.types.create_cloud_watch_alarm_template_group_request
    import capo_medialive.types.create_cloud_watch_alarm_template_group_response
    import capo_medialive.types.create_cloud_watch_alarm_template_request
    import capo_medialive.types.create_cloud_watch_alarm_template_response
    import capo_medialive.types.create_cluster_request
    import capo_medialive.types.create_cluster_response
    import capo_medialive.types.create_event_bridge_rule_template_group_request
    import capo_medialive.types.create_event_bridge_rule_template_group_response
    import capo_medialive.types.create_event_bridge_rule_template_request
    import capo_medialive.types.create_event_bridge_rule_template_response
    import capo_medialive.types.create_input_request
    import capo_medialive.types.create_input_response
    import capo_medialive.types.create_input_security_group_request
    import capo_medialive.types.create_input_security_group_response
    import capo_medialive.types.create_multiplex_program_request
    import capo_medialive.types.create_multiplex_program_response
    import capo_medialive.types.create_multiplex_request
    import capo_medialive.types.create_multiplex_response
    import capo_medialive.types.create_network_request
    import capo_medialive.types.create_network_response
    import capo_medialive.types.create_node_registration_script_request
    import capo_medialive.types.create_node_registration_script_response
    import capo_medialive.types.create_node_request
    import capo_medialive.types.create_node_response
    import capo_medialive.types.create_partner_input_request
    import capo_medialive.types.create_partner_input_response
    import capo_medialive.types.create_sdi_source_request
    import capo_medialive.types.create_sdi_source_response
    import capo_medialive.types.create_signal_map_request
    import capo_medialive.types.create_signal_map_response
    import capo_medialive.types.create_tags_request
    import capo_medialive.types.delete_channel_placement_group_request
    import capo_medialive.types.delete_channel_placement_group_response
    import capo_medialive.types.delete_channel_request
    import capo_medialive.types.delete_channel_response
    import capo_medialive.types.delete_cloud_watch_alarm_template_group_request
    import capo_medialive.types.delete_cloud_watch_alarm_template_request
    import capo_medialive.types.delete_cluster_request
    import capo_medialive.types.delete_cluster_response
    import capo_medialive.types.delete_event_bridge_rule_template_group_request
    import capo_medialive.types.delete_event_bridge_rule_template_request
    import capo_medialive.types.delete_input_request
    import capo_medialive.types.delete_input_response
    import capo_medialive.types.delete_input_security_group_request
    import capo_medialive.types.delete_input_security_group_response
    import capo_medialive.types.delete_multiplex_program_request
    import capo_medialive.types.delete_multiplex_program_response
    import capo_medialive.types.delete_multiplex_request
    import capo_medialive.types.delete_multiplex_response
    import capo_medialive.types.delete_network_request
    import capo_medialive.types.delete_network_response
    import capo_medialive.types.delete_node_request
    import capo_medialive.types.delete_node_response
    import capo_medialive.types.delete_reservation_request
    import capo_medialive.types.delete_reservation_response
    import capo_medialive.types.delete_schedule_request
    import capo_medialive.types.delete_schedule_response
    import capo_medialive.types.delete_sdi_source_request
    import capo_medialive.types.delete_sdi_source_response
    import capo_medialive.types.delete_signal_map_request
    import capo_medialive.types.delete_tags_request
    import capo_medialive.types.describe_account_configuration_request
    import capo_medialive.types.describe_account_configuration_response
    import capo_medialive.types.describe_channel_placement_group_request
    import capo_medialive.types.describe_channel_placement_group_response
    import capo_medialive.types.describe_channel_placement_group_summary
    import capo_medialive.types.describe_channel_request
    import capo_medialive.types.describe_channel_response
    import capo_medialive.types.describe_cluster_request
    import capo_medialive.types.describe_cluster_response
    import capo_medialive.types.describe_cluster_summary
    import capo_medialive.types.describe_input_device_request
    import capo_medialive.types.describe_input_device_response
    import capo_medialive.types.describe_input_device_thumbnail_request
    import capo_medialive.types.describe_input_device_thumbnail_response
    import capo_medialive.types.describe_input_request
    import capo_medialive.types.describe_input_response
    import capo_medialive.types.describe_input_security_group_request
    import capo_medialive.types.describe_input_security_group_response
    import capo_medialive.types.describe_multiplex_program_request
    import capo_medialive.types.describe_multiplex_program_response
    import capo_medialive.types.describe_multiplex_request
    import capo_medialive.types.describe_multiplex_response
    import capo_medialive.types.describe_network_request
    import capo_medialive.types.describe_network_response
    import capo_medialive.types.describe_network_summary
    import capo_medialive.types.describe_node_request
    import capo_medialive.types.describe_node_response
    import capo_medialive.types.describe_node_summary
    import capo_medialive.types.describe_offering_request
    import capo_medialive.types.describe_offering_response
    import capo_medialive.types.describe_reservation_request
    import capo_medialive.types.describe_reservation_response
    import capo_medialive.types.describe_schedule_request
    import capo_medialive.types.describe_schedule_response
    import capo_medialive.types.describe_sdi_source_request
    import capo_medialive.types.describe_sdi_source_response
    import capo_medialive.types.describe_thumbnails_request
    import capo_medialive.types.describe_thumbnails_response
    import capo_medialive.types.encoder_settings
    import capo_medialive.types.event_bridge_rule_template_event_type
    import capo_medialive.types.event_bridge_rule_template_group_summary
    import capo_medialive.types.event_bridge_rule_template_summary
    import capo_medialive.types.get_cloud_watch_alarm_template_group_request
    import capo_medialive.types.get_cloud_watch_alarm_template_group_response
    import capo_medialive.types.get_cloud_watch_alarm_template_request
    import capo_medialive.types.get_cloud_watch_alarm_template_response
    import capo_medialive.types.get_event_bridge_rule_template_group_request
    import capo_medialive.types.get_event_bridge_rule_template_group_response
    import capo_medialive.types.get_event_bridge_rule_template_request
    import capo_medialive.types.get_event_bridge_rule_template_response
    import capo_medialive.types.get_signal_map_request
    import capo_medialive.types.get_signal_map_response
    import capo_medialive.types.inference_settings
    import capo_medialive.types.input
    import capo_medialive.types.input_device_configurable_settings
    import capo_medialive.types.input_device_summary
    import capo_medialive.types.input_network_location
    import capo_medialive.types.input_sdi_sources
    import capo_medialive.types.input_security_group
    import capo_medialive.types.input_specification
    import capo_medialive.types.input_type
    import capo_medialive.types.input_vpc_request
    import capo_medialive.types.linked_channel_settings
    import capo_medialive.types.list_alerts_request
    import capo_medialive.types.list_alerts_response
    import capo_medialive.types.list_channel_placement_groups_request
    import capo_medialive.types.list_channel_placement_groups_response
    import capo_medialive.types.list_channels_request
    import capo_medialive.types.list_channels_response
    import capo_medialive.types.list_cloud_watch_alarm_template_groups_request
    import capo_medialive.types.list_cloud_watch_alarm_template_groups_response
    import capo_medialive.types.list_cloud_watch_alarm_templates_request
    import capo_medialive.types.list_cloud_watch_alarm_templates_response
    import capo_medialive.types.list_cluster_alerts_request
    import capo_medialive.types.list_cluster_alerts_response
    import capo_medialive.types.list_clusters_request
    import capo_medialive.types.list_clusters_response
    import capo_medialive.types.list_event_bridge_rule_template_groups_request
    import capo_medialive.types.list_event_bridge_rule_template_groups_response
    import capo_medialive.types.list_event_bridge_rule_templates_request
    import capo_medialive.types.list_event_bridge_rule_templates_response
    import capo_medialive.types.list_input_device_transfers_request
    import capo_medialive.types.list_input_device_transfers_response
    import capo_medialive.types.list_input_devices_request
    import capo_medialive.types.list_input_devices_response
    import capo_medialive.types.list_input_security_groups_request
    import capo_medialive.types.list_input_security_groups_response
    import capo_medialive.types.list_inputs_request
    import capo_medialive.types.list_inputs_response
    import capo_medialive.types.list_multiplex_alerts_request
    import capo_medialive.types.list_multiplex_alerts_response
    import capo_medialive.types.list_multiplex_programs_request
    import capo_medialive.types.list_multiplex_programs_response
    import capo_medialive.types.list_multiplexes_request
    import capo_medialive.types.list_multiplexes_response
    import capo_medialive.types.list_networks_request
    import capo_medialive.types.list_networks_response
    import capo_medialive.types.list_nodes_request
    import capo_medialive.types.list_nodes_response
    import capo_medialive.types.list_offerings_request
    import capo_medialive.types.list_offerings_response
    import capo_medialive.types.list_reservations_request
    import capo_medialive.types.list_reservations_response
    import capo_medialive.types.list_sdi_sources_request
    import capo_medialive.types.list_sdi_sources_response
    import capo_medialive.types.list_signal_maps_request
    import capo_medialive.types.list_signal_maps_response
    import capo_medialive.types.list_tags_for_resource_request
    import capo_medialive.types.list_tags_for_resource_response
    import capo_medialive.types.list_versions_request
    import capo_medialive.types.list_versions_response
    import capo_medialive.types.log_level
    import capo_medialive.types.maintenance_create_settings
    import capo_medialive.types.maintenance_update_settings
    import capo_medialive.types.max_results
    import capo_medialive.types.multicast_settings_create_request
    import capo_medialive.types.multicast_settings_update_request
    import capo_medialive.types.multiplex_alert
    import capo_medialive.types.multiplex_packet_identifiers_mapping
    import capo_medialive.types.multiplex_program_settings
    import capo_medialive.types.multiplex_program_summary
    import capo_medialive.types.multiplex_settings
    import capo_medialive.types.multiplex_summary
    import capo_medialive.types.node_role
    import capo_medialive.types.offering
    import capo_medialive.types.purchase_offering_request
    import capo_medialive.types.purchase_offering_response
    import capo_medialive.types.reboot_input_device_force
    import capo_medialive.types.reboot_input_device_request
    import capo_medialive.types.reboot_input_device_response
    import capo_medialive.types.reject_input_device_transfer_request
    import capo_medialive.types.reject_input_device_transfer_response
    import capo_medialive.types.renewal_settings
    import capo_medialive.types.reservation
    import capo_medialive.types.restart_channel_pipelines_request
    import capo_medialive.types.restart_channel_pipelines_response
    import capo_medialive.types.router_settings
    import capo_medialive.types.schedule_action
    import capo_medialive.types.sdi_source_mappings_update_request
    import capo_medialive.types.sdi_source_mode
    import capo_medialive.types.sdi_source_summary
    import capo_medialive.types.sdi_source_type
    import capo_medialive.types.signal_map_summary
    import capo_medialive.types.smpte2110_receiver_group_settings
    import capo_medialive.types.special_router_settings
    import capo_medialive.types.srt_settings_request
    import capo_medialive.types.start_channel_request
    import capo_medialive.types.start_channel_response
    import capo_medialive.types.start_delete_monitor_deployment_request
    import capo_medialive.types.start_delete_monitor_deployment_response
    import capo_medialive.types.start_input_device_maintenance_window_request
    import capo_medialive.types.start_input_device_maintenance_window_response
    import capo_medialive.types.start_input_device_request
    import capo_medialive.types.start_input_device_response
    import capo_medialive.types.start_monitor_deployment_request
    import capo_medialive.types.start_monitor_deployment_response
    import capo_medialive.types.start_multiplex_request
    import capo_medialive.types.start_multiplex_response
    import capo_medialive.types.start_update_signal_map_request
    import capo_medialive.types.start_update_signal_map_response
    import capo_medialive.types.stop_channel_request
    import capo_medialive.types.stop_channel_response
    import capo_medialive.types.stop_input_device_request
    import capo_medialive.types.stop_input_device_response
    import capo_medialive.types.stop_multiplex_request
    import capo_medialive.types.stop_multiplex_response
    import capo_medialive.types.tag_map
    import capo_medialive.types.tags
    import capo_medialive.types.transfer_input_device_request
    import capo_medialive.types.transfer_input_device_response
    import capo_medialive.types.transferring_input_device_summary
    import capo_medialive.types.update_account_configuration_request
    import capo_medialive.types.update_account_configuration_response
    import capo_medialive.types.update_channel_class_request
    import capo_medialive.types.update_channel_class_response
    import capo_medialive.types.update_channel_placement_group_request
    import capo_medialive.types.update_channel_placement_group_response
    import capo_medialive.types.update_channel_request
    import capo_medialive.types.update_channel_response
    import capo_medialive.types.update_cloud_watch_alarm_template_group_request
    import capo_medialive.types.update_cloud_watch_alarm_template_group_response
    import capo_medialive.types.update_cloud_watch_alarm_template_request
    import capo_medialive.types.update_cloud_watch_alarm_template_response
    import capo_medialive.types.update_cluster_request
    import capo_medialive.types.update_cluster_response
    import capo_medialive.types.update_event_bridge_rule_template_group_request
    import capo_medialive.types.update_event_bridge_rule_template_group_response
    import capo_medialive.types.update_event_bridge_rule_template_request
    import capo_medialive.types.update_event_bridge_rule_template_response
    import capo_medialive.types.update_input_device_request
    import capo_medialive.types.update_input_device_response
    import capo_medialive.types.update_input_request
    import capo_medialive.types.update_input_response
    import capo_medialive.types.update_input_security_group_request
    import capo_medialive.types.update_input_security_group_response
    import capo_medialive.types.update_multiplex_program_request
    import capo_medialive.types.update_multiplex_program_response
    import capo_medialive.types.update_multiplex_request
    import capo_medialive.types.update_multiplex_response
    import capo_medialive.types.update_network_request
    import capo_medialive.types.update_network_response
    import capo_medialive.types.update_node_request
    import capo_medialive.types.update_node_response
    import capo_medialive.types.update_node_state_request
    import capo_medialive.types.update_node_state_response
    import capo_medialive.types.update_node_state_shape
    import capo_medialive.types.update_reservation_request
    import capo_medialive.types.update_reservation_response
    import capo_medialive.types.update_sdi_source_request
    import capo_medialive.types.update_sdi_source_response
    import capo_medialive.types.vpc_output_settings


class MediaLiveClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class MediaLiveClient:
    """A client for the ``MediaLive`` service.

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
        self._config = MediaLiveClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[MediaLiveClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MediaLiveClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def accept_input_device_transfer(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.accept_input_device_transfer_response.AcceptInputDeviceTransferResponse":
        """Accept an incoming input device transfer. The ownership of the device will transfer to your AWS account.

        Args:
            input_device_id: The unique ID of the input device to accept. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.accept_input_device_transfer_request.AcceptInputDeviceTransferRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.accept_input_device_transfer_response.AcceptInputDeviceTransferResponse"
        ]:
            import capo_medialive._operations.media_live.accept_input_device_transfer

            output, http_response = (
                capo_medialive._operations.media_live.accept_input_device_transfer.accept_input_device_transfer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.accept_input_device_transfer_request.AcceptInputDeviceTransferRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        input_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        input_security_group_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_medialive.types.batch_delete_response.BatchDeleteResponse":
        """Starts delete of resources.

        Args:
            channel_ids: List of channel IDs
            input_ids: List of input IDs
            input_security_group_ids: List of input security group IDs
            multiplex_ids: List of multiplex IDs

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.batch_delete_request.BatchDeleteRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.batch_delete_response.BatchDeleteResponse"
        ]:
            import capo_medialive._operations.media_live.batch_delete

            output, http_response = (
                capo_medialive._operations.media_live.batch_delete.batch_delete(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.batch_delete_request.BatchDeleteRequest = {}
        if channel_ids is not None:
            input_["channel_ids"] = channel_ids
        if input_ids is not None:
            input_["input_ids"] = input_ids
        if input_security_group_ids is not None:
            input_["input_security_group_ids"] = input_security_group_ids
        if multiplex_ids is not None:
            input_["multiplex_ids"] = multiplex_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_start(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_medialive.types.batch_start_response.BatchStartResponse":
        """Starts existing resources

        Args:
            channel_ids: List of channel IDs
            multiplex_ids: List of multiplex IDs

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.batch_start_request.BatchStartRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.batch_start_response.BatchStartResponse"
        ]:
            import capo_medialive._operations.media_live.batch_start

            output, http_response = (
                capo_medialive._operations.media_live.batch_start.batch_start(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.batch_start_request.BatchStartRequest = {}
        if channel_ids is not None:
            input_["channel_ids"] = channel_ids
        if multiplex_ids is not None:
            input_["multiplex_ids"] = multiplex_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_stop(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_ids: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_medialive.types.batch_stop_response.BatchStopResponse":
        """Stops running resources

        Args:
            channel_ids: List of channel IDs
            multiplex_ids: List of multiplex IDs

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.batch_stop_request.BatchStopRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.batch_stop_response.BatchStopResponse"
        ]:
            import capo_medialive._operations.media_live.batch_stop

            output, http_response = (
                capo_medialive._operations.media_live.batch_stop.batch_stop(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.batch_stop_request.BatchStopRequest = {}
        if channel_ids is not None:
            input_["channel_ids"] = channel_ids
        if multiplex_ids is not None:
            input_["multiplex_ids"] = multiplex_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_schedule(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        creates: Optional[
            "capo_medialive.types.batch_schedule_action_create_request.BatchScheduleActionCreateRequest"
        ] = None,
        deletes: Optional[
            "capo_medialive.types.batch_schedule_action_delete_request.BatchScheduleActionDeleteRequest"
        ] = None,
    ) -> "capo_medialive.types.batch_update_schedule_response.BatchUpdateScheduleResponse":
        """Update a channel schedule

        Args:
            channel_id: Id of the channel whose schedule is being updated.
            creates: Schedule actions to create in the schedule.
            deletes: Schedule actions to delete from the schedule.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.batch_update_schedule_request.BatchUpdateScheduleRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.batch_update_schedule_response.BatchUpdateScheduleResponse"
        ]:
            import capo_medialive._operations.media_live.batch_update_schedule

            output, http_response = (
                capo_medialive._operations.media_live.batch_update_schedule.batch_update_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.batch_update_schedule_request.BatchUpdateScheduleRequest = {
            "channel_id": channel_id
        }
        if creates is not None:
            input_["creates"] = creates
        if deletes is not None:
            input_["deletes"] = deletes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_input_device_transfer(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.cancel_input_device_transfer_response.CancelInputDeviceTransferResponse":
        """Cancel an input device transfer that you have requested.

        Args:
            input_device_id: The unique ID of the input device to cancel. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.cancel_input_device_transfer_request.CancelInputDeviceTransferRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.cancel_input_device_transfer_response.CancelInputDeviceTransferResponse"
        ]:
            import capo_medialive._operations.media_live.cancel_input_device_transfer

            output, http_response = (
                capo_medialive._operations.media_live.cancel_input_device_transfer.cancel_input_device_transfer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.cancel_input_device_transfer_request.CancelInputDeviceTransferRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def claim_device(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        id: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.claim_device_response.ClaimDeviceResponse":
        """Send a request to claim an AWS Elemental device that you have purchased from a third-party vendor. After the request succeeds, you will own the device.

        Args:
            id: The id of the device you want to claim.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.claim_device_request.ClaimDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.claim_device_response.ClaimDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.claim_device

            output, http_response = (
                capo_medialive._operations.media_live.claim_device.claim_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.claim_device_request.ClaimDeviceRequest = {}
        if id is not None:
            input_["id"] = id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cdi_input_specification: Optional[
            "capo_medialive.types.cdi_input_specification.CdiInputSpecification"
        ] = None,
        channel_class: Optional[
            "capo_medialive.types.channel_class.ChannelClass"
        ] = None,
        destinations: Optional[
            "capo_medialive.types.__list_of_output_destination.__listOfOutputDestination"
        ] = None,
        encoder_settings: Optional[
            "capo_medialive.types.encoder_settings.EncoderSettings"
        ] = None,
        input_attachments: Optional[
            "capo_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
        ] = None,
        input_specification: Optional[
            "capo_medialive.types.input_specification.InputSpecification"
        ] = None,
        log_level: Optional["capo_medialive.types.log_level.LogLevel"] = None,
        maintenance: Optional[
            "capo_medialive.types.maintenance_create_settings.MaintenanceCreateSettings"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        reserved: Optional["capo_medialive.types.__string.__string"] = None,
        role_arn: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
        vpc: Optional[
            "capo_medialive.types.vpc_output_settings.VpcOutputSettings"
        ] = None,
        anywhere_settings: Optional[
            "capo_medialive.types.anywhere_settings.AnywhereSettings"
        ] = None,
        channel_engine_version: Optional[
            "capo_medialive.types.channel_engine_version_request.ChannelEngineVersionRequest"
        ] = None,
        dry_run: Optional["capo_medialive.types.__boolean.__boolean"] = None,
        linked_channel_settings: Optional[
            "capo_medialive.types.linked_channel_settings.LinkedChannelSettings"
        ] = None,
        channel_security_groups: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        inference_settings: Optional[
            "capo_medialive.types.inference_settings.InferenceSettings"
        ] = None,
    ) -> "capo_medialive.types.create_channel_response.CreateChannelResponse":
        """Creates a new channel

        Args:
            cdi_input_specification: Specification of CDI inputs for this channel
            channel_class: The class for this channel. STANDARD for a channel with two pipelines or SINGLE_PIPELINE for a channel with one pipeline.
            input_attachments: List of input attachments for channel.
            input_specification: Specification of network and file inputs for this channel
            log_level: The log level to write to CloudWatch Logs.
            maintenance: Maintenance settings for this channel.
            name: Name of channel.
            request_id: Unique request ID to be specified. This is needed to prevent retries from creating multiple resources.
            reserved: Deprecated field that's only usable by whitelisted customers.
            role_arn: An optional Amazon Resource Name (ARN) of the role to assume when running the Channel.
            tags: A collection of key-value pairs.
            vpc: Settings for the VPC outputs
            anywhere_settings: The Elemental Anywhere settings for this channel.
            channel_engine_version: The desired engine version for this channel.
            linked_channel_settings: The linked channel settings for the channel.
            channel_security_groups: A list of IDs for all the Input Security Groups attached to the channel.
            inference_settings: Include this setting to include Elemental Inference features in this channel.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_channel_request.CreateChannelRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_channel_response.CreateChannelResponse"
        ]:
            import capo_medialive._operations.media_live.create_channel

            output, http_response = (
                capo_medialive._operations.media_live.create_channel.create_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_channel_request.CreateChannelRequest = {}
        if cdi_input_specification is not None:
            input_["cdi_input_specification"] = cdi_input_specification
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if destinations is not None:
            input_["destinations"] = destinations
        if encoder_settings is not None:
            input_["encoder_settings"] = encoder_settings
        if input_attachments is not None:
            input_["input_attachments"] = input_attachments
        if input_specification is not None:
            input_["input_specification"] = input_specification
        if log_level is not None:
            input_["log_level"] = log_level
        if maintenance is not None:
            input_["maintenance"] = maintenance
        if name is not None:
            input_["name"] = name
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if reserved is not None:
            input_["reserved"] = reserved
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if vpc is not None:
            input_["vpc"] = vpc
        if anywhere_settings is not None:
            input_["anywhere_settings"] = anywhere_settings
        if channel_engine_version is not None:
            input_["channel_engine_version"] = channel_engine_version
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if linked_channel_settings is not None:
            input_["linked_channel_settings"] = linked_channel_settings
        if channel_security_groups is not None:
            input_["channel_security_groups"] = channel_security_groups
        if inference_settings is not None:
            input_["inference_settings"] = inference_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_channel_placement_group(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        nodes: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> "capo_medialive.types.create_channel_placement_group_response.CreateChannelPlacementGroupResponse":
        """Create a ChannelPlacementGroup in the specified Cluster. As part of the create operation, you specify the Nodes to attach the group to.After you create a ChannelPlacementGroup, you add Channels to the group (you do this by modifying the Channels to add them to a specific group). You now have an association of Channels to ChannelPlacementGroup, and ChannelPlacementGroup to Nodes. This association means that all the Channels in the group are able to run on any of the Nodes associated with the group.

        Args:
            cluster_id: The ID of the cluster.
            name: Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive.
            nodes: An array of one ID for the Node that you want to associate with the ChannelPlacementGroup. (You can't associate more than one Node with the ChannelPlacementGroup.) The Node and the ChannelPlacementGroup must be in the same Cluster.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources. the request.
            tags: A collection of key-value pairs.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_channel_placement_group_request.CreateChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_channel_placement_group_response.CreateChannelPlacementGroupResponse"
        ]:
            import capo_medialive._operations.media_live.create_channel_placement_group

            output, http_response = (
                capo_medialive._operations.media_live.create_channel_placement_group.create_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_channel_placement_group_request.CreateChannelPlacementGroupRequest = {
            "cluster_id": cluster_id
        }
        if name is not None:
            input_["name"] = name
        if nodes is not None:
            input_["nodes"] = nodes
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cloud_watch_alarm_template(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        comparison_operator: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator"
        ] = None,
        datapoints_to_alarm: Optional[
            "capo_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        evaluation_periods: Optional[
            "capo_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        group_identifier: Optional[
            "capo_medialive.types.__string_pattern_s.__stringPatternS"
        ] = None,
        metric_name: Optional[
            "capo_medialive.types.__string_max64.__stringMax64"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        period: Optional[
            "capo_medialive.types.__integer_min10_max86400.__integerMin10Max86400"
        ] = None,
        statistic: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic"
        ] = None,
        tags: Optional["capo_medialive.types.tag_map.TagMap"] = None,
        target_resource_type: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType"
        ] = None,
        threshold: Optional["capo_medialive.types.__double.__double"] = None,
        treat_missing_data: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData"
        ] = None,
        request_id: Optional[
            "capo_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "capo_medialive.types.create_cloud_watch_alarm_template_response.CreateCloudWatchAlarmTemplateResponse":
        """Creates a cloudwatch alarm template to dynamically generate cloudwatch metric alarms on targeted resource types.

        Args:
            datapoints_to_alarm: The number of datapoints within the evaluation period that must be breaching to trigger the alarm.
            description: A resource's optional description.
            evaluation_periods: The number of periods over which data is compared to the specified threshold.
            group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            metric_name: The name of the metric associated with the alarm. Must be compatible with targetResourceType.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            period: The period, in seconds, over which the specified statistic is applied.
            threshold: The threshold value to compare with the specified statistic.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_cloud_watch_alarm_template_request.CreateCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_cloud_watch_alarm_template_response.CreateCloudWatchAlarmTemplateResponse"
        ]:
            import capo_medialive._operations.media_live.create_cloud_watch_alarm_template

            output, http_response = (
                capo_medialive._operations.media_live.create_cloud_watch_alarm_template.create_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_cloud_watch_alarm_template_request.CreateCloudWatchAlarmTemplateRequest = {}
        if comparison_operator is not None:
            input_["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            input_["datapoints_to_alarm"] = datapoints_to_alarm
        if description is not None:
            input_["description"] = description
        if evaluation_periods is not None:
            input_["evaluation_periods"] = evaluation_periods
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if name is not None:
            input_["name"] = name
        if period is not None:
            input_["period"] = period
        if statistic is not None:
            input_["statistic"] = statistic
        if tags is not None:
            input_["tags"] = tags
        if target_resource_type is not None:
            input_["target_resource_type"] = target_resource_type
        if threshold is not None:
            input_["threshold"] = threshold
        if treat_missing_data is not None:
            input_["treat_missing_data"] = treat_missing_data
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cloud_watch_alarm_template_group(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        tags: Optional["capo_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "capo_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "capo_medialive.types.create_cloud_watch_alarm_template_group_response.CreateCloudWatchAlarmTemplateGroupResponse":
        """Creates a cloudwatch alarm template group to group your cloudwatch alarm templates and to attach to signal maps for dynamically creating alarms.

        Args:
            description: A resource's optional description.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_cloud_watch_alarm_template_group_request.CreateCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_cloud_watch_alarm_template_group_response.CreateCloudWatchAlarmTemplateGroupResponse"
        ]:
            import capo_medialive._operations.media_live.create_cloud_watch_alarm_template_group

            output, http_response = (
                capo_medialive._operations.media_live.create_cloud_watch_alarm_template_group.create_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_cloud_watch_alarm_template_group_request.CreateCloudWatchAlarmTemplateGroupRequest = {}
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cluster(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cluster_type: Optional["capo_medialive.types.cluster_type.ClusterType"] = None,
        instance_role_arn: Optional["capo_medialive.types.__string.__string"] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        network_settings: Optional[
            "capo_medialive.types.cluster_network_settings_create_request.ClusterNetworkSettingsCreateRequest"
        ] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> "capo_medialive.types.create_cluster_response.CreateClusterResponse":
        """Create a new Cluster.

        Args:
            cluster_type: Specify a type. All the Nodes that you later add to this Cluster must be this type of hardware. One Cluster instance can't contain different hardware types. You won't be able to change this parameter after you create the Cluster.
            instance_role_arn: The ARN of the IAM role for the Node in this Cluster. The role must include all the operations that you expect these Node to perform. If necessary, create a role in IAM, then attach it here.
            name: Specify a name that is unique in the AWS account. We recommend that you assign a name that hints at the types of Nodes in the Cluster. Names are case-sensitive.
            network_settings: Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with.
            request_id: The unique ID of the request.
            tags: A collection of key-value pairs.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_cluster_response.CreateClusterResponse"
        ]:
            import capo_medialive._operations.media_live.create_cluster

            output, http_response = (
                capo_medialive._operations.media_live.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_cluster_request.CreateClusterRequest = {}
        if cluster_type is not None:
            input_["cluster_type"] = cluster_type
        if instance_role_arn is not None:
            input_["instance_role_arn"] = instance_role_arn
        if name is not None:
            input_["name"] = name
        if network_settings is not None:
            input_["network_settings"] = network_settings
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_bridge_rule_template(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        event_targets: Optional[
            "capo_medialive.types.__list_of_event_bridge_rule_template_target.__listOfEventBridgeRuleTemplateTarget"
        ] = None,
        event_type: Optional[
            "capo_medialive.types.event_bridge_rule_template_event_type.EventBridgeRuleTemplateEventType"
        ] = None,
        group_identifier: Optional[
            "capo_medialive.types.__string_pattern_s.__stringPatternS"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        tags: Optional["capo_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "capo_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "capo_medialive.types.create_event_bridge_rule_template_response.CreateEventBridgeRuleTemplateResponse":
        """Creates an eventbridge rule template to monitor events and send notifications to your targeted resources.

        Args:
            description: A resource's optional description.
            group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_event_bridge_rule_template_request.CreateEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_event_bridge_rule_template_response.CreateEventBridgeRuleTemplateResponse"
        ]:
            import capo_medialive._operations.media_live.create_event_bridge_rule_template

            output, http_response = (
                capo_medialive._operations.media_live.create_event_bridge_rule_template.create_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_event_bridge_rule_template_request.CreateEventBridgeRuleTemplateRequest = {}
        if description is not None:
            input_["description"] = description
        if event_targets is not None:
            input_["event_targets"] = event_targets
        if event_type is not None:
            input_["event_type"] = event_type
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event_bridge_rule_template_group(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        tags: Optional["capo_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "capo_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "capo_medialive.types.create_event_bridge_rule_template_group_response.CreateEventBridgeRuleTemplateGroupResponse":
        """Creates an eventbridge rule template group to group your eventbridge rule templates and to attach to signal maps for dynamically creating notification rules.

        Args:
            description: A resource's optional description.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_event_bridge_rule_template_group_request.CreateEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_event_bridge_rule_template_group_response.CreateEventBridgeRuleTemplateGroupResponse"
        ]:
            import capo_medialive._operations.media_live.create_event_bridge_rule_template_group

            output, http_response = (
                capo_medialive._operations.media_live.create_event_bridge_rule_template_group.create_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_event_bridge_rule_template_group_request.CreateEventBridgeRuleTemplateGroupRequest = {}
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_input(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        destinations: Optional[
            "capo_medialive.types.__list_of_input_destination_request.__listOfInputDestinationRequest"
        ] = None,
        input_devices: Optional[
            "capo_medialive.types.__list_of_input_device_settings.__listOfInputDeviceSettings"
        ] = None,
        input_security_groups: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        media_connect_flows: Optional[
            "capo_medialive.types.__list_of_media_connect_flow_request.__listOfMediaConnectFlowRequest"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        role_arn: Optional["capo_medialive.types.__string.__string"] = None,
        sources: Optional[
            "capo_medialive.types.__list_of_input_source_request.__listOfInputSourceRequest"
        ] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
        type: Optional["capo_medialive.types.input_type.InputType"] = None,
        vpc: Optional["capo_medialive.types.input_vpc_request.InputVpcRequest"] = None,
        srt_settings: Optional[
            "capo_medialive.types.srt_settings_request.SrtSettingsRequest"
        ] = None,
        input_network_location: Optional[
            "capo_medialive.types.input_network_location.InputNetworkLocation"
        ] = None,
        multicast_settings: Optional[
            "capo_medialive.types.multicast_settings_create_request.MulticastSettingsCreateRequest"
        ] = None,
        smpte2110_receiver_group_settings: Optional[
            "capo_medialive.types.smpte2110_receiver_group_settings.Smpte2110ReceiverGroupSettings"
        ] = None,
        sdi_sources: Optional[
            "capo_medialive.types.input_sdi_sources.InputSdiSources"
        ] = None,
        router_settings: Optional[
            "capo_medialive.types.router_settings.RouterSettings"
        ] = None,
    ) -> "capo_medialive.types.create_input_response.CreateInputResponse":
        """Create an input

        Args:
            destinations: Destination settings for PUSH type inputs.
            input_devices: Settings for the devices.
            input_security_groups: A list of security groups referenced by IDs to attach to the input.
            media_connect_flows: A list of the MediaConnect Flows that you want to use in this input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.
            name: Name of the input.
            request_id: Unique identifier of the request to ensure the request is handled exactly once in case of retries.
            role_arn: The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
            sources: The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.
            tags: A collection of key-value pairs.
            srt_settings: The settings associated with an SRT input.
            input_network_location: The location of this input. AWS, for an input existing in the AWS Cloud, On-Prem for an input in a customer network.
            multicast_settings: Multicast Input settings.
            smpte2110_receiver_group_settings: Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_input_request.CreateInputRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_input_response.CreateInputResponse"
        ]:
            import capo_medialive._operations.media_live.create_input

            output, http_response = (
                capo_medialive._operations.media_live.create_input.create_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_input_request.CreateInputRequest = {}
        if destinations is not None:
            input_["destinations"] = destinations
        if input_devices is not None:
            input_["input_devices"] = input_devices
        if input_security_groups is not None:
            input_["input_security_groups"] = input_security_groups
        if media_connect_flows is not None:
            input_["media_connect_flows"] = media_connect_flows
        if name is not None:
            input_["name"] = name
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if sources is not None:
            input_["sources"] = sources
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type
        if vpc is not None:
            input_["vpc"] = vpc
        if srt_settings is not None:
            input_["srt_settings"] = srt_settings
        if input_network_location is not None:
            input_["input_network_location"] = input_network_location
        if multicast_settings is not None:
            input_["multicast_settings"] = multicast_settings
        if smpte2110_receiver_group_settings is not None:
            input_["smpte2110_receiver_group_settings"] = (
                smpte2110_receiver_group_settings
            )
        if sdi_sources is not None:
            input_["sdi_sources"] = sdi_sources
        if router_settings is not None:
            input_["router_settings"] = router_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_input_security_group(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
        whitelist_rules: Optional[
            "capo_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
        ] = None,
    ) -> "capo_medialive.types.create_input_security_group_response.CreateInputSecurityGroupResponse":
        """Creates a Input Security Group

        Args:
            tags: A collection of key-value pairs.
            whitelist_rules: List of IPv4 CIDR addresses to whitelist

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_input_security_group_request.CreateInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_input_security_group_response.CreateInputSecurityGroupResponse"
        ]:
            import capo_medialive._operations.media_live.create_input_security_group

            output, http_response = (
                capo_medialive._operations.media_live.create_input_security_group.create_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_input_security_group_request.CreateInputSecurityGroupRequest = {}
        if tags is not None:
            input_["tags"] = tags
        if whitelist_rules is not None:
            input_["whitelist_rules"] = whitelist_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_multiplex(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        availability_zones: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        multiplex_settings: Optional[
            "capo_medialive.types.multiplex_settings.MultiplexSettings"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> "capo_medialive.types.create_multiplex_response.CreateMultiplexResponse":
        """Create a new multiplex.

        Args:
            availability_zones: A list of availability zones for the multiplex. You must specify exactly two.
            multiplex_settings: Configuration for a multiplex event.
            name: Name of multiplex.
            request_id: Unique request ID. This prevents retries from creating multiple resources.
            tags: A collection of key-value pairs.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_multiplex_request.CreateMultiplexRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_multiplex_response.CreateMultiplexResponse"
        ]:
            import capo_medialive._operations.media_live.create_multiplex

            output, http_response = (
                capo_medialive._operations.media_live.create_multiplex.create_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_multiplex_request.CreateMultiplexRequest = {}
        if availability_zones is not None:
            input_["availability_zones"] = availability_zones
        if multiplex_settings is not None:
            input_["multiplex_settings"] = multiplex_settings
        if name is not None:
            input_["name"] = name
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_multiplex_program(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        multiplex_program_settings: Optional[
            "capo_medialive.types.multiplex_program_settings.MultiplexProgramSettings"
        ] = None,
        program_name: Optional["capo_medialive.types.__string.__string"] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.create_multiplex_program_response.CreateMultiplexProgramResponse":
        """Create a new program in the multiplex.

        Args:
            multiplex_id: ID of the multiplex where the program is to be created.
            multiplex_program_settings: The settings for this multiplex program.
            program_name: Name of multiplex program.
            request_id: Unique request ID. This prevents retries from creating multiple resources.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_multiplex_program_request.CreateMultiplexProgramRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_multiplex_program_response.CreateMultiplexProgramResponse"
        ]:
            import capo_medialive._operations.media_live.create_multiplex_program

            output, http_response = (
                capo_medialive._operations.media_live.create_multiplex_program.create_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_multiplex_program_request.CreateMultiplexProgramRequest = {
            "multiplex_id": multiplex_id
        }
        if multiplex_program_settings is not None:
            input_["multiplex_program_settings"] = multiplex_program_settings
        if program_name is not None:
            input_["program_name"] = program_name
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_network(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        ip_pools: Optional[
            "capo_medialive.types.__list_of_ip_pool_create_request.__listOfIpPoolCreateRequest"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        routes: Optional[
            "capo_medialive.types.__list_of_route_create_request.__listOfRouteCreateRequest"
        ] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> "capo_medialive.types.create_network_response.CreateNetworkResponse":
        """Create as many Networks as you need. You will associate one or more Clusters with each Network.Each Network provides MediaLive Anywhere with required information about the network in your organization that you are using for video encoding using MediaLive.

        Args:
            ip_pools: An array of IpPoolCreateRequests that identify a collection of IP addresses in your network that you want to reserve for use in MediaLive Anywhere. MediaLiveAnywhere uses these IP addresses for Push inputs (in both Bridge and NATnetworks) and for output destinations (only in Bridge networks). EachIpPoolUpdateRequest specifies one CIDR block.
            name: Specify a name that is unique in the AWS account. We recommend that you assign a name that hints at the type of traffic on the network. Names are case-sensitive.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            routes: An array of routes that MediaLive Anywhere needs to know about in order to route encoding traffic.
            tags: A collection of key-value pairs.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_network_request.CreateNetworkRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_network_response.CreateNetworkResponse"
        ]:
            import capo_medialive._operations.media_live.create_network

            output, http_response = (
                capo_medialive._operations.media_live.create_network.create_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_network_request.CreateNetworkRequest = {}
        if ip_pools is not None:
            input_["ip_pools"] = ip_pools
        if name is not None:
            input_["name"] = name
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if routes is not None:
            input_["routes"] = routes
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_node(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        node_interface_mappings: Optional[
            "capo_medialive.types.__list_of_node_interface_mapping_create_request.__listOfNodeInterfaceMappingCreateRequest"
        ] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        role: Optional["capo_medialive.types.node_role.NodeRole"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> "capo_medialive.types.create_node_response.CreateNodeResponse":
        """Create a Node in the specified Cluster. You can also create Nodes using the CreateNodeRegistrationScript. Note that you can't move a Node to another Cluster.

        Args:
            cluster_id: The ID of the cluster.
            name: The user-specified name of the Node to be created.
            node_interface_mappings: Documentation update needed
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            role: The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails.
            tags: A collection of key-value pairs.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_node_request.CreateNodeRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_node_response.CreateNodeResponse"
        ]:
            import capo_medialive._operations.media_live.create_node

            output, http_response = (
                capo_medialive._operations.media_live.create_node.create_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_node_request.CreateNodeRequest = {
            "cluster_id": cluster_id
        }
        if name is not None:
            input_["name"] = name
        if node_interface_mappings is not None:
            input_["node_interface_mappings"] = node_interface_mappings
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if role is not None:
            input_["role"] = role
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_node_registration_script(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        id: Optional["capo_medialive.types.__string.__string"] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        node_interface_mappings: Optional[
            "capo_medialive.types.__list_of_node_interface_mapping.__listOfNodeInterfaceMapping"
        ] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        role: Optional["capo_medialive.types.node_role.NodeRole"] = None,
    ) -> "capo_medialive.types.create_node_registration_script_response.CreateNodeRegistrationScriptResponse":
        """Create the Register Node script for all the nodes intended for a specific Cluster. You will then run the script on each hardware unit that is intended for that Cluster. The script creates a Node in the specified Cluster. It then binds the Node to this hardware unit, and activates the node hardware for use with MediaLive Anywhere.

        Args:
            cluster_id: The ID of the cluster
            id: If you're generating a re-registration script for an already existing node, this is where you provide the id.
            name: Specify a pattern for MediaLive Anywhere to use to assign a name to each Node in the Cluster. The pattern can include the variables $hn (hostname of the node hardware) and $ts for the date and time that the Node is created, in UTC (for example, 2024-08-20T23:35:12Z).
            node_interface_mappings: Documentation update needed
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            role: The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_node_registration_script_request.CreateNodeRegistrationScriptRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_node_registration_script_response.CreateNodeRegistrationScriptResponse"
        ]:
            import capo_medialive._operations.media_live.create_node_registration_script

            output, http_response = (
                capo_medialive._operations.media_live.create_node_registration_script.create_node_registration_script(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_node_registration_script_request.CreateNodeRegistrationScriptRequest = {
            "cluster_id": cluster_id
        }
        if id is not None:
            input_["id"] = id
        if name is not None:
            input_["name"] = name
        if node_interface_mappings is not None:
            input_["node_interface_mappings"] = node_interface_mappings
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if role is not None:
            input_["role"] = role

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_partner_input(
        self,
        input_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> (
        "capo_medialive.types.create_partner_input_response.CreatePartnerInputResponse"
    ):
        """Create a partner input

        Args:
            input_id: Unique ID of the input.
            request_id: Unique identifier of the request to ensure the request is handled exactly once in case of retries.
            tags: A collection of key-value pairs.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_partner_input_request.CreatePartnerInputRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_partner_input_response.CreatePartnerInputResponse"
        ]:
            import capo_medialive._operations.media_live.create_partner_input

            output, http_response = (
                capo_medialive._operations.media_live.create_partner_input.create_partner_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_partner_input_request.CreatePartnerInputRequest = {
            "input_id": input_id
        }
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_sdi_source(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        mode: Optional["capo_medialive.types.sdi_source_mode.SdiSourceMode"] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
        type: Optional["capo_medialive.types.sdi_source_type.SdiSourceType"] = None,
    ) -> "capo_medialive.types.create_sdi_source_response.CreateSdiSourceResponse":
        """Create an SdiSource for each video source that uses the SDI protocol. You will reference the SdiSource when you create an SDI input in MediaLive. You will also reference it in an SdiSourceMapping, in order to create a connection between the logical SdiSource and the physical SDI card and port that the physical SDI source uses.

        Args:
            mode: Applies only if the type is QUAD. Specify the mode for handling the quad-link signal: QUADRANT or INTERLEAVE.
            name: Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.
            tags: A collection of key-value pairs.
            type: Specify the type of the SDI source: SINGLE: The source is a single-link source. QUAD: The source is one part of a quad-link source.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_sdi_source_request.CreateSdiSourceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_sdi_source_response.CreateSdiSourceResponse"
        ]:
            import capo_medialive._operations.media_live.create_sdi_source

            output, http_response = (
                capo_medialive._operations.media_live.create_sdi_source.create_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_sdi_source_request.CreateSdiSourceRequest = {}
        if mode is not None:
            input_["mode"] = mode
        if name is not None:
            input_["name"] = name
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if tags is not None:
            input_["tags"] = tags
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_signal_map(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifiers: Optional[
            "capo_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        discovery_entry_point_arn: Optional[
            "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
        ] = None,
        event_bridge_rule_template_group_identifiers: Optional[
            "capo_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        tags: Optional["capo_medialive.types.tag_map.TagMap"] = None,
        request_id: Optional[
            "capo_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
        ] = None,
    ) -> "capo_medialive.types.create_signal_map_response.CreateSignalMapResponse":
        """Initiates the creation of a new signal map. Will discover a new mediaResourceMap based on the provided discoveryEntryPointArn.

        Args:
            description: A resource's optional description.
            discovery_entry_point_arn: A top-level supported AWS resource ARN to discovery a signal map from.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            request_id: An ID that you assign to a create request. This ID ensures idempotency when creating resources.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_signal_map_request.CreateSignalMapRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.create_signal_map_response.CreateSignalMapResponse"
        ]:
            import capo_medialive._operations.media_live.create_signal_map

            output, http_response = (
                capo_medialive._operations.media_live.create_signal_map.create_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_signal_map_request.CreateSignalMapRequest = {}
        if cloud_watch_alarm_template_group_identifiers is not None:
            input_["cloud_watch_alarm_template_group_identifiers"] = (
                cloud_watch_alarm_template_group_identifiers
            )
        if description is not None:
            input_["description"] = description
        if discovery_entry_point_arn is not None:
            input_["discovery_entry_point_arn"] = discovery_entry_point_arn
        if event_bridge_rule_template_group_identifiers is not None:
            input_["event_bridge_rule_template_group_identifiers"] = (
                event_bridge_rule_template_group_identifiers
            )
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_tags(
        self,
        resource_arn: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> None:
        """Create tags for a resource

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.create_tags_request.CreateTagsRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.create_tags

            output, http_response = (
                capo_medialive._operations.media_live.create_tags.create_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.create_tags_request.CreateTagsRequest = {
            "resource_arn": resource_arn
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

    def delete_channel(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_channel_response.DeleteChannelResponse":
        """Starts deletion of channel. The associated outputs are also deleted.

        Args:
            channel_id: Unique ID of the channel.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_channel_request.DeleteChannelRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_channel_response.DeleteChannelResponse"
        ]:
            import capo_medialive._operations.media_live.delete_channel

            output, http_response = (
                capo_medialive._operations.media_live.delete_channel.delete_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_channel_request.DeleteChannelRequest = {
            "channel_id": channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_channel_placement_group(
        self,
        channel_placement_group_id: "capo_medialive.types.__string.__string",
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_channel_placement_group_response.DeleteChannelPlacementGroupResponse":
        """Delete the specified ChannelPlacementGroup that exists in the specified Cluster.

        Args:
            channel_placement_group_id: The ID of the channel placement group.
            cluster_id: The ID of the cluster.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_channel_placement_group_request.DeleteChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_channel_placement_group_response.DeleteChannelPlacementGroupResponse"
        ]:
            import capo_medialive._operations.media_live.delete_channel_placement_group

            output, http_response = (
                capo_medialive._operations.media_live.delete_channel_placement_group.delete_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_channel_placement_group_request.DeleteChannelPlacementGroupRequest = {
            "channel_placement_group_id": channel_placement_group_id,
            "cluster_id": cluster_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cloud_watch_alarm_template(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes a cloudwatch alarm template.

        Args:
            identifier: A cloudwatch alarm template's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_cloud_watch_alarm_template_request.DeleteCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.delete_cloud_watch_alarm_template

            output, http_response = (
                capo_medialive._operations.media_live.delete_cloud_watch_alarm_template.delete_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_cloud_watch_alarm_template_request.DeleteCloudWatchAlarmTemplateRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cloud_watch_alarm_template_group(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes a cloudwatch alarm template group. You must detach this group from all signal maps and ensure its existing templates are moved to another group or deleted.

        Args:
            identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_cloud_watch_alarm_template_group_request.DeleteCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.delete_cloud_watch_alarm_template_group

            output, http_response = (
                capo_medialive._operations.media_live.delete_cloud_watch_alarm_template_group.delete_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_cloud_watch_alarm_template_group_request.DeleteCloudWatchAlarmTemplateGroupRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_cluster(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_cluster_response.DeleteClusterResponse":
        """Delete a Cluster. The Cluster must be idle.

        Args:
            cluster_id: The ID of the cluster.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_cluster_request.DeleteClusterRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_cluster_response.DeleteClusterResponse"
        ]:
            import capo_medialive._operations.media_live.delete_cluster

            output, http_response = (
                capo_medialive._operations.media_live.delete_cluster.delete_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_cluster_request.DeleteClusterRequest = {
            "cluster_id": cluster_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_bridge_rule_template(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes an eventbridge rule template.

        Args:
            identifier: An eventbridge rule template's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_event_bridge_rule_template_request.DeleteEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.delete_event_bridge_rule_template

            output, http_response = (
                capo_medialive._operations.media_live.delete_event_bridge_rule_template.delete_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_event_bridge_rule_template_request.DeleteEventBridgeRuleTemplateRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event_bridge_rule_template_group(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes an eventbridge rule template group. You must detach this group from all signal maps and ensure its existing templates are moved to another group or deleted.

        Args:
            identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_event_bridge_rule_template_group_request.DeleteEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.delete_event_bridge_rule_template_group

            output, http_response = (
                capo_medialive._operations.media_live.delete_event_bridge_rule_template_group.delete_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_event_bridge_rule_template_group_request.DeleteEventBridgeRuleTemplateGroupRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_input(
        self,
        input_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_input_response.DeleteInputResponse":
        """Deletes the input end point

        Args:
            input_id: Unique ID of the input

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_input_request.DeleteInputRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_input_response.DeleteInputResponse"
        ]:
            import capo_medialive._operations.media_live.delete_input

            output, http_response = (
                capo_medialive._operations.media_live.delete_input.delete_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_input_request.DeleteInputRequest = {
            "input_id": input_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_input_security_group(
        self,
        input_security_group_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_input_security_group_response.DeleteInputSecurityGroupResponse":
        """Deletes an Input Security Group

        Args:
            input_security_group_id: The Input Security Group to delete

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_input_security_group_request.DeleteInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_input_security_group_response.DeleteInputSecurityGroupResponse"
        ]:
            import capo_medialive._operations.media_live.delete_input_security_group

            output, http_response = (
                capo_medialive._operations.media_live.delete_input_security_group.delete_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_input_security_group_request.DeleteInputSecurityGroupRequest = {
            "input_security_group_id": input_security_group_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_multiplex(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_multiplex_response.DeleteMultiplexResponse":
        """Delete a multiplex. The multiplex must be idle.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_multiplex_request.DeleteMultiplexRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_multiplex_response.DeleteMultiplexResponse"
        ]:
            import capo_medialive._operations.media_live.delete_multiplex

            output, http_response = (
                capo_medialive._operations.media_live.delete_multiplex.delete_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_multiplex_request.DeleteMultiplexRequest = {
            "multiplex_id": multiplex_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_multiplex_program(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        program_name: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_multiplex_program_response.DeleteMultiplexProgramResponse":
        """Delete a program from a multiplex.

        Args:
            multiplex_id: The ID of the multiplex that the program belongs to.
            program_name: The multiplex program name.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_multiplex_program_request.DeleteMultiplexProgramRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_multiplex_program_response.DeleteMultiplexProgramResponse"
        ]:
            import capo_medialive._operations.media_live.delete_multiplex_program

            output, http_response = (
                capo_medialive._operations.media_live.delete_multiplex_program.delete_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_multiplex_program_request.DeleteMultiplexProgramRequest = {
            "multiplex_id": multiplex_id,
            "program_name": program_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_network(
        self,
        network_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_network_response.DeleteNetworkResponse":
        """Delete a Network. The Network must have no resources associated with it.

        Args:
            network_id: The ID of the network.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_network_request.DeleteNetworkRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_network_response.DeleteNetworkResponse"
        ]:
            import capo_medialive._operations.media_live.delete_network

            output, http_response = (
                capo_medialive._operations.media_live.delete_network.delete_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_network_request.DeleteNetworkRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_node(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        node_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_node_response.DeleteNodeResponse":
        """Delete a Node. The Node must be IDLE.

        Args:
            cluster_id: The ID of the cluster
            node_id: The ID of the node.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_node_request.DeleteNodeRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_node_response.DeleteNodeResponse"
        ]:
            import capo_medialive._operations.media_live.delete_node

            output, http_response = (
                capo_medialive._operations.media_live.delete_node.delete_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_node_request.DeleteNodeRequest = {
            "cluster_id": cluster_id,
            "node_id": node_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_reservation(
        self,
        reservation_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_reservation_response.DeleteReservationResponse":
        """Delete an expired reservation.

        Args:
            reservation_id: Unique reservation ID, e.g. '1234567'

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_reservation_request.DeleteReservationRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_reservation_response.DeleteReservationResponse"
        ]:
            import capo_medialive._operations.media_live.delete_reservation

            output, http_response = (
                capo_medialive._operations.media_live.delete_reservation.delete_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_reservation_request.DeleteReservationRequest = {
            "reservation_id": reservation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_schedule(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_schedule_response.DeleteScheduleResponse":
        """Delete all schedule actions on a channel.

        Args:
            channel_id: Id of the channel whose schedule is being deleted.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_schedule_request.DeleteScheduleRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_schedule_response.DeleteScheduleResponse"
        ]:
            import capo_medialive._operations.media_live.delete_schedule

            output, http_response = (
                capo_medialive._operations.media_live.delete_schedule.delete_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_schedule_request.DeleteScheduleRequest = {
            "channel_id": channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_sdi_source(
        self,
        sdi_source_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.delete_sdi_source_response.DeleteSdiSourceResponse":
        """Delete an SdiSource. The SdiSource must not be part of any SidSourceMapping and must not be attached to any input.

        Args:
            sdi_source_id: The ID of the SdiSource.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_sdi_source_request.DeleteSdiSourceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.delete_sdi_source_response.DeleteSdiSourceResponse"
        ]:
            import capo_medialive._operations.media_live.delete_sdi_source

            output, http_response = (
                capo_medialive._operations.media_live.delete_sdi_source.delete_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_sdi_source_request.DeleteSdiSourceRequest = {
            "sdi_source_id": sdi_source_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_signal_map(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> None:
        """Deletes the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_signal_map_request.DeleteSignalMapRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.delete_signal_map

            output, http_response = (
                capo_medialive._operations.media_live.delete_signal_map.delete_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_signal_map_request.DeleteSignalMapRequest = {
            "identifier": identifier
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
        resource_arn: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tag_keys: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> None:
        """Removes tags for a resource

        Args:
            tag_keys: An array of tag keys to delete

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.delete_tags_request.DeleteTagsRequest]",
        ) -> OperationResponse[None]:
            import capo_medialive._operations.media_live.delete_tags

            output, http_response = (
                capo_medialive._operations.media_live.delete_tags.delete_tags(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.delete_tags_request.DeleteTagsRequest = {
            "resource_arn": resource_arn
        }
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_configuration(
        self, *, config_overrides: Optional[MediaLiveClientConfig] = None
    ) -> "capo_medialive.types.describe_account_configuration_response.DescribeAccountConfigurationResponse":
        """Describe account configuration

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_account_configuration_request.DescribeAccountConfigurationRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_account_configuration_response.DescribeAccountConfigurationResponse"
        ]:
            import capo_medialive._operations.media_live.describe_account_configuration

            output, http_response = (
                capo_medialive._operations.media_live.describe_account_configuration.describe_account_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_account_configuration_request.DescribeAccountConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_channel_response.DescribeChannelResponse":
        """Gets details about a channel

        Args:
            channel_id: channel ID

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_channel_request.DescribeChannelRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_channel_response.DescribeChannelResponse"
        ]:
            import capo_medialive._operations.media_live.describe_channel

            output, http_response = (
                capo_medialive._operations.media_live.describe_channel.describe_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_channel_request.DescribeChannelRequest = {
            "channel_id": channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_channel_placement_group(
        self,
        channel_placement_group_id: "capo_medialive.types.__string.__string",
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_channel_placement_group_response.DescribeChannelPlacementGroupResponse":
        """Get details about a ChannelPlacementGroup.

        Args:
            channel_placement_group_id: The ID of the channel placement group.
            cluster_id: The ID of the cluster.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_channel_placement_group_request.DescribeChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_channel_placement_group_response.DescribeChannelPlacementGroupResponse"
        ]:
            import capo_medialive._operations.media_live.describe_channel_placement_group

            output, http_response = (
                capo_medialive._operations.media_live.describe_channel_placement_group.describe_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_channel_placement_group_request.DescribeChannelPlacementGroupRequest = {
            "channel_placement_group_id": channel_placement_group_id,
            "cluster_id": cluster_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_cluster(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_cluster_response.DescribeClusterResponse":
        """Get details about a Cluster.

        Args:
            cluster_id: The ID of the cluster.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_cluster_response.DescribeClusterResponse"
        ]:
            import capo_medialive._operations.media_live.describe_cluster

            output, http_response = (
                capo_medialive._operations.media_live.describe_cluster.describe_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_cluster_request.DescribeClusterRequest = {
            "cluster_id": cluster_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_input(
        self,
        input_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_input_response.DescribeInputResponse":
        """Produces details about an input

        Args:
            input_id: Unique ID of the input

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_input_request.DescribeInputRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_input_response.DescribeInputResponse"
        ]:
            import capo_medialive._operations.media_live.describe_input

            output, http_response = (
                capo_medialive._operations.media_live.describe_input.describe_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_input_request.DescribeInputRequest = {
            "input_id": input_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_input_device(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_input_device_response.DescribeInputDeviceResponse":
        """Gets the details for the input device

        Args:
            input_device_id: The unique ID of this input device. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_input_device_request.DescribeInputDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_input_device_response.DescribeInputDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.describe_input_device

            output, http_response = (
                capo_medialive._operations.media_live.describe_input_device.describe_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_input_device_request.DescribeInputDeviceRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def describe_input_device_thumbnail(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        accept: Optional["capo_medialive.types.accept_header.AcceptHeader"] = None,
    ) -> "Generator[capo_medialive.types.describe_input_device_thumbnail_response.DescribeInputDeviceThumbnailResponse]":
        """Get the latest thumbnail data for the input device.

        Args:
            input_device_id: The unique ID of this input device. For example, hd-123456789abcdef.
            accept: The HTTP Accept header. Indicates the requested type for the thumbnail.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_input_device_thumbnail_request.DescribeInputDeviceThumbnailRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_input_device_thumbnail_response.DescribeInputDeviceThumbnailResponse"
        ]:
            import capo_medialive._operations.media_live.describe_input_device_thumbnail

            output, http_response = (
                capo_medialive._operations.media_live.describe_input_device_thumbnail.describe_input_device_thumbnail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_input_device_thumbnail_request.DescribeInputDeviceThumbnailRequest = {
            "input_device_id": input_device_id
        }
        if accept is not None:
            input_["accept"] = accept

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def describe_input_security_group(
        self,
        input_security_group_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_input_security_group_response.DescribeInputSecurityGroupResponse":
        """Produces a summary of an Input Security Group

        Args:
            input_security_group_id: The id of the Input Security Group to describe

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_input_security_group_request.DescribeInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_input_security_group_response.DescribeInputSecurityGroupResponse"
        ]:
            import capo_medialive._operations.media_live.describe_input_security_group

            output, http_response = (
                capo_medialive._operations.media_live.describe_input_security_group.describe_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_input_security_group_request.DescribeInputSecurityGroupRequest = {
            "input_security_group_id": input_security_group_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_multiplex(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_multiplex_response.DescribeMultiplexResponse":
        """Gets details about a multiplex.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_multiplex_request.DescribeMultiplexRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_multiplex_response.DescribeMultiplexResponse"
        ]:
            import capo_medialive._operations.media_live.describe_multiplex

            output, http_response = (
                capo_medialive._operations.media_live.describe_multiplex.describe_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_multiplex_request.DescribeMultiplexRequest = {
            "multiplex_id": multiplex_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_multiplex_program(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        program_name: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_multiplex_program_response.DescribeMultiplexProgramResponse":
        """Get the details for a program in a multiplex.

        Args:
            multiplex_id: The ID of the multiplex that the program belongs to.
            program_name: The name of the program.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_multiplex_program_request.DescribeMultiplexProgramRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_multiplex_program_response.DescribeMultiplexProgramResponse"
        ]:
            import capo_medialive._operations.media_live.describe_multiplex_program

            output, http_response = (
                capo_medialive._operations.media_live.describe_multiplex_program.describe_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_multiplex_program_request.DescribeMultiplexProgramRequest = {
            "multiplex_id": multiplex_id,
            "program_name": program_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_network(
        self,
        network_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_network_response.DescribeNetworkResponse":
        """Get details about a Network.

        Args:
            network_id: The ID of the network.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_network_request.DescribeNetworkRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_network_response.DescribeNetworkResponse"
        ]:
            import capo_medialive._operations.media_live.describe_network

            output, http_response = (
                capo_medialive._operations.media_live.describe_network.describe_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_network_request.DescribeNetworkRequest = {
            "network_id": network_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_node(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        node_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_node_response.DescribeNodeResponse":
        """Get details about a Node in the specified Cluster.

        Args:
            cluster_id: The ID of the cluster
            node_id: The ID of the node.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_node_request.DescribeNodeRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_node_response.DescribeNodeResponse"
        ]:
            import capo_medialive._operations.media_live.describe_node

            output, http_response = (
                capo_medialive._operations.media_live.describe_node.describe_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_node_request.DescribeNodeRequest = {
            "cluster_id": cluster_id,
            "node_id": node_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_offering(
        self,
        offering_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_offering_response.DescribeOfferingResponse":
        """Get details for an offering.

        Args:
            offering_id: Unique offering ID, e.g. '87654321'

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_offering_request.DescribeOfferingRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_offering_response.DescribeOfferingResponse"
        ]:
            import capo_medialive._operations.media_live.describe_offering

            output, http_response = (
                capo_medialive._operations.media_live.describe_offering.describe_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_offering_request.DescribeOfferingRequest = {
            "offering_id": offering_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_reservation(
        self,
        reservation_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> (
        "capo_medialive.types.describe_reservation_response.DescribeReservationResponse"
    ):
        """Get details for a reservation.

        Args:
            reservation_id: Unique reservation ID, e.g. '1234567'

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_reservation_request.DescribeReservationRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_reservation_response.DescribeReservationResponse"
        ]:
            import capo_medialive._operations.media_live.describe_reservation

            output, http_response = (
                capo_medialive._operations.media_live.describe_reservation.describe_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_reservation_request.DescribeReservationRequest = {
            "reservation_id": reservation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_schedule(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.describe_schedule_response.DescribeScheduleResponse":
        """Get a channel schedule

        Args:
            channel_id: Id of the channel whose schedule is being updated.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_schedule_request.DescribeScheduleRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_schedule_response.DescribeScheduleResponse"
        ]:
            import capo_medialive._operations.media_live.describe_schedule

            output, http_response = (
                capo_medialive._operations.media_live.describe_schedule.describe_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_schedule_request.DescribeScheduleRequest = {
            "channel_id": channel_id
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

    def iter_describe_schedule(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.schedule_action.ScheduleAction]":
        _token = next_token
        while True:
            _response = self.describe_schedule(
                channel_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("schedule_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_sdi_source(
        self,
        sdi_source_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.describe_sdi_source_response.DescribeSdiSourceResponse":
        """Gets details about a SdiSource.

        Args:
            sdi_source_id: Get details about an SdiSource.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_sdi_source_request.DescribeSdiSourceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_sdi_source_response.DescribeSdiSourceResponse"
        ]:
            import capo_medialive._operations.media_live.describe_sdi_source

            output, http_response = (
                capo_medialive._operations.media_live.describe_sdi_source.describe_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_sdi_source_request.DescribeSdiSourceRequest = {
            "sdi_source_id": sdi_source_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_thumbnails(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        pipeline_id: Optional["capo_medialive.types.__string.__string"] = None,
        thumbnail_type: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.describe_thumbnails_response.DescribeThumbnailsResponse":
        """Describe the latest thumbnails data.

        Args:
            channel_id: Unique ID of the channel
            pipeline_id: Pipeline ID ("0" or "1")
            thumbnail_type: thumbnail type

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.describe_thumbnails_request.DescribeThumbnailsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.describe_thumbnails_response.DescribeThumbnailsResponse"
        ]:
            import capo_medialive._operations.media_live.describe_thumbnails

            output, http_response = (
                capo_medialive._operations.media_live.describe_thumbnails.describe_thumbnails(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.describe_thumbnails_request.DescribeThumbnailsRequest = {
            "channel_id": channel_id
        }
        if pipeline_id is not None:
            input_["pipeline_id"] = pipeline_id
        if thumbnail_type is not None:
            input_["thumbnail_type"] = thumbnail_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cloud_watch_alarm_template(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.get_cloud_watch_alarm_template_response.GetCloudWatchAlarmTemplateResponse":
        """Retrieves the specified cloudwatch alarm template.

        Args:
            identifier: A cloudwatch alarm template's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.get_cloud_watch_alarm_template_request.GetCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.get_cloud_watch_alarm_template_response.GetCloudWatchAlarmTemplateResponse"
        ]:
            import capo_medialive._operations.media_live.get_cloud_watch_alarm_template

            output, http_response = (
                capo_medialive._operations.media_live.get_cloud_watch_alarm_template.get_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.get_cloud_watch_alarm_template_request.GetCloudWatchAlarmTemplateRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_cloud_watch_alarm_template_group(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.get_cloud_watch_alarm_template_group_response.GetCloudWatchAlarmTemplateGroupResponse":
        """Retrieves the specified cloudwatch alarm template group.

        Args:
            identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.get_cloud_watch_alarm_template_group_request.GetCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.get_cloud_watch_alarm_template_group_response.GetCloudWatchAlarmTemplateGroupResponse"
        ]:
            import capo_medialive._operations.media_live.get_cloud_watch_alarm_template_group

            output, http_response = (
                capo_medialive._operations.media_live.get_cloud_watch_alarm_template_group.get_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.get_cloud_watch_alarm_template_group_request.GetCloudWatchAlarmTemplateGroupRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_bridge_rule_template(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.get_event_bridge_rule_template_response.GetEventBridgeRuleTemplateResponse":
        """Retrieves the specified eventbridge rule template.

        Args:
            identifier: An eventbridge rule template's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.get_event_bridge_rule_template_request.GetEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.get_event_bridge_rule_template_response.GetEventBridgeRuleTemplateResponse"
        ]:
            import capo_medialive._operations.media_live.get_event_bridge_rule_template

            output, http_response = (
                capo_medialive._operations.media_live.get_event_bridge_rule_template.get_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.get_event_bridge_rule_template_request.GetEventBridgeRuleTemplateRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event_bridge_rule_template_group(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse":
        """Retrieves the specified eventbridge rule template group.

        Args:
            identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.get_event_bridge_rule_template_group_response.GetEventBridgeRuleTemplateGroupResponse"
        ]:
            import capo_medialive._operations.media_live.get_event_bridge_rule_template_group

            output, http_response = (
                capo_medialive._operations.media_live.get_event_bridge_rule_template_group.get_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.get_event_bridge_rule_template_group_request.GetEventBridgeRuleTemplateGroupRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_signal_map(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.get_signal_map_response.GetSignalMapResponse":
        """Retrieves the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.get_signal_map_request.GetSignalMapRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.get_signal_map_response.GetSignalMapResponse"
        ]:
            import capo_medialive._operations.media_live.get_signal_map

            output, http_response = (
                capo_medialive._operations.media_live.get_signal_map.get_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.get_signal_map_request.GetSignalMapRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_alerts(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        state_filter: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_alerts_response.ListAlertsResponse":
        """List the alerts for a channel with optional filtering based on alert state.

        Args:
            channel_id: The unique ID of the channel
            max_results: The maximum number of items to return
            next_token: The next pagination token
            state_filter: Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_alerts_request.ListAlertsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_alerts_response.ListAlertsResponse"
        ]:
            import capo_medialive._operations.media_live.list_alerts

            output, http_response = (
                capo_medialive._operations.media_live.list_alerts.list_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_alerts_request.ListAlertsRequest = {
            "channel_id": channel_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state_filter is not None:
            input_["state_filter"] = state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_alerts(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        state_filter: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.channel_alert.ChannelAlert]":
        _token = next_token
        while True:
            _response = self.list_alerts(
                channel_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state_filter=state_filter,
            )
            _page = _resolve_path(_response, ("alerts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channel_placement_groups(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_channel_placement_groups_response.ListChannelPlacementGroupsResponse":
        """Retrieve the list of ChannelPlacementGroups in the specified Cluster.

        Args:
            cluster_id: The ID of the cluster
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_channel_placement_groups_request.ListChannelPlacementGroupsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_channel_placement_groups_response.ListChannelPlacementGroupsResponse"
        ]:
            import capo_medialive._operations.media_live.list_channel_placement_groups

            output, http_response = (
                capo_medialive._operations.media_live.list_channel_placement_groups.list_channel_placement_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_channel_placement_groups_request.ListChannelPlacementGroupsRequest = {
            "cluster_id": cluster_id
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

    def iter_list_channel_placement_groups(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.describe_channel_placement_group_summary.DescribeChannelPlacementGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_channel_placement_groups(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channel_placement_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_channels(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_channels_response.ListChannelsResponse":
        """Produces list of channels that have been created

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_channels_request.ListChannelsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_channels_response.ListChannelsResponse"
        ]:
            import capo_medialive._operations.media_live.list_channels

            output, http_response = (
                capo_medialive._operations.media_live.list_channels.list_channels(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_channels_request.ListChannelsRequest = {}
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

    def iter_list_channels(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.channel_summary.ChannelSummary]":
        _token = next_token
        while True:
            _response = self.list_channels(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("channels",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cloud_watch_alarm_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        scope: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "capo_medialive.types.list_cloud_watch_alarm_template_groups_response.ListCloudWatchAlarmTemplateGroupsResponse":
        """Lists cloudwatch alarm template groups.

        Args:
            next_token: A token used to retrieve the next set of results in paginated list responses.
            scope: Represents the scope of a resource, with options for all scopes, AWS provided resources, or local resources.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_cloud_watch_alarm_template_groups_request.ListCloudWatchAlarmTemplateGroupsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_cloud_watch_alarm_template_groups_response.ListCloudWatchAlarmTemplateGroupsResponse"
        ]:
            import capo_medialive._operations.media_live.list_cloud_watch_alarm_template_groups

            output, http_response = (
                capo_medialive._operations.media_live.list_cloud_watch_alarm_template_groups.list_cloud_watch_alarm_template_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_cloud_watch_alarm_template_groups_request.ListCloudWatchAlarmTemplateGroupsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if scope is not None:
            input_["scope"] = scope
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cloud_watch_alarm_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        scope: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_medialive.types.cloud_watch_alarm_template_group_summary.CloudWatchAlarmTemplateGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_cloud_watch_alarm_template_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                scope=scope,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("cloud_watch_alarm_template_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cloud_watch_alarm_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        scope: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "capo_medialive.types.list_cloud_watch_alarm_templates_response.ListCloudWatchAlarmTemplatesResponse":
        """Lists cloudwatch alarm templates.

        Args:
            group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            next_token: A token used to retrieve the next set of results in paginated list responses.
            scope: Represents the scope of a resource, with options for all scopes, AWS provided resources, or local resources.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_cloud_watch_alarm_templates_request.ListCloudWatchAlarmTemplatesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_cloud_watch_alarm_templates_response.ListCloudWatchAlarmTemplatesResponse"
        ]:
            import capo_medialive._operations.media_live.list_cloud_watch_alarm_templates

            output, http_response = (
                capo_medialive._operations.media_live.list_cloud_watch_alarm_templates.list_cloud_watch_alarm_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_cloud_watch_alarm_templates_request.ListCloudWatchAlarmTemplatesRequest = {}
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if scope is not None:
            input_["scope"] = scope
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cloud_watch_alarm_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        scope: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_medialive.types.cloud_watch_alarm_template_summary.CloudWatchAlarmTemplateSummary]":
        _token = next_token
        while True:
            _response = self.list_cloud_watch_alarm_templates(
                config_overrides=config_overrides,
                group_identifier=group_identifier,
                max_results=max_results,
                next_token=_token,
                scope=scope,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("cloud_watch_alarm_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_cluster_alerts(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        state_filter: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_cluster_alerts_response.ListClusterAlertsResponse":
        """List the alerts for a cluster with optional filtering based on alert state.

        Args:
            cluster_id: The unique ID of the cluster
            max_results: The maximum number of items to return
            next_token: The next pagination token
            state_filter: Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_cluster_alerts_request.ListClusterAlertsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_cluster_alerts_response.ListClusterAlertsResponse"
        ]:
            import capo_medialive._operations.media_live.list_cluster_alerts

            output, http_response = (
                capo_medialive._operations.media_live.list_cluster_alerts.list_cluster_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_cluster_alerts_request.ListClusterAlertsRequest = {
            "cluster_id": cluster_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state_filter is not None:
            input_["state_filter"] = state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cluster_alerts(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        state_filter: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.cluster_alert.ClusterAlert]":
        _token = next_token
        while True:
            _response = self.list_cluster_alerts(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state_filter=state_filter,
            )
            _page = _resolve_path(_response, ("alerts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_clusters(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_clusters_response.ListClustersResponse":
        """Retrieve the list of Clusters.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_clusters_response.ListClustersResponse"
        ]:
            import capo_medialive._operations.media_live.list_clusters

            output, http_response = (
                capo_medialive._operations.media_live.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_clusters_request.ListClustersRequest = {}
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

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> (
        "Iterator[capo_medialive.types.describe_cluster_summary.DescribeClusterSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("clusters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_bridge_rule_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "capo_medialive.types.list_event_bridge_rule_template_groups_response.ListEventBridgeRuleTemplateGroupsResponse":
        """Lists eventbridge rule template groups.

        Args:
            next_token: A token used to retrieve the next set of results in paginated list responses.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_event_bridge_rule_template_groups_request.ListEventBridgeRuleTemplateGroupsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_event_bridge_rule_template_groups_response.ListEventBridgeRuleTemplateGroupsResponse"
        ]:
            import capo_medialive._operations.media_live.list_event_bridge_rule_template_groups

            output, http_response = (
                capo_medialive._operations.media_live.list_event_bridge_rule_template_groups.list_event_bridge_rule_template_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_event_bridge_rule_template_groups_request.ListEventBridgeRuleTemplateGroupsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_event_bridge_rule_template_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_medialive.types.event_bridge_rule_template_group_summary.EventBridgeRuleTemplateGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_event_bridge_rule_template_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("event_bridge_rule_template_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_event_bridge_rule_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "capo_medialive.types.list_event_bridge_rule_templates_response.ListEventBridgeRuleTemplatesResponse":
        """Lists eventbridge rule templates.

        Args:
            group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            next_token: A token used to retrieve the next set of results in paginated list responses.
            signal_map_identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_event_bridge_rule_templates_request.ListEventBridgeRuleTemplatesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_event_bridge_rule_templates_response.ListEventBridgeRuleTemplatesResponse"
        ]:
            import capo_medialive._operations.media_live.list_event_bridge_rule_templates

            output, http_response = (
                capo_medialive._operations.media_live.list_event_bridge_rule_templates.list_event_bridge_rule_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_event_bridge_rule_templates_request.ListEventBridgeRuleTemplatesRequest = {}
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if signal_map_identifier is not None:
            input_["signal_map_identifier"] = signal_map_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_event_bridge_rule_templates(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        group_identifier: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        signal_map_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
    ) -> "Iterator[capo_medialive.types.event_bridge_rule_template_summary.EventBridgeRuleTemplateSummary]":
        _token = next_token
        while True:
            _response = self.list_event_bridge_rule_templates(
                config_overrides=config_overrides,
                group_identifier=group_identifier,
                max_results=max_results,
                next_token=_token,
                signal_map_identifier=signal_map_identifier,
            )
            _page = _resolve_path(_response, ("event_bridge_rule_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_devices(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_input_devices_response.ListInputDevicesResponse":
        """List input devices

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_input_devices_request.ListInputDevicesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_input_devices_response.ListInputDevicesResponse"
        ]:
            import capo_medialive._operations.media_live.list_input_devices

            output, http_response = (
                capo_medialive._operations.media_live.list_input_devices.list_input_devices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_input_devices_request.ListInputDevicesRequest = {}
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

    def iter_list_input_devices(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.input_device_summary.InputDeviceSummary]":
        _token = next_token
        while True:
            _response = self.list_input_devices(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_devices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_device_transfers(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        transfer_type: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_input_device_transfers_response.ListInputDeviceTransfersResponse":
        """List input devices that are currently being transferred. List input devices that you are transferring from your AWS account or input devices that another AWS account is transferring to you.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_input_device_transfers_request.ListInputDeviceTransfersRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_input_device_transfers_response.ListInputDeviceTransfersResponse"
        ]:
            import capo_medialive._operations.media_live.list_input_device_transfers

            output, http_response = (
                capo_medialive._operations.media_live.list_input_device_transfers.list_input_device_transfers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_input_device_transfers_request.ListInputDeviceTransfersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if transfer_type is not None:
            input_["transfer_type"] = transfer_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_input_device_transfers(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        transfer_type: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.transferring_input_device_summary.TransferringInputDeviceSummary]":
        _token = next_token
        while True:
            _response = self.list_input_device_transfers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                transfer_type=transfer_type,
            )
            _page = _resolve_path(_response, ("input_device_transfers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_inputs(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_inputs_response.ListInputsResponse":
        """Produces list of inputs that have been created

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_inputs_request.ListInputsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_inputs_response.ListInputsResponse"
        ]:
            import capo_medialive._operations.media_live.list_inputs

            output, http_response = (
                capo_medialive._operations.media_live.list_inputs.list_inputs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_inputs_request.ListInputsRequest = {}
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

    def iter_list_inputs(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.input.Input]":
        _token = next_token
        while True:
            _response = self.list_inputs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("inputs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_security_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_input_security_groups_response.ListInputSecurityGroupsResponse":
        """Produces a list of Input Security Groups for an account

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_input_security_groups_request.ListInputSecurityGroupsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_input_security_groups_response.ListInputSecurityGroupsResponse"
        ]:
            import capo_medialive._operations.media_live.list_input_security_groups

            output, http_response = (
                capo_medialive._operations.media_live.list_input_security_groups.list_input_security_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_input_security_groups_request.ListInputSecurityGroupsRequest = {}
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

    def iter_list_input_security_groups(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.input_security_group.InputSecurityGroup]":
        _token = next_token
        while True:
            _response = self.list_input_security_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_security_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_multiplex_alerts(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        state_filter: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_multiplex_alerts_response.ListMultiplexAlertsResponse":
        """List the alerts for a multiplex with optional filtering based on alert state.

        Args:
            max_results: The maximum number of items to return
            multiplex_id: The unique ID of the multiplex
            next_token: The next pagination token
            state_filter: Specifies the set of alerts to return based on their state. SET - Return only alerts with SET state. CLEARED - Return only alerts with CLEARED state. ALL - Return all alerts.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_multiplex_alerts_request.ListMultiplexAlertsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_multiplex_alerts_response.ListMultiplexAlertsResponse"
        ]:
            import capo_medialive._operations.media_live.list_multiplex_alerts

            output, http_response = (
                capo_medialive._operations.media_live.list_multiplex_alerts.list_multiplex_alerts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_multiplex_alerts_request.ListMultiplexAlertsRequest = {
            "multiplex_id": multiplex_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state_filter is not None:
            input_["state_filter"] = state_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_multiplex_alerts(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        state_filter: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.multiplex_alert.MultiplexAlert]":
        _token = next_token
        while True:
            _response = self.list_multiplex_alerts(
                multiplex_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state_filter=state_filter,
            )
            _page = _resolve_path(_response, ("alerts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_multiplexes(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_multiplexes_response.ListMultiplexesResponse":
        """Retrieve a list of the existing multiplexes.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_multiplexes_request.ListMultiplexesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_multiplexes_response.ListMultiplexesResponse"
        ]:
            import capo_medialive._operations.media_live.list_multiplexes

            output, http_response = (
                capo_medialive._operations.media_live.list_multiplexes.list_multiplexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_multiplexes_request.ListMultiplexesRequest = {}
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

    def iter_list_multiplexes(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.multiplex_summary.MultiplexSummary]":
        _token = next_token
        while True:
            _response = self.list_multiplexes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("multiplexes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_multiplex_programs(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_multiplex_programs_response.ListMultiplexProgramsResponse":
        """List the programs that currently exist for a specific multiplex.

        Args:
            max_results: The maximum number of items to return.
            multiplex_id: The ID of the multiplex that the programs belong to.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_multiplex_programs_request.ListMultiplexProgramsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_multiplex_programs_response.ListMultiplexProgramsResponse"
        ]:
            import capo_medialive._operations.media_live.list_multiplex_programs

            output, http_response = (
                capo_medialive._operations.media_live.list_multiplex_programs.list_multiplex_programs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_multiplex_programs_request.ListMultiplexProgramsRequest = {
            "multiplex_id": multiplex_id
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

    def iter_list_multiplex_programs(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.multiplex_program_summary.MultiplexProgramSummary]":
        _token = next_token
        while True:
            _response = self.list_multiplex_programs(
                multiplex_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("multiplex_programs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_networks(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_networks_response.ListNetworksResponse":
        """Retrieve the list of Networks.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_networks_request.ListNetworksRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_networks_response.ListNetworksResponse"
        ]:
            import capo_medialive._operations.media_live.list_networks

            output, http_response = (
                capo_medialive._operations.media_live.list_networks.list_networks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_networks_request.ListNetworksRequest = {}
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

    def iter_list_networks(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> (
        "Iterator[capo_medialive.types.describe_network_summary.DescribeNetworkSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_networks(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("networks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_nodes(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_nodes_response.ListNodesResponse":
        """Retrieve the list of Nodes.

        Args:
            cluster_id: The ID of the cluster
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_nodes_request.ListNodesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_nodes_response.ListNodesResponse"
        ]:
            import capo_medialive._operations.media_live.list_nodes

            output, http_response = (
                capo_medialive._operations.media_live.list_nodes.list_nodes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_nodes_request.ListNodesRequest = {
            "cluster_id": cluster_id
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

    def iter_list_nodes(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.describe_node_summary.DescribeNodeSummary]":
        _token = next_token
        while True:
            _response = self.list_nodes(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_offerings(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["capo_medialive.types.__string.__string"] = None,
        channel_configuration: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
        codec: Optional["capo_medialive.types.__string.__string"] = None,
        duration: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["capo_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["capo_medialive.types.__string.__string"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        resolution: Optional["capo_medialive.types.__string.__string"] = None,
        resource_type: Optional["capo_medialive.types.__string.__string"] = None,
        special_feature: Optional["capo_medialive.types.__string.__string"] = None,
        video_quality: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_offerings_response.ListOfferingsResponse":
        """List offerings available for purchase.

        Args:
            channel_class: Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE'
            channel_configuration: Filter to offerings that match the configuration of an existing channel, e.g. '2345678' (a channel ID)
            codec: Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', 'LINK', or 'AV1'
            duration: Filter by offering duration, e.g. '12'
            maximum_bitrate: Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
            maximum_framerate: Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
            resolution: Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'
            resource_type: Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
            special_feature: Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
            video_quality: Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_offerings_request.ListOfferingsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_offerings_response.ListOfferingsResponse"
        ]:
            import capo_medialive._operations.media_live.list_offerings

            output, http_response = (
                capo_medialive._operations.media_live.list_offerings.list_offerings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_offerings_request.ListOfferingsRequest = {}
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if channel_configuration is not None:
            input_["channel_configuration"] = channel_configuration
        if codec is not None:
            input_["codec"] = codec
        if duration is not None:
            input_["duration"] = duration
        if max_results is not None:
            input_["max_results"] = max_results
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if maximum_framerate is not None:
            input_["maximum_framerate"] = maximum_framerate
        if next_token is not None:
            input_["next_token"] = next_token
        if resolution is not None:
            input_["resolution"] = resolution
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if special_feature is not None:
            input_["special_feature"] = special_feature
        if video_quality is not None:
            input_["video_quality"] = video_quality

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_offerings(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["capo_medialive.types.__string.__string"] = None,
        channel_configuration: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
        codec: Optional["capo_medialive.types.__string.__string"] = None,
        duration: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["capo_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["capo_medialive.types.__string.__string"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        resolution: Optional["capo_medialive.types.__string.__string"] = None,
        resource_type: Optional["capo_medialive.types.__string.__string"] = None,
        special_feature: Optional["capo_medialive.types.__string.__string"] = None,
        video_quality: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.offering.Offering]":
        _token = next_token
        while True:
            _response = self.list_offerings(
                config_overrides=config_overrides,
                channel_class=channel_class,
                channel_configuration=channel_configuration,
                codec=codec,
                duration=duration,
                max_results=max_results,
                maximum_bitrate=maximum_bitrate,
                maximum_framerate=maximum_framerate,
                next_token=_token,
                resolution=resolution,
                resource_type=resource_type,
                special_feature=special_feature,
                video_quality=video_quality,
            )
            _page = _resolve_path(_response, ("offerings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_reservations(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["capo_medialive.types.__string.__string"] = None,
        codec: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["capo_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["capo_medialive.types.__string.__string"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        resolution: Optional["capo_medialive.types.__string.__string"] = None,
        resource_type: Optional["capo_medialive.types.__string.__string"] = None,
        special_feature: Optional["capo_medialive.types.__string.__string"] = None,
        video_quality: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_reservations_response.ListReservationsResponse":
        """List purchased reservations.

        Args:
            channel_class: Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE'
            codec: Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', 'LINK', or 'AV1'
            maximum_bitrate: Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS'
            maximum_framerate: Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
            resolution: Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'
            resource_type: Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
            special_feature: Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION'
            video_quality: Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM'

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_reservations_request.ListReservationsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_reservations_response.ListReservationsResponse"
        ]:
            import capo_medialive._operations.media_live.list_reservations

            output, http_response = (
                capo_medialive._operations.media_live.list_reservations.list_reservations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_reservations_request.ListReservationsRequest = {}
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if codec is not None:
            input_["codec"] = codec
        if max_results is not None:
            input_["max_results"] = max_results
        if maximum_bitrate is not None:
            input_["maximum_bitrate"] = maximum_bitrate
        if maximum_framerate is not None:
            input_["maximum_framerate"] = maximum_framerate
        if next_token is not None:
            input_["next_token"] = next_token
        if resolution is not None:
            input_["resolution"] = resolution
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if special_feature is not None:
            input_["special_feature"] = special_feature
        if video_quality is not None:
            input_["video_quality"] = video_quality

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_reservations(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional["capo_medialive.types.__string.__string"] = None,
        codec: Optional["capo_medialive.types.__string.__string"] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        maximum_bitrate: Optional["capo_medialive.types.__string.__string"] = None,
        maximum_framerate: Optional["capo_medialive.types.__string.__string"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
        resolution: Optional["capo_medialive.types.__string.__string"] = None,
        resource_type: Optional["capo_medialive.types.__string.__string"] = None,
        special_feature: Optional["capo_medialive.types.__string.__string"] = None,
        video_quality: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.reservation.Reservation]":
        _token = next_token
        while True:
            _response = self.list_reservations(
                config_overrides=config_overrides,
                channel_class=channel_class,
                codec=codec,
                max_results=max_results,
                maximum_bitrate=maximum_bitrate,
                maximum_framerate=maximum_framerate,
                next_token=_token,
                resolution=resolution,
                resource_type=resource_type,
                special_feature=special_feature,
                video_quality=video_quality,
            )
            _page = _resolve_path(_response, ("reservations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sdi_sources(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_sdi_sources_response.ListSdiSourcesResponse":
        """List all the SdiSources in the AWS account.

        Args:
            max_results: The maximum number of items to return.
            next_token: The token to retrieve the next page of results.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_sdi_sources_request.ListSdiSourcesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_sdi_sources_response.ListSdiSourcesResponse"
        ]:
            import capo_medialive._operations.media_live.list_sdi_sources

            output, http_response = (
                capo_medialive._operations.media_live.list_sdi_sources.list_sdi_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_sdi_sources_request.ListSdiSourcesRequest = {}
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

    def iter_list_sdi_sources(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.sdi_source_summary.SdiSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_sdi_sources(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sdi_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_signal_maps(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
        event_bridge_rule_template_group_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.list_signal_maps_response.ListSignalMapsResponse":
        """Lists signal maps.

        Args:
            cloud_watch_alarm_template_group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            event_bridge_rule_template_group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            next_token: A token used to retrieve the next set of results in paginated list responses.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_signal_maps_request.ListSignalMapsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_signal_maps_response.ListSignalMapsResponse"
        ]:
            import capo_medialive._operations.media_live.list_signal_maps

            output, http_response = (
                capo_medialive._operations.media_live.list_signal_maps.list_signal_maps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_signal_maps_request.ListSignalMapsRequest = {}
        if cloud_watch_alarm_template_group_identifier is not None:
            input_["cloud_watch_alarm_template_group_identifier"] = (
                cloud_watch_alarm_template_group_identifier
            )
        if event_bridge_rule_template_group_identifier is not None:
            input_["event_bridge_rule_template_group_identifier"] = (
                event_bridge_rule_template_group_identifier
            )
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

    def iter_list_signal_maps(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
        event_bridge_rule_template_group_identifier: Optional[
            "capo_medialive.types.__string.__string"
        ] = None,
        max_results: Optional["capo_medialive.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "Iterator[capo_medialive.types.signal_map_summary.SignalMapSummary]":
        _token = next_token
        while True:
            _response = self.list_signal_maps(
                config_overrides=config_overrides,
                cloud_watch_alarm_template_group_identifier=cloud_watch_alarm_template_group_identifier,
                event_bridge_rule_template_group_identifier=event_bridge_rule_template_group_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("signal_maps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """Produces list of tags that have been created for a resource

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_medialive._operations.media_live.list_tags_for_resource

            output, http_response = (
                capo_medialive._operations.media_live.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_versions(
        self, *, config_overrides: Optional[MediaLiveClientConfig] = None
    ) -> "capo_medialive.types.list_versions_response.ListVersionsResponse":
        """Retrieves an array of all the encoder engine versions that are available in this AWS account.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.list_versions_request.ListVersionsRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.list_versions_response.ListVersionsResponse"
        ]:
            import capo_medialive._operations.media_live.list_versions

            output, http_response = (
                capo_medialive._operations.media_live.list_versions.list_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.list_versions_request.ListVersionsRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def purchase_offering(
        self,
        offering_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        count: Optional["capo_medialive.types.__integer_min1.__integerMin1"] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        renewal_settings: Optional[
            "capo_medialive.types.renewal_settings.RenewalSettings"
        ] = None,
        request_id: Optional["capo_medialive.types.__string.__string"] = None,
        start: Optional["capo_medialive.types.__string.__string"] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
    ) -> "capo_medialive.types.purchase_offering_response.PurchaseOfferingResponse":
        """Purchase an offering and create a reservation.

        Args:
            count: Number of resources
            name: Name for the new reservation
            offering_id: Offering to purchase, e.g. '87654321'
            renewal_settings: Renewal settings for the reservation
            request_id: Unique request ID to be specified. This is needed to prevent retries from creating multiple resources.
            start: Requested reservation start time (UTC) in ISO-8601 format. The specified time must be between the first day of the current month and one year from now. If no value is given, the default is now.
            tags: A collection of key-value pairs

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.purchase_offering_request.PurchaseOfferingRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.purchase_offering_response.PurchaseOfferingResponse"
        ]:
            import capo_medialive._operations.media_live.purchase_offering

            output, http_response = (
                capo_medialive._operations.media_live.purchase_offering.purchase_offering(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.purchase_offering_request.PurchaseOfferingRequest = {
            "offering_id": offering_id
        }
        if count is not None:
            input_["count"] = count
        if name is not None:
            input_["name"] = name
        if renewal_settings is not None:
            input_["renewal_settings"] = renewal_settings
        if request_id is None:
            request_id = str(uuid.uuid4())
        input_["request_id"] = request_id
        if start is not None:
            input_["start"] = start
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reboot_input_device(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        force: Optional[
            "capo_medialive.types.reboot_input_device_force.RebootInputDeviceForce"
        ] = None,
    ) -> "capo_medialive.types.reboot_input_device_response.RebootInputDeviceResponse":
        """Send a reboot command to the specified input device. The device will begin rebooting within a few seconds of sending the command. When the reboot is complete, the device’s connection status will change to connected.

        Args:
            force: Force a reboot of an input device. If the device is streaming, it will stop streaming and begin rebooting within a few seconds of sending the command. If the device was streaming prior to the reboot, the device will resume streaming when the reboot completes.
            input_device_id: The unique ID of the input device to reboot. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.reboot_input_device_request.RebootInputDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.reboot_input_device_response.RebootInputDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.reboot_input_device

            output, http_response = (
                capo_medialive._operations.media_live.reboot_input_device.reboot_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.reboot_input_device_request.RebootInputDeviceRequest = {
            "input_device_id": input_device_id
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

    def reject_input_device_transfer(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.reject_input_device_transfer_response.RejectInputDeviceTransferResponse":
        """Reject the transfer of the specified input device to your AWS account.

        Args:
            input_device_id: The unique ID of the input device to reject. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.reject_input_device_transfer_request.RejectInputDeviceTransferRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.reject_input_device_transfer_response.RejectInputDeviceTransferResponse"
        ]:
            import capo_medialive._operations.media_live.reject_input_device_transfer

            output, http_response = (
                capo_medialive._operations.media_live.reject_input_device_transfer.reject_input_device_transfer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.reject_input_device_transfer_request.RejectInputDeviceTransferRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def restart_channel_pipelines(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        pipeline_ids: Optional[
            "capo_medialive.types.__list_of_channel_pipeline_id_to_restart.__listOfChannelPipelineIdToRestart"
        ] = None,
    ) -> "capo_medialive.types.restart_channel_pipelines_response.RestartChannelPipelinesResponse":
        """Restart pipelines in one channel that is currently running.

        Args:
            channel_id: ID of channel
            pipeline_ids: An array of pipelines to restart in this channel. Format PIPELINE_0 or PIPELINE_1.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.restart_channel_pipelines_request.RestartChannelPipelinesRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.restart_channel_pipelines_response.RestartChannelPipelinesResponse"
        ]:
            import capo_medialive._operations.media_live.restart_channel_pipelines

            output, http_response = (
                capo_medialive._operations.media_live.restart_channel_pipelines.restart_channel_pipelines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.restart_channel_pipelines_request.RestartChannelPipelinesRequest = {
            "channel_id": channel_id
        }
        if pipeline_ids is not None:
            input_["pipeline_ids"] = pipeline_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_channel(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.start_channel_response.StartChannelResponse":
        """Starts an existing channel

        Args:
            channel_id: A request to start a channel

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_channel_request.StartChannelRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_channel_response.StartChannelResponse"
        ]:
            import capo_medialive._operations.media_live.start_channel

            output, http_response = (
                capo_medialive._operations.media_live.start_channel.start_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_channel_request.StartChannelRequest = {
            "channel_id": channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_delete_monitor_deployment(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.start_delete_monitor_deployment_response.StartDeleteMonitorDeploymentResponse":
        """Initiates a deployment to delete the monitor of the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_delete_monitor_deployment_request.StartDeleteMonitorDeploymentRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_delete_monitor_deployment_response.StartDeleteMonitorDeploymentResponse"
        ]:
            import capo_medialive._operations.media_live.start_delete_monitor_deployment

            output, http_response = (
                capo_medialive._operations.media_live.start_delete_monitor_deployment.start_delete_monitor_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_delete_monitor_deployment_request.StartDeleteMonitorDeploymentRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_input_device(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.start_input_device_response.StartInputDeviceResponse":
        """Start an input device that is attached to a MediaConnect flow. (There is no need to start a device that is attached to a MediaLive input; MediaLive starts the device when the channel starts.)

        Args:
            input_device_id: The unique ID of the input device to start. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_input_device_request.StartInputDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_input_device_response.StartInputDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.start_input_device

            output, http_response = (
                capo_medialive._operations.media_live.start_input_device.start_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_input_device_request.StartInputDeviceRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_input_device_maintenance_window(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.start_input_device_maintenance_window_response.StartInputDeviceMaintenanceWindowResponse":
        """Start a maintenance window for the specified input device. Starting a maintenance window will give the device up to two hours to install software. If the device was streaming prior to the maintenance, it will resume streaming when the software is fully installed. Devices automatically install updates while they are powered on and their MediaLive channels are stopped. A maintenance window allows you to update a device without having to stop MediaLive channels that use the device. The device must remain powered on and connected to the internet for the duration of the maintenance.

        Args:
            input_device_id: The unique ID of the input device to start a maintenance window for. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_input_device_maintenance_window_request.StartInputDeviceMaintenanceWindowRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_input_device_maintenance_window_response.StartInputDeviceMaintenanceWindowResponse"
        ]:
            import capo_medialive._operations.media_live.start_input_device_maintenance_window

            output, http_response = (
                capo_medialive._operations.media_live.start_input_device_maintenance_window.start_input_device_maintenance_window(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_input_device_maintenance_window_request.StartInputDeviceMaintenanceWindowRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_monitor_deployment(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        dry_run: Optional["capo_medialive.types.__boolean.__boolean"] = None,
    ) -> "capo_medialive.types.start_monitor_deployment_response.StartMonitorDeploymentResponse":
        """Initiates a deployment to deploy the latest monitor of the specified signal map.

        Args:
            identifier: A signal map's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_monitor_deployment_request.StartMonitorDeploymentRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_monitor_deployment_response.StartMonitorDeploymentResponse"
        ]:
            import capo_medialive._operations.media_live.start_monitor_deployment

            output, http_response = (
                capo_medialive._operations.media_live.start_monitor_deployment.start_monitor_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_monitor_deployment_request.StartMonitorDeploymentRequest = {
            "identifier": identifier
        }
        if dry_run is not None:
            input_["dry_run"] = dry_run

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_multiplex(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.start_multiplex_response.StartMultiplexResponse":
        """Start (run) the multiplex. Starting the multiplex does not start the channels. You must explicitly start each channel.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_multiplex_request.StartMultiplexRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_multiplex_response.StartMultiplexResponse"
        ]:
            import capo_medialive._operations.media_live.start_multiplex

            output, http_response = (
                capo_medialive._operations.media_live.start_multiplex.start_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_multiplex_request.StartMultiplexRequest = {
            "multiplex_id": multiplex_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_update_signal_map(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cloud_watch_alarm_template_group_identifiers: Optional[
            "capo_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        discovery_entry_point_arn: Optional[
            "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
        ] = None,
        event_bridge_rule_template_group_identifiers: Optional[
            "capo_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
        ] = None,
        force_rediscovery: Optional["capo_medialive.types.__boolean.__boolean"] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
    ) -> "capo_medialive.types.start_update_signal_map_response.StartUpdateSignalMapResponse":
        """Initiates an update for the specified signal map. Will discover a new signal map if a changed discoveryEntryPointArn is provided.

        Args:
            description: A resource's optional description.
            discovery_entry_point_arn: A top-level supported AWS resource ARN to discovery a signal map from.
            force_rediscovery: If true, will force a rediscovery of a signal map if an unchanged discoveryEntryPointArn is provided.
            identifier: A signal map's identifier. Can be either be its id or current name.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.start_update_signal_map_request.StartUpdateSignalMapRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.start_update_signal_map_response.StartUpdateSignalMapResponse"
        ]:
            import capo_medialive._operations.media_live.start_update_signal_map

            output, http_response = (
                capo_medialive._operations.media_live.start_update_signal_map.start_update_signal_map(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.start_update_signal_map_request.StartUpdateSignalMapRequest = {
            "identifier": identifier
        }
        if cloud_watch_alarm_template_group_identifiers is not None:
            input_["cloud_watch_alarm_template_group_identifiers"] = (
                cloud_watch_alarm_template_group_identifiers
            )
        if description is not None:
            input_["description"] = description
        if discovery_entry_point_arn is not None:
            input_["discovery_entry_point_arn"] = discovery_entry_point_arn
        if event_bridge_rule_template_group_identifiers is not None:
            input_["event_bridge_rule_template_group_identifiers"] = (
                event_bridge_rule_template_group_identifiers
            )
        if force_rediscovery is not None:
            input_["force_rediscovery"] = force_rediscovery
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_channel(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.stop_channel_response.StopChannelResponse":
        """Stops a running channel

        Args:
            channel_id: A request to stop a running channel

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.stop_channel_request.StopChannelRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.stop_channel_response.StopChannelResponse"
        ]:
            import capo_medialive._operations.media_live.stop_channel

            output, http_response = (
                capo_medialive._operations.media_live.stop_channel.stop_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.stop_channel_request.StopChannelRequest = {
            "channel_id": channel_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_input_device(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.stop_input_device_response.StopInputDeviceResponse":
        """Stop an input device that is attached to a MediaConnect flow. (There is no need to stop a device that is attached to a MediaLive input; MediaLive automatically stops the device when the channel stops.)

        Args:
            input_device_id: The unique ID of the input device to stop. For example, hd-123456789abcdef.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.stop_input_device_request.StopInputDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.stop_input_device_response.StopInputDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.stop_input_device

            output, http_response = (
                capo_medialive._operations.media_live.stop_input_device.stop_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.stop_input_device_request.StopInputDeviceRequest = {
            "input_device_id": input_device_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_multiplex(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
    ) -> "capo_medialive.types.stop_multiplex_response.StopMultiplexResponse":
        """Stops a running multiplex. If the multiplex isn't running, this action has no effect.

        Args:
            multiplex_id: The ID of the multiplex.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.stop_multiplex_request.StopMultiplexRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.stop_multiplex_response.StopMultiplexResponse"
        ]:
            import capo_medialive._operations.media_live.stop_multiplex

            output, http_response = (
                capo_medialive._operations.media_live.stop_multiplex.stop_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.stop_multiplex_request.StopMultiplexRequest = {
            "multiplex_id": multiplex_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def transfer_input_device(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        target_customer_id: Optional["capo_medialive.types.__string.__string"] = None,
        target_region: Optional["capo_medialive.types.__string.__string"] = None,
        transfer_message: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.transfer_input_device_response.TransferInputDeviceResponse":
        """Start an input device transfer to another AWS account. After you make the request, the other account must accept or reject the transfer.

        Args:
            input_device_id: The unique ID of this input device. For example, hd-123456789abcdef.
            target_customer_id: The AWS account ID (12 digits) for the recipient of the device transfer.
            target_region: The target AWS region to transfer the device.
            transfer_message: An optional message for the recipient. Maximum 280 characters.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.transfer_input_device_request.TransferInputDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.transfer_input_device_response.TransferInputDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.transfer_input_device

            output, http_response = (
                capo_medialive._operations.media_live.transfer_input_device.transfer_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.transfer_input_device_request.TransferInputDeviceRequest = {
            "input_device_id": input_device_id
        }
        if target_customer_id is not None:
            input_["target_customer_id"] = target_customer_id
        if target_region is not None:
            input_["target_region"] = target_region
        if transfer_message is not None:
            input_["transfer_message"] = transfer_message

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_account_configuration(
        self,
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        account_configuration: Optional[
            "capo_medialive.types.account_configuration.AccountConfiguration"
        ] = None,
    ) -> "capo_medialive.types.update_account_configuration_response.UpdateAccountConfigurationResponse":
        """Update account configuration

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_account_configuration_request.UpdateAccountConfigurationRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_account_configuration_response.UpdateAccountConfigurationResponse"
        ]:
            import capo_medialive._operations.media_live.update_account_configuration

            output, http_response = (
                capo_medialive._operations.media_live.update_account_configuration.update_account_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_account_configuration_request.UpdateAccountConfigurationRequest = {}
        if account_configuration is not None:
            input_["account_configuration"] = account_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        cdi_input_specification: Optional[
            "capo_medialive.types.cdi_input_specification.CdiInputSpecification"
        ] = None,
        destinations: Optional[
            "capo_medialive.types.__list_of_output_destination.__listOfOutputDestination"
        ] = None,
        encoder_settings: Optional[
            "capo_medialive.types.encoder_settings.EncoderSettings"
        ] = None,
        input_attachments: Optional[
            "capo_medialive.types.__list_of_input_attachment.__listOfInputAttachment"
        ] = None,
        input_specification: Optional[
            "capo_medialive.types.input_specification.InputSpecification"
        ] = None,
        log_level: Optional["capo_medialive.types.log_level.LogLevel"] = None,
        maintenance: Optional[
            "capo_medialive.types.maintenance_update_settings.MaintenanceUpdateSettings"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        role_arn: Optional["capo_medialive.types.__string.__string"] = None,
        channel_engine_version: Optional[
            "capo_medialive.types.channel_engine_version_request.ChannelEngineVersionRequest"
        ] = None,
        dry_run: Optional["capo_medialive.types.__boolean.__boolean"] = None,
        anywhere_settings: Optional[
            "capo_medialive.types.anywhere_settings.AnywhereSettings"
        ] = None,
        linked_channel_settings: Optional[
            "capo_medialive.types.linked_channel_settings.LinkedChannelSettings"
        ] = None,
        channel_security_groups: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        inference_settings: Optional[
            "capo_medialive.types.inference_settings.InferenceSettings"
        ] = None,
        special_router_settings: Optional[
            "capo_medialive.types.special_router_settings.SpecialRouterSettings"
        ] = None,
    ) -> "capo_medialive.types.update_channel_response.UpdateChannelResponse":
        """Updates a channel.

        Args:
            cdi_input_specification: Specification of CDI inputs for this channel
            channel_id: channel ID
            destinations: A list of output destinations for this channel.
            encoder_settings: The encoder settings for this channel.
            input_specification: Specification of network and file inputs for this channel
            log_level: The log level to write to CloudWatch Logs.
            maintenance: Maintenance settings for this channel.
            name: The name of the channel.
            role_arn: An optional Amazon Resource Name (ARN) of the role to assume when running the Channel. If you do not specify this on an update call but the role was previously set that role will be removed.
            channel_engine_version: Channel engine version for this channel
            anywhere_settings: The Elemental Anywhere settings for this channel.
            linked_channel_settings: The linked channel settings for the channel.
            channel_security_groups: A list of IDs for all the Input Security Groups attached to the channel.
            inference_settings: Include this setting to include Elemental Inference features in this channel.
            special_router_settings: When using MediaConnect Router as the source of a MediaLive input there's a special handoff that occurs when a router output is created. This group of settings is set on your behalf by the MediaConnect Router service using this set of settings. This setting object can only by used by that service.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_channel_request.UpdateChannelRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_channel_response.UpdateChannelResponse"
        ]:
            import capo_medialive._operations.media_live.update_channel

            output, http_response = (
                capo_medialive._operations.media_live.update_channel.update_channel(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_channel_request.UpdateChannelRequest = {
            "channel_id": channel_id
        }
        if cdi_input_specification is not None:
            input_["cdi_input_specification"] = cdi_input_specification
        if destinations is not None:
            input_["destinations"] = destinations
        if encoder_settings is not None:
            input_["encoder_settings"] = encoder_settings
        if input_attachments is not None:
            input_["input_attachments"] = input_attachments
        if input_specification is not None:
            input_["input_specification"] = input_specification
        if log_level is not None:
            input_["log_level"] = log_level
        if maintenance is not None:
            input_["maintenance"] = maintenance
        if name is not None:
            input_["name"] = name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if channel_engine_version is not None:
            input_["channel_engine_version"] = channel_engine_version
        if dry_run is not None:
            input_["dry_run"] = dry_run
        if anywhere_settings is not None:
            input_["anywhere_settings"] = anywhere_settings
        if linked_channel_settings is not None:
            input_["linked_channel_settings"] = linked_channel_settings
        if channel_security_groups is not None:
            input_["channel_security_groups"] = channel_security_groups
        if inference_settings is not None:
            input_["inference_settings"] = inference_settings
        if special_router_settings is not None:
            input_["special_router_settings"] = special_router_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_class(
        self,
        channel_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        channel_class: Optional[
            "capo_medialive.types.channel_class.ChannelClass"
        ] = None,
        destinations: Optional[
            "capo_medialive.types.__list_of_output_destination.__listOfOutputDestination"
        ] = None,
    ) -> (
        "capo_medialive.types.update_channel_class_response.UpdateChannelClassResponse"
    ):
        """Changes the class of the channel.

        Args:
            channel_class: The channel class that you wish to update this channel to use.
            channel_id: Channel Id of the channel whose class should be updated.
            destinations: A list of output destinations for this channel.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_channel_class_request.UpdateChannelClassRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_channel_class_response.UpdateChannelClassResponse"
        ]:
            import capo_medialive._operations.media_live.update_channel_class

            output, http_response = (
                capo_medialive._operations.media_live.update_channel_class.update_channel_class(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_channel_class_request.UpdateChannelClassRequest = {
            "channel_id": channel_id
        }
        if channel_class is not None:
            input_["channel_class"] = channel_class
        if destinations is not None:
            input_["destinations"] = destinations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_channel_placement_group(
        self,
        channel_placement_group_id: "capo_medialive.types.__string.__string",
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        nodes: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
    ) -> "capo_medialive.types.update_channel_placement_group_response.UpdateChannelPlacementGroupResponse":
        """Change the settings for a ChannelPlacementGroup.

        Args:
            channel_placement_group_id: The ID of the channel placement group.
            cluster_id: The ID of the cluster.
            name: Include this parameter only if you want to change the current name of the ChannelPlacementGroup. Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive.
            nodes: Include this parameter only if you want to change the list of Nodes that are associated with the ChannelPlacementGroup.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_channel_placement_group_request.UpdateChannelPlacementGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_channel_placement_group_response.UpdateChannelPlacementGroupResponse"
        ]:
            import capo_medialive._operations.media_live.update_channel_placement_group

            output, http_response = (
                capo_medialive._operations.media_live.update_channel_placement_group.update_channel_placement_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_channel_placement_group_request.UpdateChannelPlacementGroupRequest = {
            "channel_placement_group_id": channel_placement_group_id,
            "cluster_id": cluster_id,
        }
        if name is not None:
            input_["name"] = name
        if nodes is not None:
            input_["nodes"] = nodes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cloud_watch_alarm_template(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        comparison_operator: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_comparison_operator.CloudWatchAlarmTemplateComparisonOperator"
        ] = None,
        datapoints_to_alarm: Optional[
            "capo_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        evaluation_periods: Optional[
            "capo_medialive.types.__integer_min1.__integerMin1"
        ] = None,
        group_identifier: Optional[
            "capo_medialive.types.__string_pattern_s.__stringPatternS"
        ] = None,
        metric_name: Optional[
            "capo_medialive.types.__string_max64.__stringMax64"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
        period: Optional[
            "capo_medialive.types.__integer_min10_max86400.__integerMin10Max86400"
        ] = None,
        statistic: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_statistic.CloudWatchAlarmTemplateStatistic"
        ] = None,
        target_resource_type: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_target_resource_type.CloudWatchAlarmTemplateTargetResourceType"
        ] = None,
        threshold: Optional["capo_medialive.types.__double.__double"] = None,
        treat_missing_data: Optional[
            "capo_medialive.types.cloud_watch_alarm_template_treat_missing_data.CloudWatchAlarmTemplateTreatMissingData"
        ] = None,
    ) -> "capo_medialive.types.update_cloud_watch_alarm_template_response.UpdateCloudWatchAlarmTemplateResponse":
        """Updates the specified cloudwatch alarm template.

        Args:
            datapoints_to_alarm: The number of datapoints within the evaluation period that must be breaching to trigger the alarm.
            description: A resource's optional description.
            evaluation_periods: The number of periods over which data is compared to the specified threshold.
            group_identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.
            identifier: A cloudwatch alarm template's identifier. Can be either be its id or current name.
            metric_name: The name of the metric associated with the alarm. Must be compatible with targetResourceType.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.
            period: The period, in seconds, over which the specified statistic is applied.
            threshold: The threshold value to compare with the specified statistic.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_cloud_watch_alarm_template_request.UpdateCloudWatchAlarmTemplateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_cloud_watch_alarm_template_response.UpdateCloudWatchAlarmTemplateResponse"
        ]:
            import capo_medialive._operations.media_live.update_cloud_watch_alarm_template

            output, http_response = (
                capo_medialive._operations.media_live.update_cloud_watch_alarm_template.update_cloud_watch_alarm_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_cloud_watch_alarm_template_request.UpdateCloudWatchAlarmTemplateRequest = {
            "identifier": identifier
        }
        if comparison_operator is not None:
            input_["comparison_operator"] = comparison_operator
        if datapoints_to_alarm is not None:
            input_["datapoints_to_alarm"] = datapoints_to_alarm
        if description is not None:
            input_["description"] = description
        if evaluation_periods is not None:
            input_["evaluation_periods"] = evaluation_periods
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if name is not None:
            input_["name"] = name
        if period is not None:
            input_["period"] = period
        if statistic is not None:
            input_["statistic"] = statistic
        if target_resource_type is not None:
            input_["target_resource_type"] = target_resource_type
        if threshold is not None:
            input_["threshold"] = threshold
        if treat_missing_data is not None:
            input_["treat_missing_data"] = treat_missing_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cloud_watch_alarm_template_group(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
    ) -> "capo_medialive.types.update_cloud_watch_alarm_template_group_response.UpdateCloudWatchAlarmTemplateGroupResponse":
        """Updates the specified cloudwatch alarm template group.

        Args:
            description: A resource's optional description.
            identifier: A cloudwatch alarm template group's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_cloud_watch_alarm_template_group_request.UpdateCloudWatchAlarmTemplateGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_cloud_watch_alarm_template_group_response.UpdateCloudWatchAlarmTemplateGroupResponse"
        ]:
            import capo_medialive._operations.media_live.update_cloud_watch_alarm_template_group

            output, http_response = (
                capo_medialive._operations.media_live.update_cloud_watch_alarm_template_group.update_cloud_watch_alarm_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_cloud_watch_alarm_template_group_request.UpdateCloudWatchAlarmTemplateGroupRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        network_settings: Optional[
            "capo_medialive.types.cluster_network_settings_update_request.ClusterNetworkSettingsUpdateRequest"
        ] = None,
    ) -> "capo_medialive.types.update_cluster_response.UpdateClusterResponse":
        """Change the settings for a Cluster.

        Args:
            cluster_id: The ID of the cluster
            name: Include this parameter only if you want to change the current name of the Cluster. Specify a name that is unique in the AWS account. You can't change the name. Names are case-sensitive.
            network_settings: Include this property only if you want to change the current connections between the Nodes in the Cluster and the Networks the Cluster is associated with.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_cluster_response.UpdateClusterResponse"
        ]:
            import capo_medialive._operations.media_live.update_cluster

            output, http_response = (
                capo_medialive._operations.media_live.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_cluster_request.UpdateClusterRequest = {
            "cluster_id": cluster_id
        }
        if name is not None:
            input_["name"] = name
        if network_settings is not None:
            input_["network_settings"] = network_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_bridge_rule_template(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
        event_targets: Optional[
            "capo_medialive.types.__list_of_event_bridge_rule_template_target.__listOfEventBridgeRuleTemplateTarget"
        ] = None,
        event_type: Optional[
            "capo_medialive.types.event_bridge_rule_template_event_type.EventBridgeRuleTemplateEventType"
        ] = None,
        group_identifier: Optional[
            "capo_medialive.types.__string_pattern_s.__stringPatternS"
        ] = None,
        name: Optional[
            "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
        ] = None,
    ) -> "capo_medialive.types.update_event_bridge_rule_template_response.UpdateEventBridgeRuleTemplateResponse":
        """Updates the specified eventbridge rule template.

        Args:
            description: A resource's optional description.
            group_identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.
            identifier: An eventbridge rule template's identifier. Can be either be its id or current name.
            name: A resource's name. Names must be unique within the scope of a resource type in a specific region.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_event_bridge_rule_template_request.UpdateEventBridgeRuleTemplateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_event_bridge_rule_template_response.UpdateEventBridgeRuleTemplateResponse"
        ]:
            import capo_medialive._operations.media_live.update_event_bridge_rule_template

            output, http_response = (
                capo_medialive._operations.media_live.update_event_bridge_rule_template.update_event_bridge_rule_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_event_bridge_rule_template_request.UpdateEventBridgeRuleTemplateRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if event_targets is not None:
            input_["event_targets"] = event_targets
        if event_type is not None:
            input_["event_type"] = event_type
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_event_bridge_rule_template_group(
        self,
        identifier: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        description: Optional[
            "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
        ] = None,
    ) -> "capo_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse":
        """Updates the specified eventbridge rule template group.

        Args:
            description: A resource's optional description.
            identifier: An eventbridge rule template group's identifier. Can be either be its id or current name.

        Raises:
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_event_bridge_rule_template_group_response.UpdateEventBridgeRuleTemplateGroupResponse"
        ]:
            import capo_medialive._operations.media_live.update_event_bridge_rule_template_group

            output, http_response = (
                capo_medialive._operations.media_live.update_event_bridge_rule_template_group.update_event_bridge_rule_template_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_event_bridge_rule_template_group_request.UpdateEventBridgeRuleTemplateGroupRequest = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_input(
        self,
        input_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        destinations: Optional[
            "capo_medialive.types.__list_of_input_destination_request.__listOfInputDestinationRequest"
        ] = None,
        input_devices: Optional[
            "capo_medialive.types.__list_of_input_device_request.__listOfInputDeviceRequest"
        ] = None,
        input_security_groups: Optional[
            "capo_medialive.types.__list_of__string.__listOf__string"
        ] = None,
        media_connect_flows: Optional[
            "capo_medialive.types.__list_of_media_connect_flow_request.__listOfMediaConnectFlowRequest"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        role_arn: Optional["capo_medialive.types.__string.__string"] = None,
        sources: Optional[
            "capo_medialive.types.__list_of_input_source_request.__listOfInputSourceRequest"
        ] = None,
        srt_settings: Optional[
            "capo_medialive.types.srt_settings_request.SrtSettingsRequest"
        ] = None,
        multicast_settings: Optional[
            "capo_medialive.types.multicast_settings_update_request.MulticastSettingsUpdateRequest"
        ] = None,
        smpte2110_receiver_group_settings: Optional[
            "capo_medialive.types.smpte2110_receiver_group_settings.Smpte2110ReceiverGroupSettings"
        ] = None,
        sdi_sources: Optional[
            "capo_medialive.types.input_sdi_sources.InputSdiSources"
        ] = None,
        special_router_settings: Optional[
            "capo_medialive.types.special_router_settings.SpecialRouterSettings"
        ] = None,
    ) -> "capo_medialive.types.update_input_response.UpdateInputResponse":
        """Updates an input.

        Args:
            destinations: Destination settings for PUSH type inputs.
            input_devices: Settings for the devices.
            input_id: Unique ID of the input.
            input_security_groups: A list of security groups referenced by IDs to attach to the input.
            media_connect_flows: A list of the MediaConnect Flow ARNs that you want to use as the source of the input. You can specify as few as one Flow and presently, as many as two. The only requirement is when you have more than one is that each Flow is in a separate Availability Zone as this ensures your EML input is redundant to AZ issues.
            name: Name of the input.
            role_arn: The Amazon Resource Name (ARN) of the role this input assumes during and after creation.
            sources: The source URLs for a PULL-type input. Every PULL type input needs exactly two source URLs for redundancy. Only specify sources for PULL type Inputs. Leave Destinations empty.
            srt_settings: The settings associated with an SRT input.
            multicast_settings: Multicast Input settings.
            smpte2110_receiver_group_settings: Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.
            special_router_settings: When using MediaConnect Router as the source of a MediaLive input there's a special handoff that occurs when a router output is created. This group of settings is set on your behalf by the MediaConnect Router service using this set of settings. This setting object can only by used by that service.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_input_request.UpdateInputRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_input_response.UpdateInputResponse"
        ]:
            import capo_medialive._operations.media_live.update_input

            output, http_response = (
                capo_medialive._operations.media_live.update_input.update_input(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_input_request.UpdateInputRequest = {
            "input_id": input_id
        }
        if destinations is not None:
            input_["destinations"] = destinations
        if input_devices is not None:
            input_["input_devices"] = input_devices
        if input_security_groups is not None:
            input_["input_security_groups"] = input_security_groups
        if media_connect_flows is not None:
            input_["media_connect_flows"] = media_connect_flows
        if name is not None:
            input_["name"] = name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if sources is not None:
            input_["sources"] = sources
        if srt_settings is not None:
            input_["srt_settings"] = srt_settings
        if multicast_settings is not None:
            input_["multicast_settings"] = multicast_settings
        if smpte2110_receiver_group_settings is not None:
            input_["smpte2110_receiver_group_settings"] = (
                smpte2110_receiver_group_settings
            )
        if sdi_sources is not None:
            input_["sdi_sources"] = sdi_sources
        if special_router_settings is not None:
            input_["special_router_settings"] = special_router_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_input_device(
        self,
        input_device_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        hd_device_settings: Optional[
            "capo_medialive.types.input_device_configurable_settings.InputDeviceConfigurableSettings"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        uhd_device_settings: Optional[
            "capo_medialive.types.input_device_configurable_settings.InputDeviceConfigurableSettings"
        ] = None,
        availability_zone: Optional["capo_medialive.types.__string.__string"] = None,
    ) -> "capo_medialive.types.update_input_device_response.UpdateInputDeviceResponse":
        """Updates the parameters for the input device.

        Args:
            hd_device_settings: The settings that you want to apply to the HD input device.
            input_device_id: The unique ID of the input device. For example, hd-123456789abcdef.
            name: The name that you assigned to this input device (not the unique ID).
            uhd_device_settings: The settings that you want to apply to the UHD input device.
            availability_zone: The Availability Zone you want associated with this input device.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_input_device_request.UpdateInputDeviceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_input_device_response.UpdateInputDeviceResponse"
        ]:
            import capo_medialive._operations.media_live.update_input_device

            output, http_response = (
                capo_medialive._operations.media_live.update_input_device.update_input_device(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_input_device_request.UpdateInputDeviceRequest = {
            "input_device_id": input_device_id
        }
        if hd_device_settings is not None:
            input_["hd_device_settings"] = hd_device_settings
        if name is not None:
            input_["name"] = name
        if uhd_device_settings is not None:
            input_["uhd_device_settings"] = uhd_device_settings
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_input_security_group(
        self,
        input_security_group_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        tags: Optional["capo_medialive.types.tags.Tags"] = None,
        whitelist_rules: Optional[
            "capo_medialive.types.__list_of_input_whitelist_rule_cidr.__listOfInputWhitelistRuleCidr"
        ] = None,
    ) -> "capo_medialive.types.update_input_security_group_response.UpdateInputSecurityGroupResponse":
        """Update an Input Security Group's Whilelists.

        Args:
            input_security_group_id: The id of the Input Security Group to update.
            tags: A collection of key-value pairs.
            whitelist_rules: List of IPv4 CIDR addresses to whitelist

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_input_security_group_request.UpdateInputSecurityGroupRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_input_security_group_response.UpdateInputSecurityGroupResponse"
        ]:
            import capo_medialive._operations.media_live.update_input_security_group

            output, http_response = (
                capo_medialive._operations.media_live.update_input_security_group.update_input_security_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_input_security_group_request.UpdateInputSecurityGroupRequest = {
            "input_security_group_id": input_security_group_id
        }
        if tags is not None:
            input_["tags"] = tags
        if whitelist_rules is not None:
            input_["whitelist_rules"] = whitelist_rules

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_multiplex(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        multiplex_settings: Optional[
            "capo_medialive.types.multiplex_settings.MultiplexSettings"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        packet_identifiers_mapping: Optional[
            "capo_medialive.types.multiplex_packet_identifiers_mapping.MultiplexPacketIdentifiersMapping"
        ] = None,
    ) -> "capo_medialive.types.update_multiplex_response.UpdateMultiplexResponse":
        """Updates a multiplex.

        Args:
            multiplex_id: ID of the multiplex to update.
            multiplex_settings: The new settings for a multiplex.
            name: Name of the multiplex.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_multiplex_request.UpdateMultiplexRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_multiplex_response.UpdateMultiplexResponse"
        ]:
            import capo_medialive._operations.media_live.update_multiplex

            output, http_response = (
                capo_medialive._operations.media_live.update_multiplex.update_multiplex(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_multiplex_request.UpdateMultiplexRequest = {
            "multiplex_id": multiplex_id
        }
        if multiplex_settings is not None:
            input_["multiplex_settings"] = multiplex_settings
        if name is not None:
            input_["name"] = name
        if packet_identifiers_mapping is not None:
            input_["packet_identifiers_mapping"] = packet_identifiers_mapping

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_multiplex_program(
        self,
        multiplex_id: "capo_medialive.types.__string.__string",
        program_name: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        multiplex_program_settings: Optional[
            "capo_medialive.types.multiplex_program_settings.MultiplexProgramSettings"
        ] = None,
    ) -> "capo_medialive.types.update_multiplex_program_response.UpdateMultiplexProgramResponse":
        """Update a program in a multiplex.

        Args:
            multiplex_id: The ID of the multiplex of the program to update.
            multiplex_program_settings: The new settings for a multiplex program.
            program_name: The name of the program to update.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_multiplex_program_request.UpdateMultiplexProgramRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_multiplex_program_response.UpdateMultiplexProgramResponse"
        ]:
            import capo_medialive._operations.media_live.update_multiplex_program

            output, http_response = (
                capo_medialive._operations.media_live.update_multiplex_program.update_multiplex_program(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_multiplex_program_request.UpdateMultiplexProgramRequest = {
            "multiplex_id": multiplex_id,
            "program_name": program_name,
        }
        if multiplex_program_settings is not None:
            input_["multiplex_program_settings"] = multiplex_program_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network(
        self,
        network_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        ip_pools: Optional[
            "capo_medialive.types.__list_of_ip_pool_update_request.__listOfIpPoolUpdateRequest"
        ] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        routes: Optional[
            "capo_medialive.types.__list_of_route_update_request.__listOfRouteUpdateRequest"
        ] = None,
    ) -> "capo_medialive.types.update_network_response.UpdateNetworkResponse":
        """Change the settings for a Network.

        Args:
            ip_pools: Include this parameter only if you want to change the pool of IP addresses in the network. An array of IpPoolCreateRequests that identify a collection of IP addresses in this network that you want to reserve for use in MediaLive Anywhere. MediaLive Anywhere uses these IP addresses for Push inputs (in both Bridge and NAT networks) and for output destinations (only in Bridge networks). Each IpPoolUpdateRequest specifies one CIDR block.
            name: Include this parameter only if you want to change the name of the Network. Specify a name that is unique in the AWS account. Names are case-sensitive.
            network_id: The ID of the network
            routes: Include this parameter only if you want to change or add routes in the Network. An array of Routes that MediaLive Anywhere needs to know about in order to route encoding traffic.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_network_request.UpdateNetworkRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_network_response.UpdateNetworkResponse"
        ]:
            import capo_medialive._operations.media_live.update_network

            output, http_response = (
                capo_medialive._operations.media_live.update_network.update_network(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_network_request.UpdateNetworkRequest = {
            "network_id": network_id
        }
        if ip_pools is not None:
            input_["ip_pools"] = ip_pools
        if name is not None:
            input_["name"] = name
        if routes is not None:
            input_["routes"] = routes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_node(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        node_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        role: Optional["capo_medialive.types.node_role.NodeRole"] = None,
        sdi_source_mappings: Optional[
            "capo_medialive.types.sdi_source_mappings_update_request.SdiSourceMappingsUpdateRequest"
        ] = None,
    ) -> "capo_medialive.types.update_node_response.UpdateNodeResponse":
        """Change the settings for a Node.

        Args:
            cluster_id: The ID of the cluster
            name: Include this parameter only if you want to change the current name of the Node. Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive.
            node_id: The ID of the node.
            role: The initial role of the Node in the Cluster. ACTIVE means the Node is available for encoding. BACKUP means the Node is a redundant Node and might get used if an ACTIVE Node fails.
            sdi_source_mappings: The mappings of a SDI capture card port to a logical SDI data stream

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_node_request.UpdateNodeRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_node_response.UpdateNodeResponse"
        ]:
            import capo_medialive._operations.media_live.update_node

            output, http_response = (
                capo_medialive._operations.media_live.update_node.update_node(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_node_request.UpdateNodeRequest = {
            "cluster_id": cluster_id,
            "node_id": node_id,
        }
        if name is not None:
            input_["name"] = name
        if role is not None:
            input_["role"] = role
        if sdi_source_mappings is not None:
            input_["sdi_source_mappings"] = sdi_source_mappings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_node_state(
        self,
        cluster_id: "capo_medialive.types.__string.__string",
        node_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        state: Optional[
            "capo_medialive.types.update_node_state_shape.UpdateNodeStateShape"
        ] = None,
    ) -> "capo_medialive.types.update_node_state_response.UpdateNodeStateResponse":
        """Update the state of a node.

        Args:
            cluster_id: The ID of the cluster
            node_id: The ID of the node.
            state: The state to apply to the Node. Set to ACTIVE (COMMISSIONED) to indicate that the Node is deployable. MediaLive Anywhere will consider this node it needs a Node to run a Channel on, or when it needs a Node to promote from a backup node to an active node. Set to DRAINING to isolate the Node so that MediaLive Anywhere won't use it.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.unprocessable_entity_exception.UnprocessableEntityException: Placeholder documentation for UnprocessableEntityException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_node_state_request.UpdateNodeStateRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_node_state_response.UpdateNodeStateResponse"
        ]:
            import capo_medialive._operations.media_live.update_node_state

            output, http_response = (
                capo_medialive._operations.media_live.update_node_state.update_node_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_node_state_request.UpdateNodeStateRequest = {
            "cluster_id": cluster_id,
            "node_id": node_id,
        }
        if state is not None:
            input_["state"] = state

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_reservation(
        self,
        reservation_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        renewal_settings: Optional[
            "capo_medialive.types.renewal_settings.RenewalSettings"
        ] = None,
    ) -> "capo_medialive.types.update_reservation_response.UpdateReservationResponse":
        """Update reservation.

        Args:
            name: Name of the reservation
            renewal_settings: Renewal settings for the reservation
            reservation_id: Unique reservation ID, e.g. '1234567'

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.not_found_exception.NotFoundException: Placeholder documentation for NotFoundException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_reservation_request.UpdateReservationRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_reservation_response.UpdateReservationResponse"
        ]:
            import capo_medialive._operations.media_live.update_reservation

            output, http_response = (
                capo_medialive._operations.media_live.update_reservation.update_reservation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_reservation_request.UpdateReservationRequest = {
            "reservation_id": reservation_id
        }
        if name is not None:
            input_["name"] = name
        if renewal_settings is not None:
            input_["renewal_settings"] = renewal_settings

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_sdi_source(
        self,
        sdi_source_id: "capo_medialive.types.__string.__string",
        *,
        config_overrides: Optional[MediaLiveClientConfig] = None,
        mode: Optional["capo_medialive.types.sdi_source_mode.SdiSourceMode"] = None,
        name: Optional["capo_medialive.types.__string.__string"] = None,
        type: Optional["capo_medialive.types.sdi_source_type.SdiSourceType"] = None,
    ) -> "capo_medialive.types.update_sdi_source_response.UpdateSdiSourceResponse":
        """Change some of the settings in an SdiSource.

        Args:
            mode: Include this parameter only if you want to change the name of the SdiSource. Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive.
            name: Include this parameter only if you want to change the name of the SdiSource. Specify a name that is unique in the AWS account. We recommend you assign a name that describes the source, for example curling-cameraA. Names are case-sensitive.
            sdi_source_id: The ID of the SdiSource
            type: Include this parameter only if you want to change the mode. Specify the type of the SDI source: SINGLE: The source is a single-link source. QUAD: The source is one part of a quad-link source.

        Raises:
            capo_medialive.errors.bad_gateway_exception.BadGatewayException: Placeholder documentation for BadGatewayException
            capo_medialive.errors.bad_request_exception.BadRequestException: Placeholder documentation for BadRequestException
            capo_medialive.errors.conflict_exception.ConflictException: Placeholder documentation for ConflictException
            capo_medialive.errors.forbidden_exception.ForbiddenException: Placeholder documentation for ForbiddenException
            capo_medialive.errors.gateway_timeout_exception.GatewayTimeoutException: Placeholder documentation for GatewayTimeoutException
            capo_medialive.errors.internal_server_error_exception.InternalServerErrorException: Placeholder documentation for InternalServerErrorException
            capo_medialive.errors.too_many_requests_exception.TooManyRequestsException: Placeholder documentation for TooManyRequestsException
            capo_medialive.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_medialive.types.update_sdi_source_request.UpdateSdiSourceRequest]",
        ) -> OperationResponse[
            "capo_medialive.types.update_sdi_source_response.UpdateSdiSourceResponse"
        ]:
            import capo_medialive._operations.media_live.update_sdi_source

            output, http_response = (
                capo_medialive._operations.media_live.update_sdi_source.update_sdi_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_medialive.types.update_sdi_source_request.UpdateSdiSourceRequest = {
            "sdi_source_id": sdi_source_id
        }
        if mode is not None:
            input_["mode"] = mode
        if name is not None:
            input_["name"] = name
        if type is not None:
            input_["type"] = type

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
