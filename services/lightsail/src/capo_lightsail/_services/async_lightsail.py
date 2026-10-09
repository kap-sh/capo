"""Generated from Smithy shape ``com.amazonaws.lightsail#Lightsail_20161128``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lightsail._auth._signers
import capo_lightsail._auth._sigv4
from capo_lightsail._auth._identity import Credentials
from capo_lightsail._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lightsail._auth._zapros_handler import AuthMiddleware
from capo_lightsail._services._aws_config import aaws_config
from capo_lightsail._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_lightsail.types.access_rules
    import capo_lightsail.types.add_on_request
    import capo_lightsail.types.add_on_request_list
    import capo_lightsail.types.add_on_type
    import capo_lightsail.types.alarm_state
    import capo_lightsail.types.allocate_static_ip_request
    import capo_lightsail.types.allocate_static_ip_result
    import capo_lightsail.types.app_category
    import capo_lightsail.types.attach_certificate_to_distribution_request
    import capo_lightsail.types.attach_certificate_to_distribution_result
    import capo_lightsail.types.attach_disk_request
    import capo_lightsail.types.attach_disk_result
    import capo_lightsail.types.attach_instances_to_load_balancer_request
    import capo_lightsail.types.attach_instances_to_load_balancer_result
    import capo_lightsail.types.attach_load_balancer_tls_certificate_request
    import capo_lightsail.types.attach_load_balancer_tls_certificate_result
    import capo_lightsail.types.attach_static_ip_request
    import capo_lightsail.types.attach_static_ip_result
    import capo_lightsail.types.attached_disk_map
    import capo_lightsail.types.auto_snapshot_date
    import capo_lightsail.types.base64
    import capo_lightsail.types.boolean
    import capo_lightsail.types.bucket_access_log_config
    import capo_lightsail.types.bucket_cors_config
    import capo_lightsail.types.bucket_metric_name
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.cache_behavior
    import capo_lightsail.types.cache_behavior_list
    import capo_lightsail.types.cache_settings
    import capo_lightsail.types.certificate_name
    import capo_lightsail.types.certificate_provider
    import capo_lightsail.types.certificate_status_list
    import capo_lightsail.types.close_instance_public_ports_request
    import capo_lightsail.types.close_instance_public_ports_result
    import capo_lightsail.types.comparison_operator
    import capo_lightsail.types.contact_method_verification_protocol
    import capo_lightsail.types.contact_protocol
    import capo_lightsail.types.contact_protocols_list
    import capo_lightsail.types.container_label
    import capo_lightsail.types.container_map
    import capo_lightsail.types.container_service_deployment_request
    import capo_lightsail.types.container_service_metric_name
    import capo_lightsail.types.container_service_name
    import capo_lightsail.types.container_service_power_name
    import capo_lightsail.types.container_service_public_domains
    import capo_lightsail.types.container_service_scale
    import capo_lightsail.types.container_services_list_result
    import capo_lightsail.types.copy_snapshot_request
    import capo_lightsail.types.copy_snapshot_result
    import capo_lightsail.types.create_bucket_access_key_request
    import capo_lightsail.types.create_bucket_access_key_result
    import capo_lightsail.types.create_bucket_request
    import capo_lightsail.types.create_bucket_result
    import capo_lightsail.types.create_certificate_request
    import capo_lightsail.types.create_certificate_result
    import capo_lightsail.types.create_cloud_formation_stack_request
    import capo_lightsail.types.create_cloud_formation_stack_result
    import capo_lightsail.types.create_contact_method_request
    import capo_lightsail.types.create_contact_method_result
    import capo_lightsail.types.create_container_service_deployment_request
    import capo_lightsail.types.create_container_service_deployment_result
    import capo_lightsail.types.create_container_service_registry_login_request
    import capo_lightsail.types.create_container_service_registry_login_result
    import capo_lightsail.types.create_container_service_request
    import capo_lightsail.types.create_container_service_result
    import capo_lightsail.types.create_disk_from_snapshot_request
    import capo_lightsail.types.create_disk_from_snapshot_result
    import capo_lightsail.types.create_disk_request
    import capo_lightsail.types.create_disk_result
    import capo_lightsail.types.create_disk_snapshot_request
    import capo_lightsail.types.create_disk_snapshot_result
    import capo_lightsail.types.create_distribution_request
    import capo_lightsail.types.create_distribution_result
    import capo_lightsail.types.create_domain_entry_request
    import capo_lightsail.types.create_domain_entry_result
    import capo_lightsail.types.create_domain_request
    import capo_lightsail.types.create_domain_result
    import capo_lightsail.types.create_gui_session_access_details_request
    import capo_lightsail.types.create_gui_session_access_details_result
    import capo_lightsail.types.create_instance_snapshot_request
    import capo_lightsail.types.create_instance_snapshot_result
    import capo_lightsail.types.create_instances_from_snapshot_request
    import capo_lightsail.types.create_instances_from_snapshot_result
    import capo_lightsail.types.create_instances_request
    import capo_lightsail.types.create_instances_result
    import capo_lightsail.types.create_key_pair_request
    import capo_lightsail.types.create_key_pair_result
    import capo_lightsail.types.create_load_balancer_request
    import capo_lightsail.types.create_load_balancer_result
    import capo_lightsail.types.create_load_balancer_tls_certificate_request
    import capo_lightsail.types.create_load_balancer_tls_certificate_result
    import capo_lightsail.types.create_relational_database_from_snapshot_request
    import capo_lightsail.types.create_relational_database_from_snapshot_result
    import capo_lightsail.types.create_relational_database_request
    import capo_lightsail.types.create_relational_database_result
    import capo_lightsail.types.create_relational_database_snapshot_request
    import capo_lightsail.types.create_relational_database_snapshot_result
    import capo_lightsail.types.delete_alarm_request
    import capo_lightsail.types.delete_alarm_result
    import capo_lightsail.types.delete_auto_snapshot_request
    import capo_lightsail.types.delete_auto_snapshot_result
    import capo_lightsail.types.delete_bucket_access_key_request
    import capo_lightsail.types.delete_bucket_access_key_result
    import capo_lightsail.types.delete_bucket_request
    import capo_lightsail.types.delete_bucket_result
    import capo_lightsail.types.delete_certificate_request
    import capo_lightsail.types.delete_certificate_result
    import capo_lightsail.types.delete_contact_method_request
    import capo_lightsail.types.delete_contact_method_result
    import capo_lightsail.types.delete_container_image_request
    import capo_lightsail.types.delete_container_image_result
    import capo_lightsail.types.delete_container_service_request
    import capo_lightsail.types.delete_container_service_result
    import capo_lightsail.types.delete_disk_request
    import capo_lightsail.types.delete_disk_result
    import capo_lightsail.types.delete_disk_snapshot_request
    import capo_lightsail.types.delete_disk_snapshot_result
    import capo_lightsail.types.delete_distribution_request
    import capo_lightsail.types.delete_distribution_result
    import capo_lightsail.types.delete_domain_entry_request
    import capo_lightsail.types.delete_domain_entry_result
    import capo_lightsail.types.delete_domain_request
    import capo_lightsail.types.delete_domain_result
    import capo_lightsail.types.delete_instance_request
    import capo_lightsail.types.delete_instance_result
    import capo_lightsail.types.delete_instance_snapshot_request
    import capo_lightsail.types.delete_instance_snapshot_result
    import capo_lightsail.types.delete_key_pair_request
    import capo_lightsail.types.delete_key_pair_result
    import capo_lightsail.types.delete_known_host_keys_request
    import capo_lightsail.types.delete_known_host_keys_result
    import capo_lightsail.types.delete_load_balancer_request
    import capo_lightsail.types.delete_load_balancer_result
    import capo_lightsail.types.delete_load_balancer_tls_certificate_request
    import capo_lightsail.types.delete_load_balancer_tls_certificate_result
    import capo_lightsail.types.delete_relational_database_request
    import capo_lightsail.types.delete_relational_database_result
    import capo_lightsail.types.delete_relational_database_snapshot_request
    import capo_lightsail.types.delete_relational_database_snapshot_result
    import capo_lightsail.types.detach_certificate_from_distribution_request
    import capo_lightsail.types.detach_certificate_from_distribution_result
    import capo_lightsail.types.detach_disk_request
    import capo_lightsail.types.detach_disk_result
    import capo_lightsail.types.detach_instances_from_load_balancer_request
    import capo_lightsail.types.detach_instances_from_load_balancer_result
    import capo_lightsail.types.detach_static_ip_request
    import capo_lightsail.types.detach_static_ip_result
    import capo_lightsail.types.disable_add_on_request
    import capo_lightsail.types.disable_add_on_result
    import capo_lightsail.types.distribution_custom_error_response_list
    import capo_lightsail.types.distribution_metric_name
    import capo_lightsail.types.domain_entry
    import capo_lightsail.types.domain_name
    import capo_lightsail.types.domain_name_list
    import capo_lightsail.types.double
    import capo_lightsail.types.download_default_key_pair_request
    import capo_lightsail.types.download_default_key_pair_result
    import capo_lightsail.types.email_address
    import capo_lightsail.types.enable_add_on_request
    import capo_lightsail.types.enable_add_on_result
    import capo_lightsail.types.endpoint_request
    import capo_lightsail.types.export_snapshot_request
    import capo_lightsail.types.export_snapshot_result
    import capo_lightsail.types.get_active_names_request
    import capo_lightsail.types.get_active_names_result
    import capo_lightsail.types.get_alarms_request
    import capo_lightsail.types.get_alarms_result
    import capo_lightsail.types.get_auto_snapshots_request
    import capo_lightsail.types.get_auto_snapshots_result
    import capo_lightsail.types.get_blueprints_request
    import capo_lightsail.types.get_blueprints_result
    import capo_lightsail.types.get_bucket_access_keys_request
    import capo_lightsail.types.get_bucket_access_keys_result
    import capo_lightsail.types.get_bucket_bundles_request
    import capo_lightsail.types.get_bucket_bundles_result
    import capo_lightsail.types.get_bucket_metric_data_request
    import capo_lightsail.types.get_bucket_metric_data_result
    import capo_lightsail.types.get_buckets_request
    import capo_lightsail.types.get_buckets_result
    import capo_lightsail.types.get_bundles_request
    import capo_lightsail.types.get_bundles_result
    import capo_lightsail.types.get_certificates_request
    import capo_lightsail.types.get_certificates_result
    import capo_lightsail.types.get_cloud_formation_stack_records_request
    import capo_lightsail.types.get_cloud_formation_stack_records_result
    import capo_lightsail.types.get_contact_methods_request
    import capo_lightsail.types.get_contact_methods_result
    import capo_lightsail.types.get_container_api_metadata_request
    import capo_lightsail.types.get_container_api_metadata_result
    import capo_lightsail.types.get_container_images_request
    import capo_lightsail.types.get_container_images_result
    import capo_lightsail.types.get_container_log_request
    import capo_lightsail.types.get_container_log_result
    import capo_lightsail.types.get_container_service_deployments_request
    import capo_lightsail.types.get_container_service_deployments_result
    import capo_lightsail.types.get_container_service_metric_data_request
    import capo_lightsail.types.get_container_service_metric_data_result
    import capo_lightsail.types.get_container_service_powers_request
    import capo_lightsail.types.get_container_service_powers_result
    import capo_lightsail.types.get_container_services_request
    import capo_lightsail.types.get_cost_estimate_request
    import capo_lightsail.types.get_cost_estimate_result
    import capo_lightsail.types.get_disk_request
    import capo_lightsail.types.get_disk_result
    import capo_lightsail.types.get_disk_snapshot_request
    import capo_lightsail.types.get_disk_snapshot_result
    import capo_lightsail.types.get_disk_snapshots_request
    import capo_lightsail.types.get_disk_snapshots_result
    import capo_lightsail.types.get_disks_request
    import capo_lightsail.types.get_disks_result
    import capo_lightsail.types.get_distribution_bundles_request
    import capo_lightsail.types.get_distribution_bundles_result
    import capo_lightsail.types.get_distribution_latest_cache_reset_request
    import capo_lightsail.types.get_distribution_latest_cache_reset_result
    import capo_lightsail.types.get_distribution_metric_data_request
    import capo_lightsail.types.get_distribution_metric_data_result
    import capo_lightsail.types.get_distributions_request
    import capo_lightsail.types.get_distributions_result
    import capo_lightsail.types.get_domain_request
    import capo_lightsail.types.get_domain_result
    import capo_lightsail.types.get_domains_request
    import capo_lightsail.types.get_domains_result
    import capo_lightsail.types.get_export_snapshot_records_request
    import capo_lightsail.types.get_export_snapshot_records_result
    import capo_lightsail.types.get_instance_access_details_request
    import capo_lightsail.types.get_instance_access_details_result
    import capo_lightsail.types.get_instance_metric_data_request
    import capo_lightsail.types.get_instance_metric_data_result
    import capo_lightsail.types.get_instance_port_states_request
    import capo_lightsail.types.get_instance_port_states_result
    import capo_lightsail.types.get_instance_request
    import capo_lightsail.types.get_instance_result
    import capo_lightsail.types.get_instance_snapshot_request
    import capo_lightsail.types.get_instance_snapshot_result
    import capo_lightsail.types.get_instance_snapshots_request
    import capo_lightsail.types.get_instance_snapshots_result
    import capo_lightsail.types.get_instance_state_request
    import capo_lightsail.types.get_instance_state_result
    import capo_lightsail.types.get_instances_request
    import capo_lightsail.types.get_instances_result
    import capo_lightsail.types.get_key_pair_request
    import capo_lightsail.types.get_key_pair_result
    import capo_lightsail.types.get_key_pairs_request
    import capo_lightsail.types.get_key_pairs_result
    import capo_lightsail.types.get_load_balancer_metric_data_request
    import capo_lightsail.types.get_load_balancer_metric_data_result
    import capo_lightsail.types.get_load_balancer_request
    import capo_lightsail.types.get_load_balancer_result
    import capo_lightsail.types.get_load_balancer_tls_certificates_request
    import capo_lightsail.types.get_load_balancer_tls_certificates_result
    import capo_lightsail.types.get_load_balancer_tls_policies_request
    import capo_lightsail.types.get_load_balancer_tls_policies_result
    import capo_lightsail.types.get_load_balancers_request
    import capo_lightsail.types.get_load_balancers_result
    import capo_lightsail.types.get_operation_request
    import capo_lightsail.types.get_operation_result
    import capo_lightsail.types.get_operations_for_resource_request
    import capo_lightsail.types.get_operations_for_resource_result
    import capo_lightsail.types.get_operations_request
    import capo_lightsail.types.get_operations_result
    import capo_lightsail.types.get_profile_request
    import capo_lightsail.types.get_profile_result
    import capo_lightsail.types.get_regions_request
    import capo_lightsail.types.get_regions_result
    import capo_lightsail.types.get_relational_database_blueprints_request
    import capo_lightsail.types.get_relational_database_blueprints_result
    import capo_lightsail.types.get_relational_database_bundles_request
    import capo_lightsail.types.get_relational_database_bundles_result
    import capo_lightsail.types.get_relational_database_events_request
    import capo_lightsail.types.get_relational_database_events_result
    import capo_lightsail.types.get_relational_database_log_events_request
    import capo_lightsail.types.get_relational_database_log_events_result
    import capo_lightsail.types.get_relational_database_log_streams_request
    import capo_lightsail.types.get_relational_database_log_streams_result
    import capo_lightsail.types.get_relational_database_master_user_password_request
    import capo_lightsail.types.get_relational_database_master_user_password_result
    import capo_lightsail.types.get_relational_database_metric_data_request
    import capo_lightsail.types.get_relational_database_metric_data_result
    import capo_lightsail.types.get_relational_database_parameters_request
    import capo_lightsail.types.get_relational_database_parameters_result
    import capo_lightsail.types.get_relational_database_request
    import capo_lightsail.types.get_relational_database_result
    import capo_lightsail.types.get_relational_database_snapshot_request
    import capo_lightsail.types.get_relational_database_snapshot_result
    import capo_lightsail.types.get_relational_database_snapshots_request
    import capo_lightsail.types.get_relational_database_snapshots_result
    import capo_lightsail.types.get_relational_databases_request
    import capo_lightsail.types.get_relational_databases_result
    import capo_lightsail.types.get_setup_history_request
    import capo_lightsail.types.get_setup_history_result
    import capo_lightsail.types.get_static_ip_request
    import capo_lightsail.types.get_static_ip_result
    import capo_lightsail.types.get_static_ips_request
    import capo_lightsail.types.get_static_ips_result
    import capo_lightsail.types.http_endpoint
    import capo_lightsail.types.http_protocol_ipv6
    import capo_lightsail.types.http_tokens
    import capo_lightsail.types.import_key_pair_request
    import capo_lightsail.types.import_key_pair_result
    import capo_lightsail.types.include_certificate_details
    import capo_lightsail.types.input_origin
    import capo_lightsail.types.instance_access_protocol
    import capo_lightsail.types.instance_entry_list
    import capo_lightsail.types.instance_metric_name
    import capo_lightsail.types.integer
    import capo_lightsail.types.ip_address_type
    import capo_lightsail.types.is_vpc_peered_request
    import capo_lightsail.types.is_vpc_peered_result
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.load_balancer_attribute_name
    import capo_lightsail.types.load_balancer_metric_name
    import capo_lightsail.types.metric_name
    import capo_lightsail.types.metric_period
    import capo_lightsail.types.metric_statistic_list
    import capo_lightsail.types.metric_unit
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.notification_trigger_list
    import capo_lightsail.types.open_instance_public_ports_request
    import capo_lightsail.types.open_instance_public_ports_result
    import capo_lightsail.types.partner_id_list
    import capo_lightsail.types.peer_vpc_request
    import capo_lightsail.types.peer_vpc_result
    import capo_lightsail.types.port
    import capo_lightsail.types.port_info
    import capo_lightsail.types.port_info_list
    import capo_lightsail.types.private_registry_access_request
    import capo_lightsail.types.put_alarm_request
    import capo_lightsail.types.put_alarm_result
    import capo_lightsail.types.put_instance_public_ports_request
    import capo_lightsail.types.put_instance_public_ports_result
    import capo_lightsail.types.reboot_instance_request
    import capo_lightsail.types.reboot_instance_result
    import capo_lightsail.types.reboot_relational_database_request
    import capo_lightsail.types.reboot_relational_database_result
    import capo_lightsail.types.region_name
    import capo_lightsail.types.register_container_image_request
    import capo_lightsail.types.register_container_image_result
    import capo_lightsail.types.relational_database_metric_name
    import capo_lightsail.types.relational_database_parameter_list
    import capo_lightsail.types.relational_database_password_version
    import capo_lightsail.types.release_static_ip_request
    import capo_lightsail.types.release_static_ip_result
    import capo_lightsail.types.reset_distribution_cache_request
    import capo_lightsail.types.reset_distribution_cache_result
    import capo_lightsail.types.resource_arn
    import capo_lightsail.types.resource_bucket_access
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.resource_name_list
    import capo_lightsail.types.resource_type
    import capo_lightsail.types.send_contact_method_verification_request
    import capo_lightsail.types.send_contact_method_verification_result
    import capo_lightsail.types.sensitive_string
    import capo_lightsail.types.set_ip_address_type_request
    import capo_lightsail.types.set_ip_address_type_result
    import capo_lightsail.types.set_resource_access_for_bucket_request
    import capo_lightsail.types.set_resource_access_for_bucket_result
    import capo_lightsail.types.setup_domain_name_list
    import capo_lightsail.types.setup_history_page_token
    import capo_lightsail.types.setup_instance_https_request
    import capo_lightsail.types.setup_instance_https_result
    import capo_lightsail.types.start_gui_session_request
    import capo_lightsail.types.start_gui_session_result
    import capo_lightsail.types.start_instance_request
    import capo_lightsail.types.start_instance_result
    import capo_lightsail.types.start_relational_database_request
    import capo_lightsail.types.start_relational_database_result
    import capo_lightsail.types.stop_gui_session_request
    import capo_lightsail.types.stop_gui_session_result
    import capo_lightsail.types.stop_instance_request
    import capo_lightsail.types.stop_instance_result
    import capo_lightsail.types.stop_relational_database_request
    import capo_lightsail.types.stop_relational_database_result
    import capo_lightsail.types.string
    import capo_lightsail.types.string_list
    import capo_lightsail.types.string_max256
    import capo_lightsail.types.subject_alternative_name_list
    import capo_lightsail.types.tag_key_list
    import capo_lightsail.types.tag_list
    import capo_lightsail.types.tag_resource_request
    import capo_lightsail.types.tag_resource_result
    import capo_lightsail.types.test_alarm_request
    import capo_lightsail.types.test_alarm_result
    import capo_lightsail.types.timestamp
    import capo_lightsail.types.treat_missing_data
    import capo_lightsail.types.unpeer_vpc_request
    import capo_lightsail.types.unpeer_vpc_result
    import capo_lightsail.types.untag_resource_request
    import capo_lightsail.types.untag_resource_result
    import capo_lightsail.types.update_bucket_bundle_request
    import capo_lightsail.types.update_bucket_bundle_result
    import capo_lightsail.types.update_bucket_request
    import capo_lightsail.types.update_bucket_result
    import capo_lightsail.types.update_container_service_request
    import capo_lightsail.types.update_container_service_result
    import capo_lightsail.types.update_distribution_bundle_request
    import capo_lightsail.types.update_distribution_bundle_result
    import capo_lightsail.types.update_distribution_request
    import capo_lightsail.types.update_distribution_result
    import capo_lightsail.types.update_domain_entry_request
    import capo_lightsail.types.update_domain_entry_result
    import capo_lightsail.types.update_instance_metadata_options_request
    import capo_lightsail.types.update_instance_metadata_options_result
    import capo_lightsail.types.update_load_balancer_attribute_request
    import capo_lightsail.types.update_load_balancer_attribute_result
    import capo_lightsail.types.update_relational_database_parameters_request
    import capo_lightsail.types.update_relational_database_parameters_result
    import capo_lightsail.types.update_relational_database_request
    import capo_lightsail.types.update_relational_database_result
    import capo_lightsail.types.viewer_minimum_tls_protocol_version_enum


class AsyncLightsailClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncLightsailClient:
    """A client for the ``Lightsail`` service.

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
        self._config = AsyncLightsailClientConfig(
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
        self, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLightsailClientConfig = config_overrides or {}
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

    async def allocate_static_ip(
        self,
        static_ip_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.allocate_static_ip_result.AllocateStaticIpResult":
        """<p>Allocates a static IP address.</p>

        Args:
            static_ip_name: <p>The name of the static IP address.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.allocate_static_ip_request.AllocateStaticIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.allocate_static_ip_result.AllocateStaticIpResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.allocate_static_ip

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.allocate_static_ip.async_allocate_static_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.allocate_static_ip_request.AllocateStaticIpRequest = {
            "static_ip_name": static_ip_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def attach_certificate_to_distribution(
        self,
        distribution_name: "capo_lightsail.types.resource_name.ResourceName",
        certificate_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.attach_certificate_to_distribution_result.AttachCertificateToDistributionResult":
        """<p>Attaches an SSL/TLS certificate to your Amazon Lightsail content delivery network (CDN) distribution.</p> <p>After the certificate is attached, your distribution accepts HTTPS traffic for all of the domains that are associated with the certificate.</p> <p>Use the <code>CreateCertificate</code> action to create a certificate that you can attach to your distribution.</p> <important> <p>Only certificates created in the <code>us-east-1</code> Amazon Web Services Region can be attached to Lightsail distributions. Lightsail distributions are global resources that can reference an origin in any Amazon Web Services Region, and distribute its content globally. However, all distributions are located in the <code>us-east-1</code> Region.</p> </important>

        Args:
            distribution_name: <p>The name of the distribution that the certificate will be attached to.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>
            certificate_name: <p>The name of the certificate to attach to a distribution.</p> <p>Only certificates with a status of <code>ISSUED</code> can be attached to a distribution.</p> <p>Use the <code>GetCertificates</code> action to get a list of certificate names that you can specify.</p> <note> <p>This is the name of the certificate resource type and is used only to reference the certificate in other API actions. It can be different than the domain name of the certificate. For example, your certificate name might be <code>WordPress-Blog-Certificate</code> and the domain name of the certificate might be <code>example.com</code>.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.attach_certificate_to_distribution_request.AttachCertificateToDistributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.attach_certificate_to_distribution_result.AttachCertificateToDistributionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.attach_certificate_to_distribution

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.attach_certificate_to_distribution.async_attach_certificate_to_distribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.attach_certificate_to_distribution_request.AttachCertificateToDistributionRequest = {
            "distribution_name": distribution_name,
            "certificate_name": certificate_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def attach_disk(
        self,
        disk_name: "capo_lightsail.types.resource_name.ResourceName",
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        disk_path: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        auto_mounting: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.attach_disk_result.AttachDiskResult":
        """<p>Attaches a block storage disk to a running or stopped Lightsail instance and exposes it to the instance with the specified disk name.</p> <p>The <code>attach disk</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>disk name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_name: <p>The unique Lightsail disk name (<code>my-disk</code>).</p>
            instance_name: <p>The name of the Lightsail instance where you want to utilize the storage disk.</p>
            disk_path: <p>The disk path to expose to the instance (<code>/dev/xvdf</code>).</p>
            auto_mounting: <p>A Boolean value used to determine the automatic mounting of a storage volume to a virtual computer. The default value is <code>False</code>.</p> <important> <p>This value only applies to Lightsail for Research resources.</p> </important>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.attach_disk_request.AttachDiskRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.attach_disk_result.AttachDiskResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.attach_disk

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.attach_disk.async_attach_disk(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.attach_disk_request.AttachDiskRequest = {
            "disk_name": disk_name,
            "instance_name": instance_name,
            "disk_path": disk_path,
        }
        if auto_mounting is not None:
            input_["auto_mounting"] = auto_mounting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def attach_instances_to_load_balancer(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        instance_names: "capo_lightsail.types.resource_name_list.ResourceNameList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.attach_instances_to_load_balancer_result.AttachInstancesToLoadBalancerResult":
        """<p>Attaches one or more Lightsail instances to a load balancer.</p> <p>After some time, the instances are attached to the load balancer and the health check status is available.</p> <p>The <code>attach instances to load balancer</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            instance_names: <p>An array of strings representing the instance name(s) you want to attach to your load balancer.</p> <p>An instance must be <code>running</code> before you can attach it to your load balancer.</p> <p>There are no additional limits on the number of instances you can attach to your load balancer, aside from the limit of Lightsail instances you can create in your account (20).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.attach_instances_to_load_balancer_request.AttachInstancesToLoadBalancerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.attach_instances_to_load_balancer_result.AttachInstancesToLoadBalancerResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.attach_instances_to_load_balancer

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.attach_instances_to_load_balancer.async_attach_instances_to_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.attach_instances_to_load_balancer_request.AttachInstancesToLoadBalancerRequest = {
            "load_balancer_name": load_balancer_name,
            "instance_names": instance_names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def attach_load_balancer_tls_certificate(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        certificate_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.attach_load_balancer_tls_certificate_result.AttachLoadBalancerTlsCertificateResult":
        """<p>Attaches a Transport Layer Security (TLS) certificate to your load balancer. TLS is just an updated, more secure version of Secure Socket Layer (SSL).</p> <p>Once you create and validate your certificate, you can attach it to your load balancer. You can also use this API to rotate the certificates on your account. Use the <code>AttachLoadBalancerTlsCertificate</code> action with the non-attached certificate, and it will replace the existing one and become the attached certificate.</p> <p>The <code>AttachLoadBalancerTlsCertificate</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer to which you want to associate the SSL/TLS certificate.</p>
            certificate_name: <p>The name of your SSL/TLS certificate.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.attach_load_balancer_tls_certificate_request.AttachLoadBalancerTlsCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.attach_load_balancer_tls_certificate_result.AttachLoadBalancerTlsCertificateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.attach_load_balancer_tls_certificate

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.attach_load_balancer_tls_certificate.async_attach_load_balancer_tls_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.attach_load_balancer_tls_certificate_request.AttachLoadBalancerTlsCertificateRequest = {
            "load_balancer_name": load_balancer_name,
            "certificate_name": certificate_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def attach_static_ip(
        self,
        static_ip_name: "capo_lightsail.types.resource_name.ResourceName",
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.attach_static_ip_result.AttachStaticIpResult":
        """<p>Attaches a static IP address to a specific Amazon Lightsail instance.</p>

        Args:
            static_ip_name: <p>The name of the static IP.</p>
            instance_name: <p>The instance name to which you want to attach the static IP address.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.attach_static_ip_request.AttachStaticIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.attach_static_ip_result.AttachStaticIpResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.attach_static_ip

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.attach_static_ip.async_attach_static_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.attach_static_ip_request.AttachStaticIpRequest = {
            "static_ip_name": static_ip_name,
            "instance_name": instance_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def close_instance_public_ports(
        self,
        port_info: "capo_lightsail.types.port_info.PortInfo",
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.close_instance_public_ports_result.CloseInstancePublicPortsResult":
        """<p>Closes ports for a specific Amazon Lightsail instance.</p> <p>The <code>CloseInstancePublicPorts</code> action supports tag-based access control via resource tags applied to the resource identified by <code>instanceName</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            port_info: <p>An object to describe the ports to close for the specified instance.</p>
            instance_name: <p>The name of the instance for which to close ports.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.close_instance_public_ports_request.CloseInstancePublicPortsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.close_instance_public_ports_result.CloseInstancePublicPortsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.close_instance_public_ports

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.close_instance_public_ports.async_close_instance_public_ports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.close_instance_public_ports_request.CloseInstancePublicPortsRequest = {
            "port_info": port_info,
            "instance_name": instance_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def copy_snapshot(
        self,
        target_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        source_region: "capo_lightsail.types.region_name.RegionName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        source_snapshot_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        source_resource_name: Optional["capo_lightsail.types.string.string"] = None,
        restore_date: Optional["capo_lightsail.types.string.string"] = None,
        use_latest_restorable_auto_snapshot: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
    ) -> "capo_lightsail.types.copy_snapshot_result.CopySnapshotResult":
        """<p>Copies a manual snapshot of an instance or disk as another manual snapshot, or copies an automatic snapshot of an instance or disk as a manual snapshot. This operation can also be used to copy a manual or automatic snapshot of an instance or a disk from one Amazon Web Services Region to another in Amazon Lightsail.</p> <p>When copying a <i>manual snapshot</i>, be sure to define the <code>source region</code>, <code>source snapshot name</code>, and <code>target snapshot name</code> parameters.</p> <p>When copying an <i>automatic snapshot</i>, be sure to define the <code>source region</code>, <code>source resource name</code>, <code>target snapshot name</code>, and either the <code>restore date</code> or the <code>use latest restorable auto snapshot</code> parameters.</p>

        Args:
            source_snapshot_name: <p>The name of the source manual snapshot to copy.</p> <p>Constraint:</p> <ul> <li> <p>Define this parameter only when copying a manual snapshot as another manual snapshot.</p> </li> </ul>
            source_resource_name: <p>The name of the source instance or disk from which the source automatic snapshot was created.</p> <p>Constraint:</p> <ul> <li> <p>Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            restore_date: <p>The date of the source automatic snapshot to copy. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            use_latest_restorable_auto_snapshot: <p>A Boolean value to indicate whether to use the latest available automatic snapshot of the specified source instance or disk.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when copying an automatic snapshot as a manual snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-keeping-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            target_snapshot_name: <p>The name of the new manual snapshot to be created as a copy.</p>
            source_region: <p>The Amazon Web Services Region where the source manual or automatic snapshot is located.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.copy_snapshot_request.CopySnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.copy_snapshot_result.CopySnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.copy_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.copy_snapshot.async_copy_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.copy_snapshot_request.CopySnapshotRequest = {
            "target_snapshot_name": target_snapshot_name,
            "source_region": source_region,
        }
        if source_snapshot_name is not None:
            input_["source_snapshot_name"] = source_snapshot_name
        if source_resource_name is not None:
            input_["source_resource_name"] = source_resource_name
        if restore_date is not None:
            input_["restore_date"] = restore_date
        if use_latest_restorable_auto_snapshot is not None:
            input_["use_latest_restorable_auto_snapshot"] = (
                use_latest_restorable_auto_snapshot
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bucket(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        enable_object_versioning: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
    ) -> "capo_lightsail.types.create_bucket_result.CreateBucketResult":
        """<p>Creates an Amazon Lightsail bucket.</p> <p>A bucket is a cloud storage resource available in the Lightsail object storage service. Use buckets to store objects such as data and its descriptive metadata. For more information about buckets, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/buckets-in-amazon-lightsail">Buckets in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Args:
            bucket_name: <p>The name for the bucket.</p> <p>For more information about bucket names, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/bucket-naming-rules-in-amazon-lightsail">Bucket naming rules in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>
            bundle_id: <p>The ID of the bundle to use for the bucket.</p> <p>A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html">GetBucketBundles</a> action to get a list of bundle IDs that you can specify.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html">UpdateBucketBundle</a> action to change the bundle after the bucket is created.</p>
            tags: <p>The tag keys and optional values to add to the bucket during creation.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_TagResource.html">TagResource</a> action to tag the bucket after it's created.</p>
            enable_object_versioning: <p>A Boolean value that indicates whether to enable versioning of objects in the bucket.</p> <p>For more information about versioning, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-bucket-object-versioning">Enabling and suspending object versioning in a bucket in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_bucket_request.CreateBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_bucket_result.CreateBucketResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_bucket

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_bucket.async_create_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_bucket_request.CreateBucketRequest = {
            "bucket_name": bucket_name,
            "bundle_id": bundle_id,
        }
        if tags is not None:
            input_["tags"] = tags
        if enable_object_versioning is not None:
            input_["enable_object_versioning"] = enable_object_versioning

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bucket_access_key(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.create_bucket_access_key_result.CreateBucketAccessKeyResult":
        """<p>Creates a new access key for the specified Amazon Lightsail bucket. Access keys consist of an access key ID and corresponding secret access key.</p> <p>Access keys grant full programmatic access to the specified bucket and its objects. You can have a maximum of two access keys per bucket. Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketAccessKeys.html">GetBucketAccessKeys</a> action to get a list of current access keys for a specific bucket. For more information about access keys, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-bucket-access-keys">Creating access keys for a bucket in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p> <important> <p>The <code>secretAccessKey</code> value is returned only in response to the <code>CreateBucketAccessKey</code> action. You can get a secret access key only when you first create an access key; you cannot get the secret access key later. If you lose the secret access key, you must create a new access key.</p> </important>

        Args:
            bucket_name: <p>The name of the bucket that the new access key will belong to, and grant access to.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_bucket_access_key_request.CreateBucketAccessKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_bucket_access_key_result.CreateBucketAccessKeyResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_bucket_access_key

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_bucket_access_key.async_create_bucket_access_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_bucket_access_key_request.CreateBucketAccessKeyRequest = {
            "bucket_name": bucket_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_certificate(
        self,
        certificate_name: "capo_lightsail.types.certificate_name.CertificateName",
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        subject_alternative_names: Optional[
            "capo_lightsail.types.subject_alternative_name_list.SubjectAlternativeNameList"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_certificate_result.CreateCertificateResult":
        """<p>Creates an SSL/TLS certificate for an Amazon Lightsail content delivery network (CDN) distribution and a container service.</p> <p>After the certificate is valid, use the <code>AttachCertificateToDistribution</code> action to use the certificate and its domains with your distribution. Or use the <code>UpdateContainerService</code> action to use the certificate and its domains with your container service.</p> <important> <p>Only certificates created in the <code>us-east-1</code> Amazon Web Services Region can be attached to Lightsail distributions. Lightsail distributions are global resources that can reference an origin in any Amazon Web Services Region, and distribute its content globally. However, all distributions are located in the <code>us-east-1</code> Region.</p> </important>

        Args:
            certificate_name: <p>The name for the certificate.</p>
            domain_name: <p>The domain name (<code>example.com</code>) for the certificate.</p>
            subject_alternative_names: <p>An array of strings that specify the alternate domains (<code>example2.com</code>) and subdomains (<code>blog.example.com</code>) for the certificate.</p> <p>You can specify a maximum of nine alternate domains (in addition to the primary domain name).</p> <p>Wildcard domain entries (<code>*.example.com</code>) are not supported.</p>
            tags: <p>The tag keys and optional values to add to the certificate during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_certificate_request.CreateCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_certificate_result.CreateCertificateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_certificate

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_certificate.async_create_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_certificate_request.CreateCertificateRequest = {
            "certificate_name": certificate_name,
            "domain_name": domain_name,
        }
        if subject_alternative_names is not None:
            input_["subject_alternative_names"] = subject_alternative_names
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cloud_formation_stack(
        self,
        instances: "capo_lightsail.types.instance_entry_list.InstanceEntryList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.create_cloud_formation_stack_result.CreateCloudFormationStackResult":
        """<p>Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance from an exported Amazon Lightsail snapshot. This operation results in a CloudFormation stack record that can be used to track the AWS CloudFormation stack created. Use the <code>get cloud formation stack records</code> operation to get a list of the CloudFormation stacks created.</p> <important> <p>Wait until after your new Amazon EC2 instance is created before running the <code>create cloud formation stack</code> operation again with the same export snapshot record.</p> </important>

        Args:
            instances: <p>An array of parameters that will be used to create the new Amazon EC2 instance. You can only pass one instance entry at a time in this array. You will get an invalid parameter error if you pass more than one instance entry in this array.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_cloud_formation_stack_request.CreateCloudFormationStackRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_cloud_formation_stack_result.CreateCloudFormationStackResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_cloud_formation_stack

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_cloud_formation_stack.async_create_cloud_formation_stack(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_cloud_formation_stack_request.CreateCloudFormationStackRequest = {
            "instances": instances
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_contact_method(
        self,
        protocol: "capo_lightsail.types.contact_protocol.ContactProtocol",
        contact_endpoint: "capo_lightsail.types.string_max256.StringMax256",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_contact_method_result.CreateContactMethodResult":
        """<p>Creates an email or SMS text message contact method.</p> <p>A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications">Notifications in Amazon Lightsail</a>.</p> <p>The <code>create contact method</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Lightsail Developer Guide</a>.</p>

        Args:
            protocol: <p>The protocol of the contact method, such as <code>Email</code> or <code>SMS</code> (text messaging).</p> <p>The <code>SMS</code> protocol is supported only in the following Amazon Web Services Regions.</p> <ul> <li> <p>US East (N. Virginia) (<code>us-east-1</code>)</p> </li> <li> <p>US West (Oregon) (<code>us-west-2</code>)</p> </li> <li> <p>Europe (Ireland) (<code>eu-west-1</code>)</p> </li> <li> <p>Asia Pacific (Tokyo) (<code>ap-northeast-1</code>)</p> </li> <li> <p>Asia Pacific (Singapore) (<code>ap-southeast-1</code>)</p> </li> <li> <p>Asia Pacific (Sydney) (<code>ap-southeast-2</code>)</p> </li> </ul> <p>For a list of countries/regions where SMS text messages can be sent, and the latest Amazon Web Services Regions where SMS text messaging is supported, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-supported-regions-countries.html">Supported Regions and Countries</a> in the <i>Amazon SNS Developer Guide</i>.</p> <p>For more information about notifications in Amazon Lightsail, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications">Notifications in Amazon Lightsail</a>.</p>
            contact_endpoint: <p>The destination of the contact method, such as an email address or a mobile phone number.</p> <p>Use the E.164 format when specifying a mobile phone number. E.164 is a standard for the phone number structure used for international telecommunication. Phone numbers that follow this format can have a maximum of 15 digits, and they are prefixed with the plus character (+) and the country code. For example, a U.S. phone number in E.164 format would be specified as +1XXX5550100. For more information, see <a href="https://en.wikipedia.org/wiki/E.164">E.164</a> on <i>Wikipedia</i>.</p>
            tags: <p>The tag keys and optional values to add to the contact method during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_contact_method_request.CreateContactMethodRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_contact_method_result.CreateContactMethodResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_contact_method

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_contact_method.async_create_contact_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_contact_method_request.CreateContactMethodRequest = {
            "protocol": protocol,
            "contact_endpoint": contact_endpoint,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_container_service(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        power: "capo_lightsail.types.container_service_power_name.ContainerServicePowerName",
        scale: "capo_lightsail.types.container_service_scale.ContainerServiceScale",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        public_domain_names: Optional[
            "capo_lightsail.types.container_service_public_domains.ContainerServicePublicDomains"
        ] = None,
        deployment: Optional[
            "capo_lightsail.types.container_service_deployment_request.ContainerServiceDeploymentRequest"
        ] = None,
        private_registry_access: Optional[
            "capo_lightsail.types.private_registry_access_request.PrivateRegistryAccessRequest"
        ] = None,
    ) -> "capo_lightsail.types.create_container_service_result.CreateContainerServiceResult":
        """<p>Creates an Amazon Lightsail container service.</p> <p>A Lightsail container service is a compute resource to which you can deploy containers. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-services">Container services in Amazon Lightsail</a> in the <i>Lightsail Dev Guide</i>.</p>

        Args:
            service_name: <p>The name for the container service.</p> <p>The name that you specify for your container service will make up part of its default domain. The default domain of a container service is typically <code>https://<ServiceName>.<RandomGUID>.<AWSRegion>.cs.amazonlightsail.com</code>. If the name of your container service is <code>container-service-1</code>, and it's located in the US East (Ohio) Amazon Web Services Region (<code>us-east-2</code>), then the domain for your container service will be like the following example: <code>https://container-service-1.ur4EXAMPLE2uq.us-east-2.cs.amazonlightsail.com</code> </p> <p>The following are the requirements for container service names:</p> <ul> <li> <p>Must be unique within each Amazon Web Services Region in your Lightsail account.</p> </li> <li> <p>Must contain 1 to 63 characters.</p> </li> <li> <p>Must contain only alphanumeric characters and hyphens.</p> </li> <li> <p>A hyphen (-) can separate words but cannot be at the start or end of the name.</p> </li> </ul>
            power: <p>The power specification for the container service.</p> <p>The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p> <p>Use the <code>GetContainerServicePowers</code> action to get a list of power options that you can specify using this parameter, and their base monthly cost.</p>
            scale: <p>The scale specification for the container service.</p> <p>The scale specifies the allocated compute nodes of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p>
            tags: <p>The tag keys and optional values to add to the container service during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p> <p>For more information about tags in Lightsail, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p>
            public_domain_names: <p>The public domain names to use with the container service, such as <code>example.com</code> and <code>www.example.com</code>.</p> <p>You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.</p> <p>If you don't specify public domain names, then you can use the default domain of the container service.</p> <important> <p>You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the <code>CreateCertificate</code> action to create a certificate for the public domain names you want to use with your container service.</p> </important> <p>You can specify public domain names using a string to array map as shown in the example later on this page.</p>
            deployment: <p>An object that describes a deployment for the container service.</p> <p>A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration.</p>
            private_registry_access: <p>An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access">Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_container_service_request.CreateContainerServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_container_service_result.CreateContainerServiceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_container_service

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_container_service.async_create_container_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_container_service_request.CreateContainerServiceRequest = {
            "service_name": service_name,
            "power": power,
            "scale": scale,
        }
        if tags is not None:
            input_["tags"] = tags
        if public_domain_names is not None:
            input_["public_domain_names"] = public_domain_names
        if deployment is not None:
            input_["deployment"] = deployment
        if private_registry_access is not None:
            input_["private_registry_access"] = private_registry_access

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_container_service_deployment(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        containers: Optional["capo_lightsail.types.container_map.ContainerMap"] = None,
        public_endpoint: Optional[
            "capo_lightsail.types.endpoint_request.EndpointRequest"
        ] = None,
    ) -> "capo_lightsail.types.create_container_service_deployment_result.CreateContainerServiceDeploymentResult":
        """<p>Creates a deployment for your Amazon Lightsail container service.</p> <p>A deployment specifies the containers that will be launched on the container service and their settings, such as the ports to open, the environment variables to apply, and the launch command to run. It also specifies the container that will serve as the public endpoint of the deployment and its settings, such as the HTTP or HTTPS port to use, and the health check configuration.</p> <p>You can deploy containers to your container service using container images from a public registry such as Amazon ECR Public, or from your local machine. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-container-images">Creating container images for your Amazon Lightsail container services</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Args:
            service_name: <p>The name of the container service for which to create the deployment.</p>
            containers: <p>An object that describes the settings of the containers that will be launched on the container service.</p>
            public_endpoint: <p>An object that describes the settings of the public endpoint for the container service.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_container_service_deployment_request.CreateContainerServiceDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_container_service_deployment_result.CreateContainerServiceDeploymentResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_container_service_deployment

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_container_service_deployment.async_create_container_service_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_container_service_deployment_request.CreateContainerServiceDeploymentRequest = {
            "service_name": service_name
        }
        if containers is not None:
            input_["containers"] = containers
        if public_endpoint is not None:
            input_["public_endpoint"] = public_endpoint

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_container_service_registry_login(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.create_container_service_registry_login_result.CreateContainerServiceRegistryLoginResult":
        """<p>Creates a temporary set of log in credentials that you can use to log in to the Docker process on your local machine. After you're logged in, you can use the native Docker commands to push your local container images to the container image registry of your Amazon Lightsail account so that you can use them with your Lightsail container service. The log in credentials expire 12 hours after they are created, at which point you will need to create a new set of log in credentials.</p> <note> <p>You can only push container images to the container service registry of your Lightsail account. You cannot pull container images or perform any other container image management actions on the container service registry.</p> </note> <p>After you push your container images to the container image registry of your Lightsail account, use the <code>RegisterContainerImage</code> action to register the pushed images to a specific Lightsail container service.</p> <note> <p>This action is not required if you install and use the Lightsail Control (lightsailctl) plugin to push container images to your Lightsail container service. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-pushing-container-images">Pushing and managing container images on your Amazon Lightsail container services</a> in the <i>Amazon Lightsail Developer Guide</i>.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_container_service_registry_login_request.CreateContainerServiceRegistryLoginRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_container_service_registry_login_result.CreateContainerServiceRegistryLoginResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_container_service_registry_login

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_container_service_registry_login.async_create_container_service_registry_login(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_container_service_registry_login_request.CreateContainerServiceRegistryLoginRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_disk(
        self,
        disk_name: "capo_lightsail.types.resource_name.ResourceName",
        availability_zone: "capo_lightsail.types.non_empty_string.NonEmptyString",
        size_in_gb: "capo_lightsail.types.integer.integer",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        add_ons: Optional[
            "capo_lightsail.types.add_on_request_list.AddOnRequestList"
        ] = None,
    ) -> "capo_lightsail.types.create_disk_result.CreateDiskResult":
        """<p>Creates a block storage disk that can be attached to an Amazon Lightsail instance in the same Availability Zone (<code>us-east-2a</code>).</p> <p>The <code>create disk</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_name: <p>The unique Lightsail disk name (<code>my-disk</code>).</p>
            availability_zone: <p>The Availability Zone where you want to create the disk (<code>us-east-2a</code>). Use the same Availability Zone as the Lightsail instance to which you want to attach the disk.</p> <p>Use the <code>get regions</code> operation to list the Availability Zones where Lightsail is currently available.</p>
            size_in_gb: <p>The size of the disk in GB (<code>32</code>).</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>
            add_ons: <p>An array of objects that represent the add-ons to enable for the new disk.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_disk_request.CreateDiskRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_disk_result.CreateDiskResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_disk

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_disk.async_create_disk(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_disk_request.CreateDiskRequest = {
            "disk_name": disk_name,
            "availability_zone": availability_zone,
            "size_in_gb": size_in_gb,
        }
        if tags is not None:
            input_["tags"] = tags
        if add_ons is not None:
            input_["add_ons"] = add_ons

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_disk_from_snapshot(
        self,
        disk_name: "capo_lightsail.types.resource_name.ResourceName",
        availability_zone: "capo_lightsail.types.non_empty_string.NonEmptyString",
        size_in_gb: "capo_lightsail.types.integer.integer",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        disk_snapshot_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        add_ons: Optional[
            "capo_lightsail.types.add_on_request_list.AddOnRequestList"
        ] = None,
        source_disk_name: Optional["capo_lightsail.types.string.string"] = None,
        restore_date: Optional["capo_lightsail.types.string.string"] = None,
        use_latest_restorable_auto_snapshot: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
    ) -> "capo_lightsail.types.create_disk_from_snapshot_result.CreateDiskFromSnapshotResult":
        """<p>Creates a block storage disk from a manual or automatic snapshot of a disk. The resulting disk can be attached to an Amazon Lightsail instance in the same Availability Zone (<code>us-east-2a</code>).</p> <p>The <code>create disk from snapshot</code> operation supports tag-based access control via request tags and resource tags applied to the resource identified by <code>disk snapshot name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_name: <p>The unique Lightsail disk name (<code>my-disk</code>).</p>
            disk_snapshot_name: <p>The name of the disk snapshot (<code>my-snapshot</code>) from which to create the new storage disk.</p> <p>Constraint:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>source disk name</code> parameter. The <code>disk snapshot name</code> and <code>source disk name</code> parameters are mutually exclusive.</p> </li> </ul>
            availability_zone: <p>The Availability Zone where you want to create the disk (<code>us-east-2a</code>). Choose the same Availability Zone as the Lightsail instance where you want to create the disk.</p> <p>Use the GetRegions operation to list the Availability Zones where Lightsail is currently available.</p>
            size_in_gb: <p>The size of the disk in GB (<code>32</code>).</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>
            add_ons: <p>An array of objects that represent the add-ons to enable for the new disk.</p>
            source_disk_name: <p>The name of the source disk from which the source automatic snapshot was created.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>disk snapshot name</code> parameter. The <code>source disk name</code> and <code>disk snapshot name</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            restore_date: <p>The date of the automatic snapshot to use for the new disk. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            use_latest_restorable_auto_snapshot: <p>A Boolean value to indicate whether to use the latest available automatic snapshot.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new disk from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_disk_from_snapshot_request.CreateDiskFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_disk_from_snapshot_result.CreateDiskFromSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_disk_from_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_disk_from_snapshot.async_create_disk_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_disk_from_snapshot_request.CreateDiskFromSnapshotRequest = {
            "disk_name": disk_name,
            "availability_zone": availability_zone,
            "size_in_gb": size_in_gb,
        }
        if disk_snapshot_name is not None:
            input_["disk_snapshot_name"] = disk_snapshot_name
        if tags is not None:
            input_["tags"] = tags
        if add_ons is not None:
            input_["add_ons"] = add_ons
        if source_disk_name is not None:
            input_["source_disk_name"] = source_disk_name
        if restore_date is not None:
            input_["restore_date"] = restore_date
        if use_latest_restorable_auto_snapshot is not None:
            input_["use_latest_restorable_auto_snapshot"] = (
                use_latest_restorable_auto_snapshot
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_disk_snapshot(
        self,
        disk_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        disk_name: Optional["capo_lightsail.types.resource_name.ResourceName"] = None,
        instance_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_disk_snapshot_result.CreateDiskSnapshotResult":
        """<p>Creates a snapshot of a block storage disk. You can use snapshots for backups, to make copies of disks, and to save data before shutting down a Lightsail instance.</p> <p>You can take a snapshot of an attached disk that is in use; however, snapshots only capture data that has been written to your disk at the time the snapshot command is issued. This may exclude any data that has been cached by any applications or the operating system. If you can pause any file systems on the disk long enough to take a snapshot, your snapshot should be complete. Nevertheless, if you cannot pause all file writes to the disk, you should unmount the disk from within the Lightsail instance, issue the create disk snapshot command, and then remount the disk to ensure a consistent and complete snapshot. You may remount and use your disk while the snapshot status is pending.</p> <p>You can also use this operation to create a snapshot of an instance's system volume. You might want to do this, for example, to recover data from the system volume of a botched instance or to create a backup of the system volume like you would for a block storage disk. To create a snapshot of a system volume, just define the <code>instance name</code> parameter when issuing the snapshot command, and a snapshot of the defined instance's system volume will be created. After the snapshot is available, you can create a block storage disk from the snapshot and attach it to a running instance to access the data on the disk.</p> <p>The <code>create disk snapshot</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_name: <p>The unique name of the source disk (<code>Disk-Virginia-1</code>).</p> <note> <p>This parameter cannot be defined together with the <code>instance name</code> parameter. The <code>disk name</code> and <code>instance name</code> parameters are mutually exclusive.</p> </note>
            disk_snapshot_name: <p>The name of the destination disk snapshot (<code>my-disk-snapshot</code>) based on the source disk.</p>
            instance_name: <p>The unique name of the source instance (<code>Amazon_Linux-512MB-Virginia-1</code>). When this is defined, a snapshot of the instance's system volume is created.</p> <note> <p>This parameter cannot be defined together with the <code>disk name</code> parameter. The <code>instance name</code> and <code>disk name</code> parameters are mutually exclusive.</p> </note>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_disk_snapshot_request.CreateDiskSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_disk_snapshot_result.CreateDiskSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_disk_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_disk_snapshot.async_create_disk_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_disk_snapshot_request.CreateDiskSnapshotRequest = {
            "disk_snapshot_name": disk_snapshot_name
        }
        if disk_name is not None:
            input_["disk_name"] = disk_name
        if instance_name is not None:
            input_["instance_name"] = instance_name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_distribution(
        self,
        distribution_name: "capo_lightsail.types.resource_name.ResourceName",
        origin: "capo_lightsail.types.input_origin.InputOrigin",
        default_cache_behavior: "capo_lightsail.types.cache_behavior.CacheBehavior",
        bundle_id: "capo_lightsail.types.string.string",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        cache_behavior_settings: Optional[
            "capo_lightsail.types.cache_settings.CacheSettings"
        ] = None,
        cache_behaviors: Optional[
            "capo_lightsail.types.cache_behavior_list.CacheBehaviorList"
        ] = None,
        ip_address_type: Optional[
            "capo_lightsail.types.ip_address_type.IpAddressType"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        certificate_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        viewer_minimum_tls_protocol_version: Optional[
            "capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.ViewerMinimumTlsProtocolVersionEnum"
        ] = None,
        enable_private_origin_access: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        default_root_object: Optional["capo_lightsail.types.string.string"] = None,
        custom_error_responses: Optional[
            "capo_lightsail.types.distribution_custom_error_response_list.DistributionCustomErrorResponseList"
        ] = None,
    ) -> "capo_lightsail.types.create_distribution_result.CreateDistributionResult":
        """<p>Creates an Amazon Lightsail content delivery network (CDN) distribution.</p> <p>A distribution is a globally distributed network of caching servers that improve the performance of your website or web application hosted on a Lightsail instance. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-content-delivery-network-distributions">Content delivery networks in Amazon Lightsail</a>.</p>

        Args:
            distribution_name: <p>The name for the distribution.</p>
            origin: <p>An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>
            default_cache_behavior: <p>An object that describes the default cache behavior for the distribution.</p>
            cache_behavior_settings: <p>An object that describes the cache behavior settings for the distribution.</p>
            cache_behaviors: <p>An array of objects that describe the per-path cache behavior for the distribution.</p>
            bundle_id: <p>The bundle ID to use for the distribution.</p> <p>A distribution bundle describes the specifications of your distribution, such as the monthly cost and monthly network transfer quota.</p> <p>Use the <code>GetDistributionBundles</code> action to get a list of distribution bundle IDs that you can specify.</p>
            ip_address_type: <p>The IP address type for the distribution.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>
            tags: <p>The tag keys and optional values to add to the distribution during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>
            certificate_name: <p>The name of the SSL/TLS certificate that you want to attach to the distribution.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html">GetCertificates</a> action to get a list of certificate names that you can specify.</p>
            viewer_minimum_tls_protocol_version: <p>The minimum TLS protocol version for the SSL/TLS certificate.</p>
            enable_private_origin_access: <p>Specifies whether to enable private origin access for the distribution. With private origin access, the distribution can serve objects that aren't publicly accessible from a Lightsail bucket.</p> <p>Lightsail grants the distribution permission to read the bucket's objects. Enabling private origin access doesn't change the bucket's access settings, and you can still retrieve publicly accessible objects directly from the bucket's endpoint.</p> <note> <p>You can enable private origin access only when the distribution's origin is a Lightsail bucket. If the origin is another resource type, the request fails.</p> </note>
            default_root_object: <p>The object (for example, <code>index.html</code>) that the distribution returns when a viewer requests the root URL of the distribution (<code>/</code>) instead of a specific object. The object that you specify must be available from the origin.</p>
            custom_error_responses: <p>An array of objects that describe the custom error responses for the distribution. With a custom error response, you can specify the page to return when the origin responds with a given HTTP error code. You can also specify the HTTP status code to send to the viewer.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_distribution_request.CreateDistributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_distribution_result.CreateDistributionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_distribution

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_distribution.async_create_distribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_distribution_request.CreateDistributionRequest = {
            "distribution_name": distribution_name,
            "origin": origin,
            "default_cache_behavior": default_cache_behavior,
            "bundle_id": bundle_id,
        }
        if cache_behavior_settings is not None:
            input_["cache_behavior_settings"] = cache_behavior_settings
        if cache_behaviors is not None:
            input_["cache_behaviors"] = cache_behaviors
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if tags is not None:
            input_["tags"] = tags
        if certificate_name is not None:
            input_["certificate_name"] = certificate_name
        if viewer_minimum_tls_protocol_version is not None:
            input_["viewer_minimum_tls_protocol_version"] = (
                viewer_minimum_tls_protocol_version
            )
        if enable_private_origin_access is not None:
            input_["enable_private_origin_access"] = enable_private_origin_access
        if default_root_object is not None:
            input_["default_root_object"] = default_root_object
        if custom_error_responses is not None:
            input_["custom_error_responses"] = custom_error_responses

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_domain(
        self,
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_domain_result.CreateDomainResult":
        """<p>Creates a domain resource for the specified domain (example.com).</p> <p>The <code>create domain</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            domain_name: <p>The domain name to manage (<code>example.com</code>).</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_domain_request.CreateDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_domain_result.CreateDomainResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_domain

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_domain_request.CreateDomainRequest = {
            "domain_name": domain_name
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_domain_entry(
        self,
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        domain_entry: "capo_lightsail.types.domain_entry.DomainEntry",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.create_domain_entry_result.CreateDomainEntryResult":
        """<p>Creates one of the following domain name system (DNS) records in a domain DNS zone: Address (A), canonical name (CNAME), mail exchanger (MX), name server (NS), start of authority (SOA), service locator (SRV), or text (TXT).</p> <p>The <code>create domain entry</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>domain name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            domain_name: <p>The domain name (<code>example.com</code>) for which you want to create the domain entry.</p>
            domain_entry: <p>An array of key-value pairs containing information about the domain entry request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_domain_entry_request.CreateDomainEntryRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_domain_entry_result.CreateDomainEntryResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_domain_entry

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_domain_entry.async_create_domain_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_domain_entry_request.CreateDomainEntryRequest = {
            "domain_name": domain_name,
            "domain_entry": domain_entry,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_gui_session_access_details(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.create_gui_session_access_details_result.CreateGUISessionAccessDetailsResult":
        """<p>Creates two URLs that are used to access a virtual computer’s graphical user interface (GUI) session. The primary URL initiates a web-based Amazon DCV session to the virtual computer's application. The secondary URL initiates a web-based Amazon DCV session to the virtual computer's operating session. </p> <p>Use <code>StartGUISession</code> to open the session.</p>

        Args:
            resource_name: <p>The resource name.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_gui_session_access_details_request.CreateGUISessionAccessDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_gui_session_access_details_result.CreateGUISessionAccessDetailsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_gui_session_access_details

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_gui_session_access_details.async_create_gui_session_access_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_gui_session_access_details_request.CreateGUISessionAccessDetailsRequest = {
            "resource_name": resource_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_instances(
        self,
        instance_names: "capo_lightsail.types.string_list.StringList",
        availability_zone: "capo_lightsail.types.string.string",
        blueprint_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        custom_image_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        user_data: Optional["capo_lightsail.types.string.string"] = None,
        key_pair_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        add_ons: Optional[
            "capo_lightsail.types.add_on_request_list.AddOnRequestList"
        ] = None,
        ip_address_type: Optional[
            "capo_lightsail.types.ip_address_type.IpAddressType"
        ] = None,
    ) -> "capo_lightsail.types.create_instances_result.CreateInstancesResult":
        """<p>Creates one or more Amazon Lightsail instances.</p> <p>The <code>create instances</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Lightsail Developer Guide</a>.</p>

        Args:
            instance_names: <p>The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: <code>["MyFirstInstance","MySecondInstance"]</code> </p>
            availability_zone: <p>The Availability Zone in which to create your instance. Use the following format: <code>us-east-2a</code> (case sensitive). You can get a list of Availability Zones by using the <a href="http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html">get regions</a> operation. Be sure to add the <code>include Availability Zones</code> parameter to your request.</p>
            custom_image_name: <p>(Discontinued) The name for your custom image.</p> <note> <p>In releases prior to June 12, 2017, this parameter was ignored by the API. It is now discontinued.</p> </note>
            blueprint_id: <p>The ID for a virtual private server image (<code>app_wordpress_x_x</code> or <code>app_lamp_x_x</code>). Use the <code>get blueprints</code> operation to return a list of available images (or <i>blueprints</i>).</p> <note> <p>Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.</p> </note>
            bundle_id: <p>The bundle of specification information for your virtual private server (or <i>instance</i>), including the pricing plan (<code>medium_x_x</code>).</p>
            user_data: <p>A launch script you can create that configures a server with additional user data. For example, you might want to run <code>apt-get -y update</code>.</p> <note> <p>Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use <code>yum</code>, Debian and Ubuntu use <code>apt-get</code>, and FreeBSD uses <code>pkg</code>. For a complete list, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image">Amazon Lightsail Developer Guide</a>.</p> </note>
            key_pair_name: <p>The name of your key pair.</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>
            add_ons: <p>An array of objects representing the add-ons to enable for the new instance.</p>
            ip_address_type: <p>The IP address type for the instance.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_instances_request.CreateInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_instances_result.CreateInstancesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_instances

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_instances.async_create_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_instances_request.CreateInstancesRequest = {
            "instance_names": instance_names,
            "availability_zone": availability_zone,
            "blueprint_id": blueprint_id,
            "bundle_id": bundle_id,
        }
        if custom_image_name is not None:
            input_["custom_image_name"] = custom_image_name
        if user_data is not None:
            input_["user_data"] = user_data
        if key_pair_name is not None:
            input_["key_pair_name"] = key_pair_name
        if tags is not None:
            input_["tags"] = tags
        if add_ons is not None:
            input_["add_ons"] = add_ons
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_instances_from_snapshot(
        self,
        instance_names: "capo_lightsail.types.string_list.StringList",
        availability_zone: "capo_lightsail.types.string.string",
        bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        attached_disk_mapping: Optional[
            "capo_lightsail.types.attached_disk_map.AttachedDiskMap"
        ] = None,
        instance_snapshot_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        user_data: Optional["capo_lightsail.types.string.string"] = None,
        key_pair_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        add_ons: Optional[
            "capo_lightsail.types.add_on_request_list.AddOnRequestList"
        ] = None,
        ip_address_type: Optional[
            "capo_lightsail.types.ip_address_type.IpAddressType"
        ] = None,
        source_instance_name: Optional["capo_lightsail.types.string.string"] = None,
        restore_date: Optional["capo_lightsail.types.string.string"] = None,
        use_latest_restorable_auto_snapshot: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
    ) -> "capo_lightsail.types.create_instances_from_snapshot_result.CreateInstancesFromSnapshotResult":
        """<p>Creates one or more new instances from a manual or automatic snapshot of an instance.</p> <p>The <code>create instances from snapshot</code> operation supports tag-based access control via request tags and resource tags applied to the resource identified by <code>instance snapshot name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_names: <p>The names for your new instances.</p>
            attached_disk_mapping: <p>An object containing information about one or more disk mappings.</p>
            availability_zone: <p>The Availability Zone where you want to create your instances. Use the following formatting: <code>us-east-2a</code> (case sensitive). You can get a list of Availability Zones by using the <a href="http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html">get regions</a> operation. Be sure to add the <code>include Availability Zones</code> parameter to your request.</p>
            instance_snapshot_name: <p>The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.</p> <p>Constraint:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>source instance name</code> parameter. The <code>instance snapshot name</code> and <code>source instance name</code> parameters are mutually exclusive.</p> </li> </ul>
            bundle_id: <p>The bundle of specification information for your virtual private server (or <i>instance</i>), including the pricing plan (<code>micro_x_x</code>).</p>
            user_data: <p>You can create a launch script that configures a server with additional user data. For example, <code>apt-get -y update</code>.</p> <note> <p>Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use <code>yum</code>, Debian and Ubuntu use <code>apt-get</code>, and FreeBSD uses <code>pkg</code>. For a complete list, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image">Amazon Lightsail Developer Guide</a>.</p> </note>
            key_pair_name: <p>The name for your key pair.</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>
            add_ons: <p>An array of objects representing the add-ons to enable for the new instance.</p>
            ip_address_type: <p>The IP address type for the instance.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>
            source_instance_name: <p>The name of the source instance from which the source automatic snapshot was created.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>instance snapshot name</code> parameter. The <code>source instance name</code> and <code>instance snapshot name</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            restore_date: <p>The date of the automatic snapshot to use for the new instance. Use the <code>get auto snapshots</code> operation to identify the dates of the available automatic snapshots.</p> <p>Constraints:</p> <ul> <li> <p>Must be specified in <code>YYYY-MM-DD</code> format.</p> </li> <li> <p>This parameter cannot be defined together with the <code>use latest restorable auto snapshot</code> parameter. The <code>restore date</code> and <code>use latest restorable auto snapshot</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>
            use_latest_restorable_auto_snapshot: <p>A Boolean value to indicate whether to use the latest available automatic snapshot.</p> <p>Constraints:</p> <ul> <li> <p>This parameter cannot be defined together with the <code>restore date</code> parameter. The <code>use latest restorable auto snapshot</code> and <code>restore date</code> parameters are mutually exclusive.</p> </li> <li> <p>Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_instances_from_snapshot_request.CreateInstancesFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_instances_from_snapshot_result.CreateInstancesFromSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_instances_from_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_instances_from_snapshot.async_create_instances_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_instances_from_snapshot_request.CreateInstancesFromSnapshotRequest = {
            "instance_names": instance_names,
            "availability_zone": availability_zone,
            "bundle_id": bundle_id,
        }
        if attached_disk_mapping is not None:
            input_["attached_disk_mapping"] = attached_disk_mapping
        if instance_snapshot_name is not None:
            input_["instance_snapshot_name"] = instance_snapshot_name
        if user_data is not None:
            input_["user_data"] = user_data
        if key_pair_name is not None:
            input_["key_pair_name"] = key_pair_name
        if tags is not None:
            input_["tags"] = tags
        if add_ons is not None:
            input_["add_ons"] = add_ons
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if source_instance_name is not None:
            input_["source_instance_name"] = source_instance_name
        if restore_date is not None:
            input_["restore_date"] = restore_date
        if use_latest_restorable_auto_snapshot is not None:
            input_["use_latest_restorable_auto_snapshot"] = (
                use_latest_restorable_auto_snapshot
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_instance_snapshot(
        self,
        instance_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_instance_snapshot_result.CreateInstanceSnapshotResult":
        """<p>Creates a snapshot of a specific virtual private server, or <i>instance</i>. You can use a snapshot to create a new instance that is based on that snapshot.</p> <p>The <code>create instance snapshot</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_snapshot_name: <p>The name for your new snapshot.</p>
            instance_name: <p>The Lightsail instance on which to base your snapshot.</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_instance_snapshot_request.CreateInstanceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_instance_snapshot_result.CreateInstanceSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_instance_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_instance_snapshot.async_create_instance_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_instance_snapshot_request.CreateInstanceSnapshotRequest = {
            "instance_snapshot_name": instance_snapshot_name,
            "instance_name": instance_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_key_pair(
        self,
        key_pair_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_key_pair_result.CreateKeyPairResult":
        """<p>Creates a custom SSH key pair that you can use with an Amazon Lightsail instance.</p> <note> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.html">DownloadDefaultKeyPair</a> action to create a Lightsail default key pair in an Amazon Web Services Region where a default key pair does not currently exist.</p> </note> <p>The <code>create key pair</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            key_pair_name: <p>The name for your new key pair.</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_key_pair_request.CreateKeyPairRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_key_pair_result.CreateKeyPairResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_key_pair

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_key_pair.async_create_key_pair(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_key_pair_request.CreateKeyPairRequest = {
            "key_pair_name": key_pair_name
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_load_balancer(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        instance_port: "capo_lightsail.types.port.Port",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        health_check_path: Optional["capo_lightsail.types.string.string"] = None,
        certificate_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        certificate_domain_name: Optional[
            "capo_lightsail.types.domain_name.DomainName"
        ] = None,
        certificate_alternative_names: Optional[
            "capo_lightsail.types.domain_name_list.DomainNameList"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
        ip_address_type: Optional[
            "capo_lightsail.types.ip_address_type.IpAddressType"
        ] = None,
        tls_policy_name: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.create_load_balancer_result.CreateLoadBalancerResult":
        """<p>Creates a Lightsail load balancer. To learn more about deciding whether to load balance your application, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/configure-lightsail-instances-for-load-balancing">Configure your Lightsail instances for load balancing</a>. You can create up to 10 load balancers per AWS Region in your account.</p> <p>When you create a load balancer, you can specify a unique name and port settings. To change additional load balancer settings, use the <code>UpdateLoadBalancerAttribute</code> operation.</p> <p>The <code>create load balancer</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The name of your load balancer.</p>
            instance_port: <p>The instance port where you're creating your load balancer.</p>
            health_check_path: <p>The path you provided to perform the load balancer health check. If you didn't specify a health check path, Lightsail uses the root path of your website (<code>"/"</code>).</p> <p>You may want to specify a custom health check path other than the root of your application if your home page loads slowly or has a lot of media or scripting on it.</p>
            certificate_name: <p>The name of the SSL/TLS certificate.</p> <p>If you specify <code>certificateName</code>, then <code>certificateDomainName</code> is required (and vice-versa).</p>
            certificate_domain_name: <p>The domain name with which your certificate is associated (<code>example.com</code>).</p> <p>If you specify <code>certificateDomainName</code>, then <code>certificateName</code> is required (and vice-versa).</p>
            certificate_alternative_names: <p>The optional alternative domains and subdomains to use with your SSL/TLS certificate (<code>www.example.com</code>, <code>example.com</code>, <code>m.example.com</code>, <code>blog.example.com</code>).</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>
            ip_address_type: <p>The IP address type for the load balancer.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p> <p>The default value is <code>dualstack</code>.</p>
            tls_policy_name: <p>The name of the TLS policy to apply to the load balancer.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsPolicies.html">GetLoadBalancerTlsPolicies</a> action to get a list of TLS policy names that you can specify.</p> <p>For more information about load balancer TLS policies, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-tls-security-policy">Configuring TLS security policies on your Amazon Lightsail load balancers</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_load_balancer_request.CreateLoadBalancerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_load_balancer_result.CreateLoadBalancerResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_load_balancer

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_load_balancer.async_create_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_load_balancer_request.CreateLoadBalancerRequest = {
            "load_balancer_name": load_balancer_name,
            "instance_port": instance_port,
        }
        if health_check_path is not None:
            input_["health_check_path"] = health_check_path
        if certificate_name is not None:
            input_["certificate_name"] = certificate_name
        if certificate_domain_name is not None:
            input_["certificate_domain_name"] = certificate_domain_name
        if certificate_alternative_names is not None:
            input_["certificate_alternative_names"] = certificate_alternative_names
        if tags is not None:
            input_["tags"] = tags
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if tls_policy_name is not None:
            input_["tls_policy_name"] = tls_policy_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_load_balancer_tls_certificate(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        certificate_name: "capo_lightsail.types.resource_name.ResourceName",
        certificate_domain_name: "capo_lightsail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        certificate_alternative_names: Optional[
            "capo_lightsail.types.domain_name_list.DomainNameList"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_load_balancer_tls_certificate_result.CreateLoadBalancerTlsCertificateResult":
        """<p>Creates an SSL/TLS certificate for an Amazon Lightsail load balancer.</p> <p>TLS is just an updated, more secure version of Secure Socket Layer (SSL).</p> <p>The <code>CreateLoadBalancerTlsCertificate</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The load balancer name where you want to create the SSL/TLS certificate.</p>
            certificate_name: <p>The SSL/TLS certificate name.</p> <p>You can have up to 10 certificates in your account at one time. Each Lightsail load balancer can have up to 2 certificates associated with it at one time. There is also an overall limit to the number of certificates that can be issue in a 365-day period. For more information, see <a href="http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html">Limits</a>.</p>
            certificate_domain_name: <p>The domain name (<code>example.com</code>) for your SSL/TLS certificate.</p>
            certificate_alternative_names: <p>An array of strings listing alternative domains and subdomains for your SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have a maximum of 9 alternative names (in addition to the 1 primary domain). We do not support wildcards (<code>*.example.com</code>).</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_load_balancer_tls_certificate_request.CreateLoadBalancerTlsCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_load_balancer_tls_certificate_result.CreateLoadBalancerTlsCertificateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_load_balancer_tls_certificate

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_load_balancer_tls_certificate.async_create_load_balancer_tls_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_load_balancer_tls_certificate_request.CreateLoadBalancerTlsCertificateRequest = {
            "load_balancer_name": load_balancer_name,
            "certificate_name": certificate_name,
            "certificate_domain_name": certificate_domain_name,
        }
        if certificate_alternative_names is not None:
            input_["certificate_alternative_names"] = certificate_alternative_names
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        relational_database_blueprint_id: "capo_lightsail.types.string.string",
        relational_database_bundle_id: "capo_lightsail.types.string.string",
        master_database_name: "capo_lightsail.types.string.string",
        master_username: "capo_lightsail.types.string.string",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        availability_zone: Optional["capo_lightsail.types.string.string"] = None,
        master_user_password: Optional[
            "capo_lightsail.types.sensitive_string.SensitiveString"
        ] = None,
        preferred_backup_window: Optional["capo_lightsail.types.string.string"] = None,
        preferred_maintenance_window: Optional[
            "capo_lightsail.types.string.string"
        ] = None,
        publicly_accessible: Optional["capo_lightsail.types.boolean.boolean"] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_relational_database_result.CreateRelationalDatabaseResult":
        """<p>Creates a new database in Amazon Lightsail.</p> <p>The <code>create relational database</code> operation supports tag-based access control via request tags. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags\">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name to use for your new Lightsail database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>
            availability_zone: <p>The Availability Zone in which to create your new database. Use the <code>us-east-2a</code> case-sensitive format.</p> <p>You can get a list of Availability Zones by using the <code>get regions</code> operation. Be sure to add the <code>include relational database Availability Zones</code> parameter to your request.</p>
            relational_database_blueprint_id: <p>The blueprint ID for your new database. A blueprint describes the major engine version of a database.</p> <p>You can get a list of database blueprints IDs by using the <code>get relational database blueprints</code> operation.</p>
            relational_database_bundle_id: <p>The bundle ID for your new database. A bundle describes the performance specifications for your database.</p> <p>You can get a list of database bundle IDs by using the <code>get relational database bundles</code> operation.</p>
            master_database_name: <p>The meaning of this parameter differs according to the database engine you use.</p> <p> <b>MySQL</b> </p> <p>The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> <p>For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for <a href=\"https://dev.mysql.com/doc/refman/5.6/en/keywords.html\">MySQL 5.6</a>, <a href=\"https://dev.mysql.com/doc/refman/5.7/en/keywords.html\">MySQL 5.7</a>, and <a href=\"https://dev.mysql.com/doc/refman/8.0/en/keywords.html\">MySQL 8.0</a>.</p> </li> </ul> <p> <b>PostgreSQL</b> </p> <p>The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named <code>postgres</code> is created in the database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 63 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> <p>For more information about reserved words in PostgreSQL, see the SQL Key Words articles for <a href=\"https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html\">PostgreSQL 9.6</a>, <a href=\"https://www.postgresql.org/docs/10/sql-keywords-appendix.html\">PostgreSQL 10</a>, <a href=\"https://www.postgresql.org/docs/11/sql-keywords-appendix.html\">PostgreSQL 11</a>, and <a href=\"https://www.postgresql.org/docs/12/sql-keywords-appendix.html\">PostgreSQL 12</a>.</p> </li> </ul>
            master_username: <p>The name for the master user.</p> <p> <b>MySQL</b> </p> <p>Constraints:</p> <ul> <li> <p>Required for MySQL.</p> </li> <li> <p>Must be 1 to 16 letters or numbers. Can contain underscores.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> <p>For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for <a href=\"https://dev.mysql.com/doc/refman/5.6/en/keywords.html\">MySQL 5.6</a>, <a href=\"https://dev.mysql.com/doc/refman/5.7/en/keywords.html\">MySQL 5.7</a>, or <a href=\"https://dev.mysql.com/doc/refman/8.0/en/keywords.html\">MySQL 8.0</a>.</p> </li> </ul> <p> <b>PostgreSQL</b> </p> <p>Constraints:</p> <ul> <li> <p>Required for PostgreSQL.</p> </li> <li> <p>Must be 1 to 63 letters or numbers. Can contain underscores.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> <p>For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for <a href=\"https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html\">PostgreSQL 9.6</a>, <a href=\"https://www.postgresql.org/docs/10/sql-keywords-appendix.html\">PostgreSQL 10</a>, <a href=\"https://www.postgresql.org/docs/11/sql-keywords-appendix.html\">PostgreSQL 11</a>, and <a href=\"https://www.postgresql.org/docs/12/sql-keywords-appendix.html\">PostgreSQL 12</a>.</p> </li> </ul>
            master_user_password: <p>The password for the master user. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\". It cannot contain spaces.</p> <p> <b>MySQL</b> </p> <p>Constraints: Must contain from 8 to 41 characters.</p> <p> <b>PostgreSQL</b> </p> <p>Constraints: Must contain from 8 to 128 characters.</p>
            preferred_backup_window: <p>The daily time range during which automated backups are created for your new database if automated backups are enabled.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow\">Working With Backups</a> guide in the Amazon Relational Database Service documentation.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the <code>hh24:mi-hh24:mi</code> format.</p> <p>Example: <code>16:00-16:30</code> </p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur on your new database.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the <code>ddd:hh24:mi-ddd:hh24:mi</code> format.</p> </li> <li> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Example: <code>Tue:17:00-Tue:17:30</code> </p> </li> </ul>
            publicly_accessible: <p>Specifies the accessibility options for your new database. A value of <code>true</code> specifies a database that is available to resources outside of your Lightsail account. A value of <code>false</code> specifies a database that is available only to your Lightsail resources in the same region as your database.</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_relational_database_request.CreateRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_relational_database_result.CreateRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_relational_database.async_create_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_relational_database_request.CreateRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name,
            "relational_database_blueprint_id": relational_database_blueprint_id,
            "relational_database_bundle_id": relational_database_bundle_id,
            "master_database_name": master_database_name,
            "master_username": master_username,
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_relational_database_from_snapshot(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        availability_zone: Optional["capo_lightsail.types.string.string"] = None,
        publicly_accessible: Optional["capo_lightsail.types.boolean.boolean"] = None,
        relational_database_snapshot_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        relational_database_bundle_id: Optional[
            "capo_lightsail.types.string.string"
        ] = None,
        source_relational_database_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        restore_time: Optional["capo_lightsail.types.iso_date.IsoDate"] = None,
        use_latest_restorable_time: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_relational_database_from_snapshot_result.CreateRelationalDatabaseFromSnapshotResult":
        """<p>Creates a new database from an existing database snapshot in Amazon Lightsail.</p> <p>You can create a new database from a snapshot in if something goes wrong with your original database, or to change it to a different plan, such as a high availability or standard plan.</p> <p>The <code>create relational database from snapshot</code> operation supports tag-based access control via request tags and resource tags applied to the resource identified by relationalDatabaseSnapshotName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name to use for your new Lightsail database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>
            availability_zone: <p>The Availability Zone in which to create your new database. Use the <code>us-east-2a</code> case-sensitive format.</p> <p>You can get a list of Availability Zones by using the <code>get regions</code> operation. Be sure to add the <code>include relational database Availability Zones</code> parameter to your request.</p>
            publicly_accessible: <p>Specifies the accessibility options for your new database. A value of <code>true</code> specifies a database that is available to resources outside of your Lightsail account. A value of <code>false</code> specifies a database that is available only to your Lightsail resources in the same region as your database.</p>
            relational_database_snapshot_name: <p>The name of the database snapshot from which to create your new database.</p>
            relational_database_bundle_id: <p>The bundle ID for your new database. A bundle describes the performance specifications for your database.</p> <p>You can get a list of database bundle IDs by using the <code>get relational database bundles</code> operation.</p> <p>When creating a new database from a snapshot, you cannot choose a bundle that is smaller than the bundle of the source database.</p>
            source_relational_database_name: <p>The name of the source database.</p>
            restore_time: <p>The date and time to restore your database from.</p> <p>Constraints:</p> <ul> <li> <p>Must be before the latest restorable time for the database.</p> </li> <li> <p>Cannot be specified if the <code>use latest restorable time</code> parameter is <code>true</code>.</p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a restore time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the restore time.</p> </li> </ul>
            use_latest_restorable_time: <p>Specifies whether your database is restored from the latest backup time. A value of <code>true</code> restores from the latest backup time. </p> <p>Default: <code>false</code> </p> <p>Constraints: Cannot be specified if the <code>restore time</code> parameter is provided.</p>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_relational_database_from_snapshot_request.CreateRelationalDatabaseFromSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_relational_database_from_snapshot_result.CreateRelationalDatabaseFromSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_relational_database_from_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_relational_database_from_snapshot.async_create_relational_database_from_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_relational_database_from_snapshot_request.CreateRelationalDatabaseFromSnapshotRequest = {
            "relational_database_name": relational_database_name
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if relational_database_snapshot_name is not None:
            input_["relational_database_snapshot_name"] = (
                relational_database_snapshot_name
            )
        if relational_database_bundle_id is not None:
            input_["relational_database_bundle_id"] = relational_database_bundle_id
        if source_relational_database_name is not None:
            input_["source_relational_database_name"] = source_relational_database_name
        if restore_time is not None:
            input_["restore_time"] = restore_time
        if use_latest_restorable_time is not None:
            input_["use_latest_restorable_time"] = use_latest_restorable_time
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_relational_database_snapshot(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        relational_database_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.create_relational_database_snapshot_result.CreateRelationalDatabaseSnapshotResult":
        """<p>Creates a snapshot of your database in Amazon Lightsail. You can use snapshots for backups, to make copies of a database, and to save data before deleting a database.</p> <p>The <code>create relational database snapshot</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of the database on which to base your new snapshot.</p>
            relational_database_snapshot_name: <p>The name for your new database snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>
            tags: <p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.create_relational_database_snapshot_request.CreateRelationalDatabaseSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.create_relational_database_snapshot_result.CreateRelationalDatabaseSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.create_relational_database_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.create_relational_database_snapshot.async_create_relational_database_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.create_relational_database_snapshot_request.CreateRelationalDatabaseSnapshotRequest = {
            "relational_database_name": relational_database_name,
            "relational_database_snapshot_name": relational_database_snapshot_name,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_alarm(
        self,
        alarm_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_alarm_result.DeleteAlarmResult":
        """<p>Deletes an alarm.</p> <p>An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms">Alarms in Amazon Lightsail</a>.</p>

        Args:
            alarm_name: <p>The name of the alarm to delete.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_alarm_request.DeleteAlarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_alarm_result.DeleteAlarmResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_alarm

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_alarm.async_delete_alarm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_alarm_request.DeleteAlarmRequest = {
            "alarm_name": alarm_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_auto_snapshot(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        date: "capo_lightsail.types.auto_snapshot_date.AutoSnapshotDate",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_auto_snapshot_result.DeleteAutoSnapshotResult":
        """<p>Deletes an automatic snapshot of an instance or disk. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            resource_name: <p>The name of the source instance or disk from which to delete the automatic snapshot.</p>
            date: <p>The date of the automatic snapshot to delete in <code>YYYY-MM-DD</code> format. Use the <code>get auto snapshots</code> operation to get the available automatic snapshots for a resource.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_auto_snapshot_request.DeleteAutoSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_auto_snapshot_result.DeleteAutoSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_auto_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_auto_snapshot.async_delete_auto_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_auto_snapshot_request.DeleteAutoSnapshotRequest = {
            "resource_name": resource_name,
            "date": date,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        force_delete: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.delete_bucket_result.DeleteBucketResult":
        """<p>Deletes a Amazon Lightsail bucket.</p> <note> <p>When you delete your bucket, the bucket name is released and can be reused for a new bucket in your account or another Amazon Web Services account.</p> </note>

        Args:
            bucket_name: <p>The name of the bucket to delete.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBuckets.html">GetBuckets</a> action to get a list of bucket names that you can specify.</p>
            force_delete: <p>A Boolean value that indicates whether to force delete the bucket.</p> <p>You must force delete the bucket if it has one of the following conditions:</p> <ul> <li> <p>The bucket is the origin of a distribution.</p> </li> <li> <p>The bucket has instances that were granted access to it using the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html">SetResourceAccessForBucket</a> action.</p> </li> <li> <p>The bucket has objects.</p> </li> <li> <p>The bucket has access keys.</p> </li> </ul> <important> <p>Force deleting a bucket might impact other resources that rely on the bucket, such as instances, distributions, or software that use the issued access keys.</p> </important>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_bucket_request.DeleteBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_bucket_result.DeleteBucketResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_bucket

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_bucket.async_delete_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_bucket_request.DeleteBucketRequest = {
            "bucket_name": bucket_name
        }
        if force_delete is not None:
            input_["force_delete"] = force_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bucket_access_key(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        access_key_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_bucket_access_key_result.DeleteBucketAccessKeyResult":
        """<p>Deletes an access key for the specified Amazon Lightsail bucket.</p> <p>We recommend that you delete an access key if the secret access key is compromised.</p> <p>For more information about access keys, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-creating-bucket-access-keys">Creating access keys for a bucket in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Args:
            bucket_name: <p>The name of the bucket that the access key belongs to.</p>
            access_key_id: <p>The ID of the access key to delete.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketAccessKeys.html">GetBucketAccessKeys</a> action to get a list of access key IDs that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_bucket_access_key_request.DeleteBucketAccessKeyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_bucket_access_key_result.DeleteBucketAccessKeyResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_bucket_access_key

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_bucket_access_key.async_delete_bucket_access_key(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_bucket_access_key_request.DeleteBucketAccessKeyRequest = {
            "bucket_name": bucket_name,
            "access_key_id": access_key_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_certificate(
        self,
        certificate_name: "capo_lightsail.types.certificate_name.CertificateName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_certificate_result.DeleteCertificateResult":
        """<p>Deletes an SSL/TLS certificate for your Amazon Lightsail content delivery network (CDN) distribution.</p> <p>Certificates that are currently attached to a distribution cannot be deleted. Use the <code>DetachCertificateFromDistribution</code> action to detach a certificate from a distribution.</p>

        Args:
            certificate_name: <p>The name of the certificate to delete.</p> <p>Use the <code>GetCertificates</code> action to get a list of certificate names that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_certificate_request.DeleteCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_certificate_result.DeleteCertificateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_certificate

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_certificate.async_delete_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_certificate_request.DeleteCertificateRequest = {
            "certificate_name": certificate_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_contact_method(
        self,
        protocol: "capo_lightsail.types.contact_protocol.ContactProtocol",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_contact_method_result.DeleteContactMethodResult":
        """<p>Deletes a contact method.</p> <p>A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications">Notifications in Amazon Lightsail</a>.</p>

        Args:
            protocol: <p>The protocol that will be deleted, such as <code>Email</code> or <code>SMS</code> (text messaging).</p> <note> <p>To delete an <code>Email</code> and an <code>SMS</code> contact method if you added both, you must run separate <code>DeleteContactMethod</code> actions to delete each protocol.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_contact_method_request.DeleteContactMethodRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_contact_method_result.DeleteContactMethodResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_contact_method

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_contact_method.async_delete_contact_method(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_contact_method_request.DeleteContactMethodRequest = {
            "protocol": protocol
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_container_image(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        image: "capo_lightsail.types.string.string",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> (
        "capo_lightsail.types.delete_container_image_result.DeleteContainerImageResult"
    ):
        """<p>Deletes a container image that is registered to your Amazon Lightsail container service.</p>

        Args:
            service_name: <p>The name of the container service for which to delete a registered container image.</p>
            image: <p>The name of the container image to delete from the container service.</p> <p>Use the <code>GetContainerImages</code> action to get the name of the container images that are registered to a container service.</p> <note> <p>Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (<code>:</code>). For example, <code>:container-service-1.mystaticwebsite.1</code>. Container images sourced from a public registry like Docker Hub don't start with a colon. For example, <code>nginx:latest</code> or <code>nginx</code>.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_container_image_request.DeleteContainerImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_container_image_result.DeleteContainerImageResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_container_image

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_container_image.async_delete_container_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_container_image_request.DeleteContainerImageRequest = {
            "service_name": service_name,
            "image": image,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_container_service(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_container_service_result.DeleteContainerServiceResult":
        """<p>Deletes your Amazon Lightsail container service.</p>

        Args:
            service_name: <p>The name of the container service to delete.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_container_service_request.DeleteContainerServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_container_service_result.DeleteContainerServiceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_container_service

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_container_service.async_delete_container_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_container_service_request.DeleteContainerServiceRequest = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_disk(
        self,
        disk_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        force_delete_add_ons: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.delete_disk_result.DeleteDiskResult":
        """<p>Deletes the specified block storage disk. The disk must be in the <code>available</code> state (not attached to a Lightsail instance).</p> <note> <p>The disk may remain in the <code>deleting</code> state for several minutes.</p> </note> <p>The <code>delete disk</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>disk name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_name: <p>The unique name of the disk you want to delete (<code>my-disk</code>).</p>
            force_delete_add_ons: <p>A Boolean value to indicate whether to delete all add-ons for the disk.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_disk_request.DeleteDiskRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_disk_result.DeleteDiskResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_disk

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_disk.async_delete_disk(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_disk_request.DeleteDiskRequest = {
            "disk_name": disk_name
        }
        if force_delete_add_ons is not None:
            input_["force_delete_add_ons"] = force_delete_add_ons

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_disk_snapshot(
        self,
        disk_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_disk_snapshot_result.DeleteDiskSnapshotResult":
        """<p>Deletes the specified disk snapshot.</p> <p>When you make periodic snapshots of a disk, the snapshots are incremental, and only the blocks on the device that have changed since your last snapshot are saved in the new snapshot. When you delete a snapshot, only the data not needed for any other snapshot is removed. So regardless of which prior snapshots have been deleted, all active snapshots will have access to all the information needed to restore the disk.</p> <p>The <code>delete disk snapshot</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>disk snapshot name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_snapshot_name: <p>The name of the disk snapshot you want to delete (<code>my-disk-snapshot</code>).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_disk_snapshot_request.DeleteDiskSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_disk_snapshot_result.DeleteDiskSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_disk_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_disk_snapshot.async_delete_disk_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_disk_snapshot_request.DeleteDiskSnapshotRequest = {
            "disk_snapshot_name": disk_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_distribution(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        distribution_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_lightsail.types.delete_distribution_result.DeleteDistributionResult":
        """<p>Deletes your Amazon Lightsail content delivery network (CDN) distribution.</p>

        Args:
            distribution_name: <p>The name of the distribution to delete.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_distribution_request.DeleteDistributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_distribution_result.DeleteDistributionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_distribution

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_distribution.async_delete_distribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_distribution_request.DeleteDistributionRequest = {}
        if distribution_name is not None:
            input_["distribution_name"] = distribution_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain(
        self,
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_domain_result.DeleteDomainResult":
        """<p>Deletes the specified domain recordset and all of its domain records.</p> <p>The <code>delete domain</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>domain name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            domain_name: <p>The specific domain name to delete.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_domain_request.DeleteDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_domain_result.DeleteDomainResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_domain

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_domain_request.DeleteDomainRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain_entry(
        self,
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        domain_entry: "capo_lightsail.types.domain_entry.DomainEntry",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_domain_entry_result.DeleteDomainEntryResult":
        """<p>Deletes a specific domain entry.</p> <p>The <code>delete domain entry</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>domain name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            domain_name: <p>The name of the domain entry to delete.</p>
            domain_entry: <p>An array of key-value pairs containing information about your domain entries.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_domain_entry_request.DeleteDomainEntryRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_domain_entry_result.DeleteDomainEntryResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_domain_entry

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_domain_entry.async_delete_domain_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_domain_entry_request.DeleteDomainEntryRequest = {
            "domain_name": domain_name,
            "domain_entry": domain_entry,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_instance(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        force_delete_add_ons: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.delete_instance_result.DeleteInstanceResult":
        """<p>Deletes an Amazon Lightsail instance.</p> <p>The <code>delete instance</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>instance name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_name: <p>The name of the instance to delete.</p>
            force_delete_add_ons: <p>A Boolean value to indicate whether to delete all add-ons for the instance.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_instance_request.DeleteInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_instance_result.DeleteInstanceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_instance

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_instance.async_delete_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_instance_request.DeleteInstanceRequest = {
            "instance_name": instance_name
        }
        if force_delete_add_ons is not None:
            input_["force_delete_add_ons"] = force_delete_add_ons

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_instance_snapshot(
        self,
        instance_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_instance_snapshot_result.DeleteInstanceSnapshotResult":
        """<p>Deletes a specific snapshot of a virtual private server (or <i>instance</i>).</p> <p>The <code>delete instance snapshot</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>instance snapshot name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_snapshot_name: <p>The name of the snapshot to delete.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_instance_snapshot_request.DeleteInstanceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_instance_snapshot_result.DeleteInstanceSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_instance_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_instance_snapshot.async_delete_instance_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_instance_snapshot_request.DeleteInstanceSnapshotRequest = {
            "instance_snapshot_name": instance_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_key_pair(
        self,
        key_pair_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        expected_fingerprint: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.delete_key_pair_result.DeleteKeyPairResult":
        """<p>Deletes the specified key pair by removing the public key from Amazon Lightsail.</p> <p>You can delete key pairs that were created using the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_ImportKeyPair.html">ImportKeyPair</a> and <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateKeyPair.html">CreateKeyPair</a> actions, as well as the Lightsail default key pair. A new default key pair will not be created unless you launch an instance without specifying a custom key pair, or you call the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_DownloadDefaultKeyPair.html">DownloadDefaultKeyPair</a> API. </p> <p>The <code>delete key pair</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>key pair name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            key_pair_name: <p>The name of the key pair to delete.</p>
            expected_fingerprint: <p>The RSA fingerprint of the Lightsail default key pair to delete.</p> <note> <p>The <code>expectedFingerprint</code> parameter is required only when specifying to delete a Lightsail default key pair.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_key_pair_request.DeleteKeyPairRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_key_pair_result.DeleteKeyPairResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_key_pair

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_key_pair.async_delete_key_pair(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_key_pair_request.DeleteKeyPairRequest = {
            "key_pair_name": key_pair_name
        }
        if expected_fingerprint is not None:
            input_["expected_fingerprint"] = expected_fingerprint

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_known_host_keys(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_known_host_keys_result.DeleteKnownHostKeysResult":
        """<p>Deletes the known host key or certificate used by the Amazon Lightsail browser-based SSH or RDP clients to authenticate an instance. This operation enables the Lightsail browser-based SSH or RDP clients to connect to the instance after a host key mismatch.</p> <important> <p>Perform this operation only if you were expecting the host key or certificate mismatch or if you are familiar with the new host key or certificate on the instance. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection">Troubleshooting connection issues when using the Amazon Lightsail browser-based SSH or RDP client</a>.</p> </important>

        Args:
            instance_name: <p>The name of the instance for which you want to reset the host key or certificate.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_known_host_keys_request.DeleteKnownHostKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_known_host_keys_result.DeleteKnownHostKeysResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_known_host_keys

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_known_host_keys.async_delete_known_host_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_known_host_keys_request.DeleteKnownHostKeysRequest = {
            "instance_name": instance_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_load_balancer(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_load_balancer_result.DeleteLoadBalancerResult":
        """<p>Deletes a Lightsail load balancer and all its associated SSL/TLS certificates. Once the load balancer is deleted, you will need to create a new load balancer, create a new certificate, and verify domain ownership again.</p> <p>The <code>delete load balancer</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer you want to delete.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_load_balancer_request.DeleteLoadBalancerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_load_balancer_result.DeleteLoadBalancerResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_load_balancer

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_load_balancer.async_delete_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_load_balancer_request.DeleteLoadBalancerRequest = {
            "load_balancer_name": load_balancer_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_load_balancer_tls_certificate(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        certificate_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        force: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.delete_load_balancer_tls_certificate_result.DeleteLoadBalancerTlsCertificateResult":
        """<p>Deletes an SSL/TLS certificate associated with a Lightsail load balancer.</p> <p>The <code>DeleteLoadBalancerTlsCertificate</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The load balancer name.</p>
            certificate_name: <p>The SSL/TLS certificate name.</p>
            force: <p>When <code>true</code>, forces the deletion of an SSL/TLS certificate.</p> <p>There can be two certificates associated with a Lightsail load balancer: the primary and the backup. The <code>force</code> parameter is required when the primary SSL/TLS certificate is in use by an instance attached to the load balancer.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_load_balancer_tls_certificate_request.DeleteLoadBalancerTlsCertificateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_load_balancer_tls_certificate_result.DeleteLoadBalancerTlsCertificateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_load_balancer_tls_certificate

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_load_balancer_tls_certificate.async_delete_load_balancer_tls_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_load_balancer_tls_certificate_request.DeleteLoadBalancerTlsCertificateRequest = {
            "load_balancer_name": load_balancer_name,
            "certificate_name": certificate_name,
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

    async def delete_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        skip_final_snapshot: Optional["capo_lightsail.types.boolean.boolean"] = None,
        final_relational_database_snapshot_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_lightsail.types.delete_relational_database_result.DeleteRelationalDatabaseResult":
        """<p>Deletes a database in Amazon Lightsail.</p> <p>The <code>delete relational database</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of the database that you are deleting.</p>
            skip_final_snapshot: <p>Determines whether a final database snapshot is created before your database is deleted. If <code>true</code> is specified, no database snapshot is created. If <code>false</code> is specified, a database snapshot is created before your database is deleted.</p> <p>You must specify the <code>final relational database snapshot name</code> parameter if the <code>skip final snapshot</code> parameter is <code>false</code>.</p> <p>Default: <code>false</code> </p>
            final_relational_database_snapshot_name: <p>The name of the database snapshot created if <code>skip final snapshot</code> is <code>false</code>, which is the default value for that parameter.</p> <note> <p>Specifying this parameter and also specifying the <code>skip final snapshot</code> parameter to <code>true</code> results in an error.</p> </note> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_relational_database_request.DeleteRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_relational_database_result.DeleteRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_relational_database.async_delete_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_relational_database_request.DeleteRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name
        }
        if skip_final_snapshot is not None:
            input_["skip_final_snapshot"] = skip_final_snapshot
        if final_relational_database_snapshot_name is not None:
            input_["final_relational_database_snapshot_name"] = (
                final_relational_database_snapshot_name
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_relational_database_snapshot(
        self,
        relational_database_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.delete_relational_database_snapshot_result.DeleteRelationalDatabaseSnapshotResult":
        """<p>Deletes a database snapshot in Amazon Lightsail.</p> <p>The <code>delete relational database snapshot</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_snapshot_name: <p>The name of the database snapshot that you are deleting.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.delete_relational_database_snapshot_request.DeleteRelationalDatabaseSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.delete_relational_database_snapshot_result.DeleteRelationalDatabaseSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.delete_relational_database_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.delete_relational_database_snapshot.async_delete_relational_database_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.delete_relational_database_snapshot_request.DeleteRelationalDatabaseSnapshotRequest = {
            "relational_database_snapshot_name": relational_database_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detach_certificate_from_distribution(
        self,
        distribution_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.detach_certificate_from_distribution_result.DetachCertificateFromDistributionResult":
        """<p>Detaches an SSL/TLS certificate from your Amazon Lightsail content delivery network (CDN) distribution.</p> <p>After the certificate is detached, your distribution stops accepting traffic for all of the domains that are associated with the certificate.</p>

        Args:
            distribution_name: <p>The name of the distribution from which to detach the certificate.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.detach_certificate_from_distribution_request.DetachCertificateFromDistributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.detach_certificate_from_distribution_result.DetachCertificateFromDistributionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.detach_certificate_from_distribution

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.detach_certificate_from_distribution.async_detach_certificate_from_distribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.detach_certificate_from_distribution_request.DetachCertificateFromDistributionRequest = {
            "distribution_name": distribution_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detach_disk(
        self,
        disk_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.detach_disk_result.DetachDiskResult":
        """<p>Detaches a stopped block storage disk from a Lightsail instance. Make sure to unmount any file systems on the device within your operating system before stopping the instance and detaching the disk.</p> <p>The <code>detach disk</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>disk name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            disk_name: <p>The unique name of the disk you want to detach from your instance (<code>my-disk</code>).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.detach_disk_request.DetachDiskRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.detach_disk_result.DetachDiskResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.detach_disk

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.detach_disk.async_detach_disk(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.detach_disk_request.DetachDiskRequest = {
            "disk_name": disk_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detach_instances_from_load_balancer(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        instance_names: "capo_lightsail.types.resource_name_list.ResourceNameList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.detach_instances_from_load_balancer_result.DetachInstancesFromLoadBalancerResult":
        """<p>Detaches the specified instances from a Lightsail load balancer.</p> <p>This operation waits until the instances are no longer needed before they are detached from the load balancer.</p> <p>The <code>detach instances from load balancer</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The name of the Lightsail load balancer.</p>
            instance_names: <p>An array of strings containing the names of the instances you want to detach from the load balancer.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.detach_instances_from_load_balancer_request.DetachInstancesFromLoadBalancerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.detach_instances_from_load_balancer_result.DetachInstancesFromLoadBalancerResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.detach_instances_from_load_balancer

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.detach_instances_from_load_balancer.async_detach_instances_from_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.detach_instances_from_load_balancer_request.DetachInstancesFromLoadBalancerRequest = {
            "load_balancer_name": load_balancer_name,
            "instance_names": instance_names,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def detach_static_ip(
        self,
        static_ip_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.detach_static_ip_result.DetachStaticIpResult":
        """<p>Detaches a static IP from the Amazon Lightsail instance to which it is attached.</p>

        Args:
            static_ip_name: <p>The name of the static IP to detach from the instance.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.detach_static_ip_request.DetachStaticIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.detach_static_ip_result.DetachStaticIpResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.detach_static_ip

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.detach_static_ip.async_detach_static_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.detach_static_ip_request.DetachStaticIpRequest = {
            "static_ip_name": static_ip_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_add_on(
        self,
        add_on_type: "capo_lightsail.types.add_on_type.AddOnType",
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.disable_add_on_result.DisableAddOnResult":
        """<p>Disables an add-on for an Amazon Lightsail resource. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            add_on_type: <p>The add-on type to disable.</p>
            resource_name: <p>The name of the source resource for which to disable the add-on.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.disable_add_on_request.DisableAddOnRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.disable_add_on_result.DisableAddOnResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.disable_add_on

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.disable_add_on.async_disable_add_on(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.disable_add_on_request.DisableAddOnRequest = {
            "add_on_type": add_on_type,
            "resource_name": resource_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def download_default_key_pair(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.download_default_key_pair_result.DownloadDefaultKeyPairResult":
        """<p>Downloads the regional Amazon Lightsail default key pair.</p> <p>This action also creates a Lightsail default key pair if a default key pair does not currently exist in the Amazon Web Services Region.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.download_default_key_pair_request.DownloadDefaultKeyPairRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.download_default_key_pair_result.DownloadDefaultKeyPairResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.download_default_key_pair

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.download_default_key_pair.async_download_default_key_pair(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.download_default_key_pair_request.DownloadDefaultKeyPairRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_add_on(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        add_on_request: "capo_lightsail.types.add_on_request.AddOnRequest",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.enable_add_on_result.EnableAddOnResult":
        """<p>Enables or modifies an add-on for an Amazon Lightsail resource. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            resource_name: <p>The name of the source resource for which to enable or modify the add-on.</p>
            add_on_request: <p>An array of strings representing the add-on to enable or modify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.enable_add_on_request.EnableAddOnRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.enable_add_on_result.EnableAddOnResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.enable_add_on

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.enable_add_on.async_enable_add_on(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.enable_add_on_request.EnableAddOnRequest = {
            "resource_name": resource_name,
            "add_on_request": add_on_request,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_snapshot(
        self,
        source_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.export_snapshot_result.ExportSnapshotResult":
        """<p>Exports an Amazon Lightsail instance or block storage disk snapshot to Amazon Elastic Compute Cloud (Amazon EC2). This operation results in an export snapshot record that can be used with the <code>create cloud formation stack</code> operation to create new Amazon EC2 instances.</p> <p>Exported instance snapshots appear in Amazon EC2 as Amazon Machine Images (AMIs), and the instance system disk appears as an Amazon Elastic Block Store (Amazon EBS) volume. Exported disk snapshots appear in Amazon EC2 as Amazon EBS volumes. Snapshots are exported to the same Amazon Web Services Region in Amazon EC2 as the source Lightsail snapshot.</p> <p></p> <p>The <code>export snapshot</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>source snapshot name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p> <note> <p>Use the <code>get instance snapshots</code> or <code>get disk snapshots</code> operations to get a list of snapshots that you can export to Amazon EC2.</p> </note>

        Args:
            source_snapshot_name: <p>The name of the instance or disk snapshot to be exported to Amazon EC2.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.export_snapshot_request.ExportSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.export_snapshot_result.ExportSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.export_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.export_snapshot.async_export_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.export_snapshot_request.ExportSnapshotRequest = {
            "source_snapshot_name": source_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_active_names(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_active_names_result.GetActiveNamesResult":
        """<p>Returns the names of all active (not deleted) resources.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetActiveNames</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_active_names_request.GetActiveNamesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_active_names_result.GetActiveNamesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_active_names

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_active_names.async_get_active_names(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_active_names_request.GetActiveNamesRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_alarms(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        alarm_name: Optional["capo_lightsail.types.resource_name.ResourceName"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
        monitored_resource_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_lightsail.types.get_alarms_result.GetAlarmsResult":
        """<p>Returns information about the configured alarms. Specify an alarm name in your request to return information about a specific alarm, or specify a monitored resource name to return information about all alarms for a specific resource.</p> <p>An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms">Alarms in Amazon Lightsail</a>.</p>

        Args:
            alarm_name: <p>The name of the alarm.</p> <p>Specify an alarm name to return information about a specific alarm.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetAlarms</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>
            monitored_resource_name: <p>The name of the Lightsail resource being monitored by the alarm.</p> <p>Specify a monitored resource name to return information about all alarms for a specific resource.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_alarms_request.GetAlarmsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_alarms_result.GetAlarmsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_alarms

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_alarms.async_get_alarms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_alarms_request.GetAlarmsRequest = {}
        if alarm_name is not None:
            input_["alarm_name"] = alarm_name
        if page_token is not None:
            input_["page_token"] = page_token
        if monitored_resource_name is not None:
            input_["monitored_resource_name"] = monitored_resource_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_auto_snapshots(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_auto_snapshots_result.GetAutoSnapshotsResult":
        """<p>Returns the available automatic snapshots for an instance or disk. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            resource_name: <p>The name of the source instance or disk from which to get automatic snapshot information.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_auto_snapshots_request.GetAutoSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_auto_snapshots_result.GetAutoSnapshotsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_auto_snapshots

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_auto_snapshots.async_get_auto_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_auto_snapshots_request.GetAutoSnapshotsRequest = {
            "resource_name": resource_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_blueprints(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        include_inactive: Optional["capo_lightsail.types.boolean.boolean"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
        app_category: Optional["capo_lightsail.types.app_category.AppCategory"] = None,
    ) -> "capo_lightsail.types.get_blueprints_result.GetBlueprintsResult":
        """<p>Returns the list of available instance images, or <i>blueprints</i>. You can use a blueprint to create a new instance already running a specific operating system, as well as a preinstalled app or development stack. The software each instance is running depends on the blueprint image you choose.</p> <note> <p>Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.</p> </note>

        Args:
            include_inactive: <p>A Boolean value that indicates whether to include inactive (unavailable) blueprints in the response of your request.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetBlueprints</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>
            app_category: <p>Returns a list of blueprints that are specific to Lightsail for Research.</p> <important> <p>You must use this parameter to view Lightsail for Research blueprints.</p> </important>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_blueprints_request.GetBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_blueprints_result.GetBlueprintsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_blueprints

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_blueprints.async_get_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_blueprints_request.GetBlueprintsRequest = {}
        if include_inactive is not None:
            input_["include_inactive"] = include_inactive
        if page_token is not None:
            input_["page_token"] = page_token
        if app_category is not None:
            input_["app_category"] = app_category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_access_keys(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_bucket_access_keys_result.GetBucketAccessKeysResult":
        """<p>Returns the existing access key IDs for the specified Amazon Lightsail bucket.</p> <important> <p>This action does not return the secret access key value of an access key. You can get a secret access key only when you create it from the response of the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucketAccessKey.html">CreateBucketAccessKey</a> action. If you lose the secret access key, you must create a new access key.</p> </important>

        Args:
            bucket_name: <p>The name of the bucket for which to return access keys.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_bucket_access_keys_request.GetBucketAccessKeysRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_bucket_access_keys_result.GetBucketAccessKeysResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_bucket_access_keys

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_bucket_access_keys.async_get_bucket_access_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_bucket_access_keys_request.GetBucketAccessKeysRequest = {
            "bucket_name": bucket_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_bundles(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        include_inactive: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.get_bucket_bundles_result.GetBucketBundlesResult":
        """<p>Returns the bundles that you can apply to a Amazon Lightsail bucket.</p> <p>The bucket bundle specifies the monthly cost, storage quota, and data transfer quota for a bucket.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html">UpdateBucketBundle</a> action to update the bundle for a bucket.</p>

        Args:
            include_inactive: <p>A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_bucket_bundles_request.GetBucketBundlesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_bucket_bundles_result.GetBucketBundlesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_bucket_bundles

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_bucket_bundles.async_get_bucket_bundles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_bucket_bundles_request.GetBucketBundlesRequest = {}
        if include_inactive is not None:
            input_["include_inactive"] = include_inactive

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bucket_metric_data(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        metric_name: "capo_lightsail.types.bucket_metric_name.BucketMetricName",
        start_time: "capo_lightsail.types.iso_date.IsoDate",
        end_time: "capo_lightsail.types.iso_date.IsoDate",
        period: "capo_lightsail.types.metric_period.MetricPeriod",
        statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList",
        unit: "capo_lightsail.types.metric_unit.MetricUnit",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_bucket_metric_data_result.GetBucketMetricDataResult":
        """<p>Returns the data points of a specific metric for an Amazon Lightsail bucket.</p> <p>Metrics report the utilization of a bucket. View and collect metric data regularly to monitor the number of objects stored in a bucket (including object versions) and the storage space used by those objects.</p>

        Args:
            bucket_name: <p>The name of the bucket for which to get metric data.</p>
            metric_name: <p>The metric for which you want to return information.</p> <p>Valid bucket metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.</p> <note> <p>These bucket metrics are reported once per day.</p> </note> <ul> <li> <p> <b> <code>BucketSizeBytes</code> </b> - The amount of data in bytes stored in a bucket. This value is calculated by summing the size of all objects in the bucket (including object versions), including the size of all parts for all incomplete multipart uploads to the bucket.</p> <p>Statistics: The most useful statistic is <code>Maximum</code>.</p> <p>Unit: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>NumberOfObjects</code> </b> - The total number of objects stored in a bucket. This value is calculated by counting all objects in the bucket (including object versions) and the total number of parts for all incomplete multipart uploads to the bucket.</p> <p>Statistics: The most useful statistic is <code>Average</code>.</p> <p>Unit: The published unit is <code>Count</code>.</p> </li> </ul>
            start_time: <p>The timestamp indicating the earliest data to be returned.</p>
            end_time: <p>The timestamp indicating the latest data to be returned.</p>
            period: <p>The granularity, in seconds, of the returned data points.</p> <note> <p>Bucket storage metrics are reported once per day. Therefore, you should specify a period of 86400 seconds, which is the number of seconds in a day.</p> </note>
            statistics: <p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - The sum of all values submitted for the matching metric. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of <code>Sum</code> / <code>SampleCount</code> during the specified period. By comparing this statistic with the <code>Minimum</code> and <code>Maximum</code> values, you can determine the full scope of a metric and how close the average use is to the <code>Minimum</code> and <code>Maximum</code> values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>
            unit: <p>The unit for the metric data request.</p> <p>Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_bucket_metric_data_request.GetBucketMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_bucket_metric_data_result.GetBucketMetricDataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_bucket_metric_data

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_bucket_metric_data.async_get_bucket_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_bucket_metric_data_request.GetBucketMetricDataRequest = {
            "bucket_name": bucket_name,
            "metric_name": metric_name,
            "start_time": start_time,
            "end_time": end_time,
            "period": period,
            "statistics": statistics,
            "unit": unit,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_buckets(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        bucket_name: Optional["capo_lightsail.types.bucket_name.BucketName"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
        include_connected_resources: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        include_cors: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.get_buckets_result.GetBucketsResult":
        """<p>Returns information about one or more Amazon Lightsail buckets. The information returned includes the synchronization status of the Amazon Simple Storage Service (Amazon S3) account-level block public access feature for your Lightsail buckets.</p> <p>For more information about buckets, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/buckets-in-amazon-lightsail">Buckets in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Args:
            bucket_name: <p>The name of the bucket for which to return information.</p> <p>When omitted, the response includes all of your buckets in the Amazon Web Services Region where the request is made.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetBuckets</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>
            include_connected_resources: <p>A Boolean value that indicates whether to include Lightsail instances that were given access to the bucket using the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html">SetResourceAccessForBucket</a> action.</p>
            include_cors: <p>A Boolean value that indicates whether to include Lightsail bucket CORS configuration in the response. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html">Configuring cross-origin resource sharing (CORS)</a>.</p> <note> <p>This parameter is only supported when getting a single bucket with <code>bucketName</code> specified. The default value for this parameter is <code>False</code>.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_buckets_request.GetBucketsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_buckets_result.GetBucketsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_buckets

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_buckets.async_get_buckets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_buckets_request.GetBucketsRequest = {}
        if bucket_name is not None:
            input_["bucket_name"] = bucket_name
        if page_token is not None:
            input_["page_token"] = page_token
        if include_connected_resources is not None:
            input_["include_connected_resources"] = include_connected_resources
        if include_cors is not None:
            input_["include_cors"] = include_cors

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_bundles(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        include_inactive: Optional["capo_lightsail.types.boolean.boolean"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
        app_category: Optional["capo_lightsail.types.app_category.AppCategory"] = None,
    ) -> "capo_lightsail.types.get_bundles_result.GetBundlesResult":
        """<p>Returns the bundles that you can apply to an Amazon Lightsail instance when you create it.</p> <p>A bundle describes the specifications of an instance, such as the monthly cost, amount of memory, the number of vCPUs, amount of storage space, and monthly network data transfer quota.</p> <note> <p>Bundles are referred to as <i>instance plans</i> in the Lightsail console.</p> </note>

        Args:
            include_inactive: <p>A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetBundles</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>
            app_category: <p>Returns a list of bundles that are specific to Lightsail for Research.</p> <important> <p>You must use this parameter to view Lightsail for Research bundles.</p> </important>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_bundles_request.GetBundlesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_bundles_result.GetBundlesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_bundles

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_bundles.async_get_bundles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_bundles_request.GetBundlesRequest = {}
        if include_inactive is not None:
            input_["include_inactive"] = include_inactive
        if page_token is not None:
            input_["page_token"] = page_token
        if app_category is not None:
            input_["app_category"] = app_category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_certificates(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        certificate_statuses: Optional[
            "capo_lightsail.types.certificate_status_list.CertificateStatusList"
        ] = None,
        include_certificate_details: Optional[
            "capo_lightsail.types.include_certificate_details.IncludeCertificateDetails"
        ] = None,
        certificate_name: Optional[
            "capo_lightsail.types.certificate_name.CertificateName"
        ] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_certificates_result.GetCertificatesResult":
        """<p>Returns information about one or more Amazon Lightsail SSL/TLS certificates.</p> <note> <p>To get a summary of a certificate, omit <code>includeCertificateDetails</code> from your request. The response will include only the certificate Amazon Resource Name (ARN), certificate name, domain name, and tags.</p> </note>

        Args:
            certificate_statuses: <p>The status of the certificates for which to return information.</p> <p>For example, specify <code>ISSUED</code> to return only certificates with an <code>ISSUED</code> status.</p> <p>When omitted, the response includes all of your certificates in the Amazon Web Services Region where the request is made, regardless of their current status.</p>
            include_certificate_details: <p>Indicates whether to include detailed information about the certificates in the response.</p> <p>When omitted, the response includes only the certificate names, Amazon Resource Names (ARNs), domain names, and tags.</p>
            certificate_name: <p>The name for the certificate for which to return information.</p> <p>When omitted, the response includes all of your certificates in the Amazon Web Services Region where the request is made.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetCertificates</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_certificates_request.GetCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_certificates_result.GetCertificatesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_certificates

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_certificates.async_get_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_certificates_request.GetCertificatesRequest = {}
        if certificate_statuses is not None:
            input_["certificate_statuses"] = certificate_statuses
        if include_certificate_details is not None:
            input_["include_certificate_details"] = include_certificate_details
        if certificate_name is not None:
            input_["certificate_name"] = certificate_name
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cloud_formation_stack_records(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_cloud_formation_stack_records_result.GetCloudFormationStackRecordsResult":
        """<p>Returns the CloudFormation stack record created as a result of the <code>create cloud formation stack</code> operation.</p> <p>An AWS CloudFormation stack is used to create a new Amazon EC2 instance from an exported Lightsail snapshot.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetClouFormationStackRecords</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_cloud_formation_stack_records_request.GetCloudFormationStackRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_cloud_formation_stack_records_result.GetCloudFormationStackRecordsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_cloud_formation_stack_records

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_cloud_formation_stack_records.async_get_cloud_formation_stack_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_cloud_formation_stack_records_request.GetCloudFormationStackRecordsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_contact_methods(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        protocols: Optional[
            "capo_lightsail.types.contact_protocols_list.ContactProtocolsList"
        ] = None,
    ) -> "capo_lightsail.types.get_contact_methods_result.GetContactMethodsResult":
        """<p>Returns information about the configured contact methods. Specify a protocol in your request to return information about a specific contact method.</p> <p>A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications">Notifications in Amazon Lightsail</a>.</p>

        Args:
            protocols: <p>The protocols used to send notifications, such as <code>Email</code>, or <code>SMS</code> (text messaging).</p> <p>Specify a protocol in your request to return information about a specific contact method protocol.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_contact_methods_request.GetContactMethodsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_contact_methods_result.GetContactMethodsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_contact_methods

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_contact_methods.async_get_contact_methods(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_contact_methods_request.GetContactMethodsRequest = {}
        if protocols is not None:
            input_["protocols"] = protocols

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_api_metadata(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.get_container_api_metadata_result.GetContainerAPIMetadataResult":
        """<p>Returns information about Amazon Lightsail containers, such as the current version of the Lightsail Control (lightsailctl) plugin.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_api_metadata_request.GetContainerAPIMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_container_api_metadata_result.GetContainerAPIMetadataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_api_metadata

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_api_metadata.async_get_container_api_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_api_metadata_request.GetContainerAPIMetadataRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_images(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_container_images_result.GetContainerImagesResult":
        """<p>Returns the container images that are registered to your Amazon Lightsail container service.</p> <note> <p>If you created a deployment on your Lightsail container service that uses container images from a public registry like Docker Hub, those images are not returned as part of this action. Those images are not registered to your Lightsail container service.</p> </note>

        Args:
            service_name: <p>The name of the container service for which to return registered container images.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_images_request.GetContainerImagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_container_images_result.GetContainerImagesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_images

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_images.async_get_container_images(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_images_request.GetContainerImagesRequest = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_log(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        container_name: "capo_lightsail.types.string.string",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        start_time: Optional["capo_lightsail.types.iso_date.IsoDate"] = None,
        end_time: Optional["capo_lightsail.types.iso_date.IsoDate"] = None,
        filter_pattern: Optional["capo_lightsail.types.string.string"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_container_log_result.GetContainerLogResult":
        """<p>Returns the log events of a container of your Amazon Lightsail container service.</p> <p>If your container service has more than one node (i.e., a scale greater than 1), then the log events that are returned for the specified container are merged from all nodes on your container service.</p> <note> <p>Container logs are retained for a certain amount of time. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/lightsail.html">Amazon Lightsail endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p> </note>

        Args:
            service_name: <p>The name of the container service for which to get a container log.</p>
            container_name: <p>The name of the container that is either running or previously ran on the container service for which to return a log.</p>
            start_time: <p>The start of the time interval for which to get log data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>
            end_time: <p>The end of the time interval for which to get log data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>
            filter_pattern: <p>The pattern to use to filter the returned log events to a specific term.</p> <p>The following are a few examples of filter patterns that you can specify:</p> <ul> <li> <p>To return all log events, specify a filter pattern of <code>""</code>.</p> </li> <li> <p>To exclude log events that contain the <code>ERROR</code> term, and return all other log events, specify a filter pattern of <code>"-ERROR"</code>.</p> </li> <li> <p>To return log events that contain the <code>ERROR</code> term, specify a filter pattern of <code>"ERROR"</code>.</p> </li> <li> <p>To return log events that contain both the <code>ERROR</code> and <code>Exception</code> terms, specify a filter pattern of <code>"ERROR Exception"</code>.</p> </li> <li> <p>To return log events that contain the <code>ERROR</code> <i>or</i> the <code>Exception</code> term, specify a filter pattern of <code>"?ERROR ?Exception"</code>.</p> </li> </ul>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetContainerLog</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_log_request.GetContainerLogRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_container_log_result.GetContainerLogResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_log

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_log.async_get_container_log(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_log_request.GetContainerLogRequest = {
            "service_name": service_name,
            "container_name": container_name,
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if filter_pattern is not None:
            input_["filter_pattern"] = filter_pattern
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_service_deployments(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_container_service_deployments_result.GetContainerServiceDeploymentsResult":
        """<p>Returns the deployments for your Amazon Lightsail container service</p> <p>A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.</p> <p>The deployments are ordered by version in ascending order. The newest version is listed at the top of the response.</p> <note> <p>A set number of deployments are kept before the oldest one is replaced with the newest one. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/lightsail.html">Amazon Lightsail endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p> </note>

        Args:
            service_name: <p>The name of the container service for which to return deployments.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_service_deployments_request.GetContainerServiceDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_container_service_deployments_result.GetContainerServiceDeploymentsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_service_deployments

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_service_deployments.async_get_container_service_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_service_deployments_request.GetContainerServiceDeploymentsRequest = {
            "service_name": service_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_service_metric_data(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        metric_name: "capo_lightsail.types.container_service_metric_name.ContainerServiceMetricName",
        start_time: "capo_lightsail.types.iso_date.IsoDate",
        end_time: "capo_lightsail.types.iso_date.IsoDate",
        period: "capo_lightsail.types.metric_period.MetricPeriod",
        statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult":
        """<p>Returns the data points of a specific metric of your Amazon Lightsail container service.</p> <p>Metrics report the utilization of your resources. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.</p>

        Args:
            service_name: <p>The name of the container service for which to get metric data.</p>
            metric_name: <p>The metric for which you want to return information.</p> <p>Valid container service metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.</p> <ul> <li> <p> <code>CPUUtilization</code> - The average percentage of compute units that are currently in use across all nodes of the container service. This metric identifies the processing power required to run containers on each node of the container service.</p> <p>Statistics: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p>Unit: The published unit is <code>Percent</code>.</p> </li> <li> <p> <code>MemoryUtilization</code> - The average percentage of available memory that is currently in use across all nodes of the container service. This metric identifies the memory required to run containers on each node of the container service.</p> <p>Statistics: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p>Unit: The published unit is <code>Percent</code>.</p> </li> </ul>
            start_time: <p>The start time of the time period.</p>
            end_time: <p>The end time of the time period.</p>
            period: <p>The granularity, in seconds, of the returned data points.</p> <p>All container service metric data is available in 5-minute (300 seconds) granularity.</p>
            statistics: <p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of <code>Sum</code> / <code>SampleCount</code> during the specified period. By comparing this statistic with the <code>Minimum</code> and <code>Maximum</code> values, you can determine the full scope of a metric and how close the average use is to the <code>Minimum</code> and <code>Maximum</code> values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_service_metric_data_request.GetContainerServiceMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_container_service_metric_data_result.GetContainerServiceMetricDataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_service_metric_data

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_service_metric_data.async_get_container_service_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_service_metric_data_request.GetContainerServiceMetricDataRequest = {
            "service_name": service_name,
            "metric_name": metric_name,
            "start_time": start_time,
            "end_time": end_time,
            "period": period,
            "statistics": statistics,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_service_powers(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.get_container_service_powers_result.GetContainerServicePowersResult":
        """<p>Returns the list of powers that can be specified for your Amazon Lightsail container services.</p> <p>The power specifies the amount of memory, the number of vCPUs, and the base price of the container service.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_service_powers_request.GetContainerServicePowersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_container_service_powers_result.GetContainerServicePowersResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_service_powers

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_service_powers.async_get_container_service_powers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_service_powers_request.GetContainerServicePowersRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_container_services(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        service_name: Optional[
            "capo_lightsail.types.container_service_name.ContainerServiceName"
        ] = None,
    ) -> "capo_lightsail.types.container_services_list_result.ContainerServicesListResult":
        """<p>Returns information about one or more of your Amazon Lightsail container services.</p>

        Args:
            service_name: <p>The name of the container service for which to return information.</p> <p>When omitted, the response includes all of your container services in the Amazon Web Services Region where the request is made.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_container_services_request.GetContainerServicesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.container_services_list_result.ContainerServicesListResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_container_services

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_container_services.async_get_container_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_container_services_request.GetContainerServicesRequest = {}
        if service_name is not None:
            input_["service_name"] = service_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cost_estimate(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        start_time: "capo_lightsail.types.iso_date.IsoDate",
        end_time: "capo_lightsail.types.iso_date.IsoDate",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_cost_estimate_result.GetCostEstimateResult":
        """<p>Retrieves information about the cost estimate for a specified resource. A cost estimate will not generate for a resource that has been deleted.</p>

        Args:
            resource_name: <p>The resource name.</p>
            start_time: <p>The cost estimate start time.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you want to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>
            end_time: <p>The cost estimate end time.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you want to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_cost_estimate_request.GetCostEstimateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_cost_estimate_result.GetCostEstimateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_cost_estimate

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_cost_estimate.async_get_cost_estimate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_cost_estimate_request.GetCostEstimateRequest = {
            "resource_name": resource_name,
            "start_time": start_time,
            "end_time": end_time,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_disk(
        self,
        disk_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_disk_result.GetDiskResult":
        """<p>Returns information about a specific block storage disk.</p>

        Args:
            disk_name: <p>The name of the disk (<code>my-disk</code>).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_disk_request.GetDiskRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_disk_result.GetDiskResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_disk

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_disk.async_get_disk(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_disk_request.GetDiskRequest = {
            "disk_name": disk_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_disks(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_disks_result.GetDisksResult":
        """<p>Returns information about all block storage disks in your AWS account and region.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetDisks</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_disks_request.GetDisksRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_disks_result.GetDisksResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_disks

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_disks.async_get_disks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_disks_request.GetDisksRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_disk_snapshot(
        self,
        disk_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_disk_snapshot_result.GetDiskSnapshotResult":
        """<p>Returns information about a specific block storage disk snapshot.</p>

        Args:
            disk_snapshot_name: <p>The name of the disk snapshot (<code>my-disk-snapshot</code>).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_disk_snapshot_request.GetDiskSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_disk_snapshot_result.GetDiskSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_disk_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_disk_snapshot.async_get_disk_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_disk_snapshot_request.GetDiskSnapshotRequest = {
            "disk_snapshot_name": disk_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_disk_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_disk_snapshots_result.GetDiskSnapshotsResult":
        """<p>Returns information about all block storage disk snapshots in your AWS account and region.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetDiskSnapshots</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_disk_snapshots_request.GetDiskSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_disk_snapshots_result.GetDiskSnapshotsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_disk_snapshots

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_disk_snapshots.async_get_disk_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_disk_snapshots_request.GetDiskSnapshotsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_distribution_bundles(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.get_distribution_bundles_result.GetDistributionBundlesResult":
        """<p>Returns the bundles that can be applied to your Amazon Lightsail content delivery network (CDN) distributions.</p> <p>A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_distribution_bundles_request.GetDistributionBundlesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_distribution_bundles_result.GetDistributionBundlesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_distribution_bundles

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_distribution_bundles.async_get_distribution_bundles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_distribution_bundles_request.GetDistributionBundlesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_distribution_latest_cache_reset(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        distribution_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_lightsail.types.get_distribution_latest_cache_reset_result.GetDistributionLatestCacheResetResult":
        """<p>Returns the timestamp and status of the last cache reset of a specific Amazon Lightsail content delivery network (CDN) distribution.</p>

        Args:
            distribution_name: <p>The name of the distribution for which to return the timestamp of the last cache reset.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p> <p>When omitted, the response includes the latest cache reset timestamp of all your distributions.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_distribution_latest_cache_reset_request.GetDistributionLatestCacheResetRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_distribution_latest_cache_reset_result.GetDistributionLatestCacheResetResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_distribution_latest_cache_reset

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_distribution_latest_cache_reset.async_get_distribution_latest_cache_reset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_distribution_latest_cache_reset_request.GetDistributionLatestCacheResetRequest = {}
        if distribution_name is not None:
            input_["distribution_name"] = distribution_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_distribution_metric_data(
        self,
        distribution_name: "capo_lightsail.types.resource_name.ResourceName",
        metric_name: "capo_lightsail.types.distribution_metric_name.DistributionMetricName",
        start_time: "capo_lightsail.types.timestamp.timestamp",
        end_time: "capo_lightsail.types.timestamp.timestamp",
        period: "capo_lightsail.types.metric_period.MetricPeriod",
        unit: "capo_lightsail.types.metric_unit.MetricUnit",
        statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_distribution_metric_data_result.GetDistributionMetricDataResult":
        """<p>Returns the data points of a specific metric for an Amazon Lightsail content delivery network (CDN) distribution.</p> <p>Metrics report the utilization of your resources, and the error counts generated by them. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.</p>

        Args:
            distribution_name: <p>The name of the distribution for which to get metric data.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>
            metric_name: <p>The metric for which you want to return information.</p> <p>Valid distribution metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value.</p> <ul> <li> <p> <b> <code>Requests</code> </b> - The total number of viewer requests received by your Lightsail distribution, for all HTTP methods, and for both HTTP and HTTPS requests.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>None</code>.</p> </li> <li> <p> <b> <code>BytesDownloaded</code> </b> - The number of bytes downloaded by viewers for GET, HEAD, and OPTIONS requests.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>None</code>.</p> </li> <li> <p> <b> <code>BytesUploaded </code> </b> - The number of bytes uploaded to your origin by your Lightsail distribution, using POST and PUT requests.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>None</code>.</p> </li> <li> <p> <b> <code>TotalErrorRate</code> </b> - The percentage of all viewer requests for which the response's HTTP status code was 4xx or 5xx.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>4xxErrorRate</code> </b> - The percentage of all viewer requests for which the response's HTTP status cod was 4xx. In these cases, the client or client viewer may have made an error. For example, a status code of 404 (Not Found) means that the client requested an object that could not be found.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>5xxErrorRate</code> </b> - The percentage of all viewer requests for which the response's HTTP status code was 5xx. In these cases, the origin server did not satisfy the requests. For example, a status code of 503 (Service Unavailable) means that the origin server is currently unavailable.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> </ul>
            start_time: <p>The start of the time interval for which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, specify <code>1538424000</code> as the start time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>
            end_time: <p>The end of the time interval for which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 9 PM UTC, specify <code>1538427600</code> as the end time.</p> </li> </ul> <p>You can convert a human-friendly time to Unix time format using a converter like <a href="https://www.epochconverter.com/">Epoch converter</a>.</p>
            period: <p>The granularity, in seconds, for the metric data points that will be returned.</p>
            unit: <p>The unit for the metric data request.</p> <p>Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>
            statistics: <p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_distribution_metric_data_request.GetDistributionMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_distribution_metric_data_result.GetDistributionMetricDataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_distribution_metric_data

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_distribution_metric_data.async_get_distribution_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_distribution_metric_data_request.GetDistributionMetricDataRequest = {
            "distribution_name": distribution_name,
            "metric_name": metric_name,
            "start_time": start_time,
            "end_time": end_time,
            "period": period,
            "unit": unit,
            "statistics": statistics,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_distributions(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        distribution_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_distributions_result.GetDistributionsResult":
        """<p>Returns information about one or more of your Amazon Lightsail content delivery network (CDN) distributions.</p>

        Args:
            distribution_name: <p>The name of the distribution for which to return information.</p> <p>When omitted, the response includes all of your distributions in the Amazon Web Services Region where the request is made.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetDistributions</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_distributions_request.GetDistributionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_distributions_result.GetDistributionsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_distributions

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_distributions.async_get_distributions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_distributions_request.GetDistributionsRequest = {}
        if distribution_name is not None:
            input_["distribution_name"] = distribution_name
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domain(
        self,
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_domain_result.GetDomainResult":
        """<p>Returns information about a specific domain recordset.</p>

        Args:
            domain_name: <p>The domain name for which your want to return information about.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_domain_request.GetDomainRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_domain_result.GetDomainResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_domain

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_domain_request.GetDomainRequest = {
            "domain_name": domain_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_domains(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_domains_result.GetDomainsResult":
        """<p>Returns a list of all domains in the user's account.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetDomains</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_domains_request.GetDomainsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_domains_result.GetDomainsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_domains

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_domains.async_get_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_domains_request.GetDomainsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_export_snapshot_records(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_export_snapshot_records_result.GetExportSnapshotRecordsResult":
        """<p>Returns all export snapshot records created as a result of the <code>export snapshot</code> operation.</p> <p>An export snapshot record can be used to create a new Amazon EC2 instance and its related resources with the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateCloudFormationStack.html">CreateCloudFormationStack</a> action.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetExportSnapshotRecords</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_export_snapshot_records_request.GetExportSnapshotRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_export_snapshot_records_result.GetExportSnapshotRecordsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_export_snapshot_records

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_export_snapshot_records.async_get_export_snapshot_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_export_snapshot_records_request.GetExportSnapshotRecordsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_instance_result.GetInstanceResult":
        """<p>Returns information about a specific Amazon Lightsail instance, which is a virtual private server.</p>

        Args:
            instance_name: <p>The name of the instance.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_request.GetInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_result.GetInstanceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance.async_get_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_request.GetInstanceRequest = {
            "instance_name": instance_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_access_details(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        protocol: Optional[
            "capo_lightsail.types.instance_access_protocol.InstanceAccessProtocol"
        ] = None,
    ) -> "capo_lightsail.types.get_instance_access_details_result.GetInstanceAccessDetailsResult":
        """<p>Returns temporary SSH keys you can use to connect to a specific virtual private server, or <i>instance</i>.</p> <p>The <code>get instance access details</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>instance name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_name: <p>The name of the instance to access.</p>
            protocol: <p>The protocol to use to connect to your instance. Defaults to <code>ssh</code>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_access_details_request.GetInstanceAccessDetailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_access_details_result.GetInstanceAccessDetailsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance_access_details

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance_access_details.async_get_instance_access_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_access_details_request.GetInstanceAccessDetailsRequest = {
            "instance_name": instance_name
        }
        if protocol is not None:
            input_["protocol"] = protocol

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_metric_data(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        metric_name: "capo_lightsail.types.instance_metric_name.InstanceMetricName",
        period: "capo_lightsail.types.metric_period.MetricPeriod",
        start_time: "capo_lightsail.types.timestamp.timestamp",
        end_time: "capo_lightsail.types.timestamp.timestamp",
        unit: "capo_lightsail.types.metric_unit.MetricUnit",
        statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_instance_metric_data_result.GetInstanceMetricDataResult":
        """<p>Returns the data points for the specified Amazon Lightsail instance metric, given an instance name.</p> <p>Metrics report the utilization of your resources, and the error counts generated by them. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.</p>

        Args:
            instance_name: <p>The name of the instance for which you want to get metrics data.</p>
            metric_name: <p>The metric for which you want to return information.</p> <p>Valid instance metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value.</p> <ul> <li> <p> <b> <code>BurstCapacityPercentage</code> </b> - The percentage of CPU performance available for your instance to burst above its baseline. Your instance continuously accrues and consumes burst capacity. Burst capacity stops accruing when your instance's <code>BurstCapacityPercentage</code> reaches 100%. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-burst-capacity">Viewing instance burst capacity in Amazon Lightsail</a>.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>BurstCapacityTime</code> </b> - The available amount of time for your instance to burst at 100% CPU utilization. Your instance continuously accrues and consumes burst capacity. Burst capacity time stops accruing when your instance's <code>BurstCapacityPercentage</code> metric reaches 100%.</p> <p>Burst capacity time is consumed at the full rate only when your instance operates at 100% CPU utilization. For example, if your instance operates at 50% CPU utilization in the burstable zone for a 5-minute period, then it consumes CPU burst capacity minutes at a 50% rate in that period. Your instance consumed 2 minutes and 30 seconds of CPU burst capacity minutes in the 5-minute period. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-viewing-instance-burst-capacity">Viewing instance burst capacity in Amazon Lightsail</a>.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Seconds</code>.</p> </li> <li> <p> <b> <code>CPUUtilization</code> </b> - The percentage of allocated compute units that are currently in use on the instance. This metric identifies the processing power to run the applications on the instance. Tools in your operating system can show a lower percentage than Lightsail when the instance is not allocated a full processor core.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>NetworkIn</code> </b> - The number of bytes received on all network interfaces by the instance. This metric identifies the volume of incoming network traffic to the instance. The number reported is the number of bytes received during the period. Because this metric is reported in 5-minute intervals, divide the reported number by 300 to find Bytes/second.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>NetworkOut</code> </b> - The number of bytes sent out on all network interfaces by the instance. This metric identifies the volume of outgoing network traffic from the instance. The number reported is the number of bytes sent during the period. Because this metric is reported in 5-minute intervals, divide the reported number by 300 to find Bytes/second.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>StatusCheckFailed</code> </b> - Reports whether the instance passed or failed both the instance status check and the system status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>StatusCheckFailed_Instance</code> </b> - Reports whether the instance passed or failed the instance status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>StatusCheckFailed_System</code> </b> - Reports whether the instance passed or failed the system status check. This metric can be either 0 (passed) or 1 (failed). This metric data is available in 1-minute (60 seconds) granularity.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>MetadataNoToken</code> </b> - Reports the number of times that the instance metadata service was successfully accessed without a token. This metric determines if there are any processes accessing instance metadata by using Instance Metadata Service Version 1, which doesn't use a token. If all requests use token-backed sessions, such as Instance Metadata Service Version 2, then the value is 0.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> </ul>
            period: <p>The granularity, in seconds, of the returned data points.</p> <p>The <code>StatusCheckFailed</code>, <code>StatusCheckFailed_Instance</code>, and <code>StatusCheckFailed_System</code> instance metric data is available in 1-minute (60 seconds) granularity. All other instance metric data is available in 5-minute (300 seconds) granularity.</p>
            start_time: <p>The start time of the time period.</p>
            end_time: <p>The end time of the time period.</p>
            unit: <p>The unit for the metric data request. Valid units depend on the metric data being requested. For the valid units to specify with each available metric, see the <code>metricName</code> parameter.</p>
            statistics: <p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_metric_data_request.GetInstanceMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_metric_data_result.GetInstanceMetricDataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance_metric_data

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance_metric_data.async_get_instance_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_metric_data_request.GetInstanceMetricDataRequest = {
            "instance_name": instance_name,
            "metric_name": metric_name,
            "period": period,
            "start_time": start_time,
            "end_time": end_time,
            "unit": unit,
            "statistics": statistics,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_port_states(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_instance_port_states_result.GetInstancePortStatesResult":
        """<p>Returns the firewall port states for a specific Amazon Lightsail instance, the IP addresses allowed to connect to the instance through the ports, and the protocol.</p>

        Args:
            instance_name: <p>The name of the instance for which to return firewall port states.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_port_states_request.GetInstancePortStatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_port_states_result.GetInstancePortStatesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance_port_states

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance_port_states.async_get_instance_port_states(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_port_states_request.GetInstancePortStatesRequest = {
            "instance_name": instance_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instances(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_instances_result.GetInstancesResult":
        """<p>Returns information about all Amazon Lightsail virtual private servers, or <i>instances</i>.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetInstances</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instances_request.GetInstancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instances_result.GetInstancesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instances

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instances.async_get_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instances_request.GetInstancesRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_snapshot(
        self,
        instance_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_instance_snapshot_result.GetInstanceSnapshotResult":
        """<p>Returns information about a specific instance snapshot.</p>

        Args:
            instance_snapshot_name: <p>The name of the snapshot for which you are requesting information.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_snapshot_request.GetInstanceSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_snapshot_result.GetInstanceSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance_snapshot.async_get_instance_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_snapshot_request.GetInstanceSnapshotRequest = {
            "instance_snapshot_name": instance_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> (
        "capo_lightsail.types.get_instance_snapshots_result.GetInstanceSnapshotsResult"
    ):
        """<p>Returns all instance snapshots for the user's account.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetInstanceSnapshots</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_snapshots_request.GetInstanceSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_snapshots_result.GetInstanceSnapshotsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance_snapshots

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance_snapshots.async_get_instance_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_snapshots_request.GetInstanceSnapshotsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_instance_state(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_instance_state_result.GetInstanceStateResult":
        """<p>Returns the state of a specific instance. Works on one instance at a time.</p>

        Args:
            instance_name: <p>The name of the instance to get state information about.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_instance_state_request.GetInstanceStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_instance_state_result.GetInstanceStateResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_instance_state

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_instance_state.async_get_instance_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_instance_state_request.GetInstanceStateRequest = {
            "instance_name": instance_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_key_pair(
        self,
        key_pair_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_key_pair_result.GetKeyPairResult":
        """<p>Returns information about a specific key pair.</p>

        Args:
            key_pair_name: <p>The name of the key pair for which you are requesting information.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_key_pair_request.GetKeyPairRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_key_pair_result.GetKeyPairResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_key_pair

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_key_pair.async_get_key_pair(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_key_pair_request.GetKeyPairRequest = {
            "key_pair_name": key_pair_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_key_pairs(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
        include_default_key_pair: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
    ) -> "capo_lightsail.types.get_key_pairs_result.GetKeyPairsResult":
        """<p>Returns information about all key pairs in the user's account.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetKeyPairs</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>
            include_default_key_pair: <p>A Boolean value that indicates whether to include the default key pair in the response of your request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_key_pairs_request.GetKeyPairsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_key_pairs_result.GetKeyPairsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_key_pairs

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_key_pairs.async_get_key_pairs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_key_pairs_request.GetKeyPairsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token
        if include_default_key_pair is not None:
            input_["include_default_key_pair"] = include_default_key_pair

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_load_balancer(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_load_balancer_result.GetLoadBalancerResult":
        """<p>Returns information about the specified Lightsail load balancer.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_load_balancer_request.GetLoadBalancerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_load_balancer_result.GetLoadBalancerResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_load_balancer

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_load_balancer.async_get_load_balancer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_load_balancer_request.GetLoadBalancerRequest = {
            "load_balancer_name": load_balancer_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_load_balancer_metric_data(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        metric_name: "capo_lightsail.types.load_balancer_metric_name.LoadBalancerMetricName",
        period: "capo_lightsail.types.metric_period.MetricPeriod",
        start_time: "capo_lightsail.types.timestamp.timestamp",
        end_time: "capo_lightsail.types.timestamp.timestamp",
        unit: "capo_lightsail.types.metric_unit.MetricUnit",
        statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_load_balancer_metric_data_result.GetLoadBalancerMetricDataResult":
        """<p>Returns information about health metrics for your Lightsail load balancer.</p> <p>Metrics report the utilization of your resources, and the error counts generated by them. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer.</p>
            metric_name: <p>The metric for which you want to return information.</p> <p>Valid load balancer metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value.</p> <ul> <li> <p> <b> <code>ClientTLSNegotiationErrorCount</code> </b> - The number of TLS connections initiated by the client that did not establish a session with the load balancer due to a TLS error generated by the load balancer. Possible causes include a mismatch of ciphers or protocols.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HealthyHostCount</code> </b> - The number of target instances that are considered healthy.</p> <p> <code>Statistics</code>: The most useful statistic are <code>Average</code>, <code>Minimum</code>, and <code>Maximum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HTTPCode_Instance_2XX_Count</code> </b> - The number of HTTP 2XX response codes generated by the target instances. This does not include any response codes generated by the load balancer.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HTTPCode_Instance_3XX_Count</code> </b> - The number of HTTP 3XX response codes generated by the target instances. This does not include any response codes generated by the load balancer.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HTTPCode_Instance_4XX_Count</code> </b> - The number of HTTP 4XX response codes generated by the target instances. This does not include any response codes generated by the load balancer.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HTTPCode_Instance_5XX_Count</code> </b> - The number of HTTP 5XX response codes generated by the target instances. This does not include any response codes generated by the load balancer.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HTTPCode_LB_4XX_Count</code> </b> - The number of HTTP 4XX client error codes that originated from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests were not received by the target instance. This count does not include response codes generated by the target instances.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>HTTPCode_LB_5XX_Count</code> </b> - The number of HTTP 5XX server error codes that originated from the load balancer. This does not include any response codes generated by the target instance. This metric is reported if there are no healthy instances attached to the load balancer, or if the request rate exceeds the capacity of the instances (spillover) or the load balancer.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>InstanceResponseTime</code> </b> - The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Seconds</code>.</p> </li> <li> <p> <b> <code>RejectedConnectionCount</code> </b> - The number of connections that were rejected because the load balancer had reached its maximum number of connections.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>RequestCount</code> </b> - The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>. Note that <code>Minimum</code>, <code>Maximum</code>, and <code>Average</code> all return <code>1</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>UnhealthyHostCount</code> </b> - The number of target instances that are considered unhealthy.</p> <p> <code>Statistics</code>: The most useful statistic are <code>Average</code>, <code>Minimum</code>, and <code>Maximum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> </ul>
            period: <p>The granularity, in seconds, of the returned data points.</p>
            start_time: <p>The start time of the period.</p>
            end_time: <p>The end time of the period.</p>
            unit: <p>The unit for the metric data request. Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>
            statistics: <p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_load_balancer_metric_data_request.GetLoadBalancerMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_load_balancer_metric_data_result.GetLoadBalancerMetricDataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_load_balancer_metric_data

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_load_balancer_metric_data.async_get_load_balancer_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_load_balancer_metric_data_request.GetLoadBalancerMetricDataRequest = {
            "load_balancer_name": load_balancer_name,
            "metric_name": metric_name,
            "period": period,
            "start_time": start_time,
            "end_time": end_time,
            "unit": unit,
            "statistics": statistics,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_load_balancers(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_load_balancers_result.GetLoadBalancersResult":
        """<p>Returns information about all load balancers in an account.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetLoadBalancers</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_load_balancers_request.GetLoadBalancersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_load_balancers_result.GetLoadBalancersResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_load_balancers

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_load_balancers.async_get_load_balancers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_load_balancers_request.GetLoadBalancersRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_load_balancer_tls_certificates(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_load_balancer_tls_certificates_result.GetLoadBalancerTlsCertificatesResult":
        """<p>Returns information about the TLS certificates that are associated with the specified Lightsail load balancer.</p> <p>TLS is just an updated, more secure version of Secure Socket Layer (SSL).</p> <p>You can have a maximum of 2 certificates associated with a Lightsail load balancer. One is active and the other is inactive.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer you associated with your SSL/TLS certificate.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_load_balancer_tls_certificates_request.GetLoadBalancerTlsCertificatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_load_balancer_tls_certificates_result.GetLoadBalancerTlsCertificatesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_load_balancer_tls_certificates

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_load_balancer_tls_certificates.async_get_load_balancer_tls_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_load_balancer_tls_certificates_request.GetLoadBalancerTlsCertificatesRequest = {
            "load_balancer_name": load_balancer_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_load_balancer_tls_policies(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_load_balancer_tls_policies_result.GetLoadBalancerTlsPoliciesResult":
        """<p>Returns a list of TLS security policies that you can apply to Lightsail load balancers.</p> <p>For more information about load balancer TLS security policies, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-tls-security-policy">Configuring TLS security policies on your Amazon Lightsail load balancers</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetLoadBalancerTlsPolicies</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_load_balancer_tls_policies_request.GetLoadBalancerTlsPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_load_balancer_tls_policies_result.GetLoadBalancerTlsPoliciesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_load_balancer_tls_policies

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_load_balancer_tls_policies.async_get_load_balancer_tls_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_load_balancer_tls_policies_request.GetLoadBalancerTlsPoliciesRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operation(
        self,
        operation_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_operation_result.GetOperationResult":
        """<p>Returns information about a specific operation. Operations include events such as when you create an instance, allocate a static IP, attach a static IP, and so on.</p>

        Args:
            operation_id: <p>A GUID used to identify the operation.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_operation_request.GetOperationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_operation_result.GetOperationResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_operation

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_operation.async_get_operation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_operation_request.GetOperationRequest = {
            "operation_id": operation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operations(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_operations_result.GetOperationsResult":
        """<p>Returns information about all operations.</p> <p>Results are returned from oldest to newest, up to a maximum of 200. Results can be paged by making each subsequent call to <code>GetOperations</code> use the maximum (last) <code>statusChangedAt</code> value from the previous request.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetOperations</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_operations_request.GetOperationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_operations_result.GetOperationsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_operations

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_operations.async_get_operations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_operations_request.GetOperationsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operations_for_resource(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_operations_for_resource_result.GetOperationsForResourceResult":
        """<p>Gets operations for a specific resource (an instance or a static IP).</p>

        Args:
            resource_name: <p>The name of the resource for which you are requesting information.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetOperationsForResource</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_operations_for_resource_request.GetOperationsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_operations_for_resource_result.GetOperationsForResourceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_operations_for_resource

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_operations_for_resource.async_get_operations_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_operations_for_resource_request.GetOperationsForResourceRequest = {
            "resource_name": resource_name
        }
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.get_profile_result.GetProfileResult":
        """<p>Returns information about the profile of the Amazon Lightsail account that makes the request. The response includes the profile type and, for accounts enrolled in the Lightsail partner program, the partner membership details.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_profile_request.GetProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_profile_result.GetProfileResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_profile

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_profile_request.GetProfileRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_regions(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        include_availability_zones: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        include_relational_database_availability_zones: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
    ) -> "capo_lightsail.types.get_regions_result.GetRegionsResult":
        """<p>Returns a list of all valid regions for Amazon Lightsail. Use the <code>include availability zones</code> parameter to also return the Availability Zones in a region.</p>

        Args:
            include_availability_zones: <p>A Boolean value indicating whether to also include Availability Zones in your get regions request. Availability Zones are indicated with a letter: <code>us-east-2a</code>.</p>
            include_relational_database_availability_zones: <p>A Boolean value indicating whether to also include Availability Zones for databases in your get regions request. Availability Zones are indicated with a letter (<code>us-east-2a</code>).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_regions_request.GetRegionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_regions_result.GetRegionsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_regions

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_regions.async_get_regions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_regions_request.GetRegionsRequest = {}
        if include_availability_zones is not None:
            input_["include_availability_zones"] = include_availability_zones
        if include_relational_database_availability_zones is not None:
            input_["include_relational_database_availability_zones"] = (
                include_relational_database_availability_zones
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_relational_database_result.GetRelationalDatabaseResult":
        """<p>Returns information about a specific database in Amazon Lightsail.</p>

        Args:
            relational_database_name: <p>The name of the database that you are looking up.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_request.GetRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_result.GetRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database.async_get_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_request.GetRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_blueprints(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_relational_database_blueprints_result.GetRelationalDatabaseBlueprintsResult":
        """<p>Returns a list of available database blueprints in Amazon Lightsail. A blueprint describes the major engine version of a database.</p> <p>You can use a blueprint ID to create a new database that runs a specific database engine.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseBlueprints</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_blueprints_request.GetRelationalDatabaseBlueprintsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_blueprints_result.GetRelationalDatabaseBlueprintsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_blueprints

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_blueprints.async_get_relational_database_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_blueprints_request.GetRelationalDatabaseBlueprintsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_bundles(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
        include_inactive: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.get_relational_database_bundles_result.GetRelationalDatabaseBundlesResult":
        """<p>Returns the list of bundles that are available in Amazon Lightsail. A bundle describes the performance specifications for a database.</p> <p>You can use a bundle ID to create a new database with explicit performance specifications.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseBundles</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>
            include_inactive: <p>A Boolean value that indicates whether to include inactive (unavailable) bundles in the response of your request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_bundles_request.GetRelationalDatabaseBundlesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_bundles_result.GetRelationalDatabaseBundlesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_bundles

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_bundles.async_get_relational_database_bundles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_bundles_request.GetRelationalDatabaseBundlesRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token
        if include_inactive is not None:
            input_["include_inactive"] = include_inactive

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_events(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        duration_in_minutes: Optional["capo_lightsail.types.integer.integer"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_relational_database_events_result.GetRelationalDatabaseEventsResult":
        """<p>Returns a list of events for a specific database in Amazon Lightsail.</p>

        Args:
            relational_database_name: <p>The name of the database from which to get events.</p>
            duration_in_minutes: <p>The number of minutes in the past from which to retrieve events. For example, to get all events from the past 2 hours, enter 120.</p> <p>Default: <code>60</code> </p> <p>The minimum is 1 and the maximum is 14 days (20160 minutes).</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseEvents</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_events_request.GetRelationalDatabaseEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_events_result.GetRelationalDatabaseEventsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_events

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_events.async_get_relational_database_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_events_request.GetRelationalDatabaseEventsRequest = {
            "relational_database_name": relational_database_name
        }
        if duration_in_minutes is not None:
            input_["duration_in_minutes"] = duration_in_minutes
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_log_events(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        log_stream_name: "capo_lightsail.types.string.string",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        start_time: Optional["capo_lightsail.types.iso_date.IsoDate"] = None,
        end_time: Optional["capo_lightsail.types.iso_date.IsoDate"] = None,
        start_from_head: Optional["capo_lightsail.types.boolean.boolean"] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_relational_database_log_events_result.GetRelationalDatabaseLogEventsResult":
        """<p>Returns a list of log events for a database in Amazon Lightsail.</p>

        Args:
            relational_database_name: <p>The name of your database for which to get log events.</p>
            log_stream_name: <p>The name of the log stream.</p> <p>Use the <code>get relational database log streams</code> operation to get a list of available log streams.</p>
            start_time: <p>The start of the time interval from which to get log events.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the start time.</p> </li> </ul>
            end_time: <p>The end of the time interval from which to get log events.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the end time.</p> </li> </ul>
            start_from_head: <p>Parameter to specify if the log should start from head or tail. If <code>true</code> is specified, the log event starts from the head of the log. If <code>false</code> is specified, the log event starts from the tail of the log.</p> <note> <p>For PostgreSQL, the default value of <code>false</code> is the only option available.</p> </note>
            page_token: <p>The token to advance to the next or previous page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseLogEvents</code> request. If your results are paginated, the response will return a next forward token and/or next backward token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_log_events_request.GetRelationalDatabaseLogEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_log_events_result.GetRelationalDatabaseLogEventsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_log_events

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_log_events.async_get_relational_database_log_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_log_events_request.GetRelationalDatabaseLogEventsRequest = {
            "relational_database_name": relational_database_name,
            "log_stream_name": log_stream_name,
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if start_from_head is not None:
            input_["start_from_head"] = start_from_head
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_log_streams(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_relational_database_log_streams_result.GetRelationalDatabaseLogStreamsResult":
        """<p>Returns a list of available log streams for a specific database in Amazon Lightsail.</p>

        Args:
            relational_database_name: <p>The name of your database for which to get log streams.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_log_streams_request.GetRelationalDatabaseLogStreamsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_log_streams_result.GetRelationalDatabaseLogStreamsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_log_streams

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_log_streams.async_get_relational_database_log_streams(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_log_streams_request.GetRelationalDatabaseLogStreamsRequest = {
            "relational_database_name": relational_database_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_master_user_password(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        password_version: Optional[
            "capo_lightsail.types.relational_database_password_version.RelationalDatabasePasswordVersion"
        ] = None,
    ) -> "capo_lightsail.types.get_relational_database_master_user_password_result.GetRelationalDatabaseMasterUserPasswordResult":
        """<p>Returns the current, previous, or pending versions of the master user password for a Lightsail database.</p> <p>The <code>GetRelationalDatabaseMasterUserPassword</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName.</p>

        Args:
            relational_database_name: <p>The name of your database for which to get the master user password.</p>
            password_version: <p>The password version to return.</p> <p>Specifying <code>CURRENT</code> or <code>PREVIOUS</code> returns the current or previous passwords respectively. Specifying <code>PENDING</code> returns the newest version of the password that will rotate to <code>CURRENT</code>. After the <code>PENDING</code> password rotates to <code>CURRENT</code>, the <code>PENDING</code> password is no longer available.</p> <p>Default: <code>CURRENT</code> </p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_master_user_password_request.GetRelationalDatabaseMasterUserPasswordRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_master_user_password_result.GetRelationalDatabaseMasterUserPasswordResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_master_user_password

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_master_user_password.async_get_relational_database_master_user_password(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_master_user_password_request.GetRelationalDatabaseMasterUserPasswordRequest = {
            "relational_database_name": relational_database_name
        }
        if password_version is not None:
            input_["password_version"] = password_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_metric_data(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        metric_name: "capo_lightsail.types.relational_database_metric_name.RelationalDatabaseMetricName",
        period: "capo_lightsail.types.metric_period.MetricPeriod",
        start_time: "capo_lightsail.types.iso_date.IsoDate",
        end_time: "capo_lightsail.types.iso_date.IsoDate",
        unit: "capo_lightsail.types.metric_unit.MetricUnit",
        statistics: "capo_lightsail.types.metric_statistic_list.MetricStatisticList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_relational_database_metric_data_result.GetRelationalDatabaseMetricDataResult":
        """<p>Returns the data points of the specified metric for a database in Amazon Lightsail.</p> <p>Metrics report the utilization of your resources, and the error counts generated by them. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.</p>

        Args:
            relational_database_name: <p>The name of your database from which to get metric data.</p>
            metric_name: <p>The metric for which you want to return information.</p> <p>Valid relational database metric names are listed below, along with the most useful <code>statistics</code> to include in your request, and the published <code>unit</code> value. All relational database metric data is available in 1-minute (60 seconds) granularity.</p> <ul> <li> <p> <b> <code>CPUUtilization</code> </b> - The percentage of CPU utilization currently in use on the database.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Percent</code>.</p> </li> <li> <p> <b> <code>DatabaseConnections</code> </b> - The number of database connections in use.</p> <p> <code>Statistics</code>: The most useful statistics are <code>Maximum</code> and <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>DiskQueueDepth</code> </b> - The number of outstanding IOs (read/write requests) that are waiting to access the disk.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Count</code>.</p> </li> <li> <p> <b> <code>FreeStorageSpace</code> </b> - The amount of available storage space.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Sum</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes</code>.</p> </li> <li> <p> <b> <code>NetworkReceiveThroughput</code> </b> - The incoming (Receive) network traffic on the database, including both customer database traffic and AWS traffic used for monitoring and replication.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes/Second</code>.</p> </li> <li> <p> <b> <code>NetworkTransmitThroughput</code> </b> - The outgoing (Transmit) network traffic on the database, including both customer database traffic and AWS traffic used for monitoring and replication.</p> <p> <code>Statistics</code>: The most useful statistic is <code>Average</code>.</p> <p> <code>Unit</code>: The published unit is <code>Bytes/Second</code>.</p> </li> </ul>
            period: <p>The granularity, in seconds, of the returned data points.</p> <p>All relational database metric data is available in 1-minute (60 seconds) granularity.</p>
            start_time: <p>The start of the time interval from which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the start time.</p> </li> </ul>
            end_time: <p>The end of the time interval from which to get metric data.</p> <p>Constraints:</p> <ul> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Specified in the Unix time format.</p> <p>For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input <code>1538424000</code> as the end time.</p> </li> </ul>
            unit: <p>The unit for the metric data request. Valid units depend on the metric data being requested. For the valid units with each available metric, see the <code>metricName</code> parameter.</p>
            statistics: <p>The statistic for the metric.</p> <p>The following statistics are available:</p> <ul> <li> <p> <code>Minimum</code> - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.</p> </li> <li> <p> <code>Maximum</code> - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.</p> </li> <li> <p> <code>Sum</code> - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.</p> </li> <li> <p> <code>Average</code> - The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum values, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum values. This comparison helps you to know when to increase or decrease your resources.</p> </li> <li> <p> <code>SampleCount</code> - The count, or number, of data points used for the statistical calculation.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_metric_data_request.GetRelationalDatabaseMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_metric_data_result.GetRelationalDatabaseMetricDataResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_metric_data

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_metric_data.async_get_relational_database_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_metric_data_request.GetRelationalDatabaseMetricDataRequest = {
            "relational_database_name": relational_database_name,
            "metric_name": metric_name,
            "period": period,
            "start_time": start_time,
            "end_time": end_time,
            "unit": unit,
            "statistics": statistics,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_parameters(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_relational_database_parameters_result.GetRelationalDatabaseParametersResult":
        """<p>Returns all of the runtime parameters offered by the underlying database software, or engine, for a specific database in Amazon Lightsail.</p> <p>In addition to the parameter names and values, this operation returns other information about each parameter. This information includes whether changes require a reboot, whether the parameter is modifiable, the allowed values, and the data types.</p>

        Args:
            relational_database_name: <p>The name of your database for which to get parameters.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseParameters</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_parameters_request.GetRelationalDatabaseParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_parameters_result.GetRelationalDatabaseParametersResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_parameters

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_parameters.async_get_relational_database_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_parameters_request.GetRelationalDatabaseParametersRequest = {
            "relational_database_name": relational_database_name
        }
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_databases(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_relational_databases_result.GetRelationalDatabasesResult":
        """<p>Returns information about all of your databases in Amazon Lightsail.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabases</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_databases_request.GetRelationalDatabasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_databases_result.GetRelationalDatabasesResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_databases

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_databases.async_get_relational_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_databases_request.GetRelationalDatabasesRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_snapshot(
        self,
        relational_database_snapshot_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_relational_database_snapshot_result.GetRelationalDatabaseSnapshotResult":
        """<p>Returns information about a specific database snapshot in Amazon Lightsail.</p>

        Args:
            relational_database_snapshot_name: <p>The name of the database snapshot for which to get information.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_snapshot_request.GetRelationalDatabaseSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_snapshot_result.GetRelationalDatabaseSnapshotResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_snapshot

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_snapshot.async_get_relational_database_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_snapshot_request.GetRelationalDatabaseSnapshotRequest = {
            "relational_database_snapshot_name": relational_database_snapshot_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_relational_database_snapshots(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_relational_database_snapshots_result.GetRelationalDatabaseSnapshotsResult":
        """<p>Returns information about all of your database snapshots in Amazon Lightsail.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetRelationalDatabaseSnapshots</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_relational_database_snapshots_request.GetRelationalDatabaseSnapshotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_relational_database_snapshots_result.GetRelationalDatabaseSnapshotsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_relational_database_snapshots

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_relational_database_snapshots.async_get_relational_database_snapshots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_relational_database_snapshots_request.GetRelationalDatabaseSnapshotsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_setup_history(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional[
            "capo_lightsail.types.setup_history_page_token.SetupHistoryPageToken"
        ] = None,
    ) -> "capo_lightsail.types.get_setup_history_result.GetSetupHistoryResult":
        """<p>Returns detailed information for five of the most recent <code>SetupInstanceHttps</code> requests that were ran on the target instance.</p>

        Args:
            resource_name: <p>The name of the resource for which you are requesting information.</p>
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetSetupHistory</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_setup_history_request.GetSetupHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_setup_history_result.GetSetupHistoryResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_setup_history

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_setup_history.async_get_setup_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_setup_history_request.GetSetupHistoryRequest = {
            "resource_name": resource_name
        }
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_static_ip(
        self,
        static_ip_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.get_static_ip_result.GetStaticIpResult":
        """<p>Returns information about an Amazon Lightsail static IP.</p>

        Args:
            static_ip_name: <p>The name of the static IP in Lightsail.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_static_ip_request.GetStaticIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_static_ip_result.GetStaticIpResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_static_ip

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_static_ip.async_get_static_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_static_ip_request.GetStaticIpRequest = {
            "static_ip_name": static_ip_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_static_ips(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        page_token: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.get_static_ips_result.GetStaticIpsResult":
        """<p>Returns information about all static IPs in the user's account.</p>

        Args:
            page_token: <p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetStaticIps</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.get_static_ips_request.GetStaticIpsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.get_static_ips_result.GetStaticIpsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.get_static_ips

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.get_static_ips.async_get_static_ips(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.get_static_ips_request.GetStaticIpsRequest = {}
        if page_token is not None:
            input_["page_token"] = page_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_key_pair(
        self,
        key_pair_name: "capo_lightsail.types.resource_name.ResourceName",
        public_key_base64: "capo_lightsail.types.base64.Base64",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.import_key_pair_result.ImportKeyPairResult":
        """<p>Imports a public SSH key from a specific key pair.</p>

        Args:
            key_pair_name: <p>The name of the key pair for which you want to import the public key.</p>
            public_key_base64: <p>A base64-encoded public key of the <code>ssh-rsa</code> type.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.import_key_pair_request.ImportKeyPairRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.import_key_pair_result.ImportKeyPairResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.import_key_pair

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.import_key_pair.async_import_key_pair(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.import_key_pair_request.ImportKeyPairRequest = {
            "key_pair_name": key_pair_name,
            "public_key_base64": public_key_base64,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def is_vpc_peered(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.is_vpc_peered_result.IsVpcPeeredResult":
        """<p>Returns a Boolean value indicating whether your Lightsail VPC is peered.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.is_vpc_peered_request.IsVpcPeeredRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.is_vpc_peered_result.IsVpcPeeredResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.is_vpc_peered

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.is_vpc_peered.async_is_vpc_peered(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.is_vpc_peered_request.IsVpcPeeredRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def open_instance_public_ports(
        self,
        port_info: "capo_lightsail.types.port_info.PortInfo",
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.open_instance_public_ports_result.OpenInstancePublicPortsResult":
        """<p>Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol.</p> <p>The <code>OpenInstancePublicPorts</code> action supports tag-based access control via resource tags applied to the resource identified by <code>instanceName</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            port_info: <p>An object to describe the ports to open for the specified instance.</p>
            instance_name: <p>The name of the instance for which to open ports.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.open_instance_public_ports_request.OpenInstancePublicPortsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.open_instance_public_ports_result.OpenInstancePublicPortsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.open_instance_public_ports

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.open_instance_public_ports.async_open_instance_public_ports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.open_instance_public_ports_request.OpenInstancePublicPortsRequest = {
            "port_info": port_info,
            "instance_name": instance_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def peer_vpc(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.peer_vpc_result.PeerVpcResult":
        """<p>Peers the Lightsail VPC with the user's default VPC.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.peer_vpc_request.PeerVpcRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.peer_vpc_result.PeerVpcResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.peer_vpc

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.peer_vpc.async_peer_vpc(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.peer_vpc_request.PeerVpcRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_alarm(
        self,
        alarm_name: "capo_lightsail.types.resource_name.ResourceName",
        metric_name: "capo_lightsail.types.metric_name.MetricName",
        monitored_resource_name: "capo_lightsail.types.resource_name.ResourceName",
        comparison_operator: "capo_lightsail.types.comparison_operator.ComparisonOperator",
        threshold: "capo_lightsail.types.double.double",
        evaluation_periods: "capo_lightsail.types.integer.integer",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        datapoints_to_alarm: Optional["capo_lightsail.types.integer.integer"] = None,
        treat_missing_data: Optional[
            "capo_lightsail.types.treat_missing_data.TreatMissingData"
        ] = None,
        contact_protocols: Optional[
            "capo_lightsail.types.contact_protocols_list.ContactProtocolsList"
        ] = None,
        notification_triggers: Optional[
            "capo_lightsail.types.notification_trigger_list.NotificationTriggerList"
        ] = None,
        notification_enabled: Optional["capo_lightsail.types.boolean.boolean"] = None,
        tags: Optional["capo_lightsail.types.tag_list.TagList"] = None,
    ) -> "capo_lightsail.types.put_alarm_result.PutAlarmResult":
        """<p>Creates or updates an alarm, and associates it with the specified metric.</p> <p>An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms">Alarms in Amazon Lightsail</a>.</p> <p>When this action creates an alarm, the alarm state is immediately set to <code>INSUFFICIENT_DATA</code>. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.</p> <p>When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm. The alarm is then evaluated with the updated configuration.</p> <p>The <code>put alarm</code> operation supports tag-based access control via request tags. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Lightsail Developer Guide</a>.</p>

        Args:
            alarm_name: <p>The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.</p>
            metric_name: <p>The name of the metric to associate with the alarm.</p> <p>You can configure up to two alarms per metric.</p> <p>The following metrics are available for each resource type:</p> <ul> <li> <p> <b>Instances</b>: <code>BurstCapacityPercentage</code>, <code>BurstCapacityTime</code>, <code>CPUUtilization</code>, <code>NetworkIn</code>, <code>NetworkOut</code>, <code>StatusCheckFailed</code>, <code>StatusCheckFailed_Instance</code>, and <code>StatusCheckFailed_System</code>.</p> </li> <li> <p> <b>Load balancers</b>: <code>ClientTLSNegotiationErrorCount</code>, <code>HealthyHostCount</code>, <code>UnhealthyHostCount</code>, <code>HTTPCode_LB_4XX_Count</code>, <code>HTTPCode_LB_5XX_Count</code>, <code>HTTPCode_Instance_2XX_Count</code>, <code>HTTPCode_Instance_3XX_Count</code>, <code>HTTPCode_Instance_4XX_Count</code>, <code>HTTPCode_Instance_5XX_Count</code>, <code>InstanceResponseTime</code>, <code>RejectedConnectionCount</code>, and <code>RequestCount</code>.</p> </li> <li> <p> <b>Relational databases</b>: <code>CPUUtilization</code>, <code>DatabaseConnections</code>, <code>DiskQueueDepth</code>, <code>FreeStorageSpace</code>, <code>NetworkReceiveThroughput</code>, and <code>NetworkTransmitThroughput</code>.</p> </li> </ul> <p>For more information about these metrics, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-resource-health-metrics#available-metrics">Metrics available in Lightsail</a>.</p>
            monitored_resource_name: <p>The name of the Lightsail resource that will be monitored.</p> <p>Instances, load balancers, and relational databases are the only Lightsail resources that can currently be monitored by alarms.</p>
            comparison_operator: <p>The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.</p>
            threshold: <p>The value against which the specified statistic is compared.</p>
            evaluation_periods: <p>The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out of N" alarm, this value (<code>evaluationPeriods</code>) is the N.</p> <p>If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies the rolling period of time in which data points are evaluated.</p> <p>Each evaluation period is five minutes long. For example, specify an evaluation period of 24 to evaluate a metric over a rolling period of two hours.</p> <p>You can specify a minimum valuation period of 1 (5 minutes), and a maximum evaluation period of 288 (24 hours).</p>
            datapoints_to_alarm: <p>The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M out of N" alarm, this value (<code>datapointsToAlarm</code>) is the M.</p>
            treat_missing_data: <p>Sets how this alarm will handle missing data points.</p> <p>An alarm can treat missing data in the following ways:</p> <ul> <li> <p> <code>breaching</code> - Assume the missing data is not within the threshold. Missing data counts towards the number of times the metric is not within the threshold.</p> </li> <li> <p> <code>notBreaching</code> - Assume the missing data is within the threshold. Missing data does not count towards the number of times the metric is not within the threshold.</p> </li> <li> <p> <code>ignore</code> - Ignore the missing data. Maintains the current alarm state.</p> </li> <li> <p> <code>missing</code> - Missing data is treated as missing.</p> </li> </ul> <p>If <code>treatMissingData</code> is not specified, the default behavior of <code>missing</code> is used.</p>
            contact_protocols: <p>The contact protocols to use for the alarm, such as <code>Email</code>, <code>SMS</code> (text messaging), or both.</p> <p>A notification is sent via the specified contact protocol if notifications are enabled for the alarm, and when the alarm is triggered.</p> <p>A notification is not sent if a contact protocol is not specified, if the specified contact protocol is not configured in the Amazon Web Services Region, or if notifications are not enabled for the alarm using the <code>notificationEnabled</code> paramater.</p> <p>Use the <code>CreateContactMethod</code> action to configure a contact protocol in an Amazon Web Services Region.</p>
            notification_triggers: <p>The alarm states that trigger a notification.</p> <p>An alarm has the following possible states:</p> <ul> <li> <p> <code>ALARM</code> - The metric is outside of the defined threshold.</p> </li> <li> <p> <code>INSUFFICIENT_DATA</code> - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.</p> </li> <li> <p> <code>OK</code> - The metric is within the defined threshold.</p> </li> </ul> <p>When you specify a notification trigger, the <code>ALARM</code> state must be specified. The <code>INSUFFICIENT_DATA</code> and <code>OK</code> states can be specified in addition to the <code>ALARM</code> state.</p> <ul> <li> <p>If you specify <code>OK</code> as an alarm trigger, a notification is sent when the alarm switches from an <code>ALARM</code> or <code>INSUFFICIENT_DATA</code> alarm state to an <code>OK</code> state. This can be thought of as an <i>all clear</i> alarm notification.</p> </li> <li> <p>If you specify <code>INSUFFICIENT_DATA</code> as the alarm trigger, a notification is sent when the alarm switches from an <code>OK</code> or <code>ALARM</code> alarm state to an <code>INSUFFICIENT_DATA</code> state.</p> </li> </ul> <p>The notification trigger defaults to <code>ALARM</code> if you don't specify this parameter.</p>
            notification_enabled: <p>Indicates whether the alarm is enabled.</p> <p>Notifications are enabled by default if you don't specify this parameter.</p>
            tags: <p>The tag keys and optional values to add to the alarm during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.put_alarm_request.PutAlarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.put_alarm_result.PutAlarmResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.put_alarm

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.put_alarm.async_put_alarm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.put_alarm_request.PutAlarmRequest = {
            "alarm_name": alarm_name,
            "metric_name": metric_name,
            "monitored_resource_name": monitored_resource_name,
            "comparison_operator": comparison_operator,
            "threshold": threshold,
            "evaluation_periods": evaluation_periods,
        }
        if datapoints_to_alarm is not None:
            input_["datapoints_to_alarm"] = datapoints_to_alarm
        if treat_missing_data is not None:
            input_["treat_missing_data"] = treat_missing_data
        if contact_protocols is not None:
            input_["contact_protocols"] = contact_protocols
        if notification_triggers is not None:
            input_["notification_triggers"] = notification_triggers
        if notification_enabled is not None:
            input_["notification_enabled"] = notification_enabled
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_instance_public_ports(
        self,
        port_infos: "capo_lightsail.types.port_info_list.PortInfoList",
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.put_instance_public_ports_result.PutInstancePublicPortsResult":
        """<p>Opens ports for a specific Amazon Lightsail instance, and specifies the IP addresses allowed to connect to the instance through the ports, and the protocol. This action also closes all currently open ports that are not included in the request. Include all of the ports and the protocols you want to open in your <code>PutInstancePublicPorts</code>request. Or use the <code>OpenInstancePublicPorts</code> action to open ports without closing currently open ports.</p> <p>The <code>PutInstancePublicPorts</code> action supports tag-based access control via resource tags applied to the resource identified by <code>instanceName</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            port_infos: <p>An array of objects to describe the ports to open for the specified instance.</p>
            instance_name: <p>The name of the instance for which to open ports.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.put_instance_public_ports_request.PutInstancePublicPortsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.put_instance_public_ports_result.PutInstancePublicPortsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.put_instance_public_ports

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.put_instance_public_ports.async_put_instance_public_ports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.put_instance_public_ports_request.PutInstancePublicPortsRequest = {
            "port_infos": port_infos,
            "instance_name": instance_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_instance(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.reboot_instance_result.RebootInstanceResult":
        """<p>Restarts a specific instance.</p> <p>The <code>reboot instance</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>instance name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_name: <p>The name of the instance to reboot.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.reboot_instance_request.RebootInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.reboot_instance_result.RebootInstanceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.reboot_instance

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.reboot_instance.async_reboot_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.reboot_instance_request.RebootInstanceRequest = {
            "instance_name": instance_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.reboot_relational_database_result.RebootRelationalDatabaseResult":
        """<p>Restarts a specific database in Amazon Lightsail.</p> <p>The <code>reboot relational database</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of your database to reboot.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.reboot_relational_database_request.RebootRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.reboot_relational_database_result.RebootRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.reboot_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.reboot_relational_database.async_reboot_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.reboot_relational_database_request.RebootRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_container_image(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        label: "capo_lightsail.types.container_label.ContainerLabel",
        digest: "capo_lightsail.types.string.string",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.register_container_image_result.RegisterContainerImageResult":
        """<p>Registers a container image to your Amazon Lightsail container service.</p> <note> <p>This action is not required if you install and use the Lightsail Control (lightsailctl) plugin to push container images to your Lightsail container service. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-pushing-container-images">Pushing and managing container images on your Amazon Lightsail container services</a> in the <i>Amazon Lightsail Developer Guide</i>.</p> </note>

        Args:
            service_name: <p>The name of the container service for which to register a container image.</p>
            label: <p>The label for the container image when it's registered to the container service.</p> <p>Use a descriptive label that you can use to track the different versions of your registered container images.</p> <p>Use the <code>GetContainerImages</code> action to return the container images registered to a Lightsail container service. The label is the <code><imagelabel></code> portion of the following image name example:</p> <ul> <li> <p> <code>:container-service-1.<imagelabel>.1</code> </p> </li> </ul> <p>If the name of your container service is <code>mycontainerservice</code>, and the label that you specify is <code>mystaticwebsite</code>, then the name of the registered container image will be <code>:mycontainerservice.mystaticwebsite.1</code>.</p> <p>The number at the end of these image name examples represents the version of the registered container image. If you push and register another container image to the same Lightsail container service, with the same label, then the version number for the new registered container image will be <code>2</code>. If you push and register another container image, the version number will be <code>3</code>, and so on.</p>
            digest: <p>The digest of the container image to be registered.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.register_container_image_request.RegisterContainerImageRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.register_container_image_result.RegisterContainerImageResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.register_container_image

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.register_container_image.async_register_container_image(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.register_container_image_request.RegisterContainerImageRequest = {
            "service_name": service_name,
            "label": label,
            "digest": digest,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def release_static_ip(
        self,
        static_ip_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.release_static_ip_result.ReleaseStaticIpResult":
        """<p>Deletes a specific static IP from your account.</p>

        Args:
            static_ip_name: <p>The name of the static IP to delete.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.release_static_ip_request.ReleaseStaticIpRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.release_static_ip_result.ReleaseStaticIpResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.release_static_ip

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.release_static_ip.async_release_static_ip(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.release_static_ip_request.ReleaseStaticIpRequest = {
            "static_ip_name": static_ip_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_distribution_cache(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        distribution_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_lightsail.types.reset_distribution_cache_result.ResetDistributionCacheResult":
        """<p>Deletes currently cached content from your Amazon Lightsail content delivery network (CDN) distribution.</p> <p>After resetting the cache, the next time a content request is made, your distribution pulls, serves, and caches it from the origin.</p>

        Args:
            distribution_name: <p>The name of the distribution for which to reset cache.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.reset_distribution_cache_request.ResetDistributionCacheRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.reset_distribution_cache_result.ResetDistributionCacheResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.reset_distribution_cache

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.reset_distribution_cache.async_reset_distribution_cache(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.reset_distribution_cache_request.ResetDistributionCacheRequest = {}
        if distribution_name is not None:
            input_["distribution_name"] = distribution_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_contact_method_verification(
        self,
        protocol: "capo_lightsail.types.contact_method_verification_protocol.ContactMethodVerificationProtocol",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.send_contact_method_verification_result.SendContactMethodVerificationResult":
        """<p>Sends a verification request to an email contact method to ensure it's owned by the requester. SMS contact methods don't need to be verified.</p> <p>A contact method is used to send you notifications about your Amazon Lightsail resources. You can add one email address and one mobile phone number contact method in each Amazon Web Services Region. However, SMS text messaging is not supported in some Amazon Web Services Regions, and SMS text messages cannot be sent to some countries/regions. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-notifications">Notifications in Amazon Lightsail</a>.</p> <p>A verification request is sent to the contact method when you initially create it. Use this action to send another verification request if a previous verification request was deleted, or has expired.</p> <important> <p>Notifications are not sent to an email contact method until after it is verified, and confirmed as valid.</p> </important>

        Args:
            protocol: <p>The protocol to verify, such as <code>Email</code> or <code>SMS</code> (text messaging).</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.send_contact_method_verification_request.SendContactMethodVerificationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.send_contact_method_verification_result.SendContactMethodVerificationResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.send_contact_method_verification

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.send_contact_method_verification.async_send_contact_method_verification(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.send_contact_method_verification_request.SendContactMethodVerificationRequest = {
            "protocol": protocol
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_ip_address_type(
        self,
        resource_type: "capo_lightsail.types.resource_type.ResourceType",
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        ip_address_type: "capo_lightsail.types.ip_address_type.IpAddressType",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        accept_bundle_update: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.set_ip_address_type_result.SetIpAddressTypeResult":
        """<p>Sets the IP address type for an Amazon Lightsail resource.</p> <p>Use this action to enable dual-stack for a resource, which enables IPv4 and IPv6 for the specified resource. Alternately, you can use this action to disable dual-stack, and enable IPv4 only.</p>

        Args:
            resource_type: <p>The resource type.</p> <p>The resource values are <code>Distribution</code>, <code>Instance</code>, and <code>LoadBalancer</code>.</p> <note> <p>Distribution-related APIs are available only in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit distributions.</p> </note>
            resource_name: <p>The name of the resource for which to set the IP address type.</p>
            ip_address_type: <p>The IP address type to set for the specified resource.</p> <p>The possible values are <code>ipv4</code> for IPv4 only, <code>ipv6</code> for IPv6 only, and <code>dualstack</code> for IPv4 and IPv6.</p>
            accept_bundle_update: <p>Required parameter to accept the instance bundle update when changing to, and from, IPv6-only.</p> <note> <p>An instance bundle will change when switching from <code>dual-stack</code> or <code>ipv4</code>, to <code>ipv6</code>. It also changes when switching from <code>ipv6</code>, to <code>dual-stack</code> or <code>ipv4</code>.</p> <p>You must include this parameter in the command to update the bundle. For example, if you switch from <code>dual-stack</code> to <code>ipv6</code>, the bundle will be updated, and billing for the IPv6-only instance bundle begins immediately.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.set_ip_address_type_request.SetIpAddressTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.set_ip_address_type_result.SetIpAddressTypeResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.set_ip_address_type

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.set_ip_address_type.async_set_ip_address_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.set_ip_address_type_request.SetIpAddressTypeRequest = {
            "resource_type": resource_type,
            "resource_name": resource_name,
            "ip_address_type": ip_address_type,
        }
        if accept_bundle_update is not None:
            input_["accept_bundle_update"] = accept_bundle_update

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def set_resource_access_for_bucket(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        access: "capo_lightsail.types.resource_bucket_access.ResourceBucketAccess",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.set_resource_access_for_bucket_result.SetResourceAccessForBucketResult":
        """<p>Sets the Amazon Lightsail resources that can access the specified Lightsail bucket.</p> <p>Lightsail buckets currently support setting access for Lightsail instances in the same Amazon Web Services Region.</p>

        Args:
            resource_name: <p>The name of the Lightsail instance for which to set bucket access. The instance must be in a running or stopped state.</p>
            bucket_name: <p>The name of the bucket for which to set access to another Lightsail resource.</p>
            access: <p>The access setting.</p> <p>The following access settings are available:</p> <ul> <li> <p> <code>allow</code> - Allows access to the bucket and its objects.</p> </li> <li> <p> <code>deny</code> - Denies access to the bucket and its objects. Use this setting to remove access for a resource previously set to <code>allow</code>.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.set_resource_access_for_bucket_request.SetResourceAccessForBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.set_resource_access_for_bucket_result.SetResourceAccessForBucketResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.set_resource_access_for_bucket

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.set_resource_access_for_bucket.async_set_resource_access_for_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.set_resource_access_for_bucket_request.SetResourceAccessForBucketRequest = {
            "resource_name": resource_name,
            "bucket_name": bucket_name,
            "access": access,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def setup_instance_https(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        email_address: "capo_lightsail.types.email_address.EmailAddress",
        domain_names: "capo_lightsail.types.setup_domain_name_list.SetupDomainNameList",
        certificate_provider: "capo_lightsail.types.certificate_provider.CertificateProvider",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.setup_instance_https_result.SetupInstanceHttpsResult":
        """<p>Creates an SSL/TLS certificate that secures traffic for your website. After the certificate is created, it is installed on the specified Lightsail instance.</p> <p>If you provide more than one domain name in the request, at least one name must be less than or equal to 63 characters in length.</p>

        Args:
            instance_name: <p>The name of the Lightsail instance.</p>
            email_address: <p>The contact method for SSL/TLS certificate renewal alerts. You can enter one email address. </p>
            domain_names: <p>The name of the domain and subdomains that were specified for the SSL/TLS certificate.</p>
            certificate_provider: <p>The certificate authority that issues the SSL/TLS certificate.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.setup_instance_https_request.SetupInstanceHttpsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.setup_instance_https_result.SetupInstanceHttpsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.setup_instance_https

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.setup_instance_https.async_setup_instance_https(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.setup_instance_https_request.SetupInstanceHttpsRequest = {
            "instance_name": instance_name,
            "email_address": email_address,
            "domain_names": domain_names,
            "certificate_provider": certificate_provider,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_gui_session(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.start_gui_session_result.StartGUISessionResult":
        """<p>Initiates a graphical user interface (GUI) session that’s used to access a virtual computer’s operating system and application. The session will be active for 1 hour. Use this action to resume the session after it expires. </p>

        Args:
            resource_name: <p>The resource name.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.start_gui_session_request.StartGUISessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.start_gui_session_result.StartGUISessionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.start_gui_session

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.start_gui_session.async_start_gui_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.start_gui_session_request.StartGUISessionRequest = {
            "resource_name": resource_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_instance(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.start_instance_result.StartInstanceResult":
        """<p>Starts a specific Amazon Lightsail instance from a stopped state. To restart an instance, use the <code>reboot instance</code> operation.</p> <note> <p>When you start a stopped instance, Lightsail assigns a new public IP address to the instance. To use the same IP address after stopping and starting an instance, create a static IP address and attach it to the instance. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-create-static-ip">Amazon Lightsail Developer Guide</a>.</p> </note> <p>The <code>start instance</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>instance name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_name: <p>The name of the instance (a virtual private server) to start.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.start_instance_request.StartInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.start_instance_result.StartInstanceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.start_instance

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.start_instance.async_start_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.start_instance_request.StartInstanceRequest = {
            "instance_name": instance_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.start_relational_database_result.StartRelationalDatabaseResult":
        """<p>Starts a specific database from a stopped state in Amazon Lightsail. To restart a database, use the <code>reboot relational database</code> operation.</p> <p>The <code>start relational database</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of your database to start.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.start_relational_database_request.StartRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.start_relational_database_result.StartRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.start_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.start_relational_database.async_start_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.start_relational_database_request.StartRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_gui_session(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.stop_gui_session_result.StopGUISessionResult":
        """<p>Terminates a web-based Amazon DCV session that’s used to access a virtual computer’s operating system or application. The session will close and any unsaved data will be lost.</p>

        Args:
            resource_name: <p>The resource name.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.stop_gui_session_request.StopGUISessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.stop_gui_session_result.StopGUISessionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.stop_gui_session

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.stop_gui_session.async_stop_gui_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.stop_gui_session_request.StopGUISessionRequest = {
            "resource_name": resource_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_instance(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        force: Optional["capo_lightsail.types.boolean.boolean"] = None,
    ) -> "capo_lightsail.types.stop_instance_result.StopInstanceResult":
        """<p>Stops a specific Amazon Lightsail instance that is currently running.</p> <note> <p>When you start a stopped instance, Lightsail assigns a new public IP address to the instance. To use the same IP address after stopping and starting an instance, create a static IP address and attach it to the instance. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-create-static-ip">Amazon Lightsail Developer Guide</a>.</p> </note> <p>The <code>stop instance</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>instance name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            instance_name: <p>The name of the instance (a virtual private server) to stop.</p>
            force: <p>When set to <code>True</code>, forces a Lightsail instance that is stuck in a <code>stopping</code> state to stop.</p> <important> <p>Only use the <code>force</code> parameter if your instance is stuck in the <code>stopping</code> state. In any other state, your instance should stop normally without adding this parameter to your API request.</p> </important>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.stop_instance_request.StopInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.stop_instance_result.StopInstanceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.stop_instance

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.stop_instance.async_stop_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.stop_instance_request.StopInstanceRequest = {
            "instance_name": instance_name
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

    async def stop_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        relational_database_snapshot_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
    ) -> "capo_lightsail.types.stop_relational_database_result.StopRelationalDatabaseResult":
        """<p>Stops a specific database that is currently running in Amazon Lightsail.</p> <note> <p>If you don't manually start your database instance after it has been stopped for seven consecutive days, Amazon Lightsail automatically starts it for you. This action helps ensure that your database instance doesn't fall behind on any required maintenance updates.</p> </note> <p>The <code>stop relational database</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of your database to stop.</p>
            relational_database_snapshot_name: <p>The name of your new database snapshot to be created before stopping your database.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.stop_relational_database_request.StopRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.stop_relational_database_result.StopRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.stop_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.stop_relational_database.async_stop_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.stop_relational_database_request.StopRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name
        }
        if relational_database_snapshot_name is not None:
            input_["relational_database_snapshot_name"] = (
                relational_database_snapshot_name
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        tags: "capo_lightsail.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        resource_arn: Optional["capo_lightsail.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_lightsail.types.tag_resource_result.TagResourceResult":
        """<p>Adds one or more tags to the specified Amazon Lightsail resource. Each resource can have a maximum of 50 tags. Each tag consists of a key and an optional value. Tag keys must be unique per resource. For more information about tags, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags">Amazon Lightsail Developer Guide</a>.</p> <p>The <code>tag resource</code> operation supports tag-based access control via request tags and resource tags applied to the resource identified by <code>resource name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            resource_name: <p>The name of the resource to which you are adding tags.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to which you want to add a tag.</p>
            tags: <p>The tag key and optional value.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.tag_resource

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.tag_resource_request.TagResourceRequest = {
            "resource_name": resource_name,
            "tags": tags,
        }
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_alarm(
        self,
        alarm_name: "capo_lightsail.types.resource_name.ResourceName",
        state: "capo_lightsail.types.alarm_state.AlarmState",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.test_alarm_result.TestAlarmResult":
        """<p>Tests an alarm by displaying a banner on the Amazon Lightsail console. If a notification trigger is configured for the specified alarm, the test also sends a notification to the notification protocol (<code>Email</code> and/or <code>SMS</code>) configured for the alarm.</p> <p>An alarm is used to monitor a single metric for one of your resources. When a metric condition is met, the alarm can notify you by email, SMS text message, and a banner displayed on the Amazon Lightsail console. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-alarms">Alarms in Amazon Lightsail</a>.</p>

        Args:
            alarm_name: <p>The name of the alarm to test.</p>
            state: <p>The alarm state to test.</p> <p>An alarm has the following possible states that can be tested:</p> <ul> <li> <p> <code>ALARM</code> - The metric is outside of the defined threshold.</p> </li> <li> <p> <code>INSUFFICIENT_DATA</code> - The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.</p> </li> <li> <p> <code>OK</code> - The metric is within the defined threshold.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.test_alarm_request.TestAlarmRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.test_alarm_result.TestAlarmResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.test_alarm

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.test_alarm.async_test_alarm(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.test_alarm_request.TestAlarmRequest = {
            "alarm_name": alarm_name,
            "state": state,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unpeer_vpc(
        self, *, config_overrides: Optional[AsyncLightsailClientConfig] = None
    ) -> "capo_lightsail.types.unpeer_vpc_result.UnpeerVpcResult":
        """<p>Unpeers the Lightsail VPC from the user's default VPC.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.unpeer_vpc_request.UnpeerVpcRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.unpeer_vpc_result.UnpeerVpcResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.unpeer_vpc

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.unpeer_vpc.async_unpeer_vpc(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.unpeer_vpc_request.UnpeerVpcRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_name: "capo_lightsail.types.resource_name.ResourceName",
        tag_keys: "capo_lightsail.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        resource_arn: Optional["capo_lightsail.types.resource_arn.ResourceArn"] = None,
    ) -> "capo_lightsail.types.untag_resource_result.UntagResourceResult":
        """<p>Deletes the specified set of tag keys and their values from the specified Amazon Lightsail resource.</p> <p>The <code>untag resource</code> operation supports tag-based access control via request tags and resource tags applied to the resource identified by <code>resource name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            resource_name: <p>The name of the resource from which you are removing a tag.</p>
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which you want to remove a tag.</p>
            tag_keys: <p>The tag keys to delete from the specified resource.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.untag_resource

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.untag_resource_request.UntagResourceRequest = {
            "resource_name": resource_name,
            "tag_keys": tag_keys,
        }
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bucket(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        access_rules: Optional["capo_lightsail.types.access_rules.AccessRules"] = None,
        versioning: Optional[
            "capo_lightsail.types.non_empty_string.NonEmptyString"
        ] = None,
        readonly_access_accounts: Optional[
            "capo_lightsail.types.partner_id_list.PartnerIdList"
        ] = None,
        access_log_config: Optional[
            "capo_lightsail.types.bucket_access_log_config.BucketAccessLogConfig"
        ] = None,
        cors: Optional[
            "capo_lightsail.types.bucket_cors_config.BucketCorsConfig"
        ] = None,
    ) -> "capo_lightsail.types.update_bucket_result.UpdateBucketResult":
        """<p>Updates an existing Amazon Lightsail bucket.</p> <p>Use this action to update the configuration of an existing bucket, such as versioning, public accessibility, and the Amazon Web Services accounts that can access the bucket.</p>

        Args:
            bucket_name: <p>The name of the bucket to update.</p>
            access_rules: <p>An object that sets the public accessibility of objects in the specified bucket.</p>
            versioning: <p>Specifies whether to enable or suspend versioning of objects in the bucket.</p> <p>The following options can be specified:</p> <ul> <li> <p> <code>Enabled</code> - Enables versioning of objects in the specified bucket.</p> </li> <li> <p> <code>Suspended</code> - Suspends versioning of objects in the specified bucket. Existing object versions are retained.</p> </li> </ul>
            readonly_access_accounts: <p>An array of strings to specify the Amazon Web Services account IDs that can access the bucket.</p> <p>You can give a maximum of 10 Amazon Web Services accounts access to a bucket.</p>
            access_log_config: <p>An object that describes the access log configuration for the bucket.</p>
            cors: <p>Sets the cross-origin resource sharing (CORS) configuration for your bucket. If a CORS configuration exists, it is replaced with the specified configuration. For AWS CLI operations, this parameter can also be passed as a file. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html">Configuring cross-origin resource sharing (CORS)</a>.</p> <note> <p>CORS information is only returned in a response when you update the CORS policy.</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_bucket_request.UpdateBucketRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_bucket_result.UpdateBucketResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_bucket

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_bucket.async_update_bucket(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_bucket_request.UpdateBucketRequest = {
            "bucket_name": bucket_name
        }
        if access_rules is not None:
            input_["access_rules"] = access_rules
        if versioning is not None:
            input_["versioning"] = versioning
        if readonly_access_accounts is not None:
            input_["readonly_access_accounts"] = readonly_access_accounts
        if access_log_config is not None:
            input_["access_log_config"] = access_log_config
        if cors is not None:
            input_["cors"] = cors

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bucket_bundle(
        self,
        bucket_name: "capo_lightsail.types.bucket_name.BucketName",
        bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.update_bucket_bundle_result.UpdateBucketBundleResult":
        """<p>Updates the bundle, or storage plan, of an existing Amazon Lightsail bucket.</p> <p>A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket. You can update a bucket's bundle only one time within a monthly Amazon Web Services billing cycle. To determine if you can update a bucket's bundle, use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBuckets.html">GetBuckets</a> action. The <code>ableToUpdateBundle</code> parameter in the response will indicate whether you can currently update a bucket's bundle.</p> <p>Update a bucket's bundle if it's consistently going over its storage space or data transfer quota, or if a bucket's usage is consistently in the lower range of its storage space or data transfer quota. Due to the unpredictable usage fluctuations that a bucket might experience, we strongly recommend that you update a bucket's bundle only as a long-term strategy, instead of as a short-term, monthly cost-cutting measure. Choose a bucket bundle that will provide the bucket with ample storage space and data transfer for a long time to come.</p>

        Args:
            bucket_name: <p>The name of the bucket for which to update the bundle.</p>
            bundle_id: <p>The ID of the new bundle to apply to the bucket.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html">GetBucketBundles</a> action to get a list of bundle IDs that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_bucket_bundle_request.UpdateBucketBundleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_bucket_bundle_result.UpdateBucketBundleResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_bucket_bundle

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_bucket_bundle.async_update_bucket_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_bucket_bundle_request.UpdateBucketBundleRequest = {
            "bucket_name": bucket_name,
            "bundle_id": bundle_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_container_service(
        self,
        service_name: "capo_lightsail.types.container_service_name.ContainerServiceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        power: Optional[
            "capo_lightsail.types.container_service_power_name.ContainerServicePowerName"
        ] = None,
        scale: Optional[
            "capo_lightsail.types.container_service_scale.ContainerServiceScale"
        ] = None,
        is_disabled: Optional["capo_lightsail.types.boolean.boolean"] = None,
        public_domain_names: Optional[
            "capo_lightsail.types.container_service_public_domains.ContainerServicePublicDomains"
        ] = None,
        private_registry_access: Optional[
            "capo_lightsail.types.private_registry_access_request.PrivateRegistryAccessRequest"
        ] = None,
    ) -> "capo_lightsail.types.update_container_service_result.UpdateContainerServiceResult":
        """<p>Updates the configuration of your Amazon Lightsail container service, such as its power, scale, and public domain names.</p>

        Args:
            service_name: <p>The name of the container service to update.</p>
            power: <p>The power for the container service.</p> <p>The power specifies the amount of memory, vCPUs, and base monthly cost of each node of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p> <p>Use the <code>GetContainerServicePowers</code> action to view the specifications of each power option.</p>
            scale: <p>The scale for the container service.</p> <p>The scale specifies the allocated compute nodes of the container service. The <code>power</code> and <code>scale</code> of a container service makes up its configured capacity. To determine the monthly price of your container service, multiply the base price of the <code>power</code> with the <code>scale</code> (the number of nodes) of the service.</p>
            is_disabled: <p>A Boolean value to indicate whether the container service is disabled.</p>
            public_domain_names: <p>The public domain names to use with the container service, such as <code>example.com</code> and <code>www.example.com</code>.</p> <p>You can specify up to four public domain names for a container service. The domain names that you specify are used when you create a deployment with a container configured as the public endpoint of your container service.</p> <p>If you don't specify public domain names, then you can use the default domain of the container service.</p> <important> <p>You must create and validate an SSL/TLS certificate before you can use public domain names with your container service. Use the <code>CreateCertificate</code> action to create a certificate for the public domain names you want to use with your container service.</p> </important> <p>You can specify public domain names using a string to array map as shown in the example later on this page.</p>
            private_registry_access: <p>An object to describe the configuration for the container service to access private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-container-service-ecr-private-repo-access">Configuring access to an Amazon ECR private repository for an Amazon Lightsail container service</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_container_service_request.UpdateContainerServiceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_container_service_result.UpdateContainerServiceResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_container_service

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_container_service.async_update_container_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_container_service_request.UpdateContainerServiceRequest = {
            "service_name": service_name
        }
        if power is not None:
            input_["power"] = power
        if scale is not None:
            input_["scale"] = scale
        if is_disabled is not None:
            input_["is_disabled"] = is_disabled
        if public_domain_names is not None:
            input_["public_domain_names"] = public_domain_names
        if private_registry_access is not None:
            input_["private_registry_access"] = private_registry_access

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_distribution(
        self,
        distribution_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        origin: Optional["capo_lightsail.types.input_origin.InputOrigin"] = None,
        default_cache_behavior: Optional[
            "capo_lightsail.types.cache_behavior.CacheBehavior"
        ] = None,
        cache_behavior_settings: Optional[
            "capo_lightsail.types.cache_settings.CacheSettings"
        ] = None,
        cache_behaviors: Optional[
            "capo_lightsail.types.cache_behavior_list.CacheBehaviorList"
        ] = None,
        is_enabled: Optional["capo_lightsail.types.boolean.boolean"] = None,
        viewer_minimum_tls_protocol_version: Optional[
            "capo_lightsail.types.viewer_minimum_tls_protocol_version_enum.ViewerMinimumTlsProtocolVersionEnum"
        ] = None,
        certificate_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        use_default_certificate: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        enable_private_origin_access: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        default_root_object: Optional["capo_lightsail.types.string.string"] = None,
        custom_error_responses: Optional[
            "capo_lightsail.types.distribution_custom_error_response_list.DistributionCustomErrorResponseList"
        ] = None,
    ) -> "capo_lightsail.types.update_distribution_result.UpdateDistributionResult":
        """<p>Updates an existing Amazon Lightsail content delivery network (CDN) distribution.</p> <p>Use this action to update the configuration of your existing distribution.</p>

        Args:
            distribution_name: <p>The name of the distribution to update.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>
            origin: <p>An object that describes the origin resource for the distribution, such as a Lightsail instance, bucket, or load balancer.</p> <p>The distribution pulls, caches, and serves content from the origin.</p>
            default_cache_behavior: <p>An object that describes the default cache behavior for the distribution.</p>
            cache_behavior_settings: <p>An object that describes the cache behavior settings for the distribution.</p> <note> <p>The <code>cacheBehaviorSettings</code> specified in your <code>UpdateDistributionRequest</code> will replace your distribution's existing settings.</p> </note>
            cache_behaviors: <p>An array of objects that describe the per-path cache behavior for the distribution.</p>
            is_enabled: <p>Indicates whether to enable the distribution.</p>
            viewer_minimum_tls_protocol_version: <p>Use this parameter to update the minimum TLS protocol version for the SSL/TLS certificate that's attached to the distribution.</p>
            certificate_name: <p>The name of the SSL/TLS certificate that you want to attach to the distribution.</p> <p>Only certificates with a status of <code>ISSUED</code> can be attached to a distribution.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetCertificates.html">GetCertificates</a> action to get a list of certificate names that you can specify.</p>
            use_default_certificate: <p>Indicates whether the default SSL/TLS certificate is attached to the distribution. The default value is <code>true</code>. When <code>true</code>, the distribution uses the default domain name such as <code>d111111abcdef8.cloudfront.net</code>.</p> <p> Set this value to <code>false</code> to attach a new certificate to the distribution.</p>
            enable_private_origin_access: <p>Specifies whether to enable private origin access for the distribution. With private origin access, the distribution can serve objects that aren't publicly accessible from a Lightsail bucket.</p> <p>Lightsail grants the distribution permission to read the bucket's objects. Enabling private origin access doesn't change the bucket's access settings, and you can still retrieve publicly accessible objects directly from the bucket's endpoint.</p> <note> <p>When you include this parameter, you must also include the <code>origin</code> parameter with the resource name, even if the origin is not changing.</p> <p>You can enable private origin access only when the distribution's origin is a Lightsail bucket. If the origin is another resource type, the request fails.</p> </note>
            default_root_object: <p>The object (for example, <code>index.html</code>) that the distribution returns when a viewer requests the root URL of the distribution (<code>/</code>) instead of a specific object. The object that you specify must be available from the origin.</p>
            custom_error_responses: <p>An array of objects that describe the custom error responses for the distribution. With a custom error response, you can specify the page to return when the origin responds with a given HTTP error code. You can also specify the HTTP status code to send to the viewer.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_distribution_request.UpdateDistributionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_distribution_result.UpdateDistributionResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_distribution

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_distribution.async_update_distribution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_distribution_request.UpdateDistributionRequest = {
            "distribution_name": distribution_name
        }
        if origin is not None:
            input_["origin"] = origin
        if default_cache_behavior is not None:
            input_["default_cache_behavior"] = default_cache_behavior
        if cache_behavior_settings is not None:
            input_["cache_behavior_settings"] = cache_behavior_settings
        if cache_behaviors is not None:
            input_["cache_behaviors"] = cache_behaviors
        if is_enabled is not None:
            input_["is_enabled"] = is_enabled
        if viewer_minimum_tls_protocol_version is not None:
            input_["viewer_minimum_tls_protocol_version"] = (
                viewer_minimum_tls_protocol_version
            )
        if certificate_name is not None:
            input_["certificate_name"] = certificate_name
        if use_default_certificate is not None:
            input_["use_default_certificate"] = use_default_certificate
        if enable_private_origin_access is not None:
            input_["enable_private_origin_access"] = enable_private_origin_access
        if default_root_object is not None:
            input_["default_root_object"] = default_root_object
        if custom_error_responses is not None:
            input_["custom_error_responses"] = custom_error_responses

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_distribution_bundle(
        self,
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        distribution_name: Optional[
            "capo_lightsail.types.resource_name.ResourceName"
        ] = None,
        bundle_id: Optional["capo_lightsail.types.string.string"] = None,
    ) -> "capo_lightsail.types.update_distribution_bundle_result.UpdateDistributionBundleResult":
        """<p>Updates the bundle of your Amazon Lightsail content delivery network (CDN) distribution.</p> <p>A distribution bundle specifies the monthly network transfer quota and monthly cost of your distribution.</p> <p>Update your distribution's bundle if your distribution is going over its monthly network transfer quota and is incurring an overage fee.</p> <p>You can update your distribution's bundle only one time within your monthly Amazon Web Services billing cycle. To determine if you can update your distribution's bundle, use the <code>GetDistributions</code> action. The <code>ableToUpdateBundle</code> parameter in the result will indicate whether you can currently update your distribution's bundle.</p>

        Args:
            distribution_name: <p>The name of the distribution for which to update the bundle.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>
            bundle_id: <p>The bundle ID of the new bundle to apply to your distribution.</p> <p>Use the <code>GetDistributionBundles</code> action to get a list of distribution bundle IDs that you can specify.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_distribution_bundle_request.UpdateDistributionBundleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_distribution_bundle_result.UpdateDistributionBundleResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_distribution_bundle

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_distribution_bundle.async_update_distribution_bundle(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_distribution_bundle_request.UpdateDistributionBundleRequest = {}
        if distribution_name is not None:
            input_["distribution_name"] = distribution_name
        if bundle_id is not None:
            input_["bundle_id"] = bundle_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_entry(
        self,
        domain_name: "capo_lightsail.types.domain_name.DomainName",
        domain_entry: "capo_lightsail.types.domain_entry.DomainEntry",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.update_domain_entry_result.UpdateDomainEntryResult":
        """<p>Updates a domain recordset after it is created.</p> <p>The <code>update domain entry</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>domain name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            domain_name: <p>The name of the domain recordset to update.</p>
            domain_entry: <p>An array of key-value pairs containing information about the domain entry.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_domain_entry_request.UpdateDomainEntryRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_domain_entry_result.UpdateDomainEntryResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_domain_entry

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_domain_entry.async_update_domain_entry(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_domain_entry_request.UpdateDomainEntryRequest = {
            "domain_name": domain_name,
            "domain_entry": domain_entry,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_instance_metadata_options(
        self,
        instance_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        http_tokens: Optional["capo_lightsail.types.http_tokens.HttpTokens"] = None,
        http_endpoint: Optional[
            "capo_lightsail.types.http_endpoint.HttpEndpoint"
        ] = None,
        http_put_response_hop_limit: Optional[
            "capo_lightsail.types.integer.integer"
        ] = None,
        http_protocol_ipv6: Optional[
            "capo_lightsail.types.http_protocol_ipv6.HttpProtocolIpv6"
        ] = None,
    ) -> "capo_lightsail.types.update_instance_metadata_options_result.UpdateInstanceMetadataOptionsResult":
        """<p>Modifies the Amazon Lightsail instance metadata parameters on a running or stopped instance. When you modify the parameters on a running instance, the <code>GetInstance</code> or <code>GetInstances</code> API operation initially responds with a state of <code>pending</code>. After the parameter modifications are successfully applied, the state changes to <code>applied</code> in subsequent <code>GetInstance</code> or <code>GetInstances</code> API calls. For more information, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-instance-metadata-service">Use IMDSv2 with an Amazon Lightsail instance</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>

        Args:
            instance_name: <p>The name of the instance for which to update metadata parameters.</p>
            http_tokens: <p>The state of token usage for your instance metadata requests. If the parameter is not specified in the request, the default state is <code>optional</code>.</p> <p>If the state is <code>optional</code>, you can choose whether to retrieve instance metadata with a signed token header on your request. If you retrieve the IAM role credentials without a token, the version 1.0 role credentials are returned. If you retrieve the IAM role credentials by using a valid signed token, the version 2.0 role credentials are returned.</p> <p>If the state is <code>required</code>, you must send a signed token header with all instance metadata retrieval requests. In this state, retrieving the IAM role credential always returns the version 2.0 credentials. The version 1.0 credentials are not available.</p>
            http_endpoint: <p>Enables or disables the HTTP metadata endpoint on your instances. If this parameter is not specified, the existing state is maintained.</p> <p>If you specify a value of <code>disabled</code>, you cannot access your instance metadata.</p>
            http_put_response_hop_limit: <p>The desired HTTP PUT response hop limit for instance metadata requests. A larger number means that the instance metadata requests can travel farther. If no parameter is specified, the existing state is maintained.</p>
            http_protocol_ipv6: <p>Enables or disables the IPv6 endpoint for the instance metadata service. This setting applies only when the HTTP metadata endpoint is enabled.</p> <note> <p>This parameter is available only for instances in the Europe (Stockholm) Amazon Web Services Region (<code>eu-north-1</code>).</p> </note>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_instance_metadata_options_request.UpdateInstanceMetadataOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_instance_metadata_options_result.UpdateInstanceMetadataOptionsResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_instance_metadata_options

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_instance_metadata_options.async_update_instance_metadata_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_instance_metadata_options_request.UpdateInstanceMetadataOptionsRequest = {
            "instance_name": instance_name
        }
        if http_tokens is not None:
            input_["http_tokens"] = http_tokens
        if http_endpoint is not None:
            input_["http_endpoint"] = http_endpoint
        if http_put_response_hop_limit is not None:
            input_["http_put_response_hop_limit"] = http_put_response_hop_limit
        if http_protocol_ipv6 is not None:
            input_["http_protocol_ipv6"] = http_protocol_ipv6

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_load_balancer_attribute(
        self,
        load_balancer_name: "capo_lightsail.types.resource_name.ResourceName",
        attribute_name: "capo_lightsail.types.load_balancer_attribute_name.LoadBalancerAttributeName",
        attribute_value: "capo_lightsail.types.string_max256.StringMax256",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.update_load_balancer_attribute_result.UpdateLoadBalancerAttributeResult":
        """<p>Updates the specified attribute for a load balancer. You can only update one attribute at a time.</p> <p>The <code>update load balancer attribute</code> operation supports tag-based access control via resource tags applied to the resource identified by <code>load balancer name</code>. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            load_balancer_name: <p>The name of the load balancer that you want to modify (<code>my-load-balancer</code>.</p>
            attribute_name: <p>The name of the attribute you want to update.</p>
            attribute_value: <p>The value that you want to specify for the attribute name.</p> <p>The following values are supported depending on what you specify for the <code>attributeName</code> request parameter:</p> <ul> <li> <p>If you specify <code>HealthCheckPath</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be the path to ping on the target (for example, <code>/weather/us/wa/seattle</code>).</p> </li> <li> <p>If you specify <code>SessionStickinessEnabled</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be <code>true</code> to activate session stickiness or <code>false</code> to deactivate session stickiness.</p> </li> <li> <p>If you specify <code>SessionStickiness_LB_CookieDurationSeconds</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be an interger that represents the cookie duration in seconds.</p> </li> <li> <p>If you specify <code>HttpsRedirectionEnabled</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be <code>true</code> to activate HTTP to HTTPS redirection or <code>false</code> to deactivate HTTP to HTTPS redirection.</p> </li> <li> <p>If you specify <code>TlsPolicyName</code> for the <code>attributeName</code> request parameter, then the <code>attributeValue</code> request parameter must be the name of the TLS policy.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetLoadBalancerTlsPolicies.html">GetLoadBalancerTlsPolicies</a> action to get a list of TLS policy names that you can specify.</p> </li> </ul>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_load_balancer_attribute_request.UpdateLoadBalancerAttributeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_load_balancer_attribute_result.UpdateLoadBalancerAttributeResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_load_balancer_attribute

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_load_balancer_attribute.async_update_load_balancer_attribute(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_load_balancer_attribute_request.UpdateLoadBalancerAttributeRequest = {
            "load_balancer_name": load_balancer_name,
            "attribute_name": attribute_name,
            "attribute_value": attribute_value,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_relational_database(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
        master_user_password: Optional[
            "capo_lightsail.types.sensitive_string.SensitiveString"
        ] = None,
        rotate_master_user_password: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        preferred_backup_window: Optional["capo_lightsail.types.string.string"] = None,
        preferred_maintenance_window: Optional[
            "capo_lightsail.types.string.string"
        ] = None,
        enable_backup_retention: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        disable_backup_retention: Optional[
            "capo_lightsail.types.boolean.boolean"
        ] = None,
        publicly_accessible: Optional["capo_lightsail.types.boolean.boolean"] = None,
        apply_immediately: Optional["capo_lightsail.types.boolean.boolean"] = None,
        ca_certificate_identifier: Optional[
            "capo_lightsail.types.string.string"
        ] = None,
        relational_database_blueprint_id: Optional[
            "capo_lightsail.types.string.string"
        ] = None,
    ) -> "capo_lightsail.types.update_relational_database_result.UpdateRelationalDatabaseResult":
        """<p>Allows the update of one or more attributes of a database in Amazon Lightsail.</p> <p>Updates are applied immediately, or in cases where the updates could result in an outage, are applied during the database's predefined maintenance window.</p> <p>The <code>update relational database</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags\">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of your Lightsail database resource to update.</p>
            master_user_password: <p>The password for the master user. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\".</p> <p>My<b>SQL</b> </p> <p>Constraints: Must contain from 8 to 41 characters.</p> <p> <b>PostgreSQL</b> </p> <p>Constraints: Must contain from 8 to 128 characters.</p>
            rotate_master_user_password: <p>When <code>true</code>, the master user password is changed to a new strong password generated by Lightsail.</p> <p>Use the <code>get relational database master user password</code> operation to get the new password.</p>
            preferred_backup_window: <p>The daily time range during which automated backups are created for your database if automated backups are enabled.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the <code>hh24:mi-hh24:mi</code> format.</p> <p>Example: <code>16:00-16:30</code> </p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur on your database.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each Amazon Web Services Region, occurring on a random day of the week.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the <code>ddd:hh24:mi-ddd:hh24:mi</code> format.</p> </li> <li> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Example: <code>Tue:17:00-Tue:17:30</code> </p> </li> </ul>
            enable_backup_retention: <p>When <code>true</code>, enables automated backup retention for your database.</p> <p>Updates are applied during the next maintenance window because this can result in an outage.</p>
            disable_backup_retention: <p>When <code>true</code>, disables automated backup retention for your database.</p> <p>Disabling backup retention deletes all automated database backups. Before disabling this, you may want to create a snapshot of your database using the <code>create relational database snapshot</code> operation.</p> <p>Updates are applied during the next maintenance window because this can result in an outage.</p>
            publicly_accessible: <p>Specifies the accessibility options for your database. A value of <code>true</code> specifies a database that is available to resources outside of your Lightsail account. A value of <code>false</code> specifies a database that is available only to your Lightsail resources in the same region as your database.</p>
            apply_immediately: <p>When <code>true</code>, applies changes immediately. When <code>false</code>, applies changes during the preferred maintenance window. Some changes may cause an outage.</p> <p>Default: <code>false</code> </p>
            ca_certificate_identifier: <p>Indicates the certificate that needs to be associated with the database.</p>
            relational_database_blueprint_id: <p>This parameter is used to update the major version of the database. Enter the <code>blueprintId</code> for the major version that you want to update to.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRelationalDatabaseBlueprints.html\">GetRelationalDatabaseBlueprints</a> action to get a list of available blueprint IDs.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_relational_database_request.UpdateRelationalDatabaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_relational_database_result.UpdateRelationalDatabaseResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_relational_database

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_relational_database.async_update_relational_database(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_relational_database_request.UpdateRelationalDatabaseRequest = {
            "relational_database_name": relational_database_name
        }
        if master_user_password is not None:
            input_["master_user_password"] = master_user_password
        if rotate_master_user_password is not None:
            input_["rotate_master_user_password"] = rotate_master_user_password
        if preferred_backup_window is not None:
            input_["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if enable_backup_retention is not None:
            input_["enable_backup_retention"] = enable_backup_retention
        if disable_backup_retention is not None:
            input_["disable_backup_retention"] = disable_backup_retention
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if ca_certificate_identifier is not None:
            input_["ca_certificate_identifier"] = ca_certificate_identifier
        if relational_database_blueprint_id is not None:
            input_["relational_database_blueprint_id"] = (
                relational_database_blueprint_id
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_relational_database_parameters(
        self,
        relational_database_name: "capo_lightsail.types.resource_name.ResourceName",
        parameters: "capo_lightsail.types.relational_database_parameter_list.RelationalDatabaseParameterList",
        *,
        config_overrides: Optional[AsyncLightsailClientConfig] = None,
    ) -> "capo_lightsail.types.update_relational_database_parameters_result.UpdateRelationalDatabaseParametersResult":
        """<p>Allows the update of one or more parameters of a database in Amazon Lightsail.</p> <p>Parameter updates don't cause outages; therefore, their application is not subject to the preferred maintenance window. However, there are two ways in which parameter updates are applied: <code>dynamic</code> or <code>pending-reboot</code>. Parameters marked with a <code>dynamic</code> apply type are applied immediately. Parameters marked with a <code>pending-reboot</code> apply type are applied only after the database is rebooted using the <code>reboot relational database</code> operation.</p> <p>The <code>update relational database parameters</code> operation supports tag-based access control via resource tags applied to the resource identified by relationalDatabaseName. For more information, see the <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags">Amazon Lightsail Developer Guide</a>.</p>

        Args:
            relational_database_name: <p>The name of your database for which to update parameters.</p>
            parameters: <p>The database parameters to update.</p>

        Raises:
            capo_lightsail.errors.access_denied_exception.AccessDeniedException: <p>Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.</p>
            capo_lightsail.errors.account_setup_in_progress_exception.AccountSetupInProgressException: <p>Lightsail throws this exception when an account is still in the setup in progress state.</p>
            capo_lightsail.errors.invalid_input_exception.InvalidInputException: <p>Lightsail throws this exception when user input does not conform to the validation rules of an input field.</p> <note> <p>Domain and distribution APIs are only available in the N. Virginia (<code>us-east-1</code>) Amazon Web Services Region. Please set your Amazon Web Services Region configuration to <code>us-east-1</code> to create, view, or edit these resources.</p> </note>
            capo_lightsail.errors.not_found_exception.NotFoundException: <p>Lightsail throws this exception when it cannot find a resource.</p>
            capo_lightsail.errors.operation_failure_exception.OperationFailureException: <p>Lightsail throws this exception when an operation fails to execute.</p>
            capo_lightsail.errors.region_setup_in_progress_exception.RegionSetupInProgressException: <p>Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.</p>
            capo_lightsail.errors.service_exception.ServiceException: <p>A general service exception.</p>
            capo_lightsail.errors.unauthenticated_exception.UnauthenticatedException: <p>Lightsail throws this exception when the user has not been authenticated.</p>
            capo_lightsail.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lightsail.types.update_relational_database_parameters_request.UpdateRelationalDatabaseParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_lightsail.types.update_relational_database_parameters_result.UpdateRelationalDatabaseParametersResult"
        ]:
            import capo_lightsail._operations.lightsail_20161128.update_relational_database_parameters

            (
                output,
                http_response,
            ) = await capo_lightsail._operations.lightsail_20161128.update_relational_database_parameters.async_update_relational_database_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lightsail.types.update_relational_database_parameters_request.UpdateRelationalDatabaseParametersRequest = {
            "relational_database_name": relational_database_name,
            "parameters": parameters,
        }

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
