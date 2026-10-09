"""Generated from Smithy shape ``com.amazonaws.gamelift#GameLift``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_gamelift._auth._signers
import capo_gamelift._auth._sigv4
from capo_gamelift._auth._identity import Credentials
from capo_gamelift._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_gamelift._auth._zapros_handler import AuthMiddleware
from capo_gamelift._pagination import resolve_path as _resolve_path
from capo_gamelift._services._aws_config import aws_config
from capo_gamelift._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_gamelift.types.accept_match_input
    import capo_gamelift.types.accept_match_output
    import capo_gamelift.types.acceptance_type
    import capo_gamelift.types.alias
    import capo_gamelift.types.alias_id_or_arn
    import capo_gamelift.types.amazon_resource_name
    import capo_gamelift.types.anywhere_configuration
    import capo_gamelift.types.arn_string_model
    import capo_gamelift.types.backfill_mode
    import capo_gamelift.types.balancing_strategy
    import capo_gamelift.types.boolean_model
    import capo_gamelift.types.build
    import capo_gamelift.types.build_id_or_arn
    import capo_gamelift.types.build_status
    import capo_gamelift.types.certificate_configuration
    import capo_gamelift.types.claim_filter_option
    import capo_gamelift.types.claim_game_server_input
    import capo_gamelift.types.claim_game_server_output
    import capo_gamelift.types.comparison_operator_type
    import capo_gamelift.types.compute
    import capo_gamelift.types.compute_name
    import capo_gamelift.types.compute_name_or_arn
    import capo_gamelift.types.compute_type
    import capo_gamelift.types.connection_port_range
    import capo_gamelift.types.container_fleet
    import capo_gamelift.types.container_fleet_billing_type
    import capo_gamelift.types.container_fleet_remove_attribute_list
    import capo_gamelift.types.container_group_definition
    import capo_gamelift.types.container_group_definition_name
    import capo_gamelift.types.container_group_definition_name_or_arn
    import capo_gamelift.types.container_group_definition_remove_attribute_list
    import capo_gamelift.types.container_group_type
    import capo_gamelift.types.container_name_query_filter
    import capo_gamelift.types.container_operating_system
    import capo_gamelift.types.container_total_memory_limit
    import capo_gamelift.types.container_total_vcpu_limit
    import capo_gamelift.types.create_alias_input
    import capo_gamelift.types.create_alias_output
    import capo_gamelift.types.create_build_input
    import capo_gamelift.types.create_build_output
    import capo_gamelift.types.create_container_fleet_input
    import capo_gamelift.types.create_container_fleet_output
    import capo_gamelift.types.create_container_group_definition_input
    import capo_gamelift.types.create_container_group_definition_output
    import capo_gamelift.types.create_fleet_input
    import capo_gamelift.types.create_fleet_locations_input
    import capo_gamelift.types.create_fleet_locations_output
    import capo_gamelift.types.create_fleet_output
    import capo_gamelift.types.create_game_server_group_input
    import capo_gamelift.types.create_game_server_group_output
    import capo_gamelift.types.create_game_session_input
    import capo_gamelift.types.create_game_session_output
    import capo_gamelift.types.create_game_session_queue_input
    import capo_gamelift.types.create_game_session_queue_output
    import capo_gamelift.types.create_location_input
    import capo_gamelift.types.create_location_output
    import capo_gamelift.types.create_matchmaking_configuration_input
    import capo_gamelift.types.create_matchmaking_configuration_output
    import capo_gamelift.types.create_matchmaking_rule_set_input
    import capo_gamelift.types.create_matchmaking_rule_set_output
    import capo_gamelift.types.create_player_session_input
    import capo_gamelift.types.create_player_session_output
    import capo_gamelift.types.create_player_sessions_input
    import capo_gamelift.types.create_player_sessions_output
    import capo_gamelift.types.create_script_input
    import capo_gamelift.types.create_script_output
    import capo_gamelift.types.create_vpc_peering_authorization_input
    import capo_gamelift.types.create_vpc_peering_authorization_output
    import capo_gamelift.types.create_vpc_peering_connection_input
    import capo_gamelift.types.create_vpc_peering_connection_output
    import capo_gamelift.types.custom_event_data
    import capo_gamelift.types.custom_input_location_string_model
    import capo_gamelift.types.custom_location_name_or_arn_model
    import capo_gamelift.types.delete_alias_input
    import capo_gamelift.types.delete_build_input
    import capo_gamelift.types.delete_container_fleet_input
    import capo_gamelift.types.delete_container_fleet_output
    import capo_gamelift.types.delete_container_group_definition_input
    import capo_gamelift.types.delete_container_group_definition_output
    import capo_gamelift.types.delete_fleet_input
    import capo_gamelift.types.delete_fleet_locations_input
    import capo_gamelift.types.delete_fleet_locations_output
    import capo_gamelift.types.delete_game_server_group_input
    import capo_gamelift.types.delete_game_server_group_output
    import capo_gamelift.types.delete_game_session_queue_input
    import capo_gamelift.types.delete_game_session_queue_output
    import capo_gamelift.types.delete_location_input
    import capo_gamelift.types.delete_location_output
    import capo_gamelift.types.delete_matchmaking_configuration_input
    import capo_gamelift.types.delete_matchmaking_configuration_output
    import capo_gamelift.types.delete_matchmaking_rule_set_input
    import capo_gamelift.types.delete_matchmaking_rule_set_output
    import capo_gamelift.types.delete_scaling_policy_input
    import capo_gamelift.types.delete_script_input
    import capo_gamelift.types.delete_vpc_peering_authorization_input
    import capo_gamelift.types.delete_vpc_peering_authorization_output
    import capo_gamelift.types.delete_vpc_peering_connection_input
    import capo_gamelift.types.delete_vpc_peering_connection_output
    import capo_gamelift.types.deployment_configuration
    import capo_gamelift.types.deployment_id
    import capo_gamelift.types.deregister_compute_input
    import capo_gamelift.types.deregister_compute_output
    import capo_gamelift.types.deregister_game_server_input
    import capo_gamelift.types.describe_alias_input
    import capo_gamelift.types.describe_alias_output
    import capo_gamelift.types.describe_build_input
    import capo_gamelift.types.describe_build_output
    import capo_gamelift.types.describe_compute_input
    import capo_gamelift.types.describe_compute_output
    import capo_gamelift.types.describe_container_fleet_input
    import capo_gamelift.types.describe_container_fleet_output
    import capo_gamelift.types.describe_container_group_definition_input
    import capo_gamelift.types.describe_container_group_definition_output
    import capo_gamelift.types.describe_container_group_port_mappings_input
    import capo_gamelift.types.describe_container_group_port_mappings_output
    import capo_gamelift.types.describe_ec2_instance_limits_input
    import capo_gamelift.types.describe_ec2_instance_limits_output
    import capo_gamelift.types.describe_fleet_attributes_input
    import capo_gamelift.types.describe_fleet_attributes_output
    import capo_gamelift.types.describe_fleet_capacity_input
    import capo_gamelift.types.describe_fleet_capacity_output
    import capo_gamelift.types.describe_fleet_deployment_input
    import capo_gamelift.types.describe_fleet_deployment_output
    import capo_gamelift.types.describe_fleet_events_input
    import capo_gamelift.types.describe_fleet_events_output
    import capo_gamelift.types.describe_fleet_location_attributes_input
    import capo_gamelift.types.describe_fleet_location_attributes_output
    import capo_gamelift.types.describe_fleet_location_capacity_input
    import capo_gamelift.types.describe_fleet_location_capacity_output
    import capo_gamelift.types.describe_fleet_location_utilization_input
    import capo_gamelift.types.describe_fleet_location_utilization_output
    import capo_gamelift.types.describe_fleet_port_settings_input
    import capo_gamelift.types.describe_fleet_port_settings_output
    import capo_gamelift.types.describe_fleet_utilization_input
    import capo_gamelift.types.describe_fleet_utilization_output
    import capo_gamelift.types.describe_game_server_group_input
    import capo_gamelift.types.describe_game_server_group_output
    import capo_gamelift.types.describe_game_server_input
    import capo_gamelift.types.describe_game_server_instances_input
    import capo_gamelift.types.describe_game_server_instances_output
    import capo_gamelift.types.describe_game_server_output
    import capo_gamelift.types.describe_game_session_details_input
    import capo_gamelift.types.describe_game_session_details_output
    import capo_gamelift.types.describe_game_session_placement_input
    import capo_gamelift.types.describe_game_session_placement_output
    import capo_gamelift.types.describe_game_session_queues_input
    import capo_gamelift.types.describe_game_session_queues_output
    import capo_gamelift.types.describe_game_sessions_input
    import capo_gamelift.types.describe_game_sessions_output
    import capo_gamelift.types.describe_instances_input
    import capo_gamelift.types.describe_instances_output
    import capo_gamelift.types.describe_matchmaking_configurations_input
    import capo_gamelift.types.describe_matchmaking_configurations_output
    import capo_gamelift.types.describe_matchmaking_input
    import capo_gamelift.types.describe_matchmaking_output
    import capo_gamelift.types.describe_matchmaking_rule_sets_input
    import capo_gamelift.types.describe_matchmaking_rule_sets_output
    import capo_gamelift.types.describe_player_sessions_input
    import capo_gamelift.types.describe_player_sessions_output
    import capo_gamelift.types.describe_runtime_configuration_input
    import capo_gamelift.types.describe_runtime_configuration_output
    import capo_gamelift.types.describe_scaling_policies_input
    import capo_gamelift.types.describe_scaling_policies_output
    import capo_gamelift.types.describe_script_input
    import capo_gamelift.types.describe_script_output
    import capo_gamelift.types.describe_vpc_peering_authorizations_input
    import capo_gamelift.types.describe_vpc_peering_authorizations_output
    import capo_gamelift.types.describe_vpc_peering_connections_input
    import capo_gamelift.types.describe_vpc_peering_connections_output
    import capo_gamelift.types.desired_player_session_list
    import capo_gamelift.types.dns_name_input
    import capo_gamelift.types.double
    import capo_gamelift.types.ec2_instance_type
    import capo_gamelift.types.event
    import capo_gamelift.types.filter_configuration
    import capo_gamelift.types.fleet_action_list
    import capo_gamelift.types.fleet_attributes
    import capo_gamelift.types.fleet_capacity
    import capo_gamelift.types.fleet_deployment
    import capo_gamelift.types.fleet_id
    import capo_gamelift.types.fleet_id_or_arn
    import capo_gamelift.types.fleet_id_or_arn_list
    import capo_gamelift.types.fleet_type
    import capo_gamelift.types.fleet_utilization
    import capo_gamelift.types.flex_match_mode
    import capo_gamelift.types.game_property_list
    import capo_gamelift.types.game_server
    import capo_gamelift.types.game_server_connection_info
    import capo_gamelift.types.game_server_container_definition_input
    import capo_gamelift.types.game_server_container_groups_per_instance
    import capo_gamelift.types.game_server_data
    import capo_gamelift.types.game_server_group
    import capo_gamelift.types.game_server_group_actions
    import capo_gamelift.types.game_server_group_auto_scaling_policy
    import capo_gamelift.types.game_server_group_delete_option
    import capo_gamelift.types.game_server_group_name
    import capo_gamelift.types.game_server_group_name_or_arn
    import capo_gamelift.types.game_server_health_check
    import capo_gamelift.types.game_server_id
    import capo_gamelift.types.game_server_instance
    import capo_gamelift.types.game_server_instance_id
    import capo_gamelift.types.game_server_instance_ids
    import capo_gamelift.types.game_server_protection_policy
    import capo_gamelift.types.game_server_utilization_status
    import capo_gamelift.types.game_session
    import capo_gamelift.types.game_session_creation_limit_policy
    import capo_gamelift.types.game_session_data
    import capo_gamelift.types.game_session_detail
    import capo_gamelift.types.game_session_queue
    import capo_gamelift.types.game_session_queue_destination_list
    import capo_gamelift.types.game_session_queue_name
    import capo_gamelift.types.game_session_queue_name_or_arn
    import capo_gamelift.types.game_session_queue_name_or_arn_list
    import capo_gamelift.types.get_compute_access_input
    import capo_gamelift.types.get_compute_access_output
    import capo_gamelift.types.get_compute_auth_token_input
    import capo_gamelift.types.get_compute_auth_token_output
    import capo_gamelift.types.get_game_session_log_url_input
    import capo_gamelift.types.get_game_session_log_url_output
    import capo_gamelift.types.get_instance_access_input
    import capo_gamelift.types.get_instance_access_output
    import capo_gamelift.types.get_player_connection_details_input
    import capo_gamelift.types.get_player_connection_details_output
    import capo_gamelift.types.iam_role_arn
    import capo_gamelift.types.id_string_model
    import capo_gamelift.types.instance
    import capo_gamelift.types.instance_definitions
    import capo_gamelift.types.instance_id
    import capo_gamelift.types.instance_role_credentials_provider
    import capo_gamelift.types.integer
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.ip_permissions_list
    import capo_gamelift.types.large_game_session_data
    import capo_gamelift.types.launch_parameters_string_model
    import capo_gamelift.types.launch_path_string_model
    import capo_gamelift.types.launch_template_specification
    import capo_gamelift.types.list_aliases_input
    import capo_gamelift.types.list_aliases_output
    import capo_gamelift.types.list_builds_input
    import capo_gamelift.types.list_builds_output
    import capo_gamelift.types.list_compute_input
    import capo_gamelift.types.list_compute_input_status
    import capo_gamelift.types.list_compute_output
    import capo_gamelift.types.list_container_fleets_input
    import capo_gamelift.types.list_container_fleets_output
    import capo_gamelift.types.list_container_group_definition_versions_input
    import capo_gamelift.types.list_container_group_definition_versions_limit
    import capo_gamelift.types.list_container_group_definition_versions_output
    import capo_gamelift.types.list_container_group_definitions_input
    import capo_gamelift.types.list_container_group_definitions_limit
    import capo_gamelift.types.list_container_group_definitions_output
    import capo_gamelift.types.list_fleet_deployments_input
    import capo_gamelift.types.list_fleet_deployments_output
    import capo_gamelift.types.list_fleets_input
    import capo_gamelift.types.list_fleets_output
    import capo_gamelift.types.list_game_server_groups_input
    import capo_gamelift.types.list_game_server_groups_output
    import capo_gamelift.types.list_game_servers_input
    import capo_gamelift.types.list_game_servers_output
    import capo_gamelift.types.list_locations_input
    import capo_gamelift.types.list_locations_limit
    import capo_gamelift.types.list_locations_output
    import capo_gamelift.types.list_scripts_input
    import capo_gamelift.types.list_scripts_output
    import capo_gamelift.types.list_tags_for_resource_request
    import capo_gamelift.types.list_tags_for_resource_response
    import capo_gamelift.types.location_configuration_list
    import capo_gamelift.types.location_filter_list
    import capo_gamelift.types.location_list
    import capo_gamelift.types.location_model
    import capo_gamelift.types.location_string_model
    import capo_gamelift.types.log_configuration
    import capo_gamelift.types.managed_capacity_configuration
    import capo_gamelift.types.matchmaking_acceptance_timeout_integer
    import capo_gamelift.types.matchmaking_configuration
    import capo_gamelift.types.matchmaking_configuration_name
    import capo_gamelift.types.matchmaking_configuration_name_list
    import capo_gamelift.types.matchmaking_id_list
    import capo_gamelift.types.matchmaking_id_string_model
    import capo_gamelift.types.matchmaking_request_timeout_integer
    import capo_gamelift.types.matchmaking_rule_set
    import capo_gamelift.types.matchmaking_rule_set_name
    import capo_gamelift.types.matchmaking_rule_set_name_list
    import capo_gamelift.types.metric_group_list
    import capo_gamelift.types.metric_name
    import capo_gamelift.types.node_js_version
    import capo_gamelift.types.non_blank_and_length_constraint_string
    import capo_gamelift.types.non_empty_string
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.operating_system
    import capo_gamelift.types.player_data
    import capo_gamelift.types.player_data_map
    import capo_gamelift.types.player_gateway_configuration
    import capo_gamelift.types.player_gateway_mode
    import capo_gamelift.types.player_id
    import capo_gamelift.types.player_id_list
    import capo_gamelift.types.player_ids_for_accept_match
    import capo_gamelift.types.player_latency_list
    import capo_gamelift.types.player_latency_policy_list
    import capo_gamelift.types.player_list
    import capo_gamelift.types.player_session
    import capo_gamelift.types.player_session_creation_policy
    import capo_gamelift.types.player_session_id
    import capo_gamelift.types.policy_type
    import capo_gamelift.types.positive_integer
    import capo_gamelift.types.priority_configuration
    import capo_gamelift.types.priority_configuration_override
    import capo_gamelift.types.protection_policy
    import capo_gamelift.types.put_scaling_policy_input
    import capo_gamelift.types.put_scaling_policy_output
    import capo_gamelift.types.queue_arns_list
    import capo_gamelift.types.queue_custom_event_data
    import capo_gamelift.types.queue_sns_arn_string_model
    import capo_gamelift.types.register_compute_input
    import capo_gamelift.types.register_compute_output
    import capo_gamelift.types.register_game_server_input
    import capo_gamelift.types.register_game_server_output
    import capo_gamelift.types.request_upload_credentials_input
    import capo_gamelift.types.request_upload_credentials_output
    import capo_gamelift.types.resolve_alias_input
    import capo_gamelift.types.resolve_alias_output
    import capo_gamelift.types.resource_creation_limit_policy
    import capo_gamelift.types.resume_game_server_group_input
    import capo_gamelift.types.resume_game_server_group_output
    import capo_gamelift.types.routing_strategy
    import capo_gamelift.types.routing_strategy_type
    import capo_gamelift.types.rule_set_body
    import capo_gamelift.types.rule_set_limit
    import capo_gamelift.types.runtime_configuration
    import capo_gamelift.types.s3_location
    import capo_gamelift.types.scaling_adjustment_type
    import capo_gamelift.types.scaling_policy
    import capo_gamelift.types.scaling_status_type
    import capo_gamelift.types.script
    import capo_gamelift.types.script_id_or_arn
    import capo_gamelift.types.search_game_sessions_input
    import capo_gamelift.types.search_game_sessions_output
    import capo_gamelift.types.server_sdk_version
    import capo_gamelift.types.sns_arn_string_model
    import capo_gamelift.types.sort_order
    import capo_gamelift.types.start_fleet_actions_input
    import capo_gamelift.types.start_fleet_actions_output
    import capo_gamelift.types.start_game_session_placement_input
    import capo_gamelift.types.start_game_session_placement_output
    import capo_gamelift.types.start_match_backfill_input
    import capo_gamelift.types.start_match_backfill_output
    import capo_gamelift.types.start_matchmaking_input
    import capo_gamelift.types.start_matchmaking_output
    import capo_gamelift.types.stop_fleet_actions_input
    import capo_gamelift.types.stop_fleet_actions_output
    import capo_gamelift.types.stop_game_session_placement_input
    import capo_gamelift.types.stop_game_session_placement_output
    import capo_gamelift.types.stop_matchmaking_input
    import capo_gamelift.types.stop_matchmaking_output
    import capo_gamelift.types.string_list
    import capo_gamelift.types.support_container_definition_input_list
    import capo_gamelift.types.suspend_game_server_group_input
    import capo_gamelift.types.suspend_game_server_group_output
    import capo_gamelift.types.tag_key_list
    import capo_gamelift.types.tag_list
    import capo_gamelift.types.tag_resource_request
    import capo_gamelift.types.tag_resource_response
    import capo_gamelift.types.target_configuration
    import capo_gamelift.types.terminate_game_session_input
    import capo_gamelift.types.terminate_game_session_output
    import capo_gamelift.types.termination_mode
    import capo_gamelift.types.timestamp
    import capo_gamelift.types.untag_resource_request
    import capo_gamelift.types.untag_resource_response
    import capo_gamelift.types.update_alias_input
    import capo_gamelift.types.update_alias_output
    import capo_gamelift.types.update_build_input
    import capo_gamelift.types.update_build_output
    import capo_gamelift.types.update_container_fleet_input
    import capo_gamelift.types.update_container_fleet_output
    import capo_gamelift.types.update_container_group_definition_input
    import capo_gamelift.types.update_container_group_definition_output
    import capo_gamelift.types.update_fleet_attributes_input
    import capo_gamelift.types.update_fleet_attributes_output
    import capo_gamelift.types.update_fleet_capacity_input
    import capo_gamelift.types.update_fleet_capacity_output
    import capo_gamelift.types.update_fleet_port_settings_input
    import capo_gamelift.types.update_fleet_port_settings_output
    import capo_gamelift.types.update_game_server_group_input
    import capo_gamelift.types.update_game_server_group_output
    import capo_gamelift.types.update_game_server_input
    import capo_gamelift.types.update_game_server_output
    import capo_gamelift.types.update_game_session_input
    import capo_gamelift.types.update_game_session_output
    import capo_gamelift.types.update_game_session_queue_input
    import capo_gamelift.types.update_game_session_queue_output
    import capo_gamelift.types.update_matchmaking_configuration_input
    import capo_gamelift.types.update_matchmaking_configuration_output
    import capo_gamelift.types.update_runtime_configuration_input
    import capo_gamelift.types.update_runtime_configuration_output
    import capo_gamelift.types.update_script_input
    import capo_gamelift.types.update_script_output
    import capo_gamelift.types.validate_matchmaking_rule_set_input
    import capo_gamelift.types.validate_matchmaking_rule_set_output
    import capo_gamelift.types.vpc_subnets
    import capo_gamelift.types.whole_number
    import capo_gamelift.types.zip_blob


class GameLiftClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class GameLiftClient:
    """A client for the ``GameLift`` service.

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
        self._config = GameLiftClientConfig(
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
        self, config_overrides: Optional[GameLiftClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: GameLiftClientConfig = config_overrides or {}
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

    def accept_match(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        ticket_id: Optional[
            "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
        ] = None,
        player_ids: Optional[
            "capo_gamelift.types.player_ids_for_accept_match.PlayerIdsForAcceptMatch"
        ] = None,
        acceptance_type: Optional[
            "capo_gamelift.types.acceptance_type.AcceptanceType"
        ] = None,
    ) -> "capo_gamelift.types.accept_match_output.AcceptMatchOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Registers a player's acceptance or rejection of a proposed FlexMatch match. A matchmaking configuration may require player acceptance; if so, then matches built with that configuration cannot be completed unless all players accept the proposed match within a specified time limit. </p> <p>When FlexMatch builds a match, all the matchmaking tickets involved in the proposed match are placed into status <code>REQUIRES_ACCEPTANCE</code>. This is a trigger for your game to get acceptance from all players in each ticket. Calls to this action are only valid for tickets that are in this status; calls for tickets not in this status result in an error.</p> <p>To register acceptance, specify the ticket ID, one or more players, and an acceptance response. When all players have accepted, Amazon GameLift Servers advances the matchmaking tickets to status <code>PLACING</code>, and attempts to create a new game session for the match. </p> <p>If any player rejects the match, or if acceptances are not received before a specified timeout, the proposed match is dropped. Each matchmaking ticket in the failed match is handled as follows: </p> <ul> <li> <p>If the ticket has one or more players who rejected the match or failed to respond, the ticket status is set to <code>CANCELLED</code> and processing is terminated.</p> </li> <li> <p>If all players in the ticket accepted the match, the ticket status is returned to <code>SEARCHING</code> to find a new match. </p> </li> </ul> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html"> Add FlexMatch to a game client</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html"> FlexMatch events</a> (reference)</p>

        Args:
            ticket_id: <p>A unique identifier for a matchmaking ticket. The ticket must be in status <code>REQUIRES_ACCEPTANCE</code>; otherwise this request will fail.</p>
            player_ids: <p>A unique identifier for a player delivering the response. This parameter can include one or multiple player IDs.</p>
            acceptance_type: <p>Player response to the proposed match.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.accept_match_input.AcceptMatchInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.accept_match_output.AcceptMatchOutput"
        ]:
            import capo_gamelift._operations.game_lift.accept_match

            output, http_response = (
                capo_gamelift._operations.game_lift.accept_match.accept_match(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.accept_match_input.AcceptMatchInput = {}
        if ticket_id is not None:
            input_["ticket_id"] = ticket_id
        if player_ids is not None:
            input_["player_ids"] = player_ids
        if acceptance_type is not None:
            input_["acceptance_type"] = acceptance_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def claim_game_server(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        game_server_id: Optional[
            "capo_gamelift.types.game_server_id.GameServerId"
        ] = None,
        game_server_data: Optional[
            "capo_gamelift.types.game_server_data.GameServerData"
        ] = None,
        filter_option: Optional[
            "capo_gamelift.types.claim_filter_option.ClaimFilterOption"
        ] = None,
    ) -> "capo_gamelift.types.claim_game_server_output.ClaimGameServerOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Locates an available game server and temporarily reserves it to host gameplay and players. This operation is called from a game client or client service (such as a matchmaker) to request hosting resources for a new game session. In response, Amazon GameLift Servers FleetIQ locates an available game server, places it in <code>CLAIMED</code> status for 60 seconds, and returns connection information that players can use to connect to the game server. </p> <p>To claim a game server, identify a game server group. You can also specify a game server ID, although this approach bypasses Amazon GameLift Servers FleetIQ placement optimization. Optionally, include game data to pass to the game server at the start of a game session, such as a game map or player information. Add filter options to further restrict how a game server is chosen, such as only allowing game servers on <code>ACTIVE</code> instances to be claimed.</p> <p>When a game server is successfully claimed, connection information is returned. A claimed game server's utilization status remains <code>AVAILABLE</code> while the claim status is set to <code>CLAIMED</code> for up to 60 seconds. This time period gives the game server time to update its status to <code>UTILIZED</code> after players join. If the game server's status is not updated within 60 seconds, the game server reverts to unclaimed status and is available to be claimed by another request. The claim time period is a fixed value and is not configurable.</p> <p>If you try to claim a specific game server, this request will fail in the following cases:</p> <ul> <li> <p>If the game server utilization status is <code>UTILIZED</code>.</p> </li> <li> <p>If the game server claim status is <code>CLAIMED</code>.</p> </li> <li> <p>If the game server is running on an instance in <code>DRAINING</code> status and the provided filter option does not allow placing on <code>DRAINING</code> instances.</p> </li> </ul> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group where the game server is running. If you are not specifying a game server to claim, this value identifies where you want Amazon GameLift Servers FleetIQ to look for an available game server to claim. </p>
            game_server_id: <p>A custom string that uniquely identifies the game server to claim. If this parameter is left empty, Amazon GameLift Servers FleetIQ searches for an available game server in the specified game server group.</p>
            game_server_data: <p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers. </p>
            filter_option: <p>Object that restricts how a claimed game server is chosen.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.out_of_capacity_exception.OutOfCapacityException: <p>The specified game server group has no available game servers to fulfill a <code>ClaimGameServer</code> request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.claim_game_server_input.ClaimGameServerInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.claim_game_server_output.ClaimGameServerOutput"
        ]:
            import capo_gamelift._operations.game_lift.claim_game_server

            output, http_response = (
                capo_gamelift._operations.game_lift.claim_game_server.claim_game_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.claim_game_server_input.ClaimGameServerInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if game_server_id is not None:
            input_["game_server_id"] = game_server_id
        if game_server_data is not None:
            input_["game_server_data"] = game_server_data
        if filter_option is not None:
            input_["filter_option"] = filter_option

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_alias(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.non_blank_and_length_constraint_string.NonBlankAndLengthConstraintString"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        routing_strategy: Optional[
            "capo_gamelift.types.routing_strategy.RoutingStrategy"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_alias_output.CreateAliasOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Creates an alias for a fleet. In most situations, you can use an alias ID in place of a fleet ID. An alias provides a level of abstraction for a fleet that is useful when redirecting player traffic from one fleet to another, such as when updating your game build. </p> <p>Amazon GameLift Servers supports two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias is used to display messaging or link to a URL instead of routing players to an active fleet. For example, you might use a terminal alias when a game version is no longer supported and you want to direct players to an upgrade site. </p> <p>To create a fleet alias, specify an alias name, routing strategy, and optional description. Each simple alias can point to only one fleet, but a fleet can have multiple aliases. If successful, a new alias record is returned, including an alias ID and an ARN. You can reassign an alias to another fleet by calling <code>UpdateAlias</code>.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            name: <p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>
            description: <p>A human-readable description of the alias.</p>
            routing_strategy: <p>The routing configuration, including routing type and fleet target, for the alias. </p>
            tags: <p>A list of labels to assign to the new alias resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_alias_input.CreateAliasInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_alias_output.CreateAliasOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_alias

            output, http_response = (
                capo_gamelift._operations.game_lift.create_alias.create_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_alias_input.CreateAliasInput = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if routing_strategy is not None:
            input_["routing_strategy"] = routing_strategy
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_build(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        version: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        storage_location: Optional["capo_gamelift.types.s3_location.S3Location"] = None,
        operating_system: Optional[
            "capo_gamelift.types.operating_system.OperatingSystem"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
        server_sdk_version: Optional[
            "capo_gamelift.types.server_sdk_version.ServerSdkVersion"
        ] = None,
    ) -> "capo_gamelift.types.create_build_output.CreateBuildOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere</p> <p>Creates a new Amazon GameLift Servers build resource for your game server binary files. Combine game server binaries into a zip file for use with Amazon GameLift Servers. </p> <important> <p>When setting up a new game build for Amazon GameLift Servers, we recommend using the CLI command <b> <a href="https://docs.aws.amazon.com/cli/latest/reference/gamelift/upload-build.html">upload-build</a> </b>. This helper command combines two tasks: (1) it uploads your build files from a file directory to an Amazon GameLift Servers Amazon S3 location, and (2) it creates a new build resource.</p> </important> <p>You can use the <code>CreateBuild</code> operation in the following scenarios:</p> <ul> <li> <p>Create a new game build with build files that are in an Amazon S3 location under an Amazon Web Services account that you control. To use this option, you give Amazon GameLift Servers access to the Amazon S3 bucket. With permissions in place, specify a build name, operating system, and the Amazon S3 storage location of your game build.</p> </li> <li> <p>Upload your build files to a Amazon GameLift Servers Amazon S3 location. To use this option, specify a build name and operating system. This operation creates a new build resource and also returns an Amazon S3 location with temporary access credentials. Use the credentials to manually upload your build files to the specified Amazon S3 location. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html">Uploading Objects</a> in the <i>Amazon S3 Developer Guide</i>. After you upload build files to the Amazon GameLift Servers Amazon S3 location, you can't update them. </p> </li> </ul> <p>If successful, this operation creates a new build resource with a unique build ID and places it in <code>INITIALIZED</code> status. A build must be in <code>READY</code> status before you can create fleets with it.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html">Uploading Your Game</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build"> Create a Build with Files in Amazon S3</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            name: <p>A descriptive label that is associated with a build. Build names do not need to be unique. You can change this value later. </p>
            version: <p>Version information that is associated with a build or script. Version strings do not need to be unique. You can change this value later. </p>
            storage_location: <p>Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift Servers to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.</p> <p>If a <code>StorageLocation</code> is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift Servers will report a <code>SizeOnDisk</code> of 0. </p>
            operating_system: <p>The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note> <note> <p>Windows Server 2016 will reach end of support on 1/12/2027. For game servers that are hosted on Windows Server 2016 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to Windows Server 2022 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>
            tags: <p>A list of labels to assign to the new build resource. Tags are developer defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. Once the resource is created, you can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html">TagResource</a>, <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html">UntagResource</a>, and <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to add, remove, and view tags. The maximum tag limit may be lower than stated. See the Amazon Web Services General Reference for actual tagging limits.</p>
            server_sdk_version: <p>A server SDK version you used when integrating your game server build with Amazon GameLift Servers. For more information see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html">Integrate games with custom game servers</a>. By default Amazon GameLift Servers sets this value to <code>4.0.2</code>.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_build_input.CreateBuildInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_build_output.CreateBuildOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_build

            output, http_response = (
                capo_gamelift._operations.game_lift.create_build.create_build(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_build_input.CreateBuildInput = {}
        if name is not None:
            input_["name"] = name
        if version is not None:
            input_["version"] = version
        if storage_location is not None:
            input_["storage_location"] = storage_location
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if tags is not None:
            input_["tags"] = tags
        if server_sdk_version is not None:
            input_["server_sdk_version"] = server_sdk_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_container_fleet(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_role_arn: Optional["capo_gamelift.types.iam_role_arn.IamRoleArn"] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        game_server_container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        per_instance_container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        instance_connection_port_range: Optional[
            "capo_gamelift.types.connection_port_range.ConnectionPortRange"
        ] = None,
        instance_inbound_permissions: Optional[
            "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
        ] = None,
        game_server_container_groups_per_instance: Optional[
            "capo_gamelift.types.game_server_container_groups_per_instance.GameServerContainerGroupsPerInstance"
        ] = None,
        instance_type: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        billing_type: Optional[
            "capo_gamelift.types.container_fleet_billing_type.ContainerFleetBillingType"
        ] = None,
        locations: Optional[
            "capo_gamelift.types.location_configuration_list.LocationConfigurationList"
        ] = None,
        metric_groups: Optional[
            "capo_gamelift.types.metric_group_list.MetricGroupList"
        ] = None,
        new_game_session_protection_policy: Optional[
            "capo_gamelift.types.protection_policy.ProtectionPolicy"
        ] = None,
        game_session_creation_limit_policy: Optional[
            "capo_gamelift.types.game_session_creation_limit_policy.GameSessionCreationLimitPolicy"
        ] = None,
        log_configuration: Optional[
            "capo_gamelift.types.log_configuration.LogConfiguration"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
        player_gateway_mode: Optional[
            "capo_gamelift.types.player_gateway_mode.PlayerGatewayMode"
        ] = None,
    ) -> "capo_gamelift.types.create_container_fleet_output.CreateContainerFleetOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Creates a managed fleet of Amazon Elastic Compute Cloud (Amazon EC2) instances to host your containerized game servers. Use this operation to define how to deploy a container architecture onto each fleet instance and configure fleet settings. You can create a container fleet in any Amazon Web Services Regions that Amazon GameLift Servers supports for multi-location fleets. A container fleet can be deployed to a single location or multiple locations. Container fleets are deployed with Amazon Linux 2023 as the instance operating system.</p> <p>Define the fleet's container architecture using container group definitions. Each fleet can have one of the following container group types:</p> <ul> <li> <p>The game server container group runs your game server build and dependent software. Amazon GameLift Servers deploys one or more replicas of this container group to each fleet instance. The number of replicas depends on the computing capabilities of the fleet instance in use. </p> </li> <li> <p>An optional per-instance container group might be used to run other software that only needs to run once per instance, such as background services, logging, or test processes. One per-instance container group is deployed to each fleet instance. </p> </li> </ul> <p>Each container group can include the definition for one or more containers. A container definition specifies a container image that is stored in an Amazon Elastic Container Registry (Amazon ECR) public or private repository.</p> <p> <b>Request options</b> </p> <p>Use this operation to make the following types of requests. Most fleet settings have default values, so you can create a working fleet with a minimal configuration and default values, which you can customize later.</p> <ul> <li> <p>Create a fleet with no container groups. You can configure a container fleet and then add container group definitions later. In this scenario, no fleet instances are deployed, and the fleet can't host game sessions until you add a game server container group definition. Provide the following required parameter values:</p> <ul> <li> <p> <code>FleetRoleArn</code> </p> </li> </ul> </li> <li> <p>Create a fleet with a game server container group. Provide the following required parameter values:</p> <ul> <li> <p> <code>FleetRoleArn</code> </p> </li> <li> <p> <code>GameServerContainerGroupDefinitionName</code> </p> </li> </ul> </li> <li> <p>Create a fleet with a game server container group and a per-instance container group. Provide the following required parameter values:</p> <ul> <li> <p> <code>FleetRoleArn</code> </p> </li> <li> <p> <code>GameServerContainerGroupDefinitionName</code> </p> </li> <li> <p> <code>PerInstanceContainerGroupDefinitionName</code> </p> </li> </ul> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation creates a new container fleet resource, places it in <code>PENDING</code> status, and initiates the <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow">fleet creation workflow</a>. For fleets with container groups, this workflow starts a fleet deployment and transitions the status to <code>ACTIVE</code>. Fleets without a container group are placed in <code>CREATED</code> status.</p> <p>You can update most of the properties of a fleet, including container group definitions, and deploy the update across all fleet instances. Use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerFleet.html">UpdateContainerFleet</a> to deploy a new game server version update across the container fleet. </p> <note> <p>A managed fleet's runtime environment depends on the Amazon Machine Image (AMI) version it uses. When a new fleet is created, Amazon GameLift Servers assigns the latest available AMI version to the fleet, and all compute instances in that fleet are deployed with that version. To update the AMI version, you must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html"> Security best practices for Amazon GameLift Servers</a>.</p> </note>

        Args:
            fleet_role_arn: <p>The unique identifier for an Identity and Access Management (IAM) role with permissions to run your containers on resources that are managed by Amazon GameLift Servers. Use an IAM service role with the <code>GameLiftContainerFleetPolicy</code> managed policy attached. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html">Set up an IAM service role</a>. You can't change this fleet property after the fleet is created.</p> <p>IAM role ARN values use the following pattern: <code>arn:aws:iam::[Amazon Web Services account]:role/[role name]</code>.</p>
            description: <p>A meaningful description of the container fleet.</p>
            game_server_container_group_definition_name: <p>A container group definition resource that describes how to deploy containers with your game server build and support software onto each fleet instance. You can specify the container group definition's name to use the latest version. Alternatively, provide an ARN value with a specific version number.</p> <p>Create a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html">CreateContainerGroupDefinition</a>. This operation creates a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html">ContainerGroupDefinition</a> resource. </p>
            per_instance_container_group_definition_name: <p>The name of a container group definition resource that describes a set of auxiliary software. A fleet instance has one process for executables in this container group. A per-instance container group is optional. You can update the fleet to add or remove a per-instance container group at any time. You can specify the container group definition's name to use the latest version. Alternatively, provide an ARN value with a specific version number. </p> <p>Create a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html">https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerGroupDefinition.html</a>. This operation creates a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html">https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html</a> resource.</p>
            instance_connection_port_range: <p>The set of port numbers to open on each fleet instance. A fleet's connection ports map to container ports that are configured in the fleet's container group definitions. </p> <p>By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. To use the calculated range, don't set this parameter. The values are:</p> <ul> <li> <p>Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift Servers uses the following formula: <code>4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the per instance container group definition]</code> </p> </li> </ul> <p>You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleet's inbound permissions port range.</p> <note> <p>If you set values manually, Amazon GameLift Servers no longer calculates a port range for you, even if you later remove the manual settings. </p> </note> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>
            instance_inbound_permissions: <p>The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. As a best practice, when remotely accessing a fleet instance, we recommend opening ports only when you need them and closing them when you're finished.</p> <p>By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. To use the calculated range, don't set this parameter. The values are:</p> <ul> <li> <p>Protocol: UDP</p> </li> <li> <p>Port range: 4192 to a number calculated based on your fleet configuration. Amazon GameLift Servers uses the following formula: <code>4192 + [# of game server container groups per fleet instance] * [# of container ports in the game server container group definition] + [# of container ports in the per instance container group definition]</code> </p> </li> </ul> <p>You can also choose to manually set this parameter. When manually setting this parameter, you must use port numbers that match the fleet's connection port range.</p> <note> <p>If you set values manually, Amazon GameLift Servers no longer calculates a port range for you, even if you later remove the manual settings. </p> </note> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>
            game_server_container_groups_per_instance: <p>The number of times to replicate the game server container group on each fleet instance. </p> <p>By default, Amazon GameLift Servers calculates the maximum number of game server container groups that can fit on each instance. This calculation is based on the CPU and memory resources of the fleet's instance type. To use the calculated maximum, don't set this parameter. If you set this number manually, Amazon GameLift Servers uses your value as long as it's less than the calculated maximum.</p>
            instance_type: <p>The Amazon EC2 instance type to use for all instances in the fleet. For multi-location fleets, the instance type must be available in the home region and all remote locations. Instance type determines the computing resources and processing power that's available to host your game servers. This includes CPU, memory, storage, and networking capacity. </p> <p>By default, Amazon GameLift Servers uses the <code>c5.large</code> instance type. If this instance type does not have sufficient resources for your container groups, you can choose a different instance type that better fits your needs. See <a href="http://aws.amazon.com/ec2/instance-types/">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions of Amazon EC2 instance types.</p> <p>You can't update this fleet property later.</p>
            billing_type: <p>Indicates whether to use On-Demand or Spot instances for this fleet. Learn more about when to use <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot"> On-Demand versus Spot Instances</a>. This fleet property can't be changed after the fleet is created.</p> <p>By default, this property is set to <code>ON_DEMAND</code>.</p> <p>You can't update this fleet property later.</p>
            locations: <p>A set of locations to deploy container fleet instances to. You can add any Amazon Web Services Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more Amazon Web Services Region codes, such as <code>us-west-2</code>, or Local Zone names. Also include the fleet's home Region, which is the Amazon Web Services Region where the fleet is created. For a list of supported Regions and Local Zones, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting.</p>
            metric_groups: <p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. You can use a metric group to aggregate metrics for multiple fleets. You can specify an existing metric group name or use a new name to create a new metric group. Each fleet can have only one metric group, but you can change this value at any time. </p>
            new_game_session_protection_policy: <p>Determines whether Amazon GameLift Servers can shut down game sessions on the fleet that are actively running and hosting players. Amazon GameLift Servers might prompt an instance shutdown when scaling down fleet capacity or when retiring unhealthy instances. You can also set game session protection for individual game sessions using <a href="gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a>.</p> <ul> <li> <p> <b>NoProtection</b> -- Game sessions can be shut down during active gameplay. </p> </li> <li> <p> <b>FullProtection</b> -- Game sessions in <code>ACTIVE</code> status can't be shut down.</p> </li> </ul> <p>By default, this property is set to <code>NoProtection</code>. </p>
            game_session_creation_limit_policy: <p>A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.</p>
            log_configuration: <p>A method for collecting container logs for the fleet. Amazon GameLift Servers saves all standard output for each container in logs, including game session logs. You can select from the following methods: </p> <ul> <li> <p> <code>CLOUDWATCH</code> -- Send logs to an Amazon CloudWatch log group that you define. Each container emits a log stream, which is organized in the log group. </p> </li> <li> <p> <code>S3</code> -- Store logs in an Amazon S3 bucket that you define.</p> </li> <li> <p> <code>NONE</code> -- Don't collect container logs.</p> </li> </ul> <p>By default, this property is set to <code>CLOUDWATCH</code>. </p> <p>Amazon GameLift Servers requires permissions to send logs to other Amazon Web Services services in your account. These permissions are included in the IAM fleet role for this container fleet (see <code>FleetRoleArn</code>).</p>
            tags: <p>A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>
            player_gateway_mode: <p>Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traffic before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy.</p> <p> <b>How it works:</b> When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html">DDoS protection with Amazon GameLift Servers player gateway</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>DISABLED</code> (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.</p> </li> <li> <p> <code>ENABLED</code> -- Player gateway is available in fleet locations where it is supported. Your game backend can call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to obtain a player gateway token and endpoints for game clients.</p> </li> <li> <p> <code>REQUIRED</code> -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an <code>InvalidRequestException</code>.</p> </li> </ul>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_container_fleet_input.CreateContainerFleetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_container_fleet_output.CreateContainerFleetOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_container_fleet

            output, http_response = (
                capo_gamelift._operations.game_lift.create_container_fleet.create_container_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_container_fleet_input.CreateContainerFleetInput = {}
        if fleet_role_arn is not None:
            input_["fleet_role_arn"] = fleet_role_arn
        if description is not None:
            input_["description"] = description
        if game_server_container_group_definition_name is not None:
            input_["game_server_container_group_definition_name"] = (
                game_server_container_group_definition_name
            )
        if per_instance_container_group_definition_name is not None:
            input_["per_instance_container_group_definition_name"] = (
                per_instance_container_group_definition_name
            )
        if instance_connection_port_range is not None:
            input_["instance_connection_port_range"] = instance_connection_port_range
        if instance_inbound_permissions is not None:
            input_["instance_inbound_permissions"] = instance_inbound_permissions
        if game_server_container_groups_per_instance is not None:
            input_["game_server_container_groups_per_instance"] = (
                game_server_container_groups_per_instance
            )
        if instance_type is not None:
            input_["instance_type"] = instance_type
        if billing_type is not None:
            input_["billing_type"] = billing_type
        if locations is not None:
            input_["locations"] = locations
        if metric_groups is not None:
            input_["metric_groups"] = metric_groups
        if new_game_session_protection_policy is not None:
            input_["new_game_session_protection_policy"] = (
                new_game_session_protection_policy
            )
        if game_session_creation_limit_policy is not None:
            input_["game_session_creation_limit_policy"] = (
                game_session_creation_limit_policy
            )
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if tags is not None:
            input_["tags"] = tags
        if player_gateway_mode is not None:
            input_["player_gateway_mode"] = player_gateway_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_container_group_definition(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.container_group_definition_name.ContainerGroupDefinitionName"
        ] = None,
        container_group_type: Optional[
            "capo_gamelift.types.container_group_type.ContainerGroupType"
        ] = None,
        total_memory_limit_mebibytes: Optional[
            "capo_gamelift.types.container_total_memory_limit.ContainerTotalMemoryLimit"
        ] = None,
        total_vcpu_limit: Optional[
            "capo_gamelift.types.container_total_vcpu_limit.ContainerTotalVcpuLimit"
        ] = None,
        game_server_container_definition: Optional[
            "capo_gamelift.types.game_server_container_definition_input.GameServerContainerDefinitionInput"
        ] = None,
        support_container_definitions: Optional[
            "capo_gamelift.types.support_container_definition_input_list.SupportContainerDefinitionInputList"
        ] = None,
        operating_system: Optional[
            "capo_gamelift.types.container_operating_system.ContainerOperatingSystem"
        ] = None,
        version_description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_container_group_definition_output.CreateContainerGroupDefinitionOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Creates a <code>ContainerGroupDefinition</code> that describes a set of containers for hosting your game server with Amazon GameLift Servers managed containers hosting. An Amazon GameLift Servers container group is similar to a container task or pod. Use container group definitions when you create a container fleet with <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerFleet.html">CreateContainerFleet</a>. </p> <p>A container group definition determines how Amazon GameLift Servers deploys your containers to each instance in a container fleet. You can maintain multiple versions of a container group definition.</p> <p>There are two types of container groups:</p> <ul> <li> <p>A <b>game server container group</b> has the containers that run your game server application and supporting software. A game server container group can have these container types:</p> <ul> <li> <p>Game server container. This container runs your game server. You can define one game server container in a game server container group.</p> </li> <li> <p>Support container. This container runs software in parallel with your game server. You can define up to 8 support containers in a game server group.</p> </li> </ul> <p>When building a game server container group definition, you can choose to bundle your game server executable and all dependent software into a single game server container. Alternatively, you can separate the software into one game server container and one or more support containers.</p> <p>On a container fleet instance, a game server container group can be deployed multiple times (depending on the compute resources of the instance). This means that all containers in the container group are replicated together.</p> </li> <li> <p>A <b>per-instance container group</b> has containers for processes that aren't replicated on a container fleet instance. This might include background services, logging, test processes, or processes that need to persist independently of the game server container group. When building a per-instance container group, you can define up to 10 support containers.</p> </li> </ul> <note> <p>This operation requires Identity and Access Management (IAM) permissions to access container images in Amazon ECR repositories. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html"> IAM permissions for Amazon GameLift Servers</a> for help setting the appropriate permissions.</p> </note> <p> <b>Request options</b> </p> <p>Use this operation to make the following types of requests. You can specify values for the minimum required parameters and customize optional values later.</p> <ul> <li> <p>Create a game server container group definition. Provide the following required parameter values:</p> <ul> <li> <p> <code>Name</code> </p> </li> <li> <p> <code>ContainerGroupType</code> (<code>GAME_SERVER</code>)</p> </li> <li> <p> <code>OperatingSystem</code> </p> </li> <li> <p> <code>TotalMemoryLimitMebibytes</code> </p> </li> <li> <p>Either <code>TotalVcpuLimit</code> or a <code>Vcpu</code> value for the game server container</p> </li> <li> <p>At least one <code>GameServerContainerDefinition</code> </p> <ul> <li> <p> <code>ContainerName</code> </p> </li> <li> <p> <code>ImageUrl</code> </p> </li> <li> <p> <code>PortConfiguration</code> </p> </li> <li> <p> <code>ServerSdkVersion</code> </p> </li> </ul> </li> </ul> </li> <li> <p>Create a per-instance container group definition. Provide the following required parameter values:</p> <ul> <li> <p> <code>Name</code> </p> </li> <li> <p> <code>ContainerGroupType</code> (<code>PER_INSTANCE</code>)</p> </li> <li> <p> <code>OperatingSystem</code> </p> </li> <li> <p> <code>TotalMemoryLimitMebibytes</code> </p> </li> <li> <p> <code>TotalVcpuLimit</code> </p> </li> <li> <p>At least one <code>SupportContainerDefinition</code> </p> <ul> <li> <p> <code>ContainerName</code> </p> </li> <li> <p> <code>ImageUrl</code> </p> </li> </ul> </li> </ul> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this request creates a <code>ContainerGroupDefinition</code> resource and assigns a unique ARN value. You can update most properties of a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html">UpdateContainerGroupDefinition</a>, and optionally save the update as a new version.</p>

        Args:
            name: <p>A descriptive identifier for the container group definition. The name value must be unique in an Amazon Web Services Region.</p>
            container_group_type: <p>The type of container group being defined. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.</p> <p>Default value: <code>GAME_SERVER</code> </p>
            total_memory_limit_mebibytes: <p>The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual container's memory limit.</p> <p>Default value: 1024</p>
            total_vcpu_limit: <p>The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. If you set vCPU reservations for individual containers, the total value must be equal to or greater than the sum of the <code>Vcpu</code> values for all containers in the group.</p> <p>This property is required for a per-instance container group.</p> <p>For a game server container group, Amazon GameLift Servers requires either a total vCPU limit or a <code>Vcpu</code> value for the game server container. If you set a total vCPU limit for a game server container group, Amazon GameLift Servers uses this value to calculate how many game server container groups fit on an instance. If you don't set a total vCPU limit, the group's containers can use up to the instance's available vCPU, and Amazon GameLift Servers uses the sum of the containers' <code>Vcpu</code> values to calculate how many game server container groups fit on an instance.</p>
            game_server_container_definition: <p>The definition for the game server container in this group. Define a game server container only when the container group type is <code>GAME_SERVER</code>. Game server containers specify a container image with your game server build. You can pass in your container definitions as a JSON file.</p>
            support_container_definitions: <p>One or more definition for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.</p>
            operating_system: <p>The platform that all containers in the group use. Containers in a group must run on the same operating system.</p> <p>Default value: <code>AMAZON_LINUX_2023</code> </p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>
            version_description: <p>A description for the initial version of this container group definition. </p>
            tags: <p>A list of labels to assign to the container group definition resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. </p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_container_group_definition_input.CreateContainerGroupDefinitionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_container_group_definition_output.CreateContainerGroupDefinitionOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_container_group_definition

            output, http_response = (
                capo_gamelift._operations.game_lift.create_container_group_definition.create_container_group_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_container_group_definition_input.CreateContainerGroupDefinitionInput = {}
        if name is not None:
            input_["name"] = name
        if container_group_type is not None:
            input_["container_group_type"] = container_group_type
        if total_memory_limit_mebibytes is not None:
            input_["total_memory_limit_mebibytes"] = total_memory_limit_mebibytes
        if total_vcpu_limit is not None:
            input_["total_vcpu_limit"] = total_vcpu_limit
        if game_server_container_definition is not None:
            input_["game_server_container_definition"] = (
                game_server_container_definition
            )
        if support_container_definitions is not None:
            input_["support_container_definitions"] = support_container_definitions
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if version_description is not None:
            input_["version_description"] = version_description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_fleet(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
        script_id: Optional[
            "capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"
        ] = None,
        server_launch_path: Optional[
            "capo_gamelift.types.launch_path_string_model.LaunchPathStringModel"
        ] = None,
        server_launch_parameters: Optional[
            "capo_gamelift.types.launch_parameters_string_model.LaunchParametersStringModel"
        ] = None,
        log_paths: Optional["capo_gamelift.types.string_list.StringList"] = None,
        ec2_instance_type: Optional[
            "capo_gamelift.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        ec2_inbound_permissions: Optional[
            "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
        ] = None,
        new_game_session_protection_policy: Optional[
            "capo_gamelift.types.protection_policy.ProtectionPolicy"
        ] = None,
        runtime_configuration: Optional[
            "capo_gamelift.types.runtime_configuration.RuntimeConfiguration"
        ] = None,
        resource_creation_limit_policy: Optional[
            "capo_gamelift.types.resource_creation_limit_policy.ResourceCreationLimitPolicy"
        ] = None,
        metric_groups: Optional[
            "capo_gamelift.types.metric_group_list.MetricGroupList"
        ] = None,
        peer_vpc_aws_account_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        peer_vpc_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        fleet_type: Optional["capo_gamelift.types.fleet_type.FleetType"] = None,
        instance_role_arn: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
        certificate_configuration: Optional[
            "capo_gamelift.types.certificate_configuration.CertificateConfiguration"
        ] = None,
        locations: Optional[
            "capo_gamelift.types.location_configuration_list.LocationConfigurationList"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
        compute_type: Optional["capo_gamelift.types.compute_type.ComputeType"] = None,
        anywhere_configuration: Optional[
            "capo_gamelift.types.anywhere_configuration.AnywhereConfiguration"
        ] = None,
        instance_role_credentials_provider: Optional[
            "capo_gamelift.types.instance_role_credentials_provider.InstanceRoleCredentialsProvider"
        ] = None,
        player_gateway_mode: Optional[
            "capo_gamelift.types.player_gateway_mode.PlayerGatewayMode"
        ] = None,
        player_gateway_configuration: Optional[
            "capo_gamelift.types.player_gateway_configuration.PlayerGatewayConfiguration"
        ] = None,
    ) -> "capo_gamelift.types.create_fleet_output.CreateFleetOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Creates a fleet of compute resources to host your game servers. Use this operation to set up a fleet for the following compute types: </p> <p> <b>Managed EC2 fleet</b> </p> <p>An EC2 fleet is a set of Amazon Elastic Compute Cloud (Amazon EC2) instances. Your game server build is deployed to each fleet instance. Amazon GameLift Servers manages the fleet's instances and controls the lifecycle of game server processes, which host game sessions for players. EC2 fleets can have instances in multiple locations. Each instance in the fleet is designated a <code>Compute</code>.</p> <p>To create an EC2 fleet, provide these required parameters:</p> <ul> <li> <p>Either <code>BuildId</code> or <code>ScriptId</code> </p> </li> <li> <p> <code>ComputeType</code> set to <code>EC2</code> (the default value)</p> </li> <li> <p> <code>EC2InboundPermissions</code> </p> </li> <li> <p> <code>EC2InstanceType</code> </p> </li> <li> <p> <code>FleetType</code> </p> </li> <li> <p> <code>Name</code> </p> </li> <li> <p> <code>RuntimeConfiguration</code> with at least one <code>ServerProcesses</code> configuration</p> </li> </ul> <p>If successful, this operation creates a new fleet resource and places it in <code>NEW</code> status while Amazon GameLift Servers initiates the <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-all.html#fleets-creation-workflow">fleet creation workflow</a>. To debug your fleet, fetch logs, view performance metrics or other actions on the fleet, create a development fleet with port 22/3389 open. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. </p> <p>When the fleet status is ACTIVE, you can adjust capacity settings and turn autoscaling on/off for each location.</p> <note> <p>A managed fleet's runtime environment depends on the Amazon Machine Image (AMI) version it uses. When a new fleet is created, Amazon GameLift Servers assigns the latest available AMI version to the fleet, and all compute instances in that fleet are deployed with that version. To update the AMI version, you must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html"> Security best practices for Amazon GameLift Servers</a>.</p> </note> <p> <b>Anywhere fleet</b> </p> <p>An Anywhere fleet represents compute resources that are not owned or managed by Amazon GameLift Servers. You might create an Anywhere fleet with your local machine for testing, or use one to host game servers with on-premises hardware or other game hosting solutions. </p> <p>To create an Anywhere fleet, provide these required parameters:</p> <ul> <li> <p> <code>ComputeType</code> set to <code>ANYWHERE</code> </p> </li> <li> <p> <code>Locations</code> specifying a custom location</p> </li> <li> <p> <code>Name</code> </p> </li> </ul> <p>If successful, this operation creates a new fleet resource and places it in <code>ACTIVE</code> status. You can register computes with a fleet in <code>ACTIVE</code> status. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html#fleets-creating-debug-creation">Debug fleet creation issues</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Multi-location fleets</a> </p>

        Args:
            name: <p>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</p>
            description: <p>A description for the fleet.</p>
            build_id: <p>The unique identifier for a custom game server build to be deployed to a fleet with compute type <code>EC2</code>. You can use either the build ID or ARN. The build must be uploaded to Amazon GameLift Servers and in <code>READY</code> status. This fleet property can't be changed after the fleet is created.</p>
            script_id: <p>The unique identifier for a Realtime configuration script to be deployed to a fleet with compute type <code>EC2</code>. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift Servers prior to creating the fleet. This fleet property can't be changed after the fleet is created.</p>
            server_launch_path: <p> <b>This parameter is no longer used.</b> Specify a server launch path using the <code>RuntimeConfiguration</code> parameter. Requests that use this parameter instead continue to be valid.</p>
            server_launch_parameters: <p> <b>This parameter is no longer used.</b> Specify server launch parameters using the <code>RuntimeConfiguration</code> parameter. Requests that use this parameter instead continue to be valid.</p>
            log_paths: <p> <b>This parameter is no longer used.</b> To specify where Amazon GameLift Servers should store log files once a server process shuts down, use the Amazon GameLift Servers server API <code>ProcessReady()</code> and specify one or more directory paths in <code>logParameters</code>. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-initialize">Initialize the server process</a> in the <i>Amazon GameLift Servers Developer Guide</i>. </p>
            ec2_instance_type: <p>The Amazon GameLift Servers-supported Amazon EC2 instance type to use with managed EC2 fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See <a href="http://aws.amazon.com/ec2/instance-types/">Amazon Elastic Compute Cloud Instance Types</a> for detailed descriptions of Amazon EC2 instance types.</p>
            ec2_inbound_permissions: <p>The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for managed EC2 fleets. You can leave this parameter empty when creating the fleet, but you must call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings">https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetPortSettings</a> to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Amazon GameLift Servers Realtime fleets, Amazon GameLift Servers automatically sets TCP and UDP ranges.</p>
            new_game_session_protection_policy: <p>The status of termination protection for active game sessions on the fleet. By default, this property is set to <code>NoProtection</code>. You can also set game session protection for an individual game session by calling <a href="gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a>.</p> <ul> <li> <p> <b>NoProtection</b> - Game sessions can be terminated during active gameplay as a result of a scale-down event. </p> </li> <li> <p> <b>FullProtection</b> - Game sessions in <code>ACTIVE</code> status cannot be terminated during a scale-down event.</p> </li> </ul>
            runtime_configuration: <p>Instructions for how to launch and run server processes on the fleet. Set runtime configuration for managed EC2 fleets. For an Anywhere fleet, set this parameter only if the fleet is running the Amazon GameLift Servers Agent. The runtime configuration defines one or more server process configurations. Each server process identifies a game executable or Realtime script file and the number of processes to run concurrently. </p> <note> <p>This parameter replaces the parameters <code>ServerLaunchPath</code> and <code>ServerLaunchParameters</code>, which are still supported for backward compatibility.</p> </note>
            resource_creation_limit_policy: <p>A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.</p>
            metric_groups: <p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time. </p>
            peer_vpc_aws_account_id: <p>Used when peering your Amazon GameLift Servers fleet with a VPC, the unique identifier for the Amazon Web Services account that owns the VPC. You can find your account ID in the Amazon Web Services Management Console under account settings. </p>
            peer_vpc_id: <p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>
            fleet_type: <p>Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to <code>ON_DEMAND</code>. Learn more about when to use <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot"> On-Demand versus Spot Instances</a>. This fleet property can't be changed after the fleet is created.</p>
            instance_role_arn: <p>A unique identifier for an IAM role that manages access to your Amazon Web Services services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the <a href="https://console.aws.amazon.com/iam/">IAM dashboard</a> in the Amazon Web Services Management Console. Learn more about using on-box credentials for your game servers at <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html"> Access external resources from a game server</a>. This fleet property can't be changed after the fleet is created.</p>
            certificate_configuration: <p>Prompts Amazon GameLift Servers to generate a TLS/SSL certificate for the fleet. Amazon GameLift Servers uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift Servers. By default, the <code>CertificateConfiguration</code> is <code>DISABLED</code>. You can't change this property after you create the fleet. </p> <p>Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.</p> <note> <p>ACM isn't available in all Amazon Web Services regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see <a href="https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html">Supported Regions</a> in the <i>Certificate Manager User Guide</i>.</p> </note>
            locations: <p>A set of remote locations to deploy additional instances to and manage as a multi-location fleet. Use this parameter when creating a fleet in Amazon Web Services Regions that support multiple locations. You can add any Amazon Web Services Region or Local Zone that's supported by Amazon GameLift Servers. Provide a list of one or more Amazon Web Services Region codes, such as <code>us-west-2</code>, or Local Zone names. When using this parameter, Amazon GameLift Servers requires you to include your home location in the request. For a list of supported Regions and Local Zones, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting.</p>
            tags: <p>A list of labels to assign to the new fleet resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>
            compute_type: <p>The type of compute resource used to host your game servers. </p> <ul> <li> <p> <code>EC2</code> – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.</p> </li> <li> <p> <code>ANYWHERE</code> – Game servers and supporting software are deployed to compute resources that you provide and manage. With this compute type, you can also set the <code>AnywhereConfiguration</code> parameter.</p> </li> </ul>
            anywhere_configuration: <p>Amazon GameLift Servers Anywhere configuration options.</p>
            instance_role_credentials_provider: <p>Prompts Amazon GameLift Servers to generate a shared credentials file for the IAM role that's defined in <code>InstanceRoleArn</code>. The shared credentials file is stored on each fleet instance and refreshed as needed. Use shared credentials for applications that are deployed along with the game server executable, if the game server is integrated with server SDK version 5.x. For more information about using shared credentials, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html"> Communicate with other Amazon Web Services resources from your fleets</a>.</p>
            player_gateway_mode: <p>Configures player gateway for your fleet. Player gateway provides benefits such as DDoS protection by rate limiting and validating traffic before it reaches game servers, hiding game server IP addresses from players, and providing updated endpoints when relay endpoints become unhealthy. Note, player gateway is only available for fleets using server SDK 5.x or later game server builds.</p> <p> <b>How it works:</b> When enabled, game clients connect to relay endpoints instead of to your game servers. Player gateway validates player gateway tokens and routes traffic to the appropriate game server. Your game backend calls <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to retrieve relay endpoints and player gateway tokens for your game clients. To learn more about this topic, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html">DDoS protection with Amazon GameLift Servers player gateway</a>.</p> <p>Possible values include:</p> <ul> <li> <p> <code>DISABLED</code> (default) -- Game clients connect to the game server endpoint. Use this when you do not intend to integrate your game with player gateway.</p> </li> <li> <p> <code>ENABLED</code> -- Player gateway is available in fleet locations where it is supported. Your game backend can call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to obtain a player gateway token and endpoints for game clients.</p> </li> <li> <p> <code>REQUIRED</code> -- Player gateway is available in fleet locations where it is supported, and the fleet can only use locations that support this feature. Attempting to add a remote location to your fleet which does not support player gateway will result in an <code>InvalidRequestException</code>.</p> </li> </ul>
            player_gateway_configuration: <p>Configuration settings for player gateway. Use this to specify advanced options for how player gateway handles connections.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.not_ready_exception.NotReadyException: <p> The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with <a href="http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">exponential backoffs and jitter</a>. </p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_fleet_input.CreateFleetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_fleet_output.CreateFleetOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_fleet

            output, http_response = (
                capo_gamelift._operations.game_lift.create_fleet.create_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_fleet_input.CreateFleetInput = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if build_id is not None:
            input_["build_id"] = build_id
        if script_id is not None:
            input_["script_id"] = script_id
        if server_launch_path is not None:
            input_["server_launch_path"] = server_launch_path
        if server_launch_parameters is not None:
            input_["server_launch_parameters"] = server_launch_parameters
        if log_paths is not None:
            input_["log_paths"] = log_paths
        if ec2_instance_type is not None:
            input_["ec2_instance_type"] = ec2_instance_type
        if ec2_inbound_permissions is not None:
            input_["ec2_inbound_permissions"] = ec2_inbound_permissions
        if new_game_session_protection_policy is not None:
            input_["new_game_session_protection_policy"] = (
                new_game_session_protection_policy
            )
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration
        if resource_creation_limit_policy is not None:
            input_["resource_creation_limit_policy"] = resource_creation_limit_policy
        if metric_groups is not None:
            input_["metric_groups"] = metric_groups
        if peer_vpc_aws_account_id is not None:
            input_["peer_vpc_aws_account_id"] = peer_vpc_aws_account_id
        if peer_vpc_id is not None:
            input_["peer_vpc_id"] = peer_vpc_id
        if fleet_type is not None:
            input_["fleet_type"] = fleet_type
        if instance_role_arn is not None:
            input_["instance_role_arn"] = instance_role_arn
        if certificate_configuration is not None:
            input_["certificate_configuration"] = certificate_configuration
        if locations is not None:
            input_["locations"] = locations
        if tags is not None:
            input_["tags"] = tags
        if compute_type is not None:
            input_["compute_type"] = compute_type
        if anywhere_configuration is not None:
            input_["anywhere_configuration"] = anywhere_configuration
        if instance_role_credentials_provider is not None:
            input_["instance_role_credentials_provider"] = (
                instance_role_credentials_provider
            )
        if player_gateway_mode is not None:
            input_["player_gateway_mode"] = player_gateway_mode
        if player_gateway_configuration is not None:
            input_["player_gateway_configuration"] = player_gateway_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_fleet_locations(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        locations: Optional[
            "capo_gamelift.types.location_configuration_list.LocationConfigurationList"
        ] = None,
    ) -> "capo_gamelift.types.create_fleet_locations_output.CreateFleetLocationsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Adds remote locations to an EC2 fleet and begins populating the new locations with instances. The new instances conform to the fleet's instance type, auto-scaling, and other configuration settings.</p> <note> <p>You can't add remote locations to a fleet that resides in an Amazon Web Services Region that doesn't support multiple locations. Fleets created prior to March 2021 can't support multiple locations.</p> </note> <p>To add fleet locations, specify the fleet to be updated and provide a list of one or more locations. </p> <p>If successful, this operation returns the list of added locations with their status set to <code>NEW</code>. Amazon GameLift Servers initiates the process of starting an instance in each added location. You can track the status of each new location by monitoring location creation events using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html">DescribeFleetEvents</a>.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-editing.html#fleets-update-locations">Update fleet locations</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting.</p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to add locations to. You can use either the fleet ID or ARN value.</p>
            locations: <p>A list of locations to deploy additional instances to and manage as part of the fleet. You can add any Amazon GameLift Servers-supported Amazon Web Services Region as a remote location, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>. </p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.not_ready_exception.NotReadyException: <p> The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with <a href="http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">exponential backoffs and jitter</a>. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_fleet_locations_input.CreateFleetLocationsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_fleet_locations_output.CreateFleetLocationsOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_fleet_locations

            output, http_response = (
                capo_gamelift._operations.game_lift.create_fleet_locations.create_fleet_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_fleet_locations_input.CreateFleetLocationsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if locations is not None:
            input_["locations"] = locations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_game_server_group(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name.GameServerGroupName"
        ] = None,
        role_arn: Optional["capo_gamelift.types.iam_role_arn.IamRoleArn"] = None,
        min_size: Optional["capo_gamelift.types.whole_number.WholeNumber"] = None,
        max_size: Optional[
            "capo_gamelift.types.positive_integer.PositiveInteger"
        ] = None,
        launch_template: Optional[
            "capo_gamelift.types.launch_template_specification.LaunchTemplateSpecification"
        ] = None,
        instance_definitions: Optional[
            "capo_gamelift.types.instance_definitions.InstanceDefinitions"
        ] = None,
        auto_scaling_policy: Optional[
            "capo_gamelift.types.game_server_group_auto_scaling_policy.GameServerGroupAutoScalingPolicy"
        ] = None,
        balancing_strategy: Optional[
            "capo_gamelift.types.balancing_strategy.BalancingStrategy"
        ] = None,
        game_server_protection_policy: Optional[
            "capo_gamelift.types.game_server_protection_policy.GameServerProtectionPolicy"
        ] = None,
        vpc_subnets: Optional["capo_gamelift.types.vpc_subnets.VpcSubnets"] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_game_server_group_output.CreateGameServerGroupOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Creates a Amazon GameLift Servers FleetIQ game server group for managing game hosting on a collection of Amazon Elastic Compute Cloud instances for game hosting. This operation creates the game server group, creates an Auto Scaling group in your Amazon Web Services account, and establishes a link between the two groups. You can view the status of your game server groups in the Amazon GameLift Servers console. Game server group metrics and events are emitted to Amazon CloudWatch.</p> <p>Before creating a new game server group, you must have the following: </p> <ul> <li> <p>An Amazon Elastic Compute Cloud launch template that specifies how to launch Amazon Elastic Compute Cloud instances with your game server build. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html"> Launching an Instance from a Launch Template</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. </p> </li> <li> <p>An IAM role that extends limited access to your Amazon Web Services account to allow Amazon GameLift Servers FleetIQ to create and interact with the Auto Scaling group. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-iam-permissions-roles.html">Create IAM roles for cross-service interaction</a> in the <i>Amazon GameLift Servers FleetIQ Developer Guide</i>.</p> </li> </ul> <p>To create a new game server group, specify a unique group name, IAM role and Amazon Elastic Compute Cloud launch template, and provide a list of instance types that can be used in the group. You must also set initial maximum and minimum limits on the group's instance count. You can optionally set an Auto Scaling policy with target tracking based on a Amazon GameLift Servers FleetIQ metric.</p> <p>Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling group's configuration as needed. Several properties that are set when creating a game server group, including maximum/minimum size and auto-scaling policy settings, must be updated directly in the Auto Scaling group. Keep in mind that some Auto Scaling group properties are periodically updated by Amazon GameLift Servers FleetIQ as part of its balancing activities to optimize for availability and cost.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>An identifier for the new game server group. This value is used to generate unique ARN identifiers for the Amazon EC2 Auto Scaling group and the Amazon GameLift Servers FleetIQ game server group. The name must be unique per Region per Amazon Web Services account.</p>
            role_arn: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.</p>
            min_size: <p>The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p>
            max_size: <p>The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift Servers FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p>
            launch_template: <p>The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html">Creating a Launch Template for an Auto Scaling Group</a> in the <i>Amazon Elastic Compute Cloud Auto Scaling User Guide</i>. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p> <note> <p>If you specify network interfaces in your launch template, you must explicitly set the property <code>AssociatePublicIpAddress</code> to "true". If no network interface is specified in the launch template, Amazon GameLift Servers FleetIQ uses your account's default VPC.</p> </note>
            instance_definitions: <p>The Amazon EC2 instance types and sizes to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift Servers FleetIQ. For more information on instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">EC2 Instance Types</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value "1". For more information about capacity weighting, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html"> Instance Weighting for Amazon EC2 Auto Scaling</a> in the Amazon EC2 Auto Scaling User Guide.</p>
            auto_scaling_policy: <p>Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric <code>"PercentUtilizedGameServers"</code> to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the Amazon Web Services console or APIs.</p>
            balancing_strategy: <p>Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:</p> <ul> <li> <p> <code>SPOT_ONLY</code> - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.</p> </li> <li> <p> <code>SPOT_PREFERRED</code> - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.</p> </li> <li> <p> <code>ON_DEMAND_ONLY</code> - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.</p> </li> </ul>
            game_server_protection_policy: <p>A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion. An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status. This property is set to <code>NO_PROTECTION</code> by default.</p>
            vpc_subnets: <p>A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift Servers FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.</p>
            tags: <p>A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management, and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_game_server_group_input.CreateGameServerGroupInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_game_server_group_output.CreateGameServerGroupOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_game_server_group

            output, http_response = (
                capo_gamelift._operations.game_lift.create_game_server_group.create_game_server_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_game_server_group_input.CreateGameServerGroupInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if min_size is not None:
            input_["min_size"] = min_size
        if max_size is not None:
            input_["max_size"] = max_size
        if launch_template is not None:
            input_["launch_template"] = launch_template
        if instance_definitions is not None:
            input_["instance_definitions"] = instance_definitions
        if auto_scaling_policy is not None:
            input_["auto_scaling_policy"] = auto_scaling_policy
        if balancing_strategy is not None:
            input_["balancing_strategy"] = balancing_strategy
        if game_server_protection_policy is not None:
            input_["game_server_protection_policy"] = game_server_protection_policy
        if vpc_subnets is not None:
            input_["vpc_subnets"] = vpc_subnets
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_game_session(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        maximum_player_session_count: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        game_properties: Optional[
            "capo_gamelift.types.game_property_list.GamePropertyList"
        ] = None,
        creator_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        game_session_id: Optional[
            "capo_gamelift.types.id_string_model.IdStringModel"
        ] = None,
        idempotency_token: Optional[
            "capo_gamelift.types.id_string_model.IdStringModel"
        ] = None,
        game_session_data: Optional[
            "capo_gamelift.types.large_game_session_data.LargeGameSessionData"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.create_game_session_output.CreateGameSessionOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Creates a multiplayer game session for players in a specific fleet location. This operation prompts an available server process to start a game session and retrieves connection information for the new game session. As an alternative, consider using the Amazon GameLift Servers game session placement feature with <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html">StartGameSessionPlacement</a>, which uses the FleetIQ algorithm and queues to optimize the placement process.</p> <p>When creating a game session, you specify exactly where you want to place it and provide a set of game session configuration settings. The target fleet must be in <code>ACTIVE</code> status. </p> <p>You can use this operation in the following ways: </p> <ul> <li> <p>To create a game session on an instance in a fleet's home Region, provide a fleet or alias ID along with your game session configuration. </p> </li> <li> <p>To create a game session on an instance in a fleet's remote location, provide a fleet or alias ID and a location name, along with your game session configuration. </p> </li> <li> <p>To create a game session on an instance in an Anywhere fleet, specify the fleet's custom location.</p> </li> </ul> <p>If successful, Amazon GameLift Servers initiates a workflow to start a new game session and returns a <code>GameSession</code> object containing the game session configuration and status. When the game session status is <code>ACTIVE</code>, it is updated with connection information and you can create player sessions for the game session. By default, newly created game sessions are open to new players. You can restrict new player access by using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a> to change the game session's player session creation policy.</p> <p>Amazon GameLift Servers retains logs for active game sessions for 14 days. To access the logs, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetGameSessionLogUrl.html">GetGameSessionLogUrl</a> to download the log files.</p> <p> <i>Available in Amazon GameLift Servers Local.</i> </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to create a game session in. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.</p>
            alias_id: <p>A unique identifier for the alias associated with the fleet to create a game session in. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.</p>
            maximum_player_session_count: <p>The maximum number of players that can be connected simultaneously to the game session.</p>
            name: <p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>
            game_properties: <p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. For an example, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-create">Create a game session with custom properties</a>. </p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>
            creator_id: <p>A unique identifier for a player or entity creating the game session. </p> <p>If you add a resource creation limit policy to a fleet, the <code>CreateGameSession</code> operation requires a <code>CreatorId</code>. Amazon GameLift Servers limits the number of game session creation requests with the same <code>CreatorId</code> in a specified time period.</p> <p>If your fleet doesn't have a resource creation limit policy and you provide a <code>CreatorId</code> in your <code>CreateGameSession</code> requests, Amazon GameLift Servers limits requests to one request per <code>CreatorId</code> per second.</p> <p>To not limit <code>CreateGameSession</code> requests with the same <code>CreatorId</code>, don't provide a <code>CreatorId</code> in your <code>CreateGameSession</code> request.</p>
            game_session_id: <p> <i>This parameter is deprecated. Use <code>IdempotencyToken</code> instead.</i> </p> <p>Custom string that uniquely identifies a request for a new game session. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID.</p>
            idempotency_token: <p>Custom string that uniquely identifies the new game session request. This is useful for ensuring that game session requests with the same idempotency token are processed only once. Subsequent requests with the same string return the original <code>GameSession</code> object, with an updated status. Maximum token length is 48 characters. If provided, this string is included in the new game session's ID. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>. Idempotency tokens remain in use for 30 days after a game session has ended; game session objects are retained for this time period and then deleted.</p>
            game_session_data: <p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>.</p>
            location: <p>A fleet's remote location to place the new game session in. If this parameter is not set, the new game session is placed in the fleet's home Region. Specify a remote location with an Amazon Web Services Region code such as <code>us-west-2</code>. When using an Anywhere fleet, this parameter is required and must be set to the Anywhere fleet's custom location.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.fleet_capacity_exceeded_exception.FleetCapacityExceededException: <p>The specified fleet has no available instances to fulfill a <code>CreateGameSession</code> request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException: <p>A game session with this custom ID string already exists in this fleet. Resolve this conflict before retrying this request.</p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_game_session_input.CreateGameSessionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_game_session_output.CreateGameSessionOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_game_session

            output, http_response = (
                capo_gamelift._operations.game_lift.create_game_session.create_game_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_game_session_input.CreateGameSessionInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if alias_id is not None:
            input_["alias_id"] = alias_id
        if maximum_player_session_count is not None:
            input_["maximum_player_session_count"] = maximum_player_session_count
        if name is not None:
            input_["name"] = name
        if game_properties is not None:
            input_["game_properties"] = game_properties
        if creator_id is not None:
            input_["creator_id"] = creator_id
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if idempotency_token is not None:
            input_["idempotency_token"] = idempotency_token
        if game_session_data is not None:
            input_["game_session_data"] = game_session_data
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_game_session_queue(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.game_session_queue_name.GameSessionQueueName"
        ] = None,
        timeout_in_seconds: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        player_latency_policies: Optional[
            "capo_gamelift.types.player_latency_policy_list.PlayerLatencyPolicyList"
        ] = None,
        destinations: Optional[
            "capo_gamelift.types.game_session_queue_destination_list.GameSessionQueueDestinationList"
        ] = None,
        filter_configuration: Optional[
            "capo_gamelift.types.filter_configuration.FilterConfiguration"
        ] = None,
        priority_configuration: Optional[
            "capo_gamelift.types.priority_configuration.PriorityConfiguration"
        ] = None,
        custom_event_data: Optional[
            "capo_gamelift.types.queue_custom_event_data.QueueCustomEventData"
        ] = None,
        notification_target: Optional[
            "capo_gamelift.types.queue_sns_arn_string_model.QueueSnsArnStringModel"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_game_session_queue_output.CreateGameSessionQueueOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Creates a placement queue that processes requests for new game sessions. A queue uses FleetIQ algorithms to locate the best available placement locations for a new game session, and then prompts the game server process to start a new game session.</p> <p>A game session queue is configured with a set of destinations (Amazon GameLift Servers fleets or aliases) that determine where the queue can place new game sessions. These destinations can span multiple Amazon Web Services Regions, can use different instance types, and can include both Spot and On-Demand fleets. If the queue includes multi-location fleets, the queue can place game sessions in any of a fleet's remote locations.</p> <p>You can configure a queue to determine how it selects the best available placement for a new game session. Queues can prioritize placement decisions based on a combination of location, hosting cost, and player latency. You can set up the queue to use the default prioritization or provide alternate instructions using <code>PriorityConfiguration</code>.</p> <p> <b>Request options</b> </p> <p>Use this operation to make these common types of requests. </p> <ul> <li> <p>Create a queue with the minimum required parameters.</p> <ul> <li> <p> <code>Name</code> </p> </li> <li> <p> <code>Destinations</code> (This parameter isn't required, but a queue can't make placements without at least one destination.)</p> </li> </ul> </li> <li> <p>Create a queue with placement notification. Queues that have high placement activity must use a notification system, such as with Amazon Simple Notification Service (Amazon SNS) or Amazon CloudWatch.</p> <ul> <li> <p>Required parameters <code>Name</code> and <code>Destinations</code> </p> </li> <li> <p> <code>NotificationTarget</code> </p> </li> </ul> </li> <li> <p>Create a queue with custom prioritization settings. These custom settings replace the default prioritization configuration for a queue.</p> <ul> <li> <p>Required parameters <code>Name</code> and <code>Destinations</code> </p> </li> <li> <p> <code>PriorityConfiguration</code> </p> </li> </ul> </li> <li> <p>Create a queue with special rules for processing player latency data.</p> <ul> <li> <p>Required parameters <code>Name</code> and <code>Destinations</code> </p> </li> <li> <p> <code>PlayerLatencyPolicies</code> </p> </li> </ul> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation returns a new <code>GameSessionQueue</code> object with an assigned queue ARN. Use the queue's name or ARN when submitting new game session requests with <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html">StartGameSessionPlacement</a> or <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartMatchmaking.html">StartMatchmaking</a>. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-design.html"> Design a game session queue</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-creating.html"> Create a game session queue</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateGameSessionQueue.html">CreateGameSessionQueue</a> | <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionQueues.html">DescribeGameSessionQueues</a> | <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSessionQueue.html">UpdateGameSessionQueue</a> | <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteGameSessionQueue.html">DeleteGameSessionQueue</a> | <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            name: <p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region.</p>
            timeout_in_seconds: <p>The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a <code>TIMED_OUT</code> status. If you don't specify a request timeout, the queue uses a default value.</p> <note> <p>The minimum value is 10 and the maximum value is 600.</p> </note>
            player_latency_policies: <p>A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value.</p>
            destinations: <p>A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.</p>
            filter_configuration: <p>A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as <code>us-west-2</code>. If this parameter is not set, game sessions can be placed in any queue location. </p>
            priority_configuration: <p>Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process. </p>
            custom_event_data: <p>Information to be added to all events that are related to this game session queue.</p>
            notification_target: <p>An SNS topic ARN that is set up to receive game session placement notifications. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html"> Setting up notifications for game session placement</a>.</p>
            tags: <p>A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_game_session_queue_input.CreateGameSessionQueueInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_game_session_queue_output.CreateGameSessionQueueOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_game_session_queue

            output, http_response = (
                capo_gamelift._operations.game_lift.create_game_session_queue.create_game_session_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_game_session_queue_input.CreateGameSessionQueueInput = {}
        if name is not None:
            input_["name"] = name
        if timeout_in_seconds is not None:
            input_["timeout_in_seconds"] = timeout_in_seconds
        if player_latency_policies is not None:
            input_["player_latency_policies"] = player_latency_policies
        if destinations is not None:
            input_["destinations"] = destinations
        if filter_configuration is not None:
            input_["filter_configuration"] = filter_configuration
        if priority_configuration is not None:
            input_["priority_configuration"] = priority_configuration
        if custom_event_data is not None:
            input_["custom_event_data"] = custom_event_data
        if notification_target is not None:
            input_["notification_target"] = notification_target
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_location(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        location_name: Optional[
            "capo_gamelift.types.custom_input_location_string_model.CustomInputLocationStringModel"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_location_output.CreateLocationOutput":
        """<p> <b>This API works with the following fleet types:</b> Anywhere</p> <p>Creates a custom location for use in an Anywhere fleet.</p>

        Args:
            location_name: <p>A descriptive name for the custom location.</p>
            tags: <p>A list of labels to assign to the new resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management, and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_location_input.CreateLocationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_location_output.CreateLocationOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_location

            output, http_response = (
                capo_gamelift._operations.game_lift.create_location.create_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_location_input.CreateLocationInput = {}
        if location_name is not None:
            input_["location_name"] = location_name
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_matchmaking_configuration(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        game_session_queue_arns: Optional[
            "capo_gamelift.types.queue_arns_list.QueueArnsList"
        ] = None,
        request_timeout_seconds: Optional[
            "capo_gamelift.types.matchmaking_request_timeout_integer.MatchmakingRequestTimeoutInteger"
        ] = None,
        acceptance_timeout_seconds: Optional[
            "capo_gamelift.types.matchmaking_acceptance_timeout_integer.MatchmakingAcceptanceTimeoutInteger"
        ] = None,
        acceptance_required: Optional[
            "capo_gamelift.types.boolean_model.BooleanModel"
        ] = None,
        rule_set_name: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
        ] = None,
        notification_target: Optional[
            "capo_gamelift.types.sns_arn_string_model.SnsArnStringModel"
        ] = None,
        additional_player_count: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        custom_event_data: Optional[
            "capo_gamelift.types.custom_event_data.CustomEventData"
        ] = None,
        game_properties: Optional[
            "capo_gamelift.types.game_property_list.GamePropertyList"
        ] = None,
        game_session_data: Optional[
            "capo_gamelift.types.game_session_data.GameSessionData"
        ] = None,
        backfill_mode: Optional[
            "capo_gamelift.types.backfill_mode.BackfillMode"
        ] = None,
        flex_match_mode: Optional[
            "capo_gamelift.types.flex_match_mode.FlexMatchMode"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_matchmaking_configuration_output.CreateMatchmakingConfigurationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Defines a new matchmaking configuration for use with FlexMatch. Whether you are using FlexMatch with Amazon GameLift Servers hosting or as a standalone matchmaking service, the matchmaking configuration sets out rules for matching players and forming teams. If you're also using Amazon GameLift Servers hosting, it defines how to start game sessions for each match. Your matchmaking system can use multiple configurations to handle different game scenarios. All matchmaking requests identify the matchmaking configuration to use and provide player attributes consistent with that configuration. </p> <p>To create a matchmaking configuration, you must provide the following: configuration name and FlexMatch mode (with or without Amazon GameLift Servers hosting); a rule set that specifies how to evaluate players and find acceptable matches; whether player acceptance is required; and the maximum time allowed for a matchmaking attempt. When using FlexMatch with Amazon GameLift Servers hosting, you also need to identify the game session queue to use when starting a game session for the match.</p> <p>In addition, you must set up an Amazon Simple Notification Service topic to receive matchmaking notifications. Provide the topic ARN in the matchmaking configuration.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html"> Design a FlexMatch matchmaker</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html"> Set up FlexMatch event notification</a> </p>

        Args:
            name: <p>A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.</p>
            description: <p>A human-readable description of the matchmaking configuration. </p>
            game_session_queue_arns: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::gamesessionqueue/<queue name></code>. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. A matchmaking configuration supports only one queue; if you specify more than one ARN, the request fails with an <code>InvalidRequestException</code>. If <code>FlexMatchMode</code> is set to <code>STANDALONE</code>, do not set this parameter. </p>
            request_timeout_seconds: <p>The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.</p>
            acceptance_timeout_seconds: <p>The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required. </p>
            acceptance_required: <p>A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to <code>TRUE</code>. With this option enabled, matchmaking tickets use the status <code>REQUIRES_ACCEPTANCE</code> to indicate when a completed potential match is waiting for player acceptance. </p>
            rule_set_name: <p>A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.</p>
            notification_target: <p>An SNS topic ARN that is set up to receive matchmaking notifications. See <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html"> Setting up notifications for matchmaking</a> for more information.</p>
            additional_player_count: <p>The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>
            custom_event_data: <p>Information to be added to all events related to this matchmaking configuration. </p>
            game_properties: <p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. This information is added to the new <code>GameSession</code> object that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>
            game_session_data: <p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>. This information is added to the new <code>GameSession</code> object that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>
            backfill_mode: <p>The method used to backfill game sessions that are created with this matchmaking configuration. Specify <code>MANUAL</code> when your game manages backfill requests manually or does not use the match backfill feature. Specify <code>AUTOMATIC</code> to have Amazon GameLift Servers create a backfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html"> Backfill Existing Games with FlexMatch</a>. Automatic backfill is not available when <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>
            flex_match_mode: <p>Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution. </p> <ul> <li> <p> <b>STANDALONE</b> - FlexMatch forms matches and returns match information, including players and team assignments, in a <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded"> MatchmakingSucceeded</a> event.</p> </li> <li> <p> <b>WITH_QUEUE</b> - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match. </p> </li> </ul>
            tags: <p>A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_matchmaking_configuration_input.CreateMatchmakingConfigurationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_matchmaking_configuration_output.CreateMatchmakingConfigurationOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_matchmaking_configuration

            output, http_response = (
                capo_gamelift._operations.game_lift.create_matchmaking_configuration.create_matchmaking_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_matchmaking_configuration_input.CreateMatchmakingConfigurationInput = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if game_session_queue_arns is not None:
            input_["game_session_queue_arns"] = game_session_queue_arns
        if request_timeout_seconds is not None:
            input_["request_timeout_seconds"] = request_timeout_seconds
        if acceptance_timeout_seconds is not None:
            input_["acceptance_timeout_seconds"] = acceptance_timeout_seconds
        if acceptance_required is not None:
            input_["acceptance_required"] = acceptance_required
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name
        if notification_target is not None:
            input_["notification_target"] = notification_target
        if additional_player_count is not None:
            input_["additional_player_count"] = additional_player_count
        if custom_event_data is not None:
            input_["custom_event_data"] = custom_event_data
        if game_properties is not None:
            input_["game_properties"] = game_properties
        if game_session_data is not None:
            input_["game_session_data"] = game_session_data
        if backfill_mode is not None:
            input_["backfill_mode"] = backfill_mode
        if flex_match_mode is not None:
            input_["flex_match_mode"] = flex_match_mode
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_matchmaking_rule_set(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
        ] = None,
        rule_set_body: Optional["capo_gamelift.types.rule_set_body.RuleSetBody"] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.create_matchmaking_rule_set_output.CreateMatchmakingRuleSetOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Creates a new rule set for FlexMatch matchmaking. A rule set describes the type of match to create, such as the number and size of teams. It also sets the parameters for acceptable player matches, such as minimum skill level or character type.</p> <p>To create a matchmaking rule set, provide unique rule set name and the rule set body in JSON format. Rule sets must be defined in the same Region as the matchmaking configuration they are used with.</p> <p>Since matchmaking rule sets cannot be edited, it is a good idea to check the rule set syntax using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ValidateMatchmakingRuleSet.html">ValidateMatchmakingRuleSet</a> before creating a new rule set.</p> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html">Build a rule set</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html">Design a matchmaker</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-intro.html">Matchmaking with FlexMatch</a> </p> </li> </ul>

        Args:
            name: <p>A unique identifier for the matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional <code>name</code> field in the rule set body.</p>
            rule_set_body: <p>A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.</p>
            tags: <p>A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_matchmaking_rule_set_input.CreateMatchmakingRuleSetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_matchmaking_rule_set_output.CreateMatchmakingRuleSetOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_matchmaking_rule_set

            output, http_response = (
                capo_gamelift._operations.game_lift.create_matchmaking_rule_set.create_matchmaking_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_matchmaking_rule_set_input.CreateMatchmakingRuleSetInput = {}
        if name is not None:
            input_["name"] = name
        if rule_set_body is not None:
            input_["rule_set_body"] = rule_set_body
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_player_session(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        player_id: Optional["capo_gamelift.types.player_id.PlayerId"] = None,
        player_data: Optional["capo_gamelift.types.player_data.PlayerData"] = None,
    ) -> "capo_gamelift.types.create_player_session_output.CreatePlayerSessionOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Reserves an open player slot in a game session for a player. New player sessions can be created in any game session with an open slot that is in <code>ACTIVE</code> status and has a player creation policy of <code>ACCEPT_ALL</code>. You can add a group of players to a game session with <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreatePlayerSessions.html">CreatePlayerSessions</a> . </p> <p>To create a player session, specify a game session ID, player ID, and optionally a set of player data. </p> <p>If successful, a slot is reserved in the game session for the player and a new <code>PlayerSessions</code> object is returned with a player session ID. The player references the player session ID when sending a connection request to the game session, and the game server can use it to validate the player reservation with the Amazon GameLift Servers service. Player sessions cannot be updated. </p> <p>The maximum number of players per game session is 200. It is not adjustable. </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions to add a player to. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            player_id: <p>A unique identifier for a player. Player IDs are developer-defined.</p>
            player_data: <p>Developer-defined information related to a player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game.</p>

        Raises:
            capo_gamelift.errors.game_session_full_exception.GameSessionFullException: <p>The game instance is currently full and cannot allow the requested player(s) to join. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_game_session_status_exception.InvalidGameSessionStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_player_session_input.CreatePlayerSessionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_player_session_output.CreatePlayerSessionOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_player_session

            output, http_response = (
                capo_gamelift._operations.game_lift.create_player_session.create_player_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_player_session_input.CreatePlayerSessionInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if player_id is not None:
            input_["player_id"] = player_id
        if player_data is not None:
            input_["player_data"] = player_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_player_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        player_ids: Optional["capo_gamelift.types.player_id_list.PlayerIdList"] = None,
        player_data_map: Optional[
            "capo_gamelift.types.player_data_map.PlayerDataMap"
        ] = None,
    ) -> "capo_gamelift.types.create_player_sessions_output.CreatePlayerSessionsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Reserves open slots in a game session for a group of players. New player sessions can be created in any game session with an open slot that is in <code>ACTIVE</code> status and has a player creation policy of <code>ACCEPT_ALL</code>. To add a single player to a game session, use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreatePlayerSession.html">CreatePlayerSession</a> </p> <p>To create player sessions, specify a game session ID and a list of player IDs. Optionally, provide a set of player data for each player ID. </p> <p>If successful, a slot is reserved in the game session for each player, and new <code>PlayerSession</code> objects are returned with player session IDs. Each player references their player session ID when sending a connection request to the game session, and the game server can use it to validate the player reservation with the Amazon GameLift Servers service. Player sessions cannot be updated.</p> <p>The maximum number of players per game session is 200. It is not adjustable. </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions to add players to. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            player_ids: <p>List of unique identifiers for the players to be added.</p>
            player_data_map: <p>Map of string pairs, each specifying a player ID and a set of developer-defined information related to the player. Amazon GameLift Servers does not use this data, so it can be formatted as needed for use in the game. Any player data strings for player IDs that are not included in the <code>PlayerIds</code> parameter are ignored. </p>

        Raises:
            capo_gamelift.errors.game_session_full_exception.GameSessionFullException: <p>The game instance is currently full and cannot allow the requested player(s) to join. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_game_session_status_exception.InvalidGameSessionStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_player_sessions_input.CreatePlayerSessionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_player_sessions_output.CreatePlayerSessionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_player_sessions

            output, http_response = (
                capo_gamelift._operations.game_lift.create_player_sessions.create_player_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_player_sessions_input.CreatePlayerSessionsInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if player_ids is not None:
            input_["player_ids"] = player_ids
        if player_data_map is not None:
            input_["player_data_map"] = player_data_map

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_script(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        version: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        storage_location: Optional["capo_gamelift.types.s3_location.S3Location"] = None,
        zip_file: Optional["capo_gamelift.types.zip_blob.ZipBlob"] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
        node_js_version: Optional[
            "capo_gamelift.types.node_js_version.NodeJsVersion"
        ] = None,
    ) -> "capo_gamelift.types.create_script_output.CreateScriptOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere</p> <p>Creates a new script record for your Amazon GameLift Servers Realtime script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Amazon GameLift Servers Realtime fleet to host your game sessions. Script logic is executed during an active game session. </p> <p>To create a new script record, specify a script name and provide the script file(s). The script files and all dependencies must be zipped into a single file. You can pull the zip file from either of these locations: </p> <ul> <li> <p>A locally available directory. Use the <i>ZipFile</i> parameter for this option.</p> </li> <li> <p>An Amazon Simple Storage Service (Amazon S3) bucket under your Amazon Web Services account. Use the <i>StorageLocation</i> parameter for this option. You'll need to have an Identity Access Management (IAM) role that allows the Amazon GameLift Servers service to access your S3 bucket. </p> </li> </ul> <p>If the call is successful, a new script record is created with a unique script ID. If the script file is provided as a local file, the file is uploaded to an Amazon GameLift Servers-owned S3 bucket and the script record's storage location reflects this location. If the script file is provided as an S3 bucket, Amazon GameLift Servers accesses the file at this storage location as needed for deployment.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html">Amazon GameLift Servers Amazon GameLift Servers Realtime</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/setting-up-role.html">Set Up a Role for Amazon GameLift Servers Access</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            name: <p>A descriptive label that is associated with a script. Script names do not need to be unique. You can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateScript.html">UpdateScript</a> to change this value later. </p>
            version: <p>Version information that is associated with a build or script. Version strings do not need to be unique. You can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateScript.html">UpdateScript</a> to change this value later. </p>
            storage_location: <p>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the <code>ObjectVersion</code> parameter to specify an earlier version. </p>
            zip_file: <p>A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.</p> <p>When using the Amazon Web Services CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: <code>--zip-file fileb://myRealtimeScript.zip</code>.</p>
            tags: <p>A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. Once the resource is created, you can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html">TagResource</a>, <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html">UntagResource</a>, and <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to add, remove, and view tags. The maximum tag limit may be lower than stated. See the Amazon Web Services General Reference for actual tagging limits.</p>
            node_js_version: <p>The Node.js version used for execution of your Realtime script. The valid values are <code>10.x | 24.x</code>. By default, <code>NodeJsVersion</code> is <code>10.x</code>. This value cannot be updated later. </p> <note> <p>Node.js 10 will reach end of support on September 30, 2026. See more details in the <a href="http://aws.amazon.com/gamelift/faq/nodejs10/">Node.js 10 FAQs</a>. For migration guidance, see <a href="https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration"> Migrating from Node.js 10 to 24</a>.</p> </note>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_script_input.CreateScriptInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_script_output.CreateScriptOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_script

            output, http_response = (
                capo_gamelift._operations.game_lift.create_script.create_script(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_script_input.CreateScriptInput = {}
        if name is not None:
            input_["name"] = name
        if version is not None:
            input_["version"] = version
        if storage_location is not None:
            input_["storage_location"] = storage_location
        if zip_file is not None:
            input_["zip_file"] = zip_file
        if tags is not None:
            input_["tags"] = tags
        if node_js_version is not None:
            input_["node_js_version"] = node_js_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_peering_authorization(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_lift_aws_account_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        peer_vpc_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.create_vpc_peering_authorization_output.CreateVpcPeeringAuthorizationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Requests authorization to create or delete a peer connection between the VPC for your Amazon GameLift Servers fleet and a virtual private cloud (VPC) in your Amazon Web Services account. VPC peering enables the game servers on your fleet to communicate directly with other Amazon Web Services resources. After you've received authorization, use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringConnection.html">CreateVpcPeeringConnection</a> to establish the peering connection. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p> <p>You can peer with VPCs that are owned by any Amazon Web Services account you have access to, including the account that you use to manage your Amazon GameLift Servers fleets. You cannot peer with VPCs that are in different Regions.</p> <p>To request authorization to create a connection, call this operation from the Amazon Web Services account with the VPC that you want to peer to your Amazon GameLift Servers fleet. For example, to enable your game servers to retrieve data from a DynamoDB table, use the account that manages that DynamoDB resource. Identify the following values: (1) The ID of the VPC that you want to peer with, and (2) the ID of the Amazon Web Services account that you use to manage Amazon GameLift Servers. If successful, VPC peering is authorized for the specified VPC. </p> <p>To request authorization to delete a connection, call this operation from the Amazon Web Services account with the VPC that is peered with your Amazon GameLift Servers fleet. Identify the following values: (1) VPC ID that you want to delete the peering connection for, and (2) ID of the Amazon Web Services account that you use to manage Amazon GameLift Servers. </p> <p>The authorization remains valid for 24 hours unless it is canceled. You must create or delete the peering connection while the authorization is valid. </p> <note> <p>Amazon GameLift Servers uses the caller's credentials to update peer-VPC resources. The IAM user that calls this operation must have the following Amazon EC2 permissions enabled:</p> <ul> <li> <p> <code>ec2:AcceptVpcPeeringConnection</code> </p> </li> <li> <p> <code>ec2:AuthorizeSecurityGroupEgress</code> </p> </li> <li> <p> <code>ec2:AuthorizeSecurityGroupIngress</code> </p> </li> <li> <p> <code>ec2:CreateRoute</code> </p> </li> <li> <p> <code>ec2:DescribeRouteTables</code> </p> </li> <li> <p> <code>ec2:DescribeSecurityGroups</code> </p> </li> </ul> </note> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_lift_aws_account_id: <p>A unique identifier for the Amazon Web Services account that you use to manage your Amazon GameLift Servers fleet. You can find your Account ID in the Amazon Web Services Management Console under account settings.</p>
            peer_vpc_id: <p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_vpc_peering_authorization_input.CreateVpcPeeringAuthorizationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_vpc_peering_authorization_output.CreateVpcPeeringAuthorizationOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_vpc_peering_authorization

            output, http_response = (
                capo_gamelift._operations.game_lift.create_vpc_peering_authorization.create_vpc_peering_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_vpc_peering_authorization_input.CreateVpcPeeringAuthorizationInput = {}
        if game_lift_aws_account_id is not None:
            input_["game_lift_aws_account_id"] = game_lift_aws_account_id
        if peer_vpc_id is not None:
            input_["peer_vpc_id"] = peer_vpc_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_vpc_peering_connection(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id.FleetId"] = None,
        peer_vpc_aws_account_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        peer_vpc_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.create_vpc_peering_connection_output.CreateVpcPeeringConnectionOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Establishes a VPC peering connection between a virtual private cloud (VPC) in an Amazon Web Services account with the VPC for your Amazon GameLift Servers fleet. VPC peering enables the game servers on your fleet to communicate directly with other Amazon Web Services resources. You can peer with VPCs in any Amazon Web Services account that you have access to, including the account that you use to manage your Amazon GameLift Servers fleets. You cannot peer with VPCs that are in different Regions. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p> <p>Before calling this operation to establish the peering connection, you first need to use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html">CreateVpcPeeringAuthorization</a> and identify the VPC you want to peer with. Once the authorization for the specified VPC is issued, you have 24 hours to establish the connection. These two operations handle all tasks necessary to peer the two VPCs, including acceptance, updating routing tables, etc. </p> <p>To establish the connection, call this operation from the Amazon Web Services account that is used to manage the Amazon GameLift Servers fleets. Identify the following values: (1) The ID of the fleet you want to enable a VPC peering connection for; (2) The Amazon Web Services account with the VPC that you want to peer with; and (3) The ID of the VPC you want to peer with. This operation is asynchronous. If successful, a connection request is created. You can use continuous polling to track the request's status using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeVpcPeeringConnections.html">DescribeVpcPeeringConnections</a> , or by monitoring fleet events for success or failure using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html">DescribeFleetEvents</a> . </p> <note> <p>Amazon GameLift Servers uses the caller's credentials to update peer-VPC resources. The IAM user that calls this operation must have the following Amazon EC2 permissions enabled:</p> <ul> <li> <p> <code>ec2:AcceptVpcPeeringConnection</code> </p> </li> <li> <p> <code>ec2:AuthorizeSecurityGroupEgress</code> </p> </li> <li> <p> <code>ec2:AuthorizeSecurityGroupIngress</code> </p> </li> <li> <p> <code>ec2:CreateRoute</code> </p> </li> <li> <p> <code>ec2:DescribeRouteTables</code> </p> </li> <li> <p> <code>ec2:DescribeSecurityGroups</code> </p> </li> </ul> </note> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet. You can use either the fleet ID or ARN value. This tells Amazon GameLift Servers which GameLift VPC to peer with. </p>
            peer_vpc_aws_account_id: <p>A unique identifier for the Amazon Web Services account with the VPC that you want to peer your Amazon GameLift Servers fleet with. You can find your Account ID in the Amazon Web Services Management Console under account settings.</p>
            peer_vpc_id: <p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.create_vpc_peering_connection_input.CreateVpcPeeringConnectionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.create_vpc_peering_connection_output.CreateVpcPeeringConnectionOutput"
        ]:
            import capo_gamelift._operations.game_lift.create_vpc_peering_connection

            output, http_response = (
                capo_gamelift._operations.game_lift.create_vpc_peering_connection.create_vpc_peering_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.create_vpc_peering_connection_input.CreateVpcPeeringConnectionInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if peer_vpc_aws_account_id is not None:
            input_["peer_vpc_aws_account_id"] = peer_vpc_aws_account_id
        if peer_vpc_id is not None:
            input_["peer_vpc_id"] = peer_vpc_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_alias(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
    ) -> None:
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Deletes an alias. This operation removes all record of the alias. Game clients attempting to access a server process using the deleted alias receive an error. To delete an alias, specify the alias ID to be deleted.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            alias_id: <p>A unique identifier of the alias that you want to delete. You can use either the alias ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_alias_input.DeleteAliasInput]",
        ) -> OperationResponse[None]:
            import capo_gamelift._operations.game_lift.delete_alias

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_alias.delete_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_alias_input.DeleteAliasInput = {}
        if alias_id is not None:
            input_["alias_id"] = alias_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_build(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
    ) -> None:
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Deletes a build. This operation permanently deletes the build resource and any uploaded build files. Deleting a build does not affect the status of any active fleets using the build, but you can no longer create new fleets with the deleted build.</p> <p>To delete a build, specify the build ID. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html"> Upload a Custom Server Build</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            build_id: <p>A unique identifier for the build to delete. You can use either the build ID or ARN value. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_build_input.DeleteBuildInput]",
        ) -> OperationResponse[None]:
            import capo_gamelift._operations.game_lift.delete_build

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_build.delete_build(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_build_input.DeleteBuildInput = {}
        if build_id is not None:
            input_["build_id"] = build_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_container_fleet(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
    ) -> "capo_gamelift.types.delete_container_fleet_output.DeleteContainerFleetOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Deletes all resources and information related to a container fleet and shuts down currently running fleet instances, including those in remote locations. The container fleet must be in <code>ACTIVE</code> status to be deleted.</p> <p>To delete a fleet, specify the fleet ID to be terminated. During the deletion process, the fleet status is changed to <code>DELETING</code>. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers Fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the container fleet to delete. You can use either the fleet ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_container_fleet_input.DeleteContainerFleetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_container_fleet_output.DeleteContainerFleetOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_container_fleet

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_container_fleet.delete_container_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_container_fleet_input.DeleteContainerFleetInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_container_group_definition(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        version_number: Optional[
            "capo_gamelift.types.positive_integer.PositiveInteger"
        ] = None,
        version_count_to_retain: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
    ) -> "capo_gamelift.types.delete_container_group_definition_output.DeleteContainerGroupDefinitionOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p> <b>Request options:</b> </p> <p>Deletes a container group definition. </p> <ul> <li> <p>Delete an entire container group definition, including all versions. Specify the container group definition name, or use an ARN value without the version number.</p> </li> <li> <p>Delete a particular version. Specify the container group definition name and a version number, or use an ARN value that includes the version number.</p> </li> <li> <p>Keep the newest versions and delete all older versions. Specify the container group definition name and the number of versions to retain. For example, set <code>VersionCountToRetain</code> to 5 to delete all but the five most recent versions.</p> </li> </ul> <p> <b>Result</b> </p> <p>If successful, Amazon GameLift Servers removes the container group definition versions that you request deletion for. This request will fail for any requested versions if the following is true: </p> <ul> <li> <p>If the version is being used in an active fleet</p> </li> <li> <p>If the version is being deployed to a fleet in a deployment that's currently in progress.</p> </li> <li> <p>If the version is designated as a rollback definition in a fleet deployment that's currently in progress.</p> </li> </ul> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html">Manage a container group definition</a> </p> </li> </ul>

        Args:
            name: <p>The unique identifier for the container group definition to delete. You can use either the <code>Name</code> or <code>ARN</code> value.</p>
            version_number: <p>The specific version to delete.</p>
            version_count_to_retain: <p>The number of most recent versions to keep while deleting all older versions.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_container_group_definition_input.DeleteContainerGroupDefinitionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_container_group_definition_output.DeleteContainerGroupDefinitionOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_container_group_definition

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_container_group_definition.delete_container_group_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_container_group_definition_input.DeleteContainerGroupDefinitionInput = {}
        if name is not None:
            input_["name"] = name
        if version_number is not None:
            input_["version_number"] = version_number
        if version_count_to_retain is not None:
            input_["version_count_to_retain"] = version_count_to_retain

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_fleet(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
    ) -> None:
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere</p> <p>Deletes all resources and information related to a fleet and shuts down any currently running fleet instances, including those in remote locations.</p> <note> <p>If the fleet being deleted has a VPC peering connection, you first need to get a valid authorization (good for 24 hours) by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.html">CreateVpcPeeringAuthorization</a>. You don't need to explicitly delete the VPC peering connection.</p> </note> <p>To delete a fleet, specify the fleet ID to be terminated. During the deletion process, the fleet status is changed to <code>DELETING</code>. When completed, the status switches to <code>TERMINATED</code> and the fleet event <code>FLEET_DELETED</code> is emitted.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers Fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to be deleted. You can use either the fleet ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_fleet_input.DeleteFleetInput]",
        ) -> OperationResponse[None]:
            import capo_gamelift._operations.game_lift.delete_fleet

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_fleet.delete_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_fleet_input.DeleteFleetInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_fleet_locations(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        locations: Optional["capo_gamelift.types.location_list.LocationList"] = None,
    ) -> "capo_gamelift.types.delete_fleet_locations_output.DeleteFleetLocationsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Removes locations from a multi-location fleet. When deleting a location, all game server processes and all instances that are still active in the location are shut down. </p> <p>To delete fleet locations, identify the fleet ID and provide a list of the locations to be deleted. </p> <p>If successful, GameLift sets the location status to <code>DELETING</code>, and begins to shut down existing server processes and terminate instances in each location being deleted. When completed, the location status changes to <code>TERMINATED</code>.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to delete locations for. You can use either the fleet ID or ARN value.</p>
            locations: <p>The list of fleet locations to delete. Specify locations in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_fleet_locations_input.DeleteFleetLocationsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_fleet_locations_output.DeleteFleetLocationsOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_fleet_locations

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_fleet_locations.delete_fleet_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_fleet_locations_input.DeleteFleetLocationsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if locations is not None:
            input_["locations"] = locations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_game_server_group(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        delete_option: Optional[
            "capo_gamelift.types.game_server_group_delete_option.GameServerGroupDeleteOption"
        ] = None,
    ) -> "capo_gamelift.types.delete_game_server_group_output.DeleteGameServerGroupOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Terminates a game server group and permanently deletes the game server group record. You have several options for how these resources are impacted when deleting the game server group. Depending on the type of delete operation selected, this operation might affect these resources:</p> <ul> <li> <p>The game server group</p> </li> <li> <p>The corresponding Auto Scaling group</p> </li> <li> <p>All game servers that are currently running in the group</p> </li> </ul> <p>To delete a game server group, identify the game server group to delete and specify the type of delete operation to initiate. Game server groups can only be deleted if they are in <code>ACTIVE</code> or <code>ERROR</code> status.</p> <p>If the delete request is successful, a series of operations are kicked off. The game server group status is changed to <code>DELETE_SCHEDULED</code>, which prevents new game servers from being registered and stops automatic scaling activity. Once all game servers in the game server group are deregistered, Amazon GameLift Servers FleetIQ can begin deleting resources. If any of the delete operations fail, the game server group is placed in <code>ERROR</code> status.</p> <p>Amazon GameLift Servers FleetIQ emits delete events to Amazon CloudWatch.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group. Use either the name or ARN value.</p>
            delete_option: <p>The type of delete to perform. Options include the following:</p> <ul> <li> <p> <code>SAFE_DELETE</code> – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in <code>UTILIZED</code> status.</p> </li> <li> <p> <code>FORCE_DELETE</code> – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group. </p> </li> <li> <p> <code>RETAIN</code> – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.</p> </li> </ul>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_game_server_group_input.DeleteGameServerGroupInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_game_server_group_output.DeleteGameServerGroupOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_game_server_group

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_game_server_group.delete_game_server_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_game_server_group_input.DeleteGameServerGroupInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if delete_option is not None:
            input_["delete_option"] = delete_option

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_game_session_queue(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
        ] = None,
    ) -> "capo_gamelift.types.delete_game_session_queue_output.DeleteGameSessionQueueOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Deletes a game session queue. Once a queue is successfully deleted, unfulfilled <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartGameSessionPlacement.html">StartGameSessionPlacement</a> requests that reference the queue will fail. To delete a queue, specify the queue name.</p>

        Args:
            name: <p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_game_session_queue_input.DeleteGameSessionQueueInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_game_session_queue_output.DeleteGameSessionQueueOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_game_session_queue

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_game_session_queue.delete_game_session_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_game_session_queue_input.DeleteGameSessionQueueInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_location(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        location_name: Optional[
            "capo_gamelift.types.custom_location_name_or_arn_model.CustomLocationNameOrArnModel"
        ] = None,
    ) -> "capo_gamelift.types.delete_location_output.DeleteLocationOutput":
        """<p> <b>This API works with the following fleet types:</b> Anywhere</p> <p>Deletes a custom location.</p> <p>Before deleting a custom location, review any fleets currently using the custom location and deregister the location if it is in use. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeregisterCompute.html">DeregisterCompute</a>.</p>

        Args:
            location_name: <p>The location name of the custom location to be deleted.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_location_input.DeleteLocationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_location_output.DeleteLocationOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_location

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_location.delete_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_location_input.DeleteLocationInput = {}
        if location_name is not None:
            input_["location_name"] = location_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_matchmaking_configuration(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
        ] = None,
    ) -> "capo_gamelift.types.delete_matchmaking_configuration_output.DeleteMatchmakingConfigurationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Permanently removes a FlexMatch matchmaking configuration. To delete, specify the configuration name. A matchmaking configuration cannot be deleted if it is being used in any active matchmaking tickets.</p>

        Args:
            name: <p>A unique identifier for the matchmaking configuration. You can use either the configuration name or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_matchmaking_configuration_input.DeleteMatchmakingConfigurationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_matchmaking_configuration_output.DeleteMatchmakingConfigurationOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_matchmaking_configuration

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_matchmaking_configuration.delete_matchmaking_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_matchmaking_configuration_input.DeleteMatchmakingConfigurationInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_matchmaking_rule_set(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
        ] = None,
    ) -> "capo_gamelift.types.delete_matchmaking_rule_set_output.DeleteMatchmakingRuleSetOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Deletes an existing matchmaking rule set. To delete the rule set, provide the rule set name. Rule sets cannot be deleted if they are currently being used by a matchmaking configuration. </p> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html">Build a rule set</a> </p> </li> </ul>

        Args:
            name: <p>A unique identifier for the matchmaking rule set to be deleted. (Note: The rule set name is different from the optional "name" field in the rule set body.) You can use either the rule set name or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_matchmaking_rule_set_input.DeleteMatchmakingRuleSetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_matchmaking_rule_set_output.DeleteMatchmakingRuleSetOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_matchmaking_rule_set

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_matchmaking_rule_set.delete_matchmaking_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_matchmaking_rule_set_input.DeleteMatchmakingRuleSetInput = {}
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scaling_policy(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
    ) -> None:
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Deletes a fleet scaling policy. Once deleted, the policy is no longer in force and Amazon GameLift Servers removes all record of it. To delete a scaling policy, specify both the scaling policy name and the fleet ID it is associated with.</p> <p>To temporarily suspend scaling policies, use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html">StopFleetActions</a>. This operation suspends all policies for the fleet.</p>

        Args:
            name: <p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.</p>
            fleet_id: <p>A unique identifier for the fleet to be deleted. You can use either the fleet ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_scaling_policy_input.DeleteScalingPolicyInput]",
        ) -> OperationResponse[None]:
            import capo_gamelift._operations.game_lift.delete_scaling_policy

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_scaling_policy.delete_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_scaling_policy_input.DeleteScalingPolicyInput = {}
        if name is not None:
            input_["name"] = name
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_script(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        script_id: Optional[
            "capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"
        ] = None,
    ) -> None:
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Deletes a Realtime script. This operation permanently deletes the script record. If script files were uploaded, they are also deleted (files stored in an S3 bucket are not deleted). </p> <p>To delete a script, specify the script ID. Before deleting a script, be sure to terminate all fleets that are deployed with the script being deleted. Fleet instances periodically check for script updates, and if the script record no longer exists, the instance will go into an error state and be unable to host game sessions.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html">Amazon GameLift Servers Amazon GameLift Servers Realtime</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            script_id: <p>A unique identifier for the Realtime script to delete. You can use either the script ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_script_input.DeleteScriptInput]",
        ) -> OperationResponse[None]:
            import capo_gamelift._operations.game_lift.delete_script

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_script.delete_script(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_script_input.DeleteScriptInput = {}
        if script_id is not None:
            input_["script_id"] = script_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_peering_authorization(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_lift_aws_account_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        peer_vpc_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.delete_vpc_peering_authorization_output.DeleteVpcPeeringAuthorizationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Cancels a pending VPC peering authorization for the specified VPC. If you need to delete an existing VPC peering connection, use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DeleteVpcPeeringConnection.html">DeleteVpcPeeringConnection</a>.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_lift_aws_account_id: <p>A unique identifier for the Amazon Web Services account that you use to manage your Amazon GameLift Servers fleet. You can find your Account ID in the Amazon Web Services Management Console under account settings.</p>
            peer_vpc_id: <p>A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the <a href="https://console.aws.amazon.com/vpc/">VPC Dashboard</a> in the Amazon Web Services Management Console. Learn more about VPC peering in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html">VPC Peering with Amazon GameLift Servers Fleets</a>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_vpc_peering_authorization_input.DeleteVpcPeeringAuthorizationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_vpc_peering_authorization_output.DeleteVpcPeeringAuthorizationOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_vpc_peering_authorization

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_vpc_peering_authorization.delete_vpc_peering_authorization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_vpc_peering_authorization_input.DeleteVpcPeeringAuthorizationInput = {}
        if game_lift_aws_account_id is not None:
            input_["game_lift_aws_account_id"] = game_lift_aws_account_id
        if peer_vpc_id is not None:
            input_["peer_vpc_id"] = peer_vpc_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vpc_peering_connection(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id.FleetId"] = None,
        vpc_peering_connection_id: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.delete_vpc_peering_connection_output.DeleteVpcPeeringConnectionOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Removes a VPC peering connection. To delete the connection, you must have a valid authorization for the VPC peering connection that you want to delete. </p> <p>Once a valid authorization exists, call this operation from the Amazon Web Services account that is used to manage the Amazon GameLift Servers fleets. Identify the connection to delete by the connection ID and fleet ID. If successful, the connection is removed. </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet. This fleet specified must match the fleet referenced in the VPC peering connection record. You can use either the fleet ID or ARN value.</p>
            vpc_peering_connection_id: <p>A unique identifier for a VPC peering connection.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.delete_vpc_peering_connection_input.DeleteVpcPeeringConnectionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.delete_vpc_peering_connection_output.DeleteVpcPeeringConnectionOutput"
        ]:
            import capo_gamelift._operations.game_lift.delete_vpc_peering_connection

            output, http_response = (
                capo_gamelift._operations.game_lift.delete_vpc_peering_connection.delete_vpc_peering_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.delete_vpc_peering_connection_input.DeleteVpcPeeringConnectionInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if vpc_peering_connection_id is not None:
            input_["vpc_peering_connection_id"] = vpc_peering_connection_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_compute(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        compute_name: Optional[
            "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
        ] = None,
    ) -> "capo_gamelift.types.deregister_compute_output.DeregisterComputeOutput":
        """<p> <b>This API works with the following fleet types:</b> Anywhere</p> <p>Removes a compute resource from an Anywhere fleet. Deregistered computes can no longer host game sessions through Amazon GameLift Servers. Use this operation with an Anywhere fleet that doesn't use the Amazon GameLift Servers Agent. For Anywhere fleets with the Agent, the Agent handles all compute registry tasks for you. </p> <p>To deregister a compute, call this operation from the compute that's being deregistered and specify the compute name and the fleet ID. </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet the compute resource is currently registered to.</p>
            compute_name: <p>The unique identifier of the compute resource to deregister. For an Anywhere fleet compute, use the registered compute name.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.deregister_compute_input.DeregisterComputeInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.deregister_compute_output.DeregisterComputeOutput"
        ]:
            import capo_gamelift._operations.game_lift.deregister_compute

            output, http_response = (
                capo_gamelift._operations.game_lift.deregister_compute.deregister_compute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.deregister_compute_input.DeregisterComputeInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if compute_name is not None:
            input_["compute_name"] = compute_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_game_server(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        game_server_id: Optional[
            "capo_gamelift.types.game_server_id.GameServerId"
        ] = None,
    ) -> None:
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Removes the game server from a game server group. As a result of this operation, the deregistered game server can no longer be claimed and will not be returned in a list of active game servers. </p> <p>To deregister a game server, specify the game server group and game server ID. If successful, this operation emits a CloudWatch event with termination timestamp and reason.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group where the game server is running.</p>
            game_server_id: <p>A custom string that uniquely identifies the game server to deregister.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.deregister_game_server_input.DeregisterGameServerInput]",
        ) -> OperationResponse[None]:
            import capo_gamelift._operations.game_lift.deregister_game_server

            output, http_response = (
                capo_gamelift._operations.game_lift.deregister_game_server.deregister_game_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.deregister_game_server_input.DeregisterGameServerInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if game_server_id is not None:
            input_["game_server_id"] = game_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_alias(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
    ) -> "capo_gamelift.types.describe_alias_output.DescribeAliasOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves properties for an alias. This operation returns all alias metadata and settings. To get an alias's target fleet ID only, use <code>ResolveAlias</code>. </p> <p>To get alias properties, specify the alias ID. If successful, the requested alias record is returned.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            alias_id: <p>The unique identifier for the fleet alias that you want to retrieve. You can use either the alias ID or ARN value. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_alias_input.DescribeAliasInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_alias_output.DescribeAliasOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_alias

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_alias.describe_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_alias_input.DescribeAliasInput = {}
        if alias_id is not None:
            input_["alias_id"] = alias_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_build(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
    ) -> "capo_gamelift.types.describe_build_output.DescribeBuildOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves properties for a custom game build. To request a build resource, specify a build ID. If successful, an object containing the build properties is returned.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html"> Upload a Custom Server Build</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            build_id: <p>A unique identifier for the build to retrieve properties for. You can use either the build ID or ARN value. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_build_input.DescribeBuildInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_build_output.DescribeBuildOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_build

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_build.describe_build(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_build_input.DescribeBuildInput = {}
        if build_id is not None:
            input_["build_id"] = build_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_compute(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        compute_name: Optional[
            "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
        ] = None,
    ) -> "capo_gamelift.types.describe_compute_output.DescribeComputeOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves properties for a specific compute resource in an Amazon GameLift Servers fleet. You can list all computes in a fleet by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html">ListCompute</a>. </p> <p> <b>Request options</b> </p> <p>Provide the fleet ID and compute name. The compute name varies depending on the type of fleet.</p> <ul> <li> <p>For a compute in a managed EC2 fleet, provide an instance ID. Each instance in the fleet is a compute.</p> </li> <li> <p>For a compute in a managed container fleet, provide a compute name. In a container fleet, each game server container group on a fleet instance is assigned a compute name.</p> </li> <li> <p>For a compute in an Anywhere fleet, provide a registered compute name. Anywhere fleet computes are created when you register a hosting resource with the fleet.</p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation returns details for the requested compute resource. Depending on the fleet's compute type, the result includes the following information: </p> <ul> <li> <p>For a managed EC2 fleet, this operation returns information about the EC2 instance.</p> </li> <li> <p>For an Anywhere fleet, this operation returns information about the registered compute.</p> </li> </ul>

        Args:
            fleet_id: <p>A unique identifier for the fleet that the compute belongs to. You can use either the fleet ID or ARN value.</p>
            compute_name: <p>The unique identifier of the compute resource to retrieve properties for. For a managed container fleet or Anywhere fleet, use a compute name. For an EC2 fleet, use an instance ID. To retrieve a fleet's compute identifiers, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html">ListCompute</a>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_compute_input.DescribeComputeInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_compute_output.DescribeComputeOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_compute

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_compute.describe_compute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_compute_input.DescribeComputeInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if compute_name is not None:
            input_["compute_name"] = compute_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_container_fleet(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
    ) -> "capo_gamelift.types.describe_container_fleet_output.DescribeContainerFleetOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves the properties for a container fleet. When requesting attributes for multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. </p> <p> <b>Request options</b> </p> <ul> <li> <p>Get container fleet properties for a single fleet. Provide either the fleet ID or ARN value. </p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, a <code>ContainerFleet</code> object is returned. This object includes the fleet properties, including information about the most recent deployment.</p> <note> <p>Some API operations limit the number of fleet IDs that are allowed in one request. If a request exceeds this limit, the request fails and the error message contains the maximum allowed number.</p> </note>

        Args:
            fleet_id: <p>A unique identifier for the container fleet to retrieve. You can use either the fleet ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_container_fleet_input.DescribeContainerFleetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_container_fleet_output.DescribeContainerFleetOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_container_fleet

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_container_fleet.describe_container_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_container_fleet_input.DescribeContainerFleetInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_container_group_definition(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        version_number: Optional[
            "capo_gamelift.types.positive_integer.PositiveInteger"
        ] = None,
    ) -> "capo_gamelift.types.describe_container_group_definition_output.DescribeContainerGroupDefinitionOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves the properties of a container group definition, including all container definitions in the group. </p> <p> <b>Request options:</b> </p> <ul> <li> <p>Retrieve the latest version of a container group definition. Specify the container group definition name only, or use an ARN value without a version number.</p> </li> <li> <p>Retrieve a particular version. Specify the container group definition name and a version number, or use an ARN value that includes the version number.</p> </li> </ul> <p> <b>Results:</b> </p> <p>If successful, this operation returns the complete properties of a container group definition version.</p> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html">Manage a container group definition</a> </p> </li> </ul>

        Args:
            name: <p>The unique identifier for the container group definition to retrieve properties for. You can use either the <code>Name</code> or <code>ARN</code> value.</p>
            version_number: <p>The specific version to retrieve.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_container_group_definition_input.DescribeContainerGroupDefinitionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_container_group_definition_output.DescribeContainerGroupDefinitionOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_container_group_definition

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_container_group_definition.describe_container_group_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_container_group_definition_input.DescribeContainerGroupDefinitionInput = {}
        if name is not None:
            input_["name"] = name
        if version_number is not None:
            input_["version_number"] = version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_container_group_port_mappings(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        container_group_type: Optional[
            "capo_gamelift.types.container_group_type.ContainerGroupType"
        ] = None,
        compute_name: Optional[
            "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
        ] = None,
        instance_id: Optional["capo_gamelift.types.instance_id.InstanceId"] = None,
        container_name: Optional[
            "capo_gamelift.types.container_name_query_filter.ContainerNameQueryFilter"
        ] = None,
    ) -> "capo_gamelift.types.describe_container_group_port_mappings_output.DescribeContainerGroupPortMappingsOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves the port mappings for a container group running on a container fleet. Port mappings show how container ports are mapped to connection ports on the fleet instance. Use this operation to find the connection port for a specific container on a fleet instance.</p> <p> <b>Request options</b> </p> <ul> <li> <p>Get port mappings for a game server container group. Provide the fleet ID, set <code>ContainerGroupType</code> to <code>GAME_SERVER</code>, and specify the <code>ComputeName</code> for the game server container group.</p> </li> <li> <p>Get port mappings for a per-instance container group. Provide the fleet ID, set <code>ContainerGroupType</code> to <code>PER_INSTANCE</code>, and specify the <code>InstanceId</code> for the instance.</p> </li> <li> <p>Optionally filter results to a single container by providing a <code>ContainerName</code>.</p> </li> </ul> <p> <b>Results</b> </p> <p>This operation returns the fleet ID, fleet ARN, location, container group definition ARN, container group type, compute name (for game server container groups), instance ID, and a list of <code>ContainerGroupPortMapping</code> objects. Each object contains the container name, runtime ID, and a list of port mappings that show how container ports map to connection ports on the instance.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-remote-access.html">Connect to containers</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html">Create a container group definition</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the container fleet. You can use either the fleet ID or ARN value.</p>
            container_group_type: <p>The type of container group to retrieve port mappings for.</p> <ul> <li> <p> <code>GAME_SERVER</code> -- Get port mappings for a game server container group.</p> </li> <li> <p> <code>PER_INSTANCE</code> -- Get port mappings for a per-instance container group.</p> </li> </ul>
            compute_name: <p>A unique identifier for the compute resource for which to retrieve port mappings. For a container fleet, a compute represents a game server container group running on a fleet instance. You can use either the compute name or ARN value.</p> <p>When <code>ContainerGroupType</code> is <code>GAME_SERVER</code>, this parameter is required.</p> <p>When <code>ContainerGroupType</code> is <code>PER_INSTANCE</code>, do not provide this parameter. If you provide a compute name with <code>PER_INSTANCE</code>, the request fails with an <code>InvalidRequestException</code>.</p>
            instance_id: <p>A unique identifier for the fleet instance to retrieve port mappings for.</p> <p>When <code>ContainerGroupType</code> is <code>PER_INSTANCE</code>, this parameter is required.</p> <p>When <code>ContainerGroupType</code> is <code>GAME_SERVER</code>, this parameter is optional. If you provide an instance ID, it must match the instance that's running the specified compute. If the instance ID doesn't match, the request fails with an <code>InvalidRequestException</code>.</p>
            container_name: <p>A container name to filter the results. When provided, the operation returns port mappings for the specified container only. If no container with the specified name exists in the container group, the request fails with a <code>NotFoundException</code>.</p> <p>If not provided, the operation returns port mappings for all containers in the container group.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_container_group_port_mappings_input.DescribeContainerGroupPortMappingsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_container_group_port_mappings_output.DescribeContainerGroupPortMappingsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_container_group_port_mappings

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_container_group_port_mappings.describe_container_group_port_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_container_group_port_mappings_input.DescribeContainerGroupPortMappingsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if container_group_type is not None:
            input_["container_group_type"] = container_group_type
        if compute_name is not None:
            input_["compute_name"] = compute_name
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if container_name is not None:
            input_["container_name"] = container_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_ec2_instance_limits(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        ec2_instance_type: Optional[
            "capo_gamelift.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_ec2_instance_limits_output.DescribeEC2InstanceLimitsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves the instance limits and current utilization for an Amazon Web Services Region or location. Instance limits control the number of instances, per instance type, per location, that your Amazon Web Services account can use. Learn more at <a href="http://aws.amazon.com/ec2/instance-types/">Amazon EC2 Instance Types</a>. The information returned includes the maximum number of instances allowed and your account's current usage across all fleets. This information can affect your ability to scale your Amazon GameLift Servers fleets. You can request a limit increase for your account by using the <b>Service limits</b> page in the Amazon GameLift Servers console.</p> <p>Instance limits differ based on whether the instances are deployed in a fleet's home Region or in a remote location. For remote locations, limits also differ based on the combination of home Region and remote location. All requests must specify an Amazon Web Services Region (either explicitly or as your default settings). To get the limit for a remote location, you must also specify the location. To learn more about how Amazon GameLift Servers handles locations, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html">Amazon GameLift Servers service locations</a>. For example, the following requests all return different results: </p> <ul> <li> <p>Request specifies the Region <code>ap-northeast-1</code> with no location. The result is limits and usage data on all of the fleets that reside in <code>ap-northeast-1</code>, for all instance types that are deployed in <code>ap-northeast-1</code>. </p> </li> <li> <p>Request specifies the Region <code>ap-northeast-1</code> with location <code>us-west-2</code>. The result is limits and usage data on all of the fleets that reside in <code>ap-northeast-1</code>, for all instance types that are deployed in <code>us-west-2</code>.</p> </li> <li> <p>Request specifies the Region <code>us-east-1</code> with location <code>ap-northeast-1</code>. The result is limits and usage data on all of the fleets that reside in <code>us-east-1</code>, for all instance types that are deployed in <code>ap-northeast-1</code>. These limits do not affect fleets in any other Regions that deploy instances to <code>ap-northeast-1</code>.</p> </li> </ul> <p>This operation can be used in the following ways:</p> <ul> <li> <p>To get limit and usage data for all instance types that are deployed in an Amazon Web Services Region by fleets that reside in the same Region: Specify the Region only. Optionally, specify a single instance type to retrieve information for.</p> </li> <li> <p>To get limit and usage data for all instance types that are deployed to a remote location by fleets that reside in different Amazon Web Services Region: Provide both the Amazon Web Services Region and the remote location. Optionally, specify a single instance type to retrieve information for.</p> </li> </ul> <p>If successful, an <code>EC2InstanceLimits</code> object is returned with limits and usage data for each requested instance type.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            ec2_instance_type: <p>Name of an Amazon EC2 instance type that is supported in Amazon GameLift Servers. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Do not specify a value for this parameter to retrieve limits for all instance types.</p>
            location: <p>The name of a remote location to request instance limits for, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_ec2_instance_limits_input.DescribeEC2InstanceLimitsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_ec2_instance_limits_output.DescribeEC2InstanceLimitsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_ec2_instance_limits

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_ec2_instance_limits.describe_ec2_instance_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_ec2_instance_limits_input.DescribeEC2InstanceLimitsInput = {}
        if ec2_instance_type is not None:
            input_["ec2_instance_type"] = ec2_instance_type
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fleet_attributes(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_ids: Optional[
            "capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_attributes_output.DescribeFleetAttributesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere</p> <p>Retrieves core fleet-wide properties for fleets in an Amazon Web Services Region. Properties include the computing hardware and deployment configuration for instances in the fleet.</p> <p>You can use this operation in the following ways: </p> <ul> <li> <p>To get attributes for specific fleets, provide a list of fleet IDs or fleet ARNs.</p> </li> <li> <p>To get attributes for all fleets, do not provide a fleet identifier.</p> </li> </ul> <p>When requesting attributes for multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>FleetAttributes</code> object is returned for each fleet requested, unless the fleet identifier is not found. </p> <note> <p>Some API operations limit the number of fleet IDs that are allowed in one request. If a request exceeds this limit, the request fails and the error message contains the maximum allowed number.</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_ids: <p>A list of unique fleet identifiers to retrieve attributes for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_attributes_input.DescribeFleetAttributesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_attributes_output.DescribeFleetAttributesOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_attributes

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_attributes.describe_fleet_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_attributes_input.DescribeFleetAttributesInput = {}
        if fleet_ids is not None:
            input_["fleet_ids"] = fleet_ids
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

    def iter_describe_fleet_attributes(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_ids: Optional[
            "capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.fleet_attributes.FleetAttributes]":
        _token = next_token
        while True:
            _response = self.describe_fleet_attributes(
                config_overrides=config_overrides,
                fleet_ids=fleet_ids,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fleet_attributes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_fleet_capacity(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_ids: Optional[
            "capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> (
        "capo_gamelift.types.describe_fleet_capacity_output.DescribeFleetCapacityOutput"
    ):
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Retrieves the resource capacity settings for one or more fleets. For a container fleet, this operation also returns counts for game server container groups.</p> <p>With multi-location fleets, this operation retrieves data for the fleet's home Region only. To retrieve capacity for remote locations, see <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html">https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html</a>.</p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To get capacity data for one or more specific fleets, provide a list of fleet IDs or fleet ARNs. </p> </li> <li> <p>To get capacity data for all fleets, do not provide a fleet identifier. </p> </li> </ul> <p>When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>FleetCapacity</code> object is returned for each requested fleet ID. Each <code>FleetCapacity</code> object includes a <code>Location</code> property, which is set to the fleet's home Region. Capacity values are returned only for fleets that currently exist.</p> <note> <p>Some API operations may limit the number of fleet IDs that are allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet">GameLift metrics for fleets</a> </p>

        Args:
            fleet_ids: <p>A unique identifier for the fleet to retrieve capacity information for. You can use either the fleet ID or ARN value. Leave this parameter empty to retrieve capacity information for all fleets.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_capacity_input.DescribeFleetCapacityInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_capacity_output.DescribeFleetCapacityOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_capacity

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_capacity.describe_fleet_capacity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_capacity_input.DescribeFleetCapacityInput = {}
        if fleet_ids is not None:
            input_["fleet_ids"] = fleet_ids
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

    def iter_describe_fleet_capacity(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_ids: Optional[
            "capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.fleet_capacity.FleetCapacity]":
        _token = next_token
        while True:
            _response = self.describe_fleet_capacity(
                config_overrides=config_overrides,
                fleet_ids=fleet_ids,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fleet_capacity",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_fleet_deployment(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        deployment_id: Optional[
            "capo_gamelift.types.deployment_id.DeploymentId"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_deployment_output.DescribeFleetDeploymentOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves information about a managed container fleet deployment. </p> <p> <b>Request options</b> </p> <ul> <li> <p>Get information about the latest deployment for a specific fleet. Provide the fleet ID or ARN.</p> </li> <li> <p> Get information about a specific deployment. Provide the fleet ID or ARN and the deployment ID.</p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, a <code>FleetDeployment</code> object is returned.</p>

        Args:
            fleet_id: <p>A unique identifier for the container fleet. You can use either the fleet ID or ARN value.</p>
            deployment_id: <p>A unique identifier for the deployment to return information for. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_deployment_input.DescribeFleetDeploymentInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_deployment_output.DescribeFleetDeploymentOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_deployment

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_deployment.describe_fleet_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_deployment_input.DescribeFleetDeploymentInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if deployment_id is not None:
            input_["deployment_id"] = deployment_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fleet_events(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        start_time: Optional["capo_gamelift.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_gamelift.types.timestamp.Timestamp"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_events_output.DescribeFleetEventsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves entries from a fleet's event log. Fleet events are initiated by changes in status, such as during fleet creation and termination, changes in capacity, etc. If a fleet has multiple locations, events are also initiated by changes to status and capacity in remote locations.</p> <p>You can specify a time range to limit the result set. Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a collection of event log entries matching the request are returned.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to get event logs for. You can use either the fleet ID or ARN value.</p>
            start_time: <p>The earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").</p>
            end_time: <p>The most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: "1469498468.057").</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_events_input.DescribeFleetEventsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_events_output.DescribeFleetEventsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_events

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_events.describe_fleet_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_events_input.DescribeFleetEventsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    def iter_describe_fleet_events(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        start_time: Optional["capo_gamelift.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_gamelift.types.timestamp.Timestamp"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.event.Event]":
        _token = next_token
        while True:
            _response = self.describe_fleet_events(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_fleet_location_attributes(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        locations: Optional["capo_gamelift.types.location_list.LocationList"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_location_attributes_output.DescribeFleetLocationAttributesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves information on a fleet's remote locations, including life-cycle status and any suspended fleet activity. </p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To get data for specific locations, provide a fleet identifier and a list of locations. Location data is returned in the order that it is requested. </p> </li> <li> <p>To get data for all locations, provide a fleet identifier only. Location data is returned in no particular order. </p> </li> </ul> <p>When requesting attributes for multiple locations, use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>LocationAttributes</code> object is returned for each requested location. If the fleet does not have a requested location, no information is returned. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting</p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to retrieve remote locations for. You can use either the fleet ID or ARN value.</p>
            locations: <p>A list of fleet locations to retrieve information for. Specify locations in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This limit is not currently enforced.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_location_attributes_input.DescribeFleetLocationAttributesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_location_attributes_output.DescribeFleetLocationAttributesOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_location_attributes

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_location_attributes.describe_fleet_location_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_location_attributes_input.DescribeFleetLocationAttributesInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if locations is not None:
            input_["locations"] = locations
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

    def iter_describe_fleet_location_attributes(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        locations: Optional["capo_gamelift.types.location_list.LocationList"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.describe_fleet_location_attributes_output.DescribeFleetLocationAttributesOutput]":
        _token = next_token
        while True:
            _response = self.describe_fleet_location_attributes(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                locations=locations,
                limit=limit,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_fleet_location_capacity(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_location_capacity_output.DescribeFleetLocationCapacityOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves the resource capacity settings for a fleet location. The data returned includes the current capacity (number of EC2 instances) and some scaling settings for the requested fleet location. For a managed container fleet, this operation also returns counts for game server container groups.</p> <p>Use this operation to retrieve capacity information for a fleet's remote location or home Region (you can also retrieve home Region capacity by calling <code>DescribeFleetCapacity</code>).</p> <p>To retrieve capacity data, identify a fleet and location. </p> <p>If successful, a <code>FleetCapacity</code> object is returned for the requested fleet location. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting</p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet">GameLift metrics for fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to request location capacity for. You can use either the fleet ID or ARN value.</p>
            location: <p>The fleet location to retrieve capacity information for. Specify a location in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_location_capacity_input.DescribeFleetLocationCapacityInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_location_capacity_output.DescribeFleetLocationCapacityOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_location_capacity

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_location_capacity.describe_fleet_location_capacity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_location_capacity_input.DescribeFleetLocationCapacityInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fleet_location_utilization(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_location_utilization_output.DescribeFleetLocationUtilizationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere</p> <p>Retrieves current usage data for a fleet location. Utilization data provides a snapshot of current game hosting activity at the requested location. Use this operation to retrieve utilization information for a fleet's remote location or home Region (you can also retrieve home Region utilization by calling <code>DescribeFleetUtilization</code>).</p> <p>To retrieve utilization data, identify a fleet and location. </p> <p>If successful, a <code>FleetUtilization</code> object is returned for the requested fleet location. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html"> Amazon GameLift Servers service locations</a> for managed hosting</p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet">GameLift metrics for fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to request location utilization for. You can use either the fleet ID or ARN value.</p>
            location: <p>The fleet location to retrieve utilization information for. Specify a location in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_location_utilization_input.DescribeFleetLocationUtilizationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_location_utilization_output.DescribeFleetLocationUtilizationOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_location_utilization

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_location_utilization.describe_fleet_location_utilization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_location_utilization_input.DescribeFleetLocationUtilizationInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fleet_port_settings(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_port_settings_output.DescribeFleetPortSettingsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves a fleet's inbound connection permissions. Connection permissions specify IP addresses and port settings that incoming traffic can use to access server processes in the fleet. Game server processes that are running in the fleet must use a port that falls within this range. </p> <p>Use this operation in the following ways: </p> <ul> <li> <p>To retrieve the port settings for a fleet, identify the fleet's unique identifier. </p> </li> <li> <p>To check the status of recent updates to a fleet remote location, specify the fleet ID and a location. Port setting updates can take time to propagate across all locations. </p> </li> </ul> <p>If successful, a set of <code>IpPermission</code> objects is returned for the requested fleet ID. When specifying a location, this operation returns a pending status. If the requested fleet has been deleted, the result set is empty.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to retrieve port settings for. You can use either the fleet ID or ARN value.</p>
            location: <p>A remote location to check for status of port setting updates. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_port_settings_input.DescribeFleetPortSettingsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_port_settings_output.DescribeFleetPortSettingsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_port_settings

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_port_settings.describe_fleet_port_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_port_settings_input.DescribeFleetPortSettingsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_fleet_utilization(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_ids: Optional[
            "capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_fleet_utilization_output.DescribeFleetUtilizationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves utilization statistics for one or more fleets. Utilization data provides a snapshot of how the fleet's hosting resources are currently being used. For fleets with remote locations, this operation retrieves data for the fleet's home Region only. See <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationUtilization.html">DescribeFleetLocationUtilization</a> to get utilization statistics for a fleet's remote locations.</p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To get utilization data for one or more specific fleets, provide a list of fleet IDs or fleet ARNs. </p> </li> <li> <p>To get utilization data for all fleets, do not provide a fleet identifier. </p> </li> </ul> <p>When requesting multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_FleetUtilization.html">FleetUtilization</a> object is returned for each requested fleet ID, unless the fleet identifier is not found. Each fleet utilization object includes a <code>Location</code> property, which is set to the fleet's home Region. </p> <note> <p>Some API operations may limit the number of fleet IDs allowed in one request. If a request exceeds this limit, the request fails and the error message includes the maximum allowed.</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers Fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet">GameLift Metrics for Fleets</a> </p>

        Args:
            fleet_ids: <p>A unique identifier for the fleet to retrieve utilization data for. You can use either the fleet ID or ARN value. To retrieve attributes for all current fleets, do not include this parameter. </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. This parameter is ignored when the request specifies one or a list of fleet IDs.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_fleet_utilization_input.DescribeFleetUtilizationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_fleet_utilization_output.DescribeFleetUtilizationOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_fleet_utilization

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_fleet_utilization.describe_fleet_utilization(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_fleet_utilization_input.DescribeFleetUtilizationInput = {}
        if fleet_ids is not None:
            input_["fleet_ids"] = fleet_ids
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

    def iter_describe_fleet_utilization(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_ids: Optional[
            "capo_gamelift.types.fleet_id_or_arn_list.FleetIdOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.fleet_utilization.FleetUtilization]":
        _token = next_token
        while True:
            _response = self.describe_fleet_utilization(
                config_overrides=config_overrides,
                fleet_ids=fleet_ids,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fleet_utilization",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_game_server(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        game_server_id: Optional[
            "capo_gamelift.types.game_server_id.GameServerId"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_server_output.DescribeGameServerOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Retrieves information for a registered game server. Information includes game server status, health check info, and the instance that the game server is running on. </p> <p>To retrieve game server information, specify the game server ID. If successful, the requested game server object is returned. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group where the game server is running.</p>
            game_server_id: <p>A custom string that uniquely identifies the game server information to be retrieved.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_server_input.DescribeGameServerInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_server_output.DescribeGameServerOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_server

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_server.describe_game_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_server_input.DescribeGameServerInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if game_server_id is not None:
            input_["game_server_id"] = game_server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_game_server_group(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_server_group_output.DescribeGameServerGroupOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Retrieves information on a game server group. This operation returns only properties related to Amazon GameLift Servers FleetIQ. To view or update properties for the corresponding Auto Scaling group, such as launch template, auto scaling policies, and maximum/minimum group size, access the Auto Scaling group directly.</p> <p>To get attributes for a game server group, provide a group name or ARN value. If successful, a <code>GameServerGroup</code> object is returned.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group. Use either the name or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_server_group_input.DescribeGameServerGroupInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_server_group_output.DescribeGameServerGroupOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_server_group

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_server_group.describe_game_server_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_server_group_input.DescribeGameServerGroupInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_game_server_instances(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        instance_ids: Optional[
            "capo_gamelift.types.game_server_instance_ids.GameServerInstanceIds"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_server_instances_output.DescribeGameServerInstancesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Retrieves status information about the Amazon EC2 instances associated with a Amazon GameLift Servers FleetIQ game server group. Use this operation to detect when instances are active or not available to host new game servers.</p> <p>To request status for all instances in the game server group, provide a game server group ID only. To request status for specific instances, provide the game server group ID and one or more instance IDs. Use the pagination parameters to retrieve results in sequential segments. If successful, a collection of <code>GameServerInstance</code> objects is returned. </p> <p>This operation is not designed to be called with every game server claim request; this practice can cause you to exceed your API limit, which results in errors. Instead, as a best practice, cache the results and refresh your cache no more than once every 10 seconds.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group. Use either the name or ARN value.</p>
            instance_ids: <p>The Amazon EC2 instance IDs that you want to retrieve status on. Amazon EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>. To retrieve all instances in the game server group, leave this parameter empty. </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_server_instances_input.DescribeGameServerInstancesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_server_instances_output.DescribeGameServerInstancesOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_server_instances

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_server_instances.describe_game_server_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_server_instances_input.DescribeGameServerInstancesInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
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

    def iter_describe_game_server_instances(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        instance_ids: Optional[
            "capo_gamelift.types.game_server_instance_ids.GameServerInstanceIds"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_server_instance.GameServerInstance]":
        _token = next_token
        while True:
            _response = self.describe_game_server_instances(
                config_overrides=config_overrides,
                game_server_group_name=game_server_group_name,
                instance_ids=instance_ids,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_server_instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_game_session_details(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        status_filter: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_session_details_output.DescribeGameSessionDetailsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves additional game session properties, including the game session protection policy in force, for a set of one or more game sessions in a specific fleet location. You can optionally filter the results by current game session status.</p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To retrieve details for all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID, with an optional status filter. This approach returns details from the fleet's home Region and all remote locations.</p> </li> <li> <p>To retrieve details for all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name, with optional status filter. The location can be the fleet's home Region or any remote location.</p> </li> <li> <p>To retrieve details for a specific game session, provide the game session ID. This approach looks for the game session ID in all fleets that reside in the Amazon Web Services Region defined in the request.</p> </li> </ul> <p>Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>GameSessionDetail</code> object is returned for each game session that matches the request.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-find">Find a game session</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to retrieve all game sessions active on the fleet. You can use either the fleet ID or ARN value.</p>
            game_session_id: <p>An identifier for the game session that is unique across all regions to retrieve. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            alias_id: <p>A unique identifier for the alias associated with the fleet to retrieve all game sessions for. You can use either the alias ID or ARN value.</p>
            location: <p>A fleet location to get game session details for. You can specify a fleet's home Region or a remote location. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>. </p>
            status_filter: <p>Game session status to filter results on. Possible game session statuses include <code>ACTIVE</code>, <code>TERMINATED</code>, <code>ACTIVATING</code> and <code>TERMINATING</code> (the last two are transitory). </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_session_details_input.DescribeGameSessionDetailsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_session_details_output.DescribeGameSessionDetailsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_session_details

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_session_details.describe_game_session_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_session_details_input.DescribeGameSessionDetailsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if alias_id is not None:
            input_["alias_id"] = alias_id
        if location is not None:
            input_["location"] = location
        if status_filter is not None:
            input_["status_filter"] = status_filter
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

    def iter_describe_game_session_details(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        status_filter: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_session_detail.GameSessionDetail]":
        _token = next_token
        while True:
            _response = self.describe_game_session_details(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                game_session_id=game_session_id,
                alias_id=alias_id,
                location=location,
                status_filter=status_filter,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_session_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_game_session_placement(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        placement_id: Optional[
            "capo_gamelift.types.id_string_model.IdStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_session_placement_output.DescribeGameSessionPlacementOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves information, including current status, about a game session placement request. </p> <p>To get game session placement details, specify the placement ID.</p> <p>This operation is not designed to be continually called to track game session status. This practice can cause you to exceed your API limit, which results in errors. Instead, you must configure an Amazon Simple Notification Service (SNS) topic to receive notifications from FlexMatch or queues. Continuously polling with <code>DescribeGameSessionPlacement</code> should only be used for games in development with low game session usage. For a reference implementation of event-based game session placement tracking, see <a href="https://github.com/amazon-gamelift/amazon-gamelift-toolkit/tree/main/event-based-session-placement"> Event-based game session placement guidance</a> in the Amazon GameLift Toolkit.</p>

        Args:
            placement_id: <p>A unique identifier for a game session placement to retrieve.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_session_placement_input.DescribeGameSessionPlacementInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_session_placement_output.DescribeGameSessionPlacementOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_session_placement

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_session_placement.describe_game_session_placement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_session_placement_input.DescribeGameSessionPlacementInput = {}
        if placement_id is not None:
            input_["placement_id"] = placement_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_game_session_queues(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        names: Optional[
            "capo_gamelift.types.game_session_queue_name_or_arn_list.GameSessionQueueNameOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_session_queues_output.DescribeGameSessionQueuesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves the properties for one or more game session queues. When requesting multiple queues, use the pagination parameters to retrieve results as a set of sequential pages. When specifying a list of queues, objects are returned only for queues that currently exist in the Region.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-console.html"> View Your Queues</a> </p>

        Args:
            names: <p>A list of queue names to retrieve information for. You can use either the queue ID or ARN value. To request settings for all queues, leave this parameter empty. </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. You can request up to 50 results.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_session_queues_input.DescribeGameSessionQueuesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_session_queues_output.DescribeGameSessionQueuesOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_session_queues

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_session_queues.describe_game_session_queues(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_session_queues_input.DescribeGameSessionQueuesInput = {}
        if names is not None:
            input_["names"] = names
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

    def iter_describe_game_session_queues(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        names: Optional[
            "capo_gamelift.types.game_session_queue_name_or_arn_list.GameSessionQueueNameOrArnList"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_session_queue.GameSessionQueue]":
        _token = next_token
        while True:
            _response = self.describe_game_session_queues(
                config_overrides=config_overrides,
                names=names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_session_queues",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_game_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        status_filter: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_game_sessions_output.DescribeGameSessionsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves a set of one or more game sessions in a specific fleet location. You can optionally filter the results by current game session status.</p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To retrieve all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID, with an optional status filter. This approach returns all game sessions in the fleet's home Region and all remote locations.</p> </li> <li> <p>To retrieve all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name, with optional status filter. The location can be the fleet's home Region or any remote location.</p> </li> <li> <p>To retrieve a specific game session, provide the game session ID. This approach looks for the game session ID in all fleets that reside in the Amazon Web Services Region defined in the request.</p> </li> </ul> <p>Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>GameSession</code> object is returned for each game session that matches the request.</p> <p>This operation is not designed to be continually called to track game session status. This practice can cause you to exceed your API limit, which results in errors. Instead, you must configure an Amazon Simple Notification Service (SNS) topic to receive notifications from FlexMatch or queues. Continuously polling with <code>DescribeGameSessions</code> should only be used for games in development with low game session usage. </p> <p> <i>Available in Amazon GameLift Servers Local.</i> </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-find">Find a game session</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to retrieve game sessions for. You can use either the fleet ID or ARN value. </p>
            game_session_id: <p>An identifier for the game session that is unique across all regions to retrieve. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            alias_id: <p>A unique identifier for the alias associated with the fleet to retrieve game sessions for. You can use either the alias ID or ARN value.</p>
            location: <p>A fleet location to get game sessions for. You can specify a fleet's home Region or a remote location. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>. </p>
            status_filter: <p>Game session status to filter results on. You can filter on the following states: <code>ACTIVE</code>, <code>TERMINATED</code>, <code>ACTIVATING</code>, and <code>TERMINATING</code>. The last two are transitory and used for only very brief periods of time. </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_game_sessions_input.DescribeGameSessionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_game_sessions_output.DescribeGameSessionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_game_sessions

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_game_sessions.describe_game_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_game_sessions_input.DescribeGameSessionsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if alias_id is not None:
            input_["alias_id"] = alias_id
        if location is not None:
            input_["location"] = location
        if status_filter is not None:
            input_["status_filter"] = status_filter
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

    def iter_describe_game_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        status_filter: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_session.GameSession]":
        _token = next_token
        while True:
            _response = self.describe_game_sessions(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                game_session_id=game_session_id,
                alias_id=alias_id,
                location=location,
                status_filter=status_filter,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_instances(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        instance_id: Optional["capo_gamelift.types.instance_id.InstanceId"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_instances_output.DescribeInstancesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Retrieves information about the EC2 instances in an Amazon GameLift Servers managed fleet, including instance ID, connection data, and status. You can use this operation with a multi-location fleet to get location-specific instance information. As an alternative, use the operations <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute">https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute</a> and <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute">https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute</a> to retrieve information for compute resources, including EC2 and Anywhere fleets.</p> <p>You can call this operation in the following ways:</p> <ul> <li> <p>To get information on all instances in a fleet's home Region, specify the fleet ID.</p> </li> <li> <p>To get information on all instances in a fleet's remote location, specify the fleet ID and location name.</p> </li> <li> <p>To get information on a specific instance in a fleet, specify the fleet ID and instance ID.</p> </li> </ul> <p>Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, this operation returns <code>Instance</code> objects for each requested instance, listed in no particular order. If you call this operation for an Anywhere fleet, you receive an InvalidRequestException.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html">Remotely connect to fleet instances</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html">Debug fleet issues</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to retrieve instance information for. You can use either the fleet ID or ARN value.</p>
            instance_id: <p>A unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>
            location: <p>The name of a location to retrieve instance information for, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_instances_input.DescribeInstancesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_instances_output.DescribeInstancesOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_instances

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_instances.describe_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_instances_input.DescribeInstancesInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_instances(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        instance_id: Optional["capo_gamelift.types.instance_id.InstanceId"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.instance.Instance]":
        _token = next_token
        while True:
            _response = self.describe_instances(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                instance_id=instance_id,
                limit=limit,
                next_token=_token,
                location=location,
            )
            _page = _resolve_path(_response, ("instances",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_matchmaking(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        ticket_ids: Optional[
            "capo_gamelift.types.matchmaking_id_list.MatchmakingIdList"
        ] = None,
    ) -> "capo_gamelift.types.describe_matchmaking_output.DescribeMatchmakingOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves one or more matchmaking tickets. Use this operation to retrieve ticket information, including--after a successful match is made--connection information for the resulting new game session. </p> <p>To request matchmaking tickets, provide a list of up to 10 ticket IDs. If the request is successful, a ticket object is returned for each requested ID that currently exists.</p> <p>This operation is not designed to be continually called to track matchmaking ticket status. This practice can cause you to exceed your API limit, which results in errors. Instead, as a best practice, set up an Amazon Simple Notification Service to receive notifications, and provide the topic ARN in the matchmaking configuration.</p> <p></p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html"> Add FlexMatch to a game client</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html"> Set Up FlexMatch event notification</a> </p>

        Args:
            ticket_ids: <p>A unique identifier for a matchmaking ticket. You can include up to 10 ID values. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_matchmaking_input.DescribeMatchmakingInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_matchmaking_output.DescribeMatchmakingOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_matchmaking

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_matchmaking.describe_matchmaking(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_matchmaking_input.DescribeMatchmakingInput = {}
        if ticket_ids is not None:
            input_["ticket_ids"] = ticket_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_matchmaking_configurations(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        names: Optional[
            "capo_gamelift.types.matchmaking_configuration_name_list.MatchmakingConfigurationNameList"
        ] = None,
        rule_set_name: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_matchmaking_configurations_output.DescribeMatchmakingConfigurationsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves the details of FlexMatch matchmaking configurations. </p> <p>This operation offers the following options: (1) retrieve all matchmaking configurations, (2) retrieve configurations for a specified list, or (3) retrieve all configurations that use a specified rule set name. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a configuration is returned for each requested name. When specifying a list of names, only configurations that currently exist are returned. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/matchmaker-build.html"> Setting up FlexMatch matchmakers</a> </p>

        Args:
            names: <p>A unique identifier for the matchmaking configuration(s) to retrieve. You can use either the configuration name or ARN value. To request all existing configurations, leave this parameter empty.</p>
            rule_set_name: <p>A unique identifier for the matchmaking rule set. You can use either the rule set name or ARN value. Use this parameter to retrieve all matchmaking configurations that use this rule set.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. This parameter is limited to 10.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_matchmaking_configurations_input.DescribeMatchmakingConfigurationsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_matchmaking_configurations_output.DescribeMatchmakingConfigurationsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_matchmaking_configurations

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_matchmaking_configurations.describe_matchmaking_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_matchmaking_configurations_input.DescribeMatchmakingConfigurationsInput = {}
        if names is not None:
            input_["names"] = names
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name
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

    def iter_describe_matchmaking_configurations(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        names: Optional[
            "capo_gamelift.types.matchmaking_configuration_name_list.MatchmakingConfigurationNameList"
        ] = None,
        rule_set_name: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.matchmaking_configuration.MatchmakingConfiguration]":
        _token = next_token
        while True:
            _response = self.describe_matchmaking_configurations(
                config_overrides=config_overrides,
                names=names,
                rule_set_name=rule_set_name,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_matchmaking_rule_sets(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        names: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name_list.MatchmakingRuleSetNameList"
        ] = None,
        limit: Optional["capo_gamelift.types.rule_set_limit.RuleSetLimit"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_matchmaking_rule_sets_output.DescribeMatchmakingRuleSetsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves the details for FlexMatch matchmaking rule sets. You can request all existing rule sets for the Region, or provide a list of one or more rule set names. When requesting multiple items, use the pagination parameters to retrieve results as a set of sequential pages. If successful, a rule set is returned for each requested name. </p> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html">Build a rule set</a> </p> </li> </ul>

        Args:
            names: <p>A list of one or more matchmaking rule set names to retrieve details for. (Note: The rule set name is different from the optional "name" field in the rule set body.) You can use either the rule set name or ARN value. </p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_matchmaking_rule_sets_input.DescribeMatchmakingRuleSetsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_matchmaking_rule_sets_output.DescribeMatchmakingRuleSetsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_matchmaking_rule_sets

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_matchmaking_rule_sets.describe_matchmaking_rule_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_matchmaking_rule_sets_input.DescribeMatchmakingRuleSetsInput = {}
        if names is not None:
            input_["names"] = names
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

    def iter_describe_matchmaking_rule_sets(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        names: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name_list.MatchmakingRuleSetNameList"
        ] = None,
        limit: Optional["capo_gamelift.types.rule_set_limit.RuleSetLimit"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.matchmaking_rule_set.MatchmakingRuleSet]":
        _token = next_token
        while True:
            _response = self.describe_matchmaking_rule_sets(
                config_overrides=config_overrides,
                names=names,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rule_sets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_player_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        player_id: Optional["capo_gamelift.types.player_id.PlayerId"] = None,
        player_session_id: Optional[
            "capo_gamelift.types.player_session_id.PlayerSessionId"
        ] = None,
        player_session_status_filter: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.describe_player_sessions_output.DescribePlayerSessionsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves properties for one or more player sessions. </p> <p>This action can be used in the following ways: </p> <ul> <li> <p>To retrieve a specific player session, provide the player session ID only.</p> </li> <li> <p>To retrieve all player sessions in a game session, provide the game session ID only.</p> </li> <li> <p>To retrieve all player sessions for a specific player, provide a player ID only.</p> </li> </ul> <p>To request player sessions, specify either a player session ID, game session ID, or player ID. You can filter this request by player session status. If you provide a specific <code>PlayerSessionId</code> or <code>PlayerId</code>, Amazon GameLift Servers ignores the filter criteria. Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>PlayerSession</code> object is returned for each session that matches the request.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions to retrieve player sessions for. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            player_id: <p>A unique identifier for a player to retrieve player sessions for.</p>
            player_session_id: <p>A unique identifier for a player session to retrieve.</p>
            player_session_status_filter: <p>Player session status to filter results on. Note that when a PlayerSessionId or PlayerId is provided in a DescribePlayerSessions request, then the PlayerSessionStatusFilter has no effect on the response.</p> <p>Possible player session statuses include the following:</p> <ul> <li> <p> <b>RESERVED</b> -- The player session request has been received, but the player has not yet connected to the server process and/or been validated. </p> </li> <li> <p> <b>ACTIVE</b> -- The player has been validated by the server process and is currently connected.</p> </li> <li> <p> <b>COMPLETED</b> -- The player connection has been dropped.</p> </li> <li> <p> <b>TIMEDOUT</b> -- A player session request was received, but the player did not connect and/or was not validated within the timeout limit (60 seconds).</p> </li> </ul>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. If a player session ID is specified, this parameter is ignored.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value. If a player session ID is specified, this parameter is ignored.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_player_sessions_input.DescribePlayerSessionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_player_sessions_output.DescribePlayerSessionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_player_sessions

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_player_sessions.describe_player_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_player_sessions_input.DescribePlayerSessionsInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if player_id is not None:
            input_["player_id"] = player_id
        if player_session_id is not None:
            input_["player_session_id"] = player_session_id
        if player_session_status_filter is not None:
            input_["player_session_status_filter"] = player_session_status_filter
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

    def iter_describe_player_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        player_id: Optional["capo_gamelift.types.player_id.PlayerId"] = None,
        player_session_id: Optional[
            "capo_gamelift.types.player_session_id.PlayerSessionId"
        ] = None,
        player_session_status_filter: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.player_session.PlayerSession]":
        _token = next_token
        while True:
            _response = self.describe_player_sessions(
                config_overrides=config_overrides,
                game_session_id=game_session_id,
                player_id=player_id,
                player_session_id=player_session_id,
                player_session_status_filter=player_session_status_filter,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("player_sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_runtime_configuration(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
    ) -> "capo_gamelift.types.describe_runtime_configuration_output.DescribeRuntimeConfigurationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves a fleet's runtime configuration settings. The runtime configuration determines which server processes run, and how, on computes in the fleet. For managed EC2 fleets, the runtime configuration describes server processes that run on each fleet instance. You can update a fleet's runtime configuration at any time using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateRuntimeConfiguration.html">UpdateRuntimeConfiguration</a>.</p> <p>To get the current runtime configuration for a fleet, provide the fleet ID. </p> <p>If successful, a <code>RuntimeConfiguration</code> object is returned for the requested fleet. If the requested fleet has been deleted, the result set is empty.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html">Running multiple processes on a fleet</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to get the runtime configuration for. You can use either the fleet ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_runtime_configuration_input.DescribeRuntimeConfigurationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_runtime_configuration_output.DescribeRuntimeConfigurationOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_runtime_configuration

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_runtime_configuration.describe_runtime_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_runtime_configuration_input.DescribeRuntimeConfigurationInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scaling_policies(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        status_filter: Optional[
            "capo_gamelift.types.scaling_status_type.ScalingStatusType"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.describe_scaling_policies_output.DescribeScalingPoliciesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Retrieves all scaling policies applied to a fleet.</p> <p>To get a fleet's scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of <code>ScalingPolicy</code> objects is returned for the fleet.</p> <p>A fleet may have all of its scaling policies suspended. This operation does not affect the status of the scaling policies, which remains ACTIVE.</p>

        Args:
            fleet_id: <p>A unique identifier for the fleet for which to retrieve scaling policies. You can use either the fleet ID or ARN value.</p>
            status_filter: <p>Scaling policy status to filter results on. A scaling policy is only in force when in an <code>ACTIVE</code> status.</p> <ul> <li> <p> <b>ACTIVE</b> -- The scaling policy is currently in force.</p> </li> <li> <p> <b>UPDATEREQUESTED</b> -- A request to update the scaling policy has been received.</p> </li> <li> <p> <b>UPDATING</b> -- A change is being made to the scaling policy.</p> </li> <li> <p> <b>DELETEREQUESTED</b> -- A request to delete the scaling policy has been received.</p> </li> <li> <p> <b>DELETING</b> -- The scaling policy is being deleted.</p> </li> <li> <p> <b>DELETED</b> -- The scaling policy has been deleted.</p> </li> <li> <p> <b>ERROR</b> -- An error occurred in creating the policy. It should be removed and recreated.</p> </li> </ul>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>
            location: <p> The fleet location. If you don't specify this value, the response contains the scaling policies of every location in the fleet. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_scaling_policies_input.DescribeScalingPoliciesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_scaling_policies_output.DescribeScalingPoliciesOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_scaling_policies

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_scaling_policies.describe_scaling_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_scaling_policies_input.DescribeScalingPoliciesInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if status_filter is not None:
            input_["status_filter"] = status_filter
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_scaling_policies(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        status_filter: Optional[
            "capo_gamelift.types.scaling_status_type.ScalingStatusType"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.scaling_policy.ScalingPolicy]":
        _token = next_token
        while True:
            _response = self.describe_scaling_policies(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                status_filter=status_filter,
                limit=limit,
                next_token=_token,
                location=location,
            )
            _page = _resolve_path(_response, ("scaling_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_script(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        script_id: Optional[
            "capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"
        ] = None,
    ) -> "capo_gamelift.types.describe_script_output.DescribeScriptOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves properties for a Realtime script. </p> <p>To request a script record, specify the script ID. If successful, an object containing the script properties is returned.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html">Amazon GameLift Servers Amazon GameLift Servers Realtime</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            script_id: <p>A unique identifier for the Realtime script to retrieve properties for. You can use either the script ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_script_input.DescribeScriptInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_script_output.DescribeScriptOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_script

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_script.describe_script(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_script_input.DescribeScriptInput = {}
        if script_id is not None:
            input_["script_id"] = script_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vpc_peering_authorizations(
        self, *, config_overrides: Optional[GameLiftClientConfig] = None
    ) -> "capo_gamelift.types.describe_vpc_peering_authorizations_output.DescribeVpcPeeringAuthorizationsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves valid VPC peering authorizations that are pending for the Amazon Web Services account. This operation returns all VPC peering authorizations and requests for peering. This includes those initiated and received by this account. </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_vpc_peering_authorizations_input.DescribeVpcPeeringAuthorizationsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_vpc_peering_authorizations_output.DescribeVpcPeeringAuthorizationsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_vpc_peering_authorizations

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_vpc_peering_authorizations.describe_vpc_peering_authorizations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_vpc_peering_authorizations_input.DescribeVpcPeeringAuthorizationsInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vpc_peering_connections(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id.FleetId"] = None,
    ) -> "capo_gamelift.types.describe_vpc_peering_connections_output.DescribeVpcPeeringConnectionsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves information on VPC peering connections. Use this operation to get peering information for all fleets or for one specific fleet ID. </p> <p>To retrieve connection information, call this operation from the Amazon Web Services account that is used to manage the Amazon GameLift Servers fleets. Specify a fleet ID or leave the parameter empty to retrieve all connection records. If successful, the retrieved information includes both active and pending connections. Active connections identify the IpV4 CIDR block that the VPC uses to connect. </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet. You can use either the fleet ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.describe_vpc_peering_connections_input.DescribeVpcPeeringConnectionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.describe_vpc_peering_connections_output.DescribeVpcPeeringConnectionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.describe_vpc_peering_connections

            output, http_response = (
                capo_gamelift._operations.game_lift.describe_vpc_peering_connections.describe_vpc_peering_connections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.describe_vpc_peering_connections_input.DescribeVpcPeeringConnectionsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compute_access(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        compute_name: Optional[
            "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
        ] = None,
    ) -> "capo_gamelift.types.get_compute_access_output.GetComputeAccessOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Requests authorization to remotely connect to a hosting resource in a Amazon GameLift Servers managed fleet. This operation is not used with Amazon GameLift Servers Anywhere fleets.</p> <p> <b>Request options</b> </p> <p>Provide the fleet ID and compute name. The compute name varies depending on the type of fleet.</p> <ul> <li> <p>For a compute in a managed EC2 fleet, provide an instance ID. Each instance in the fleet is a compute.</p> </li> <li> <p>For a compute in a managed container fleet, provide a compute name. In a container fleet, each game server container group on a fleet instance is assigned a compute name. </p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation returns a set of temporary Amazon Web Services credentials, including a two-part access key and a session token.</p> <ul> <li> <p>With a managed EC2 fleet (where compute type is <code>EC2</code>), use these credentials with Amazon EC2 Systems Manager (SSM) to start a session with the compute. For more details, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#sessions-start-cli"> Starting a session (CLI)</a> in the <i>Amazon EC2 Systems Manager User Guide</i>.</p> </li> </ul>

        Args:
            fleet_id: <p>A unique identifier for the fleet that holds the compute resource that you want to connect to. You can use either the fleet ID or ARN value.</p>
            compute_name: <p>A unique identifier for the compute resource that you want to connect to. For an EC2 fleet, use an instance ID. For a managed container fleet, use a compute name. You can retrieve a fleet's compute names by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute.html">ListCompute</a>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.get_compute_access_input.GetComputeAccessInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.get_compute_access_output.GetComputeAccessOutput"
        ]:
            import capo_gamelift._operations.game_lift.get_compute_access

            output, http_response = (
                capo_gamelift._operations.game_lift.get_compute_access.get_compute_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.get_compute_access_input.GetComputeAccessInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if compute_name is not None:
            input_["compute_name"] = compute_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_compute_auth_token(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        compute_name: Optional[
            "capo_gamelift.types.compute_name_or_arn.ComputeNameOrArn"
        ] = None,
    ) -> "capo_gamelift.types.get_compute_auth_token_output.GetComputeAuthTokenOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Requests an authentication token from Amazon GameLift Servers for a compute resource in an Amazon GameLift Servers fleet. Game servers that are running on the compute use this token to communicate with the Amazon GameLift Servers service, such as when calling the Amazon GameLift Servers server SDK action <code>InitSDK()</code>. Authentication tokens are valid for a limited time span, so you need to request a fresh token before the current token expires.</p> <p> <b>Request options</b> </p> <ul> <li> <p>For managed EC2 fleets (compute type <code>EC2</code>), auth token retrieval and refresh is handled automatically. All game servers that are running on all fleet instances have access to a valid auth token.</p> </li> <li> <p>For Anywhere fleets (compute type <code>ANYWHERE</code>), if you're using the Amazon GameLift Servers Agent, auth token retrieval and refresh is handled automatically for any compute where the Agent is running. If you're not using the Agent, create a mechanism to retrieve and refresh auth tokens for computes that are running game server processes.</p> </li> </ul> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html">Create an Anywhere fleet</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-testing.html">Test your integration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html">Server SDK reference guides</a> (for version 5.x)</p> </li> </ul>

        Args:
            fleet_id: <p>A unique identifier for the fleet that the compute is registered to.</p>
            compute_name: <p>The name of the compute resource you are requesting the authentication token for. For an Anywhere fleet compute, use the registered compute name. For an EC2 fleet instance, use the instance ID.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.get_compute_auth_token_input.GetComputeAuthTokenInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.get_compute_auth_token_output.GetComputeAuthTokenOutput"
        ]:
            import capo_gamelift._operations.game_lift.get_compute_auth_token

            output, http_response = (
                capo_gamelift._operations.game_lift.get_compute_auth_token.get_compute_auth_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.get_compute_auth_token_input.GetComputeAuthTokenInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if compute_name is not None:
            input_["compute_name"] = compute_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_game_session_log_url(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
    ) -> (
        "capo_gamelift.types.get_game_session_log_url_output.GetGameSessionLogUrlOutput"
    ):
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves the location of stored game session logs for a specified game session on Amazon GameLift Servers managed fleets. When a game session is terminated, Amazon GameLift Servers automatically stores the logs in Amazon S3 and retains them for 14 days. Use this URL to download the logs.</p> <note> <p>See the <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_gamelift">Amazon Web Services Service Limits</a> page for maximum log file sizes. Log files that exceed this limit are not saved.</p> </note> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions to get logs for. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.get_game_session_log_url_input.GetGameSessionLogUrlInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.get_game_session_log_url_output.GetGameSessionLogUrlOutput"
        ]:
            import capo_gamelift._operations.game_lift.get_game_session_log_url

            output, http_response = (
                capo_gamelift._operations.game_lift.get_game_session_log_url.get_game_session_log_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.get_game_session_log_url_input.GetGameSessionLogUrlInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_instance_access(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        instance_id: Optional["capo_gamelift.types.instance_id.InstanceId"] = None,
    ) -> "capo_gamelift.types.get_instance_access_output.GetInstanceAccessOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Requests authorization to remotely connect to an instance in an Amazon GameLift Servers managed fleet. Use this operation to connect to instances with game servers that use Amazon GameLift Servers server SDK 4.x or earlier. To connect to instances with game servers that use server SDK 5.x or later, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess">https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess</a>.</p> <p>To request access to an instance, specify IDs for the instance and the fleet it belongs to. You can retrieve instance IDs for a fleet by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeInstances.html">DescribeInstances</a> with the fleet ID. </p> <p>If successful, this operation returns an IP address and credentials. The returned credentials match the operating system of the instance, as follows: </p> <ul> <li> <p>For a Windows instance: returns a user name and secret (password) for use with a Windows Remote Desktop client. </p> </li> <li> <p>For a Linux instance: returns a user name and secret (RSA private key) for use with an SSH client. You must save the secret to a <code>.pem</code> file. If you're using the CLI, see the example <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess.html#API_GetInstanceAccess_Examples"> Get credentials for a Linux instance</a> for tips on automatically saving the secret to a <code>.pem</code> file. </p> </li> </ul> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html">Remotely connect to fleet instances</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html">Debug fleet issues</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet that contains the instance you want to access. You can request access to instances in EC2 fleets with the following statuses: <code>ACTIVATING</code>, <code>ACTIVE</code>, or <code>ERROR</code>. Use either a fleet ID or an ARN value. </p> <note> <p>You can access fleets in <code>ERROR</code> status for a short period of time before Amazon GameLift Servers deletes them.</p> </note>
            instance_id: <p>A unique identifier for the instance you want to access. You can access an instance in any status.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.get_instance_access_input.GetInstanceAccessInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.get_instance_access_output.GetInstanceAccessOutput"
        ]:
            import capo_gamelift._operations.game_lift.get_instance_access

            output, http_response = (
                capo_gamelift._operations.game_lift.get_instance_access.get_instance_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.get_instance_access_input.GetInstanceAccessInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if instance_id is not None:
            input_["instance_id"] = instance_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_player_connection_details(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        player_ids: Optional["capo_gamelift.types.player_id_list.PlayerIdList"] = None,
    ) -> "capo_gamelift.types.get_player_connection_details_output.GetPlayerConnectionDetailsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (server SDK 5.x or later), Container</p> <p>Retrieves connection details for game clients to connect to game sessions. </p> <p> <b>Player gateway benefits:</b> DDoS protection with negligible impact to latency. </p> <p>To enable player gateway on your fleet, set <code>PlayerGatewayMode</code> to <code>ENABLED</code> or <code>REQUIRED</code> when calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateFleet.html">CreateFleet</a> or <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerFleet.html">CreateContainerFleet</a>.</p> <p> <b>How to use:</b> After creating a game session and adding players, call this operation with the game session ID and player IDs. When player gateway is enabled, the response includes connection endpoints and player gateway tokens that your game clients can use to connect to the game session through player gateway. To learn more about player gateway integration, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/ddos-protection-intro.html">DDoS protection with Amazon GameLift Servers player gateway</a>.</p> <p>When player gateway is disabled or in locations where player gateway is not supported, this operation returns game server connection information without player gateway tokens, so that your game clients directly connect to the game server endpoint.</p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions for which to retrieve player connection details. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            player_ids: <p>List of unique identifiers for players. Connection details are returned for each player in this list.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_game_session_status_exception.InvalidGameSessionStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.get_player_connection_details_input.GetPlayerConnectionDetailsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.get_player_connection_details_output.GetPlayerConnectionDetailsOutput"
        ]:
            import capo_gamelift._operations.game_lift.get_player_connection_details

            output, http_response = (
                capo_gamelift._operations.game_lift.get_player_connection_details.get_player_connection_details(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.get_player_connection_details_input.GetPlayerConnectionDetailsInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if player_ids is not None:
            input_["player_ids"] = player_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_aliases(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        routing_strategy_type: Optional[
            "capo_gamelift.types.routing_strategy_type.RoutingStrategyType"
        ] = None,
        name: Optional["capo_gamelift.types.non_empty_string.NonEmptyString"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_gamelift.types.list_aliases_output.ListAliasesOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves all aliases for this Amazon Web Services account. You can filter the result set by alias name and/or routing strategy type. Use the pagination parameters to retrieve results in sequential pages.</p> <note> <p>Returned aliases are not listed in any particular order.</p> </note> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            routing_strategy_type: <p>The routing type to filter results on. Use this parameter to retrieve only aliases with a certain routing type. To retrieve all aliases, leave this parameter empty.</p> <p>Possible routing types include the following:</p> <ul> <li> <p> <b>SIMPLE</b> -- The alias resolves to one specific fleet. Use this type when routing to active fleets.</p> </li> <li> <p> <b>TERMINAL</b> -- The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_RoutingStrategy.html">RoutingStrategy</a> message embedded.</p> </li> </ul>
            name: <p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_aliases_input.ListAliasesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_aliases_output.ListAliasesOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_aliases

            output, http_response = (
                capo_gamelift._operations.game_lift.list_aliases.list_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_aliases_input.ListAliasesInput = {}
        if routing_strategy_type is not None:
            input_["routing_strategy_type"] = routing_strategy_type
        if name is not None:
            input_["name"] = name
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

    def iter_list_aliases(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        routing_strategy_type: Optional[
            "capo_gamelift.types.routing_strategy_type.RoutingStrategyType"
        ] = None,
        name: Optional["capo_gamelift.types.non_empty_string.NonEmptyString"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.alias.Alias]":
        _token = next_token
        while True:
            _response = self.list_aliases(
                config_overrides=config_overrides,
                routing_strategy_type=routing_strategy_type,
                name=name,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("aliases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_builds(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        status: Optional["capo_gamelift.types.build_status.BuildStatus"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_gamelift.types.list_builds_output.ListBuildsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves build resources for all builds associated with the Amazon Web Services account in use. You can limit results to builds that are in a specific status by using the <code>Status</code> parameter. Use the pagination parameters to retrieve results in </p> <note> <p>Build resources are not listed in any particular order.</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html"> Upload a Custom Server Build</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            status: <p>Build status to filter results by. To retrieve all builds, leave this parameter empty.</p> <p>Possible build statuses include the following:</p> <ul> <li> <p> <b>INITIALIZED</b> -- A new build has been defined, but no files have been uploaded. You cannot create fleets for builds that are in this status. When a build is successfully created, the build status is set to this value. </p> </li> <li> <p> <b>READY</b> -- The game build has been successfully uploaded. You can now create new fleets for this build.</p> </li> <li> <p> <b>FAILED</b> -- The game build upload failed. You cannot create new fleets for this build. </p> </li> </ul>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_builds_input.ListBuildsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_builds_output.ListBuildsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_builds

            output, http_response = (
                capo_gamelift._operations.game_lift.list_builds.list_builds(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_builds_input.ListBuildsInput = {}
        if status is not None:
            input_["status"] = status
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

    def iter_list_builds(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        status: Optional["capo_gamelift.types.build_status.BuildStatus"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.build.Build]":
        _token = next_token
        while True:
            _response = self.list_builds(
                config_overrides=config_overrides,
                status=status,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("builds",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_compute(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        compute_status: Optional[
            "capo_gamelift.types.list_compute_input_status.ListComputeInputStatus"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_compute_output.ListComputeOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves information on the compute resources in an Amazon GameLift Servers fleet. Use the pagination parameters to retrieve results in a set of sequential pages.</p> <p> <b>Request options</b> </p> <ul> <li> <p>Retrieve a list of all computes in a fleet. Specify a fleet ID. </p> </li> <li> <p>Retrieve a list of all computes in a specific fleet location. Specify a fleet ID and location.</p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation returns information on a set of computes. Depending on the type of fleet, the result includes the following information: </p> <ul> <li> <p>For a managed EC2 fleet (compute type <code>EC2</code>), this operation returns information about the EC2 instance. Compute names are EC2 instance IDs.</p> </li> <li> <p>For an Anywhere fleet (compute type <code>ANYWHERE</code>), this operation returns compute names and details from when the compute was registered with <code>RegisterCompute</code>. This includes <code>GameLiftServiceSdkEndpoint</code> or <code>GameLiftAgentEndpoint</code>.</p> </li> </ul>

        Args:
            fleet_id: <p>A unique identifier for the fleet to retrieve compute resources for.</p>
            location: <p>The name of a location to retrieve compute resources for. For an Amazon GameLift Servers Anywhere fleet, use a custom location. For a managed fleet, provide a Amazon Web Services Region or Local Zone code (for example: <code>us-west-2</code> or <code>us-west-2-lax-1</code>).</p>
            container_group_definition_name: <p>For computes in a managed container fleet, the name of the deployed container group definition. </p>
            compute_status: <p>The status of computes in a managed container fleet, based on the success of the latest update deployment.</p> <ul> <li> <p> <code>ACTIVE</code> -- The compute is deployed with the correct container definitions. It is ready to process game servers and host game sessions.</p> </li> <li> <p> <code>IMPAIRED</code> -- An update deployment to the compute failed, and the compute is deployed with incorrect container definitions.</p> </li> </ul>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_compute_input.ListComputeInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_compute_output.ListComputeOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_compute

            output, http_response = (
                capo_gamelift._operations.game_lift.list_compute.list_compute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_compute_input.ListComputeInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if location is not None:
            input_["location"] = location
        if container_group_definition_name is not None:
            input_["container_group_definition_name"] = container_group_definition_name
        if compute_status is not None:
            input_["compute_status"] = compute_status
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

    def iter_list_compute(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        compute_status: Optional[
            "capo_gamelift.types.list_compute_input_status.ListComputeInputStatus"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.compute.Compute]":
        _token = next_token
        while True:
            _response = self.list_compute(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                location=location,
                container_group_definition_name=container_group_definition_name,
                compute_status=compute_status,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("compute_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_container_fleets(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_container_fleets_output.ListContainerFleetsOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves a collection of container fleet resources in an Amazon Web Services Region. For fleets that have multiple locations, this operation retrieves fleets based on their home Region only.</p> <p> <b>Request options</b> </p> <ul> <li> <p>Get a list of all fleets. Call this operation without specifying a container group definition. </p> </li> <li> <p>Get a list of fleets filtered by container group definition. Provide the container group definition name or ARN value.</p> </li> <li> <p>To get a list of all Amazon GameLift Servers Realtime fleets with a specific configuration script, provide the script ID. </p> </li> </ul> <p>Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, this operation returns a collection of container fleets that match the request parameters. A NextToken value is also returned if there are more result pages to retrieve.</p> <note> <p>Fleet IDs are returned in no particular order.</p> </note>

        Args:
            container_group_definition_name: <p>The container group definition to filter the list on. Use this parameter to retrieve only those fleets that use the specified container group definition. You can specify the container group definition's name to get fleets with the latest versions. Alternatively, provide an ARN value to get fleets with a specific version number.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_container_fleets_input.ListContainerFleetsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_container_fleets_output.ListContainerFleetsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_container_fleets

            output, http_response = (
                capo_gamelift._operations.game_lift.list_container_fleets.list_container_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_container_fleets_input.ListContainerFleetsInput = {}
        if container_group_definition_name is not None:
            input_["container_group_definition_name"] = container_group_definition_name
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

    def iter_list_container_fleets(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.container_fleet.ContainerFleet]":
        _token = next_token
        while True:
            _response = self.list_container_fleets(
                config_overrides=config_overrides,
                container_group_definition_name=container_group_definition_name,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("container_fleets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_container_group_definitions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        container_group_type: Optional[
            "capo_gamelift.types.container_group_type.ContainerGroupType"
        ] = None,
        limit: Optional[
            "capo_gamelift.types.list_container_group_definitions_limit.ListContainerGroupDefinitionsLimit"
        ] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_container_group_definitions_output.ListContainerGroupDefinitionsOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves container group definitions for the Amazon Web Services account and Amazon Web Services Region. Use the pagination parameters to retrieve results in a set of sequential pages.</p> <p>This operation returns only the latest version of each definition. To retrieve all versions of a container group definition, use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListContainerGroupDefinitionVersions.html">ListContainerGroupDefinitionVersions</a>.</p> <p> <b>Request options:</b> </p> <ul> <li> <p>Retrieve the most recent versions of all container group definitions. </p> </li> <li> <p>Retrieve the most recent versions of all container group definitions, filtered by type. Specify the container group type to filter on. </p> </li> </ul> <p> <b>Results:</b> </p> <p>If successful, this operation returns the complete properties of a set of container group definition versions that match the request.</p> <note> <p>This operation returns the list of container group definitions in no particular order. </p> </note>

        Args:
            container_group_type: <p>The type of container group to retrieve. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_container_group_definitions_input.ListContainerGroupDefinitionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_container_group_definitions_output.ListContainerGroupDefinitionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_container_group_definitions

            output, http_response = (
                capo_gamelift._operations.game_lift.list_container_group_definitions.list_container_group_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_container_group_definitions_input.ListContainerGroupDefinitionsInput = {}
        if container_group_type is not None:
            input_["container_group_type"] = container_group_type
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

    def iter_list_container_group_definitions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        container_group_type: Optional[
            "capo_gamelift.types.container_group_type.ContainerGroupType"
        ] = None,
        limit: Optional[
            "capo_gamelift.types.list_container_group_definitions_limit.ListContainerGroupDefinitionsLimit"
        ] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.container_group_definition.ContainerGroupDefinition]":
        _token = next_token
        while True:
            _response = self.list_container_group_definitions(
                config_overrides=config_overrides,
                container_group_type=container_group_type,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("container_group_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_container_group_definition_versions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        limit: Optional[
            "capo_gamelift.types.list_container_group_definition_versions_limit.ListContainerGroupDefinitionVersionsLimit"
        ] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_container_group_definition_versions_output.ListContainerGroupDefinitionVersionsOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves all versions of a container group definition. Use the pagination parameters to retrieve results in a set of sequential pages.</p> <p> <b>Request options:</b> </p> <ul> <li> <p>Get all versions of a specified container group definition. Specify the container group definition name or ARN value. (If the ARN value has a version number, it's ignored.)</p> </li> </ul> <p> <b>Results:</b> </p> <p>If successful, this operation returns the complete properties of a set of container group definition versions that match the request.</p> <note> <p>This operation returns the list of container group definitions in descending version order (latest first). </p> </note> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html">Manage a container group definition</a> </p> </li> </ul>

        Args:
            name: <p>The unique identifier for the container group definition to retrieve properties for. You can use either the <code>Name</code> or <code>ARN</code> value.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_container_group_definition_versions_input.ListContainerGroupDefinitionVersionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_container_group_definition_versions_output.ListContainerGroupDefinitionVersionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_container_group_definition_versions

            output, http_response = (
                capo_gamelift._operations.game_lift.list_container_group_definition_versions.list_container_group_definition_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_container_group_definition_versions_input.ListContainerGroupDefinitionVersionsInput = {}
        if name is not None:
            input_["name"] = name
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

    def iter_list_container_group_definition_versions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        limit: Optional[
            "capo_gamelift.types.list_container_group_definition_versions_limit.ListContainerGroupDefinitionVersionsLimit"
        ] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.container_group_definition.ContainerGroupDefinition]":
        _token = next_token
        while True:
            _response = self.list_container_group_definition_versions(
                config_overrides=config_overrides,
                name=name,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("container_group_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_fleet_deployments(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_fleet_deployments_output.ListFleetDeploymentsOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Retrieves a collection of container fleet deployments in an Amazon Web Services Region. Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p> <b>Request options</b> </p> <ul> <li> <p>Get a list of all deployments. Call this operation without specifying a fleet ID. </p> </li> <li> <p>Get a list of all deployments for a fleet. Specify the container fleet ID or ARN value.</p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation returns a list of deployments that match the request parameters. A NextToken value is also returned if there are more result pages to retrieve.</p> <note> <p>Deployments are returned starting with the latest.</p> </note>

        Args:
            fleet_id: <p>A unique identifier for the container fleet. You can use either the fleet ID or ARN value.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_fleet_deployments_input.ListFleetDeploymentsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_fleet_deployments_output.ListFleetDeploymentsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_fleet_deployments

            output, http_response = (
                capo_gamelift._operations.game_lift.list_fleet_deployments.list_fleet_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_fleet_deployments_input.ListFleetDeploymentsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
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

    def iter_list_fleet_deployments(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.fleet_deployment.FleetDeployment]":
        _token = next_token
        while True:
            _response = self.list_fleet_deployments(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fleet_deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_fleets(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
        script_id: Optional[
            "capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_fleets_output.ListFleetsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves a collection of fleet resources in an Amazon Web Services Region. You can filter the result set to find only those fleets that are deployed with a specific build or script. For fleets that have multiple locations, this operation retrieves fleets based on their home Region only.</p> <p>You can use this operation in the following ways: </p> <ul> <li> <p>To get a list of all fleets in a Region, don't provide a build or script identifier.</p> </li> <li> <p>To get a list of all fleets where a specific game build is deployed, provide the build ID.</p> </li> <li> <p>To get a list of all Amazon GameLift Servers Realtime fleets with a specific configuration script, provide the script ID. </p> </li> </ul> <p>Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, this operation returns a list of fleet IDs that match the request parameters. A NextToken value is also returned if there are more result pages to retrieve.</p> <note> <p>Fleet IDs are returned in no particular order.</p> </note>

        Args:
            build_id: <p>A unique identifier for the build to request fleets for. Use this parameter to return only fleets using a specified build. Use either the build ID or ARN value.</p>
            script_id: <p>A unique identifier for the Realtime script to request fleets for. Use this parameter to return only fleets using a specified script. Use either the script ID or ARN value.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_fleets_input.ListFleetsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_fleets_output.ListFleetsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_fleets

            output, http_response = (
                capo_gamelift._operations.game_lift.list_fleets.list_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_fleets_input.ListFleetsInput = {}
        if build_id is not None:
            input_["build_id"] = build_id
        if script_id is not None:
            input_["script_id"] = script_id
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

    def iter_list_fleets(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
        script_id: Optional[
            "capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.fleet_id.FleetId]":
        _token = next_token
        while True:
            _response = self.list_fleets(
                config_overrides=config_overrides,
                build_id=build_id,
                script_id=script_id,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("fleet_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_game_server_groups(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> (
        "capo_gamelift.types.list_game_server_groups_output.ListGameServerGroupsOutput"
    ):
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Lists game server groups.</p>

        Args:
            limit: <p>The game server groups' limit.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_game_server_groups_input.ListGameServerGroupsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_game_server_groups_output.ListGameServerGroupsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_game_server_groups

            output, http_response = (
                capo_gamelift._operations.game_lift.list_game_server_groups.list_game_server_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_game_server_groups_input.ListGameServerGroupsInput = {}
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

    def iter_list_game_server_groups(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_server_group.GameServerGroup]":
        _token = next_token
        while True:
            _response = self.list_game_server_groups(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_server_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_game_servers(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        sort_order: Optional["capo_gamelift.types.sort_order.SortOrder"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_game_servers_output.ListGameServersOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Retrieves information on all game servers that are currently active in a specified game server group. You can opt to sort the list by game server age. Use the pagination parameters to retrieve results in a set of sequential segments. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>An identifier for the game server group to retrieve a list of game servers from. Use either the name or ARN value.</p>
            sort_order: <p>Indicates how to sort the returned data based on game server registration timestamp. Use <code>ASCENDING</code> to retrieve oldest game servers first, or use <code>DESCENDING</code> to retrieve newest game servers first. If this parameter is left empty, game servers are returned in no particular order.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_game_servers_input.ListGameServersInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_game_servers_output.ListGameServersOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_game_servers

            output, http_response = (
                capo_gamelift._operations.game_lift.list_game_servers.list_game_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_game_servers_input.ListGameServersInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_game_servers(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        sort_order: Optional["capo_gamelift.types.sort_order.SortOrder"] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_server.GameServer]":
        _token = next_token
        while True:
            _response = self.list_game_servers(
                config_overrides=config_overrides,
                game_server_group_name=game_server_group_name,
                sort_order=sort_order,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_servers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_locations(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        filters: Optional[
            "capo_gamelift.types.location_filter_list.LocationFilterList"
        ] = None,
        limit: Optional[
            "capo_gamelift.types.list_locations_limit.ListLocationsLimit"
        ] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.list_locations_output.ListLocationsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Lists all custom and Amazon Web Services locations where Amazon GameLift Servers can host game servers. This operation also returns UDP ping beacon information for locations, which you can use to measure network latency between player devices and potential hosting locations.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html">Service locations</a> </p>

        Args:
            filters: <p>Filters the list for <code>AWS</code> or <code>CUSTOM</code> locations. Use this parameter to narrow down results to only Amazon Web Services-managed locations (Amazon EC2 or container) or only your custom locations (such as an Amazon GameLift Servers Anywhere fleet).</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_locations_input.ListLocationsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_locations_output.ListLocationsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_locations

            output, http_response = (
                capo_gamelift._operations.game_lift.list_locations.list_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_locations_input.ListLocationsInput = {}
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

    def iter_list_locations(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        filters: Optional[
            "capo_gamelift.types.location_filter_list.LocationFilterList"
        ] = None,
        limit: Optional[
            "capo_gamelift.types.list_locations_limit.ListLocationsLimit"
        ] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.location_model.LocationModel]":
        _token = next_token
        while True:
            _response = self.list_locations(
                config_overrides=config_overrides,
                filters=filters,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("locations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scripts(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_gamelift.types.list_scripts_output.ListScriptsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves script records for all Realtime scripts that are associated with the Amazon Web Services account in use. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html">Amazon GameLift Servers Amazon GameLift Servers Realtime</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_scripts_input.ListScriptsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_scripts_output.ListScriptsOutput"
        ]:
            import capo_gamelift._operations.game_lift.list_scripts

            output, http_response = (
                capo_gamelift._operations.game_lift.list_scripts.list_scripts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_scripts_input.ListScriptsInput = {}
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

    def iter_list_scripts(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.script.Script]":
        _token = next_token
        while True:
            _response = self.list_scripts(
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scripts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        resource_arn: Optional[
            "capo_gamelift.types.amazon_resource_name.AmazonResourceName"
        ] = None,
    ) -> "capo_gamelift.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves all tags assigned to a Amazon GameLift Servers resource. Use resource tags to organize Amazon Web Services resources for a range of purposes. This operation handles the permissions necessary to manage tags for Amazon GameLift Servers resources that support tagging.</p> <p>To list tags for a resource, specify the unique ARN value for the resource.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i> </p> <p> <a href="http://aws.amazon.com/answers/account-management/aws-tagging-strategies/"> Amazon Web Services Tagging Strategies</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that uniquely identifies the Amazon GameLift Servers resource that you want to retrieve tags for. Amazon GameLift Servers includes resource ARNs in the data object for the resource. You can retrieve the ARN by calling a <code>List</code> or <code>Describe</code> operation for the resource type. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_gamelift.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_gamelift._operations.game_lift.list_tags_for_resource

            output, http_response = (
                capo_gamelift._operations.game_lift.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.list_tags_for_resource_request.ListTagsForResourceRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_scaling_policy(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        scaling_adjustment: Optional["capo_gamelift.types.integer.Integer"] = None,
        scaling_adjustment_type: Optional[
            "capo_gamelift.types.scaling_adjustment_type.ScalingAdjustmentType"
        ] = None,
        threshold: Optional["capo_gamelift.types.double.Double"] = None,
        comparison_operator: Optional[
            "capo_gamelift.types.comparison_operator_type.ComparisonOperatorType"
        ] = None,
        evaluation_periods: Optional[
            "capo_gamelift.types.positive_integer.PositiveInteger"
        ] = None,
        metric_name: Optional["capo_gamelift.types.metric_name.MetricName"] = None,
        policy_type: Optional["capo_gamelift.types.policy_type.PolicyType"] = None,
        target_configuration: Optional[
            "capo_gamelift.types.target_configuration.TargetConfiguration"
        ] = None,
    ) -> "capo_gamelift.types.put_scaling_policy_output.PutScalingPolicyOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Creates or updates a scaling policy for a fleet. Scaling policies are used to automatically scale a fleet's hosting capacity to meet player demand. An active scaling policy instructs Amazon GameLift Servers to track a fleet metric and automatically change the fleet's capacity when a certain threshold is reached. There are two types of scaling policies: target-based and rule-based. Use a target-based policy to quickly and efficiently manage fleet scaling; this option is the most commonly used. Use rule-based policies when you need to exert fine-grained control over auto-scaling. </p> <p>Fleets can have multiple scaling policies of each type in force at the same time; you can have one target-based policy, one or multiple rule-based scaling policies, or both. We recommend caution, however, because multiple auto-scaling policies can have unintended consequences.</p> <p>Learn more about how to work with auto-scaling in <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-autoscaling.html">Set Up Fleet Automatic Scaling</a>.</p> <p> <b>Target-based policy</b> </p> <p>A target-based policy tracks a single metric: PercentAvailableGameSessions. This metric tells us how much of a fleet's hosting capacity is ready to host game sessions but is not currently in use. This is the fleet's buffer; it measures the additional player demand that the fleet could handle at current capacity. With a target-based policy, you set your ideal buffer size and leave it to Amazon GameLift Servers to take whatever action is needed to maintain that target. </p> <p>For example, you might choose to maintain a 10% buffer for a fleet that has the capacity to host 100 simultaneous game sessions. This policy tells Amazon GameLift Servers to take action whenever the fleet's available capacity falls below or rises above 10 game sessions. Amazon GameLift Servers will start new instances or stop unused instances in order to return to the 10% buffer. </p> <p>To create or update a target-based policy, specify a fleet ID and name, and set the policy type to "TargetBased". Specify the metric to track (PercentAvailableGameSessions) and reference a <code>TargetConfiguration</code> object with your desired buffer value. Exclude all other parameters. On a successful request, the policy name is returned. The scaling policy is automatically in force as soon as it's successfully created. If the fleet's auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.</p> <p> <b>Rule-based policy</b> </p> <p>A rule-based policy tracks specified fleet metric, sets a threshold value, and specifies the type of action to initiate when triggered. With a rule-based policy, you can select from several available fleet metrics. Each policy specifies whether to scale up or scale down (and by how much), so you need one policy for each type of action. </p> <p>For example, a policy may make the following statement: "If the percentage of idle instances is greater than 20% for more than 15 minutes, then reduce the fleet capacity by 10%."</p> <p>A policy's rule statement has the following structure:</p> <p>If <code>[MetricName]</code> is <code>[ComparisonOperator]</code> <code>[Threshold]</code> for <code>[EvaluationPeriods]</code> minutes, then <code>[ScalingAdjustmentType]</code> to/by <code>[ScalingAdjustment]</code>.</p> <p>To implement the example, the rule statement would look like this:</p> <p>If <code>[PercentIdleInstances]</code> is <code>[GreaterThanThreshold]</code> <code>[20]</code> for <code>[15]</code> minutes, then <code>[PercentChangeInCapacity]</code> to/by <code>[10]</code>.</p> <p>To create or update a scaling policy, specify a unique combination of name and fleet ID, and set the policy type to "RuleBased". Specify the parameter values for a policy rule statement. On a successful request, the policy name is returned. Scaling policies are automatically in force as soon as they're successfully created. If the fleet's auto-scaling actions are temporarily suspended, the new policy will be in force once the fleet actions are restarted.</p>

        Args:
            name: <p>A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique. A fleet can have only one scaling policy with the same name.</p>
            fleet_id: <p>A unique identifier for the fleet to apply this policy to. You can use either the fleet ID or ARN value. The fleet cannot be in any of the following statuses: ERROR or DELETING.</p>
            scaling_adjustment: <p>Amount of adjustment to make, based on the scaling adjustment type.</p>
            scaling_adjustment_type: <p>The type of adjustment to make to a fleet's instance count:</p> <ul> <li> <p> <b>ChangeInCapacity</b> -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.</p> </li> <li> <p> <b>ExactCapacity</b> -- set the instance count to the scaling adjustment value.</p> </li> <li> <p> <b>PercentChangeInCapacity</b> -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down; for example, a value of "-10" scales the fleet down by 10%.</p> </li> </ul>
            threshold: <p>Metric value used to trigger a scaling event.</p>
            comparison_operator: <p>Comparison operator to use when measuring the metric against the threshold value.</p>
            evaluation_periods: <p>Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.</p>
            metric_name: <p>Name of the Amazon GameLift Servers-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html">Monitor Amazon GameLift Servers with Amazon CloudWatch</a>. </p> <ul> <li> <p> <b>ActivatingGameSessions</b> -- Game sessions in the process of being created.</p> </li> <li> <p> <b>ActiveGameSessions</b> -- Game sessions that are currently running.</p> </li> <li> <p> <b>ActiveInstances</b> -- Fleet instances that are currently running at least one game session.</p> </li> <li> <p> <b>AvailableGameSessions</b> -- Additional game sessions that a fleet could host simultaneously, given current capacity.</p> </li> <li> <p> <b>AvailablePlayerSessions</b> -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.</p> </li> <li> <p> <b>CurrentPlayerSessions</b> -- Player slots in active game sessions that are being used by a player or are reserved for a player. </p> </li> <li> <p> <b>IdleInstances</b> -- Active instances that are currently hosting zero game sessions. </p> </li> <li> <p> <b>PercentAvailableGameSessions</b> -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.</p> </li> <li> <p> <b>PercentIdleInstances</b> -- Percentage of the total number of active instances that are hosting zero game sessions.</p> </li> <li> <p> <b>QueueDepth</b> -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.</p> </li> <li> <p> <b>WaitTime</b> -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination. </p> </li> </ul>
            policy_type: <p>The type of scaling policy to create. For a target-based policy, set the parameter <i>MetricName</i> to 'PercentAvailableGameSessions' and specify a <i>TargetConfiguration</i>. For a rule-based policy set the following parameters: <i>MetricName</i>, <i>ComparisonOperator</i>, <i>Threshold</i>, <i>EvaluationPeriods</i>, <i>ScalingAdjustmentType</i>, and <i>ScalingAdjustment</i>.</p>
            target_configuration: <p>An object that contains settings for a target-based scaling policy.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.put_scaling_policy_input.PutScalingPolicyInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.put_scaling_policy_output.PutScalingPolicyOutput"
        ]:
            import capo_gamelift._operations.game_lift.put_scaling_policy

            output, http_response = (
                capo_gamelift._operations.game_lift.put_scaling_policy.put_scaling_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.put_scaling_policy_input.PutScalingPolicyInput = {}
        if name is not None:
            input_["name"] = name
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if scaling_adjustment is not None:
            input_["scaling_adjustment"] = scaling_adjustment
        if scaling_adjustment_type is not None:
            input_["scaling_adjustment_type"] = scaling_adjustment_type
        if threshold is not None:
            input_["threshold"] = threshold
        if comparison_operator is not None:
            input_["comparison_operator"] = comparison_operator
        if evaluation_periods is not None:
            input_["evaluation_periods"] = evaluation_periods
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if policy_type is not None:
            input_["policy_type"] = policy_type
        if target_configuration is not None:
            input_["target_configuration"] = target_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_compute(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        compute_name: Optional["capo_gamelift.types.compute_name.ComputeName"] = None,
        certificate_path: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        dns_name: Optional["capo_gamelift.types.dns_name_input.DnsNameInput"] = None,
        ip_address: Optional["capo_gamelift.types.ip_address.IpAddress"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.register_compute_output.RegisterComputeOutput":
        """<p> <b>This API works with the following fleet types:</b> Anywhere</p> <p>Registers a compute resource in an Amazon GameLift Servers Anywhere fleet. </p> <p>For an Anywhere fleet that's running the Amazon GameLift Servers Agent, the Agent handles all compute registry tasks for you. For an Anywhere fleet that doesn't use the Agent, call this operation to register fleet computes.</p> <p>To register a compute, give the compute a name (must be unique within the fleet) and specify the compute resource's DNS name or IP address. Provide a fleet ID and a fleet location to associate with the compute being registered. You can optionally include the path to a TLS certificate on the compute resource.</p> <p>If successful, this operation returns compute details, including an Amazon GameLift Servers SDK endpoint or Agent endpoint. Game server processes running on the compute can use this endpoint to communicate with the Amazon GameLift Servers service. Each server process includes the SDK endpoint in its call to the Amazon GameLift Servers server SDK action <code>InitSDK()</code>. </p> <p>To view compute details, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute.html">DescribeCompute</a> with the compute name. </p> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-anywhere.html">Create an Anywhere fleet</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-testing.html">Test your integration</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html">Server SDK reference guides</a> (for version 5.x)</p> </li> </ul>

        Args:
            fleet_id: <p>A unique identifier for the fleet to register the compute to. You can use either the fleet ID or ARN value.</p>
            compute_name: <p>A descriptive label for the compute resource.</p>
            certificate_path: <p>The path to a TLS certificate on your compute resource. Amazon GameLift Servers doesn't validate the path and certificate.</p>
            dns_name: <p>The DNS name of the compute resource. Amazon GameLift Servers requires either a DNS name or IP address.</p>
            ip_address: <p>The IP address of the compute resource. Amazon GameLift Servers requires either a DNS name or IP address. When registering an Anywhere fleet, an IP address is required.</p>
            location: <p>The name of a custom location to associate with the compute resource being registered. This parameter is required when registering a compute for an Anywhere fleet.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_ready_exception.NotReadyException: <p> The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with <a href="http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">exponential backoffs and jitter</a>. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.register_compute_input.RegisterComputeInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.register_compute_output.RegisterComputeOutput"
        ]:
            import capo_gamelift._operations.game_lift.register_compute

            output, http_response = (
                capo_gamelift._operations.game_lift.register_compute.register_compute(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.register_compute_input.RegisterComputeInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if compute_name is not None:
            input_["compute_name"] = compute_name
        if certificate_path is not None:
            input_["certificate_path"] = certificate_path
        if dns_name is not None:
            input_["dns_name"] = dns_name
        if ip_address is not None:
            input_["ip_address"] = ip_address
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_game_server(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        game_server_id: Optional[
            "capo_gamelift.types.game_server_id.GameServerId"
        ] = None,
        instance_id: Optional[
            "capo_gamelift.types.game_server_instance_id.GameServerInstanceId"
        ] = None,
        connection_info: Optional[
            "capo_gamelift.types.game_server_connection_info.GameServerConnectionInfo"
        ] = None,
        game_server_data: Optional[
            "capo_gamelift.types.game_server_data.GameServerData"
        ] = None,
    ) -> "capo_gamelift.types.register_game_server_output.RegisterGameServerOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Creates a new game server resource and notifies Amazon GameLift Servers FleetIQ that the game server is ready to host gameplay and players. This operation is called by a game server process that is running on an instance in a game server group. Registering game servers enables Amazon GameLift Servers FleetIQ to track available game servers and enables game clients and services to claim a game server for a new game session. </p> <p>To register a game server, identify the game server group and instance where the game server is running, and provide a unique identifier for the game server. You can also include connection and game server data.</p> <p>Once a game server is successfully registered, it is put in status <code>AVAILABLE</code>. A request to register a game server may fail if the instance it is running on is in the process of shutting down as part of instance balancing or scale-down activity. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group where the game server is running.</p>
            game_server_id: <p>A custom string that uniquely identifies the game server to register. Game server IDs are developer-defined and must be unique across all game server groups in your Amazon Web Services account.</p>
            instance_id: <p>The unique identifier for the instance where the game server is running. This ID is available in the instance metadata. EC2 instance IDs use a 17-character format, for example: <code>i-1234567890abcdef0</code>.</p>
            connection_info: <p>Information that is needed to make inbound client connections to the game server. This might include the IP address and port, DNS name, and other information.</p>
            game_server_data: <p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers. </p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.register_game_server_input.RegisterGameServerInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.register_game_server_output.RegisterGameServerOutput"
        ]:
            import capo_gamelift._operations.game_lift.register_game_server

            output, http_response = (
                capo_gamelift._operations.game_lift.register_game_server.register_game_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.register_game_server_input.RegisterGameServerInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if game_server_id is not None:
            input_["game_server_id"] = game_server_id
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if connection_info is not None:
            input_["connection_info"] = connection_info
        if game_server_data is not None:
            input_["game_server_data"] = game_server_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def request_upload_credentials(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
    ) -> "capo_gamelift.types.request_upload_credentials_output.RequestUploadCredentialsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Retrieves a fresh set of credentials for use when uploading a new set of game build files to Amazon GameLift Servers's Amazon S3. This is done as part of the build creation process; see <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateBuild.html">CreateBuild</a>.</p> <p>To request new credentials, specify the build ID as returned with an initial <code>CreateBuild</code> request. If successful, a new set of credentials are returned, along with the S3 storage location associated with the build ID.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-cli-uploading.html#gamelift-build-cli-uploading-create-build"> Create a Build with Files in S3</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            build_id: <p>A unique identifier for the build to get credentials for. You can use either the build ID or ARN value. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.request_upload_credentials_input.RequestUploadCredentialsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.request_upload_credentials_output.RequestUploadCredentialsOutput"
        ]:
            import capo_gamelift._operations.game_lift.request_upload_credentials

            output, http_response = (
                capo_gamelift._operations.game_lift.request_upload_credentials.request_upload_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.request_upload_credentials_input.RequestUploadCredentialsInput = {}
        if build_id is not None:
            input_["build_id"] = build_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resolve_alias(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
    ) -> "capo_gamelift.types.resolve_alias_output.ResolveAliasOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Attempts to retrieve a fleet ID that is associated with an alias. Specify a unique alias identifier.</p> <p>If the alias has a <code>SIMPLE</code> routing strategy, Amazon GameLift Servers returns a fleet ID. If the alias has a <code>TERMINAL</code> routing strategy, the result is a <code>TerminalRoutingStrategyException</code>.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            alias_id: <p>The unique identifier of the alias that you want to retrieve a fleet ID for. You can use either the alias ID or ARN value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.resolve_alias_input.ResolveAliasInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.resolve_alias_output.ResolveAliasOutput"
        ]:
            import capo_gamelift._operations.game_lift.resolve_alias

            output, http_response = (
                capo_gamelift._operations.game_lift.resolve_alias.resolve_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.resolve_alias_input.ResolveAliasInput = {}
        if alias_id is not None:
            input_["alias_id"] = alias_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resume_game_server_group(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        resume_actions: Optional[
            "capo_gamelift.types.game_server_group_actions.GameServerGroupActions"
        ] = None,
    ) -> "capo_gamelift.types.resume_game_server_group_output.ResumeGameServerGroupOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Reinstates activity on a game server group after it has been suspended. A game server group might be suspended by the <a href="gamelift/latest/apireference/API_SuspendGameServerGroup.html">SuspendGameServerGroup</a> operation, or it might be suspended involuntarily due to a configuration problem. In the second case, you can manually resume activity on the group once the configuration problem has been resolved. Refer to the game server group status and status reason for more information on why group activity is suspended.</p> <p>To resume activity, specify a game server group ARN and the type of activity to be resumed. If successful, a <code>GameServerGroup</code> object is returned showing that the resumed activity is no longer listed in <code>SuspendedActions</code>. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group. Use either the name or ARN value.</p>
            resume_actions: <p>The activity to resume for this game server group.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.resume_game_server_group_input.ResumeGameServerGroupInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.resume_game_server_group_output.ResumeGameServerGroupOutput"
        ]:
            import capo_gamelift._operations.game_lift.resume_game_server_group

            output, http_response = (
                capo_gamelift._operations.game_lift.resume_game_server_group.resume_game_server_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.resume_game_server_group_input.ResumeGameServerGroupInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if resume_actions is not None:
            input_["resume_actions"] = resume_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_game_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        filter_expression: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        sort_expression: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.search_game_sessions_output.SearchGameSessionsOutput":
        r"""<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Retrieves all active game sessions that match a set of search criteria and sorts them into a specified order. </p> <p>This operation is not designed to continually track game session status because that practice can cause you to exceed your API limit and generate errors. Instead, configure an Amazon Simple Notification Service (Amazon SNS) topic to receive notifications from a matchmaker or a game session placement queue.</p> <p>When searching for game sessions, you specify exactly where you want to search and provide a search filter expression, a sort expression, or both. A search request can search only one fleet, but it can search all of a fleet's locations. </p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To search all game sessions that are currently running on all locations in a fleet, provide a fleet or alias ID. This approach returns game sessions in the fleet's home Region and all remote locations that fit the search criteria.</p> </li> <li> <p>To search all game sessions that are currently running on a specific fleet location, provide a fleet or alias ID and a location name. For location, you can specify a fleet's home Region or any remote location.</p> </li> </ul> <p>Use the pagination parameters to retrieve results as a set of sequential pages. </p> <p>If successful, a <code>GameSession</code> object is returned for each game session that matches the request. Search finds game sessions that are in <code>ACTIVE</code> status only. To retrieve information on game sessions in other statuses, use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessions.html">DescribeGameSessions</a>.</p> <p>To set search and sort criteria, create a filter expression using the following game session attributes. For game session search examples, see the Examples section of this topic.</p> <ul> <li> <p> <b>gameSessionId</b> -- An identifier for the game session that is unique across all regions. You must use the full ARN value. </p> </li> <li> <p> <b>gameSessionName</b> -- Name assigned to a game session. Game session names do not need to be unique to a game session.</p> </li> <li> <p> <b>gameSessionProperties</b> -- A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. The filter expression must specify the <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameProperty.html">GameProperty</a> -- a <code>Key</code> and a string <code>Value</code> to search for the game sessions.</p> <p>For example, to search for the above key-value pair, specify the following search filter: <code>gameSessionProperties.difficulty = "novice"</code>. All game property values are searched as strings.</p> <p> For examples of searching game sessions, see the ones below, and also see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-search">Search game sessions by game property</a>. </p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note> </li> <li> <p> <b>maximumSessions</b> -- Maximum number of player sessions allowed for a game session.</p> </li> <li> <p> <b>creationTimeMillis</b> -- Value indicating when a game session was created. It is expressed in Unix time as milliseconds.</p> </li> <li> <p> <b>playerSessionCount</b> -- Number of players currently connected to a game session. This value changes rapidly as players join the session or drop out.</p> </li> <li> <p> <b>hasAvailablePlayerSessions</b> -- Boolean value indicating whether a game session has reached its maximum number of players. It is highly recommended that all search requests include this filter attribute to optimize search performance and return only sessions that players can join. </p> </li> </ul> <note> <p>Returned values for <code>playerSessionCount</code> and <code>hasAvailablePlayerSessions</code> change quickly as players join sessions and others drop out. Results should be considered a snapshot in time. Be sure to refresh search results often, and handle sessions that fill up before a player can join. </p> </note> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to search for active game sessions. You can use either the fleet ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.</p>
            alias_id: <p>A unique identifier for the alias associated with the fleet to search for active game sessions. You can use either the alias ID or ARN value. Each request must reference either a fleet ID or alias ID, but not both.</p>
            location: <p>A fleet location to search for game sessions. You can specify a fleet's home Region or a remote location. Use the Amazon Web Services Region code format, such as <code>us-west-2</code>. </p>
            filter_expression: <p>String containing the search criteria for the session search. If no filter expression is included, the request returns results for all game sessions in the fleet that are in <code>ACTIVE</code> status.</p> <p>A filter expression can contain one or multiple conditions. Each condition consists of the following:</p> <ul> <li> <p> <b>Operand</b> -- Name of a game session attribute. Valid values are <code>gameSessionName</code>, <code>gameSessionId</code>, <code>gameSessionProperties</code>, <code>maximumSessions</code>, <code>creationTimeMillis</code>, <code>playerSessionCount</code>, <code>hasAvailablePlayerSessions</code>.</p> </li> <li> <p> <b>Comparator</b> -- Valid comparators are: <code>=</code>, <code><></code>, <code><</code>, <code>></code>, <code><=</code>, <code>>=</code>. </p> </li> <li> <p> <b>Value</b> -- Value to be searched for. Values may be numbers, boolean values (true/false) or strings depending on the operand. String values are case sensitive and must be enclosed in single quotes. Special characters must be escaped. Boolean and string values can only be used with the comparators <code>=</code> and <code><></code>. For example, the following filter expression searches on <code>gameSessionName</code>: "<code>FilterExpression": "gameSessionName = 'Matt\\'s Awesome Game 1'"</code>. </p> </li> </ul> <p>To chain multiple conditions in a single expression, use the logical keywords <code>AND</code>, <code>OR</code>, and <code>NOT</code> and parentheses as needed. For example: <code>x AND y AND NOT z</code>, <code>NOT (x OR y)</code>.</p> <p>Session search evaluates conditions from left to right using the following precedence rules:</p> <ol> <li> <p> <code>=</code>, <code><></code>, <code><</code>, <code>></code>, <code><=</code>, <code>>=</code> </p> </li> <li> <p>Parentheses</p> </li> <li> <p>NOT</p> </li> <li> <p>AND</p> </li> <li> <p>OR</p> </li> </ol> <p>For example, this filter expression retrieves game sessions hosting at least ten players that have an open player slot: <code>"maximumSessions>=10 AND hasAvailablePlayerSessions=true"</code>. </p>
            sort_expression: <p>Instructions on how to sort the search results. If no sort expression is included, the request returns results in random order. A sort expression consists of the following elements:</p> <ul> <li> <p> <b>Operand</b> -- Name of a game session attribute. Valid values are <code>gameSessionName</code>, <code>gameSessionId</code>, <code>gameSessionProperties</code>, <code>maximumSessions</code>, <code>creationTimeMillis</code>, <code>playerSessionCount</code>, <code>hasAvailablePlayerSessions</code>.</p> </li> <li> <p> <b>Order</b> -- Valid sort orders are <code>ASC</code> (ascending) and <code>DESC</code> (descending).</p> </li> </ul> <p>For example, this sort expression returns the oldest active sessions first: <code>"SortExpression": "creationTimeMillis ASC"</code>. Results with a null value for the sort operand are returned at the end of the list.</p>
            limit: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages. The maximum number of results returned is 20, even if this value is not set or is set higher than 20. </p>
            next_token: <p>A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.terminal_routing_strategy_exception.TerminalRoutingStrategyException: <p>The service is unable to resolve the routing for a particular alias because it has a terminal <code>RoutingStrategy</code> associated with it. The message returned in this exception is the message defined in the routing strategy itself. Such requests should only be retried if the routing strategy for the specified alias is modified. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.search_game_sessions_input.SearchGameSessionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.search_game_sessions_output.SearchGameSessionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.search_game_sessions

            output, http_response = (
                capo_gamelift._operations.game_lift.search_game_sessions.search_game_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.search_game_sessions_input.SearchGameSessionsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if alias_id is not None:
            input_["alias_id"] = alias_id
        if location is not None:
            input_["location"] = location
        if filter_expression is not None:
            input_["filter_expression"] = filter_expression
        if sort_expression is not None:
            input_["sort_expression"] = sort_expression
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

    def iter_search_game_sessions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        filter_expression: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        sort_expression: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        limit: Optional["capo_gamelift.types.positive_integer.PositiveInteger"] = None,
        next_token: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "Iterator[capo_gamelift.types.game_session.GameSession]":
        _token = next_token
        while True:
            _response = self.search_game_sessions(
                config_overrides=config_overrides,
                fleet_id=fleet_id,
                alias_id=alias_id,
                location=location,
                filter_expression=filter_expression,
                sort_expression=sort_expression,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("game_sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_fleet_actions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        actions: Optional[
            "capo_gamelift.types.fleet_action_list.FleetActionList"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.start_fleet_actions_output.StartFleetActionsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Resumes certain types of activity on fleet instances that were suspended with <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StopFleetActions.html">StopFleetActions</a>. For multi-location fleets, fleet actions are managed separately for each location. Currently, this operation is used to restart a fleet's auto-scaling activity.</p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To restart actions on instances in the fleet's home Region, provide a fleet ID and the type of actions to resume. </p> </li> <li> <p>To restart actions on instances in one of the fleet's remote locations, provide a fleet ID, a location name, and the type of actions to resume. </p> </li> </ul> <p>If successful, Amazon GameLift Servers once again initiates scaling events as triggered by the fleet's scaling policies. If actions on the fleet location were never stopped, this operation will have no effect.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to restart actions on. You can use either the fleet ID or ARN value.</p>
            actions: <p>List of actions to restart on the fleet.</p>
            location: <p>The fleet location to restart fleet actions for. Specify a location in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.start_fleet_actions_input.StartFleetActionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.start_fleet_actions_output.StartFleetActionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.start_fleet_actions

            output, http_response = (
                capo_gamelift._operations.game_lift.start_fleet_actions.start_fleet_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.start_fleet_actions_input.StartFleetActionsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if actions is not None:
            input_["actions"] = actions
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_game_session_placement(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        placement_id: Optional[
            "capo_gamelift.types.id_string_model.IdStringModel"
        ] = None,
        game_session_queue_name: Optional[
            "capo_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
        ] = None,
        game_properties: Optional[
            "capo_gamelift.types.game_property_list.GamePropertyList"
        ] = None,
        maximum_player_session_count: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        game_session_name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        player_latencies: Optional[
            "capo_gamelift.types.player_latency_list.PlayerLatencyList"
        ] = None,
        desired_player_sessions: Optional[
            "capo_gamelift.types.desired_player_session_list.DesiredPlayerSessionList"
        ] = None,
        game_session_data: Optional[
            "capo_gamelift.types.large_game_session_data.LargeGameSessionData"
        ] = None,
        priority_configuration_override: Optional[
            "capo_gamelift.types.priority_configuration_override.PriorityConfigurationOverride"
        ] = None,
    ) -> "capo_gamelift.types.start_game_session_placement_output.StartGameSessionPlacementOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Makes a request to start a new game session using a game session queue. When processing a placement request, Amazon GameLift Servers looks for the best possible available resource to host the game session, based on how the queue is configured to prioritize factors such as resource cost, latency, and location. After selecting an available resource, Amazon GameLift Servers prompts the resource to start a game session. A placement request can include a list of players to create a set of player sessions. The request can also include information to pass to the new game session, such as to specify a game map or other options.</p> <p> <b>Request options</b> </p> <p>Use this operation to make the following types of requests. </p> <ul> <li> <p>Request a placement using the queue's default prioritization process (see the default prioritization described in <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_PriorityConfiguration.html">PriorityConfiguration</a>). Include these required parameters:</p> <ul> <li> <p> <code>GameSessionQueueName</code> </p> </li> <li> <p> <code>MaximumPlayerSessionCount</code> </p> </li> <li> <p> <code>PlacementID</code> </p> </li> </ul> </li> <li> <p>Request a placement and prioritize based on latency. Include these parameters:</p> <ul> <li> <p>Required parameters <code>GameSessionQueueName</code>, <code>MaximumPlayerSessionCount</code>, <code>PlacementID</code>.</p> </li> <li> <p> <code>PlayerLatencies</code>. Include a set of latency values for destinations in the queue. When a request includes latency data, Amazon GameLift Servers automatically reorders the queue's locations priority list based on lowest available latency values. If a request includes latency data for multiple players, Amazon GameLift Servers calculates each location's average latency for all players and reorders to find the lowest latency across all players. </p> </li> <li> <p>Don't include <code>PriorityConfigurationOverride</code>.</p> </li> </ul> <ul> <li> <p>Prioritize based on a custom list of locations. If you're using a queue that's configured to prioritize location first (see <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_PriorityConfiguration.html">PriorityConfiguration</a> for game session queues), you can optionally use the <i>PriorityConfigurationOverride</i> parameter to substitute a different location priority list for this placement request. Amazon GameLift Servers searches each location on the priority override list to find an available hosting resource for the new game session. Specify a fallback strategy to use in the event that Amazon GameLift Servers fails to place the game session in any of the locations on the override list. </p> </li> </ul> </li> <li> <p>Request a placement and prioritize based on a custom list of locations. </p> </li> <li> <p>You can request new player sessions for a group of players. Include the <i>DesiredPlayerSessions</i> parameter and include at minimum a unique player ID for each. You can also include player-specific data to pass to the new game session. </p> </li> </ul> <p> <b>Result</b> </p> <p>If successful, this operation generates a new game session placement request and adds it to the game session queue for processing. You can track the status of individual placement requests by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeGameSessionPlacement.html">DescribeGameSessionPlacement</a> or by monitoring queue notifications. When the request status is <code>FULFILLED</code>, a new game session has started and the placement request is updated with connection information for the game session (IP address and port). If the request included player session data, Amazon GameLift Servers creates a player session for each player ID in the request.</p> <p>The request results in a <code>InvalidRequestException</code> in the following situations:</p> <ul> <li> <p>If the request includes both <i>PlayerLatencies</i> and <i>PriorityConfigurationOverride</i> parameters.</p> </li> <li> <p>If the request includes the <i>PriorityConfigurationOverride</i> parameter and specifies a queue that doesn't prioritize locations.</p> </li> </ul> <p>Amazon GameLift Servers continues to retry each placement request until it reaches the queue's timeout setting. If a request times out, you can resubmit the request to the same queue or try a different queue. </p>

        Args:
            placement_id: <p>A unique identifier to assign to the new game session placement. This value is developer-defined. The value must be unique across all Regions and cannot be reused.</p>
            game_session_queue_name: <p>Name of the queue to use to place the new game session. You can use either the queue name or ARN value. </p>
            game_properties: <p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>
            maximum_player_session_count: <p>The maximum number of players that can be connected simultaneously to the game session.</p>
            game_session_name: <p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>
            player_latencies: <p>A set of values, expressed in milliseconds, that indicates the amount of latency that a player experiences when connected to a fleet location (Amazon Web Services Regions or custom locations for Amazon GameLift Servers Anywhere fleets). This information is used to try to place the new game session where it can offer the best possible gameplay experience for the players. </p>
            desired_player_sessions: <p>Set of information on each player to create a player session for.</p>
            game_session_data: <p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>.</p>
            priority_configuration_override: <p>A prioritized list of locations to use for the game session placement and instructions on how to use it. This list overrides a queue's prioritized location list for this game session placement request only. You can include Amazon Web Services Regions, local zones, and custom locations (for Anywhere fleets). You can choose to limit placements to locations on the override list only, or you can prioritize locations on the override list first and then fall back to the queue's other locations if needed. Choose a fallback strategy to use in the event that Amazon GameLift Servers fails to place a game session in any of the locations on the priority override list. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.start_game_session_placement_input.StartGameSessionPlacementInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.start_game_session_placement_output.StartGameSessionPlacementOutput"
        ]:
            import capo_gamelift._operations.game_lift.start_game_session_placement

            output, http_response = (
                capo_gamelift._operations.game_lift.start_game_session_placement.start_game_session_placement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.start_game_session_placement_input.StartGameSessionPlacementInput = {}
        if placement_id is not None:
            input_["placement_id"] = placement_id
        if game_session_queue_name is not None:
            input_["game_session_queue_name"] = game_session_queue_name
        if game_properties is not None:
            input_["game_properties"] = game_properties
        if maximum_player_session_count is not None:
            input_["maximum_player_session_count"] = maximum_player_session_count
        if game_session_name is not None:
            input_["game_session_name"] = game_session_name
        if player_latencies is not None:
            input_["player_latencies"] = player_latencies
        if desired_player_sessions is not None:
            input_["desired_player_sessions"] = desired_player_sessions
        if game_session_data is not None:
            input_["game_session_data"] = game_session_data
        if priority_configuration_override is not None:
            input_["priority_configuration_override"] = priority_configuration_override

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_match_backfill(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        ticket_id: Optional[
            "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
        ] = None,
        configuration_name: Optional[
            "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
        ] = None,
        game_session_arn: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        players: Optional["capo_gamelift.types.player_list.PlayerList"] = None,
    ) -> "capo_gamelift.types.start_match_backfill_output.StartMatchBackfillOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Finds new players to fill open slots in currently running game sessions. The backfill match process is essentially identical to the process of forming new matches. Backfill requests use the same matchmaker that was used to make the original match, and they provide matchmaking data for all players currently in the game session. FlexMatch uses this information to select new players so that the backfilled match continues to meet the original match requirements. </p> <p>When using FlexMatch with Amazon GameLift Servers managed hosting, you can request a backfill match from a client service by calling this operation with a <code>GameSessions</code> ID. You also have the option of making backfill requests directly from your game server. In response to a request, FlexMatch creates player sessions for the new players, updates the <code>GameSession</code> resource, and sends updated matchmaking data to the game server. You can request a backfill match at any point after a game session is started. Each game session can have only one active backfill request at a time; a subsequent request automatically replaces the earlier request.</p> <p>When using FlexMatch as a standalone component, request a backfill match by calling this operation without a game session identifier. As with newly formed matches, matchmaking results are returned in a matchmaking event so that your game can update the game session that is being backfilled.</p> <p>To request a backfill match, specify a unique ticket ID, the original matchmaking configuration, and matchmaking data for all current players in the game session being backfilled. Optionally, specify the <code>GameSession</code> ARN. If successful, a match backfill ticket is created and returned with status set to QUEUED. Track the status of backfill tickets using the same method for tracking tickets for new matches.</p> <p>Only game sessions created by FlexMatch are supported for match backfill.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html"> Backfill existing games with FlexMatch</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html"> Matchmaking events</a> (reference)</p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html"> How Amazon GameLift Servers FlexMatch works</a> </p>

        Args:
            ticket_id: <p>A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the match backfill ticket status and retrieve match results.</p>
            configuration_name: <p>Name of the matchmaker to use for this request. You can use either the configuration name or ARN value. The ARN of the matchmaker that was used with the original game session is listed in the <code>GameSession</code> object, <code>MatchmakerData</code> property.</p>
            game_session_arn: <p>An identifier for the game session that is unique across all regions. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>. When using FlexMatch as a standalone matchmaking solution, this parameter is not needed. </p>
            players: <p>Match information on all players that are currently assigned to the game session. This information is used by the matchmaker to find new players and add them to the existing game.</p> <p>You can include up to 199 <code>Players</code> in a <code>StartMatchBackfill</code> request.</p> <ul> <li> <p>PlayerID, PlayerAttributes, Team -- This information is maintained in the <code>GameSession</code> object, <code>MatchmakerData</code> property, for all players who are currently assigned to the game session. The matchmaker data is in JSON syntax, formatted as a string. For more details, see <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-server.html#match-server-data"> Match Data</a>. </p> <p>The backfill request must specify the team membership for every player. Do not specify team if you are not using backfill.</p> </li> <li> <p>LatencyInMs -- If the matchmaker uses player latency, include a latency value, in milliseconds, for the Region that the game session is currently in. Do not include latency values for any other Region.</p> </li> </ul>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.start_match_backfill_input.StartMatchBackfillInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.start_match_backfill_output.StartMatchBackfillOutput"
        ]:
            import capo_gamelift._operations.game_lift.start_match_backfill

            output, http_response = (
                capo_gamelift._operations.game_lift.start_match_backfill.start_match_backfill(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.start_match_backfill_input.StartMatchBackfillInput = {}
        if ticket_id is not None:
            input_["ticket_id"] = ticket_id
        if configuration_name is not None:
            input_["configuration_name"] = configuration_name
        if game_session_arn is not None:
            input_["game_session_arn"] = game_session_arn
        if players is not None:
            input_["players"] = players

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_matchmaking(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        ticket_id: Optional[
            "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
        ] = None,
        configuration_name: Optional[
            "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
        ] = None,
        players: Optional["capo_gamelift.types.player_list.PlayerList"] = None,
    ) -> "capo_gamelift.types.start_matchmaking_output.StartMatchmakingOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Uses FlexMatch to create a game match for a group of players based on custom matchmaking rules. With games that use Amazon GameLift Servers managed hosting, this operation also triggers Amazon GameLift Servers to find hosting resources and start a new game session for the new match. Each matchmaking request includes information on one or more players and specifies the FlexMatch matchmaker to use. When a request is for multiple players, FlexMatch attempts to build a match that includes all players in the request, placing them in the same team and finding additional players as needed to fill the match. </p> <p>To start matchmaking, provide a unique ticket ID, specify a matchmaking configuration, and include the players to be matched. You must also include any player attributes that are required by the matchmaking configuration's rule set. If successful, a matchmaking ticket is returned with status set to <code>QUEUED</code>. </p> <p>Track matchmaking events to respond as needed and acquire game session connection information for successfully completed matches. Ticket status updates are tracked using event notification through Amazon Simple Notification Service, which is defined in the matchmaking configuration.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html"> Add FlexMatch to a game client</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html"> Set Up FlexMatch event notification</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/gamelift-match.html"> How Amazon GameLift Servers FlexMatch works</a> </p>

        Args:
            ticket_id: <p>A unique identifier for a matchmaking ticket. If no ticket ID is specified here, Amazon GameLift Servers will generate one in the form of a UUID. Use this identifier to track the matchmaking ticket status and retrieve match results.</p>
            configuration_name: <p>Name of the matchmaking configuration to use for this request. Matchmaking configurations must exist in the same Region as this request. You can use either the configuration name or ARN value.</p>
            players: <p>Information on each player to be matched. This information must include a player ID, and may contain player attributes and latency data to be used in the matchmaking process. After a successful match, <code>Player</code> objects contain the name of the team the player is assigned to.</p> <p>You can include up to 10 <code>Players</code> in a <code>StartMatchmaking</code> request.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.start_matchmaking_input.StartMatchmakingInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.start_matchmaking_output.StartMatchmakingOutput"
        ]:
            import capo_gamelift._operations.game_lift.start_matchmaking

            output, http_response = (
                capo_gamelift._operations.game_lift.start_matchmaking.start_matchmaking(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.start_matchmaking_input.StartMatchmakingInput = {}
        if ticket_id is not None:
            input_["ticket_id"] = ticket_id
        if configuration_name is not None:
            input_["configuration_name"] = configuration_name
        if players is not None:
            input_["players"] = players

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_fleet_actions(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        actions: Optional[
            "capo_gamelift.types.fleet_action_list.FleetActionList"
        ] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
    ) -> "capo_gamelift.types.stop_fleet_actions_output.StopFleetActionsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Suspends certain types of activity in a fleet location. Currently, this operation is used to stop auto-scaling activity. For multi-location fleets, fleet actions are managed separately for each location. </p> <p>Stopping fleet actions has several potential purposes. It allows you to temporarily stop auto-scaling activity but retain your scaling policies for use in the future. For multi-location fleets, you can set up fleet-wide auto-scaling, and then opt out of it for certain locations. </p> <p>This operation can be used in the following ways: </p> <ul> <li> <p>To stop actions on instances in the fleet's home Region, provide a fleet ID and the type of actions to suspend. </p> </li> <li> <p>To stop actions on instances in one of the fleet's remote locations, provide a fleet ID, a location name, and the type of actions to suspend. </p> </li> </ul> <p>If successful, Amazon GameLift Servers no longer initiates scaling events except in response to manual changes using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html">UpdateFleetCapacity</a>. To restart fleet actions again, call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_StartFleetActions.html">StartFleetActions</a>.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers Fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to stop actions on. You can use either the fleet ID or ARN value.</p>
            actions: <p>List of actions to suspend on the fleet. </p>
            location: <p>The fleet location to stop fleet actions for. Specify a location in the form of an Amazon Web Services Region code, such as <code>us-west-2</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.stop_fleet_actions_input.StopFleetActionsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.stop_fleet_actions_output.StopFleetActionsOutput"
        ]:
            import capo_gamelift._operations.game_lift.stop_fleet_actions

            output, http_response = (
                capo_gamelift._operations.game_lift.stop_fleet_actions.stop_fleet_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.stop_fleet_actions_input.StopFleetActionsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if actions is not None:
            input_["actions"] = actions
        if location is not None:
            input_["location"] = location

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_game_session_placement(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        placement_id: Optional[
            "capo_gamelift.types.id_string_model.IdStringModel"
        ] = None,
    ) -> "capo_gamelift.types.stop_game_session_placement_output.StopGameSessionPlacementOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Cancels a game session placement that's in <code>PENDING</code> status. To stop a placement, provide the placement ID value. </p> <p>Results</p> <p>If successful, this operation removes the placement request from the queue and moves the <code>GameSessionPlacement</code> to <code>CANCELLED</code> status.</p> <p>This operation results in an <code>InvalidRequestException</code> (400) error if a game session has already been created for this placement. You can clean up an unneeded game session by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_TerminateGameSession">TerminateGameSession</a>.</p>

        Args:
            placement_id: <p>A unique identifier for a game session placement to stop.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.stop_game_session_placement_input.StopGameSessionPlacementInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.stop_game_session_placement_output.StopGameSessionPlacementOutput"
        ]:
            import capo_gamelift._operations.game_lift.stop_game_session_placement

            output, http_response = (
                capo_gamelift._operations.game_lift.stop_game_session_placement.stop_game_session_placement(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.stop_game_session_placement_input.StopGameSessionPlacementInput = {}
        if placement_id is not None:
            input_["placement_id"] = placement_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_matchmaking(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        ticket_id: Optional[
            "capo_gamelift.types.matchmaking_id_string_model.MatchmakingIdStringModel"
        ] = None,
    ) -> "capo_gamelift.types.stop_matchmaking_output.StopMatchmakingOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Cancels a matchmaking ticket or match backfill ticket that is currently being processed. To stop the matchmaking operation, specify the ticket ID. If successful, work on the ticket is stopped, and the ticket status is changed to <code>CANCELLED</code>.</p> <p>This call is also used to turn off automatic backfill for an individual game session. This is for game sessions that are created with a matchmaking configuration that has automatic backfill enabled. The ticket ID is included in the <code>MatchmakerData</code> of an updated game session object, which is provided to the game server.</p> <note> <p>If the operation is successful, the service sends back an empty JSON struct with the HTTP 200 response (not an empty HTTP body).</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-client.html"> Add FlexMatch to a game client</a> </p>

        Args:
            ticket_id: <p>A unique identifier for a matchmaking ticket.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.stop_matchmaking_input.StopMatchmakingInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.stop_matchmaking_output.StopMatchmakingOutput"
        ]:
            import capo_gamelift._operations.game_lift.stop_matchmaking

            output, http_response = (
                capo_gamelift._operations.game_lift.stop_matchmaking.stop_matchmaking(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.stop_matchmaking_input.StopMatchmakingInput = {}
        if ticket_id is not None:
            input_["ticket_id"] = ticket_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def suspend_game_server_group(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        suspend_actions: Optional[
            "capo_gamelift.types.game_server_group_actions.GameServerGroupActions"
        ] = None,
    ) -> "capo_gamelift.types.suspend_game_server_group_output.SuspendGameServerGroupOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Temporarily stops activity on a game server group without terminating instances or the game server group. You can restart activity by calling <a href="gamelift/latest/apireference/API_ResumeGameServerGroup.html">ResumeGameServerGroup</a>. You can suspend the following activity:</p> <ul> <li> <p> <b>Instance type replacement</b> - This activity evaluates the current game hosting viability of all Spot instance types that are defined for the game server group. It updates the Auto Scaling group to remove nonviable Spot Instance types, which have a higher chance of game server interruptions. It then balances capacity across the remaining viable Spot Instance types. When this activity is suspended, the Auto Scaling group continues with its current balance, regardless of viability. Instance protection, utilization metrics, and capacity scaling activities continue to be active. </p> </li> </ul> <p>To suspend activity, specify a game server group ARN and the type of activity to be suspended. If successful, a <code>GameServerGroup</code> object is returned showing that the activity is listed in <code>SuspendedActions</code>.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group. Use either the name or ARN value.</p>
            suspend_actions: <p>The activity to suspend for this game server group.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.suspend_game_server_group_input.SuspendGameServerGroupInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.suspend_game_server_group_output.SuspendGameServerGroupOutput"
        ]:
            import capo_gamelift._operations.game_lift.suspend_game_server_group

            output, http_response = (
                capo_gamelift._operations.game_lift.suspend_game_server_group.suspend_game_server_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.suspend_game_server_group_input.SuspendGameServerGroupInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if suspend_actions is not None:
            input_["suspend_actions"] = suspend_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        resource_arn: Optional[
            "capo_gamelift.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tags: Optional["capo_gamelift.types.tag_list.TagList"] = None,
    ) -> "capo_gamelift.types.tag_resource_response.TagResourceResponse":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Assigns a tag to an Amazon GameLift Servers resource. You can use tags to organize resources, create IAM permissions policies to manage access to groups of resources, customize Amazon Web Services cost breakdowns, and more. This operation handles the permissions necessary to manage tags for Amazon GameLift Servers resources that support tagging.</p> <p>To add a tag to a resource, specify the unique ARN value for the resource and provide a tag list containing one or more tags. The operation succeeds even if the list includes tags that are already assigned to the resource. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i> </p> <p> <a href="http://aws.amazon.com/answers/account-management/aws-tagging-strategies/"> Amazon Web Services Tagging Strategies</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that uniquely identifies the Amazon GameLift Servers resource that you want to assign tags to. Amazon GameLift Servers includes resource ARNs in the data object for the resource. You can retrieve the ARN by calling a <code>List</code> or <code>Describe</code> operation for the resource type. </p>
            tags: <p>A list of one or more tags to assign to the specified Amazon GameLift Servers resource. Tags are developer-defined and structured as key-value pairs. The maximum tag limit may be lower than stated. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> for tagging limits.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_gamelift.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_gamelift._operations.game_lift.tag_resource

            output, http_response = (
                capo_gamelift._operations.game_lift.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.tag_resource_request.TagResourceRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_game_session(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        termination_mode: Optional[
            "capo_gamelift.types.termination_mode.TerminationMode"
        ] = None,
    ) -> "capo_gamelift.types.terminate_game_session_output.TerminateGameSessionOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Ends a game session that's currently in progress. Use this action to terminate any game session that isn't in <code>ERROR</code> status. Terminating a game session is the most efficient way to free up a server process when it's hosting a game session that's in a bad state or not ending properly. You can use this action to terminate a game session that's being hosted on any type of Amazon GameLift Servers fleet compute, including computes for managed EC2, managed container, and Anywhere fleets. The game server must be integrated with Amazon GameLift Servers server SDK 5.x or greater.</p> <p> <b>Request options</b> </p> <p>Request termination for a single game session. Provide the game session ID and the termination mode. There are two potential methods for terminating a game session:</p> <ul> <li> <p>Initiate a graceful termination using the normal game session shutdown sequence. With this mode, the Amazon GameLift Servers service prompts the server process that's hosting the game session by calling the server SDK callback method <code>OnProcessTerminate()</code>. The callback implementation is part of the custom game server code. It might involve a variety of actions to gracefully end a game session, such as notifying players, before stopping the server process.</p> </li> <li> <p>Force an immediate game session termination. With this mode, the Amazon GameLift Servers service takes action to stop the server process, which ends the game session without the normal game session shutdown sequence. </p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, game session termination is initiated. During this activity, the game session status is changed to <code>TERMINATING</code>. When completed, the server process that was hosting the game session has been stopped and replaced with a new server process that's ready to host a new game session. The old game session's status is changed to <code>TERMINATED</code> with a status reason that indicates the termination method used.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html">Add Amazon GameLift Servers to your game server</a> </p> <p>Amazon GameLift Servers server SDK 5 reference guide for <code>OnProcessTerminate()</code> (<a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-cpp-initsdk.html">C++</a>) (<a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-csharp-initsdk.html">C#</a>) (<a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk5-unreal-initsdk.html">Unreal</a>) (<a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-server-sdk-go-initsdk.html">Go</a>) </p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions to be terminated. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            termination_mode: <p>The method to use to terminate the game session. Available methods include: </p> <ul> <li> <p> <code>TRIGGER_ON_PROCESS_TERMINATE</code> – Prompts the Amazon GameLift Servers service to send an <code>OnProcessTerminate()</code> callback to the server process and initiate the normal game session shutdown sequence. The <code>OnProcessTerminate</code> method, which is implemented in the game server code, must include a call to the server SDK action <code>ProcessEnding()</code>, which is how the server process signals to Amazon GameLift Servers that a game session is ending. If the server process doesn't call <code>ProcessEnding()</code>, the game session termination won't conclude successfully.</p> </li> <li> <p> <code>FORCE_TERMINATE</code> – Prompts the Amazon GameLift Servers service to stop the server process immediately. Amazon GameLift Servers takes action (depending on the type of fleet) to shut down the server process without the normal game session shutdown sequence. </p> <note> <p>This method is not available for game sessions that are running on Anywhere fleets unless the fleet is deployed with the Amazon GameLift Servers Agent. In this scenario, a force terminate request results in an invalid or bad request exception.</p> </note> </li> </ul>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_game_session_status_exception.InvalidGameSessionStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.not_ready_exception.NotReadyException: <p> The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with <a href="http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">exponential backoffs and jitter</a>. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.terminate_game_session_input.TerminateGameSessionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.terminate_game_session_output.TerminateGameSessionOutput"
        ]:
            import capo_gamelift._operations.game_lift.terminate_game_session

            output, http_response = (
                capo_gamelift._operations.game_lift.terminate_game_session.terminate_game_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.terminate_game_session_input.TerminateGameSessionInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if termination_mode is not None:
            input_["termination_mode"] = termination_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        resource_arn: Optional[
            "capo_gamelift.types.amazon_resource_name.AmazonResourceName"
        ] = None,
        tag_keys: Optional["capo_gamelift.types.tag_key_list.TagKeyList"] = None,
    ) -> "capo_gamelift.types.untag_resource_response.UntagResourceResponse":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Removes a tag assigned to a Amazon GameLift Servers resource. You can use resource tags to organize Amazon Web Services resources for a range of purposes. This operation handles the permissions necessary to manage tags for Amazon GameLift Servers resources that support tagging.</p> <p>To remove a tag from a resource, specify the unique ARN value for the resource and provide a string list containing one or more tags to remove. This operation succeeds even if the list includes tags that aren't assigned to the resource.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i> </p> <p> <a href="http://aws.amazon.com/answers/account-management/aws-tagging-strategies/"> Amazon Web Services Tagging Strategies</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            resource_arn: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that uniquely identifies the Amazon GameLift Servers resource that you want to remove tags from. Amazon GameLift Servers includes resource ARNs in the data object for the resource. You can retrieve the ARN by calling a <code>List</code> or <code>Describe</code> operation for the resource type. </p>
            tag_keys: <p>A list of one or more tag keys to remove from the specified Amazon GameLift Servers resource. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.tagging_failed_exception.TaggingFailedException: <p>The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_gamelift.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_gamelift._operations.game_lift.untag_resource

            output, http_response = (
                capo_gamelift._operations.game_lift.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.untag_resource_request.UntagResourceRequest = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if tag_keys is not None:
            input_["tag_keys"] = tag_keys

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_alias(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        alias_id: Optional["capo_gamelift.types.alias_id_or_arn.AliasIdOrArn"] = None,
        name: Optional[
            "capo_gamelift.types.non_blank_and_length_constraint_string.NonBlankAndLengthConstraintString"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        routing_strategy: Optional[
            "capo_gamelift.types.routing_strategy.RoutingStrategy"
        ] = None,
    ) -> "capo_gamelift.types.update_alias_output.UpdateAliasOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Updates properties for an alias. Specify the unique identifier of the alias to be updated and the new property values.</p> <p>When reassigning an alias to a new fleet, provide an updated routing strategy. If successful, the updated alias record is returned.</p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            alias_id: <p>A unique identifier for the alias that you want to update. You can use either the alias ID or ARN value.</p>
            name: <p>A descriptive label that is associated with an alias. Alias names do not need to be unique.</p>
            description: <p>A human-readable description of the alias.</p>
            routing_strategy: <p>The routing configuration, including routing type and fleet target, for the alias.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_alias_input.UpdateAliasInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_alias_output.UpdateAliasOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_alias

            output, http_response = (
                capo_gamelift._operations.game_lift.update_alias.update_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_alias_input.UpdateAliasInput = {}
        if alias_id is not None:
            input_["alias_id"] = alias_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if routing_strategy is not None:
            input_["routing_strategy"] = routing_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_build(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        build_id: Optional["capo_gamelift.types.build_id_or_arn.BuildIdOrArn"] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        version: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
    ) -> "capo_gamelift.types.update_build_output.UpdateBuildOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Updates metadata in a build resource, including the build name and version. To update the metadata, specify the build ID to update and provide the new values. If successful, a build object containing the updated metadata is returned.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-build-intro.html"> Upload a Custom Server Build</a> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            build_id: <p>A unique identifier for the build to update. You can use either the build ID or ARN value. </p>
            name: <p>A descriptive label that is associated with a build. Build names do not need to be unique. </p>
            version: <p>Version information that is associated with a build or script. Version strings do not need to be unique.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_build_input.UpdateBuildInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_build_output.UpdateBuildOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_build

            output, http_response = (
                capo_gamelift._operations.game_lift.update_build.update_build(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_build_input.UpdateBuildInput = {}
        if build_id is not None:
            input_["build_id"] = build_id
        if name is not None:
            input_["name"] = name
        if version is not None:
            input_["version"] = version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_container_fleet(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        game_server_container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        per_instance_container_group_definition_name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        game_server_container_groups_per_instance: Optional[
            "capo_gamelift.types.game_server_container_groups_per_instance.GameServerContainerGroupsPerInstance"
        ] = None,
        instance_connection_port_range: Optional[
            "capo_gamelift.types.connection_port_range.ConnectionPortRange"
        ] = None,
        instance_inbound_permission_authorizations: Optional[
            "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
        ] = None,
        instance_inbound_permission_revocations: Optional[
            "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
        ] = None,
        deployment_configuration: Optional[
            "capo_gamelift.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        metric_groups: Optional[
            "capo_gamelift.types.metric_group_list.MetricGroupList"
        ] = None,
        new_game_session_protection_policy: Optional[
            "capo_gamelift.types.protection_policy.ProtectionPolicy"
        ] = None,
        game_session_creation_limit_policy: Optional[
            "capo_gamelift.types.game_session_creation_limit_policy.GameSessionCreationLimitPolicy"
        ] = None,
        log_configuration: Optional[
            "capo_gamelift.types.log_configuration.LogConfiguration"
        ] = None,
        remove_attributes: Optional[
            "capo_gamelift.types.container_fleet_remove_attribute_list.ContainerFleetRemoveAttributeList"
        ] = None,
    ) -> "capo_gamelift.types.update_container_fleet_output.UpdateContainerFleetOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Updates the properties of a managed container fleet. Depending on the properties being updated, this operation might initiate a fleet deployment. You can track deployments for a fleet using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html">https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html</a>.</p> <note> <p>A managed fleet's runtime environment, which depends on the fleet's Amazon Machine Image (AMI) version, can't be updated. You must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html"> Security best practices for Amazon GameLift Servers</a>.</p> </note> <p> <b>Request options</b> </p> <p>As with CreateContainerFleet, many fleet properties use common defaults or are calculated based on the fleet's container group definitions. </p> <ul> <li> <p>Update fleet properties that result in a fleet deployment. Include only those properties that you want to change. Specify deployment configuration settings.</p> </li> <li> <p>Update fleet properties that don't result in a fleet deployment. Include only those properties that you want to change.</p> </li> </ul> <p>Changes to the following properties initiate a fleet deployment: </p> <ul> <li> <p> <code>GameServerContainerGroupDefinition</code> </p> </li> <li> <p> <code>PerInstanceContainerGroupDefinition</code> </p> </li> <li> <p> <code>GameServerContainerGroupsPerInstance</code> </p> </li> <li> <p> <code>InstanceInboundPermissions</code> </p> </li> <li> <p> <code>InstanceConnectionPortRange</code> </p> </li> <li> <p> <code>LogConfiguration</code> </p> </li> </ul> <p> <b>Results</b> </p> <p>If successful, this operation updates the container fleet resource, and might initiate a new deployment of fleet resources using the deployment configuration provided. A deployment replaces existing fleet instances with new instances that are deployed with the updated fleet properties. The fleet is placed in <code>UPDATING</code> status until the deployment is complete, then returns to <code>ACTIVE</code>. </p> <p>You can have only one update deployment active at a time for a fleet. If a second update request initiates a deployment while another deployment is in progress, the first deployment is cancelled.</p>

        Args:
            fleet_id: <p>A unique identifier for the container fleet to update. You can use either the fleet ID or ARN value.</p>
            game_server_container_group_definition_name: <p>The name or ARN value of a new game server container group definition to deploy on the fleet. If you're updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If you're updating the fleet to the latest version of a container group definition, you can use the name value. You can't remove a fleet's game server container group definition, you can only update or replace it with another definition.</p> <p>Update a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html">UpdateContainerGroupDefinition</a>. This operation creates a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html">ContainerGroupDefinition</a> resource with an incremented version. </p>
            per_instance_container_group_definition_name: <p>The name or ARN value of a new per-instance container group definition to deploy on the fleet. If you're updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If you're updating the fleet to the latest version of a container group definition, you can use the name value.</p> <p>Update a container group definition by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html">UpdateContainerGroupDefinition</a>. This operation creates a <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html">ContainerGroupDefinition</a> resource with an incremented version. </p> <p>To remove a fleet's per-instance container group definition, leave this parameter empty and use the parameter <code>RemoveAttributes</code>.</p>
            game_server_container_groups_per_instance: <p>The number of times to replicate the game server container group on each fleet instance. By default, Amazon GameLift Servers calculates the maximum number of game server container groups that can fit on each instance. You can remove this property value to use the calculated value, or set it manually. If you set this number manually, Amazon GameLift Servers uses your value as long as it's less than the calculated maximum.</p>
            instance_connection_port_range: <p>A revised set of port numbers to open on each fleet instance. By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. If you previously set this parameter manually, you can't reset this to use the calculated settings.</p> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>
            instance_inbound_permission_authorizations: <p>A set of ports to add to the container fleet's inbound permissions.</p> <p>The port range must not overlap with the Amazon GameLift Servers reserved port range <code>4092-4191</code>. This range is reserved for internal Amazon GameLift Servers services.</p>
            instance_inbound_permission_revocations: <p>A set of ports to remove from the container fleet's inbound permissions.</p>
            deployment_configuration: <p>Instructions for how to deploy updates to a container fleet, if the fleet update initiates a deployment. The deployment configuration lets you determine how to replace fleet instances and what actions to take if the deployment fails.</p>
            description: <p>A meaningful description of the container fleet.</p>
            metric_groups: <p>The name of an Amazon Web Services CloudWatch metric group to add this fleet to. </p>
            new_game_session_protection_policy: <p>The game session protection policy to apply to all new game sessions that are started in this fleet. Game sessions that already exist are not affected. </p>
            game_session_creation_limit_policy: <p>A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.</p>
            log_configuration: <p>The method for collecting container logs for the fleet. </p>
            remove_attributes: <p>If set, this update removes a fleet's per-instance container group definition. You can't remove a fleet's game server container group definition.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.not_ready_exception.NotReadyException: <p> The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with <a href="http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">exponential backoffs and jitter</a>. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_container_fleet_input.UpdateContainerFleetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_container_fleet_output.UpdateContainerFleetOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_container_fleet

            output, http_response = (
                capo_gamelift._operations.game_lift.update_container_fleet.update_container_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_container_fleet_input.UpdateContainerFleetInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if game_server_container_group_definition_name is not None:
            input_["game_server_container_group_definition_name"] = (
                game_server_container_group_definition_name
            )
        if per_instance_container_group_definition_name is not None:
            input_["per_instance_container_group_definition_name"] = (
                per_instance_container_group_definition_name
            )
        if game_server_container_groups_per_instance is not None:
            input_["game_server_container_groups_per_instance"] = (
                game_server_container_groups_per_instance
            )
        if instance_connection_port_range is not None:
            input_["instance_connection_port_range"] = instance_connection_port_range
        if instance_inbound_permission_authorizations is not None:
            input_["instance_inbound_permission_authorizations"] = (
                instance_inbound_permission_authorizations
            )
        if instance_inbound_permission_revocations is not None:
            input_["instance_inbound_permission_revocations"] = (
                instance_inbound_permission_revocations
            )
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if description is not None:
            input_["description"] = description
        if metric_groups is not None:
            input_["metric_groups"] = metric_groups
        if new_game_session_protection_policy is not None:
            input_["new_game_session_protection_policy"] = (
                new_game_session_protection_policy
            )
        if game_session_creation_limit_policy is not None:
            input_["game_session_creation_limit_policy"] = (
                game_session_creation_limit_policy
            )
        if log_configuration is not None:
            input_["log_configuration"] = log_configuration
        if remove_attributes is not None:
            input_["remove_attributes"] = remove_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_container_group_definition(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.container_group_definition_name_or_arn.ContainerGroupDefinitionNameOrArn"
        ] = None,
        game_server_container_definition: Optional[
            "capo_gamelift.types.game_server_container_definition_input.GameServerContainerDefinitionInput"
        ] = None,
        support_container_definitions: Optional[
            "capo_gamelift.types.support_container_definition_input_list.SupportContainerDefinitionInputList"
        ] = None,
        total_memory_limit_mebibytes: Optional[
            "capo_gamelift.types.container_total_memory_limit.ContainerTotalMemoryLimit"
        ] = None,
        total_vcpu_limit: Optional[
            "capo_gamelift.types.container_total_vcpu_limit.ContainerTotalVcpuLimit"
        ] = None,
        version_description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        source_version_number: Optional[
            "capo_gamelift.types.positive_integer.PositiveInteger"
        ] = None,
        operating_system: Optional[
            "capo_gamelift.types.container_operating_system.ContainerOperatingSystem"
        ] = None,
        remove_attributes: Optional[
            "capo_gamelift.types.container_group_definition_remove_attribute_list.ContainerGroupDefinitionRemoveAttributeList"
        ] = None,
    ) -> "capo_gamelift.types.update_container_group_definition_output.UpdateContainerGroupDefinitionOutput":
        """<p> <b>This API works with the following fleet types:</b> Container</p> <p>Updates properties in an existing container group definition. This operation doesn't replace the definition. Instead, it creates a new version of the definition and saves it separately. You can access all versions that you choose to retain.</p> <p>The only property you can't update is the container group type.</p> <p> <b>Request options:</b> </p> <ul> <li> <p>Update based on the latest version of the container group definition. Specify the container group definition name only, or use an ARN value without a version number. Provide updated values for the properties that you want to change only. All other values remain the same as the latest version.</p> </li> <li> <p>Update based on a specific version of the container group definition. Specify the container group definition name and a source version number, or use an ARN value with a version number. Provide updated values for the properties that you want to change only. All other values remain the same as the source version.</p> </li> <li> <p>Change a game server container definition. Provide a complete set of container definitions, including the updated definition.</p> </li> <li> <p>Add or change a support container definition. Provide a complete set of container definitions, including the updated definition.</p> </li> <li> <p>Remove a support container definition. Provide a complete set of container definitions, excluding the definition to remove. If the container group has only one support container definition, provide an empty set.</p> </li> <li> <p>Remove the total vCPU limit from a game server container group so that its containers can use up to the instance's available vCPU. Set <code>RemoveAttributes</code> to <code>TOTAL_VCPU_LIMIT</code>. The game server container must have a <code>Vcpu</code> value, because a game server container group needs either a total vCPU limit or a game server <code>Vcpu</code> value.</p> </li> </ul> <p> <b>Results:</b> </p> <p>If successful, this operation returns the complete properties of the new container group definition version.</p> <p>If the container group definition version is used in an active fleet, the update automatically initiates a new fleet deployment of the new version. You can track a fleet's deployments using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListFleetDeployments.html">ListFleetDeployments</a>.</p>

        Args:
            name: <p>A descriptive identifier for the container group definition. The name value must be unique in an Amazon Web Services Region.</p>
            game_server_container_definition: <p>An updated definition for the game server container in this group. Define a game server container only when the container group type is <code>GAME_SERVER</code>. You can pass in your container definitions as a JSON file.</p>
            support_container_definitions: <p>One or more definitions for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.</p>
            total_memory_limit_mebibytes: <p>The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual container's memory limit.</p>
            total_vcpu_limit: <p>The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share these resources. If you set vCPU reservations for individual containers, the total value must be equal to or greater than the sum of the <code>Vcpu</code> values for all containers in the group.</p> <p>For a game server container group, Amazon GameLift Servers requires either a total vCPU limit or a <code>Vcpu</code> value for the game server container. If the container group has a total vCPU limit, Amazon GameLift Servers uses this value to calculate how many game server container groups fit on an instance. If the container group doesn't have a total vCPU limit, its containers can use up to the instance's available vCPU, and Amazon GameLift Servers uses the sum of the containers' <code>Vcpu</code> values to calculate how many game server container groups fit on an instance. To remove the total vCPU limit, omit this parameter and set <code>RemoveAttributes</code> to <code>TOTAL_VCPU_LIMIT</code>.</p>
            version_description: <p>A description for this update to the container group definition. </p>
            source_version_number: <p>The container group definition version to update. The new version starts with values from the source version, and then updates values included in this request. </p>
            operating_system: <p>The platform that all containers in the group use. Containers in a group must run on the same operating system.</p> <note> <p>Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the <a href="http://aws.amazon.com/amazon-linux-2/faqs/">Amazon Linux 2 FAQs</a>. For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html"> Migrate to server SDK version 5.</a> </p> </note>
            remove_attributes: <p>If set, this update removes the container group's total vCPU limit, and the group's containers can use up to the instance's available vCPU. You can't remove the total vCPU limit from a per-instance container group. A game server container group needs either a total vCPU limit or a <code>Vcpu</code> value for the game server container. You can't set <code>TotalVcpuLimit</code> in the same request.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_container_group_definition_input.UpdateContainerGroupDefinitionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_container_group_definition_output.UpdateContainerGroupDefinitionOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_container_group_definition

            output, http_response = (
                capo_gamelift._operations.game_lift.update_container_group_definition.update_container_group_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_container_group_definition_input.UpdateContainerGroupDefinitionInput = {}
        if name is not None:
            input_["name"] = name
        if game_server_container_definition is not None:
            input_["game_server_container_definition"] = (
                game_server_container_definition
            )
        if support_container_definitions is not None:
            input_["support_container_definitions"] = support_container_definitions
        if total_memory_limit_mebibytes is not None:
            input_["total_memory_limit_mebibytes"] = total_memory_limit_mebibytes
        if total_vcpu_limit is not None:
            input_["total_vcpu_limit"] = total_vcpu_limit
        if version_description is not None:
            input_["version_description"] = version_description
        if source_version_number is not None:
            input_["source_version_number"] = source_version_number
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if remove_attributes is not None:
            input_["remove_attributes"] = remove_attributes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_fleet_attributes(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        new_game_session_protection_policy: Optional[
            "capo_gamelift.types.protection_policy.ProtectionPolicy"
        ] = None,
        resource_creation_limit_policy: Optional[
            "capo_gamelift.types.resource_creation_limit_policy.ResourceCreationLimitPolicy"
        ] = None,
        metric_groups: Optional[
            "capo_gamelift.types.metric_group_list.MetricGroupList"
        ] = None,
        anywhere_configuration: Optional[
            "capo_gamelift.types.anywhere_configuration.AnywhereConfiguration"
        ] = None,
    ) -> (
        "capo_gamelift.types.update_fleet_attributes_output.UpdateFleetAttributesOutput"
    ):
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere</p> <p>Updates a fleet's mutable attributes, such as game session protection and resource creation limits.</p> <p>To update fleet attributes, specify the fleet ID and the property values that you want to change. If successful, Amazon GameLift Servers returns the identifiers for the updated fleet.</p> <note> <p>A managed fleet's runtime environment, which depends on the fleet's Amazon Machine Image (AMI) version, can't be updated. You must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see <a href="https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html"> Security best practices for Amazon GameLift Servers</a>.</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to update attribute metadata for. You can use either the fleet ID or ARN value.</p>
            name: <p>A descriptive label that is associated with a fleet. Fleet names do not need to be unique.</p>
            description: <p>A human-readable description of a fleet.</p>
            new_game_session_protection_policy: <p>The game session protection policy to apply to all new game sessions created in this fleet. Game sessions that already exist are not affected. You can set protection for individual game sessions using <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateGameSession.html">UpdateGameSession</a> .</p> <ul> <li> <p> <b>NoProtection</b> -- The game session can be terminated during a scale-down event.</p> </li> <li> <p> <b>FullProtection</b> -- If the game session is in an <code>ACTIVE</code> status, it cannot be terminated during a scale-down event.</p> </li> </ul>
            resource_creation_limit_policy: <p>Policy settings that limit the number of game sessions an individual player can create over a span of time. </p>
            metric_groups: <p>The name of a metric group to add this fleet to. Use a metric group in Amazon CloudWatch to aggregate the metrics from multiple fleets. Provide an existing metric group name, or create a new metric group by providing a new name. A fleet can only be in one metric group at a time.</p>
            anywhere_configuration: <p>Amazon GameLift Servers Anywhere configuration options.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_fleet_attributes_input.UpdateFleetAttributesInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_fleet_attributes_output.UpdateFleetAttributesOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_fleet_attributes

            output, http_response = (
                capo_gamelift._operations.game_lift.update_fleet_attributes.update_fleet_attributes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_fleet_attributes_input.UpdateFleetAttributesInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if new_game_session_protection_policy is not None:
            input_["new_game_session_protection_policy"] = (
                new_game_session_protection_policy
            )
        if resource_creation_limit_policy is not None:
            input_["resource_creation_limit_policy"] = resource_creation_limit_policy
        if metric_groups is not None:
            input_["metric_groups"] = metric_groups
        if anywhere_configuration is not None:
            input_["anywhere_configuration"] = anywhere_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_fleet_capacity(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        desired_instances: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        min_size: Optional["capo_gamelift.types.whole_number.WholeNumber"] = None,
        max_size: Optional["capo_gamelift.types.whole_number.WholeNumber"] = None,
        location: Optional[
            "capo_gamelift.types.location_string_model.LocationStringModel"
        ] = None,
        managed_capacity_configuration: Optional[
            "capo_gamelift.types.managed_capacity_configuration.ManagedCapacityConfiguration"
        ] = None,
    ) -> "capo_gamelift.types.update_fleet_capacity_output.UpdateFleetCapacityOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Container</p> <p>Updates capacity settings for a managed EC2 fleet or managed container fleet. For these fleets, you adjust capacity by changing the number of instances in the fleet. Fleet capacity determines the number of game sessions and players that the fleet can host based on its configuration. For fleets with multiple locations, use this operation to manage capacity settings in each location individually.</p> <ul> <li> <p>Minimum/maximum size: Set hard limits on the number of Amazon EC2 instances allowed. If Amazon GameLift Servers receives a request--either through manual update or automatic scaling--it won't change the capacity to a value outside of this range.</p> </li> <li> <p>Desired capacity: As an alternative to automatic scaling, manually set the number of Amazon EC2 instances to be maintained. Before changing a fleet's desired capacity, check the maximum capacity of the fleet's Amazon EC2 instance type by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeEC2InstanceLimits.html">DescribeEC2InstanceLimits</a>.</p> </li> </ul> <p>To update capacity for a fleet's home Region, or if the fleet has no remote locations, omit the <code>Location</code> parameter. The fleet must be in <code>ACTIVE</code> status. </p> <p>To update capacity for a fleet's remote location, set the <code>Location</code> parameter to the location to update. The location must be in <code>ACTIVE</code> status.</p> <p>If successful, Amazon GameLift Servers updates the capacity settings and returns the identifiers for the updated fleet and/or location. If a requested change to desired capacity exceeds the instance type's limit, the <code>LimitExceeded</code> exception occurs. </p> <p>Updates often prompt an immediate change in fleet capacity, such as when current capacity is different than the new desired capacity or outside the new limits. In this scenario, Amazon GameLift Servers automatically initiates steps to add or remove instances in the fleet location. You can track a fleet's current capacity by calling <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html">DescribeFleetCapacity</a> or <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html">DescribeFleetLocationCapacity</a>.</p> <p> Use ManagedCapacityConfiguration with the "SCALE_TO_AND_FROM_ZERO" ZeroCapacityStrategy to enable Amazon GameLift Servers to fully manage the MinSize value, switching between 0 and 1 based on game session activity. This is ideal for eliminating compute costs during periods of no game activity. It is particularly beneficial during development when you're away from your desk, iterating on builds for extended periods, in production environments serving low-traffic locations, or for games with long, predictable downtime windows. By automatically managing capacity between 0 and 1 instances, you avoid paying for idle instances while maintaining the ability to serve game sessions when demand arrives. Note that while scale-out is triggered immediately upon receiving a game session request, actual game session availability depends on your server process startup time, so this approach works best with multi-location Fleets where cold-start latency is tolerable. With a "MANUAL" ZeroCapacityStrategy Amazon GameLift Servers will not modify Fleet MinSize values automatically and will not scale out from zero instances in response to game sessions. This is configurable per-location.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-manage-capacity.html">Scaling fleet capacity</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to update capacity settings for. You can use either the fleet ID or ARN value.</p>
            desired_instances: <p>The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.</p>
            min_size: <p>The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0. This parameter cannot be set when using a ManagedCapacityConfiguration where ZeroCapacityStrategy has a value of SCALE_TO_AND_FROM_ZERO.</p>
            max_size: <p>The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.</p>
            location: <p>The name of a remote location to update fleet capacity settings for, in the form of an Amazon Web Services Region code such as <code>us-west-2</code>.</p>
            managed_capacity_configuration: <p>Configuration for Amazon GameLift Servers-managed capacity scaling options.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_fleet_capacity_input.UpdateFleetCapacityInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_fleet_capacity_output.UpdateFleetCapacityOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_fleet_capacity

            output, http_response = (
                capo_gamelift._operations.game_lift.update_fleet_capacity.update_fleet_capacity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_fleet_capacity_input.UpdateFleetCapacityInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if desired_instances is not None:
            input_["desired_instances"] = desired_instances
        if min_size is not None:
            input_["min_size"] = min_size
        if max_size is not None:
            input_["max_size"] = max_size
        if location is not None:
            input_["location"] = location
        if managed_capacity_configuration is not None:
            input_["managed_capacity_configuration"] = managed_capacity_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_fleet_port_settings(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        inbound_permission_authorizations: Optional[
            "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
        ] = None,
        inbound_permission_revocations: Optional[
            "capo_gamelift.types.ip_permissions_list.IpPermissionsList"
        ] = None,
    ) -> "capo_gamelift.types.update_fleet_port_settings_output.UpdateFleetPortSettingsOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Updates permissions that allow inbound traffic to connect to game sessions in the fleet. </p> <p>To update settings, specify the fleet ID to be updated and specify the changes to be made. List the permissions you want to add in <code>InboundPermissionAuthorizations</code>, and permissions you want to remove in <code>InboundPermissionRevocations</code>. Permissions to be removed must match existing fleet permissions. </p> <p>If successful, the fleet identifiers for the updated fleet are returned. For fleets with remote locations, port setting updates can take time to propagate across all locations. You can check the status of updates in each location by calling <code>DescribeFleetPortSettings</code> with a location name.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to update port settings for. You can use either the fleet ID or ARN value.</p>
            inbound_permission_authorizations: <p>A collection of port settings to be added to the fleet resource.</p>
            inbound_permission_revocations: <p>A collection of port settings to be removed from the fleet resource.</p>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_fleet_port_settings_input.UpdateFleetPortSettingsInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_fleet_port_settings_output.UpdateFleetPortSettingsOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_fleet_port_settings

            output, http_response = (
                capo_gamelift._operations.game_lift.update_fleet_port_settings.update_fleet_port_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_fleet_port_settings_input.UpdateFleetPortSettingsInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if inbound_permission_authorizations is not None:
            input_["inbound_permission_authorizations"] = (
                inbound_permission_authorizations
            )
        if inbound_permission_revocations is not None:
            input_["inbound_permission_revocations"] = inbound_permission_revocations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_game_server(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        game_server_id: Optional[
            "capo_gamelift.types.game_server_id.GameServerId"
        ] = None,
        game_server_data: Optional[
            "capo_gamelift.types.game_server_data.GameServerData"
        ] = None,
        utilization_status: Optional[
            "capo_gamelift.types.game_server_utilization_status.GameServerUtilizationStatus"
        ] = None,
        health_check: Optional[
            "capo_gamelift.types.game_server_health_check.GameServerHealthCheck"
        ] = None,
    ) -> "capo_gamelift.types.update_game_server_output.UpdateGameServerOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Updates information about a registered game server to help Amazon GameLift Servers FleetIQ track game server availability. This operation is called by a game server process that is running on an instance in a game server group. </p> <p>Use this operation to update the following types of game server information. You can make all three types of updates in the same request:</p> <ul> <li> <p>To update the game server's utilization status from <code>AVAILABLE</code> (when the game server is available to be claimed) to <code>UTILIZED</code> (when the game server is currently hosting games). Identify the game server and game server group and specify the new utilization status. You can't change the status from <code>UTILIZED</code> to <code>AVAILABLE</code> .</p> </li> <li> <p>To report health status, identify the game server and game server group and set health check to <code>HEALTHY</code>. If a game server does not report health status for a certain length of time, the game server is no longer considered healthy. As a result, it will be eventually deregistered from the game server group to avoid affecting utilization metrics. The best practice is to report health every 60 seconds.</p> </li> <li> <p>To change game server metadata, provide updated game server data.</p> </li> </ul> <p>Once a game server is successfully updated, the relevant statuses and timestamps are updated.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group where the game server is running.</p>
            game_server_id: <p>A custom string that uniquely identifies the game server to update.</p>
            game_server_data: <p>A set of custom game server properties, formatted as a single string value. This data is passed to a game client or service when it requests information on game servers. </p>
            utilization_status: <p>Indicates if the game server is available or is currently hosting gameplay. You can update a game server status from <code>AVAILABLE</code> to <code>UTILIZED</code>, but you can't change the status from <code>UTILIZED</code> to <code>AVAILABLE</code>.</p>
            health_check: <p>Indicates health status of the game server. A request that includes this parameter updates the game server's <i>LastHealthCheckTime</i> timestamp. </p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_game_server_input.UpdateGameServerInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_game_server_output.UpdateGameServerOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_game_server

            output, http_response = (
                capo_gamelift._operations.game_lift.update_game_server.update_game_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_game_server_input.UpdateGameServerInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if game_server_id is not None:
            input_["game_server_id"] = game_server_id
        if game_server_data is not None:
            input_["game_server_data"] = game_server_data
        if utilization_status is not None:
            input_["utilization_status"] = utilization_status
        if health_check is not None:
            input_["health_check"] = health_check

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_game_server_group(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_server_group_name: Optional[
            "capo_gamelift.types.game_server_group_name_or_arn.GameServerGroupNameOrArn"
        ] = None,
        role_arn: Optional["capo_gamelift.types.iam_role_arn.IamRoleArn"] = None,
        instance_definitions: Optional[
            "capo_gamelift.types.instance_definitions.InstanceDefinitions"
        ] = None,
        game_server_protection_policy: Optional[
            "capo_gamelift.types.game_server_protection_policy.GameServerProtectionPolicy"
        ] = None,
        balancing_strategy: Optional[
            "capo_gamelift.types.balancing_strategy.BalancingStrategy"
        ] = None,
    ) -> "capo_gamelift.types.update_game_server_group_output.UpdateGameServerGroupOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2 (FleetIQ)</p> <p>Updates Amazon GameLift Servers FleetIQ-specific properties for a game server group. Many Auto Scaling group properties are updated on the Auto Scaling group directly, including the launch template, Auto Scaling policies, and maximum/minimum/desired instance counts.</p> <p>To update the game server group, specify the game server group ID and provide the updated values. Before applying the updates, the new values are validated to ensure that Amazon GameLift Servers FleetIQ can continue to perform instance balancing activity. If successful, a <code>GameServerGroup</code> object is returned.</p> <note> <p>Target tracking Auto Scaling policies on the Auto Scaling group cannot be updated through the Amazon Web Services Management Console. Instead, use the Amazon Elastic Compute Cloud Auto Scaling <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html"> <code>PutScalingPolicy</code> </a> API action to update these policies.</p> </note> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html">Amazon GameLift Servers FleetIQ Guide</a> </p>

        Args:
            game_server_group_name: <p>A unique identifier for the game server group. Use either the name or ARN value.</p>
            role_arn: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) for an IAM role that allows Amazon GameLift Servers to access your Amazon EC2 Auto Scaling groups.</p>
            instance_definitions: <p>An updated list of Amazon EC2 instance types to use in the Auto Scaling group. The instance definitions must specify at least two different instance types that are supported by Amazon GameLift Servers FleetIQ. This updated list replaces the entire current list of instance definitions for the game server group. For more information on instance types, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">EC2 Instance Types</a> in the <i>Amazon EC2 User Guide</i>. You can optionally specify capacity weighting for each instance type. If no weight value is specified for an instance type, it is set to the default value "1". For more information about capacity weighting, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html"> Instance Weighting for Amazon EC2 Auto Scaling</a> in the Amazon EC2 Auto Scaling User Guide.</p>
            game_server_protection_policy: <p>A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion. An exception to this is with Spot Instances, which can be terminated by Amazon Web Services regardless of protection status. This property is set to <code>NO_PROTECTION</code> by default.</p>
            balancing_strategy: <p>Indicates how Amazon GameLift Servers FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following:</p> <ul> <li> <p> <code>SPOT_ONLY</code> - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.</p> </li> <li> <p> <code>SPOT_PREFERRED</code> - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.</p> </li> <li> <p> <code>ON_DEMAND_ONLY</code> - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.</p> </li> </ul>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_game_server_group_input.UpdateGameServerGroupInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_game_server_group_output.UpdateGameServerGroupOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_game_server_group

            output, http_response = (
                capo_gamelift._operations.game_lift.update_game_server_group.update_game_server_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_game_server_group_input.UpdateGameServerGroupInput = {}
        if game_server_group_name is not None:
            input_["game_server_group_name"] = game_server_group_name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if instance_definitions is not None:
            input_["instance_definitions"] = instance_definitions
        if game_server_protection_policy is not None:
            input_["game_server_protection_policy"] = game_server_protection_policy
        if balancing_strategy is not None:
            input_["balancing_strategy"] = balancing_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_game_session(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        game_session_id: Optional[
            "capo_gamelift.types.arn_string_model.ArnStringModel"
        ] = None,
        maximum_player_session_count: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        player_session_creation_policy: Optional[
            "capo_gamelift.types.player_session_creation_policy.PlayerSessionCreationPolicy"
        ] = None,
        protection_policy: Optional[
            "capo_gamelift.types.protection_policy.ProtectionPolicy"
        ] = None,
        game_properties: Optional[
            "capo_gamelift.types.game_property_list.GamePropertyList"
        ] = None,
    ) -> "capo_gamelift.types.update_game_session_output.UpdateGameSessionOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Updates the mutable properties of a game session. </p> <p>To update a game session, specify the game session ID and the values you want to change. </p> <p>If successful, the updated <code>GameSession</code> object is returned. </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            game_session_id: <p>An identifier for the game session that is unique across all regions to update. The value is always a full ARN in the following format: For Home Region game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<ID string></code>. For Remote Location game session - <code>arn:aws:gamelift:<home_region>::gamesession/<fleet ID>/<location>/<ID string></code>.</p>
            maximum_player_session_count: <p>The maximum number of players that can be connected simultaneously to the game session.</p>
            name: <p>A descriptive label that is associated with a game session. Session names do not need to be unique.</p>
            player_session_creation_policy: <p>A policy that determines whether the game session is accepting new players.</p>
            protection_policy: <p>Game session protection policy to apply to this game session only.</p> <ul> <li> <p> <code>NoProtection</code> -- The game session can be terminated during a scale-down event.</p> </li> <li> <p> <code>FullProtection</code> -- If the game session is in an <code>ACTIVE</code> status, it cannot be terminated during a scale-down event.</p> </li> </ul>
            game_properties: <p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. You can use this parameter to modify game properties in an active game session. This action adds new properties and modifies existing properties. There is no way to delete properties. For an example, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties-update">Update the value of a game property</a>. </p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>

        Raises:
            capo_gamelift.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.</p> <p></p>
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_game_session_status_exception.InvalidGameSessionStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the game instance. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.not_ready_exception.NotReadyException: <p> The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with <a href="http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">exponential backoffs and jitter</a>. </p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_game_session_input.UpdateGameSessionInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_game_session_output.UpdateGameSessionOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_game_session

            output, http_response = (
                capo_gamelift._operations.game_lift.update_game_session.update_game_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_game_session_input.UpdateGameSessionInput = {}
        if game_session_id is not None:
            input_["game_session_id"] = game_session_id
        if maximum_player_session_count is not None:
            input_["maximum_player_session_count"] = maximum_player_session_count
        if name is not None:
            input_["name"] = name
        if player_session_creation_policy is not None:
            input_["player_session_creation_policy"] = player_session_creation_policy
        if protection_policy is not None:
            input_["protection_policy"] = protection_policy
        if game_properties is not None:
            input_["game_properties"] = game_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_game_session_queue(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
        ] = None,
        timeout_in_seconds: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        player_latency_policies: Optional[
            "capo_gamelift.types.player_latency_policy_list.PlayerLatencyPolicyList"
        ] = None,
        destinations: Optional[
            "capo_gamelift.types.game_session_queue_destination_list.GameSessionQueueDestinationList"
        ] = None,
        filter_configuration: Optional[
            "capo_gamelift.types.filter_configuration.FilterConfiguration"
        ] = None,
        priority_configuration: Optional[
            "capo_gamelift.types.priority_configuration.PriorityConfiguration"
        ] = None,
        custom_event_data: Optional[
            "capo_gamelift.types.queue_custom_event_data.QueueCustomEventData"
        ] = None,
        notification_target: Optional[
            "capo_gamelift.types.queue_sns_arn_string_model.QueueSnsArnStringModel"
        ] = None,
    ) -> "capo_gamelift.types.update_game_session_queue_output.UpdateGameSessionQueueOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Updates the configuration of a game session queue, which determines how the queue processes new game session requests. To update settings, specify the queue name to be updated and provide the new settings. When updating destinations, provide a complete list of destinations. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html"> Using Multi-Region Queues</a> </p>

        Args:
            name: <p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value. </p>
            timeout_in_seconds: <p>The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a <code>TIMED_OUT</code> status.</p> <note> <p>The minimum value is 10 and the maximum value is 600.</p> </note>
            player_latency_policies: <p>A set of policies that enforce a sliding cap on player latency when processing game sessions placement requests. Use multiple policies to gradually relax the cap over time if Amazon GameLift Servers can't make a placement. Policies are evaluated in order starting with the lowest maximum latency value. When updating policies, provide a complete collection of policies.</p>
            destinations: <p>A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference. When updating this list, provide a complete list of destinations.</p>
            filter_configuration: <p>A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of Amazon Web Services Region codes, such as <code>us-west-2</code>. If this parameter is not set, game sessions can be placed in any queue location. To remove an existing filter configuration, pass in an empty set.</p>
            priority_configuration: <p>Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process. To remove an existing priority configuration, pass in an empty set.</p>
            custom_event_data: <p>Information to be added to all events that are related to this game session queue.</p>
            notification_target: <p>An SNS topic ARN that is set up to receive game session placement notifications. See <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html"> Setting up notifications for game session placement</a>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_game_session_queue_input.UpdateGameSessionQueueInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_game_session_queue_output.UpdateGameSessionQueueOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_game_session_queue

            output, http_response = (
                capo_gamelift._operations.game_lift.update_game_session_queue.update_game_session_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_game_session_queue_input.UpdateGameSessionQueueInput = {}
        if name is not None:
            input_["name"] = name
        if timeout_in_seconds is not None:
            input_["timeout_in_seconds"] = timeout_in_seconds
        if player_latency_policies is not None:
            input_["player_latency_policies"] = player_latency_policies
        if destinations is not None:
            input_["destinations"] = destinations
        if filter_configuration is not None:
            input_["filter_configuration"] = filter_configuration
        if priority_configuration is not None:
            input_["priority_configuration"] = priority_configuration
        if custom_event_data is not None:
            input_["custom_event_data"] = custom_event_data
        if notification_target is not None:
            input_["notification_target"] = notification_target

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_matchmaking_configuration(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        name: Optional[
            "capo_gamelift.types.matchmaking_configuration_name.MatchmakingConfigurationName"
        ] = None,
        description: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        game_session_queue_arns: Optional[
            "capo_gamelift.types.queue_arns_list.QueueArnsList"
        ] = None,
        request_timeout_seconds: Optional[
            "capo_gamelift.types.matchmaking_request_timeout_integer.MatchmakingRequestTimeoutInteger"
        ] = None,
        acceptance_timeout_seconds: Optional[
            "capo_gamelift.types.matchmaking_acceptance_timeout_integer.MatchmakingAcceptanceTimeoutInteger"
        ] = None,
        acceptance_required: Optional[
            "capo_gamelift.types.boolean_model.BooleanModel"
        ] = None,
        rule_set_name: Optional[
            "capo_gamelift.types.matchmaking_rule_set_name.MatchmakingRuleSetName"
        ] = None,
        notification_target: Optional[
            "capo_gamelift.types.sns_arn_string_model.SnsArnStringModel"
        ] = None,
        additional_player_count: Optional[
            "capo_gamelift.types.whole_number.WholeNumber"
        ] = None,
        custom_event_data: Optional[
            "capo_gamelift.types.custom_event_data.CustomEventData"
        ] = None,
        game_properties: Optional[
            "capo_gamelift.types.game_property_list.GamePropertyList"
        ] = None,
        game_session_data: Optional[
            "capo_gamelift.types.game_session_data.GameSessionData"
        ] = None,
        backfill_mode: Optional[
            "capo_gamelift.types.backfill_mode.BackfillMode"
        ] = None,
        flex_match_mode: Optional[
            "capo_gamelift.types.flex_match_mode.FlexMatchMode"
        ] = None,
    ) -> "capo_gamelift.types.update_matchmaking_configuration_output.UpdateMatchmakingConfigurationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Updates settings for a FlexMatch matchmaking configuration. These changes affect all matches and game sessions that are created after the update. To update settings, specify the configuration name to be updated and provide the new settings. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html"> Design a FlexMatch matchmaker</a> </p>

        Args:
            name: <p>A unique identifier for the matchmaking configuration to update. You can use either the configuration name or ARN value. </p>
            description: <p>A description for the matchmaking configuration.</p>
            game_session_queue_arns: <p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html">ARN</a>) that is assigned to a Amazon GameLift Servers game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is <code>arn:aws:gamelift:<region>::gamesessionqueue/<queue name></code>. Queues can be located in any Region. Queues are used to start new Amazon GameLift Servers-hosted game sessions for matches that are created with this matchmaking configuration. A matchmaking configuration supports only one queue; if you specify more than one ARN, the request fails with an <code>InvalidRequestException</code>. If <code>FlexMatchMode</code> is set to <code>STANDALONE</code>, do not set this parameter.</p>
            request_timeout_seconds: <p>The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.</p>
            acceptance_timeout_seconds: <p>The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.</p>
            acceptance_required: <p>A flag that indicates whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to TRUE. With this option enabled, matchmaking tickets use the status <code>REQUIRES_ACCEPTANCE</code> to indicate when a completed potential match is waiting for player acceptance. </p>
            rule_set_name: <p>A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.</p>
            notification_target: <p>An SNS topic ARN that is set up to receive matchmaking notifications. See <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html"> Setting up notifications for matchmaking</a> for more information.</p>
            additional_player_count: <p>The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 12-person team, and the additional player count is set to 2, only 10 players are selected for the match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>
            custom_event_data: <p>Information to add to all events related to the matchmaking configuration. </p>
            game_properties: <p>A set of key-value pairs that can store custom data in a game session. For example: <code>{"Key": "difficulty", "Value": "novice"}</code>. This information is added to the new <code>GameSession</code> object that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>
            game_session_data: <p>A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. For more information, see <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession">Start a game session</a>. This information is added to the game session that is created for a successful match. This parameter is not used if <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>
            backfill_mode: <p>The method that is used to backfill game sessions created with this matchmaking configuration. Specify MANUAL when your game manages backfill requests manually or does not use the match backfill feature. Specify AUTOMATIC to have GameLift create a match backfill request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html">Backfill Existing Games with FlexMatch</a>. Automatic backfill is not available when <code>FlexMatchMode</code> is set to <code>STANDALONE</code>.</p>
            flex_match_mode: <p>Indicates whether this matchmaking configuration is being used with Amazon GameLift Servers hosting or as a standalone matchmaking solution. </p> <ul> <li> <p> <b>STANDALONE</b> - FlexMatch forms matches and returns match information, including players and team assignments, in a <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded"> MatchmakingSucceeded</a> event.</p> </li> <li> <p> <b>WITH_QUEUE</b> - FlexMatch forms matches and uses the specified Amazon GameLift Servers queue to start a game session for the match. </p> </li> </ul>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_matchmaking_configuration_input.UpdateMatchmakingConfigurationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_matchmaking_configuration_output.UpdateMatchmakingConfigurationOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_matchmaking_configuration

            output, http_response = (
                capo_gamelift._operations.game_lift.update_matchmaking_configuration.update_matchmaking_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_matchmaking_configuration_input.UpdateMatchmakingConfigurationInput = {}
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if game_session_queue_arns is not None:
            input_["game_session_queue_arns"] = game_session_queue_arns
        if request_timeout_seconds is not None:
            input_["request_timeout_seconds"] = request_timeout_seconds
        if acceptance_timeout_seconds is not None:
            input_["acceptance_timeout_seconds"] = acceptance_timeout_seconds
        if acceptance_required is not None:
            input_["acceptance_required"] = acceptance_required
        if rule_set_name is not None:
            input_["rule_set_name"] = rule_set_name
        if notification_target is not None:
            input_["notification_target"] = notification_target
        if additional_player_count is not None:
            input_["additional_player_count"] = additional_player_count
        if custom_event_data is not None:
            input_["custom_event_data"] = custom_event_data
        if game_properties is not None:
            input_["game_properties"] = game_properties
        if game_session_data is not None:
            input_["game_session_data"] = game_session_data
        if backfill_mode is not None:
            input_["backfill_mode"] = backfill_mode
        if flex_match_mode is not None:
            input_["flex_match_mode"] = flex_match_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_runtime_configuration(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        fleet_id: Optional["capo_gamelift.types.fleet_id_or_arn.FleetIdOrArn"] = None,
        runtime_configuration: Optional[
            "capo_gamelift.types.runtime_configuration.RuntimeConfiguration"
        ] = None,
    ) -> "capo_gamelift.types.update_runtime_configuration_output.UpdateRuntimeConfigurationOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Updates the runtime configuration for the specified fleet. The runtime configuration tells Amazon GameLift Servers how to launch server processes on computes in managed EC2 and Anywhere fleets. You can update a fleet's runtime configuration at any time after the fleet is created; it does not need to be in <code>ACTIVE</code> status.</p> <p>To update runtime configuration, specify the fleet ID and provide a <code>RuntimeConfiguration</code> with an updated set of server process configurations.</p> <p>If successful, the fleet's runtime configuration settings are updated. Fleet computes that run game server processes regularly check for and receive updated runtime configurations. The computes immediately take action to comply with the new configuration by launching new server processes or by not replacing existing processes when they shut down. Updating a fleet's runtime configuration never affects existing server processes.</p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html">Setting up Amazon GameLift Servers fleets</a> </p>

        Args:
            fleet_id: <p>A unique identifier for the fleet to update runtime configuration for. You can use either the fleet ID or ARN value.</p>
            runtime_configuration: <p>Instructions for launching server processes on fleet computes. Server processes run either a custom game build executable or a Amazon GameLift Servers Realtime script. The runtime configuration lists the types of server processes to run, how to launch them, and the number of processes to run concurrently.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_fleet_status_exception.InvalidFleetStatusException: <p>The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.limit_exceeded_exception.LimitExceededException: <p>The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_runtime_configuration_input.UpdateRuntimeConfigurationInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_runtime_configuration_output.UpdateRuntimeConfigurationOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_runtime_configuration

            output, http_response = (
                capo_gamelift._operations.game_lift.update_runtime_configuration.update_runtime_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_runtime_configuration_input.UpdateRuntimeConfigurationInput = {}
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id
        if runtime_configuration is not None:
            input_["runtime_configuration"] = runtime_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_script(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        script_id: Optional[
            "capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"
        ] = None,
        name: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        version: Optional[
            "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
        ] = None,
        storage_location: Optional["capo_gamelift.types.s3_location.S3Location"] = None,
        zip_file: Optional["capo_gamelift.types.zip_blob.ZipBlob"] = None,
    ) -> "capo_gamelift.types.update_script_output.UpdateScriptOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2</p> <p>Updates Realtime script metadata and content.</p> <p>To update script metadata, specify the script ID and provide updated name and/or version values. </p> <p>To update script content, provide an updated zip file by pointing to either a local file or an Amazon S3 bucket location. You can use either method regardless of how the original script was uploaded. Use the <i>Version</i> parameter to track updates to the script.</p> <p>If the call is successful, the updated metadata is stored in the script record and a revised script is uploaded to the Amazon GameLift Servers service. Once the script is updated and acquired by a fleet instance, the new version is used for all new game sessions. </p> <p> <b>Learn more</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/realtime-intro.html">Amazon GameLift Servers Amazon GameLift Servers Realtime</a> </p> <p> <b>Related actions</b> </p> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets">All APIs by task</a> </p>

        Args:
            script_id: <p>A unique identifier for the Realtime script to update. You can use either the script ID or ARN value.</p>
            name: <p>A descriptive label that is associated with a script. Script names do not need to be unique.</p>
            version: <p>Version information that is associated with a build or script. Version strings do not need to be unique.</p>
            storage_location: <p>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the <code>ObjectVersion</code> parameter to specify an earlier version. </p>
            zip_file: <p>A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.</p> <p>When using the Amazon Web Services CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: <code>--zip-file fileb://myRealtimeScript.zip</code>.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.not_found_exception.NotFoundException: <p>The requested resource was not found. The resource was either not created yet or deleted.</p>
            capo_gamelift.errors.unauthorized_exception.UnauthorizedException: <p>The client failed authentication. Clients should not retry such requests.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.update_script_input.UpdateScriptInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.update_script_output.UpdateScriptOutput"
        ]:
            import capo_gamelift._operations.game_lift.update_script

            output, http_response = (
                capo_gamelift._operations.game_lift.update_script.update_script(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.update_script_input.UpdateScriptInput = {}
        if script_id is not None:
            input_["script_id"] = script_id
        if name is not None:
            input_["name"] = name
        if version is not None:
            input_["version"] = version
        if storage_location is not None:
            input_["storage_location"] = storage_location
        if zip_file is not None:
            input_["zip_file"] = zip_file

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_matchmaking_rule_set(
        self,
        *,
        config_overrides: Optional[GameLiftClientConfig] = None,
        rule_set_body: Optional["capo_gamelift.types.rule_set_body.RuleSetBody"] = None,
    ) -> "capo_gamelift.types.validate_matchmaking_rule_set_output.ValidateMatchmakingRuleSetOutput":
        """<p> <b>This API works with the following fleet types:</b> EC2, Anywhere, Container</p> <p>Validates the syntax of a matchmaking rule or rule set. This operation checks that the rule set is using syntactically correct JSON and that it conforms to allowed property expressions. To validate syntax, provide a rule set JSON string.</p> <p> <b>Learn more</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html">Build a rule set</a> </p> </li> </ul>

        Args:
            rule_set_body: <p>A collection of matchmaking rules to validate, formatted as a JSON string.</p>

        Raises:
            capo_gamelift.errors.internal_service_exception.InternalServiceException: <p>The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.</p>
            capo_gamelift.errors.invalid_request_exception.InvalidRequestException: <p>One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.</p>
            capo_gamelift.errors.unsupported_region_exception.UnsupportedRegionException: <p>The requested operation is not supported in the Region specified.</p>
            capo_gamelift.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_gamelift.types.validate_matchmaking_rule_set_input.ValidateMatchmakingRuleSetInput]",
        ) -> OperationResponse[
            "capo_gamelift.types.validate_matchmaking_rule_set_output.ValidateMatchmakingRuleSetOutput"
        ]:
            import capo_gamelift._operations.game_lift.validate_matchmaking_rule_set

            output, http_response = (
                capo_gamelift._operations.game_lift.validate_matchmaking_rule_set.validate_matchmaking_rule_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_gamelift.types.validate_matchmaking_rule_set_input.ValidateMatchmakingRuleSetInput = {}
        if rule_set_body is not None:
            input_["rule_set_body"] = rule_set_body

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
